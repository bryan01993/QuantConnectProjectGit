-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_trade_duration_return_summary
-- Purpose: Groups 4EVC consolidated calendar spread trades by holding duration bins
--          per backtestId, computing min, max, and avg combo_return_pct (PnL %),
--          trade counts, and win rates for duration sensitivity analysis.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_trade_duration_return_summary`
OPTIONS(
  description="Groups consolidated spread trades into holding duration bins per backtestId, returning min, max, avg combo_return_pct, trade count, and win rate."
) AS

WITH binned_trades AS (
  SELECT
    backtestId,
    backtest_name,
    combo_trade_id,
    underlying,
    holding_hours,
    combo_return_pct,
    CASE
      WHEN holding_hours < 12 THEN 1
      WHEN holding_hours < 24 THEN 2
      WHEN holding_hours < 48 THEN 3
      WHEN holding_hours < 72 THEN 4
      WHEN holding_hours < 120 THEN 5
      ELSE 6
    END AS duration_bin_order,
    CASE
      WHEN holding_hours < 12 THEN '0-12h'
      WHEN holding_hours < 24 THEN '12-24h'
      WHEN holding_hours < 48 THEN '24-48h (1-2d)'
      WHEN holding_hours < 72 THEN '48-72h (2-3d)'
      WHEN holding_hours < 120 THEN '72-120h (3-5d)'
      ELSE '>120h (>5d)'
    END AS duration_bin
  FROM `bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades`
  WHERE combo_return_pct IS NOT NULL AND holding_hours IS NOT NULL
)

SELECT
  backtestId,
  backtest_name,
  duration_bin_order,
  duration_bin,
  COUNT(*) AS total_trades,
  COUNTIF(combo_return_pct > 0) AS winning_trades,
  COUNTIF(combo_return_pct <= 0) AS losing_trades,
  ROUND(COUNTIF(combo_return_pct > 0) / COUNT(*) * 100, 2) AS win_rate_pct,
  ROUND(MIN(combo_return_pct), 2) AS min_combo_return_pct,
  ROUND(MAX(combo_return_pct), 2) AS max_combo_return_pct,
  ROUND(AVG(combo_return_pct), 2) AS avg_combo_return_pct
FROM binned_trades
GROUP BY backtestId, backtest_name, duration_bin_order, duration_bin
ORDER BY duration_bin_order ASC;
