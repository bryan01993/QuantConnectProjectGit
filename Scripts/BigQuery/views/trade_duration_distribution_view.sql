-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_trade_duration_distribution
-- Purpose: Bins 4EVC trade holding durations (in hours and days) into positive
--          numeric bins for continuous frequency distribution plots in Looker Studio.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_trade_duration_distribution`
OPTIONS(
  description="High-resolution continuous numeric binning for 4EVC trade holding duration distribution histograms in Looker Studio."
) AS

SELECT
    tes.pk,
    tes.backtestId,
    tes.backtest_name,
    tes.algo_code,
    tes.trade_seq,
    tes.underlying,
    tes.open_time,
    tes.close_time,
    tes.pnl AS return_pct,
    tes.outcome, -- 'Winner', 'Loser'
    
    -- Numeric holding duration in hours (must be >= 0)
    tes.holding_duration_hours,
    
    -- Numeric holding duration in days
    ROUND(tes.holding_duration_hours / 24.0, 2) AS holding_duration_days,

    -- Continuous numeric bin in hours (0, 1, 2, 3... 278) for native numeric X-axis sorting in Looker
    tes.holding_duration_hours AS duration_bin_hours,

    -- Continuous numeric bin in days rounded to 0.5 day resolution (0.0, 0.5, 1.0, 1.5...)
    ROUND(FLOOR(tes.holding_duration_hours / 12.0) * 0.5, 1) AS duration_bin_days,

    -- Formatted label for tooltips
    CASE
        WHEN tes.holding_duration_hours < 24 THEN CONCAT(CAST(tes.holding_duration_hours AS STRING), 'h')
        ELSE CONCAT(CAST(ROUND(tes.holding_duration_hours / 24.0, 1) AS STRING), 'd (', CAST(tes.holding_duration_hours AS STRING), 'h)')
    END AS duration_bin_label

FROM `bav-personal-cloud.develop.v_4EVC_trade_execution_sequence` tes
WHERE tes.holding_duration_hours IS NOT NULL 
  AND tes.holding_duration_hours >= 0;
