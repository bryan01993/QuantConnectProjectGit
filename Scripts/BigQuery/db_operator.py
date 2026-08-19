from __future__ import annotations

import argparse
import datetime as dt
from typing import Any, Dict, List, Optional, Callable, Union, Iterable
import json
import os
import tempfile
import time
import sys

from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPICallError, RetryError, ServiceUnavailable
from requests.exceptions import SSLError as RequestsSSLError
from google.oauth2 import service_account
import shutil


def safe_move(src: str, dst: str) -> None:
    """Move src → dst; if dst exists, append a timestamp."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        base, ext = os.path.splitext(dst)
        dst = f"{base}_{int(time.time())}{ext}"
    shutil.move(src, dst)
    print(f"File moved to {dst}")


_CLOCK_SKEW_SYNCED = False


def sync_clock_skew_if_needed() -> None:
    """
    Checks for network time skew against Google HTTP endpoints.
    If local system time is skewed by > 15 seconds, monkey-patches
    google.auth._helpers.utcnow so JWT authentication succeeds.
    """
    global _CLOCK_SKEW_SYNCED
    if _CLOCK_SKEW_SYNCED:
        return

    try:
        import urllib.request
        import urllib.error
        import datetime
        import email.utils
        import google.auth._helpers
        import google.oauth2.service_account

        date_hdr = None
        try:
            with urllib.request.urlopen("https://www.google.com", timeout=3) as resp:
                date_hdr = resp.headers.get("date")
        except urllib.error.HTTPError as e:
            date_hdr = e.headers.get("date")

        if date_hdr:
            server_dt = email.utils.parsedate_to_datetime(date_hdr)
            local_dt = datetime.datetime.now(datetime.timezone.utc)
            skew = server_dt - local_dt
            if abs(skew.total_seconds()) > 15:
                if not hasattr(google.auth._helpers, "_unpatched_utcnow"):
                    google.auth._helpers._unpatched_utcnow = google.auth._helpers.utcnow
                base_utcnow = google.auth._helpers._unpatched_utcnow
                fixed_utcnow = lambda: base_utcnow() + skew
                google.auth._helpers.utcnow = fixed_utcnow
                google.oauth2.service_account._helpers.utcnow = fixed_utcnow
                print(f"[TIME SYNC] Automatically compensated for system clock skew ({skew.total_seconds():.1f}s)")
            _CLOCK_SKEW_SYNCED = True
    except Exception as err:
        print(f"[TIME SYNC WARN] Clock sync check failed: {err}")


def get_bigquery_client(project_id: Optional[str] = None) -> bigquery.Client:
    """
    Returns a BigQuery client.
    First checks for a Service Account key in Resources/gcp_keys.json.
    If found, uses it. Otherwise, falls back to Application Default Credentials.
    """
    sync_clock_skew_if_needed()

    if not project_id:
        project_id = os.getenv("BIGQUERY_PROJECT", "bav-personal-cloud")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming Resources is at the project root: Scripts/BigQuery/../../Resources
    key_path = os.path.abspath(os.path.join(script_dir, "..", "..", "Resources", "gcp_keys.json"))

    if os.path.exists(key_path):
        print(f"Authenticating with service account key: {key_path}")
        credentials = service_account.Credentials.from_service_account_file(key_path)
        return bigquery.Client(project=project_id, credentials=credentials)
    else:
        print(f"Authenticating with Application Default Credentials (ADC) for project: {project_id}")
        return bigquery.Client(project=project_id)


def guess_backtest_id_from_filename(file_name: str) -> Optional[str]:
    """
    Extract backtestId from filenames like:
      6bfd78b1c53c2e682ab8f3635d8541f3.json
      6bfd78b1c53c2e682ab8f3635d8541f3_orders.json
      7df74aeb1e2f..._24_orders.json   (suffix pages etc. are ignored)
    """
    base = os.path.splitext(file_name)[0]
    return base.split("_")[0] if base else None


def _to_timestamp_str(val: Any) -> Optional[str]:
    if val is None:
        return None
    if isinstance(val, (int, float)):
        # Epoch timestamp seconds (10 digits) vs milliseconds (13 digits) vs microseconds (16 digits)
        if val > 1e14:
            val = val / 1e6
        elif val > 1e11:
            val = val / 1e3
        return dt.datetime.utcfromtimestamp(val).isoformat() + "Z"
    return str(val)


def insert_rows_chunked_with_fallback(
    client: bigquery.Client,
    table_id: str,
    rows_to_insert: List[Dict[str, Any]],
    *,
    max_rows_per_request: int = 500,
    max_request_bytes: int = 9_000_000,   # < 10MB request cap
    max_row_bytes_streaming: int = 950_000,  # streaming row hard-ish limit (~1MB)
    max_retries: int = 5,
    base_sleep: float = 1.0,
) -> None:
    """
    Stream rows in size-aware chunks with retry/backoff. If any single row is too large
    for streaming or repeated SSL/retry errors occur, fall back to a load job via NDJSON.
    """

    def _row_size_b(row: Dict[str, Any]) -> int:
        return len(json.dumps(row, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))

    # If any row is too big for streaming, go straight to load job.
    if any(_row_size_b(r) > max_row_bytes_streaming for r in rows_to_insert):
        _load_via_ndjson(client, table_id, rows_to_insert)
        return

    batch: List[Dict[str, Any]] = []
    batch_bytes = 0

    def _send_batch(b: List[Dict[str, Any]]) -> None:
        if not b:
            return
        # retry/backoff on transient/SSL errors; if still failing → fallback
        for attempt in range(max_retries):
            try:
                errors = client.insert_rows_json(table_id, b)
                if errors:  # API returned per-row errors
                    # If many rows error (often size/shape), fallback is safer
                    raise RuntimeError(f"Streaming insert errors: {errors!r}")
                return
            except (RequestsSSLError, ServiceUnavailable, GoogleAPICallError, RetryError, RuntimeError) as exc:
                last = attempt == max_retries - 1
                if last:
                    # Fallback this batch via load job
                    _load_via_ndjson(client, table_id, b)
                    return
                time.sleep(base_sleep * (2 ** attempt))

    for row in rows_to_insert:
        size = _row_size_b(row)
        if batch and (len(batch) >= max_rows_per_request or batch_bytes + size > max_request_bytes):
            _send_batch(batch)
            batch = []
            batch_bytes = 0
        batch.append(row)
        batch_bytes += size

    _send_batch(batch)


def _load_via_ndjson(client: bigquery.Client, table_id: str, rows: Iterable[Dict[str, Any]]) -> None:
    """Append rows using a load job from a local NDJSON temp file."""
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".ndjson", delete=False) as tmp:
        path = tmp.name
        for r in rows:
            tmp.write(json.dumps(r, ensure_ascii=False))
            tmp.write("\n")

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    )
    try:
        with open(path, "rb") as f:
            job = client.load_table_from_file(f, table_id, job_config=job_config)
        job.result()  # wait
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


def insert_rows_with_logging(client: bigquery.Client, table_id: str, rows_to_insert: List[Dict[str, Any]]) -> None:
    """
    Inserts rows into the given BigQuery table and logs any errors.

    Args:
        client (bigquery.Client): The BigQuery client.
        table_id (str): The full table ID ("dataset.table").
        rows_to_insert (List[Dict]): The rows to insert.
    """
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        print(f"Errors inserting into {table_id}: {errors}")
    else:
        print(f"Successfully inserted rows into {table_id}")


def load_json_to_bigquery(
    json_file_path: str,
    dataset_id: str,
    backtest_id: Optional[str] = None,
    project_id: Optional[str] = None
) -> None:
    """
    Load a JSON file into BigQuery. Supports:
      - Backtest result files:   Scripts/backtest_results/<backtestId>.json
      - Orders result files:     Scripts/orders_results/<backtestId>[_...]_orders.json

    Dedupe:
      - Backtests  -> BTOPResults(backtestId)
      - Orders     -> BTOPOrders(backtestId)  (any rows for that backtest => considered uploaded)

    After upload (or if already uploaded), move the file to the respective 'already_uploaded_*' folder.
    """
    client = get_bigquery_client(project_id)

    file_name = os.path.basename(json_file_path)
    is_orders = file_name.endswith("_orders.json")

    # Destination for moved files (relative to parent Scripts/ directory)
    scripts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    already_uploaded_dir = os.path.join(
        scripts_dir,
        "already_uploaded_orders_results" if is_orders
        else "already_uploaded_backtest_results"
    )
    destination_file = os.path.join(already_uploaded_dir, file_name)

    # Dedupe logic per kind
    if is_orders:
        backtest_id_guess = backtest_id or guess_backtest_id_from_filename(file_name)
        if not backtest_id_guess:
            print(f"Could not infer backtestId from {file_name}; skipping.")
            safe_move(json_file_path, destination_file)
            return

        query = f"""
            SELECT COUNT(1) AS count
            FROM `{dataset_id}.BTOPOrders`
            WHERE backtestId = '{backtest_id_guess}'
        """
        query_job = client.query(query)
        count = [row.count for row in query_job.result()][0]

        if count > 0:
            print(f"Orders for backtestId={backtest_id_guess} already uploaded. Moving file...")
            safe_move(json_file_path, destination_file)
            return

        # Load file, wrap as expected for load_orders()
        with open(json_file_path, 'r', encoding='utf-8') as f:
            payload = json.load(f)

        if isinstance(payload, list):
            data = {"backtest": {"backtestId": backtest_id_guess}, "orders": payload}
        elif isinstance(payload, dict):
            data = payload
            data.setdefault("backtest", {}).setdefault("backtestId", backtest_id_guess)
            if "orders" not in data:
                data["orders"] = []
        else:
            print(f"Unrecognized JSON structure in {file_name}; skipping.")
            safe_move(json_file_path, destination_file)
            return

        print("Loading orders data...")
        load_orders(data, client, dataset_id, backtest_id_guess)
        print("Orders load complete.")
        safe_move(json_file_path, destination_file)
        return

    # ----- Backtest results path -----
    uploaded_files_table = f"{dataset_id}.BTOPResults"
    backtest_id_from_name = backtest_id or file_name.replace(".json", "")
    query = f"""
        SELECT COUNT(backtestId) as count
        FROM `{uploaded_files_table}`
        WHERE backtestId = '{backtest_id_from_name}'
    """
    query_job = client.query(query)
    results = query_job.result()
    count = [row.count for row in results][0]

    if count > 0:
        print(f"File {file_name} has already been uploaded. Moving file...")
        safe_move(json_file_path, destination_file)
        return

    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check if 'backtest' key exists
    if not data.get("backtest"):
        print(f"Warning: 'backtest' key missing in {file_name}. Likely a failed backtest or invalid ID.")
        print(f"Data received: {json.dumps(data, indent=2)}")
        print(f"Skipping detailed stats upload for {file_name}. Moving to uploaded folder.")
        safe_move(json_file_path, destination_file)
        return

    print("Loading backtest data...")
    load_backtest(data, client, dataset_id, backtest_id_from_name)
    print("Loading research guide data...")
    load_research_guide(data, client, dataset_id, backtest_id_from_name)
    print("Loading backtest statistics data...")
    load_backtest_statistics(data, client, dataset_id, backtest_id_from_name)
    print("Loading charts data...")
    load_charts(data, client, dataset_id, backtest_id_from_name)
    print("Loading parameter set data...")
    load_parameter_set(data, client, dataset_id, backtest_id_from_name)
    print("Loading rolling window stats data...")
    load_rolling_window_stats(data, client, dataset_id, backtest_id_from_name)
    print("Loading runtime statistics data...")
    load_runtime_statistics(data, client, dataset_id, backtest_id_from_name)
    print("Loading total performance data...")
    load_total_performance(data, client, dataset_id, backtest_id_from_name)
    print("Loading errors data...")
    load_errors(data, client, dataset_id, backtest_id_from_name)

    # Check if orders have been loaded for this backtestId; if not, load/ensure placeholder in BTOPOrders
    orders_check_query = f"SELECT COUNT(1) as cnt FROM `{dataset_id}.BTOPOrders` WHERE backtestId = '{backtest_id_from_name}'"
    try:
        ord_cnt = list(client.query(orders_check_query, location="europe-west1").result())[0]["cnt"]
        if ord_cnt == 0:
            print("No orders found in BTOPOrders for backtest; writing placeholder...")
            load_orders(data, client, dataset_id, backtest_id_from_name)
    except Exception as e:
        print(f"Warning checking BTOPOrders count: {e}")

    print("Backtest load complete.")

    safe_move(json_file_path, destination_file)


def load_backtest(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    table_id = f"{dataset_id}.BTOPResults"
    bt_data = data.get("backtest", {})
    bt_id = bt_data.get("backtestId") or backtest_id
    rows_to_insert = [{
        "backtestId": bt_id,
        "name": bt_data.get("name"),
        "note": bt_data.get("note"),
        "organizationId": bt_data.get("organizationId"),
        "projectId": bt_data.get("projectId"),
        "completed": bt_data.get("completed"),
        "optimizationId": bt_data.get("optimizationId"),
        "tradeableDates": bt_data.get("tradeableDates"),
        "backtestStart": bt_data.get("backtestStart"),
        "backtestEnd": bt_data.get("backtestEnd"),
        "created": bt_data.get("created"),
        "snapshotId": bt_data.get("snapshotId"),
        "status": bt_data.get("status"),
        "error": bt_data.get("error"),
        "stacktrace": bt_data.get("stacktrace"),
        "progress": bt_data.get("progress"),
        "hasInitializeError": bt_data.get("hasInitializeError"),
        "nodeName": bt_data.get("nodeName"),
        "outOfSampleMaxEndDate": bt_data.get("outOfSampleMaxEndDate"),
        "outOfSampleDays": bt_data.get("outOfSampleDays"),
        "_ingested_at": dt.datetime.now(dt.timezone.utc).isoformat()
    }] if bt_data or bt_id else []

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)


def load_research_guide(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    table_id = f"{dataset_id}.BTOPResearchGuide"
    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    guide = data.get("backtest", {}).get("researchGuide") if data.get("backtest") else None
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    rows_to_insert = [{
        "guideId": f"{bt_id}_guide",
        "backtestId": bt_id,
        "minutes": guide.get("minutes"),
        "backtestCount": guide.get("backtestCount"),
        "parameters": guide.get("parameters"),
        "_ingested_at": now_ts
    }] if bt_id and guide else []

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)


def load_charts(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    table_id = f"{dataset_id}.BTOPCharts"
    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    charts = data.get("backtest", {}).get("charts", {}) if data.get("backtest") else {}
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    rows_to_insert = [{
        "chartId": f"{bt_id}_chart",
        "backtestId": bt_id,
        "name": chart_data.get("name"),
        "_ingested_at": now_ts
    } for chart_key, chart_data in charts.items()] if bt_id else []

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)


def load_parameter_set(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    table_id = f"{dataset_id}.BTOPParameterSet"
    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    param_dict = data.get("backtest", {}).get("parameterSet", {}) if data.get("backtest") else {}
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    if not bt_id:
        return

    if not param_dict:
        parameters_value = [{
            "name": "empty",
            "value": "empty"
        }]
    else:
        parameters_value = []
        for key, val in param_dict.items():
            parameters_value.append({
                "name": key,
                "value": str(val)
            })

    rows_to_insert = [{
        "parameterId": f"{bt_id}_param",
        "backtestId": bt_id,
        "parameters": parameters_value,
        "_ingested_at": now_ts
    }]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)


def load_rolling_window_stats(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    trade_table_id = f"{dataset_id}.BTOPRollingWindowTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPRollingWindowPortfolioStats"
    closed_trades_table_id = f"{dataset_id}.BTOPRollingWindowClosedTrades"

    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    if not bt_id:
        return

    rolling_window = data.get("backtest", {}).get("rollingWindow", {}) if data.get("backtest") else {}
    if not rolling_window:
        return

    rolling_trade_rows = []
    rolling_portfolio_rows = []
    rolling_closed_trades_rows = []

    for period_key, period_data in rolling_window.items():
        trade_stats = period_data.get("tradeStatistics")
        if trade_stats:
            rolling_trade_rows.append({
                "tradeStatId": f'{bt_id}_rw_trade',
                "backtestId": bt_id,
                "rollingWindowId": period_key,
                "startDateTime": trade_stats.get("startDateTime"),
                "endDateTime": trade_stats.get("endDateTime"),
                "totalNumberOfTrades": trade_stats.get("totalNumberOfTrades"),
                "numberOfWinningTrades": trade_stats.get("numberOfWinningTrades"),
                "numberOfLosingTrades": trade_stats.get("numberOfLosingTrades"),
                "totalProfitLoss": trade_stats.get("totalProfitLoss"),
                "totalProfit": trade_stats.get("totalProfit"),
                "totalLoss": trade_stats.get("totalLoss"),
                "largestProfit": trade_stats.get("largestProfit"),
                "largestLoss": trade_stats.get("largestLoss"),
                "averageProfitLoss": trade_stats.get("averageProfitLoss"),
                "averageProfit": trade_stats.get("averageProfit"),
                "averageLoss": trade_stats.get("averageLoss"),
                "averageTradeDuration": trade_stats.get("averageTradeDuration"),
                "averageWinningTradeDuration": trade_stats.get("averageWinningTradeDuration"),
                "averageLosingTradeDuration": trade_stats.get("averageLosingTradeDuration"),
                "medianTradeDuration": trade_stats.get("medianTradeDuration"),
                "medianWinningTradeDuration": trade_stats.get("medianWinningTradeDuration"),
                "medianLosingTradeDuration": trade_stats.get("medianLosingTradeDuration"),
                "maxConsecutiveWinningTrades": trade_stats.get("maxConsecutiveWinningTrades"),
                "maxConsecutiveLosingTrades": trade_stats.get("maxConsecutiveLosingTrades"),
                "profitLossRatio": trade_stats.get("profitLossRatio"),
                "winLossRatio": trade_stats.get("winLossRatio"),
                "winRate": trade_stats.get("winRate"),
                "lossRate": trade_stats.get("lossRate"),
                "averageMAE": trade_stats.get("averageMAE"),
                "averageMFE": trade_stats.get("averageMFE"),
                "largestMAE": trade_stats.get("largestMAE"),
                "largestMFE": trade_stats.get("largestMFE"),
                "maximumClosedTradeDrawdown": trade_stats.get("maximumClosedTradeDrawdown"),
                "maximumIntraTradeDrawdown": trade_stats.get("maximumIntraTradeDrawdown"),
                "profitLossStandardDeviation": trade_stats.get("profitLossStandardDeviation"),
                "profitLossDownsideDeviation": trade_stats.get("profitLossDownsideDeviation"),
                "profitFactor": trade_stats.get("profitFactor"),
                "sharpeRatio": trade_stats.get("sharpeRatio"),
                "sortinoRatio": trade_stats.get("sortinoRatio"),
                "profitToMaxDrawdownRatio": trade_stats.get("profitToMaxDrawdownRatio"),
                "maximumEndTradeDrawdown": trade_stats.get("maximumEndTradeDrawdown"),
                "averageEndTradeDrawdown": trade_stats.get("averageEndTradeDrawdown"),
                "maximumDrawdownDuration": trade_stats.get("maximumDrawdownDuration"),
                "totalFees": trade_stats.get("totalFees")
            })

        portfolio_stats = period_data.get("portfolioStatistics")
        if portfolio_stats:
            rolling_portfolio_rows.append({
                "portfolioStatId": f'{bt_id}_rw_portfolio',
                "backtestId": bt_id,
                "rollingWindowId": period_key,
                "averageWinRate": portfolio_stats.get("averageWinRate"),
                "averageLossRate": portfolio_stats.get("averageLossRate"),
                "profitLossRatio": portfolio_stats.get("profitLossRatio"),
                "winRate": portfolio_stats.get("winRate"),
                "lossRate": portfolio_stats.get("lossRate"),
                "expectancy": portfolio_stats.get("expectancy"),
                "startEquity": portfolio_stats.get("startEquity"),
                "endEquity": portfolio_stats.get("endEquity"),
                "compoundingAnnualReturn": portfolio_stats.get("compoundingAnnualReturn"),
                "drawdown": portfolio_stats.get("drawdown"),
                "totalNetProfit": portfolio_stats.get("totalNetProfit"),
                "sharpeRatio": portfolio_stats.get("sharpeRatio"),
                "probabilisticSharpeRatio": portfolio_stats.get("probabilisticSharpeRatio"),
                "sortinoRatio": portfolio_stats.get("sortinoRatio"),
                "alpha": portfolio_stats.get("alpha"),
                "beta": portfolio_stats.get("beta"),
                "annualStandardDeviation": portfolio_stats.get("annualStandardDeviation"),
                "annualVariance": portfolio_stats.get("annualVariance"),
                "informationRatio": portfolio_stats.get("informationRatio"),
                "trackingError": portfolio_stats.get("trackingError"),
                "treynorRatio": portfolio_stats.get("treynorRatio"),
                "portfolioTurnover": portfolio_stats.get("portfolioTurnover"),
                "valueAtRisk99": portfolio_stats.get("valueAtRisk99"),
                "valueAtRisk95": portfolio_stats.get("valueAtRisk95")
            })

        closed_list = period_data.get("closedTrades", [])
        for ct in closed_list:
            rolling_closed_trades_rows.append({
                "rollingWindowId": period_key,
                "backtestId": bt_id,
                "entryTime": ct.get("entryTime"),
                "entryPrice": ct.get("entryPrice"),
                "exitTime": ct.get("exitTime"),
                "exitPrice": ct.get("exitPrice"),
                "profitLoss": ct.get("profitLoss"),
                "totalFees": ct.get("totalFees"),
                "isWin": ct.get("isWin"),
            })

    if rolling_trade_rows:
        insert_rows_with_logging(client, trade_table_id, rolling_trade_rows)
    if rolling_portfolio_rows:
        insert_rows_with_logging(client, portfolio_table_id, rolling_portfolio_rows)
    if rolling_closed_trades_rows:
        insert_rows_with_logging(client, closed_trades_table_id, rolling_closed_trades_rows)


def load_runtime_statistics(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    table_id = f"{dataset_id}.BTOPRuntimeStatistics"
    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    if not bt_id:
        return
    runtime_stats = data.get("backtest", {}).get("runtimeStatistics", {}) if data.get("backtest") else {}
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    rows_to_insert = [{
        "runtimeStatId": f"{bt_id}_runtime",
        "backtestId": bt_id,
        "equity": runtime_stats.get("Equity"),
        "fees": runtime_stats.get("Fees"),
        "holdings": runtime_stats.get("Holdings"),
        "netProfit": runtime_stats.get("Net Profit"),
        "probabilisticSharpeRatio": runtime_stats.get("Probabilistic Sharpe Ratio"),
        "return": runtime_stats.get("Return"),
        "unrealized": runtime_stats.get("Unrealized"),
        "volume": runtime_stats.get("Volume"),
        "_ingested_at": now_ts
    }]
    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)


def load_orders(
    data: Union[Dict[str, Any], List[Dict[str, Any]]],
    client: bigquery.Client,
    dataset_id: str,
    backtest_id: Optional[str] = None
) -> None:
    """
    Load QC order payloads into BigQuery table `BTOPOrders`.
    """
    table_id = f"{dataset_id}.BTOPOrders"
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    def _to_ts(value: Any) -> Optional[str]:
        """Accept ISO8601 string or epoch (int/float) and return RFC3339 UTC string."""
        if value is None or value == "":
            return None
        if isinstance(value, (int, float)):
            return dt.datetime.fromtimestamp(float(value), tz=dt.timezone.utc).isoformat()
        if isinstance(value, str):
            try:
                if value.endswith("Z"):
                    value = value.replace("Z", "+00:00")
                return dt.datetime.fromisoformat(value).astimezone(dt.timezone.utc).isoformat()
            except Exception:
                return None
        if isinstance(value, dt.datetime):
            return value.astimezone(dt.timezone.utc).isoformat()
        return None

    def _int_or_none(v: Any) -> Optional[int]:
        try:
            return int(v)
        except Exception:
            return None

    def _float_or_none(v: Any) -> Optional[float]:
        try:
            return float(v)
        except Exception:
            return None

    def _bool_or_none(v: Any) -> Optional[bool]:
        if isinstance(v, bool):
            return v
        if isinstance(v, (int, float)):
            return bool(v)
        if isinstance(v, str):
            if v.lower() in {"true", "t", "1"}:
                return True
            if v.lower() in {"false", "f", "0"}:
                return False
        return None

    if isinstance(data, list):
        orders = data
        resolved_backtest_id = backtest_id
    elif isinstance(data, dict):
        orders = data.get("orders") or data.get("Orders") or []
        bt = data.get("backtest") or {}
        resolved_backtest_id = bt.get("backtestId") or bt.get("BacktestId") or backtest_id
        if not orders and isinstance(data.get("backtest"), list):
            orders = data["backtest"]
    else:
        return

    if not orders:
        if resolved_backtest_id:
            bt_name = (
                data.get("backtest", {}).get("name")
                if isinstance(data, dict) and isinstance(data.get("backtest"), dict)
                else "BT_UNKNOWN"
            ) if isinstance(data, dict) else "BT_UNKNOWN"
            placeholder_row = [{
                "backtestId": resolved_backtest_id,
                "id": -1,
                "status": 0,
                "type": 0,
                "direction": 0,
                "quantity": 0.0,
                "time": now_ts,
                "backtest_name": bt_name,
                "_ingested_at": now_ts
            }]
            insert_rows_with_logging(client, table_id, placeholder_row)
        return

    rows: List[Dict[str, Any]] = []
    for o in orders:
        bt_id = resolved_backtest_id or o.get("backtestId") or o.get("BacktestId")

        symbol = o.get("symbol", {}) or {}
        properties = o.get("properties", {}) or {}
        order_submission = o.get("orderSubmissionData", {}) or {}

        evs_src = o.get("events", []) or []
        events_bq = []
        for e in evs_src:
            events_bq.append(
                {
                    "algorithmId": e.get("algorithmId"),
                    "symbol": e.get("symbol"),
                    "symbolValue": e.get("symbolValue"),
                    "symbolPermtick": e.get("symbolPermtick"),
                    "orderId": _int_or_none(e.get("orderId")),
                    "orderEventId": _int_or_none(e.get("orderEventId")),
                    "id": e.get("id") if isinstance(e.get("id"), int) else _int_or_none(e.get("id")),
                    "status": e.get("status"),
                    "orderFeeAmount": _float_or_none(e.get("orderFeeAmount")),
                    "orderFeeCurrency": e.get("orderFeeCurrency"),
                    "fillPrice": _float_or_none(e.get("fillPrice")),
                    "fillPriceCurrency": e.get("fillPriceCurrency"),
                    "fillQuantity": _float_or_none(e.get("fillQuantity")),
                    "direction": e.get("direction"),
                    "message": e.get("message"),
                    "isAssignment": _bool_or_none(e.get("isAssignment")),
                    "stopPrice": _float_or_none(e.get("stopPrice")),
                    "limitPrice": _float_or_none(e.get("limitPrice")),
                    "quantity": _float_or_none(e.get("quantity")),
                    "time": _to_ts(e.get("time")),
                    "isInTheMoney": _bool_or_none(e.get("isInTheMoney")),
                }
            )

        gom = o.get("groupOrderManager") or {}
        gom_bq = {
            "id": _int_or_none(gom.get("id")),
            "quantity": _float_or_none(gom.get("quantity")),
            "count": _int_or_none(gom.get("count")),
            "limitPrice": _float_or_none(gom.get("limitPrice")),
            "orderIds": [int(x) for x in (gom.get("orderIds") or []) if isinstance(x, (int, str)) and str(x).isdigit()],
            "direction": _int_or_none(gom.get("direction")),
        }

        row = {
            "backtestId": bt_id,
            "id": _int_or_none(o.get("id")),
            "contingentId": _int_or_none(o.get("contingentId")),
            "brokerId": [str(x) for x in (o.get("brokerId") or [])],
            "symbol": {
                "value": symbol.get("value"),
                "id": symbol.get("id"),
                "permtick": symbol.get("permtick"),
            },
            "limitPrice": _float_or_none(o.get("limitPrice")),
            "stopPrice": _float_or_none(o.get("stopPrice")),
            "stopTriggered": _bool_or_none(o.get("stopTriggered")),
            "price": _float_or_none(o.get("price")),
            "priceCurrency": o.get("priceCurrency"),
            "quantity": _float_or_none(o.get("quantity")),
            "value": _float_or_none(o.get("value")),
            "time": _to_ts(o.get("time")),
            "createdTime": _to_ts(o.get("createdTime")),
            "lastFillTime": _to_ts(o.get("lastFillTime")),
            "lastUpdateTime": _to_ts(o.get("lastUpdateTime")),
            "canceledTime": _to_ts(o.get("canceledTime")),
            "type": _int_or_none(o.get("type")),
            "status": _int_or_none(o.get("status")),
            "securityType": _int_or_none(o.get("securityType")),
            "direction": _int_or_none(o.get("direction")),
            "tag": o.get("tag"),
            "orderSubmissionData": {
                "bidPrice": _float_or_none(order_submission.get("bidPrice")),
                "askPrice": _float_or_none(order_submission.get("askPrice")),
                "lastPrice": _float_or_none(order_submission.get("lastPrice")),
            },
            "isMarketable": _bool_or_none(o.get("isMarketable")),
            "properties": {
                "timeInForce": _int_or_none(properties.get("timeInForce")) if isinstance(properties.get("timeInForce"), (int, str)) else None
            },
            "events": events_bq,
            "trailingAmount": _float_or_none(o.get("trailingAmount")),
            "trailingPercentage": _bool_or_none(o.get("trailingPercentage")),
            "groupOrderManager": gom_bq if any(v is not None and v != [] for v in gom_bq.values()) else None,
            "triggerPrice": _float_or_none(o.get("triggerPrice")),
            "triggerTouched": _bool_or_none(o.get("triggerTouched")),
            "_ingestedAt": now_ts,
            "_ingested_at": now_ts,
        }

        if row["backtestId"] and row["id"] is not None:
            rows.append(row)

    if rows:
        insert_rows_chunked_with_fallback(client, table_id, rows)


def _parse_pct(val: Any) -> Optional[float]:
    if val is None or val == "":
        return None
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        cleaned = val.replace("%", "").replace("$", "").replace(",", "").strip()
        try:
            v = float(cleaned)
            return v / 100.0 if "%" in val else v
        except Exception:
            return None
    return None


def load_backtest_statistics(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    table_id = f"{dataset_id}.BTOPStatistics"
    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    if not bt_id:
        return
    bt_stats = data.get("backtest", {}).get("statistics") if data.get("backtest") else None
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    def _int(v: Any) -> Optional[int]:
        try:
            return int(str(v).replace(",", "").strip())
        except Exception:
            return None

    if bt_stats:
        rows_to_insert = [{
            "statisticId": f"{bt_id}_stat",
            "backtestId": bt_id,
            "totalOrders": _int(bt_stats.get("Total Orders")),
            "averageWin": _parse_pct(bt_stats.get("Average Win")),
            "averageLoss": _parse_pct(bt_stats.get("Average Loss")),
            "compoundingAnnualReturn": _parse_pct(bt_stats.get("Compounding Annual Return")),
            "drawdown": _parse_pct(bt_stats.get("Drawdown")),
            "expectancy": _parse_pct(bt_stats.get("Expectancy")),
            "startEquity": _parse_pct(bt_stats.get("Start Equity")),
            "endEquity": _parse_pct(bt_stats.get("End Equity")),
            "netProfit": _parse_pct(bt_stats.get("Net Profit")),
            "sharpeRatio": _parse_pct(bt_stats.get("Sharpe Ratio")),
            "sortinoRatio": _parse_pct(bt_stats.get("Sortino Ratio")),
            "probabilisticSharpeRatio": _parse_pct(bt_stats.get("Probabilistic Sharpe Ratio")),
            "lossRate": _parse_pct(bt_stats.get("Loss Rate")),
            "winRate": _parse_pct(bt_stats.get("Win Rate")),
            "profitLossRatio": _parse_pct(bt_stats.get("Profit-Loss Ratio")),
            "alpha": _parse_pct(bt_stats.get("Alpha")),
            "beta": _parse_pct(bt_stats.get("Beta")),
            "annualStandardDeviation": _parse_pct(bt_stats.get("Annual Standard Deviation")),
            "annualVariance": _parse_pct(bt_stats.get("Annual Variance")),
            "informationRatio": _parse_pct(bt_stats.get("Information Ratio")),
            "totalFees": _parse_pct(bt_stats.get("Total Fees")),
            "estimatedStrategyCapacity": _parse_pct(bt_stats.get("Estimated Strategy Capacity")),
            "lowestCapacityAsset": str(bt_stats.get("Lowest Capacity Asset")) if bt_stats.get("Lowest Capacity Asset") else None,
            "portfolioTurnover": _parse_pct(bt_stats.get("Portfolio Turnover")),
            "_ingested_at": now_ts,
        }]
        insert_rows_with_logging(client, table_id, rows_to_insert)


def build_symbol_struct(trade_obj: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Builds standardized BigQuery RECORD struct for BTOPTotalPerformanceClosedTrades.symbol."""
    if not isinstance(trade_obj, dict):
        return None
    sym_list = trade_obj.get("symbols") or ([trade_obj["symbol"]] if trade_obj.get("symbol") else [])
    sym_obj = sym_list[0] if (sym_list and isinstance(sym_list[0], dict)) else {}
    if not sym_obj and isinstance(trade_obj.get("symbol"), dict):
        sym_obj = trade_obj["symbol"]

    und_obj = sym_obj.get("underlying") or {}
    if isinstance(und_obj, str):
        und_obj = {"value": und_obj, "permtick": und_obj}

    val = sym_obj.get("value") or sym_obj.get("permtick") or ""
    und_val = und_obj.get("value") or und_obj.get("permtick")
    if not und_val and val:
        import re
        match = re.match(r'^([A-Za-z0-9]+)', val.strip())
        if match:
            und_val = match.group(1)
            und_obj = {"value": und_val, "permtick": und_val}

    if not sym_obj and not val:
        return None

    return {
        "value": val or None,
        "id": sym_obj.get("id"),
        "permtick": sym_obj.get("permtick"),
        "underlying": {
            "value": und_obj.get("value"),
            "id": und_obj.get("id"),
            "permtick": und_obj.get("permtick")
        } if und_obj and und_obj.get("value") else None
    }


def load_total_performance(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    trade_table_id = f"{dataset_id}.BTOPTotalPerformanceTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPTotalPerformancePortfolioStats"
    closed_trades_table_id = f"{dataset_id}.BTOPTotalPerformanceClosedTrades"

    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    if not bt_id:
        return
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    total_performance = data.get("backtest", {}).get("totalPerformance") if data.get("backtest") else None
    bt_name = data.get("backtest", {}).get("name") or backtest_name
    if total_performance:
        trade_rows = [{
            "tradeStatId": f"{bt_id}_tp_trade",
            "backtestId": bt_id,
            "backtest_name": bt_name,
            "startDateTime": total_performance["tradeStatistics"].get("startDateTime"),
            "endDateTime": total_performance["tradeStatistics"].get("endDateTime"),
            "totalNumberOfTrades": total_performance["tradeStatistics"].get("totalNumberOfTrades"),
            "numberOfWinningTrades": total_performance["tradeStatistics"].get("numberOfWinningTrades"),
            "numberOfLosingTrades": total_performance["tradeStatistics"].get("numberOfLosingTrades"),
            "totalProfitLoss": total_performance["tradeStatistics"].get("totalProfitLoss"),
            "totalProfit": total_performance["tradeStatistics"].get("totalProfit"),
            "totalLoss": total_performance["tradeStatistics"].get("totalLoss"),
            "largestProfit": total_performance["tradeStatistics"].get("largestProfit"),
            "largestLoss": total_performance["tradeStatistics"].get("largestLoss"),
            "averageProfitLoss": total_performance["tradeStatistics"].get("averageProfitLoss"),
            "averageProfit": total_performance["tradeStatistics"].get("averageProfit"),
            "averageLoss": total_performance["tradeStatistics"].get("averageLoss"),
            "averageTradeDuration": total_performance["tradeStatistics"].get("averageTradeDuration"),
            "averageWinningTradeDuration": total_performance["tradeStatistics"].get("averageWinningTradeDuration"),
            "averageLosingTradeDuration": total_performance["tradeStatistics"].get("averageLosingTradeDuration"),
            "medianTradeDuration": total_performance["tradeStatistics"].get("medianTradeDuration"),
            "medianWinningTradeDuration": total_performance["tradeStatistics"].get("medianWinningTradeDuration"),
            "medianLosingTradeDuration": total_performance["tradeStatistics"].get("medianLosingTradeDuration"),
            "maxConsecutiveWinningTrades": total_performance["tradeStatistics"].get("maxConsecutiveWinningTrades"),
            "maxConsecutiveLosingTrades": total_performance["tradeStatistics"].get("maxConsecutiveLosingTrades"),
            "profitLossRatio": total_performance["tradeStatistics"].get("profitLossRatio"),
            "winLossRatio": total_performance["tradeStatistics"].get("winLossRatio"),
            "winRate": total_performance["tradeStatistics"].get("winRate"),
            "lossRate": total_performance["tradeStatistics"].get("lossRate"),
            "averageMAE": total_performance["tradeStatistics"].get("averageMAE"),
            "averageMFE": total_performance["tradeStatistics"].get("averageMFE"),
            "largestMAE": total_performance["tradeStatistics"].get("largestMAE"),
            "largestMFE": total_performance["tradeStatistics"].get("largestMFE"),
            "maximumClosedTradeDrawdown": total_performance["tradeStatistics"].get("maximumClosedTradeDrawdown"),
            "maximumIntraTradeDrawdown": total_performance["tradeStatistics"].get("maximumIntraTradeDrawdown"),
            "profitLossStandardDeviation": total_performance["tradeStatistics"].get("profitLossStandardDeviation"),
            "profitLossDownsideDeviation": total_performance["tradeStatistics"].get("profitLossDownsideDeviation"),
            "profitFactor": total_performance["tradeStatistics"].get("profitFactor"),
            "sharpeRatio": total_performance["tradeStatistics"].get("sharpeRatio"),
            "sortinoRatio": total_performance["tradeStatistics"].get("sortinoRatio"),
            "profitToMaxDrawdownRatio": total_performance["tradeStatistics"].get("profitToMaxDrawdownRatio"),
            "maximumEndTradeDrawdown": total_performance["tradeStatistics"].get("maximumEndTradeDrawdown"),
            "averageEndTradeDrawdown": total_performance["tradeStatistics"].get("averageEndTradeDrawdown"),
            "maximumDrawdownDuration": total_performance["tradeStatistics"].get("maximumDrawdownDuration"),
            "totalFees": total_performance["tradeStatistics"].get("totalFees"),
            "_ingested_at": now_ts,
        }] if total_performance.get("tradeStatistics") else []

        portfolio_rows = [{
            "portfolioStatId": f"{bt_id}_tp_portfolio",
            "backtestId": bt_id,
            "backtest_name": bt_name,
            "averageWinRate": total_performance["portfolioStatistics"].get("averageWinRate"),
            "averageLossRate": total_performance["portfolioStatistics"].get("averageLossRate"),
            "profitLossRatio": total_performance["portfolioStatistics"].get("profitLossRatio"),
            "winRate": total_performance["portfolioStatistics"].get("winRate"),
            "lossRate": total_performance["portfolioStatistics"].get("lossRate"),
            "expectancy": total_performance["portfolioStatistics"].get("expectancy"),
            "startEquity": total_performance["portfolioStatistics"].get("startEquity"),
            "endEquity": total_performance["portfolioStatistics"].get("endEquity"),
            "compoundingAnnualReturn": total_performance["portfolioStatistics"].get("compoundingAnnualReturn"),
            "drawdown": total_performance["portfolioStatistics"].get("drawdown"),
            "totalNetProfit": total_performance["portfolioStatistics"].get("totalNetProfit"),
            "sharpeRatio": total_performance["portfolioStatistics"].get("sharpeRatio"),
            "probabilisticSharpeRatio": total_performance["portfolioStatistics"].get("probabilisticSharpeRatio"),
            "sortinoRatio": total_performance["portfolioStatistics"].get("sortinoRatio"),
            "alpha": total_performance["portfolioStatistics"].get("alpha"),
            "beta": total_performance["portfolioStatistics"].get("beta"),
            "annualStandardDeviation": total_performance["portfolioStatistics"].get("annualStandardDeviation"),
            "annualVariance": total_performance["portfolioStatistics"].get("annualVariance"),
            "informationRatio": total_performance["portfolioStatistics"].get("informationRatio"),
            "trackingError": total_performance["portfolioStatistics"].get("trackingError"),
            "treynorRatio": total_performance["portfolioStatistics"].get("treynorRatio"),
            "portfolioTurnover": total_performance["portfolioStatistics"].get("portfolioTurnover"),
            "valueAtRisk99": total_performance["portfolioStatistics"].get("valueAtRisk99"),
            "valueAtRisk95": total_performance["portfolioStatistics"].get("valueAtRisk95"),
            "_ingested_at": now_ts,
        }] if total_performance.get("portfolioStatistics") else []

        bt_name = data.get("backtest", {}).get("name") or backtest_name
        closed_trades = total_performance.get("closedTrades", [])
        closed_trades_rows = []
        for i, t in enumerate(closed_trades):
            symbol_struct = build_symbol_struct(t)

            closed_trades_rows.append({
                "tradeId": f"{bt_id}_ct_{i}",
                "backtestId": bt_id,
                "backtest_name": bt_name,
                "symbol": symbol_struct,
                "entryTime": _to_timestamp_str(t.get("entryTime")),
                "entryPrice": t.get("entryPrice"),
                "direction": t.get("direction"),
                "quantity": t.get("quantity"),
                "exitTime": _to_timestamp_str(t.get("exitTime")),
                "exitPrice": t.get("exitPrice"),
                "profitLoss": t.get("profitLoss"),
                "totalFees": t.get("totalFees"),
                "mae": t.get("mae"),
                "mfe": t.get("mfe"),
                "duration": t.get("duration"),
                "endTradeDrawdown": t.get("endTradeDrawdown"),
                "isWin": t.get("isWin"),
                "_ingested_at": now_ts,
            })

        if trade_rows:
            insert_rows_with_logging(client, trade_table_id, trade_rows)
        if portfolio_rows:
            insert_rows_with_logging(client, portfolio_table_id, portfolio_rows)
        if closed_trades_rows:
            insert_rows_with_logging(client, closed_trades_table_id, closed_trades_rows)


def load_errors(data: Dict[str, Any], client: bigquery.Client, dataset_id: str, backtest_id: Optional[str] = None) -> None:
    table_id = f"{dataset_id}.BTOPErrors"
    bt_id = data.get("backtest", {}).get("backtestId") or backtest_id
    if not bt_id:
        return
    bt = data.get("backtest", data)
    err_msg = bt.get("error") or bt.get("RuntimeError") or data.get("error")
    stack = bt.get("stacktrace") or bt.get("StackTrace")
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    if err_msg or stack:
        full_msg = f"{err_msg}\nStacktrace: {stack}" if (err_msg and stack) else (err_msg or stack)
        rows_to_insert = [{
            "errorId": f"{bt_id}_error_0",
            "backtestId": bt_id,
            "errorMessage": str(full_msg)[:4000],
            "_ingested_at": now_ts,
        }]
    else:
        rows_to_insert = [{
            "errorId": f"{bt_id}_no_error",
            "backtestId": bt_id,
            "errorMessage": "NO_ERROR",
            "_ingested_at": now_ts,
        }]
    insert_rows_with_logging(client, table_id, rows_to_insert)


def parse_args():
    parser = argparse.ArgumentParser(description="Upload backtest results and orders to BigQuery.")
    parser.add_argument(
        "--results-path",
        type=str,
        help="Path to a single JSON file (backtest or orders results) to upload.",
    )
    parser.add_argument(
        "--backtest-id",
        type=str,
        help="Optional backtest ID override. If not specified, inferred from the filename.",
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default=os.getenv("BIGQUERY_DATASET", "develop"),
        help="BigQuery dataset to load data into (default: 'develop').",
    )
    parser.add_argument(
        "--project-id",
        type=str,
        default=os.getenv("BIGQUERY_PROJECT", "bav-personal-cloud"),
        help="BigQuery project ID (default: 'bav-personal-cloud').",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    project_id = args.project_id
    dataset = args.dataset

    if args.results_path:
        if os.path.exists(args.results_path):
            load_json_to_bigquery(args.results_path, dataset, args.backtest_id, project_id)
        else:
            print(f"Error: Specified --results-path does not exist: {args.results_path}")
            sys.exit(1)
    else:
        scripts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        backtest_results_dir = os.path.join(scripts_dir, "backtest_results")
        orders_results_dir   = os.path.join(scripts_dir, "orders_results")

        # Process BACKTEST files
        if os.path.isdir(backtest_results_dir):
            for file_name in os.listdir(backtest_results_dir):
                time.sleep(1)
                if file_name.endswith(".json"):
                    json_file = os.path.join(backtest_results_dir, file_name)
                    load_json_to_bigquery(json_file, dataset, project_id=project_id)

        # Process ORDERS files
        if os.path.isdir(orders_results_dir):
            for file_name in os.listdir(orders_results_dir):
                time.sleep(1)
                if file_name.endswith(".json"):
                    json_file = os.path.join(orders_results_dir, file_name)
                    load_json_to_bigquery(json_file, dataset, project_id=project_id)
