---
name: quant-statistical-audit
description: Triggers when conducting adversarial quantitative analysis, statistical factor validation, decile monotonicity testing, trade sequence runs tests, expected return OLS scatter plots, or risk audits on QuantConnect algorithms using BigQuery.
---

# Quant Statistical Audit Skill

Use this skill when auditing, stress testing, or verifying QuantConnect algorithm performance against BigQuery statistical validation gates.

## Core Mindset
Operate under **Prejudicial Skepticism**:
- Every backtest result is assumed to be **overfitted, lucky, or curve-fitted by default**.
- High Sharpe ratios or cumulative PnL figures must prove their statistical validity through non-negotiable quantitative gates.

## Automated Execution Command
To run the automated BigQuery statistical audit pipeline:

```bash
# Audit specific algorithm (all backtests in BigQuery)
poetry run python Scripts/BigQuery/quant_statistical_audit.py --algo 4EVC

# Audit specific single backtest ID
poetry run python Scripts/BigQuery/quant_statistical_audit.py --algo 4EVC --backtest-id <BACKTEST_ID>

# Demo run with synthetic data
poetry run python Scripts/BigQuery/quant_statistical_audit.py --demo
```

## Mandatory Statistical Evaluation Gates

1. **Multivariate Factor Correlation**:
   - Evaluate Pearson & Spearman rank correlation between trade PnL and factors (`vol_ratio`, `slope`, `ivrv_ratio`, DTE, Delta, duration).
   - Require \(p < 0.01\) for statistical significance.

2. **Decile Monotonicity Analysis**:
   - Bin factors into 10 quantiles (\(D_1..D_{10}\)).
   - Require Spearman rank correlation \(r_s \ge 0.80\) across decile mean PnLs.

3. **Expected Return OLS Scatter Plots**:
   - Fit OLS linear regression for expected trade returns vs predictor signals.
   - Check for non-zero slope (\(p < 0.05\)) and check heteroscedasticity.

4. **Trade Sequence Independence**:
   - Perform Wald-Wolfowitz Runs Test on timestamp-ordered trade PnL sequences.
   - Require \(Z\)-score in \([-1.96, +1.96]\) to confirm win/loss independence (no streak clustering).

5. **Outlier Trade Sensitivity**:
   - Trim top 2% win outlier trades and verify that cumulative PnL and mean return remain strictly positive.

6. **Deflated Sharpe Ratio (DSR)**:
   - Compute López de Prado DSR to adjust for multiple parameter trial selection bias.
