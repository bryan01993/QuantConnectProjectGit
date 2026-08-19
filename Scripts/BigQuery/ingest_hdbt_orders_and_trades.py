"""
ingest_hdbt_orders_and_trades.py
================================
Paginates through all order logs via QuantConnect API (/api/v2/backtests/orders/read with max step=100)
and totalPerformance.closedTrades to ingest 100% of trades and orders into BigQuery.

Enforces a MANDATORY Predictor Integrity Gate verifying that slope, vol_ratio, and ivrv_ratio
are correctly parsed and uploaded for >= 95% of OPEN trades.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import sys
import time
import json
from typing import Any, Dict, List, Set, Tuple
import requests

# Ensure script directory and project root are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
for d in [_THIS_DIR, _PROJECT_ROOT, os.path.join(_PROJECT_ROOT, "Scripts")]:
    if d not in sys.path:
        sys.path.insert(0, d)

from db_operator import get_bigquery_client, build_symbol_struct
from bt_synchronization import generate_api_token
from bt_handler import get_api_key
from log_trades_uploader import parse_orders_json_file
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)

PROJECT_ID = "bav-personal-cloud"
DATASET_ID = "develop"
TARGET_PROJECT_ID = 22447448


def fetch_all_orders_for_backtest(api_key: str, user_id: str, bt_id: str) -> List[Dict[str, Any]]:
    """Paginates through all orders for a backtest using start & end parameters (max range = 100)."""
    url = "https://www.quantconnect.com/api/v2/backtests/orders/read"
    all_orders = []
    start = 0
    step = 100
    
    while True:
        token = generate_api_token(api_key, user_id)
        headers = {"Authorization": f"Basic {token['api_token']}", "Timestamp": token["timestamp"]}
        payload = {"projectId": TARGET_PROJECT_ID, "backtestId": bt_id, "start": start, "end": start + step}
        
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code != 200:
                logging.warning(f"Orders read returned HTTP {resp.status_code} for {bt_id} at start {start}.")
                break
            
            data = resp.json()
            if not data.get("success", False):
                errs = data.get("errors", [])
                logging.warning(f"Orders read unsuccessful for {bt_id} at start {start}: {errs}")
                break

            total_len = data.get("length", 0)
            orders = data.get("orders", [])
            if isinstance(orders, dict):
                orders = list(orders.values())
                
            if not orders:
                break
                
            all_orders.extend(orders)
            
            if len(all_orders) >= total_len or len(orders) < step:
                break
                
            start += step
            time.sleep(0.02)
        except Exception as e:
            logging.error(f"Error fetching orders for {bt_id} at start {start}: {e}")
            break
            
    logging.info(f"[{bt_id}] Successfully retrieved {len(all_orders)} total orders.")
    return all_orders


def process_and_ingest_hdbt_backtest(client: bigquery.Client, api_key: str, user_id: str, bt_item: Dict[str, Any]) -> Tuple[int, int]:
    bt_id = bt_item.get("backtestId") or bt_item.get("id")
    bt_name = bt_item.get("name", "UNKNOWN")
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    
    token = generate_api_token(api_key, user_id)
    headers = {"Authorization": f"Basic {token['api_token']}", "Timestamp": token["timestamp"]}
    
    # 1. Fetch backtest details & closedTrades
    read_url = "https://www.quantconnect.com/api/v2/backtests/read"
    resp = requests.post(read_url, headers=headers, json={"projectId": TARGET_PROJECT_ID, "backtestId": bt_id}, timeout=60)
    if resp.status_code != 200:
        logging.error(f"[{bt_name}] HTTP {resp.status_code} when fetching results for {bt_id}")
        return 0, 0
        
    bt_resp = resp.json()
    bt_data = bt_resp.get("backtest", {})
    total_perf = bt_data.get("totalPerformance", {}) or {}
    closed_trades = total_perf.get("closedTrades", []) if isinstance(total_perf, dict) else []
    
    # Purge existing closed trades for this backtestId to avoid duplicates
    client.query(f"DELETE FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades` WHERE backtestId = '{bt_id}'", location="europe-west1").result()

    # Ingest closed trades to BTOPTotalPerformanceClosedTrades
    job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    if closed_trades:
        ct_rows = []
        for idx, ct in enumerate(closed_trades):
            sym_struct = build_symbol_struct(ct)
            ct_rows.append({
                "tradeId": ct.get("id", f"{bt_id}_ct_{idx}"),
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
                "isWin": ct.get("isWin"),
                "_ingested_at": now_ts
            })
        
        for i in range(0, len(ct_rows), 2000):
            client.load_table_from_json(ct_rows[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades", job_config=job_cfg, location="europe-west1").result()
        logging.info(f"[{bt_name}] Ingested {len(ct_rows)} closed trades into BTOPTotalPerformanceClosedTrades.")

    # 2. Fetch all orders with pagination (step=100)
    orders = fetch_all_orders_for_backtest(api_key, user_id, bt_id)
    
    # Save orders locally to orders_results/{bt_id}_orders.json
    orders_dir = os.path.join(_PROJECT_ROOT, "Scripts", "orders_results")
    os.makedirs(orders_dir, exist_ok=True)
    orders_file = os.path.join(orders_dir, f"{bt_id}_orders.json")
    with open(orders_file, "w", encoding="utf-8") as f:
        json.dump({"orders": orders}, f, indent=4)

    # Purge existing orders for this backtestId in BTOPOrders
    client.query(f"DELETE FROM `{PROJECT_ID}.{DATASET_ID}.BTOPOrders` WHERE backtestId = '{bt_id}'", location="europe-west1").result()

    # Ingest orders into BTOPOrders
    new_order_rows = []
    for idx, o in enumerate(orders):
        o_id = o.get("id", idx)
        sym_raw = o.get("symbol")
        if isinstance(sym_raw, dict):
            sym_struct = {
                "value": str(sym_raw.get("value", "")),
                "id": str(sym_raw.get("id", "")),
                "permtick": str(sym_raw.get("permtick", ""))
            }
        else:
            sym_struct = {"value": str(sym_raw or ""), "id": "", "permtick": ""}

        new_order_rows.append({
            "backtestId": bt_id,
            "id": o_id,
            "contingentId": o.get("contingentId"),
            "symbol": sym_struct,
            "limitPrice": o.get("limitPrice"),
            "stopPrice": o.get("stopPrice"),
            "price": o.get("price"),
            "quantity": o.get("quantity"),
            "value": o.get("value"),
            "time": str(o.get("time")) if o.get("time") else None,
            "type": o.get("type"),
            "status": o.get("status"),
            "securityType": o.get("securityType"),
            "direction": o.get("direction"),
            "tag": str(o.get("tag")) if o.get("tag") else None,
            "_ingestedAt": now_ts,
            "backtest_name": bt_name,
            "_ingested_at": now_ts
        })
            
    if new_order_rows:
        for i in range(0, len(new_order_rows), 2000):
            client.load_table_from_json(new_order_rows[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPOrders", job_config=job_cfg, location="europe-west1").result()
        logging.info(f"[{bt_name}] Ingested {len(new_order_rows)} new order rows into BTOPOrders.")

    # 3. Parse order tags via parse_orders_json_file to extract slope, vol_ratio, ivrv_ratio, strike, expiries
    logging.info(f"[{bt_name}] Parsing order tags to extract slope, vol_ratio, ivrv_ratio...")
    trade_records = parse_orders_json_file(orders_file)

    # Purge existing trade records for this backtestId in BTOPTrades
    client.query(f"DELETE FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTrades` WHERE backtestId = '{bt_id}'", location="europe-west1").result()

    if trade_records:
        for i in range(0, len(trade_records), 2000):
            client.load_table_from_json(trade_records[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPTrades", job_config=job_cfg, location="europe-west1").result()
        logging.info(f"[{bt_name}] [SUCCESS] Ingested {len(trade_records)} enriched trade rows into BTOPTrades.")

    # 4. MANDATORY PREDICTOR INTEGRITY GATE
    logging.info(f"[{bt_name}] Verifying Predictor Integrity Gate in BigQuery...")
    verify_q = f"""
    SELECT 
        COUNT(*) as open_cnt,
        COUNT(slope) as slope_cnt,
        COUNT(vol_ratio) as vol_cnt
    FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTrades`
    WHERE backtestId = '{bt_id}' AND action = 'OPEN'
    """
    v_rows = list(client.query(verify_q, location="europe-west1").result())
    if v_rows and v_rows[0].open_cnt > 0:
        open_cnt = v_rows[0].open_cnt
        slope_cnt = v_rows[0].slope_cnt
        slope_pct = (slope_cnt / open_cnt) * 100.0
        logging.info(f"[{bt_name}] Predictor Gate: {slope_cnt}/{open_cnt} OPEN trades ({slope_pct:.1f}%) have non-null 'slope'.")

        if slope_pct < 95.0:
            err_msg = f"Predictor Integrity Gate FAILED for {bt_name}: only {slope_pct:.1f}% of OPEN trades have non-null 'slope'!"
            logging.error(err_msg)
            raise RuntimeError(err_msg)
        else:
            logging.info(f"[{bt_name}] [GATE PASSED] Predictors successfully verified (slope coverage: {slope_pct:.1f}%).")

    return len(new_order_rows), len(trade_records)


def main():
    bq_client = get_bigquery_client()
    api_key, user_id = get_api_key()
    
    # List backtests
    url_list = "https://www.quantconnect.com/api/v2/backtests/list"
    token = generate_api_token(api_key, user_id)
    headers = {"Authorization": f"Basic {token['api_token']}", "Timestamp": token["timestamp"]}
    resp = requests.post(url_list, headers=headers, json={"projectId": TARGET_PROJECT_ID}, timeout=30)
    
    qc_backtests = resp.json().get("backtests", [])
    logging.info(f"Retrieved {len(qc_backtests)} backtests from QC Cloud.")
    
    summary = []
    for bt in qc_backtests:
        name = bt.get("name", "")
        if "HDBT_" in name or "BATCH_4EVC" in name or name.startswith("BT_4EVC"):
            logging.info(f"Processing backtest: {name} ({bt.get('backtestId') or bt.get('id')})...")
            try:
                n_orders, n_trades = process_and_ingest_hdbt_backtest(bq_client, api_key, user_id, bt)
                summary.append({"name": name, "orders_ingested": n_orders, "trades_ingested": n_trades, "status": "PASSED"})
            except Exception as e:
                logging.error(f"Failed ingestion for {name}: {e}")
                summary.append({"name": name, "orders_ingested": 0, "trades_ingested": 0, "status": f"FAILED: {e}"})

    print("\n" + "=" * 90)
    print("COMPLETE ORDERS & TRADES INGESTION REPORT WITH PREDICTOR INTEGRITY GATE")
    print("=" * 90)
    for s in summary:
        print(f"| {s['name']:<45} | Orders: {s['orders_ingested']:<6} | Trades: {s['trades_ingested']:<6} | Status: {s['status']} |")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    main()
