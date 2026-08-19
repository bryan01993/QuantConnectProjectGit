---
name: trading-logic-optimizer
description: Triggers when the user or agent needs to optimize, parameterize, refactor, or type-hint a QuantConnect strategy main.py file.
---

# QuantConnect Trading Logic & Optimization Skill

Use this skill when optimizing, parameterizing, refactoring, or adding type annotations to QuantConnect algorithms located within their respective strategy folders (e.g., `4_EarningsVolatilityCrunch/main.py`).

## Guidelines & Best Practices
- **Contrarian Evaluation**: Evaluate algorithm design critically against backtest results. Challenge assumptions on order entry/exit rules, option chain filtering, and risk limits.
- **Parameterization**: Ensure key trading parameters, thresholds, lookback periods, and capital allocations are parameterized using `self.GetParameter()` or reading from configuration files (`Resources/AlgoConfig.yaml` / `config.json`).
- **Type Annotations**: Add explicit type annotations for all function parameters, return types, and class attributes referencing QuantConnect types in `Docu/combined_documentation.pyi`.
- **Hourly Timeframe Default**: Always configure, code, and test strategies using the **Hour** (hourly) timeframe resolution for data subscriptions and scheduler events by default.

## Research Directives
- **DD (Deep Dive)**: Iterate deep into trade mechanics, option chain selection formulas, and execution filters. Document analysis thoroughly in implementation plans.
- **ASAP (As Soon As Possible)**: Apply targeted logic tweaks directly to strategy parameters or functions.
- **Single Algorithm Focus**: Keep all logic optimization focused on the active strategy (e.g. `4EVC`).
