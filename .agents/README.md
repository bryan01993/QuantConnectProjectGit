# QuantConnect Strategy Research Agent Guidelines & Rules

## Core Operational Protocols

### 1. Mandatory 4EVC Consolidated Trade Return Audit Gate (< -105% Loss Rule)
Whenever a backtest (regular backtest or HDBT chunk) for `4EVC` is executed and ingested into BigQuery dataset `bav-personal-cloud.develop` (`europe-west1`), the **Quant Verification & Risk Auditor Agent** MUST run the following mandatory verification SQL query:

```sql
SELECT * 
FROM `bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades` 
WHERE backtestId = '<backtest_id>' AND combo_return_pct < -105
```

* **Quantitative Threshold Standard**: **STRICTLY ZERO (0) RECORDS**.
* **Mandatory Escalation & Deep Dive Protocol**: If ANY consolidated trade exhibits a loss worse than **-105%** (`combo_return_pct < -105`), the Quant Verification Agent MUST:
  1. Initiate an immediate Deep Dive (DD).
  2. Inspect the exact option contracts (`short_leg_symbol`, `long_leg_symbol`), entry/exit prices, bid-ask quotes, and order fill events.
  3. Identify the precise root cause mechanism (e.g. illiquid bid-ask spread friction, single-leg orphan sweeps, or deep ITM liquidation debit).
  4. Continuously review the cause and pass the exact surgical fix instructions to the **Code Agent** until the backtest produces **0 records** below -105%.

---

### 2. General Pipeline Protocols

* **BigQuery Default Region**: Everything created, queried, modified, or executed in Google BigQuery MUST ALWAYS default to region/location `europe-west1`.
* **Percentage Return Standard**: All trade returns, factor correlations, deciles, and risk audits MUST be evaluated in percentage terms (`combo_return_pct` / `return_pct`), NEVER raw dollar PnL.
* **Single Algorithm Focus**: Keep all code and audit modifications strictly scoped to the active strategy (`4EVC` / `4_EarningsVolatilityCrunch`).
