"""
log_trades_uploader.py
======================
Parses QuantConnect backtest log text files (log.txt) for [BIGQUERY_TRADE_RECORD]
JSON payloads and streams them into BigQuery table `bav-personal-cloud.develop.BTOPTrades`.

Usage:
    poetry run python Scripts/BigQuery/log_trades_uploader.py
"""

from __future__ import annotations

import json
import os
import sys
import datetime as dt
from typing import List, Set
from google.cloud import bigquery

# Ensure current BigQuery directory is in sys.path for db_operator imports
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client  # noqa: E402

_WORKSPACE_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
_LIBRARY_DIR = os.path.join(_WORKSPACE_DIR, "Library")
for path_dir in [_WORKSPACE_DIR, _LIBRARY_DIR]:
    if path_dir not in sys.path:
        sys.path.insert(0, path_dir)

from PropietaryCode import normalize_exit_reason

PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"
TABLE_NAME: str = "BTOPTrades"

SCHEMA = [
    bigquery.SchemaField(
        "pk", "STRING", mode="REQUIRED", 
        description="Unique Event Primary Key formatted as <backtestId>_<underlying>_<sequence_id>_<action>."
    ),
    bigquery.SchemaField(
        "trade_id", "STRING", mode="NULLABLE", 
        description="Composite Lifecycle Key formatted as <backtestId>_<underlying>_<sequence_id> shared between OPEN and CLOSE events."
    ),
    bigquery.SchemaField(
        "backtestId", "STRING", mode="REQUIRED", 
        description="Foreign Key identifying the specific cloud or local backtest run."
    ),
    bigquery.SchemaField(
        "algo_code", "STRING", mode="REQUIRED", 
        description="Short code identifying the active strategy (e.g. 4EVC, 0AT, 1SAOP)."
    ),
    bigquery.SchemaField(
        "timestamp", "TIMESTAMP", mode="REQUIRED", 
        description="UTC timestamp of the trade event."
    ),
    bigquery.SchemaField(
        "underlying", "STRING", mode="REQUIRED", 
        description="Ticker symbol of the underlying equity or option asset."
    ),
    bigquery.SchemaField(
        "action", "STRING", mode="REQUIRED", 
        description="Action type: OPEN or CLOSE."
    ),
    bigquery.SchemaField(
        "qty", "INTEGER", mode="REQUIRED", 
        description="Number of contracts or shares traded."
    ),
    bigquery.SchemaField(
        "strike", "FLOAT", mode="NULLABLE", 
        description="Strike price of the option legs (null if equity)."
    ),
    bigquery.SchemaField(
        "near_expiry", "DATE", mode="NULLABLE", 
        description="Expiration date of the front/near option leg."
    ),
    bigquery.SchemaField(
        "far_expiry", "DATE", mode="NULLABLE", 
        description="Expiration date of the back/far option leg."
    ),
    bigquery.SchemaField(
        "vol_ratio", "FLOAT", mode="NULLABLE", 
        description="Front-to-back IV ratio at entry."
    ),
    bigquery.SchemaField(
        "slope", "FLOAT", mode="NULLABLE", 
        description="Implied volatility term structure slope at entry."
    ),
    bigquery.SchemaField(
        "ivrv_ratio", "FLOAT", mode="NULLABLE", 
        description="IV to Realized Volatility ratio at entry."
    ),
    bigquery.SchemaField(
        "entry_price", "FLOAT", mode="NULLABLE", 
        description="Price/debit paid when the trade was opened."
    ),
    bigquery.SchemaField(
        "exit_price", "FLOAT", mode="NULLABLE", 
        description="Price/credit received when the trade was closed (0.0 if open)."
    ),
    bigquery.SchemaField(
        "pnl", "FLOAT", mode="NULLABLE", 
        description="Realized return percentage of the trade (0.0 if open)."
    ),
    bigquery.SchemaField(
        "exit_reason", "STRING", mode="NULLABLE",
        description="Normalized exit category for CLOSE records. One of: Stop Loss, Take Profit, Time Exit, DTE Safety, Signal Exit, Risk Exit, Other."
    ),
    bigquery.SchemaField(
        "parameters", "STRING", mode="NULLABLE", 
        description="JSON-serialized string containing custom parameters, indicators, and metrics specific to that algorithm."
    ),
    bigquery.SchemaField(
        "mae_pct", "FLOAT", mode="NULLABLE", 
        description="Maximum Adverse Excursion percentage (worst unrealized drawdown %) during holding."
    ),
    bigquery.SchemaField(
        "mfe_pct", "FLOAT", mode="NULLABLE", 
        description="Maximum Favorable Excursion percentage (peak unrealized gain %) during holding."
    ),
    bigquery.SchemaField(
        "earnings_date", "DATE", mode="NULLABLE", 
        description="Scheduled earnings announcement date for the underlying stock."
    ),
    bigquery.SchemaField(
        "batch_id", "STRING", mode="NULLABLE", 
        description="Unique identifier for multi-chunk batch executions (e.g. BATCH_4EVC_V1_2022_2024)."
    ),
    bigquery.SchemaField(
        "chunk_index", "INTEGER", mode="NULLABLE", 
        description="Sequential index of the date-chunk within a multi-year batch run."
    ),
    bigquery.SchemaField(
        "backtest_name", "STRING", mode="NULLABLE", 
        description="Human-readable name assigned to the backtest (e.g. BT_4EVC_V1_20251127_210419)."
    ),
    bigquery.SchemaField(
        "_ingested_at", "TIMESTAMP", mode="NULLABLE", 
        default_value_expression="CURRENT_TIMESTAMP()",
        description="UTC timestamp tracking when the row was ingested into BigQuery."
    ),
]


def ensure_table_exists(client: bigquery.Client, project_id: str, dataset_id: str) -> None:
    table_id = f"{project_id}.{dataset_id}.{TABLE_NAME}"
    try:
        table = client.get_table(table_id)
        existing_field_names = {f.name for f in table.schema}
        new_fields = [f for f in SCHEMA if f.name not in existing_field_names]
        if new_fields:
            table.schema = list(table.schema) + new_fields
            client.update_table(table, ["schema"])
            print(f"Updated schema for table {TABLE_NAME} with new fields: {[f.name for f in new_fields]}")
        else:
            print(f"Table {TABLE_NAME} already exists in dataset '{dataset_id}'.")
    except Exception:
        print(f"Table {TABLE_NAME} does not exist. Creating...")
        table = bigquery.Table(table_id, schema=SCHEMA)
        client.create_table(table)
        print(f"Created table {table_id}.")


def get_existing_records(client: bigquery.Client, project_id: str, dataset_id: str) -> Set[tuple[str, str]]:
    table_id = f"{project_id}.{dataset_id}.{TABLE_NAME}"
    query = f"SELECT pk, action FROM `{table_id}`"
    try:
        query_job = client.query(query)
        results = query_job.result()
        return {(row.pk, row.action) for row in results}
    except Exception as e:
        print(f"Could not check existing records (table might be new): {e}")
        return set()


def sanitize_record(row: dict) -> dict:
    if "backtest_run_id" in row and "backtestId" not in row:
        row["backtestId"] = row["backtest_run_id"]
    allowed = {f.name for f in SCHEMA}
    clean = {k: v for k, v in row.items() if k in allowed and k != "earnings_date"}
    if "earnings_date" in row and row["earnings_date"]:
        try:
            params = json.loads(clean.get("parameters") or "{}")
            params["earnings_date"] = row["earnings_date"]
            clean["parameters"] = json.dumps(params, separators=(',', ':'))
        except Exception:
            pass
    return clean


def normalize_timestamp(raw_ts: Any) -> str:
    """Normalizes raw timestamp values (epoch seconds/ms, ISO strings) into ISO-8601 UTC string."""
    if not raw_ts:
        return dt.datetime.now(dt.timezone.utc).isoformat()
        
    if isinstance(raw_ts, (int, float)):
        ts_val = float(raw_ts)
        if ts_val > 1e11:
            ts_val /= 1000.0
        return dt.datetime.fromtimestamp(ts_val, tz=dt.timezone.utc).isoformat()
        
    if isinstance(raw_ts, str):
        cleaned = raw_ts.strip()
        if cleaned.replace('.', '', 1).isdigit():
            ts_val = float(cleaned)
            if ts_val > 1e11:
                ts_val /= 1000.0
            return dt.datetime.fromtimestamp(ts_val, tz=dt.timezone.utc).isoformat()
        return cleaned
        
    return str(raw_ts)


def normalize_exit_reason(tag: str) -> str:
    """Extracts human-readable exit reason from QuantConnect order tag."""
    if not tag:
        return "Unknown Exit"
    if "CLOSE:" in tag:
        parts = tag.split("CLOSE:")
        if len(parts) > 1:
            raw_reason = parts[1].split(":")[0]
            return raw_reason.strip()
    if "End-of-Backtest Liquidation" in tag:
        return "End-of-Backtest Liquidation"
    if "Time-Based Exit" in tag:
        return "Time-Based Exit"
    if "Stop Loss" in tag:
        return "Emergency Stop Loss"
    return tag


def parse_log_file(file_path: str) -> List[dict]:
    """Reads a log file and extracts BIGQUERY_TRADE_RECORD JSON payloads."""
    rows = []
    if not os.path.exists(file_path):
        return rows
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if "[BIGQUERY_TRADE_RECORD]" in line:
                try:
                    parts = line.split("[BIGQUERY_TRADE_RECORD] ")
                    if len(parts) == 2:
                        payload = json.loads(parts[1].strip())
                        if "timestamp" in payload:
                            raw_ts = payload["timestamp"]
                            if isinstance(raw_ts, (int, float)) and raw_ts > 0:
                                if raw_ts > 1e14:
                                    payload["timestamp"] = dt.datetime.fromtimestamp(raw_ts / 1e6, tz=dt.timezone.utc).isoformat()
                                elif raw_ts > 1e11:
                                    payload["timestamp"] = dt.datetime.fromtimestamp(raw_ts / 1e3, tz=dt.timezone.utc).isoformat()
                                else:
                                    payload["timestamp"] = dt.datetime.fromtimestamp(raw_ts, tz=dt.timezone.utc).isoformat()
                        rows.append(sanitize_record(payload))
                except Exception as e:
                    print(f"Error parsing line in {file_path}: {e}")
    return rows


def parse_object_store_file(file_path: str) -> List[dict]:
    """Reads a QuantConnect ObjectStore JSON file containing a list of trade records."""
    rows = []
    if not os.path.exists(file_path):
        return rows
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                rows = data
    except Exception as e:
        print(f"Error reading ObjectStore JSON file {file_path}: {e}")
    return rows


def _extract_expiry_from_symbol(symbol_val: str) -> str | None:
    """
    Extracts the expiration date from a QuantConnect option symbol string.
    QC option symbols follow the format: 'TICKER  YYMMDD[C/P]STRIKE'
    e.g. 'BKU   230217C00035000' -> '2023-02-17'
    Returns None if the symbol does not match the expected pattern.
    """
    import re
    if not symbol_val:
        return None
    # QC option symbol: letters + spaces + 6-digit date + C/P + strike
    match = re.search(r'(\d{6})[CP]', symbol_val)
    if match:
        yymmmdd = match.group(1)  # e.g. '230217'
        try:
            return dt.datetime.strptime(yymmmdd, "%y%m%d").strftime("%Y-%m-%d")
        except ValueError:
            return None
    return None


def _resolve_algo_code(backtest_run_id: str) -> str:
    """
    Dynamically extracts algorithm short name (e.g. 0AT, 4EVC) from backtest name.
    Follows project naming convention: 'BT_{algo_code}_V...'
    """
    # 1. Direct parse if backtest_run_id follows BT_{algo}_... naming
    if backtest_run_id.startswith("BT_") and "_" in backtest_run_id:
        parts = backtest_run_id.split("_")
        if len(parts) > 1:
            return parts[1]

    # 2. Look up backtest results JSON to extract full backtest name
    workspace_root = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
    for folder in ["backtest_results", "already_uploaded_backtest_results"]:
        json_path = os.path.join(workspace_root, "Scripts", folder, f"{backtest_run_id}.json")
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                bt_dict = data.get("backtest", {}) if isinstance(data, dict) else {}
                bt_name = str(bt_dict.get("name") or data.get("name") or "")
                if bt_name.startswith("BT_") and "_" in bt_name:
                    parts = bt_name.split("_")
                    if len(parts) > 1:
                        return parts[1]
            except Exception:
                pass

    return "UNKNOWN"


def parse_orders_json_file(file_path: str) -> List[dict]:
    """
    Parses QuantConnect orders JSON file (orders_results/<id>_orders.json)
    and reconstructs OPEN and CLOSE trade records for BigQuery ingestion.

    Correctly handles combo/spread orders via groupOrderManager:
    - OPEN records: 1 record per combo group (entry spread). The LONG leg provides
      expiry metadata; groupOrderManager.limitPrice is the spread entry price.
    - CLOSE records: 1 record per underlying close event. Detected via the
      'CLOSE:' or 'FLATTEN:' tag prefix on individual market orders; front+back
      close legs are deduplicated into a single CLOSE record per underlying.
    - Underlying is extracted from the tag JSON key 'u' (not the option contract ticker).
    """
    rows: List[dict] = []
    if not os.path.exists(file_path):
        return rows
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        if isinstance(raw_data, dict):
            orders = raw_data.get("orders") or raw_data.get("Orders") or raw_data
        elif isinstance(raw_data, list):
            orders = raw_data
        else:
            orders = []

        flat_orders = []
        if isinstance(orders, dict):
            orders = list(orders.values())
        if isinstance(orders, list):
            for item in orders:
                if isinstance(item, list):
                    flat_orders.extend(item)
                elif isinstance(item, dict):
                    flat_orders.append(item)
        orders = flat_orders

        backtest_run_id = os.path.basename(file_path).replace("_orders.json", "")
        algo_code = _resolve_algo_code(backtest_run_id)

        # open_queues: underlying -> FIFO list of open_records
        # Supports multiple sequential trades for the same underlying within one backtest.
        open_queues: dict = {}  # underlying -> [open_record, ...] (oldest first)
        trade_counter = 0

        # ------------------------------------------------------------------ #
        # Pass 1: Separate filled orders into combo legs vs individual orders  #
        # ------------------------------------------------------------------ #
        combo_legs: dict = {}         # gom_id -> list of leg orders
        individual_orders: list = []  # orders without groupOrderManager

        for order in orders:
            status = order.get("status")
            if status not in [3, "filled", "Filled"]:
                continue

            gom = order.get("groupOrderManager")
            if gom:
                gom_id = gom.get("id")
                if gom_id not in combo_legs:
                    combo_legs[gom_id] = []
                combo_legs[gom_id].append(order)
            else:
                individual_orders.append(order)

        # ------------------------------------------------------------------ #
        # Pass 2: Emit OPEN records — one per combo group (entry spread)       #
        # ------------------------------------------------------------------ #
        for gom_id, legs in combo_legs.items():
            # Identify LONG leg (far / back) and SHORT leg (near / front)
            long_leg = next((l for l in legs if l.get("quantity", 0) > 0), None)
            short_leg = next((l for l in legs if l.get("quantity", 0) < 0), None)

            if long_leg is None:
                continue  # malformed group, skip

            # Use LONG leg for timestamp and tag metadata
            raw_ts = long_leg.get("time", "")
            timestamp = normalize_timestamp(raw_ts)
            raw_tag = long_leg.get("tag", "")

            tag_data: dict = {}
            if isinstance(raw_tag, str) and raw_tag.startswith("{") and raw_tag.endswith("}"):
                try:
                    tag_data = json.loads(raw_tag)
                except Exception:
                    tag_data = {}

            # Extract underlying from tag JSON key "u"; fallback to symbol value
            underlying = str(tag_data.get("u", long_leg.get("symbol", {}).get("value", "UNKNOWN")))

            # Use groupOrderManager limitPrice as the spread entry price
            gom = long_leg.get("groupOrderManager", {})
            entry_price = round(float(gom.get("limitPrice", long_leg.get("price", 0.0))), 5)
            qty = int(abs(gom.get("quantity", long_leg.get("quantity", 0))))

            slope_val = float(tag_data["slope"]) if "slope" in tag_data else None
            ivrv_val = float(tag_data.get("ivrv_ratio") or tag_data.get("ivrv") or 0.0) if ("ivrv" in tag_data or "ivrv_ratio" in tag_data) else None
            vol_val = float(tag_data["vol_ratio"]) if "vol_ratio" in tag_data else None
            strike_val = float(tag_data["k"]) if "k" in tag_data else None
            near_val = str(tag_data["near"]) if "near" in tag_data else (
                _extract_expiry_from_symbol(short_leg.get("symbol", {}).get("value", "")) if short_leg else None
            )
            far_val = str(tag_data["far"]) if "far" in tag_data else (
                _extract_expiry_from_symbol(long_leg.get("symbol", {}).get("value", ""))
            )

            trade_counter += 1
            trade_id = f"CLOUD_{backtest_run_id}_{underlying}_{trade_counter}"
            pk = f"{trade_id}_OPEN"
            open_record = {
                "pk": pk,
                "trade_id": trade_id,
                "backtestId": backtest_run_id,
                "algo_code": algo_code,
                "timestamp": timestamp,
                "underlying": underlying,
                "action": "OPEN",
                "qty": qty,
                "strike": strike_val,
                "near_expiry": near_val,
                "far_expiry": far_val,
                "vol_ratio": vol_val,
                "slope": slope_val,
                "ivrv_ratio": ivrv_val,
                "entry_price": entry_price,
                "exit_price": 0.0,
                "pnl": 0.0,
                "exit_reason": "",
                "parameters": json.dumps(tag_data, separators=(',', ':')) if tag_data else "{}",
            }
            open_queues.setdefault(underlying, []).append(open_record)
            rows.append(open_record)

        # ------------------------------------------------------------------ #
        # Pass 3: Emit CLOSE records from individual (non-combo) orders        #
        # ------------------------------------------------------------------ #
        close_groups: dict = {}  # underlying -> list of close legs, sorted chrono

        for order in individual_orders:
            raw_tag = str(order.get("tag", ""))
            is_tagged_close = raw_tag.startswith("CLOSE:") or "FLATTEN" in raw_tag
            if is_tagged_close:
                # Extract underlying from tag JSON key "u" if available; fallback to symbol value
                tag_data: dict = {}
                if raw_tag.startswith("{") and raw_tag.endswith("}"):
                    try:
                        tag_data = json.loads(raw_tag)
                    except Exception:
                        tag_data = {}
                und = str(tag_data.get("u", order.get("symbol", {}).get("value", "UNKNOWN")))
                close_groups.setdefault(und, []).append(order)

        # For each underlying, pair close legs chronologically with open records
        for underlying, open_recs in open_queues.items():
            legs = close_groups.get(underlying, [])
            if not legs:
                continue

            # Sort close legs by fill time
            legs = sorted(legs, key=lambda o: o.get("time", ""))

            # Group legs by close event timestamp (legs within 5 seconds belong to same exit)
            event_groups: list = []
            current_group: list = []
            last_ts_val = None

            for leg in legs:
                raw_ts = leg.get("time", "")
                ts_str = normalize_timestamp(raw_ts)
                if last_ts_val is None:
                    current_group.append(leg)
                    last_ts_val = ts_str
                else:
                    # check time diff
                    try:
                        t1 = dt.datetime.fromisoformat(last_ts_val.replace("Z", "+00:00"))
                        t2 = dt.datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                        if abs((t2 - t1).total_seconds()) <= 5:
                            current_group.append(leg)
                        else:
                            event_groups.append(current_group)
                            current_group = [leg]
                            last_ts_val = ts_str
                    except Exception:
                        current_group.append(leg)

            if current_group:
                event_groups.append(current_group)

            # Pair each exit event group with the oldest open_record
            for event_legs in event_groups:
                if not open_queues[underlying]:
                    break  # no more open trades to close

                rep_leg = event_legs[0]
                timestamp = normalize_timestamp(rep_leg.get("time", ""))
                prices = [float(l.get("price", 0.0)) for l in event_legs if float(l.get("price", 0.0)) > 0]
                exit_price = round(sum(prices) / len(prices), 5) if prices else 0.0
                exit_reason = normalize_exit_reason(str(rep_leg.get("tag", "")))

                open_rec = open_queues[underlying].pop(0)
                trade_id = open_rec.get("trade_id") or open_rec["pk"].replace("_OPEN", "")
                pk = f"{trade_id}_CLOSE"
                entry_price = open_rec["entry_price"]

                net_close_credit = 0.0
                for leg in event_legs:
                    p = float(leg.get("price", 0.0))
                    q = float(leg.get("quantity", 0))
                    if q < 0:
                        net_close_credit += p  # selling leg (credit)
                    else:
                        net_close_credit -= p  # buying back leg (debit)

                if net_close_credit != 0.0:
                    realized_pnl = (net_close_credit - entry_price) / entry_price if entry_price > 0 else 0.0
                else:
                    realized_pnl = (exit_price - entry_price) / entry_price if entry_price > 0 else 0.0

                pnl = round(realized_pnl, 5)

                close_record = {
                    "pk": pk,
                    "trade_id": trade_id,
                    "backtestId": backtest_run_id,
                    "algo_code": open_rec["algo_code"],
                    "timestamp": timestamp,
                    "underlying": underlying,
                    "action": "CLOSE",
                    "qty": open_rec["qty"],
                    "strike": open_rec["strike"],
                    "near_expiry": open_rec["near_expiry"],
                    "far_expiry": open_rec["far_expiry"],
                    "vol_ratio": open_rec["vol_ratio"],
                    "slope": open_rec["slope"],
                    "ivrv_ratio": open_rec["ivrv_ratio"],
                    "entry_price": entry_price,
                    "exit_price": exit_price,
                    "pnl": pnl,
                    "exit_reason": exit_reason,
                    "parameters": open_rec["parameters"],
                }
                rows.append(close_record)

    except Exception as e:
        print(f"Error parsing orders JSON file {file_path}: {e}")
        import traceback
        traceback.print_exc()

    return rows


def cleanup_processed_object_store_files(object_store_files: List[str]) -> None:
    """
    Cleans up local ObjectStore JSON files after successful BigQuery upload
    by archiving them to Scripts/already_uploaded_backtest_results/ to prevent disk clutter.
    """
    if not object_store_files:
        return
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archive_dir = os.path.abspath(os.path.join(script_dir, "..", "already_uploaded_backtest_results"))
    os.makedirs(archive_dir, exist_ok=True)

    for file_path in object_store_files:
        try:
            if os.path.exists(file_path):
                base_name = os.path.basename(file_path)
                dest_path = os.path.join(archive_dir, base_name)
                # Overwrite if exists in archive
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                os.rename(file_path, dest_path)
                print(f"[Cleanup] Archived local ObjectStore payload: {base_name}")
        except Exception as err:
            print(f"[Cleanup Warning] Could not archive {file_path}: {err}")


def upload_trade_records(trade_records: List[dict] | None = None) -> None:
    client = get_bigquery_client(project_id=PROJECT_ID)
    ensure_table_exists(client, PROJECT_ID, DATASET_ID)
    
    existing_ids = get_existing_records(client, PROJECT_ID, DATASET_ID)
    print(f"Fetched {len(existing_ids)} existing (pk, action) records from BigQuery.")

    new_rows = []
    if trade_records:
        for row in trade_records:
            if isinstance(row, dict) and "pk" in row and "action" in row:
                key = (row["pk"], row["action"])
                if key not in existing_ids:
                    if "backtest_run_id" in row and "backtestId" not in row:
                        row["backtestId"] = row.pop("backtest_run_id")
                    new_rows.append(row)
                    existing_ids.add(key)

    log_files: List[str] = []
    object_store_files: List[str] = []
    orders_json_files: List[str] = []
    
    # Dynamically scan backtests directories across ALL algorithm folders in project root
    workspace_root = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
    for item in os.listdir(workspace_root):
        algo_dir = os.path.join(workspace_root, item)
        backtests_dir = os.path.join(algo_dir, "backtests")
        if os.path.isdir(backtests_dir):
            for root, dirs, files in os.walk(backtests_dir):
                for file in files:
                    if file == "log.txt" or file.endswith("-log.txt"):
                        log_files.append(os.path.join(root, file))
                    elif file.startswith("BTOPTrades_") and file.endswith(".json"):
                        object_store_files.append(os.path.join(root, file))

    # Scan dedicated backtest_logs & orders_results folders
    cloud_logs_dir = os.path.join(workspace_root, "Scripts", "backtest_logs")
    if os.path.exists(cloud_logs_dir):
        for file in os.listdir(cloud_logs_dir):
            if file.endswith(".txt") or file.endswith(".log"):
                log_files.append(os.path.join(cloud_logs_dir, file))
            elif file.startswith("BTOPTrades_") and file.endswith(".json"):
                object_store_files.append(os.path.join(cloud_logs_dir, file))

    orders_results_dir = os.path.join(workspace_root, "Scripts", "orders_results")
    archived_orders_dir = os.path.join(workspace_root, "Scripts", "already_uploaded_orders_results")
    for d in [orders_results_dir, archived_orders_dir]:
        if os.path.exists(d):
            for file in os.listdir(d):
                if file.endswith("_orders.json"):
                    orders_json_files.append(os.path.join(d, file))

    target_id = None
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if arg == "--backtest-id" and i + 1 < len(sys.argv):
                target_id = sys.argv[i + 1].strip()
                break
        if not target_id and not sys.argv[1].startswith("--"):
            target_id = sys.argv[1].strip()

    if target_id:
        orders_json_files = [f for f in orders_json_files if target_id in os.path.basename(f)]
        log_files = [f for f in log_files if target_id in os.path.basename(f)]
        object_store_files = [f for f in object_store_files if target_id in os.path.basename(f)]

    print(f"Found {len(log_files)} log files, {len(object_store_files)} ObjectStore JSON files, and {len(orders_json_files)} orders JSON files to process.")

    new_rows = []
    # 1. Parse ObjectStore JSON files (downloaded from QC API / ObjectStore)
    for file_path in object_store_files:
        parsed_rows = parse_object_store_file(file_path)
        for row in parsed_rows:
            if isinstance(row, dict) and "pk" in row and "action" in row:
                key = (row["pk"], row["action"])
                if key not in existing_ids:
                    # Normalize field name to backtestId if present
                    if "backtest_run_id" in row and "backtestId" not in row:
                        row["backtestId"] = row.pop("backtest_run_id")
                    new_rows.append(row)
                    existing_ids.add(key)

    # 2. Parse Orders JSON files (downloaded from QC API)
    for file_path in orders_json_files:
        parsed_rows = parse_orders_json_file(file_path)
        for row in parsed_rows:
            if isinstance(row, dict) and "pk" in row and "action" in row:
                key = (row["pk"], row["action"])
                if key not in existing_ids:
                    if "backtest_run_id" in row and "backtestId" not in row:
                        row["backtestId"] = row.pop("backtest_run_id")
                    new_rows.append(row)
                    existing_ids.add(key)

    if not new_rows:
        print("No new trade records to upload.")
        # Perform cleanup on processed ObjectStore files even if no new rows
        cleanup_processed_object_store_files(object_store_files)
        return

    # Resolve backtest_name for all new rows
    name_map = {}
    try:
        q_names = f"SELECT backtestId, MAX(name) AS name FROM `{PROJECT_ID}.{DATASET_ID}.BTOPResults` WHERE name IS NOT NULL AND name != '' GROUP BY backtestId"
        for r in client.query(q_names).result():
            name_map[r['backtestId']] = r['name']
    except Exception as e:
        print(f"[Warning] Failed to fetch backtest_name map: {e}")

    # Inject ingestion timestamp and backtest_name into every row
    ingested_at = dt.datetime.now(dt.timezone.utc).isoformat()
    for row in new_rows:
        row["_ingested_at"] = ingested_at
        bt_id = row.get("backtestId")
        if bt_id and not row.get("backtest_name"):
            row["backtest_name"] = name_map.get(bt_id, bt_id)

    # Use BigQuery load job (not streaming insert) to avoid the 3,650-day timestamp
    # restriction that blocks historical backtest data older than ~2016.
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}"
    print(f"Uploading {len(new_rows)} new trade records to BigQuery via load job...")

    job_config = bigquery.LoadJobConfig(
        schema=SCHEMA,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )

    # Serialize rows to newline-delimited JSON in memory
    import io
    ndjson_data = "\n".join(json.dumps(row, default=str) for row in new_rows)
    data_stream = io.BytesIO(ndjson_data.encode("utf-8"))

    load_job = client.load_table_from_file(
        data_stream,
        table_id,
        job_config=job_config,
    )
    load_job.result()  # Wait for completion

    if load_job.errors:
        print(f"Load job completed with errors ({len(load_job.errors)}): {load_job.errors[:5]}")
    else:
        print(f"Upload completed successfully. Total inserted: {len(new_rows)} rows.")
        cleanup_processed_object_store_files(object_store_files)


if __name__ == "__main__":
    upload_trade_records()
