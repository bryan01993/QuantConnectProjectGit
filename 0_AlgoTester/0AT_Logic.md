# 0AT — Fire-Ring Decorator & Logging Stress Test Algorithm

This document details the architecture, dynamic indicator generation, exit category mapping, and verification flow implemented in **`0_AlgoTester` ([main.py](file:///c:/Users/bryan/QuantConnectProjectGit/0_AlgoTester/main.py))**.

---

## 1. Objectives

The `0AT` algorithm serves as an automated "Fire-Ring" test harness designed to stress-test:
1. **Universal Decorators**: `@log_trade_entry`, `@log_trade_exit`, `@monitor_execution`, and `@measure_memory_usage`.
2. **Dynamic Indicator Serialization**: Generates dynamic technical/statistical metrics (`rsi`, `zscore`, `momentum_pct`, `moving_avg_ratio`, `volatility_ann`, `signal_strength`) and serializes them into the `parameters` JSON column without assuming 4EVC-specific indicators (`vol_ratio`, `slope`, `ivrv_ratio`).
3. **Zero "Other" Exit Classification**: Tests explicit tag strings to ensure that exit reasons are categorized into clean, descriptive BigQuery categories (`Stop Loss`, `Take Profit`, `Time Exit`, `DTE Safety`, `Signal Exit`, `Risk Exit`, `Rebalance`, `Trailing Stop`).
4. **Stacked Decorators**: Verifies that placing both `@monitor_execution` and `@log_trade_exit` on the same method causes zero conflicts or memory leaks.

---

## 2. Dynamic Indicator Generation (`GenerateRandomIndicators`)

Unlike strategy-specific algorithms, `0AT` dynamically constructs a dict of arbitrary quantitative indicators:

```python
{
    "rsi": 45.20,
    "zscore": -1.45,
    "momentum_pct": 0.023,
    "moving_avg_ratio": 1.015,
    "signal_strength": 0.65,
    "volatility_ann": 0.22,
    "random_threshold": 0.50
}
```

These values are serialized as JSON into the `parameters` field of `BTOPTrades` for post-backtest analysis.

---

## 3. Exit Reason Classification Mapping

To keep the `"Other"` tag as close to **0%** as possible, `0AT` liquidates positions under explicit, descriptive tag strings:

| Liquidation Tag in `0AT` | Normalized `exit_reason` |
|---|---|
| `"Stop Loss Triggered (Unrealized loss exceeded threshold)"` | `Stop Loss` |
| `"Take Profit Target Achieved (Profit target reached)"` | `Take Profit` |
| `"Time-Based Exit (Holding period limit reached)"` | `Time Exit` |
| `"DTE Safety Expiry Close"` | `DTE Safety` |
| `"Signal Reversion (Indicator crossed threshold)"` | `Signal Exit` |
| `"Risk Margin Reduction (Portfolio allocation cap)"` | `Risk Exit` |

---

## 4. End-to-End Execution & Ingestion Command Chain

```bash
# 1. Launch 0AT backtest (local or cloud)
poetry run python Scripts/bt_launcher.py 0AT

# 2. Extract [BIGQUERY_TRADE_RECORD] payloads and upload to BigQuery
poetry run python Scripts/log_trades_uploader.py

# 3. Generate interactive Sankey diagram for 0AT
poetry run python Scripts/Visualizations/trade_flow_sankey.py --backtest-id <0AT_RUN_ID>
```
