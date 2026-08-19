"""
decile_factor_analyzer.py
========================
Queries BigQuery table `bav-personal-cloud.develop.BTOPTrades`, groups predictor factors
(slope, ivrv_ratio, vol_ratio) into 10 deciles, and generates decile-versus-profitability
sensitivity line charts matching video analysis specifications.

Usage:
    poetry run python Scripts/BigQuery/decile_factor_analyzer.py [--output-dir OUTPUT_DIR]
"""

from __future__ import annotations

import argparse
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client  # noqa: E402

def fetch_trade_data(algo_code: str = '4EVC', backtest_id: Optional[str] = None) -> pd.DataFrame:
    """Queries BigQuery for trade records with factor metrics on a per-backtest or global basis."""
    client = get_bigquery_client()
    where_clause = f"WHERE algo_code = '{algo_code}'"
    if backtest_id:
        where_clause += f" AND (backtestId = '{backtest_id}' OR pk LIKE '%{backtest_id}%')"

    query = f"""
        SELECT
            pk,
            backtestId,
            timestamp,
            underlying,
            pnl,
            entry_price,
            exit_price,
            COALESCE(slope, SAFE_CAST(JSON_EXTRACT_SCALAR(parameters, '$.slope') AS FLOAT64)) AS slope,
            COALESCE(ivrv_ratio, SAFE_CAST(JSON_EXTRACT_SCALAR(parameters, '$.ivrv_ratio') AS FLOAT64), SAFE_CAST(JSON_EXTRACT_SCALAR(parameters, '$.ivrv') AS FLOAT64)) AS ivrv_ratio,
            COALESCE(vol_ratio, SAFE_CAST(JSON_EXTRACT_SCALAR(parameters, '$.vol_ratio') AS FLOAT64)) AS vol_ratio
        FROM `develop.BTOPTrades`
        {where_clause}
          AND pnl IS NOT NULL
          AND action = 'CLOSE'
    """
    query_job = client.query(query)
    results = query_job.result()
    rows = [dict(row) for row in results]
    df = pd.DataFrame(rows)
    return df

def analyze_factor_deciles(df: pd.DataFrame, factor_name: str, num_deciles: int = 10) -> pd.DataFrame:
    """Splits factor values into deciles and computes mean return and bin ranges."""
    clean_df = df.dropna(subset=[factor_name, 'pnl']).copy()
    if clean_df.empty:
        return pd.DataFrame()

    # Create quantile decile bins
    try:
        clean_df['decile'] = pd.qcut(clean_df[factor_name], q=num_deciles, labels=False, duplicates='drop')
    except Exception:
        clean_df['decile'] = pd.cut(clean_df[factor_name], bins=num_deciles, labels=False)

    summary = []
    for decile_idx, group in clean_df.groupby('decile'):
        min_val = group[factor_name].min()
        max_val = group[factor_name].max()
        mean_pnl = group['pnl'].mean()
        win_rate = (group['pnl'] > 0).mean() * 100.0
        count = len(group)
        bin_label = f"({min_val:.4f}, {max_val:.4f}]"

        summary.append({
            "decile": decile_idx + 1,
            "bin_range": bin_label,
            "min_val": min_val,
            "max_val": max_val,
            "mean_pnl": mean_pnl,
            "win_rate": win_rate,
            "count": count
        })

    return pd.DataFrame(summary)

def plot_decile_chart(summary_df: pd.DataFrame, factor_name: str, output_path: str) -> None:
    """Plots decile line chart matching the video design (mean return vs decile range)."""
    if summary_df.empty:
        print(f"No data to plot for factor {factor_name}")
        return

    plt.figure(figsize=(12, 6))
    plt.plot(summary_df['bin_range'], summary_df['mean_pnl'], marker='o', linewidth=2, color='#1f77b4', label=f'Mean Return ({factor_name})')
    plt.axhline(0, color='red', linestyle='--', linewidth=1.5, label='Zero PnL Benchmark')

    plt.title(f"Mean Calendar Return Jump by {factor_name} Decile", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel(f"{factor_name} Decile Range", fontsize=12, fontweight='bold')
    plt.ylabel("Mean Realized Return (PnL)", fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper right')
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[OK] Saved decile factor chart to {output_path}")

def generate_demo_data(num_samples: int = 500) -> pd.DataFrame:
    """Generates realistic synthetic factor dataset for instant terminal visualization."""
    np.random.seed(42)
    slopes = np.random.uniform(-0.015, 0.035, num_samples)
    # Factor relationship: higher slope correlates with higher PnL
    pnl = 2.5 * slopes + np.random.normal(0, 0.02, num_samples) - 0.01
    ivrv = np.random.uniform(0.8, 3.5, num_samples)
    vol = np.random.uniform(0.5, 4.0, num_samples)

    return pd.DataFrame({
        "pk": [f"DEMO_{i}" for i in range(num_samples)],
        "slope": slopes,
        "ivrv_ratio": ivrv,
        "vol_ratio": vol,
        "pnl": pnl
    })

def main():
    parser = argparse.ArgumentParser(description="BigQuery Decile Factor Sensitivity Analyzer")
    parser.add_argument("--output-dir", type=str, default=".", help="Directory to save generated chart PNGs")
    parser.add_argument("--backtest-id", type=str, default=None, help="Filter trade records for a single specific backtest run ID")
    parser.add_argument("--demo", action="store_true", help="Run with demo sample data for instant chart preview")
    args = parser.parse_args()

    if args.demo:
        print("Running in DEMO mode with sample factor dataset...")
        df = generate_demo_data(500)
    else:
        bt_msg = f"for backtest ID: {args.backtest_id}" if args.backtest_id else "(all backtests)"
        print(f"Fetching closed trade records from BigQuery {bt_msg}...")
        df = fetch_trade_data(backtest_id=args.backtest_id)
        print(f"Retrieved {len(df)} closed trade records.")

    if df.empty:
        print("No trade records found in BigQuery. Use --demo to view a sample chart preview.")
        return

    factors = ['slope', 'ivrv_ratio', 'vol_ratio']
    for factor in factors:
        summary_df = analyze_factor_deciles(df, factor, num_deciles=10)
        if not summary_df.empty:
            print(f"\n=== Decile Sensitivity Summary for: {factor} ===")
            print(summary_df.to_string(index=False))

            suffix = "_demo" if args.demo else ""
            chart_path = os.path.join(args.output_dir, f"decile_sensitivity_{factor}{suffix}.png")
            plot_decile_chart(summary_df, factor, chart_path)

if __name__ == "__main__":
    main()
