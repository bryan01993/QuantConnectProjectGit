"""
qc_batch_poller.py
==================
Serverless ingestor and poller for chunked QuantConnect backtests.

Functionality:
- Queries BigQuery table `BTOPBatchChunks` for active/pending chunks.
- Checks QuantConnect REST API (`/api/v2/backtests/list` or `/api/v2/backtests/read`) for backtest completion.
- When finished:
    1. Downloads backtest results JSON and orders JSON.
    2. Writes statistics into `BTOPResults` and performance tables.
    3. Streams trade records into `BTOPTrades`, tagging rows with `batch_id` and `chunk_index`.
    4. Updates `BTOPBatchChunks` status to 'COMPLETED'.
- Ideal for GCP Cloud Functions, Cloud Scheduler (every 5 mins), or lightweight cron tasks (takes ~5s per check).

Usage:
    poetry run python Scripts/BigQuery/qc_batch_poller.py
"""

from __future__ import annotations

import json
import logging
import os
import sys
import datetime as dt
from typing import Any, Dict, List
import requests

# Ensure script directory and project root are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
for d in [_THIS_DIR, _PROJECT_ROOT]:
    if d not in sys.path:
        sys.path.insert(0, d)

from batch_manager import (  # noqa: E402
    get_bigquery_client,
    get_pending_batch_chunks,
    update_chunk_status,
)
from bt_synchronization import generate_api_token, load_user_config  # noqa: E402
from bt_handler import download_backtest_results, download_backtest_orders, download_backtest_logs, write_results_to_database, get_api_key, get_project_id  # noqa: E402
from log_trades_uploader import upload_trade_records, parse_log_file, parse_orders_json_file, get_existing_records, PROJECT_ID, DATASET_ID, TABLE_NAME  # noqa: E402
from db_operator import build_symbol_struct, load_orders  # noqa: E402


logging.basicConfig(level=logging.INFO)


def poll_and_ingest_chunks() -> None:
    bq_client = get_bigquery_client()
    pending_chunks = get_pending_batch_chunks(bq_client)

    if not pending_chunks:
        logging.info("[Batch Poller] No pending or running batch chunks found in BTOPBatchChunks.")
        return

    logging.info(f"[Batch Poller] Found {len(pending_chunks)} active batch chunks to check.")

    # Resolve QC API credentials
    api_key, user_id = get_api_key()
    api_token = generate_api_token(api_key, user_id)
    defaults = load_user_config()
    project_id = int(defaults.get("PROJECT_ID", 22447448))

    # Fetch all backtests from QC Cloud to build a name/id resolution map
    url_list = "https://www.quantconnect.com/api/v2/backtests/list"
    headers = {
        "Authorization": f"Basic {api_token['api_token']}",
        "Timestamp": api_token["timestamp"],
    }
    
    # Try 4EVC project ID first (22447448) if defaults is set to generic project
    search_project_ids = [22447448] if project_id != 22447448 else [project_id]
    if project_id not in search_project_ids:
        search_project_ids.append(project_id)

    name_to_bt_map: Dict[str, Dict[str, Any]] = {}
    id_to_bt_map: Dict[str, Dict[str, Any]] = {}

    for pid in search_project_ids:
        try:
            resp_list = requests.post(url_list, headers=headers, json={"projectId": pid}, timeout=30)
            if resp_list.status_code == 200:
                for bt_item in resp_list.json().get("backtests", []):
                    bt_item["_projectId"] = pid
                    bt_hex_id = bt_item.get("backtestId") or bt_item.get("id")
                    bt_name_str = bt_item.get("name")
                    if bt_hex_id:
                        id_to_bt_map[bt_hex_id] = bt_item
                    if bt_name_str:
                        name_to_bt_map[bt_name_str] = bt_item
        except Exception as e:
            logging.warning(f"[Batch Poller] Could not list backtests for project {pid}: {e}")

    for chunk in pending_chunks:
        batch_id = chunk["batch_id"]
        bt_id_or_name = chunk["backtest_id"]
        chunk_idx = chunk["chunk_index"]

        logging.info(f"[Batch Poller] Checking chunk ({batch_id}, {bt_id_or_name}, Chunk #{chunk_idx})...")

        try:
            # Resolve real 32-char hex backtest ID and project ID
            matched_bt = name_to_bt_map.get(bt_id_or_name) or id_to_bt_map.get(bt_id_or_name)
            if matched_bt:
                real_backtest_id = matched_bt.get("backtestId") or matched_bt.get("id") or bt_id_or_name
                chunk_project_id = matched_bt.get("_projectId", project_id)
                completed = matched_bt.get("completed", False)
                progress = matched_bt.get("progress", 0.0)
            else:
                real_backtest_id = bt_id_or_name
                chunk_project_id = project_id
                
                # Fallback to direct read
                url_read = "https://www.quantconnect.com/api/v2/backtests/read"
                payload = {"projectId": int(chunk_project_id), "backtestId": real_backtest_id}
                resp = requests.post(url_read, headers=headers, json=payload, timeout=30)
                if resp.status_code != 200:
                    logging.warning(f"[Batch Poller] Could not read status for {bt_id_or_name} (HTTP {resp.status_code}). Will retry next cycle.")
                    continue
                bt_data = resp.json().get("backtest", {})
                completed = bt_data.get("completed", False)
                progress = bt_data.get("progress", 0.0)

            if not completed and progress < 1.0:
                logging.info(f"[Batch Poller] Chunk {bt_id_or_name} is still running on QC Cloud (Progress: {progress*100:.1f}%).")
                continue

            logging.info(f"[Batch Poller] Chunk {bt_id_or_name} ({real_backtest_id}) is COMPLETED! Downloading results, orders, and logs...")

            # 1. Download results JSON and store summary tables
            results_path, response_data = download_backtest_results(real_backtest_id, api_token, int(chunk_project_id))
            if results_path:
                write_results_to_database(results_path, real_backtest_id)

            # 2. Download orders JSON and ingest into BTOPOrders
            orders_path, orders = download_backtest_orders(real_backtest_id, api_token, int(chunk_project_id))
            try:
                load_orders({"orders": orders}, bq_client, "develop", real_backtest_id)
                logging.info(f"[Batch Poller] Ingested orders/placeholder into BTOPOrders for backtest ID: {real_backtest_id}")
            except Exception as ord_err:
                logging.error(f"[Batch Poller] Failed to ingest BTOPOrders for {real_backtest_id}: {ord_err}")

            # 3. Parse trade records directly from orders JSON / closedTrades JSON (dismissing log.txt)
            parsed_rows = []
            if orders_path and os.path.exists(orders_path):
                parsed_rows = parse_orders_json_file(orders_path)

            # Fallback: Parse closedTrades directly from results if parsed_rows is empty
            if not parsed_rows and response_data:
                bt_info = response_data.get("backtest", {}) if isinstance(response_data, dict) else {}
                total_perf = bt_info.get("totalPerformance", {}) or {}
                closed_trades = total_perf.get("closedTrades", []) if isinstance(total_perf, dict) else []
                now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
                bt_name = bt_info.get("name", real_backtest_id)

                for idx, ct in enumerate(closed_trades):
                    ct_id = str(ct.get("id") or f"{real_backtest_id}_ct_{idx}")
                    sym_struct = build_symbol_struct(ct)
                    und_ticker = sym_struct.get("underlying", {}).get("value") if (sym_struct and sym_struct.get("underlying")) else "UNKNOWN"
                    if not und_ticker or und_ticker == "UNKNOWN":
                        sym_val = ct.get("symbols", [{}])[0].get("value", "") if ct.get("symbols") else ""
                        und_ticker = sym_val.split()[0] if sym_val else "UNKNOWN"

                    entry_p = float(ct.get("entryPrice") or 0.0)
                    exit_p = float(ct.get("exitPrice") or 0.0)
                    qty = abs(float(ct.get("quantity") or 0.0))
                    pnl_val = float(ct.get("profitLoss") or 0.0)
                    # Option contract capital = entry_p * qty * 100
                    denom = entry_p * qty * 100.0
                    pnl_pct = round(pnl_val / denom, 5) if denom > 0 else (round((exit_p - entry_p) / entry_p, 5) if entry_p > 0 else 0.0)

                    parsed_rows.append({
                        "pk": f"CLOUD_{real_backtest_id}_{ct_id}_OPEN",
                        "backtestId": real_backtest_id,
                        "algo_code": "4EVC",
                        "timestamp": str(ct.get("entryTime")) if ct.get("entryTime") else now_ts,
                        "underlying": und_ticker[:32],
                        "action": "OPEN",
                        "qty": int(qty),
                        "entry_price": entry_p,
                        "exit_price": 0.0,
                        "pnl": 0.0,
                        "batch_id": batch_id,
                        "chunk_index": chunk_idx,
                        "backtest_name": bt_name,
                        "_ingested_at": now_ts,
                        "trade_id": ct_id
                    })
                    parsed_rows.append({
                        "pk": f"CLOUD_{real_backtest_id}_{ct_id}_CLOSE",
                        "backtestId": real_backtest_id,
                        "algo_code": "4EVC",
                        "timestamp": str(ct.get("exitTime")) if ct.get("exitTime") else now_ts,
                        "underlying": und_ticker[:32],
                        "action": "CLOSE",
                        "qty": int(qty),
                        "entry_price": entry_p,
                        "exit_price": exit_p,
                        "pnl": pnl_pct,
                        "batch_id": batch_id,
                        "chunk_index": chunk_idx,
                        "backtest_name": bt_name,
                        "_ingested_at": now_ts,
                        "trade_id": ct_id
                    })

            # Ensure all parsed rows carry batch_id, chunk_index, backtestId, and backtest_name tags
            for r in parsed_rows:
                r["batch_id"] = batch_id
                r["chunk_index"] = chunk_idx
                if "backtest_run_id" in r and "backtestId" not in r:
                    r["backtestId"] = r.pop("backtest_run_id")
                if not r.get("backtest_name"):
                    r["backtest_name"] = bt_id_or_name

            # Stream to BigQuery BTOPTrades
            existing_keys = get_existing_records(bq_client, PROJECT_ID, DATASET_ID)
            new_rows = []
            for r in parsed_rows:
                k = (r.get("pk"), r.get("action"))
                if k[0] and k[1] and k not in existing_keys:
                    new_rows.append(r)
                    existing_keys.add(k)

            if new_rows:
                logging.info(f"[Batch Poller] Uploading {len(new_rows)} trade records for batch '{batch_id}' to BTOPTrades via batch load job...")
                upload_trade_records(trade_records=new_rows)

            # 4. Mark chunk as COMPLETED in BigQuery BTOPBatchChunks
            update_chunk_status(bq_client, batch_id, bt_id_or_name, "COMPLETED")
            logging.info(f"[Batch Poller] [SUCCESS] Chunk {bt_id_or_name} fully ingested.")

            # 5. Automatically trigger next PENDING chunk in this batch
            trigger_next_pending_chunk(bq_client, batch_id, headers)

        except Exception as err:
            logging.error(f"[Batch Poller] Exception processing chunk {bt_id_or_name}: {err}")


def trigger_next_pending_chunk(client, batch_id: str, headers: Dict[str, str]) -> None:
    """Finds the next PENDING chunk for a batch ID and triggers it on QC Cloud."""
    query = f"""
    SELECT batch_id, backtest_id, chunk_index, CAST(start_date AS STRING) as start_date, CAST(end_date AS STRING) as end_date, compile_id
    FROM `{PROJECT_ID}.{DATASET_ID}.BTOPBatchChunks`
    WHERE batch_id = '{batch_id}' AND status = 'PENDING'
    ORDER BY chunk_index ASC
    LIMIT 1
    """
    results = list(client.query(query).result())
    if not results:
        logging.info(f"[Batch Poller] No more pending chunks for batch '{batch_id}'. Batch is 100% COMPLETE!")
        return

    next_chunk = dict(results[0])
    chunk_name = next_chunk["backtest_id"]
    compile_id = next_chunk.get("compile_id")
    start_date = next_chunk["start_date"]
    end_date = next_chunk["end_date"]
    project_id = 22447448

    if not compile_id:
        logging.warning(f"[Batch Poller] Missing compile_id for {chunk_name}. Cannot trigger next chunk.")
        return

    logging.info(f"[Batch Poller] Auto-triggering next chunk {chunk_name} ({start_date} to {end_date}) on QC Cloud...")

    url_create = "https://www.quantconnect.com/api/v2/backtests/create"
    payload = {
        "projectId": project_id,
        "compileId": compile_id,
        "backtestName": chunk_name,
        "parameters": [
            {"key": "exec.start_date", "value": start_date},
            {"key": "exec.end_date", "value": end_date},
            {"key": "algo.is_hdbt", "value": "true"},
            {"key": "algo.pass_all", "value": "true"},
            {"key": "univ.coarse.max_symbols", "value": "1000"}
        ]
    }
    resp = requests.post(url_create, headers=headers, json=payload, timeout=30)
    data = resp.json()
    if data.get("success"):
        bt_info = data.get("backtest", {})
        real_hex = bt_info.get("backtestId") or bt_info.get("id") or chunk_name
        update_chunk_status(client, batch_id, chunk_name, "RUNNING", new_backtest_id=real_hex)
        logging.info(f"[Batch Poller] [SUCCESS] Triggered next chunk {chunk_name} -> Hex ID: {real_hex}")
    else:
        logging.error(f"[Batch Poller] Failed to trigger chunk {chunk_name}: {data}")


if __name__ == "__main__":
    poll_and_ingest_chunks()
