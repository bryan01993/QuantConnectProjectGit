"""
verify_and_ingest_hdbt_trades.py
=================================
Verifies and ingests all trade and order records for HDBT batch backtest runs on QC Cloud into BTOPTrades.
"""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import os
import sys
import time
from typing import Any, Dict, List, Set, Tuple
import requests

# Ensure script directory and project root are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
for d in [_THIS_DIR, _PROJECT_ROOT]:
    if d not in sys.path:
        sys.path.insert(0, d)

from db_operator import get_bigquery_client, load_orders  # noqa: E402
from bt_synchronization import generate_api_token, load_user_config  # noqa: E402
from bt_handler import get_api_key  # noqa: E402
from log_trades_uploader import get_existing_records, PROJECT_ID, DATASET_ID, TABLE_NAME as TRADES_TABLE  # noqa: E402

logging.basicConfig(level=logging.INFO)

TARGET_PROJECT_ID = 22447448


def main():
    bq_client = get_bigquery_client()
    api_key, user_id = get_api_key()
    token = generate_api_token(api_key, user_id)
    headers = {
        "Authorization": f"Basic {token['api_token']}",
        "Timestamp": token["timestamp"],
    }

    # 1. Fetch backtest list from QC Cloud
    logging.info(f"Fetching backtests list from QC Cloud for project {TARGET_PROJECT_ID}...")
    url_list = "https://www.quantconnect.com/api/v2/backtests/list"
    resp = requests.post(url_list, headers=headers, json={"projectId": TARGET_PROJECT_ID}, timeout=30)
    if resp.status_code != 200:
        logging.error(f"Failed to list backtests: HTTP {resp.status_code}")
        return

    qc_backtests = resp.json().get("backtests", [])
    logging.info(f"Retrieved {len(qc_backtests)} backtests from QC Cloud.")

    name_map = {}
    id_map = {}
    for bt in qc_backtests:
        b_name = bt.get("name")
        b_id = bt.get("backtestId") or bt.get("id")
        if b_name:
            name_map[b_name] = bt
        if b_id:
            id_map[b_id] = bt

    # 2. Get existing trade records from BigQuery BTOPTrades
    existing_keys = get_existing_records(bq_client, PROJECT_ID, DATASET_ID)
    logging.info(f"Existing trade keys in BTOPTrades: {len(existing_keys)}")

    # 3. Target HDBT runs from user screenshot
    target_names = [
        "BATCH_4EVC_V1_20260803_232019_Y2020",
        "BATCH_4EVC_V1_20260803_232019_Y2021",
        "BATCH_4EVC_V1_20260803_232019_Y2022",
        "BATCH_4EVC_V1_20260803_232019_Y2023",
        "BATCH_4EVC_V1_20260803_232019_Y2024",
        "BATCH_4EVC_V1.0_20260804_200430_Y2016",
        "BATCH_4EVC_V1.0_20260804_200430_Y2017",
        "BATCH_4EVC_V1.0_20260804_200430_Y2018",
        "BATCH_4EVC_V1.0_20260804_200430_Y2019",
        "BATCH_4EVC_V1.0_20260804_200654_Y2016",
        "BATCH_4EVC_V1.0_20260804_200654_Y2017",
        "BATCH_4EVC_V1.0_20260804_200654_Y2018",
        "BATCH_4EVC_V1.0_20260804_200654_Y2019",
    ]

    report = []

    for name in target_names:
        matched = name_map.get(name)
        if not matched:
            report.append({"name": name, "hex_id": "NOT_FOUND_ON_QC", "status": "NOT_FOUND", "orders_count": 0, "trades_inserted": 0})
            continue

        hex_id = matched.get("backtestId") or matched.get("id")
        completed = matched.get("completed", False)
        progress = matched.get("progress", 0.0)

        # Fresh headers per call
        t = generate_api_token(api_key, user_id)
        h = {"Authorization": f"Basic {t['api_token']}", "Timestamp": t["timestamp"]}

        # Download orders from QC API
        orders_url = "https://www.quantconnect.com/api/v2/backtests/orders/read"
        payload = {"start": 0, "end": 50000, "projectId": TARGET_PROJECT_ID, "backtestId": hex_id}
        ord_resp = requests.post(orders_url, headers=h, json=payload, timeout=30)

        raw_orders = ord_resp.json().get("orders", {}) if ord_resp.status_code == 200 else {}
        orders = list(raw_orders.values()) if isinstance(raw_orders, dict) else raw_orders

        # Parse trade records
        trade_rows = []
        open_positions = {}
        counter = 0

        for o in orders:
            sym = o.get("symbol", {}).get("value", "UNKNOWN")
            qty = o.get("quantity", 0)
            price = o.get("price", 0.0)
            ts = o.get("time", "")

            if qty > 0:
                counter += 1
                pk = f"CLOUD_{hex_id}_{sym}_{counter}"
                rec = {
                    "pk": pk, "backtest_run_id": hex_id, "algo_code": "4EVC",
                    "timestamp": ts, "underlying": sym, "action": "OPEN", "qty": int(qty),
                    "entry_price": round(float(price), 5), "exit_price": 0.0, "pnl": 0.0,
                    "batch_id": name.rsplit("_Y", 1)[0], "chunk_index": int(name[-4:]) if name[-4:].isdigit() else 1
                }
                open_positions[sym] = rec
                trade_rows.append(rec)
            elif qty < 0 and sym in open_positions:
                open_rec = open_positions.pop(sym)
                entry_p = open_rec["entry_price"]
                exit_p = round(float(price), 5)
                pnl = round((exit_p - entry_p) / entry_p, 5) if entry_p > 0 else 0.0
                trade_rows.append({
                    "pk": open_rec["pk"], "backtest_run_id": hex_id, "algo_code": "4EVC",
                    "timestamp": ts, "underlying": sym, "action": "CLOSE", "qty": int(abs(qty)),
                    "entry_price": entry_p, "exit_price": exit_p, "pnl": pnl,
                    "batch_id": name.rsplit("_Y", 1)[0], "chunk_index": int(name[-4:]) if name[-4:].isdigit() else 1
                })

        # Check new trade rows to insert
        new_rows = []
        for r in trade_rows:
            k = (r.get("pk"), r.get("action"))
            if k not in existing_keys:
                new_rows.append(r)
                existing_keys.add(k)

        inserted_count = 0
        if new_rows:
            table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TRADES_TABLE}"
            for i in range(0, len(new_rows), 500):
                bq_client.insert_rows_json(table_ref, new_rows[i:i + 500])
            inserted_count = len(new_rows)
            logging.info(f"[{name}] Streamed {inserted_count} trade records to BTOPTrades.")

        report.append({
            "name": name,
            "hex_id": hex_id,
            "completed": completed,
            "progress": f"{progress*100:.1f}%",
            "orders_count": len(orders),
            "trade_records": len(trade_rows),
            "newly_inserted_trades": inserted_count
        })

    print("\n" + "=" * 90)
    print("HDBT CHUNK INGESTION & VERIFICATION REPORT")
    print("=" * 90)
    print(f"| {'Backtest Name':<38} | {'Hex ID':<12} | {'Orders':<6} | {'Trades':<6} | {'Inserted':<8} |")
    print("| " + "-"*38 + " | " + "-"*12 + " | " + "-"*6 + " | " + "-"*6 + " | " + "-"*8 + " |")
    for r in report:
        print(f"| {r['name']:<38} | {str(r['hex_id'])[:12]:<12} | {r.get('orders_count', 0):<6} | {r.get('trade_records', 0):<6} | {r.get('newly_inserted_trades', 0):<8} |")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    main()
