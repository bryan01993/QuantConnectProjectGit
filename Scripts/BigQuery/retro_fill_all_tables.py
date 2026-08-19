"""
retro_fill_all_tables.py
========================
Backfills missing backtest data across all BigQuery tables in bav-personal-cloud.develop.
Fetches full backtest results JSON & orders JSON from QuantConnect Cloud API
and populates BTOPResults, BTOPTotalPerformancePortfolioStats, BTOPTotalPerformanceTradeStats,
BTOPTotalPerformanceClosedTrades, BTOPTrades, BTOPParameterSet, BTOPStatistics, etc.
"""

from __future__ import annotations

import logging
import os
import sys
import time
from typing import Any, Dict, Set, List
import requests

# Ensure script directory and project root are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
for d in [_THIS_DIR, _PROJECT_ROOT]:
    if d not in sys.path:
        sys.path.insert(0, d)

from db_operator import (  # noqa: E402
    get_bigquery_client,
    load_backtest,
    load_total_performance,
    load_parameter_set,
    load_backtest_statistics,
    load_runtime_statistics,
    load_rolling_window_stats,
    load_charts,
    load_research_guide,
    load_errors,
    load_orders,
)
from bt_synchronization import generate_api_token, load_user_config  # noqa: E402
from bt_handler import get_api_key  # noqa: E402
from log_trades_uploader import (  # noqa: E402
    parse_orders_json_file,
    get_existing_records,
    PROJECT_ID,
    DATASET_ID,
    TABLE_NAME as TRADES_TABLE,
)

logging.basicConfig(level=logging.INFO)


def get_all_warehouse_backtest_ids(client: Any) -> Set[str]:
    """Collects all unique backtest IDs across key tables in BigQuery."""
    all_ids: Set[str] = set()
    
    queries = [
        ("BTOPResults", "backtestId"),
        ("BTOPTrades", "backtestId"),
        ("BTOPBatchChunks", "backtest_id"),
        ("BTOPOrders", "backtestId"),
        ("BTOPTotalPerformancePortfolioStats", "backtestId"),
        ("BTOPParameterSet", "backtestId"),
    ]
    
    for tbl, col in queries:
        q = f"SELECT DISTINCT {col} FROM `{PROJECT_ID}.{DATASET_ID}.{tbl}` WHERE {col} IS NOT NULL"
        try:
            results = client.query(q).result()
            for r in results:
                val = r[col]
                # Ignore non-hex placeholder names like BATCH_...
                if val and len(val) == 32 and not val.startswith("BATCH_"):
                    all_ids.add(val)
        except Exception as e:
            logging.warning(f"Could not fetch IDs from {tbl}.{col}: {e}")
            
    return all_ids


def get_existing_table_ids(client: Any, table_name: str, id_col: str) -> Set[str]:
    """Returns set of backtest IDs already existing in a given table."""
    q = f"SELECT DISTINCT {id_col} FROM `{PROJECT_ID}.{DATASET_ID}.{table_name}` WHERE {id_col} IS NOT NULL"
    try:
        results = client.query(q).result()
        return {r[id_col] for r in results if r[id_col]}
    except Exception as e:
        logging.warning(f"Could not query {table_name}.{id_col}: {e}")
        return set()


def main():
    bq_client = get_bigquery_client()
    
    # 1. Collect all distinct backtest IDs in warehouse
    all_bt_ids = get_all_warehouse_backtest_ids(bq_client)
    logging.info(f"[Retro-Fill] Discovered {len(all_bt_ids)} unique 32-hex backtest IDs across warehouse tables.")
    
    # 2. Get existing IDs in destination stats tables
    results_ids = get_existing_table_ids(bq_client, "BTOPResults", "backtestId")
    portfolio_stats_ids = get_existing_table_ids(bq_client, "BTOPTotalPerformancePortfolioStats", "backtestId")
    trades_ids = get_existing_table_ids(bq_client, "BTOPTrades", "backtestId")
    
    # 3. Resolve QC API Credentials
    api_key, user_id = get_api_key()
    defaults = load_user_config()
    project_ids = [22447448]
    user_pid = defaults.get("PROJECT_ID")
    if user_pid and int(user_pid) not in project_ids:
        project_ids.append(int(user_pid))
        
    logging.info(f"[Retro-Fill] Project IDs to search: {project_ids}")
    
    processed_count = 0
    
    for bt_id in sorted(all_bt_ids):
        needs_results = bt_id not in results_ids or bt_id not in portfolio_stats_ids
        needs_trades = bt_id not in trades_ids
        
        if not needs_results and not needs_trades:
            continue
            
        logging.info(f"[Retro-Fill] Processing missing data for Backtest ID: {bt_id}...")
        
        # Fresh API headers for each request
        token = generate_api_token(api_key, user_id)
        headers = {
            "Authorization": f"Basic {token['api_token']}",
            "Timestamp": token["timestamp"],
        }
        
        bt_data = None
        matched_pid = None
        
        # Try fetching from project IDs
        for pid in project_ids:
            url_read = "https://www.quantconnect.com/api/v2/backtests/read"
            payload = {"projectId": pid, "backtestId": bt_id}
            try:
                resp = requests.post(url_read, headers=headers, json=payload, timeout=30)
                if resp.status_code == 200:
                    d = resp.json()
                    if d.get("success") and d.get("backtest"):
                        bt_data = d
                        matched_pid = pid
                        break
            except Exception as e:
                logging.warning(f"Error fetching backtest {bt_id} for pid {pid}: {e}")
                
        if not bt_data:
            logging.warning(f"[Retro-Fill] Could not fetch backtest {bt_id} from QC Cloud API.")
            continue
            
        # A) Ingest missing portfolio and detailed statistics tables
        if needs_results:
            try:
                logging.info(f"[Retro-Fill] Ingesting portfolio stats & metadata for {bt_id}...")
                load_backtest(bt_data, bq_client, DATASET_ID, bt_id)
                load_research_guide(bt_data, bq_client, DATASET_ID, bt_id)
                load_backtest_statistics(bt_data, bq_client, DATASET_ID, bt_id)
                load_charts(bt_data, bq_client, DATASET_ID, bt_id)
                load_parameter_set(bt_data, bq_client, DATASET_ID, bt_id)
                load_rolling_window_stats(bt_data, bq_client, DATASET_ID, bt_id)
                load_runtime_statistics(bt_data, bq_client, DATASET_ID, bt_id)
                load_total_performance(bt_data, bq_client, DATASET_ID, bt_id)
                load_errors(bt_data, bq_client, DATASET_ID, bt_id)
            except Exception as e:
                logging.error(f"[Retro-Fill] Error loading stats for {bt_id}: {e}")
                
        # B) Ingest missing order and trade records
        if needs_trades and matched_pid:
            try:
                url_orders = "https://www.quantconnect.com/api/v2/backtests/orders/read"
                ord_payload = {"start": 0, "end": 50000, "projectId": matched_pid, "backtestId": bt_id}
                ord_resp = requests.post(url_orders, headers=headers, json=ord_payload, timeout=45)
                if ord_resp.status_code == 200:
                    raw_orders = ord_resp.json().get("orders", {})
                    orders = list(raw_orders.values()) if isinstance(raw_orders, dict) else raw_orders
                    
                    if orders:
                        # Ingest into BTOPOrders
                        load_orders({"backtest": {"backtestId": bt_id}, "orders": orders}, bq_client, DATASET_ID, bt_id)
                        
                        # Ingest trade records into BTOPTrades
                        open_pos = {}
                        trade_rows = []
                        counter = 0
                        for o in orders:
                            sym = o.get("symbol", {}).get("value", "UNKNOWN")
                            qty = o.get("quantity", 0)
                            price = o.get("price", 0.0)
                            ts = o.get("time", "")
                            
                            if qty > 0:
                                counter += 1
                                rec = {
                                    "pk": f"CLOUD_{bt_id}_{sym}_{counter}",
                                    "backtestId": bt_id, "algo_code": "4EVC",
                                    "timestamp": ts, "underlying": sym, "action": "OPEN", "qty": int(qty),
                                    "entry_price": round(float(price), 5), "exit_price": 0.0, "pnl": 0.0
                                }
                                open_pos[sym] = rec
                                trade_rows.append(rec)
                            elif qty < 0 and sym in open_pos:
                                open_rec = open_pos.pop(sym)
                                entry_p = open_rec["entry_price"]
                                exit_p = round(float(price), 5)
                                pnl = round((exit_p - entry_p) / entry_p, 5) if entry_p > 0 else 0.0
                                trade_rows.append({
                                    "pk": open_rec["pk"], "backtestId": bt_id, "algo_code": "4EVC",
                                    "timestamp": ts, "underlying": sym, "action": "CLOSE", "qty": int(abs(qty)),
                                    "entry_price": entry_p, "exit_price": exit_p, "pnl": pnl
                                })
                                
                        if trade_rows:
                            existing_keys = get_existing_records(bq_client, PROJECT_ID, DATASET_ID)
                            new_rows = [r for r in trade_rows if (r.get("pk"), r.get("action")) not in existing_keys]
                            if new_rows:
                                table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TRADES_TABLE}"
                                for i in range(0, len(new_rows), 500):
                                    bq_client.insert_rows_json(table_ref, new_rows[i:i+500])
                                logging.info(f"[Retro-Fill] Inserted {len(new_rows)} trade records for {bt_id} into BTOPTrades.")
            except Exception as e:
                logging.error(f"[Retro-Fill] Error loading trades for {bt_id}: {e}")
                
        processed_count += 1
        time.sleep(1)
        
    logging.info(f"[Retro-Fill COMPLETE] Processed {processed_count} backtest IDs across all warehouse tables.")


if __name__ == "__main__":
    main()
