-- ============================================================================
-- VIEW DDL: v_4EVC_flattened_trade_details
-- ============================================================================
-- Description: Flattened trade-by-trade view pairing entry/exit prices, holding
--              duration, financial PnL ($ and %), option leg attributes (short/long leg),
--              and strategy predictor variables (vol_ratio, slope, ivrv_ratio, etc.).
-- ============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_flattened_trade_details` AS
WITH open_trades AS (
  SELECT 
    REGEXP_REPLACE(t.pk, r'_(OPEN|CLOSE)$', '') AS base_trade_id,
    t.backtestId,
    COALESCE(t.backtest_name, r.name) AS backtest_name,
    t.underlying,
    t.qty,
    t.timestamp AS entry_time,
    t.entry_price AS net_entry_debit,
    t.strike,
    t.near_expiry AS short_leg_expiry,
    t.far_expiry AS long_leg_expiry,
    t.vol_ratio,
    t.slope,
    t.ivrv_ratio,
    t.earnings_date,
    t.parameters
  FROM `bav-personal-cloud.develop.BTOPTrades` t
  LEFT JOIN `bav-personal-cloud.develop.BTOPResults` r ON t.backtestId = r.backtestId
  WHERE t.action = 'OPEN'
),
close_trades AS (
  SELECT 
    REGEXP_REPLACE(pk, r'_(OPEN|CLOSE)$', '') AS base_trade_id,
    timestamp AS exit_time,
    exit_price AS net_exit_credit,
    pnl AS raw_logged_pnl,
    exit_reason
  FROM `bav-personal-cloud.develop.BTOPTrades`
  WHERE action = 'CLOSE'
)
SELECT 
  o.base_trade_id AS trade_id,
  o.backtestId,
  o.backtest_name,
  o.underlying,
  o.qty,
  o.entry_time,
  c.exit_time,
  TIMESTAMP_DIFF(c.exit_time, o.entry_time, HOUR) AS holding_hours,
  o.net_entry_debit,
  c.net_exit_credit,
  CASE 
    WHEN o.net_entry_debit > 0 AND c.net_exit_credit IS NOT NULL 
    THEN ROUND(((c.net_exit_credit - o.net_entry_debit) / o.net_entry_debit) * 100, 2)
    ELSE NULL 
  END AS net_pnl_pct,
  ROUND((COALESCE(c.net_exit_credit, 0.0) - o.net_entry_debit) * o.qty * 100, 2) AS net_pnl_dollars,
  o.strike,
  o.short_leg_expiry,
  o.long_leg_expiry,
  ROUND(o.vol_ratio, 4) AS vol_ratio,
  ROUND(o.slope, 5) AS slope,
  ROUND(o.ivrv_ratio, 4) AS ivrv_ratio,
  o.earnings_date,
  COALESCE(c.exit_reason, 'STILL OPEN') AS exit_reason,
  o.parameters
FROM open_trades o
LEFT JOIN close_trades c ON o.base_trade_id = c.base_trade_id;
