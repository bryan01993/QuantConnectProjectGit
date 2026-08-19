-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_trade_return_summary_stats
-- Purpose: Pre-computes Pandas .describe() summary statistics (count, mean, std,
--          min, 25%, 50%, 75%, max) and VaR tail percentiles (5%, 1%, 0.1%, 0.01%)
--          per backtest for display alongside 4EVC histograms in Looker Studio.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_trade_return_summary_stats`
OPTIONS(
  description="Pandas .describe() and VaR tail percentiles per backtest for 4EVC profit histograms in Looker Studio."
) AS

SELECT
    backtestId,
    backtest_name,
    COUNT(pnl) AS count,
    ROUND(AVG(pnl), 6) AS mean,
    ROUND(STDDEV(pnl), 6) AS std,
    ROUND(MIN(pnl), 6) AS min,
    ROUND(APPROX_QUANTILES(pnl, 10000)[OFFSET(2500)], 6) AS p25,
    ROUND(APPROX_QUANTILES(pnl, 10000)[OFFSET(5000)], 6) AS p50_median,
    ROUND(APPROX_QUANTILES(pnl, 10000)[OFFSET(7500)], 6) AS p75,
    ROUND(MAX(pnl), 6) AS max,
    -- Extreme tail percentiles (VaR)
    ROUND(APPROX_QUANTILES(pnl, 10000)[OFFSET(500)], 6) AS var_5pct,   -- 5.00% of time
    ROUND(APPROX_QUANTILES(pnl, 10000)[OFFSET(100)], 6) AS var_1pct,   -- 1.00% of time
    ROUND(APPROX_QUANTILES(pnl, 10000)[OFFSET(10)], 6)  AS var_01pct,  -- 0.10% of time
    ROUND(APPROX_QUANTILES(pnl, 10000)[OFFSET(1)], 6)   AS var_001pct  -- 0.01% of time
FROM `bav-personal-cloud.develop.v_4EVC_trade_execution_sequence`
WHERE pnl IS NOT NULL
GROUP BY backtestId, backtest_name;
