"""
quant_statistical_audit.py
===========================
Automated Adversarial Quantitative Audit & Statistical Verification Pipeline.
Sourced exclusively from BigQuery dataset `bav-personal-cloud.develop`.

Performs non-negotiable statistical audit gates:
1. Multivariate Factor Correlation Matrix (Pearson & Spearman rank + p-values)
2. Factor Decile Sensitivity & Monotonicity Analysis (10 Deciles, D1..D10)
3. Expected Return Scatter Plots & OLS Linear Regression Fit
4. Trade Sequence Independence (Wald-Wolfowitz Runs Test)
5. Outlier Trade Sensitivity Analysis (Top 2% profit trim)
6. Deflated Sharpe Ratio (DSR) Estimation

Usage:
    poetry run python Scripts/BigQuery/quant_statistical_audit.py [--algo ALGO] [--backtest-id ID] [--output-dir DIR] [--demo]
"""

from __future__ import annotations

import argparse
import os
import sys
import math
from typing import Dict, List, Tuple, Optional, Any

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client  # noqa: E402


def fetch_quant_audit_data(
    algo_code: str = "4EVC",
    backtest_id: Optional[Union[str, List[str]]] = None,
    backtest_name: Optional[Union[str, List[str]]] = None
) -> pd.DataFrame:
    """
    Queries BigQuery BTOPTrades and child entities for trade factors and return percentages.
    Supports single or list of backtest IDs (backtest_id) and/or backtest names (backtest_name).
    Automatically concatenates multi-backtest trade results into a unified DataFrame.
    """
    client = get_bigquery_client()
    target_ids: List[str] = []

    # 1. Process backtest_id input (single str or list of strs)
    if backtest_id:
        if isinstance(backtest_id, str):
            target_ids.append(backtest_id)
        elif isinstance(backtest_id, (list, tuple, set)):
            target_ids.extend([str(bid) for bid in backtest_id if bid])

    # 2. Process backtest_name input (resolve names to backtestId via BTOPResults)
    if backtest_name:
        name_list = [backtest_name] if isinstance(backtest_name, str) else list(backtest_name)
        clean_names = [str(n).strip() for n in name_list if n and str(n).strip()]
        if clean_names:
            name_conds = []
            for n in clean_names:
                if "%" in n or "*" in n:
                    pattern = n.replace("*", "%")
                    name_conds.append(f"name LIKE '{pattern}'")
                else:
                    name_conds.append(f"name = '{n}'")

            name_query = f"""
                SELECT DISTINCT backtestId, name
                FROM `develop.BTOPResults`
                WHERE {' OR '.join(name_conds)}
            """
            try:
                name_job = client.query(name_query)
                name_rows = [dict(r) for r in name_job.result()]
                for r in name_rows:
                    bid = r.get("backtestId")
                    bname = r.get("name")
                    if bid:
                        target_ids.append(bid)
                        print(f"[RESOLVED] Backtest Name '{bname}' -> ID '{bid}'")
            except Exception as err:
                print(f"[WARN] Failed to resolve backtest_name against BTOPResults: {err}")

    # Deduplicate IDs while preserving order
    unique_ids = list(dict.fromkeys(target_ids))

    where_conditions = []
    if unique_ids:
        id_clauses = [f"backtestId = '{bid}'" for bid in unique_ids]
        where_conditions.append(f"({' OR '.join(id_clauses)})")

    where_clause = ("WHERE " + " AND ".join(where_conditions)) if where_conditions else ""

    query = f"""
        SELECT
            combo_trade_id AS pk,
            backtestId,
            backtest_name,
            entry_time AS timestamp,
            exit_time,
            underlying,
            holding_hours,
            contracts_qty AS qty,
            short_leg_symbol,
            long_leg_symbol,
            short_leg_entry_price,
            long_leg_entry_price,
            net_debit_paid_per_unit,
            total_net_debit_paid,
            short_leg_exit_price,
            long_leg_exit_price,
            net_credit_received_at_exit,
            short_leg_pnl,
            long_leg_pnl,
            total_combo_pnl_dollars AS pnl,
            total_combo_fees,
            combo_return_pct AS return_pct,
            is_combo_win,
            strike,
            short_leg_expiry,
            long_leg_expiry,
            slope,
            ivrv_ratio,
            vol_ratio,
            earnings_date,
            raw_parameters_json
        FROM `develop.v_4EVC_consolidated_spread_trades`
        {where_clause}
        ORDER BY entry_time ASC
    """

    query_job = client.query(query)
    results = query_job.result()
    rows = [dict(row) for row in results]

    expected_cols = [
        "pk", "backtestId", "timestamp", "underlying", "pnl",
        "entry_price", "exit_price", "return_pct", "exit_reason",
        "slope", "ivrv_ratio", "vol_ratio"
    ]

    if not rows:
        return pd.DataFrame(columns=expected_cols)

    df = pd.DataFrame(rows)

    for col in expected_cols:
        if col not in df.columns:
            df[col] = np.nan

    # combo_return_pct from v_4EVC_consolidated_spread_trades measures net-debit spread return %
    df['return_pct'] = pd.to_numeric(df['return_pct'], errors='coerce')

    # Also compute capital_return_pct (return relative to $1,000 trade capital) for scale consistency
    df['capital_return_pct'] = pd.Series(np.where(df['pnl'].notnull(), (df['pnl'] / 1000.0) * 100.0, 0.0), index=df.index).fillna(df['pnl'])

    return df


def generate_synthetic_audit_data(num_trades: int = 600) -> pd.DataFrame:
    """Generates realistic synthetic multi-factor trade dataset for demonstration/testing (in return %)."""
    np.random.seed(42)
    slopes = np.random.uniform(-0.015, 0.035, num_trades)
    ivrv = np.random.uniform(0.8, 3.5, num_trades)
    vol = np.random.uniform(0.5, 4.0, num_trades)

    # Percentage return driven by slope and vol_ratio with noise
    return_pct = (3.2 * slopes + 0.005 * vol + np.random.normal(0, 0.025, num_trades) - 0.008) * 100.0

    # Inject a few outliers
    return_pct[::150] = return_pct[::150] * 3.5

    dates = pd.date_range("2023-01-01", periods=num_trades, freq="H")

    return pd.DataFrame({
        "pk": [f"SYNTH_{i:04d}" for i in range(num_trades)],
        "backtestId": ["DEMO_BACKTEST_001"] * num_trades,
        "timestamp": dates,
        "underlying": np.random.choice(["AAPL", "AMD", "NVDA", "MSFT"], size=num_trades),
        "pnl": return_pct * 10.0,
        "return_pct": return_pct,
        "slope": slopes,
        "ivrv_ratio": ivrv,
        "vol_ratio": vol,
        "exit_reason": "TAKE_PROFIT"
    })


def analyze_return_distribution(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Computes trade return summary statistics (describe, skew, kurtosis) and layman_term explanations."""
    target_col = 'return_pct' if 'return_pct' in df.columns else ('pnl' if 'pnl' in df.columns else df.columns[0])
    clean_series = df[target_col].dropna()

    if clean_series.empty:
        return pd.DataFrame(), {}

    desc = clean_series.describe()
    skew_val = float(clean_series.skew())
    kurt_val = float(clean_series.kurtosis())

    stats_rows = [
        {"statistic": "count", "value": desc["count"], "layman_term": f"Total Sample Size: Analyzed {int(desc['count'])} consolidated 2-leg spread trade executions across the selected backtest run(s)."},
        {"statistic": "mean", "value": desc["mean"], "layman_term": f"Arithmetic Mean Return: The expected trade profit/loss is {desc['mean']:.4f}% per position relative to total net debit capital risked."},
        {"statistic": "std", "value": desc["std"], "layman_term": f"Return Dispersion (Volatility): Standard deviation of trade returns is {desc['std']:.4f}%, reflecting outcome variability across market regimes."},
        {"statistic": "min", "value": desc["min"], "layman_term": f"Maximum Single-Trade Loss: Worst historical trade outcome reached {desc['min']:.4f}% loss on net debit invested (including spread slippage and transaction fees)."},
        {"statistic": "25%", "value": desc["25%"], "layman_term": f"First Quartile (Q1): 25% of all executed trades suffered a loss worse than {desc['25%']:.4f}% return on debit."},
        {"statistic": "50% (median)", "value": desc["50%"], "layman_term": f"Median Trade Return: 50th percentile trade result sits at {desc['50%']:.4f}%, providing a robust central return measure resistant to extreme outliers."},
        {"statistic": "75%", "value": desc["75%"], "layman_term": f"Third Quartile (Q3): 75% of all executed trades achieved returns below {desc['75%']:.4f}% on net debit invested."},
        {"statistic": "max", "value": desc["max"], "layman_term": f"Maximum Single-Trade Gain: Best historical trade outcome generated a +{desc['max']:.4f}% profit on initial net debit invested."},
        {"statistic": "skewness", "value": skew_val, "layman_term": f"Asymmetry of Return Distribution (Skewness = {skew_val:.4f}): {'Positive right-skewed tail where winner payouts exceed average losses.' if skew_val > 0 else 'Negative left-skewed tail indicating asymmetric downside tail risk where rare large losses drag down performance.'}"},
        {"statistic": "kurtosis", "value": kurt_val, "layman_term": f"Tail Risk Heavy-Tailedness (Excess Kurtosis = {kurt_val:.4f}): {'Fat-tailed distribution exhibiting heightened jump risk and frequent extreme outlier returns.' if kurt_val > 3 else 'Platykurtic / Gaussian-like return distribution with well-behaved tail risk dispersion.'}"}
    ]

    stats_df = pd.DataFrame(stats_rows)
    metrics_dict = {row["statistic"]: row["value"] for row in stats_rows}
    return stats_df, metrics_dict


def analyze_multivariate_correlations(df: pd.DataFrame, factors: List[str]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Computes Pearson & Spearman correlation matrices, p-values, and layman_term translations against return_pct."""
    pearson_rows = []
    spearman_rows = []
    for factor in factors:
        if factor not in df.columns:
            clean_data = pd.DataFrame()
        else:
            clean_data = df.dropna(subset=[factor, 'return_pct'])

        if len(clean_data) < 5:
            pearson_rows.append({
                "factor": factor,
                "pearson_r": np.nan,
                "p_value": np.nan,
                "statistically_significant": False,
                "layman_term": f"No Factor Data Available: Predictor column '{factor}' contains insufficient or entirely NULL records across the selected backtest dataset."
            })
            spearman_rows.append({
                "factor": factor,
                "spearman_r": np.nan,
                "p_value": np.nan,
                "statistically_significant": False,
                "layman_term": f"No Factor Data Available: Predictor column '{factor}' contains insufficient or entirely NULL records across the selected backtest dataset."
            })
            continue

        r_p, p_p = stats.pearsonr(clean_data[factor], clean_data['return_pct'])
        r_s, p_s = stats.spearmanr(clean_data[factor], clean_data['return_pct'])

        sig_p = p_p < 0.01
        sig_s = p_s < 0.01

        if sig_p:
            layman_p = f"Statistically Significant Linear Factor (Pearson r = {r_p:.4f}, p = {p_p:.2e} < 0.01): Empirical proof that '{factor}' has a direct {'positive' if r_p > 0 else 'negative'} linear correlation with trade percentage return."
        else:
            layman_p = f"Statistically Insignificant Linear Factor (Pearson r = {r_p:.4f}, p = {p_p:.4f} >= 0.01): Unproven linear relationship; variation in '{factor}' acts as random market noise relative to percentage return."

        if sig_s:
            layman_s = f"Statistically Significant Rank Factor (Spearman rs = {r_s:.4f}, p = {p_s:.2e} < 0.01): Strong monotonic rank edge proving higher '{factor}' values systematically predict {'higher' if r_s > 0 else 'lower'} percentage returns."
        else:
            layman_s = f"Statistically Insignificant Rank Factor (Spearman rs = {r_s:.4f}, p = {p_s:.4f} >= 0.01): Monotonic rank ordering fails significance threshold; factor values do not consistently rank-order trade returns."

        pearson_rows.append({
            "factor": factor,
            "pearson_r": r_p,
            "p_value": p_p,
            "statistically_significant": sig_p,
            "layman_term": layman_p
        })
        spearman_rows.append({
            "factor": factor,
            "spearman_r": r_s,
            "p_value": p_s,
            "statistically_significant": sig_s,
            "layman_term": layman_s
        })

    p_cols = ["factor", "pearson_r", "p_value", "statistically_significant", "layman_term"]
    s_cols = ["factor", "spearman_r", "p_value", "statistically_significant", "layman_term"]
    p_df = pd.DataFrame(pearson_rows, columns=p_cols) if pearson_rows else pd.DataFrame(columns=p_cols)
    s_df = pd.DataFrame(spearman_rows, columns=s_cols) if spearman_rows else pd.DataFrame(columns=s_cols)
    return p_df, s_df


def analyze_decile_monotonicity(df: pd.DataFrame, factor_name: str, num_deciles: int = 10) -> Tuple[pd.DataFrame, float, bool]:
    """Partitions factor values into 10 deciles and evaluates monotonic trend of return_pct via Spearman rank correlation."""
    target_col = 'return_pct' if 'return_pct' in df.columns else ('pnl' if 'pnl' in df.columns else df.columns[0])
    clean_df = df.dropna(subset=[factor_name, target_col]).copy()
    if len(clean_df) < num_deciles * 2:
        return pd.DataFrame(), 0.0, False

    try:
        clean_df['decile'] = pd.qcut(clean_df[factor_name], q=num_deciles, labels=False, duplicates='drop')
    except Exception:
        clean_df['decile'] = pd.cut(clean_df[factor_name], bins=num_deciles, labels=False)

    summary = []
    for decile_idx, group in clean_df.groupby('decile'):
        min_val = group[factor_name].min()
        max_val = group[factor_name].max()
        mean_val = group[target_col].mean()
        win_rate = (group[target_col] > 0).mean() * 100.0
        count = len(group)

        summary.append({
            "decile": decile_idx + 1,
            "bin_range": f"({min_val:.4f}, {max_val:.4f}]",
            "min_val": min_val,
            "max_val": max_val,
            "mean_return_pct": mean_val,
            "mean_pnl": mean_val,  # Alias to prevent KeyError
            "win_rate": win_rate,
            "count": count
        })

    decile_df = pd.DataFrame(summary)

    # Compute monotonicity: Spearman correlation between decile rank (1..10) and mean_return_pct
    rs, p_val = stats.spearmanr(decile_df['decile'], decile_df['mean_return_pct'])
    is_monotonic = rs >= 0.80 and p_val < 0.05

    return decile_df, rs, is_monotonic


def fit_expected_return_ols(df: pd.DataFrame, factor_name: str) -> Dict[str, Any]:
    """Fits OLS linear regression of trade percentage return (return_pct) against a predictor variable."""
    target_col = 'return_pct' if 'return_pct' in df.columns else ('pnl' if 'pnl' in df.columns else df.columns[0])
    clean_data = df.dropna(subset=[factor_name, target_col])
    x = clean_data[factor_name].values
    y = clean_data[target_col].values

    if len(x) < 10:
        return {}

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    # Residuals & Heteroscedasticity check (correlation between |residuals| and x)
    residuals = y - (slope * x + intercept)
    abs_res = np.abs(residuals)
    het_r, het_p = stats.spearmanr(x, abs_res)
    is_het = het_p < 0.05

    if p_value < 0.05:
        if is_het:
            layman = f"Statistically Significant Predictive Slope with Heteroscedastic Variance (Slope = {slope:.4f} %/unit, R^2 = {r_value**2:.4f}, p = {p_value:.2e}): The factor '{factor_name}' linearly predicts trade returns, but error variance expands across factor magnitudes (unstable risk profile)."
        else:
            layman = f"Statistically Significant Stable Regression Fit (Slope = {slope:.4f} %/unit, R^2 = {r_value**2:.4f}, p = {p_value:.2e}): Robust linear model proving each 1-unit change in '{factor_name}' reliably shifts trade percentage return by {slope:.4f}%."
    else:
        layman = f"No Predictive Linear Power (Slope = {slope:.4f} %/unit, R^2 = {r_value**2:.4f}, p = {p_value:.4f} >= 0.05): Regression slope for '{factor_name}' is not statistically distinguishable from zero; factor cannot forecast expected trade return."

    return {
        "factor": factor_name,
        "slope": slope,
        "intercept": intercept,
        "r_squared": r_value ** 2,
        "p_value": p_value,
        "std_err": std_err,
        "het_p_value": het_p,
        "is_heteroscedastic": is_het,
        "layman_term": layman
    }


def perform_runs_test(df: pd.DataFrame) -> Dict[str, Any]:
    """Executes Wald-Wolfowitz Runs Test for sequential trade win/loss independence."""
    target_col = 'return_pct' if 'return_pct' in df.columns else ('pnl' if 'pnl' in df.columns else df.columns[0])
    clean_df = df.dropna(subset=[target_col]).copy()
    wins = (clean_df[target_col] > 0).astype(int).values

    n = len(wins)
    if n < 10:
        return {"z_score": 0.0, "p_value": 1.0, "is_independent": False, "layman_term": "Insufficient Trade Sample Size: At least 10 executed trade records are required to perform the Wald-Wolfowitz sequence independence test."}

    n1 = np.sum(wins == 1)
    n2 = np.sum(wins == 0)

    if n1 == 0 or n2 == 0:
        return {"z_score": 0.0, "p_value": 0.0, "is_independent": False, "layman_term": "Zero Sequence Variance: Trade dataset consists exclusively of 100% winning or 100% losing trades; cannot evaluate sequence independence."}

    # Count runs (transitions)
    runs = 1 + np.sum(wins[1:] != wins[:-1])

    expected_runs = 1 + (2 * n1 * n2) / n
    variance = (2 * n1 * n2 * (2 * n1 * n2 - n)) / (n ** 2 * (n - 1))

    if variance <= 0:
        return {"z_score": 0.0, "p_value": 1.0, "is_independent": False, "layman_term": "Degenerate Variance: Sequence variance calculation resulted in zero or negative value."}

    z_score = (runs - expected_runs) / math.sqrt(variance)
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

    is_independent = -1.96 <= z_score <= 1.96

    if is_independent:
        layman = f"Independent Trade Sequence (Z-Score = {z_score:.4f}, p = {p_value:.4f}): Trade win/loss outcomes occur randomly and independently over time, passing the Wald-Wolfowitz test with no loss clustering or regime dependency."
    elif z_score < -1.96:
        layman = f"Severe Streak Risk & Loss Clustering (Z-Score = {z_score:.4f} < -1.96, p = {p_value:.4f}): Trade wins and losses form prolonged consecutive loss streaks, indicating heavy market regime dependency and drawdown vulnerability."
    else:
        layman = f"Abnormal Win/Loss Oscillation (Z-Score = {z_score:.4f} > 1.96, p = {p_value:.4f}): Consecutive trade outcomes alternate back and forth far more frequently than expected by random chance."

    return {
        "total_trades": n,
        "wins": int(n1),
        "losses": int(n2),
        "actual_runs": int(runs),
        "expected_runs": float(expected_runs),
        "z_score": float(z_score),
        "p_value": float(p_value),
        "is_independent": is_independent,
        "layman_term": layman
    }


def analyze_outlier_sensitivity(df: pd.DataFrame, trim_pct: float = 0.02) -> Dict[str, Any]:
    """Tests if strategy profitability collapses after removing top N% win trades (evaluated in return %)."""
    target_col = 'return_pct' if 'return_pct' in df.columns else ('pnl' if 'pnl' in df.columns else df.columns[0])
    clean_df = df.dropna(subset=[target_col]).copy()
    if len(clean_df) < 20:
        return {
            "passes_gate": False,
            "orig_mean_return_pct": 0.0,
            "orig_mean_pnl": 0.0,
            "trimmed_mean_return_pct": 0.0,
            "trimmed_mean_pnl": 0.0,
            "orig_total_pnl": 0.0,
            "trimmed_total_pnl": 0.0,
            "layman_term": "Insufficient Trade Sample Size: Requires at least 20 trades to perform 2% top-trade outlier sensitivity trimming."
        }

    orig_mean = clean_df[target_col].mean()
    orig_sum = clean_df[target_col].sum()

    # Trim top 2% return trades
    cutoff = clean_df[target_col].quantile(1.0 - trim_pct)
    trimmed_df = clean_df[clean_df[target_col] < cutoff]

    trimmed_mean = trimmed_df[target_col].mean()
    trimmed_sum = trimmed_df[target_col].sum()

    passes = trimmed_mean > 0

    if passes:
        layman = f"Robust Structural Edge (Passes 2% Trim Gate): Original mean return of {orig_mean:.2f}% remains positive at {trimmed_mean:.2f}% after completely removing the top 2% best winning outlier trades."
    else:
        layman = f"Fragile Overfitted Edge (Fails 2% Trim Gate): Strategy profitability relies entirely on rare lucky wins; removing the top 2% outlier win trades causes mean return to collapse from {orig_mean:.2f}% down to {trimmed_mean:.2f}%."

    return {
        "trim_pct": trim_pct * 100.0,
        "orig_mean_return_pct": orig_mean,
        "orig_mean_pnl": orig_mean,
        "orig_total_pnl": orig_sum,
        "trimmed_mean_return_pct": trimmed_mean,
        "trimmed_mean_pnl": trimmed_mean,
        "trimmed_total_pnl": trimmed_sum,
        "passes_gate": passes,
        "layman_term": layman
    }


def compute_deflated_sharpe_ratio(sharpe: float, n_trials: int = 10, n_samples: int = 252) -> float:
    """Computes López de Prado's Deflated Sharpe Ratio (DSR) for multiple parameter trials."""
    if n_trials <= 1:
        return 1.0 if sharpe > 0 else 0.0

    # Euler-Mascheroni constant estimate for max Sharpe under null hypothesis
    gamma = 0.5772156649
    e_max_z = (1 - gamma) * stats.norm.ppf(1 - 1.0 / n_trials) + gamma * stats.norm.ppf(1 - 1.0 / (n_trials * math.e))
    sr_std = math.sqrt((1 + 0.5 * sharpe ** 2) / (n_samples - 1))

    dsr_stat = (sharpe - e_max_z) / sr_std
    return float(stats.norm.cdf(dsr_stat))


def generate_quant_audit_charts(df: pd.DataFrame, factors: List[str], output_dir: str, prefix: str = "") -> None:
    """Generates visual audit diagnostic charts (Scatter OLS fit & Decile Monotonicity in %)."""
    os.makedirs(output_dir, exist_ok=True)
    plt.style.use('ggplot')

    for factor in factors:
        clean_df = df.dropna(subset=[factor, 'return_pct'])
        if len(clean_df) < 10:
            continue

        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # 1. Scatter Plot & OLS Fit (Pure Matplotlib)
        x_vals = clean_df[factor].values
        y_vals = clean_df['return_pct'].values
        axes[0].scatter(x_vals, y_vals, alpha=0.5, color='#1f77b4', s=25, label='Trade Executions')

        slope, intercept, r_val, p_val, std_err = stats.linregress(x_vals, y_vals)
        x_line = np.linspace(x_vals.min(), x_vals.max(), 100)
        y_line = slope * x_line + intercept
        axes[0].plot(x_line, y_line, color='red', linewidth=2, label=f'OLS Fit ($R^2={r_val**2:.3f}$)')

        axes[0].set_title(f"Expected Return OLS Scatter: {factor} vs Realized Return (%)", fontsize=12, fontweight="bold")
        axes[0].set_xlabel(factor, fontsize=10, fontweight="bold")
        axes[0].set_ylabel("Realized Return (%)", fontsize=10, fontweight="bold")
        axes[0].axhline(0, color="gray", linestyle="--", alpha=0.7)
        axes[0].legend(loc='upper right')

        # 2. Decile Monotonicity Bar Chart
        decile_df, rs, is_mono = analyze_decile_monotonicity(clean_df, factor, num_deciles=10)
        if not decile_df.empty:
            colors = ["#d62728" if p < 0 else "#2ca02c" for p in decile_df['mean_return_pct']]
            axes[1].bar(decile_df['decile'].astype(str), decile_df['mean_return_pct'], color=colors, alpha=0.85, edgecolor="black")
            axes[1].axhline(0, color="gray", linestyle="--")
            axes[1].set_title(f"Decile Monotonicity ({factor}): Spearman $r_s={rs:.3f}$", fontsize=12, fontweight="bold")
            axes[1].set_xlabel("Decile (D1 = Lowest, D10 = Highest)", fontsize=10, fontweight="bold")
            axes[1].set_ylabel("Mean Realized Return (%)", fontsize=10, fontweight="bold")

        plt.tight_layout()
        plot_path = os.path.join(output_dir, f"{prefix}quant_audit_{factor}.png")
        plt.savefig(plot_path, dpi=300)
        plt.close()
        print(f"[OK] Saved statistical audit chart: {plot_path}")


def run_quant_audit(
    algo_code: str = "4EVC",
    backtest_id: Optional[Union[str, List[str]]] = None,
    backtest_name: Optional[Union[str, List[str]]] = None,
    output_dir: str = ".",
    demo: bool = False
) -> Dict[str, Any]:
    """Executes full adversarial quantitative audit suite on single or concatenated backtest runs."""
    print("=========================================================")
    print("  QUANT VERIFICATION & RISK AUDITOR AGENT - AUDIT RUNNER")
    print("=========================================================")
    print("Axiom: Presumed Overfitted / Zero Edge until proven innocent.")

    if demo:
        print("[DEMO MODE] Loading synthetic multi-factor trade dataset...")
        df = generate_synthetic_audit_data(600)
    else:
        target_descr = []
        if backtest_id:
            target_descr.append(f"backtest_id={backtest_id}")
        if backtest_name:
            target_descr.append(f"backtest_name={backtest_name}")
        target_str = ", ".join(target_descr) if target_descr else f"algo: {algo_code}"

        print(f"[BIGQUERY MODE] Fetching trade dataset from BigQuery for {target_str}...")
        df = fetch_quant_audit_data(algo_code=algo_code, backtest_id=backtest_id, backtest_name=backtest_name)

    if df.empty:
        print("[ERROR] No trade records found for audit execution. Exiting.")
        return {"status": "NO_DATA"}

    print(f"[DATA INTEGRITY] Audit sample size: {len(df)} trade executions concatenated.")

    # 0. Trade Profitability & Return Distribution Analysis
    print("\n--- 0. TRADE PROFITABILITY DISTRIBUTION ANALYSIS ---")
    dist_df, dist_dict = analyze_return_distribution(df)
    print(dist_df.to_string(index=False))

    factors = ["slope", "ivrv_ratio", "vol_ratio"]
    audit_results: Dict[str, Any] = {
        "total_trades": len(df),
        "backtest_id": backtest_id or "BATCH_AGGREGATE",
        "algo_code": algo_code,
        "return_distribution": dist_dict,
        "gates": {}
    }

    # 1. Multivariate Correlation Analysis
    print("\n--- 1. MULTIVARIATE FACTOR CORRELATION AUDIT ---")
    p_df, s_df = analyze_multivariate_correlations(df, factors)
    print("Pearson Correlations:")
    print(p_df.to_string(index=False))
    print("\nSpearman Rank Correlations:")
    print(s_df.to_string(index=False))

    corr_pass = any(s_df["statistically_significant"])
    audit_results["gates"]["factor_correlation"] = {
        "pass": corr_pass,
        "spearman_table": s_df.to_dict(orient="records")
    }

    # 2. Decile Monotonicity Analysis
    print("\n--- 2. DECILE FACTOR MONOTONICITY AUDIT ---")
    decile_results = {}
    mono_passes = []
    for factor in factors:
        d_df, rs, is_mono = analyze_decile_monotonicity(df, factor, 10)
        mono_passes.append(is_mono)
        decile_results[factor] = {"spearman_rs": rs, "is_monotonic": is_mono}
        print(f"Factor: {factor:<12} | Decile Spearman rs: {rs:.4f} | Monotonic Pass: {is_mono}")

    audit_results["gates"]["decile_monotonicity"] = {
        "pass": any(mono_passes),
        "details": decile_results
    }

    # 3. Expected Return OLS Regression
    print("\n--- 3. EXPECTED RETURN OLS REGRESSION AUDIT ---")
    ols_results = {}
    for factor in factors:
        res = fit_expected_return_ols(df, factor)
        ols_results[factor] = res
        if res:
            print(f"Factor: {factor:<12} | Slope: {res['slope']:.4f} | R^2: {res['r_squared']:.4f} | p-val: {res['p_value']:.4e} | Het p-val: {res['het_p_value']:.4f}")

    audit_results["gates"]["ols_regression"] = ols_results

    # 4. Sequence Independence (Runs Test)
    print("\n--- 4. TRADE SEQUENCE INDEPENDENCE (RUNS TEST) ---")
    runs_res = perform_runs_test(df)
    print(f"Total Trades: {runs_res['total_trades']} | Wins: {runs_res['wins']} | Losses: {runs_res['losses']}")
    print(f"Actual Runs: {runs_res['actual_runs']} | Expected Runs: {runs_res['expected_runs']:.2f}")
    print(f"Z-Score: {runs_res['z_score']:.4f} | p-value: {runs_res['p_value']:.4f} | Independent Pass: {runs_res['is_independent']}")

    audit_results["gates"]["sequence_independence"] = runs_res

    # 5. Outlier Trade Sensitivity
    print("\n--- 5. OUTLIER TRADE SENSITIVITY AUDIT (TOP 2% TRIM) ---")
    outlier_res = analyze_outlier_sensitivity(df, 0.02)
    print(f"Original Mean Return : {outlier_res['orig_mean_return_pct']:.2f}%")
    print(f"Trimmed Mean Return  : {outlier_res['trimmed_mean_return_pct']:.2f}%")
    print(f"Outlier Resilience Pass: {outlier_res['passes_gate']}")

    audit_results["gates"]["outlier_sensitivity"] = outlier_res

    # Overall Audit Scorecard
    print("\n=========================================================")
    print("                QUANT AUDIT SCORECARD SUMMARY")
    print("=========================================================")
    g = audit_results["gates"]
    pass_count = sum([
        1 if g["factor_correlation"]["pass"] else 0,
        1 if g["decile_monotonicity"]["pass"] else 0,
        1 if g["sequence_independence"]["is_independent"] else 0,
        1 if g["outlier_sensitivity"]["passes_gate"] else 0
    ])

    print(f"Factor Correlation Gate   : {'[PASS]' if g['factor_correlation']['pass'] else '[FAIL]'}")
    print(f"Decile Monotonicity Gate  : {'[PASS]' if g['decile_monotonicity']['pass'] else '[FAIL]'}")
    print(f"Sequence Independence Gate: {'[PASS]' if g['sequence_independence']['is_independent'] else '[FAIL]'}")
    print(f"Outlier Resilience Gate  : {'[PASS]' if g['outlier_sensitivity']['passes_gate'] else '[FAIL]'}")
    print(f"\nFinal Audit Rating: {pass_count}/4 Gates Passed")
    print("=========================================================")

    # Render Charts
    prefix = "demo_" if demo else ""
    generate_quant_audit_charts(df, factors, output_dir, prefix=prefix)

    return audit_results


def main():
    parser = argparse.ArgumentParser(description="Quant Verification & Risk Auditor Agent BigQuery Statistical Audit Runner")
    parser.add_argument("--algo", type=str, default="4EVC", help="Strategy short code (e.g. 4EVC)")
    parser.add_argument("--backtest-id", type=str, default=None, help="Specific QuantConnect backtest run ID")
    parser.add_argument("--output-dir", type=str, default=".", help="Output directory for generated statistical audit charts")
    parser.add_argument("--demo", action="store_true", help="Run statistical audit suite using synthetic test data")

    args = parser.parse_args()
    run_quant_audit(algo_code=args.algo, backtest_id=args.backtest_id, output_dir=args.output_dir, demo=args.demo)


if __name__ == "__main__":
    main()
