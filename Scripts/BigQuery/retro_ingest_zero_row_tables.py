"""
retro_ingest_zero_row_tables.py
================================
Populates `BTOPOrders`, `BTOPStatistics`, and `BTOPErrors` from existing
downloaded backtest results and order JSON files.
"""

from __future__ import annotations

import glob
import json
import os
import sys
from typing import Any, Dict, List
from google.cloud import bigquery

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client, load_orders, load_backtest_statistics, load_errors  # noqa: E402

PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"


def retro_ingest_orders(client: bigquery.Client) -> int:
    ord_dirs = [
        os.path.join(_PROJECT_ROOT, "Scripts", "already_uploaded_orders_results"),
        os.path.join(_PROJECT_ROOT, "Scripts", "orders_results"),
    ]
    ord_files = []
    for d in ord_dirs:
        if os.path.exists(d):
            ord_files.extend(glob.glob(os.path.join(d, "*.json")))

    print(f"\n--- Retro-ingesting BTOPOrders from {len(ord_files)} order files ---")
    ingested_count = 0

    for file_path in ord_files:
        base_name = os.path.basename(file_path)
        backtest_id = base_name.split("_")[0]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                payload = json.load(f)

            if isinstance(payload, dict) and "orders" in payload:
                orders_list = payload["orders"]
            elif isinstance(payload, list):
                orders_list = payload
            else:
                orders_list = []

            if orders_list:
                data_wrap = {"orders": orders_list}
                load_orders(data_wrap, client, DATASET_ID, backtest_id)
                ingested_count += 1
                print(f"[SUCCESS] Ingested {len(orders_list)} orders for backtest '{backtest_id}'.")
        except Exception as e:
            print(f"[ERROR] Ingesting orders for {base_name}: {e}")

    return ingested_count


def retro_ingest_statistics_and_errors(client: bigquery.Client) -> tuple[int, int]:
    bt_dirs = [
        os.path.join(_PROJECT_ROOT, "Scripts", "already_uploaded_backtest_results"),
        os.path.join(_PROJECT_ROOT, "Scripts", "backtest_results"),
    ]
    bt_files = []
    for d in bt_dirs:
        if os.path.exists(d):
            bt_files.extend(glob.glob(os.path.join(d, "*.json")))

    print(f"\n--- Retro-ingesting BTOPStatistics and BTOPErrors from {len(bt_files)} result files ---")
    stats_count = 0
    errors_count = 0

    for file_path in bt_files:
        base_name = os.path.basename(file_path)
        backtest_id = base_name.replace(".json", "")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            bt = data.get("backtest", data)
            if not isinstance(bt, dict):
                continue

            # 1. Ingest BTOPStatistics
            stats = bt.get("statistics") or bt.get("Statistics")
            if isinstance(stats, dict) and stats:
                load_backtest_statistics(data, client, DATASET_ID, backtest_id)
                stats_count += 1

            # 2. Ingest BTOPErrors
            err_msg = bt.get("error") or bt.get("RuntimeError") or data.get("error")
            stack = bt.get("stacktrace") or bt.get("StackTrace")
            if err_msg or stack:
                table_id = f"{DATASET_ID}.BTOPErrors"
                row = [{
                    "errorId": f"{backtest_id}_error_0",
                    "backtestId": backtest_id,
                    "message": str(err_msg)[:1000] if err_msg else "Runtime Error",
                    "stackTrace": str(stack)[:4000] if stack else None
                }]
                client.insert_rows_json(table_id, row)
                errors_count += 1
                print(f"[SUCCESS] Ingested BTOPErrors record for backtest '{backtest_id}'.")

        except Exception as e:
            print(f"[ERROR] Ingesting stats/errors for {base_name}: {e}")

    return stats_count, errors_count


def main():
    client = get_bigquery_client(PROJECT_ID)
    orders_ingested = retro_ingest_orders(client)
    stats_ingested, errors_ingested = retro_ingest_statistics_and_errors(client)

    print("\n========================================================")
    print(" RETRO-INGESTION SUMMARY")
    print("========================================================")
    print(f"  BTOPOrders files ingested:     {orders_ingested}")
    print(f"  BTOPStatistics runs ingested:  {stats_ingested}")
    print(f"  BTOPErrors runs ingested:      {errors_ingested}")
    print("========================================================\n")


if __name__ == "__main__":
    main()
