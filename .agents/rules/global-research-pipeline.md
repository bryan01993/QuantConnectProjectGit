---
trigger: always_on
---

# Global Research Pipeline Rules

These rules apply across all agents and research workflows within this QuantConnect codebase.

## Standard Directives & Acronyms
- **DD (Deep Dive)**: When requested or performing deep analysis, iterate deeply in every single thought chain and summarize in detail within implementation plans before writing code. When presenting backtest results during a DD, always include **both** the QuantConnect cloud **Backtest ID** and the **Backtest Name** (the `--name` parameter sent to the cloud via `bt_launcher.py`).
- **ASAP (As Soon As Possible)**: Execute direct, targeted fixes/hotfixes straight to code without creating extensive plans. Focus strictly on speed and correctness of the targeted issue.
- **FRP (Full Research Pipeline)**: Execute an end-to-end cloud backtesting workflow:
  1. Trigger backtest **ALWAYS** using the launcher script: `poetry run python Scripts/bt_launcher.py <algo_short_name>`. **Never** run bare `lean cloud push` / `lean cloud backtest` commands directly.
  2. Await backtest completion (up to maximum 15 minutes).
  3. Fetch and ingest results JSON and order JSON into local/BigQuery database (`bt_handler.py`, `log_trades_uploader.py`).
  4. Perform thorough analysis of backtest results and trade logs.
- **HDBT (Heavy Duty Backtest)**: Is a backtest launched with the purpose of obtaining correlation between trades/opportunities against predictor variables without filtering the trades based on trading rules (like min thresholds), and must be aimed to be executed on a per year basis. The algo variable `pass_all` must be set to true, must also be launched exclusively by the HDBT process. The universe of these HDBT must be set to a 1000 as default and minimum. All the information for all the bigquery tables MUST be uploaded just as a regular backtest. HDBT batch runs are **ALWAYS** queued through the **Google Cloud Function** — never launched locally via `batch_launcher.py` or any other local script:
  1. The Cloud Function pushes code once, compiles once via QC REST API, then asynchronously creates year-chunked backtests.
  2. Chunk metadata is registered into BigQuery table `BTOPBatchChunks`.
  3. The serverless poller (`Scripts/BigQuery/qc_batch_poller.py`) ingests completed chunk results into BigQuery.
  4. No local compute is kept alive — the entire HDBT lifecycle is serverless.

## Core Protocols
- **BigQuery Default Region Standard**: ALL operations, queries, table creations, dataset interactions, and execution scripts involving Google BigQuery MUST ALWAYS default to region/location **`europe-west1`**.
- **Percentage Return Standard (Zero-Dollar PnL Rule)**: All profit, loss, trade return, decile monotonicity, regression analysis, risk metrics, and drawdowns MUST be evaluated strictly in **percentage terms (`return_pct` / `%`)**, NEVER in raw dollar amounts ($).
- **Mandatory 4EVC Trade Loss Verification Rule (< -105% Rule)**: Once a backtest is uploaded to BigQuery, verify via `SELECT * FROM bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades WHERE backtestId = '<id>' AND combo_return_pct < -105` that there are **STRICTLY ZERO (0) TRADES** with losses worse than **-105%**. Any violation requires the Quant Agent to delve deeper into the root cause, inspect the specific option contracts, and pass surgical fixes to the Code Agent until zero records remain.
- **Single Algorithm Focus**: Whenever discussing or optimizing an algorithm, maintain strict focus on the active algorithm (e.g., `4EVC` / `4_EarningsVolatilityCrunch`) without switching to another algorithm unless explicitly instructed by the user.
- **Timeframe Preference**: By default, design, configure, and parameterize strategies to target the **Hour** (hourly) resolution/timeframe for data subscriptions and scheduled execution.
- **Delimited Responsibilities**: Maintain clear and precise agent boundaries. Do not attempt to solve problems outside the specific scope of your assigned agent role.


## Backtest Naming Convention

All backtest names MUST follow this standardized format. **Version strings (`ALGO_VERSION`) are semantic strings (`"MAJOR.MINOR"`, e.g. `"1.0"`, `"2.1"`) — NEVER parse or cast them as floats.**

### Format

```
{PREFIX}_{ALGO_SHORT_NAME}_V{VERSION}_{YYYYMMDD}_{HHMMSS}[_Y{YYYY}]
```

| Segment | Description | Source |
|---|---|---|
| `PREFIX` | `BT` for regular backtests, `HDBT` for heavy duty backtests | Fixed per run type |
| `ALGO_SHORT_NAME` | Algorithm short identifier | `AlgoConfig.yaml` → `ALGO_SHORT_NAME` |
| `V{VERSION}` | Semantic version string, verbatim from config | `AlgoConfig.yaml` → `ALGO_VERSION` |
| `YYYYMMDD_HHMMSS` | Launch timestamp | Generated at launch time |
| `_Y{YYYY}` | Year chunk suffix (HDBT chunk names only) | Derived from `--years` arg |

### Examples

- **Regular backtest**: `BT_4EVC_V1.0_20260805_194500`
- **HDBT batch ID**: `HDBT_4EVC_V1.0_20260805_194500`
- **HDBT chunk name**: `HDBT_4EVC_V1.0_20260805_194500_Y2020`
