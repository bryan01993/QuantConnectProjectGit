"""
analyze_mae_mfe_correlation.py
================================
Calculates Pearson & Spearman rank correlations between MAE (Maximum Adverse Excursion %),
MFE (Maximum Favorable Excursion %), holding_hours, and realized return % (combo_return_pct)
on consolidated 4EVC calendar spread trades stored in BigQuery.

Usage:
    poetry run python Scripts/BigQuery/analyze_mae_mfe_correlation.py [--backtest-id <id>]
"""

import sys
import os
import argparse
import pandas as pd
import numpy as np
from scipy import stats

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
for d in [_PROJECT_ROOT, _THIS_DIR]:
    if d not in sys.path:
        sys.path.insert(0, d)

import db_operator

def run_mae_mfe_analysis(backtest_id: str = None):
    client = db_operator.get_bigquery_client()
    
    where_clause = f"WHERE backtestId = '{backtest_id}'" if backtest_id else "WHERE combo_return_pct IS NOT NULL"
    
    query = f"""
    SELECT 
        combo_trade_id,
        backtestId,
        underlying,
        entry_time,
        exit_time,
        holding_hours,
        combo_return_pct,
        is_combo_win,
        mae_pct,
        mfe_pct,
        vol_ratio,
        slope,
        ivrv_ratio
    FROM `bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades`
    {where_clause}
    ORDER BY entry_time ASC
    """
    
    query_job = client.query(query)
    rows = list(query_job.result())
    if not rows:
        print("No trade records found matching criteria.")
        return
    df = pd.DataFrame([dict(r) for r in rows])

    print(f"============================================================")
    print(f"QUANTITATIVE MAE / MFE & DURATION CORRELATION ANALYSIS")
    print(f"Filter Backtest ID: {backtest_id if backtest_id else 'ALL BACKTESTS'}")
    print(f"Total Consolidated Trades Analyzed: {len(df)}")
    print(f"============================================================")
    
    # 1. Summary Statistics
    print("\n--- Summary Statistics ---")
    summary_cols = ['combo_return_pct', 'holding_hours', 'mae_pct', 'mfe_pct']
    valid_cols = [c for c in summary_cols if c in df.columns and df[c].notnull().sum() > 0]
    print(df[valid_cols].describe().round(2).T[['count', 'mean', 'std', 'min', '50%', 'max']])
    
    # 2. Pearson & Spearman Correlation Matrices
    print("\n--- Pearson Correlation Matrix (Linear Relationships) ---")
    num_df = df[valid_cols].dropna()
    if len(num_df) > 5:
        pearson_corr = num_df.corr(method='pearson').round(4)
        print(pearson_corr)

        print("\n--- Spearman Rank Correlation Matrix (Monotonic Relationships) ---")
        spearman_corr = num_df.corr(method='spearman').round(4)
        print(spearman_corr)

        # Statistical significance of correlations with combo_return_pct
        print("\n--- Statistical Significance (p-values) vs. Realized Return % ---")
        for col in ['holding_hours', 'mae_pct', 'mfe_pct']:
            if col in num_df.columns:
                p_r, p_p = stats.pearsonr(num_df[col], num_df['combo_return_pct'])
                s_r, s_p = stats.spearmanr(num_df[col], num_df['combo_return_pct'])
                print(f"  {col:15s} | Pearson r: {p_r:+.4f} (p={p_p:.4e}) | Spearman r_s: {s_r:+.4f} (p={s_p:.4e})")

    # 3. Holding Window Bucket Analysis (Does holding longer increase MFE or MAE?)
    if 'holding_hours' in df.columns:
        df['duration_bucket'] = pd.cut(
            df['holding_hours'], 
            bins=[-1, 24, 72, 168, 720, 9999],
            labels=['<1 Day', '1-3 Days (Post-Earnings)', '3-7 Days', '7-30 Days', '>30 Days']
        )
        print("\n--- Performance & Excursion Metrics by Holding Window Bucket ---")
        bucket_stats = df.groupby('duration_bucket', observed=False).agg(
            trade_count=('combo_trade_id', 'count'),
            win_rate=('is_combo_win', 'mean'),
            avg_return=('combo_return_pct', 'mean'),
            median_return=('combo_return_pct', 'median'),
            avg_mae=('mae_pct', 'mean'),
            avg_mfe=('mfe_pct', 'mean')
        ).round(2)
        bucket_stats['win_rate'] = (bucket_stats['win_rate'] * 100).round(2)
        print(bucket_stats)

    # 4. MFE Utilization Rate (How much of peak MFE is captured at exit?)
    if 'mfe_pct' in df.columns and 'combo_return_pct' in df.columns:
        df_mfe = df[df['mfe_pct'] > 0].copy()
        if not df_mfe.empty:
            df_mfe['mfe_realized_ratio'] = df_mfe['combo_return_pct'] / df_mfe['mfe_pct']
            avg_mfe_captured = df_mfe['mfe_realized_ratio'].mean() * 100
            print(f"\n--- MFE Capture Efficiency ---")
            print(f"  Average Peak MFE Captured at Exit: {avg_mfe_captured:.2f}% of peak unrealized profit")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze MAE, MFE, and duration correlations in BigQuery")
    parser.add_argument("--backtest-id", type=str, help="Backtest ID filter")
    args = parser.parse_args()
    
    run_mae_mfe_analysis(backtest_id=args.backtest_id)
