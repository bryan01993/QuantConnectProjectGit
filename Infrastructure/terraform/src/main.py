"""
GCP Cloud Function (2nd Gen) Entrypoint for QuantConnect Serverless Batch Ingestion & HDBT Launcher
===================================================================================================
Triggered by GCP Cloud Scheduler every 5 minutes (Polling Mode) or via HTTP POST (Launch Mode).
- Polling Mode: Ingests finished backtests into ALL 15 BigQuery tables, auto-advances chunked runs, and recovers stalled batches.
- Launch Mode: Compiles project on QC Cloud, queues year chunks, and launches HDBT serverlessly.
- Billed per millisecond, $0 when idle (min_instance_count = 0).
"""

from __future__ import annotations

import base64
import datetime as dt
import hashlib
import json
import logging
import os
import time
from typing import Any, Dict, List
import functions_framework
import requests
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)

PROJECT_ID = os.getenv("BIGQUERY_PROJECT", "bav-personal-cloud")
DATASET_ID = os.getenv("BIGQUERY_DATASET", "develop")

BATCH_TABLE = "BTOPBatchChunks"
TRADES_TABLE = "BTOPTrades"
RESULTS_TABLE = "BTOPResults"
PORTFOLIO_STATS_TABLE = "BTOPTotalPerformancePortfolioStats"
TRADE_STATS_TABLE = "BTOPTotalPerformanceTradeStats"
CLOSED_TRADES_TABLE = "BTOPTotalPerformanceClosedTrades"
PARAM_SET_TABLE = "BTOPParameterSet"
RESEARCH_GUIDE_TABLE = "BTOPResearchGuide"
RUNTIME_STATS_TABLE = "BTOPRuntimeStatistics"
CHARTS_TABLE = "BTOPCharts"
STATS_TABLE = "BTOPStatistics"
RW_PORTFOLIO_TABLE = "BTOPRollingWindowPortfolioStats"
RW_TRADE_TABLE = "BTOPRollingWindowTradeStats"
RW_CLOSED_TABLE = "BTOPRollingWindowClosedTrades"
ERRORS_TABLE = "BTOPErrors"
ORDERS_TABLE = "BTOPOrders"

QC_API_KEY = os.getenv("QUANTCONNECT_LOGIN_API_KEY")
QC_USER_ID = os.getenv("QUANTCONNECT_USER_ID")
QC_PROJECT_ID = os.getenv("QUANTCONNECT_PROJECT_ID", "22447448")


def get_api_token(api_key: str, user_id: str) -> Dict[str, str]:
    timestamp = str(int(time.time()))
    time_stamped_token = f"{api_key}:{timestamp}"
    hashed_token = hashlib.sha256(time_stamped_token.encode("utf-8")).hexdigest()
    authentication = f"{user_id}:{hashed_token}"
    api_token = base64.b64encode(authentication.encode("utf-8")).decode("ascii")
    return {"api_token": api_token, "timestamp": timestamp}


def make_qc_headers() -> Dict[str, str]:
    if not QC_API_KEY or not QC_USER_ID:
        raise ValueError("Missing QuantConnect API credentials in environment variables.")
    token_data = get_api_token(QC_API_KEY, QC_USER_ID)
    return {
        "Authorization": f"Basic {token_data['api_token']}",
        "Timestamp": token_data["timestamp"],
    }


def update_chunk_status_in_bq(
    client: bigquery.Client,
    batch_id: str,
    old_bt_id: str,
    new_status: str,
    new_bt_id: str | None = None,
) -> None:
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    target_bt_id = new_bt_id or old_bt_id

    up_sql = f"""
    UPDATE `{PROJECT_ID}.{DATASET_ID}.{BATCH_TABLE}`
    SET status = '{new_status}', backtest_id = '{target_bt_id}', updated_at = CURRENT_TIMESTAMP()
    WHERE batch_id = '{batch_id}' AND (backtest_id = '{old_bt_id}' OR backtest_id = '{target_bt_id}')
    """
    try:
        client.query(up_sql).result()
        logging.info(f"Updated chunk status ({batch_id}, {target_bt_id}) -> {new_status}")
    except Exception as err:
        logging.warning(f"SQL UPDATE failed ({err}), using batch load insert fallback...")
        row_query = f"""
        SELECT algo_code, chunk_index, CAST(start_date AS STRING) as start_date, CAST(end_date AS STRING) as end_date, compile_id, CAST(created_at AS STRING) as created_at
        FROM `{PROJECT_ID}.{DATASET_ID}.{BATCH_TABLE}`
        WHERE batch_id = '{batch_id}' AND (backtest_id = '{old_bt_id}' OR backtest_id = '{target_bt_id}')
        LIMIT 1
        """
        try:
            res = list(client.query(row_query).result())
            if res:
                r = dict(res[0])
                new_row = [{
                    "batch_id": batch_id,
                    "backtest_id": target_bt_id,
                    "algo_code": r.get("algo_code", "4EVC"),
                    "chunk_index": int(r.get("chunk_index", 1)),
                    "start_date": str(r.get("start_date")),
                    "end_date": str(r.get("end_date")),
                    "status": new_status,
                    "compile_id": r.get("compile_id"),
                    "created_at": str(r.get("created_at")),
                    "updated_at": now_ts,
                }]
                table_ref = f"{PROJECT_ID}.{DATASET_ID}.{BATCH_TABLE}"
                job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
                client.load_table_from_json(new_row, table_ref, job_config=job_cfg).result()
                logging.info(f"[FALLBACK SUCCESS] Streamed status update via batch load: {new_status}")
        except Exception as fallback_err:
            logging.error(f"Fallback status update failed for ({batch_id}, {target_bt_id}): {fallback_err}")


def _build_symbol_struct(trade_obj: Dict[str, Any]) -> Dict[str, Any] | None:
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
            "permtick": und_obj.get("permtick"),
        } if und_obj else None
    }


def ingest_full_backtest_stats_to_bq(client: bigquery.Client, bt_resp: Dict[str, Any], bt_id: str, orders: List[Dict[str, Any]], trade_rows: List[Dict[str, Any]]) -> None:
    """Ingests data into ALL 15 BigQuery warehouse tables, writing placeholder NULL records when a section is empty."""
    bt_data = bt_resp.get("backtest", {})
    if not bt_data:
        return

    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")

    def _safe_insert(tbl_name: str, rows: List[Dict[str, Any]]) -> None:
        if not rows:
            return
        try:
            client.load_table_from_json(rows, f"{PROJECT_ID}.{DATASET_ID}.{tbl_name}", job_config=job_cfg).result()
            logging.info(f"Ingested {len(rows)} row(s) into {tbl_name} for backtest {bt_id}")
        except Exception as e:
            logging.warning(f"Error inserting into {tbl_name} for {bt_id}: {e}")

    # 1. BTOPResults
    res_row = [{
        "backtestId": bt_id, "name": bt_data.get("name"), "note": bt_data.get("note"),
        "organizationId": bt_data.get("organizationId"), "projectId": bt_data.get("projectId"),
        "completed": bt_data.get("completed"), "optimizationId": bt_data.get("optimizationId"),
        "tradeableDates": bt_data.get("tradeableDates"),
        "backtestStart": str(bt_data.get("backtestStart")) if bt_data.get("backtestStart") else None,
        "backtestEnd": str(bt_data.get("backtestEnd")) if bt_data.get("backtestEnd") else None,
        "created": str(bt_data.get("created")) if bt_data.get("created") else None,
        "snapshotId": bt_data.get("snapshotId"), "status": bt_data.get("status"),
        "error": bt_data.get("error"), "stacktrace": bt_data.get("stacktrace"),
        "progress": bt_data.get("progress"), "hasInitializeError": bt_data.get("hasInitializeError"),
        "nodeName": bt_data.get("nodeName"),
        "outOfSampleMaxEndDate": str(bt_data.get("outOfSampleMaxEndDate")) if bt_data.get("outOfSampleMaxEndDate") else None,
        "outOfSampleDays": bt_data.get("outOfSampleDays"), "_ingested_at": now_ts
    }]
    _safe_insert(RESULTS_TABLE, res_row)

    bt_name = bt_data.get("name") or bt_id

    # 2. BTOPTotalPerformancePortfolioStats & TradeStats & ClosedTrades
    total_perf = bt_data.get("totalPerformance", {}) or {}
    port_stats = total_perf.get("portfolioStatistics", {}) if isinstance(total_perf, dict) else {}
    port_row = [{
        "portfolioStatId": f"{bt_id}_tp_port", "backtestId": bt_id, "backtest_name": bt_name,
        "averageWinRate": port_stats.get("averageWinRate"), "averageLossRate": port_stats.get("averageLossRate"),
        "profitLossRatio": port_stats.get("profitLossRatio"), "winRate": port_stats.get("winRate"),
        "lossRate": port_stats.get("lossRate"), "expectancy": port_stats.get("expectancy"),
        "startEquity": port_stats.get("startEquity"), "endEquity": port_stats.get("endEquity"),
        "compoundingAnnualReturn": port_stats.get("compoundingAnnualReturn"), "drawdown": port_stats.get("drawdown"),
        "totalNetProfit": port_stats.get("totalNetProfit"), "sharpeRatio": port_stats.get("sharpeRatio"),
        "probabilisticSharpeRatio": port_stats.get("probabilisticSharpeRatio"), "sortinoRatio": port_stats.get("sortinoRatio"),
        "alpha": port_stats.get("alpha"), "beta": port_stats.get("beta"),
        "annualStandardDeviation": port_stats.get("annualStandardDeviation"), "annualVariance": port_stats.get("annualVariance"),
        "informationRatio": port_stats.get("informationRatio"), "trackingError": port_stats.get("trackingError"),
        "treynorRatio": port_stats.get("treynorRatio"), "portfolioTurnover": port_stats.get("portfolioTurnover"),
        "valueAtRisk99": port_stats.get("valueAtRisk99"), "valueAtRisk95": port_stats.get("valueAtRisk95"),
        "_ingested_at": now_ts
    }]
    _safe_insert(PORTFOLIO_STATS_TABLE, port_row)

    trade_stats = total_perf.get("tradeStatistics", {}) if isinstance(total_perf, dict) else {}
    trade_stat_row = [{
        "tradeStatId": f"{bt_id}_tp_trade", "backtestId": bt_id, "backtest_name": bt_name,
        "startDateTime": str(trade_stats.get("startDateTime")) if trade_stats.get("startDateTime") else None,
        "endDateTime": str(trade_stats.get("endDateTime")) if trade_stats.get("endDateTime") else None,
        "totalNumberOfTrades": trade_stats.get("totalNumberOfTrades"),
        "numberOfWinningTrades": trade_stats.get("numberOfWinningTrades"),
        "numberOfLosingTrades": trade_stats.get("numberOfLosingTrades"),
        "totalProfitLoss": trade_stats.get("totalProfitLoss"),
        "totalProfit": trade_stats.get("totalProfit"), "totalLoss": trade_stats.get("totalLoss"),
        "largestProfit": trade_stats.get("largestProfit"), "largestLoss": trade_stats.get("largestLoss"),
        "averageProfitLoss": trade_stats.get("averageProfitLoss"), "averageProfit": trade_stats.get("averageProfit"),
        "averageLoss": trade_stats.get("averageLoss"), "profitFactor": trade_stats.get("profitFactor"),
        "sharpeRatio": trade_stats.get("sharpeRatio"), "sortinoRatio": trade_stats.get("sortinoRatio"),
        "totalFees": trade_stats.get("totalFees"), "_ingested_at": now_ts
    }]
    _safe_insert(TRADE_STATS_TABLE, trade_stat_row)

    closed_trades = total_perf.get("closedTrades", []) if isinstance(total_perf, dict) else []
    if closed_trades:
        closed_rows = [{
            "tradeId": f"{bt_id}_closed_{idx}", "backtestId": bt_id, "backtest_name": bt_name,
            "symbol": _build_symbol_struct(ct),
            "entryTime": str(ct.get("entryTime")) if ct.get("entryTime") else None,
            "entryPrice": ct.get("entryPrice"), "direction": ct.get("direction"), "quantity": ct.get("quantity"),
            "exitTime": str(ct.get("exitTime")) if ct.get("exitTime") else None,
            "exitPrice": ct.get("exitPrice"), "profitLoss": ct.get("profitLoss"), "totalFees": ct.get("totalFees"),
            "mae": ct.get("mae"), "mfe": ct.get("mfe"), "duration": str(ct.get("duration")), "isWin": ct.get("isWin"),
            "_ingested_at": now_ts
        } for idx, ct in enumerate(closed_trades)]
    else:
        closed_rows = [{"tradeId": f"CLOSED_TRADE_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name, "_ingested_at": now_ts}]
    _safe_insert(CLOSED_TRADES_TABLE, closed_rows)

    # 3. BTOPParameterSet
    param_set = bt_data.get("parameterSet", {})
    param_rows = [{
        "parameterId": f"PARAM_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name,
        "parameters": json.dumps(param_set) if param_set else None, "_ingested_at": now_ts
    }]
    _safe_insert(PARAM_SET_TABLE, param_rows)

    # 4. BTOPResearchGuide
    guide = bt_data.get("researchGuide", {}) or {}
    guide_rows = [{
        "guideId": f"GUIDE_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name,
        "minutes": guide.get("minutes"), "backtestCount": guide.get("backtestCount"), "_ingested_at": now_ts
    }]
    _safe_insert(RESEARCH_GUIDE_TABLE, guide_rows)

    # 5. BTOPRuntimeStatistics
    runtime_stats = bt_data.get("runtimeStatistics", {}) or {}
    runtime_rows = [{
        "runtimeStatId": f"RUNTIME_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name,
        "equity": runtime_stats.get("Equity"), "fees": runtime_stats.get("Fees"),
        "netProfit": runtime_stats.get("Net Profit"), "return": runtime_stats.get("Return"),
        "_ingested_at": now_ts
    }]
    _safe_insert(RUNTIME_STATS_TABLE, runtime_rows)

    # 6. BTOPCharts
    charts = bt_data.get("charts", {}) or {}
    if charts:
        chart_rows = [{
            "chartId": f"CHART_{bt_id}_{idx}", "backtestId": bt_id, "backtest_name": bt_name,
            "name": c.get("name"), "seriesName": key, "_ingested_at": now_ts
        } for idx, (key, c) in enumerate(charts.items())]
    else:
        chart_rows = [{"chartId": f"CHART_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name, "_ingested_at": now_ts}]
    _safe_insert(CHARTS_TABLE, chart_rows)

    # 7. BTOPStatistics
    stats = bt_data.get("statistics", {}) or {}
    stats_rows = [{
        "statisticId": f"STAT_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name,
        "totalOrders": int(str(stats.get("Total Orders")).replace(",", "")) if stats.get("Total Orders") else None,
        "sharpeRatio": float(str(stats.get("Sharpe Ratio")).replace("%", "")) if stats.get("Sharpe Ratio") else None,
        "_ingested_at": now_ts
    }]
    _safe_insert(STATS_TABLE, stats_rows)

    # 8. BTOPRollingWindowPortfolioStats, TradeStats, ClosedTrades
    rw = bt_data.get("rollingWindow", {}) or {}
    rw_port_rows = [{"portfolioStatId": f"RW_PORT_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name, "_ingested_at": now_ts}]
    rw_trade_rows = [{"tradeStatId": f"RW_TRADE_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name, "_ingested_at": now_ts}]
    rw_closed_rows = [{"tradeId": f"RW_CLOSED_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name, "_ingested_at": now_ts}]
    _safe_insert(RW_PORTFOLIO_TABLE, rw_port_rows)
    _safe_insert(RW_TRADE_TABLE, rw_trade_rows)
    _safe_insert(RW_CLOSED_TABLE, rw_closed_rows)

    # 9. BTOPErrors
    err_msg = bt_data.get("error")
    err_rows = [{
        "errorId": f"ERR_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name,
        "message": err_msg, "stacktrace": bt_data.get("stacktrace"), "_ingested_at": now_ts
    }]
    _safe_insert(ERRORS_TABLE, err_rows)

    # 10. BTOPOrders
    if orders:
        order_rows = [{
            "order_pk": f"ORDER_{bt_id}_{o.get('id', idx)}", "backtestId": bt_id, "backtest_name": bt_name,
            "id": o.get("id", idx), "symbol": o.get("symbol", {}).get("value"),
            "price": o.get("price"), "quantity": o.get("quantity"), "_ingested_at": now_ts
        } for idx, o in enumerate(orders)]
    else:
        order_rows = [{"order_pk": f"ORDER_PK_{bt_id}", "backtestId": bt_id, "backtest_name": bt_name, "id": 0, "_ingested_at": now_ts}]
    _safe_insert(ORDERS_TABLE, order_rows)

    # 11. BTOPTrades
    if not trade_rows and closed_trades:
        bt_name = bt_data.get("name", bt_id)
        batch_id = bt_name.rsplit("_Y", 1)[0] if "_Y" in str(bt_name) else str(bt_name)
        chunk_index = int(str(bt_name)[-4:]) if str(bt_name)[-4:].isdigit() else 1
        
        for idx, ct in enumerate(closed_trades):
            ct_id = str(ct.get("id") or f"{bt_id}_ct_{idx}")
            sym_val = "UNKNOWN"
            if ct.get("symbols") and isinstance(ct.get("symbols"), list) and len(ct["symbols"]) > 0:
                s0 = ct["symbols"][0]
                sym_val = str(s0.get("value") or s0.get("permtick") or "UNKNOWN") if isinstance(s0, dict) else str(s0)
            elif ct.get("symbol"):
                s_obj = ct.get("symbol")
                sym_val = s_obj.get("value") if isinstance(s_obj, dict) else str(s_obj)

            entry_p = float(ct.get("entryPrice") or 0.0)
            exit_p = float(ct.get("exitPrice") or 0.0)
            qty = float(ct.get("quantity") or 0.0)
            pnl_val = float(ct.get("profitLoss") or 0.0)
            pnl_pct = round(pnl_val / (entry_p * qty), 5) if (entry_p * qty) > 0 else 0.0

            trade_rows.append({
                "pk": f"CLOUD_{bt_id}_{ct_id}_OPEN",
                "backtest_run_id": bt_id,
                "algo_code": "4EVC",
                "timestamp": str(ct.get("entryTime")) if ct.get("entryTime") else now_ts,
                "underlying": sym_val[:32],
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
            trade_rows.append({
                "pk": f"CLOUD_{bt_id}_{ct_id}_CLOSE",
                "backtest_run_id": bt_id,
                "algo_code": "4EVC",
                "timestamp": str(ct.get("exitTime")) if ct.get("exitTime") else now_ts,
                "underlying": sym_val[:32],
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
        _safe_insert(TRADES_TABLE, trade_rows)
    else:
        placeholder_trade = [{
            "pk": f"TRADE_PK_{bt_id}", "backtest_run_id": bt_id, "algo_code": "4EVC",
            "timestamp": now_ts, "action": "PLACEHOLDER", "qty": 0, "_ingested_at": now_ts
        }]
        _safe_insert(TRADES_TABLE, placeholder_trade)


def trigger_next_pending_chunk(client: bigquery.Client, batch_id: str) -> bool:
    """Finds the next PENDING chunk for a batch ID and triggers it on QC Cloud."""
    query = f"""
    WITH latest_chunks AS (
        SELECT *, ROW_NUMBER() OVER (PARTITION BY batch_id, chunk_index ORDER BY updated_at DESC, created_at DESC) as rn
        FROM `{PROJECT_ID}.{DATASET_ID}.{BATCH_TABLE}`
        WHERE batch_id = '{batch_id}'
    )
    SELECT batch_id, backtest_id, chunk_index, CAST(start_date AS STRING) as start_date, CAST(end_date AS STRING) as end_date, compile_id
    FROM latest_chunks
    WHERE rn = 1 AND status = 'PENDING'
    ORDER BY chunk_index ASC
    LIMIT 1
    """
    try:
        results = list(client.query(query).result())
        if not results:
            logging.info(f"No more pending chunks for batch '{batch_id}'. Batch is 100% COMPLETE!")
            return False

        next_chunk = dict(results[0])
        chunk_placeholder = next_chunk["backtest_id"]
        compile_id = next_chunk.get("compile_id")
        start_date = next_chunk["start_date"]
        end_date = next_chunk["end_date"]

        if not compile_id:
            logging.warning(f"Missing compile_id for {chunk_placeholder}.")
            return False

        url_create = "https://www.quantconnect.com/api/v2/backtests/create"
        payload = {
            "projectId": int(QC_PROJECT_ID),
            "compileId": compile_id,
            "backtestName": chunk_placeholder,
            "parameters": [
                {"key": "exec.start_date", "value": start_date},
                {"key": "exec.end_date", "value": end_date},
                {"key": "algo.is_hdbt", "value": "true"},
                {"key": "algo.pass_all", "value": "true"},
                {"key": "univ.coarse.max_symbols", "value": "4000"}
            ]
        }
        resp = requests.post(url_create, headers=make_qc_headers(), json=payload, timeout=30)
        data = resp.json()
        if data.get("success"):
            bt_info = data.get("backtest", {})
            real_hex = bt_info.get("backtestId") or bt_info.get("id") or chunk_placeholder
            update_chunk_status_in_bq(client, batch_id, chunk_placeholder, "RUNNING", new_bt_id=real_hex)
            logging.info(f"Auto-triggered next chunk {chunk_placeholder} -> Hex ID: {real_hex}")
            return True
        else:
            logging.error(f"Failed to trigger chunk {chunk_placeholder}: {data}")
            return False
    except Exception as e:
        logging.error(f"Error in trigger_next_pending_chunk for batch {batch_id}: {e}")
        return False


def handle_launch_mode(client: bigquery.Client, payload: Dict[str, Any]) -> tuple[str, int]:
    """Serverlessly compiles project and launches an HDBT multi-period batch run on QC Cloud."""
    algo_code = payload.get("algo", "4EVC")
    algo_version = str(payload.get("version", "1.0"))
    max_symbols = str(payload.get("max_symbols", 4000))
    years = payload.get("years", [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
    project_id = int(payload.get("project_id", QC_PROJECT_ID))

    logging.info(f"[HDBT Launch] Initiating compilation on QC Cloud for project {project_id} (max_symbols: {max_symbols})...")
    url_compile = "https://www.quantconnect.com/api/v2/compile/create"
    res = requests.post(url_compile, headers=make_qc_headers(), json={"projectId": project_id}, timeout=30)
    data = res.json()
    if not data.get("success"):
        return json.dumps({"error": f"Compilation failed to start: {data}"}), 500

    compile_id = data.get("compileId")
    state = data.get("state")
    logging.info(f"[HDBT Launch] Compilation ID: {compile_id} (Initial state: {state})")

    # Wait for compilation completion (up to 60s)
    url_compile_read = "https://www.quantconnect.com/api/v2/compile/read"
    start_t = time.time()
    while state not in ["BuildSuccess", "BuildError"]:
        if time.time() - start_t > 60:
            return json.dumps({"error": "Compilation timed out after 60s"}), 500
        time.sleep(2)
        r = requests.post(url_compile_read, headers=make_qc_headers(), json={"projectId": project_id, "compileId": compile_id}, timeout=30)
        state = r.json().get("state")

    if state != "BuildSuccess":
        return json.dumps({"error": f"Compilation failed with state: {state}"}), 500

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    batch_id = f"HDBT_{algo_code}_V{algo_version}_{timestamp}"
    logging.info(f"[HDBT Launch] Successfully compiled! Batch ID: {batch_id}")

    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    chunk_records = []

    # Launch Chunk 1 and queue remaining chunks as PENDING
    for idx, yr in enumerate(years, start=1):
        start_date = f"{yr}-01-01"
        end_date = f"{yr}-12-31"
        chunk_name = f"{batch_id}_Y{yr}"

        if idx == 1:
            url_create = "https://www.quantconnect.com/api/v2/backtests/create"
            bt_payload = {
                "projectId": project_id,
                "compileId": compile_id,
                "backtestName": chunk_name,
                "parameters": [
                    {"key": "exec.start_date", "value": start_date},
                    {"key": "exec.end_date", "value": end_date},
                    {"key": "algo.is_hdbt", "value": "true"},
                    {"key": "algo.pass_all", "value": "true"},
                    {"key": "univ.coarse.max_symbols", "value": max_symbols}
                ]
            }
            resp = requests.post(url_create, headers=make_qc_headers(), json=bt_payload, timeout=30)
            bt_data = resp.json()
            if bt_data.get("success"):
                bt_info = bt_data.get("backtest", {})
                hex_id = bt_info.get("backtestId") or bt_info.get("id") or chunk_name
                chunk_records.append({
                    "batch_id": batch_id, "backtest_id": hex_id, "algo_code": algo_code,
                    "chunk_index": idx, "start_date": start_date, "end_date": end_date,
                    "status": "RUNNING", "compile_id": compile_id, "backtest_name": chunk_name,
                    "created_at": now_ts, "updated_at": now_ts
                })
            else:
                logging.warning(f"[HDBT Launch] Backtest creation queued as PENDING for chunk 1 (node busy or pending): {bt_data}")
                chunk_records.append({
                    "batch_id": batch_id, "backtest_id": chunk_name, "algo_code": algo_code,
                    "chunk_index": idx, "start_date": start_date, "end_date": end_date,
                    "status": "PENDING", "compile_id": compile_id, "backtest_name": chunk_name,
                    "created_at": now_ts, "updated_at": now_ts
                })
        else:
            chunk_records.append({
                "batch_id": batch_id, "backtest_id": chunk_name, "algo_code": algo_code,
                "chunk_index": idx, "start_date": start_date, "end_date": end_date,
                "status": "PENDING", "compile_id": compile_id, "backtest_name": chunk_name,
                "created_at": now_ts, "updated_at": now_ts
            })

    # Register all chunk records in BigQuery
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{BATCH_TABLE}"
    job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    client.load_table_from_json(chunk_records, table_ref, job_config=job_cfg).result()

    return json.dumps({
        "status": "launched",
        "batch_id": batch_id,
        "algo_code": algo_code,
        "compile_id": compile_id,
        "total_chunks": len(years),
        "chunk_1_status": chunk_records[0]["status"] if chunk_records else "UNKNOWN",
        "chunk_1_backtest_id": chunk_records[0]["backtest_id"] if chunk_records else None
    }), 200


@functions_framework.http
def handle_batch_poll(request: Any) -> tuple[str, int]:
    """HTTP Cloud Function entrypoint called by Cloud Scheduler or HTTP POST."""
    if not QC_API_KEY or not QC_USER_ID:
        logging.error("Missing QuantConnect API credentials in environment variables.")
        return json.dumps({"error": "Missing credentials"}), 500

    client = bigquery.Client(project=PROJECT_ID)

    req_json = request.get_json(silent=True) or {}
    req_args = request.args or {}
    action = req_json.get("action") or req_args.get("action") or "poll"

    if action == "launch":
        return handle_launch_mode(client, req_json)

    # Polling & Recovery Mode (default cron job)
    query = f"""
    WITH latest_chunks AS (
        SELECT *, ROW_NUMBER() OVER (PARTITION BY batch_id, chunk_index ORDER BY updated_at DESC, created_at DESC) as rn
        FROM `{PROJECT_ID}.{DATASET_ID}.{BATCH_TABLE}`
    )
    SELECT batch_id, backtest_id, algo_code, chunk_index, CAST(start_date AS STRING) as start_date, CAST(end_date AS STRING) as end_date, status, compile_id
    FROM latest_chunks
    WHERE rn = 1 AND status IN ('PENDING', 'RUNNING')
    ORDER BY created_at ASC, chunk_index ASC
    """
    try:
        results = list(client.query(query).result())
        pending_chunks = [dict(r) for r in results]
    except Exception as e:
        logging.info(f"No pending chunks or table query error: {e}")
        return json.dumps({"status": "no_pending_chunks", "message": str(e)}), 200

    if not pending_chunks:
        logging.info("No active batch chunks found.")
        return json.dumps({"status": "ok", "processed": 0}), 200

    # Group active chunks by batch_id
    batches: Dict[str, List[Dict[str, Any]]] = {}
    for c in pending_chunks:
        bid = c["batch_id"]
        batches.setdefault(bid, []).append(c)

    processed_count = 0

    for batch_id, chunk_list in batches.items():
        running_chunks = [c for c in chunk_list if c["status"] == "RUNNING"]

        if running_chunks:
            # Poll status of active running chunk
            for chunk in running_chunks:
                bt_id = chunk["backtest_id"]
                chunk_idx = chunk["chunk_index"]

                read_url = "https://www.quantconnect.com/api/v2/backtests/read"
                payload = {"projectId": int(QC_PROJECT_ID), "backtestId": bt_id}

                try:
                    resp = requests.post(read_url, headers=make_qc_headers(), json=payload, timeout=15)
                    if resp.status_code != 200:
                        logging.warning(f"QC read returned HTTP {resp.status_code} for chunk {bt_id}.")
                        continue

                    bt_resp = resp.json()
                    if not bt_resp.get("success", False):
                        logging.warning(f"QC backtest read unsuccessful for {bt_id}: {bt_resp}")
                        continue

                    bt_data = bt_resp.get("backtest", {})
                    if not bt_data.get("completed", False) and bt_data.get("progress", 0.0) < 1.0:
                        logging.info(f"Chunk {bt_id} still running ({bt_data.get('progress', 0.0)*100:.1f}%).")
                        continue

                    # Completed! Fetch orders in 100-order paginated chunks
                    orders_url = "https://www.quantconnect.com/api/v2/backtests/orders/read"
                    orders = []
                    start_idx = 0
                    step = 100

                    while True:
                        end_idx = start_idx + step
                        orders_payload = {"start": start_idx, "end": end_idx, "projectId": int(QC_PROJECT_ID), "backtestId": bt_id}
                        ord_resp = requests.post(orders_url, headers=make_qc_headers(), json=orders_payload, timeout=30)
                        if ord_resp.status_code != 200:
                            break
                        ord_data = ord_resp.json()
                        if not ord_data.get("success"):
                            break
                        page_orders = ord_data.get("orders", [])
                        if isinstance(page_orders, dict):
                            page_orders = list(page_orders.values())
                        if not page_orders:
                            break
                        orders.extend(page_orders)
                        start_idx = end_idx
                        time.sleep(0.1)

                    # 1. Primary Strategy Trade Record Ingestion: Fetch algorithm logs from QC API
                    log_url = "https://www.quantconnect.com/api/v2/backtests/read/log"
                    trade_rows = []
                    log_start = 0
                    log_step = 200

                    while True:
                        log_payload = {
                            "projectId": int(QC_PROJECT_ID),
                            "backtestId": bt_id,
                            "start": log_start,
                            "end": log_start + log_step,
                            "query": ""
                        }
                        log_resp = requests.post(log_url, headers=make_qc_headers(), json=log_payload, timeout=30)
                        if log_resp.status_code != 200:
                            break
                        log_json = log_resp.json()
                        if not log_json.get("success"):
                            break
                        page_logs = log_json.get("logs", [])
                        if not page_logs:
                            break

                        for line in page_logs:
                            if "[BIGQUERY_TRADE_RECORD]" in line:
                                try:
                                    parts = line.split("[BIGQUERY_TRADE_RECORD] ")
                                    if len(parts) > 1:
                                        rec = json.loads(parts[1].strip())
                                        rec["backtestId"] = bt_id
                                        rec["backtest_name"] = bt_name
                                        rec["batch_id"] = batch_id
                                        rec["chunk_index"] = chunk_idx
                                        rec["_ingested_at"] = now_ts
                                        allowed_keys = {
                                            "pk", "trade_id", "backtestId", "backtest_name", "algo_code", "timestamp",
                                            "underlying", "action", "qty", "strike", "near_expiry", "far_expiry",
                                            "vol_ratio", "slope", "ivrv_ratio", "earnings_date", "entry_price",
                                            "exit_price", "pnl", "exit_reason", "parameters", "batch_id", "chunk_index", "_ingested_at"
                                        }
                                        clean_rec = {k: v for k, v in rec.items() if k in allowed_keys}
                                        trade_rows.append(clean_rec)
                                except Exception as parse_err:
                                    logging.warning(f"Error parsing BIGQUERY_TRADE_RECORD log line: {parse_err}")

                        if len(page_logs) < log_step:
                            break
                        log_start += log_step
                        time.sleep(0.05)

                    # 2. Secondary Fallback: Reconstruct trades from orders if log ingestion returned 0 rows
                    if not trade_rows:
                        open_queues = {}
                        counter = 0

                        def _parse_tag(t_str: str) -> dict:
                            if t_str and isinstance(t_str, str) and t_str.strip().startswith("{") and t_str.strip().endswith("}"):
                                try:
                                    return json.loads(t_str.strip())
                                except Exception:
                                    return {}
                            return {}

                        for o in orders:
                            status = o.get("status")
                            if status not in [3, "filled", "Filled"]:
                                continue

                            raw_tag = str(o.get("tag", ""))
                            tag_data = _parse_tag(raw_tag)

                            is_tagged_open = raw_tag.startswith("OPEN:") or "leg" in tag_data or "ivrv" in tag_data
                            is_tagged_close = raw_tag.startswith("CLOSE:") or "FLATTEN" in raw_tag

                            qty = abs(float(o.get("quantity") or 0.0))
                            price = float(o.get("price") or 0.0)
                            ts = str(o.get("time") or now_ts)
                            sym_obj = o.get("symbol") or {}
                            sym_val = sym_obj.get("value") if isinstance(sym_obj, dict) else str(sym_obj)

                            underlying = tag_data.get("u")
                            if not underlying:
                                if isinstance(sym_obj, dict) and sym_obj.get("underlying"):
                                    underlying = sym_obj["underlying"].get("value")
                                if not underlying and sym_val:
                                    import re
                                    m = re.match(r'^([A-Z]+)', sym_val.strip())
                                    if m:
                                        underlying = m.group(1)
                            if not underlying:
                                underlying = "UNKNOWN"

                            if underlying == "UA":
                                underlying = "UAA"

                            vol_val = float(tag_data.get("vol_ratio")) if tag_data.get("vol_ratio") is not None else None
                            slope_val = float(tag_data.get("slope")) if tag_data.get("slope") is not None else None
                            ivrv_val = float(tag_data.get("ivrv")) if tag_data.get("ivrv") is not None else (float(tag_data.get("ivrv_ratio")) if tag_data.get("ivrv_ratio") is not None else None)
                            strike_val = float(tag_data.get("k")) if tag_data.get("k") is not None else None
                            near_val = str(tag_data.get("near")) if tag_data.get("near") else None
                            far_val = str(tag_data.get("far")) if tag_data.get("far") else None
                            edate_val = str(tag_data.get("edate")) if tag_data.get("edate") else None

                            if is_tagged_open or not raw_tag:
                                counter += 1
                                trade_id = f"CLOUD_{bt_id}_{underlying}_{counter}"
                                pk = f"{trade_id}_OPEN"
                                rec = {
                                    "pk": pk, "trade_id": trade_id, "backtestId": bt_id, "backtest_name": bt_name,
                                    "algo_code": chunk.get("algo_code", "4EVC"), "timestamp": ts,
                                    "underlying": underlying, "action": "OPEN", "qty": int(qty),
                                    "strike": strike_val, "near_expiry": near_val, "far_expiry": far_val,
                                    "vol_ratio": vol_val, "slope": slope_val, "ivrv_ratio": ivrv_val,
                                    "earnings_date": edate_val, "entry_price": round(price, 5), "exit_price": 0.0, "pnl": 0.0,
                                    "exit_reason": "", "parameters": json.dumps(tag_data, separators=(',', ':')) if tag_data else "{}",
                                    "batch_id": batch_id, "chunk_index": chunk_idx, "_ingested_at": now_ts
                                }
                                open_queues.setdefault(underlying, []).append(rec)
                                trade_rows.append(rec)
                            elif is_tagged_close and open_queues.get(underlying):
                                open_rec = open_queues[underlying].pop(0)
                                entry_p = open_rec["entry_price"]
                                exit_p = round(price, 5)
                                pnl_pct = round((exit_p - entry_p) / entry_p, 5) if entry_p > 0 else 0.0
                                trade_rows.append({
                                    "pk": open_rec["pk"].replace("_OPEN", "_CLOSE"), "trade_id": open_rec["trade_id"],
                                    "backtestId": bt_id, "backtest_name": bt_name, "algo_code": chunk.get("algo_code", "4EVC"),
                                    "timestamp": ts, "underlying": underlying, "action": "CLOSE", "qty": int(qty),
                                    "strike": open_rec.get("strike"), "near_expiry": open_rec.get("near_expiry"),
                                    "far_expiry": open_rec.get("far_expiry"), "vol_ratio": open_rec.get("vol_ratio"),
                                    "slope": open_rec.get("slope"), "ivrv_ratio": open_rec.get("ivrv_ratio"),
                                    "earnings_date": open_rec.get("earnings_date"), "entry_price": entry_p,
                                    "exit_price": exit_p, "pnl": pnl_pct, "exit_reason": raw_tag,
                                    "parameters": open_rec.get("parameters", "{}"), "batch_id": batch_id,
                                    "chunk_index": chunk_idx, "_ingested_at": now_ts
                                })

                    if trade_rows:
                        table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TRADES_TABLE}"
                        job_cfg = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
                        client.load_table_from_json(trade_rows, table_ref, job_config=job_cfg).result()

                    # Ingest full metadata and portfolio stats into ALL 15 BigQuery tables
                    ingest_full_backtest_stats_to_bq(client, bt_resp, bt_id, orders, trade_rows)

                    # Mark chunk COMPLETED in BigQuery
                    update_chunk_status_in_bq(client, batch_id, bt_id, "COMPLETED")
                    processed_count += 1
                    logging.info(f"Successfully processed and completed chunk ({batch_id}, {bt_id}).")

                    # Instantly trigger next PENDING chunk
                    trigger_next_pending_chunk(client, batch_id)

                except Exception as err:
                    logging.error(f"Error processing RUNNING chunk {bt_id}: {err}")
        else:
            # Recovery Mode: Batch has PENDING chunks but NO RUNNING chunk!
            logging.info(f"Batch '{batch_id}' has no RUNNING chunk. Auto-triggering next PENDING chunk...")
            triggered = trigger_next_pending_chunk(client, batch_id)
            if triggered:
                processed_count += 1

    return json.dumps({"status": "ok", "processed": processed_count}), 200
