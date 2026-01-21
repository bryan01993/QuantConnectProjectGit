from __future__ import annotations

import datetime as dt
from typing import Any, Dict, List, Optional, Callable, Union
import json, os, tempfile, time
from typing import List, Dict, Any, Iterable

from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPICallError, RetryError, ServiceUnavailable
from requests.exceptions import SSLError as RequestsSSLError
from google.oauth2 import service_account
# If you run into cross-partition or cross-filesystem issues with os.rename, consider using shutil.move.
import shutil

def safe_move(src: str, dst: str) -> None:
    """Move src → dst; if dst exists, append a timestamp."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        base, ext = os.path.splitext(dst)
        dst = f"{base}_{int(time.time())}{ext}"
    shutil.move(src, dst)
    print(f"File moved to {dst}")


def get_bigquery_client(project_id='bav-personal-cloud') -> bigquery.Client:
    """
    Returns a BigQuery client.
    First checks for a Service Account key in Resources/gcp_keys.json.
    If found, uses it. Otherwise, falls back to Application Default Credentials.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming Resources is at the project root, which is one level up from scripts
    key_path = os.path.abspath(os.path.join(script_dir, "..", "Resources", "gcp_keys.json"))

    if os.path.exists(key_path):
        print(f"Authenticating with service account key: {key_path}")
        credentials = service_account.Credentials.from_service_account_file(key_path)
        return bigquery.Client(project=project_id, credentials=credentials)
    else:
        print("Authenticating with Application Default Credentials (ADC)")
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
def insert_rows_with_logging(client, table_id, rows_to_insert):
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


def load_json_to_bigquery(json_file_path, dataset_id):
    """
    Load a JSON file into BigQuery. Supports:
      - Backtest result files:   Scripts/backtest_results/<backtestId>.json
      - Orders result files:     Scripts/orders_results/<backtestId>[_...]_orders.json

    Dedupe:
      - Backtests  -> BTOPResults(backtestId)
      - Orders     -> BTOPOrders(backtestId)  (any rows for that backtest => considered uploaded)

    After upload (or if already uploaded), move the file to the respective 'already_uploaded_*' folder.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Use helper to get client with explicit credentials if available
    client = get_bigquery_client()

    file_name = os.path.basename(json_file_path)
    is_orders = file_name.endswith("_orders.json")

    # Destination for moved files
    already_uploaded_dir = os.path.join(
        current_dir,
        "../Scripts/already_uploaded_orders_results" if is_orders
        else "../Scripts/already_uploaded_backtest_results"
    )
    destination_file = os.path.join(already_uploaded_dir, file_name)

    # Dedupe logic per kind
    if is_orders:
        backtest_id_guess = guess_backtest_id_from_filename(file_name)
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
        with open(json_file_path, 'r') as f:
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
        load_orders(data, client, dataset_id)
        print("Orders load complete.")
        safe_move(json_file_path, destination_file)
        return

    # ----- Backtest results path (existing behavior) -----
    uploaded_files_table = f"{dataset_id}.BTOPResults"
    backtest_id_from_name = file_name.strip(".json")
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

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Check if 'backtest' key exists (it might be missing if the backtest failed or wasn't found)
    if not data.get("backtest"):
        print(f"Warning: 'backtest' key missing in {file_name}. Likely a failed backtest or invalid ID.")
        print(f"Data received: {json.dumps(data, indent=2)}")
        
        # TODO: if that is the case uploads the results based on the backtestId and the Error in the corresponding table
        
        print(f"Skipping detailed stats upload for {file_name}. Moving to uploaded folder.")
        safe_move(json_file_path, destination_file)
        return

    print("Loading backtest data...")
    load_backtest(data, client, dataset_id)
    print("Loading research guide data...")
    load_research_guide(data, client, dataset_id)
    print("Loading backtest statistics data...")
    load_backtest_statistics(data, client, dataset_id)
    print("Loading charts data...")
    load_charts(data, client, dataset_id)
    print("Loading parameter set data...")
    load_parameter_set(data, client, dataset_id)
    print("Loading rolling window stats data...")
    load_rolling_window_stats(data, client, dataset_id)
    print("Loading runtime statistics data...")
    load_runtime_statistics(data, client, dataset_id)
    print("Loading total performance data...")
    load_total_performance(data, client, dataset_id)
    print("Loading errors data...")
    load_errors(data, client, dataset_id)
    print("Backtest load complete.")

    safe_move(json_file_path, destination_file)


def load_backtest(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPResults"
    rows_to_insert = [{
        "backtestId": bt.get("backtestId"),
        "name": bt.get("name"),
        "note": bt.get("note"),
        "organizationId": bt.get("organizationId"),
        "projectId": bt.get("projectId"),
        "completed": bt.get("completed"),
        "optimizationId": bt.get("optimizationId"),
        "tradeableDates": bt.get("tradeableDates"),
        "backtestStart": bt.get("backtestStart"),
        "backtestEnd": bt.get("backtestEnd"),
        "created": bt.get("created"),
        "snapshotId": bt.get("snapshotId"),
        "status": bt.get("status"),
        "error": bt.get("error"),
        "stacktrace": bt.get("stacktrace"),
        "progress": bt.get("progress"),
        "hasInitializeError": bt.get("hasInitializeError"),
        "nodeName": bt.get("nodeName"),
        "outOfSampleMaxEndDate": bt.get("outOfSampleMaxEndDate"),
        "outOfSampleDays": bt.get("outOfSampleDays")
    } for bt in [data.get("backtest", {})]]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_research_guide(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPResearchGuide"
    rows_to_insert = [{
        "guideId": f"{data['backtest'].get('backtestId')}_guide",
        "backtestId": data["backtest"].get("backtestId"),
        "minutes": data["backtest"]["researchGuide"].get("minutes"),
        "backtestCount": data["backtest"]["researchGuide"].get("backtestCount"),
        "parameters": data["backtest"]["researchGuide"].get("parameters")
    }] if data.get("backtest") and data["backtest"].get("researchGuide") else []

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_charts(data, client, dataset_id):
    #TODO It is not inserting at least Strategy Equity Chart, which does come populated in Results
    table_id = f"{dataset_id}.BTOPCharts"
    rows_to_insert = [{
        "chartId": f"{data['backtest'].get('backtestId')}_chart",
        "backtestId": data["backtest"].get("backtestId"),
        "name": chart_data["name"]
    } for chart_key, chart_data in data["backtest"].get("charts", {}).items()]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_parameter_set(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPParameterSet"
    param_dict = data["backtest"].get("parameterSet", {})

    if not param_dict:
        # If param_dict is empty or missing, we make 'parameters' = None
        parameters_value = [{
            "name": "empty",
            "value": "empty"
        }]
    else:
        # Build a list of { "name": <key>, "value": <value> } records
        parameters_value = []
        for key, val in param_dict.items():
            parameters_value.append({
                "name": key,
                "value": str(val)  # Convert to string if your schema expects STRING
            })

    # Insert exactly one row, containing all the key/value pairs (or None if empty)
    rows_to_insert = [{
        "parameterId": f"{data['backtest'].get('backtestId')}_param",
        "backtestId": data["backtest"].get("backtestId"),
        "parameters": parameters_value
    }]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_rolling_window_stats(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPRollingWindowTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPRollingWindowPortfolioStats"
    closed_trades_table_id = f"{dataset_id}.BTOPRollingWindowClosedTrades"

    rolling_window = data["backtest"].get("rollingWindow", {})
    if not rolling_window:
        return

    # We'll accumulate all rows across all rolling-window entries here:
    rolling_trade_rows = []
    rolling_portfolio_rows = []

    # TODO
    # Still have not found observation on these items, hence more testing is needed.
    rolling_closed_trades_rows = []

    for period_key, period_data in rolling_window.items():
        trade_stats = period_data.get("tradeStatistics")
        if trade_stats:
            rolling_trade_rows.append({
                "tradeStatId": f'{data["backtest"].get("backtestId")}_rw_trade',
                "backtestId": data["backtest"].get("backtestId"),
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
                "portfolioStatId": f'{data["backtest"].get("backtestId")}_rw_portfolio',
                "backtestId": data["backtest"].get("backtestId"),
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
                "backtestId": data["backtest"].get("backtestId"),
                "entryTime": ct.get("entryTime"),
                "entryPrice": ct.get("entryPrice"),
                "exitTime": ct.get("exitTime"),
                "exitPrice": ct.get("exitPrice"),
                "profitLoss": ct.get("profitLoss"),
                "totalFees": ct.get("totalFees"),
                "isWin": ct.get("isWin"),
            })

    # Finally, insert each accumulated list
    if rolling_trade_rows:
        insert_rows_with_logging(client, trade_table_id, rolling_trade_rows)
    if rolling_portfolio_rows:
        insert_rows_with_logging(client, portfolio_table_id, rolling_portfolio_rows)
    if rolling_closed_trades_rows:
        insert_rows_with_logging(client, closed_trades_table_id, rolling_closed_trades_rows)

def load_runtime_statistics(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPRuntimeStatistics"
    runtime_stats = data["backtest"].get("runtimeStatistics", {})

    rows_to_insert = [{
        "runtimeStatId": f"{data['backtest'].get('backtestId')}_runtime",
        "backtestId": data["backtest"].get("backtestId"),
        "equity": runtime_stats.get("Equity"),
        "fees": runtime_stats.get("Fees"),
        "holdings": runtime_stats.get("Holdings"),
        "netProfit": runtime_stats.get("Net Profit"),
        "probabilisticSharpeRatio": runtime_stats.get("Probabilistic Sharpe Ratio"),
        "return": runtime_stats.get("Return"),
        "unrealized": runtime_stats.get("Unrealized"),
        "volume": runtime_stats.get("Volume"),
    }]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)




def load_orders(
    data: Union[Dict[str, Any], List[Dict[str, Any]]],
    client,
    dataset_id: str,
    insert_fn: Optional[Callable[[Any, str, List[Dict[str, Any]]], None]] = None,
) -> None:
    """
    Load QC order payloads into BigQuery table `BTOPOrders`.

    Parameters
    ----------
    data : dict | list
        Either:
          - a dict containing 'backtest' (with 'backtestId') and 'orders' (list), or
          - a bare list of order dicts (in which case 'backtest.backtestId' must be present in data['backtest'] or is provided via each row's tag).
    client : bigquery.Client
        Initialized BigQuery client.
    dataset_id : str
        Target dataset (e.g., "develop").
    insert_fn : callable(client, table_id, rows)
        Injection point for `insert_rows_with_logging`. If None, uses global `insert_rows_with_logging`.

    Notes
    -----
    - Maps only the fields present in the BTOPOrders DDL; extra fields in the payload are ignored.
    - Timestamps are normalized to RFC3339 strings for safety.
    - Events.time in QC can be epoch seconds; converted to UTC timestamp.
    """
    if insert_fn is None:
        # falls back to helper used elsewhere in your codebase
        insert_fn = insert_rows_with_logging  # noqa: F821 (assumed to exist in caller's module)

    table_id = f"{dataset_id}.BTOPOrders"
    now_ts = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc).isoformat()

    # ---- helpers -----------------------------------------------------------
    def _to_ts(value: Any) -> Optional[str]:
        """Accept ISO8601 string or epoch (int/float) and return RFC3339 UTC string."""
        if value is None or value == "":
            return None
        if isinstance(value, (int, float)):
            return dt.datetime.fromtimestamp(float(value), tz=dt.timezone.utc).isoformat()
        if isinstance(value, str):
            try:
                # Normalize Z → +00:00 for ISO compliance
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

    # ---- extract containers -----------------------------------------------
    if isinstance(data, list):
        orders = data
        backtest_id = None
    elif isinstance(data, dict):
        orders = data.get("orders") or data.get("Orders") or []
        bt = data.get("backtest") or {}
        backtest_id = bt.get("backtestId") or bt.get("BacktestId")
        # Some QC endpoints return the list directly under the root
        if not orders and isinstance(data.get("backtest"), list):
            orders = data["backtest"]
    else:
        return

    if not orders:
        return  # nothing to insert

    rows: List[Dict[str, Any]] = []
    for o in orders:
        # Determine backtestId per row (prefer global, fall back to tag decoding if you encode it yourself)
        bt_id = backtest_id
        if not bt_id:
            bt_id = (o.get("backtestId") or o.get("BacktestId") or None)

        symbol = o.get("symbol", {}) or {}
        properties = o.get("properties", {}) or {}
        order_submission = o.get("orderSubmissionData", {}) or {}

        # Build events array
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

        # Group order manager
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
                # QC sometimes returns {} — store None when absent
                "timeInForce": _int_or_none(properties.get("timeInForce")) if isinstance(properties.get("timeInForce"), (int, str)) else None
            },
            "events": events_bq,
            "trailingAmount": _float_or_none(o.get("trailingAmount")),
            "trailingPercentage": _bool_or_none(o.get("trailingPercentage")),
            "groupOrderManager": gom_bq if any(v is not None and v != [] for v in gom_bq.values()) else None,
            "triggerPrice": _float_or_none(o.get("triggerPrice")),
            "triggerTouched": _bool_or_none(o.get("triggerTouched")),
            "_ingestedAt": now_ts,
        }

        # Only append valid rows (must have backtestId and id)
        if row["backtestId"] and row["id"] is not None:
            rows.append(row)

    if rows:
        insert_rows_chunked_with_fallback(client, table_id, rows)


def load_backtest_statistics(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPStatistics"
    bt_stats = data["backtest"].get("statistics")

    if bt_stats:
        rows_to_insert = [{
            "statisticId": f"{data['backtest'].get('backtestId')}_stat",
            "backtestId": data["backtest"].get("backtestId"),
            "totalOrders": bt_stats.get("Total Orders"),
            "averageWin": bt_stats.get("Average Win"),
            "averageLoss": bt_stats.get("Average Loss"),
            "compoundingAnnualReturn": bt_stats.get("Compounding Annual Return"),
            "drawdown": bt_stats.get("Drawdown"),
            "expectancy": bt_stats.get("Expectancy"),
            "startEquity": bt_stats.get("Start Equity"),
            "endEquity": bt_stats.get("End Equity"),
            "netProfit": bt_stats.get("Net Profit"),
            "sharpeRatio": bt_stats.get("Sharpe Ratio"),
            "sortinoRatio": bt_stats.get("Sortino Ratio"),
            "probabilisticSharpeRatio": bt_stats.get("Probabilistic Sharpe Ratio"),
            "lossRate": bt_stats.get("Loss Rate"),
            "winRate": bt_stats.get("Win Rate"),
            "profitLossRatio": bt_stats.get("Profit-Loss Ratio"),
            "alpha": bt_stats.get("Alpha"),
            "beta": bt_stats.get("Beta"),
            "annualStandardDeviation": bt_stats.get("Annual Standard Deviation"),
            "annualVariance": bt_stats.get("Annual Variance"),
            "informationRatio": bt_stats.get("Information Ratio"),
            "totalFees": bt_stats.get("Total Fees"),
            "estimatedStrategyCapacity": bt_stats.get("Estimated Strategy Capacity"),
            "lowestCapacityAsset": bt_stats.get("Lowest Capacity Asset"),
            "portfolioTurnover": bt_stats.get("Portfolio Turnover"),
        }]
    else:
        rows_to_insert = None

        if rows_to_insert:
            insert_rows_with_logging(client, table_id, rows_to_insert)
def load_total_performance(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPTotalPerformanceTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPTotalPerformancePortfolioStats"
    closed_trades_table_id = f"{dataset_id}.BTOPTotalPerformanceClosedTrades"

    total_performance = data["backtest"].get("totalPerformance")
    if total_performance:
        trade_rows = [{
            "tradeStatId": f"{data['backtest'].get('backtestId')}_tp_trade",
            "backtestId": data["backtest"].get("backtestId"),
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
        }] if total_performance.get("tradeStatistics") else []

        portfolio_rows = [{
            "portfolioStatId": f"{data['backtest'].get('backtestId')}_tp_portfolio",
            "backtestId": data["backtest"].get("backtestId"),
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
        }] if total_performance.get("portfolioStatistics") else []

        closed_trades = total_performance.get("closedTrades", [])
        closed_trades_rows = [
            {
                "tradeId": f"{data['backtest'].get('backtestId')}_ct_{i}",
                "backtestId": data["backtest"].get("backtestId"),

                # Symbol details
                "symbol": {
                    "value": t["symbol"].get("value") if t.get("symbol") else None,
                    "id": t["symbol"].get("id") if t.get("symbol") else None,
                    "permtick": t["symbol"].get("permtick") if t.get("symbol") else None,
                    "underlying": {
                        "value": t["symbol"]["underlying"].get("value") if t.get("symbol") and t["symbol"].get("underlying") else None,
                        "id": t["symbol"]["underlying"].get("id") if t.get("symbol") and t["symbol"].get("underlying") else None,
                        "permtick": t["symbol"]["underlying"].get("permtick") if t.get("symbol") and t["symbol"].get("underlying") else None,
                    } if t.get("symbol") and t["symbol"].get("underlying") else None
                } if t.get("symbol") else None,

                # Trade fields
                "entryTime": t.get("entryTime"),
                "entryPrice": t.get("entryPrice"),
                "direction": t.get("direction"),
                "quantity": t.get("quantity"),
                "exitTime": t.get("exitTime"),
                "exitPrice": t.get("exitPrice"),
                "profitLoss": t.get("profitLoss"),
                "totalFees": t.get("totalFees"),
                "mae": t.get("mae"),
                "mfe": t.get("mfe"),
                "duration": t.get("duration"),
                "endTradeDrawdown": t.get("endTradeDrawdown"),
                "isWin": t.get("isWin")
            }
            for i, t in enumerate(closed_trades)
        ]

        if trade_rows:
            insert_rows_with_logging(client, trade_table_id, trade_rows)

        if portfolio_rows:
            insert_rows_with_logging(client, portfolio_table_id, portfolio_rows)

        if closed_trades_rows:
            insert_rows_with_logging(client, closed_trades_table_id, closed_trades_rows)

def load_errors(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPErrors"
    errors = data.get("errors", [])
    rows_to_insert = [{
        "errorId": f"{data['backtest'].get('backtestId')}_error_{i}",
        "backtestId": data["backtest"].get("backtestId"),
        "errorMessage": error
    } for i, error in enumerate(errors)]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset = "develop"

    backtest_results_dir = os.path.join(current_dir, "../Scripts/backtest_results")
    orders_results_dir   = os.path.join(current_dir, "../Scripts/orders_results")

    # Process BACKTEST files
    if os.path.isdir(backtest_results_dir):
        for file_name in os.listdir(backtest_results_dir):
            time.sleep(1)
            if file_name.endswith(".json"):
                json_file = os.path.join(backtest_results_dir, file_name)
                load_json_to_bigquery(json_file, dataset)

    # Process ORDERS files
    if os.path.isdir(orders_results_dir):
        for file_name in os.listdir(orders_results_dir):
            time.sleep(1)
            if file_name.endswith(".json"):
                json_file = os.path.join(orders_results_dir, file_name)
                load_json_to_bigquery(json_file, dataset)