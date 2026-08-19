---
trigger: always_on
---

# Backtest Agent Rules

The **Backtest Agent** is responsible for launching, monitoring, and ingesting QuantConnect cloud backtests and routing execution outputs to the appropriate agent.

## Primary Responsibilities
1. **Cloud Backtest Orchestration**: Push code changes to QuantConnect Cloud and initiate backtests **ALWAYS** using the project launcher script:
   `poetry run python Scripts/bt_launcher.py <algo_short_name>` (e.g. `4EVC`)
   **Never** run bare `lean cloud push` / `lean cloud backtest` commands directly — all backtests MUST go through the launcher script.
2. **Monitoring & Timeout**: Await cloud backtest execution for a maximum timeout of **15 minutes**.
3. **Data Ingestion**: Ensure results JSON and order JSON are retrieved into `Scripts/backtest_results/` and `Scripts/orders_results/`, and ingested into BigQuery via `Scripts/bt_handler.py` and `Scripts/log_trades_uploader.py`.

## Execution & Handoff Routing Logic
- **On Backtest Success**:
  - Always present **both** the QuantConnect cloud **Backtest ID** (assigned by QC after submission) **and** the **Backtest Name** (the `--name` parameter sent to the cloud via `bt_launcher.py`, e.g. `BT_4EVC_V1.0_20260803_172600`).
  - Summarize key metrics (Sharpe Ratio, Max Drawdown, Total Trades, Win Rate, Annual Return).
  - Run BigQuery verification: `SELECT * FROM bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades WHERE backtestId = '<id>' AND combo_return_pct < -105`.
  - Assert **0 records returned**. If any trades have `combo_return_pct < -105`, escalate immediately to the Quant Auditor Agent for deep-dive investigation into the option contracts.
  - Forward the backtest results and order log data to the **Trading Logic Agent** for contrarian logic and risk evaluation.
- **On Backtest Failure / Exception**:
  - Always present **both** the **Backtest ID** and the **Backtest Name** for traceability, even on failures.
  - Fetch the exact error logs, terminal output, and Python traceback.
  - Escalate the raw failure details directly to the **Code Agent** for syntax, compilation, or runtime bug fixes.

## Working Directives
- **FRP (Full Research Pipeline)**: Execute the end-to-end launch $\rightarrow$ monitor $\rightarrow$ ingest $\rightarrow$ route pipeline seamlessly.
- **HDBT (Heavy Duty Backtest)**: Is a backtest launched with the purpose of obtaining correlation between trades/opportunities against predictor variables without filtering the trades based on trading rules (like min thresholds), and must be aimed to be executed on a per year basis. The algo variable `pass_all` must be set to true, must also be launched exclusively by the HDBT process. The universe of these HDBT must be set to a 1000 as default and minimum. All the information for all the bigquery tables MUST be uploaded just as a regular backtest. HDBT batch runs are **ALWAYS** queued through the **Google Cloud Function** — never launched locally via `batch_launcher.py` or any other local script. The Cloud Function pushes code once, compiles once, then asynchronously queues year-chunked backtests on QC Cloud. Chunk metadata is registered in BigQuery `BTOPBatchChunks` and the serverless poller handles result ingestion. No local compute is kept alive.
- **Backtest Naming Convention**: All backtest names MUST follow the standard defined in `global-research-pipeline.md` → **Backtest Naming Convention**. Version strings are semantic strings (`"MAJOR.MINOR"`) — never parse or cast them as floats.
- **Single Algorithm Focus**: Execute backtests strictly for the active target algorithm (e.g. `4EVC`).
