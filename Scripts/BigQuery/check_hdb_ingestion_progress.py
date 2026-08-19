"""
check_hdb_ingestion_progress.py
================================
Checks progress of HDB order and trade ingestion in BigQuery and finishes any remaining backtests with robust HTTP retry handling.
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


def safe_post(url: str, headers: Dict[str, str], json_payload: Dict[str, Any], max_retries: int = 3, timeout: int = 60) -> requests.Response | None:
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(url, headers=headers, json=json_payload, timeout=timeout)
            if resp.status_code == 200:
                return resp
            logging.warning(f"HTTP {resp.status_code} on attempt {attempt}/{max_retries} for {url}")
        except Exception as err:
            logging.warning(f"Request exception on attempt {attempt}/{max_retries}: {err}")
        time.sleep(2 * attempt)
    return None


def get_ingested_counts_by_backtest(client: bigquery.Client) -> Dict[str, Dict[str, int]]:
    q = f"""
    SELECT backtest_run_id as bt_id, 'trades' as category, COUNT(*) as cnt
    FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTrades`
    WHERE action != 'PLACEHOLDER'
    GROUP BY bt_id
    UNION ALL
    SELECT backtestId as bt_id, 'orders' as category, COUNT(*) as cnt
    FROM `{PROJECT_ID}.{DATASET_ID}.BTOPOrders`
    GROUP BY bt_id
    UNION ALL
    SELECT backtestId as bt_id, 'closed_trades' as category, COUNT(*) as cnt
    FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades`
    WHERE tradeId NOT LIKE 'CLOSED_TRADE_%'
    GROUP BY bt_id
    """
    res = list(client.query(q).result())
    stats: Dict[str, Dict[str, int]] = {}
    for r in res:
        bt_id = r["bt_id"]
        cat = r["category"]
        cnt = r["cnt"]
        stats.setdefault(bt_id, {})[cat] = cnt
    return stats


def get_existing_trade_pks(client: bigquery.Client) -> Set[str]:
    q = f"SELECT DISTINCT pk FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTrades` WHERE pk IS NOT NULL"
    res = list(client.query(q).result())
    return {r["pk"] for r in res}


def get_existing_order_keys(client: bigquery.Client) -> Set[str]:
    q = f"SELECT DISTINCT CONCAT(backtestId, '_', CAST(id AS STRING)) as opk FROM `{PROJECT_ID}.{DATASET_ID}.BTOPOrders` WHERE backtestId IS NOT NULL"
    res = list(client.query(q).result())
    return {r["opk"] for r in res}


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
        
        resp = safe_post(url, headers, payload, max_retries=3, timeout=45)
        if not resp:
            logging.error(f"Failed to read orders for {bt_id} at start {start}")
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
        time.sleep(0.01)
            
    logging.info(f"[{bt_id}] Retrieved {len(all_orders)} total orders from QC Cloud.")
    return all_orders


def process_and_ingest_hdb_backtest(client: bigquery.Client, api_key: str, user_id: str, bt_item: Dict[str, Any], existing_trade_pks: Set[str], existing_order_keys: Set[str]) -> Tuple[int, int]:
    bt_id = bt_item.get("backtestId") or bt_item.get("id")
    bt_name = bt_item.get("name", "UNKNOWN")
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    
    token = generate_api_token(api_key, user_id)
    headers = {"Authorization": f"Basic {token['api_token']}", "Timestamp": token["timestamp"]}
    
    # 1. Fetch backtest details & closedTrades
    read_url = "https://www.quantconnect.com/api/v2/backtests/read"
    resp = safe_post(read_url, headers, {"projectId": TARGET_PROJECT_ID, "backtestId": bt_id}, max_retries=3, timeout=60)
    if not resp:
        return 0, 0
        
    bt_resp = resp.json()
    bt_data = bt_resp.get("backtest", {})
    total_perf = bt_data.get("totalPerformance", {}) or {}
    closed_trades = total_perf.get("closedTrades", []) if isinstance(total_perf, dict) else []
    
    # Ingest closed trades to BTOPTotalPerformanceClosedTrades
    job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    if closed_trades:
        ct_rows = []
        for idx, ct in enumerate(closed_trades):
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

            ct_rows.append({
                "tradeId": ct.get("id", f"{bt_id}_ct_{idx}"),
                "backtestId": bt_id,
                "symbol": sym_val[:64],
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
            try:
                client.load_table_from_json(ct_rows[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades", job_config=job_cfg).result()
            except Exception as e:
                logging.warning(f"Closed trades load warning for {bt_name}: {e}")
        logging.info(f"[{bt_name}] Ingested {len(ct_rows)} closed trades into BTOPTotalPerformanceClosedTrades.")

    # 2. Fetch all orders with pagination (step=100)
    orders = fetch_all_orders_for_backtest(api_key, user_id, bt_id)
    
    # Ingest orders into BTOPOrders
    new_order_rows = []
    for idx, o in enumerate(orders):
        o_id = o.get("id", idx)
        order_key = f"{bt_id}_{o_id}"
        if order_key not in existing_order_keys:
            existing_order_keys.add(order_key)
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
            try:
                client.load_table_from_json(new_order_rows[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPOrders", job_config=job_cfg).result()
            except Exception as e:
                logging.warning(f"Orders load warning for {bt_name}: {e}")
        logging.info(f"[{bt_name}] Ingested {len(new_order_rows)} new order rows into BTOPOrders.")

    # 3. Parse orders into trade rows for BTOPTrades
    trade_rows = []
    open_positions = {}
    counter = 0

    batch_id = bt_name.rsplit("_Y", 1)[0] if "_Y" in bt_name else bt_name
    chunk_index = int(bt_name[-4:]) if bt_name[-4:].isdigit() else 1

    for o in orders:
        sym_raw = o.get("symbol")
        if isinstance(sym_raw, dict):
            sym = str(sym_raw.get("value") or sym_raw.get("permtick") or "UNKNOWN")
        else:
            sym = str(sym_raw or "UNKNOWN")

        qty = o.get("quantity", 0)
        price = o.get("price", 0.0)
        ts = o.get("time", "")

        if qty > 0:
            counter += 1
            pk = f"CLOUD_{bt_id}_{sym}_{counter}"
            rec = {
                "pk": pk, "backtest_run_id": bt_id, "algo_code": "4EVC",
                "timestamp": ts, "underlying": sym[:32], "action": "OPEN", "qty": int(qty),
                "entry_price": round(float(price), 5), "exit_price": 0.0, "pnl": 0.0,
                "batch_id": batch_id, "chunk_index": chunk_index, "backtest_name": bt_name, "_ingested_at": now_ts
            }
            open_positions[sym] = rec
            trade_rows.append(rec)
        elif qty < 0 and sym in open_positions:
            open_rec = open_positions.pop(sym)
            entry_p = open_rec["entry_price"]
            exit_p = round(float(price), 5)
            pnl = round((exit_p - entry_p) / entry_p, 5) if entry_p > 0 else 0.0
            trade_rows.append({
                "pk": open_rec["pk"], "backtest_run_id": bt_id, "algo_code": "4EVC",
                "timestamp": ts, "underlying": sym[:32], "action": "CLOSE", "qty": int(abs(qty)),
                "entry_price": entry_p, "exit_price": exit_p, "pnl": pnl,
                "batch_id": batch_id, "chunk_index": chunk_index, "backtest_name": bt_name, "_ingested_at": now_ts
            })

    new_trade_rows = []
    for r in trade_rows:
        if r["pk"] not in existing_trade_pks:
            existing_trade_pks.add(r["pk"])
            new_trade_rows.append(r)

    if new_trade_rows:
        for i in range(0, len(new_trade_rows), 2000):
            try:
                client.load_table_from_json(new_trade_rows[i:i+2000], f"{PROJECT_ID}.{DATASET_ID}.BTOPTrades", job_config=job_cfg).result()
            except Exception as e:
                logging.warning(f"Trades load warning for {bt_name}: {e}")
        logging.info(f"[{bt_name}] [SUCCESS] Ingested {len(new_trade_rows)} trade rows into BTOPTrades.")

    return len(new_order_rows), len(new_trade_rows)


def main():
    bq_client = get_bigquery_client()
    api_key, user_id = get_api_key()
    
    ingested_stats = get_ingested_counts_by_backtest(bq_client)
    existing_trade_pks = get_existing_trade_pks(bq_client)
    existing_order_keys = get_existing_order_keys(bq_client)
    
    # List backtests
    url_list = "https://www.quantconnect.com/api/v2/backtests/list"
    token = generate_api_token(api_key, user_id)
    headers = {"Authorization": f"Basic {token['api_token']}", "Timestamp": token["timestamp"]}
    resp = safe_post(url_list, headers, {"projectId": TARGET_PROJECT_ID}, max_retries=3, timeout=30)
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
            stats = ingested_stats.get(bt_id, {})
            n_trades_in_bq = stats.get("trades", 0)
            n_orders_in_bq = stats.get("orders", 0)
            
            # If already has orders & trades in BQ, report as complete
            if n_trades_in_bq > 0 and n_orders_in_bq > 0:
                report.append({"name": name, "bt_id": bt_id, "orders_bq": n_orders_in_bq, "trades_bq": n_trades_in_bq, "status": "ALREADY_INGESTED"})
                continue
                
            logging.info(f"Processing remaining HDB run: {name} ({bt_id})...")
            n_orders, n_trades = process_and_ingest_hdb_backtest(bq_client, api_key, user_id, bt, existing_trade_pks, existing_order_keys)
            report.append({"name": name, "bt_id": bt_id, "orders_bq": n_orders_in_bq + n_orders, "trades_bq": n_trades_in_bq + n_trades, "status": "NEWLY_INGESTED"})

    print("\n" + "=" * 95)
    print("HDB BACKTEST ORDERS & TRADES INGESTION AUDIT REPORT")
    print("=" * 95)
    print(f"| {'Backtest Name':<42} | {'Orders in BQ':<12} | {'Trades in BQ':<12} | {'Status':<16} |")
    print("| " + "-"*42 + " | " + "-"*12 + " | " + "-"*12 + " | " + "-"*16 + " |")
    for r in report:
        print(f"| {r['name']:<42} | {r['orders_bq']:<12} | {r['trades_bq']:<12} | {r['status']:<16} |")
    print("=" * 95 + "\n")


if __name__ == "__main__":
    main()
