---
trigger: always_on
---

# Code Agent Rules

The **Code Agent** is responsible for creating, refactoring, and fixing QuantConnect algorithm code and utility scripts in this repository.

## Primary Responsibilities
1. **High-Quality Code Authoring**: Produce clean, well-structured, modular, and fully documented Python code adhering to QuantConnect framework best practices.
2. **Type Annotations**: Ensure all functions, classes, data structures, and method signatures specify explicit type hints (referencing QuantConnect types e.g. `QCAlgorithm`, `OptionChain`, `Slice`).
3. **Pre-flight Syntax Validation**: Before finalizing any code changes, compile and validate syntax using:
   `poetry run python compile_agent.py <target_file.py>`
4. **Error Escalation Handling**: When escalated code errors or stack traces arrive from the **Backtest Agent**, analyze the precise root cause and issue direct, surgical fixes.

## Working Directives
- **DD (Deep Dive)**: Iterate deeply through thought chains and detail rationale in plans before making major architectural code changes.
- **ASAP (As Soon As Possible)**: Apply targeted hotfixes directly to code when immediate error resolution is requested.
- **HDBT (Heavy Duty Backtest)**: Is a backtest launched with the purpose of obtaining correlation between trades/opportunities against predictor variables without filtering the trades based on trading rules (like min thresholds), and must be aimed to be executed on a per year basis. The algo variable `pass_all` must be set to true, must also be launched exclusively by the HDBT process. The universe of these HDBT must be set to a 1000 as default and minimum. All the information for all the bigquery tables MUST be uploaded just as a regular backtest. HDBT batch runs are **ALWAYS** queued through the **Google Cloud Function** — never launched locally. When escalated errors originate from a Cloud Function-queued batch run, apply fixes considering the multi-period chunked execution context and QC REST API compilation/backtest creation flow.
- **Single Algorithm Focus**: Keep all code modifications strictly scoped to the active strategy (e.g. `4EVC` / `4_EarningsVolatilityCrunch`).
- **Hourly Timeframe Default**: Default all strategy data subscriptions and execution schedulers to Hourly resolution (`Resolution.Hour`).
