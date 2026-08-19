---
name: full-research-pipeline
description: Triggers when executing an automated end-to-end QuantConnect cloud backtest, data ingestion, and result analysis pipeline (FRP).
---

# Full Research Pipeline (FRP) Skill

Use this skill when performing a **Full Research Pipeline (FRP)** run on a QuantConnect strategy folder (e.g. `4_EarningsVolatilityCrunch` / `4EVC`).

## Pipeline Execution Steps

1. **Pre-flight Validation**:
   - Run compilation check:
     `poetry run python compile_agent.py <folder>/main.py`

2. **Launch Cloud Backtest**:
   - Execute the backtest launcher script with the algorithm short name (e.g. `4EVC`):
     `poetry run python Scripts/bt_launcher.py <algo_short_name>`
   - **ALWAYS** use this launcher script. **Never** run bare `lean cloud push` / `lean cloud backtest` commands directly.
   - This script automatically pushes the code to QuantConnect Cloud (`lean cloud push`) and triggers the cloud backtest (`lean cloud backtest`).

3. **Await Completion & Ingest Results**:
   - Monitor the cloud backtest process (maximum wait time: **15 minutes**).
   - Once completed, `bt_launcher.py` triggers `bt_handler.py`, which:
     - Downloads backtest metrics JSON to `Scripts/backtest_results/<backtest_id>.json`.
     - Downloads all orders JSON to `Scripts/orders_results/<backtest_id>_orders.json`.
     - Ingests metrics into Google BigQuery via `Scripts/BigQuery/db_operator.py`.
   - Optionally run trade log uploader:
     `poetry run python Scripts/log_trades_uploader.py`

4. **Result Routing**:
   - **Always present both** the QuantConnect cloud **Backtest ID** and the **Backtest Name** (the `--name` parameter sent via `bt_launcher.py`, e.g. `BT_4EVC_V1.0_20260803_172600`) in every summary or report.
   - **If successful**: Forward backtest metrics and order logs to the **Trading Logic Agent** for contrarian logic evaluation and risk/performance critique.
   - **If failed/error**: Extract traceback and logs from `Scripts/backtest_logs/` or terminal output and escalate to the **Code Agent** for bug fixes.

## Heavy Duty Backtest (HDBT) — Batch Mode

Use HDBT instead of the standard FRP when the user requests a multi-period, chunked cloud backtest spanning multiple years.

1. **Queue via Google Cloud Function**:
   - HDBT batch runs are **ALWAYS** queued through the **Google Cloud Function** — never launched locally via `batch_launcher.py` or any other local script.
   - The Cloud Function is invoked with the algorithm short name and year list.
2. **What the Cloud Function Does**:
   - Pushes code once to QuantConnect Cloud.
   - Compiles the project once via QC REST API to obtain a `compileId`.
   - Asynchronously creates year-chunked backtests via QC REST API.
   - Registers all chunk metadata into BigQuery table `BTOPBatchChunks`.
   - No local compute is kept alive — the entire HDBT lifecycle is serverless.
3. **Serverless Polling & Ingestion**:
   - The serverless poller (`Scripts/BigQuery/qc_batch_poller.py`) picks up completed chunks and ingests results into BigQuery.
4. **Result Routing**: Same as FRP step 4 above, applied per chunk and aggregated across the full batch.

