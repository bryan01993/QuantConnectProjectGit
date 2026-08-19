-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_trade_return_distribution
-- Purpose: Provides high-resolution numeric binning (0.01 step = 1% return bins)
--          for 4EVC consolidated calendar spread trade returns (combined legs PnL),
--          matching matplotlib/seaborn density plots in Looker Studio.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_trade_return_distribution`
OPTIONS(
  description="High-resolution numeric binning (0.01 resolution) for 4EVC consolidated spread trade return density histograms in Looker Studio based on combined calendar spread legs."
) AS

SELECT
    c.combo_trade_id AS pk,
    c.backtestId,
    c.backtest_name,
    '4EVC' AS algo_code,
    c.underlying,
    c.entry_time AS open_time,
    c.exit_time AS close_time,
    ROUND(c.combo_return_pct / 100.0, 4) AS return_pct,
    CASE WHEN c.is_combo_win THEN 'Winner' ELSE 'Loser' END AS outcome,

    -- Pure continuous numeric bin (0.01 / 1% step: -1.00, -0.99, ..., 0.00, 0.01, ..., +1.00)
    ROUND(c.combo_return_pct / 100.0, 2) AS return_bin,

    -- Fine bin label formatted as percentage for tooltips
    CONCAT(CAST(CAST(ROUND(c.combo_return_pct, 0) AS INT64) AS STRING), '%') AS return_bin_label

FROM `bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades` c
WHERE c.combo_return_pct IS NOT NULL;
