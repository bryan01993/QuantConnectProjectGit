-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_decile_signals
-- Purpose: Performs partitioned NTILE(10) decile binning for 4EVC entry signals
--          (vol_ratio, slope, ivrv_ratio) across consolidated Calendar Spread trades 
--          (v_4EVC_consolidated_spread_trades) per backtestId/backtest_name.
--          Provides exactly 10 standardized decile buckets (D01..D10) per metric
--          for clean 10-point line graphs in Looker Studio.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_decile_signals`
OPTIONS(
  description="Performs partitioned NTILE(10) decile binning for 4EVC entry signals (vol_ratio, slope, ivrv_ratio) on consolidated spread trades (v_4EVC_consolidated_spread_trades) linked strictly to Mean Realized Spread Return PnL %, providing exactly 10 standardized decile buckets (D01..D10) per metric per backtest for Looker research graphs."
) AS

WITH
closed_trades AS (
    SELECT
        '4EVC' AS algo_code,
        backtestId,
        backtest_name,
        combo_trade_id AS pk,
        underlying,
        exit_time,
        vol_ratio,
        slope,
        ivrv_ratio,
        combo_return_pct AS pnl
    FROM `bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades`
    WHERE
        vol_ratio IS NOT NULL
        AND slope IS NOT NULL
        AND ivrv_ratio IS NOT NULL
        AND combo_return_pct IS NOT NULL
),

binned_trades AS (
    SELECT
        *,
        NTILE(10) OVER (PARTITION BY backtestId ORDER BY vol_ratio ASC)  AS decile_vol_ratio,
        NTILE(10) OVER (PARTITION BY backtestId ORDER BY slope ASC)      AS decile_slope,
        NTILE(10) OVER (PARTITION BY backtestId ORDER BY ivrv_ratio ASC) AS decile_ivrv_ratio
    FROM closed_trades
),

vol_ratio_deciles AS (
    SELECT
        algo_code,
        backtestId,
        backtest_name,
        'vol_ratio'              AS metric_name,
        decile_vol_ratio         AS decile_bucket,
        CONCAT('D', LPAD(CAST(decile_vol_ratio AS STRING), 2, '0')) AS decile_label,
        COUNT(*)                 AS trade_count,
        ROUND(AVG(vol_ratio), 5) AS avg_metric_value,
        ROUND(MIN(vol_ratio), 5) AS min_metric_value,
        ROUND(MAX(vol_ratio), 5) AS max_metric_value,
        CONCAT('(', CAST(ROUND(MIN(vol_ratio), 4) AS STRING), ', ', CAST(ROUND(MAX(vol_ratio), 4) AS STRING), ']') AS decile_range_label,
        ROUND(AVG(pnl), 4)       AS mean_pnl,
        0.0                      AS zero_pnl_benchmark,
        ROUND(SUM(pnl), 4)       AS total_pnl,
        ROUND(COUNTIF(pnl > 0) / COUNT(*), 4) AS win_rate
    FROM binned_trades
    GROUP BY algo_code, backtestId, backtest_name, decile_vol_ratio
),

slope_deciles AS (
    SELECT
        algo_code,
        backtestId,
        backtest_name,
        'slope'                  AS metric_name,
        decile_slope             AS decile_bucket,
        CONCAT('D', LPAD(CAST(decile_slope AS STRING), 2, '0')) AS decile_label,
        COUNT(*)                 AS trade_count,
        ROUND(AVG(slope), 5)     AS avg_metric_value,
        ROUND(MIN(slope), 5)     AS min_metric_value,
        ROUND(MAX(slope), 5)     AS max_metric_value,
        CONCAT('(', CAST(ROUND(MIN(slope), 4) AS STRING), ', ', CAST(ROUND(MAX(slope), 4) AS STRING), ']') AS decile_range_label,
        ROUND(AVG(pnl), 4)       AS mean_pnl,
        0.0                      AS zero_pnl_benchmark,
        ROUND(SUM(pnl), 4)       AS total_pnl,
        ROUND(COUNTIF(pnl > 0) / COUNT(*), 4) AS win_rate
    FROM binned_trades
    GROUP BY algo_code, backtestId, backtest_name, decile_slope
),

ivrv_ratio_deciles AS (
    SELECT
        algo_code,
        backtestId,
        backtest_name,
        'ivrv_ratio'              AS metric_name,
        decile_ivrv_ratio         AS decile_bucket,
        CONCAT('D', LPAD(CAST(decile_ivrv_ratio AS STRING), 2, '0')) AS decile_label,
        COUNT(*)                  AS trade_count,
        ROUND(AVG(ivrv_ratio), 5) AS avg_metric_value,
        ROUND(MIN(ivrv_ratio), 5) AS min_metric_value,
        ROUND(MAX(ivrv_ratio), 5) AS max_metric_value,
        CONCAT('(', CAST(ROUND(MIN(ivrv_ratio), 4) AS STRING), ', ', CAST(ROUND(MAX(ivrv_ratio), 4) AS STRING), ']') AS decile_range_label,
        ROUND(AVG(pnl), 4)        AS mean_pnl,
        0.0                       AS zero_pnl_benchmark,
        ROUND(SUM(pnl), 4)        AS total_pnl,
        ROUND(COUNTIF(pnl > 0) / COUNT(*), 4) AS win_rate
    FROM binned_trades
    GROUP BY algo_code, backtestId, backtest_name, decile_ivrv_ratio
)

SELECT * FROM vol_ratio_deciles
UNION ALL
SELECT * FROM slope_deciles
UNION ALL
SELECT * FROM ivrv_ratio_deciles
ORDER BY metric_name, backtestId, decile_bucket;
