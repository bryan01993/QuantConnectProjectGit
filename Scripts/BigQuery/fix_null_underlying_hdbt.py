"""
fix_null_underlying_hdbt.py
===========================
Data repair script that identifies HDBT backtests with NULL or missing underlying symbols
in BigQuery tables, re-fetches closedTrades from QuantConnect REST API, formats the nested
symbol RECORD struct correctly using build_symbol_struct(), and re-ingests clean rows.
"""

import os
import sys
import time
import json
import base64
import hashlib
import logging
import requests
from typing import List, Dict, Any, Set
import yaml

from google.cloud import bigquery

# Ensure script directory and project root are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
for d in [_THIS_DIR, _PROJECT_ROOT, os.path.join(_PROJECT_ROOT, "Scripts")]:
    if d not in sys.path:
        sys.path.insert(0, d)

from db_operator import get_bigquery_client, build_symbol_struct, _to_timestamp_str

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

PROJECT_ID = "bav-personal-cloud"
DATASET_ID = "develop"
TARGET_PROJECT_ID = 22447448


def load_qc_credentials() -> tuple[str, str]:
    config_path = os.path.join(_PROJECT_ROOT, "Resources", "UserConfig.yaml")
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    user_id = str(cfg["defaults"]["USER_ID"])
    api_key = str(cfg["defaults"]["LOGIN_API_KEY"])
    return user_id, api_key


def generate_headers(user_id: str, api_key: str) -> dict:
    ts = str(int(time.time()))
    to_hash = f"{api_key}:{ts}"
    api_token = hashlib.sha256(to_hash.encode("utf-8")).hexdigest()
    auth_str = f"{user_id}:{api_token}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    return {"Authorization": f"Basic {auth_b64}", "Timestamp": ts}


def get_affected_backtest_ids(client: bigquery.Client) -> List[tuple[str, str]]:
    """Returns distinct (backtestId, backtest_name) tuples needing underlying repair."""
    query = f"""
    SELECT DISTINCT backtestId, backtest_name 
    FROM `{PROJECT_ID}.{DATASET_ID}.v_4EVC_consolidated_spread_trades` 
    WHERE underlying IS NULL
    """
    rows = list(client.query(query, location="europe-west1").result())
    result = [(r.backtestId, r.backtest_name or "UNKNOWN") for r in rows if r.backtestId]
    
    # Also check BTOPTotalPerformanceClosedTrades directly for null symbols
    query2 = f"""
    SELECT DISTINCT backtestId, backtest_name
    FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades`
    WHERE symbol IS NULL OR symbol.underlying.value IS NULL
    """
    rows2 = list(client.query(query2, location="europe-west1").result())
    for r in rows2:
        if r.backtestId and (r.backtestId, r.backtest_name or "UNKNOWN") not in result:
            result.append((r.backtestId, r.backtest_name or "UNKNOWN"))
            
    return result


def repair_backtest_data(client: bigquery.Client, user_id: str, api_key: str, bt_id: str, bt_name: str) -> bool:
    """Purges defective rows for bt_id and re-ingests formatted closedTrades and BTOPTrades."""
    read_url = "https://www.quantconnect.com/api/v2/backtests/read"
    
    resp = None
    for attempt in range(3):
        try:
            headers = generate_headers(user_id, api_key)
            resp = requests.post(read_url, headers=headers, json={"projectId": TARGET_PROJECT_ID, "backtestId": bt_id}, timeout=120)
            if resp.status_code == 200:
                break
        except Exception as e:
            logging.warning(f"[{bt_id}] QC API attempt {attempt+1}/3 failed: {e}. Retrying...")
            time.sleep(3)

    if resp is None or resp.status_code != 200:
        logging.error(f"[{bt_id}] Failed to fetch QC backtest data after retries.")
        return False
        
    data = resp.json()
    if not data.get("success"):
        logging.error(f"[{bt_id}] QC API returned success=False: {data.get('errors')}")
        return False

    bt_data = data.get("backtest", {})
    real_bt_name = bt_data.get("name") or bt_name
    total_perf = bt_data.get("totalPerformance", {}) or {}
    closed_trades = total_perf.get("closedTrades", []) if isinstance(total_perf, dict) else []

    if not closed_trades:
        logging.warning(f"[{real_bt_name}] No closedTrades found in QC API response.")
        return False

    now_ts = time.strftime("%Y-%m-%d %H:%M:%S")
    job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")

    # 1. Delete existing corrupted rows for this backtestId from BTOPTotalPerformanceClosedTrades and BTOPTrades
    del_query1 = f"DELETE FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades` WHERE backtestId = '{bt_id}'"
    del_query2 = f"DELETE FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTrades` WHERE backtestId = '{bt_id}'"
    client.query(del_query1, location="europe-west1").result()
    client.query(del_query2, location="europe-west1").result()
    logging.info(f"[{real_bt_name}] Purged obsolete records for backtestId {bt_id}")

    # 2. Build clean closedTrades rows with proper symbol RECORD struct
    ct_rows = []
    trade_rows = []
    batch_id = real_bt_name.rsplit("_Y", 1)[0] if "_Y" in real_bt_name else real_bt_name
    chunk_idx = int(real_bt_name[-4:]) if real_bt_name[-4:].isdigit() else 1

    for idx, ct in enumerate(closed_trades):
        ct_id = str(ct.get("id") or f"{bt_id}_ct_{idx}")
        sym_struct = build_symbol_struct(ct)
        und_ticker = sym_struct.get("underlying", {}).get("value") if (sym_struct and sym_struct.get("underlying")) else "UNKNOWN"
        if not und_ticker or und_ticker == "UNKNOWN":
            sym_val = ct.get("symbols", [{}])[0].get("value", "") if ct.get("symbols") else ""
            und_ticker = sym_val.split()[0] if sym_val else "UNKNOWN"

        entry_p = float(ct.get("entryPrice") or 0.0)
        exit_p = float(ct.get("exitPrice") or 0.0)
        qty = abs(float(ct.get("quantity") or 0.0))
        pnl_val = float(ct.get("profitLoss") or 0.0)
        denom = entry_p * qty * 100.0
        pnl_pct = round(pnl_val / denom, 5) if denom > 0 else (round((exit_p - entry_p) / entry_p, 5) if entry_p > 0 else 0.0)

        ct_rows.append({
            "tradeId": ct_id,
            "backtestId": bt_id,
            "backtest_name": real_bt_name,
            "symbol": sym_struct,
            "entryTime": _to_timestamp_str(ct.get("entryTime")),
            "entryPrice": entry_p,
            "direction": ct.get("direction"),
            "quantity": qty,
            "exitTime": _to_timestamp_str(ct.get("exitTime")),
            "exitPrice": exit_p,
            "profitLoss": pnl_val,
            "totalFees": ct.get("totalFees"),
            "mae": ct.get("mae"),
            "mfe": ct.get("mfe"),
            "duration": str(ct.get("duration")),
            "isWin": ct.get("isWin"),
            "_ingested_at": now_ts
        })

        trade_rows.append({
            "pk": f"CLOUD_{bt_id}_{ct_id}_OPEN",
            "backtestId": bt_id,
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
            "backtest_name": real_bt_name,
            "_ingested_at": now_ts,
            "trade_id": ct_id
        })
        trade_rows.append({
            "pk": f"CLOUD_{bt_id}_{ct_id}_CLOSE",
            "backtestId": bt_id,
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
            "backtest_name": real_bt_name,
            "_ingested_at": now_ts,
            "trade_id": ct_id
        })

    # Load repaired rows to BigQuery
    if ct_rows:
        client.load_table_from_json(ct_rows, f"{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades", job_config=job_cfg).result()
        logging.info(f"[{real_bt_name}] Re-ingested {len(ct_rows)} closed trades into BTOPTotalPerformanceClosedTrades.")

    if trade_rows:
        client.load_table_from_json(trade_rows, f"{PROJECT_ID}.{DATASET_ID}.BTOPTrades", job_config=job_cfg).result()
        logging.info(f"[{real_bt_name}] Re-ingested {len(trade_rows)} trade rows into BTOPTrades.")

    return True


def main():
    client = get_bigquery_client()
    user_id, api_key = load_qc_credentials()

    logging.info("Identifying backtests with NULL underlying symbol data...")
    affected = get_affected_backtest_ids(client)
    logging.info(f"Found {len(affected)} backtest runs requiring data repair.")

    success_count = 0
    for bt_id, bt_name in affected:
        logging.info(f"Repairing [{bt_name}] ({bt_id})...")
        if repair_backtest_data(client, user_id, api_key, bt_id, bt_name):
            success_count += 1

    logging.info(f"=== Repair Complete: {success_count}/{len(affected)} backtests successfully repaired ===")


if __name__ == "__main__":
    main()
