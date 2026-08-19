"""
sync_closed_trades_to_btoptrades.py
===================================
Fetches totalPerformance.closedTrades directly from QuantConnect Cloud API (/api/v2/backtests/read)
with extended 300s socket read timeouts for large HDB backtest JSON payloads,
and streams trade rows into both BTOPTotalPerformanceClosedTrades and BTOPTrades.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import sys
import time
from typing import Any, Dict, List, Set, Tuple
import requests

# Ensure script directory and project root are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
for d in [_THIS_DIR, _PROJECT_ROOT, os.path.join(_PROJECT_ROOT, "Scripts")]:
    if d not in sys.path:
        sys.path.insert(0, d)

from db_operator import get_bigquery_client
from bt_synchronization import generate_api_token
from bt_handler import get_api_key
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)

PROJECT_ID = "bav-personal-cloud"
DATASET_ID = "develop"
TARGET_PROJECT_ID = 22447448


def safe_post(url: str, headers: Dict[str, str], json_payload: Dict[str, Any], max_retries: int = 3, timeout: Tuple[int, int] = (30, 300)) -> requests.Response | None:
    session = requests.Session()
    for attempt in range(1, max_retries + 1):
        try:
            resp = session.post(url, headers=headers, json=json_payload, timeout=timeout)
            if resp.status_code == 200:
                return resp
            logging.warning(f"HTTP {resp.status_code} on attempt {attempt}/{max_retries} for {url}")
        except Exception as err:
            logging.warning(f"Request exception on attempt {attempt}/{max_retries}: {err}")
        time.sleep(3 * attempt)
    return None


def get_existing_trade_pks(client: bigquery.Client) -> Set[str]:
    q = f"SELECT DISTINCT pk FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTrades` WHERE pk IS NOT NULL"
    res = list(client.query(q).result())
    return {r["pk"] for r in res}


def get_existing_closed_trade_ids(client: bigquery.Client) -> Set[str]:
    q = f"SELECT DISTINCT tradeId FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades` WHERE tradeId IS NOT NULL"
    res = list(client.query(q).result())
    return {r["tradeId"] for r in res}


def process_hdb_backtest(client: bigquery.Client, api_key: str, user_id: str, bt_item: Dict[str, Any], existing_trade_pks: Set[str], existing_ct_ids: Set[str]) -> Tuple[int, int]:
    bt_id = bt_item.get("backtestId") or bt_item.get("id")
    bt_name = bt_item.get("name", "UNKNOWN")
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    
    token = generate_api_token(api_key, user_id)
    headers = {"Authorization": f"Basic {token['api_token']}", "Timestamp": token["timestamp"]}
    
    read_url = "https://www.quantconnect.com/api/v2/backtests/read"
    resp = safe_post(read_url, headers, {"projectId": TARGET_PROJECT_ID, "backtestId": bt_id}, max_retries=3, timeout=(30, 300))
    if not resp:
        logging.error(f"[{bt_name}] Could not fetch backtest data from QC Cloud after retries.")
        return 0, 0
        
    bt_resp = resp.json()
    bt_data = bt_resp.get("backtest", {})
    total_perf = bt_data.get("totalPerformance", {}) or {}
    closed_trades = total_perf.get("closedTrades", []) if isinstance(total_perf, dict) else []

    if not closed_trades:
        logging.info(f"[{bt_name}] 0 closed trades found.")
        return 0, 0

    batch_id = bt_name.rsplit("_Y", 1)[0] if "_Y" in bt_name else bt_name
    chunk_index = int(bt_name[-4:]) if bt_name[-4:].isdigit() else 1

    job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")

    # 1. Format and stream into BTOPTotalPerformanceClosedTrades (symbol is RECORD struct)
    ct_rows = []
    for idx, ct in enumerate(closed_trades):
        ct_id = str(ct.get("id") or f"{bt_id}_ct_{idx}")
        if ct_id in existing_ct_ids:
            continue
            
        existing_ct_ids.add(ct_id)

        sym_val = "UNKNOWN"
        if ct.get("symbols") and isinstance(ct.get("symbols"), list) and len(ct["symbols"]) > 0:
            s0 = ct["symbols"][0]
            if isinstance(s0, dict):
                sym_val = str(s0.get("value") or s0.get("permtick") or "UNKNOWN")
            else:
                sym_val = str(s0)
        elif ct.get("symbol"):
            s_obj = ct.get("symbol")
            sym_val = s_obj.get("value") if isinstance(s_obj, dict) else str(s_obj)

        sym_struct = {"value": sym_val[:64], "id": "", "permtick": ""}

        ct_rows.append({
            "tradeId": ct_id,
            "backtestId": bt_id,
            "backtest_name": bt_name,
            "symbol": sym_struct,
            "entryTime": str(ct.get("entryTime")) if ct.get("entryTime") else None,
            "entryPrice": ct.get("entryPrice"),
            "direction": ct.get("direction"),
            "quantity": ct.get("quantity"),
            "exitTime": str(ct.get("exitTime")) if ct.get("exitTime") else None,
            "exitPrice": ct.get("exitPrice"),
            "profitLoss": ct.get("profitLoss"),
            "totalFees": ct.get("totalFees"),
            "mae": ct.get("mae"),
            "mfe": ct.get("mfe"),
            "duration": str(ct.get("duration")),
            "endTradeDrawdown": ct.get("endTradeDrawdown"),
            "isWin": ct.get("isWin"),
            "_ingested_at": now_ts
        })

    if ct_rows:
        for i in range(0, len(ct_rows), 2000):
            client.load_table_from_json(ct_rows[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades", job_config=job_cfg).result()
        logging.info(f"[{bt_name}] Ingested {len(ct_rows)} closed trade rows into BTOPTotalPerformanceClosedTrades.")

    # 2. Format and stream into BTOPTrades (underlying is STRING)
    trade_rows = []
    for idx, ct in enumerate(closed_trades):
        ct_id = str(ct.get("id") or f"{bt_id}_ct_{idx}")
        open_pk = f"CLOUD_{bt_id}_{ct_id}_OPEN"
        close_pk = f"CLOUD_{bt_id}_{ct_id}_CLOSE"

        sym_val = "UNKNOWN"
        und_val = "UNKNOWN"
        if ct.get("symbols") and isinstance(ct.get("symbols"), list) and len(ct["symbols"]) > 0:
            s0 = ct["symbols"][0]
            if isinstance(s0, dict):
                sym_val = str(s0.get("value") or s0.get("permtick") or "UNKNOWN")
                und_obj = s0.get("underlying")
                if isinstance(und_obj, dict):
                    und_val = str(und_obj.get("value") or und_obj.get("permtick") or sym_val[:4])
                else:
                    und_val = sym_val[:4]
            else:
                sym_val = str(s0)
                und_val = sym_val[:4]

        entry_p = float(ct.get("entryPrice") or 0.0)
        exit_p = float(ct.get("exitPrice") or 0.0)
        qty = abs(float(ct.get("quantity") or 0.0))
        pnl_val = float(ct.get("profitLoss") or 0.0)
        # Option contract capital = entry_p * qty * 100
        denom = entry_p * qty * 100.0
        pnl_pct = round(pnl_val / denom, 5) if denom > 0 else (round((exit_p - entry_p) / entry_p, 5) if entry_p > 0 else 0.0)

        if open_pk not in existing_trade_pks:
            existing_trade_pks.add(open_pk)
            trade_rows.append({
                "pk": open_pk,
                "backtestId": bt_id,
                "algo_code": "4EVC",
                "timestamp": str(ct.get("entryTime")) if ct.get("entryTime") else None,
                "underlying": und_val[:32],
                "action": "OPEN",
                "qty": int(qty),
                "entry_price": entry_p,
                "exit_price": 0.0,
                "pnl": 0.0,
                "batch_id": batch_id,
                "chunk_index": chunk_index,
                "backtest_name": bt_name,
                "_ingested_at": now_ts,
                "trade_id": ct_id
            })

        if close_pk not in existing_trade_pks:
            existing_trade_pks.add(close_pk)
            trade_rows.append({
                "pk": close_pk,
                "backtestId": bt_id,
                "algo_code": "4EVC",
                "timestamp": str(ct.get("exitTime")) if ct.get("exitTime") else None,
                "underlying": und_val[:32],
                "action": "CLOSE",
                "qty": int(qty),
                "entry_price": entry_p,
                "exit_price": exit_p,
                "pnl": pnl_pct,
                "batch_id": batch_id,
                "chunk_index": chunk_index,
                "backtest_name": bt_name,
                "_ingested_at": now_ts,
                "trade_id": ct_id
            })

    if trade_rows:
        for i in range(0, len(trade_rows), 2000):
            client.load_table_from_json(trade_rows[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPTrades", job_config=job_cfg).result()
        logging.info(f"[{bt_name}] [SUCCESS] Ingested {len(trade_rows)} trade rows into BTOPTrades.")

    return len(ct_rows), len(trade_rows)


def main():
    bq_client = get_bigquery_client()
    api_key, user_id = get_api_key()
    
    existing_trade_pks = get_existing_trade_pks(bq_client)
    existing_ct_ids = get_existing_closed_trade_ids(bq_client)
    
    url_list = "https://www.quantconnect.com/api/v2/backtests/list"
    token = generate_api_token(api_key, user_id)
    headers = {"Authorization": f"Basic {token['api_token']}", "Timestamp": token["timestamp"]}
    resp = safe_post(url_list, headers, {"projectId": TARGET_PROJECT_ID}, max_retries=3, timeout=(30, 60))
    if not resp:
        logging.error("Could not fetch backtests list from QC Cloud.")
        return

    qc_backtests = resp.json().get("backtests", [])
    logging.info(f"Retrieved {len(qc_backtests)} total backtests from QC Cloud.")

    target_names = [
        "BATCH_4EVC_V1.0_20260804_200654_Y2019",
        "BATCH_4EVC_V1.0_20260804_200654_Y2018",
        "BATCH_4EVC_V1.0_20260804_200654_Y2017",
        "BATCH_4EVC_V1.0_20260804_200654_Y2016",
        "BATCH_4EVC_V1.0_20260804_200430_Y2019",
        "BATCH_4EVC_V1.0_20260804_200430_Y2018",
        "BATCH_4EVC_V1.0_20260804_200430_Y2017",
        "BATCH_4EVC_V1.0_20260804_200430_Y2016",
        "BATCH_4EVC_V1_20260803_232019_Y2024",
        "BATCH_4EVC_V1_20260803_232019_Y2023",
        "BATCH_4EVC_V1_20260803_232019_Y2022",
        "BATCH_4EVC_V1_20260803_232019_Y2021",
        "BATCH_4EVC_V1_20260803_232019_Y2020",
    ]

    report = []
    for bt in qc_backtests:
        name = bt.get("name")
        if name in target_names or "BATCH_4EVC" in name:
            bt_id = bt.get("backtestId") or bt.get("id")
            logging.info(f"Processing HDB run: {name} ({bt_id})...")
            n_ct, n_tr = process_hdb_backtest(bq_client, api_key, user_id, bt, existing_trade_pks, existing_ct_ids)
            report.append({"name": name, "bt_id": bt_id, "closed_trades": n_ct, "btoptrades_rows": n_tr})

    print("\n" + "=" * 95)
    print("FINAL HDB CLOSED TRADES & BTOPTRADES INGESTION REPORT")
    print("=" * 95)
    print(f"| {'Backtest Name':<42} | {'Closed Trades':<14} | {'BTOPTrades Rows':<16} |")
    print("| " + "-"*42 + " | " + "-"*14 + " | " + "-"*16 + " |")
    for r in report:
        print(f"| {r['name']:<42} | {r['closed_trades']:<14} | {r['btoptrades_rows']:<16} |")
    print("=" * 95 + "\n")


if __name__ == "__main__":
    main()
