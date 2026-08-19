-- ============================================================================
-- VIEW DDL: v_4EVC_consolidated_spread_trades
-- ============================================================================
-- Description: Authoritative consolidated view of Calendar Spread trades,
--              grouping option legs (Short & Long) into a single trade row
--              with net debit paid, net credit exit, consolidated PnL $, PnL %,
--              and strategy predictor signals (slope, vol_ratio, ivrv_ratio).
-- ============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_consolidated_spread_trades` AS
WITH enriched_legs AS (
  SELECT * FROM `bav-personal-cloud.develop.v_4EVC_enriched_trades`
),
paired_spreads AS (
  SELECT
    backtestId,
    backtest_name,
    underlying,
    engine_entry_time AS entry_time,
    MAX(engine_exit_time) AS exit_time,
    MAX(qty) AS contracts_qty,
    
    -- Short Leg (Near Expiry)
    MAX(CASE WHEN leg_direction = 'SELL_TO_OPEN' THEN contract_symbol END) AS short_leg_symbol,
    MAX(CASE WHEN leg_direction = 'SELL_TO_OPEN' THEN leg_entry_price END) AS short_leg_entry_price,
    MAX(CASE WHEN leg_direction = 'SELL_TO_OPEN' THEN leg_exit_price END) AS short_leg_exit_price,
    SUM(CASE WHEN leg_direction = 'SELL_TO_OPEN' THEN leg_pnl_dollars ELSE 0 END) AS short_leg_pnl,
    SUM(CASE WHEN leg_direction = 'SELL_TO_OPEN' THEN leg_total_fees ELSE 0 END) AS short_leg_fees,

    -- Long Leg (Far Expiry)
    MAX(CASE WHEN leg_direction = 'BUY_TO_OPEN' THEN contract_symbol END) AS long_leg_symbol,
    MAX(CASE WHEN leg_direction = 'BUY_TO_OPEN' THEN leg_entry_price END) AS long_leg_entry_price,
    MAX(CASE WHEN leg_direction = 'BUY_TO_OPEN' THEN leg_exit_price END) AS long_leg_exit_price,
    SUM(CASE WHEN leg_direction = 'BUY_TO_OPEN' THEN leg_pnl_dollars ELSE 0 END) AS long_leg_pnl,
    SUM(CASE WHEN leg_direction = 'BUY_TO_OPEN' THEN leg_total_fees ELSE 0 END) AS long_leg_fees,

    -- Net PnL and Fees
    SUM(leg_pnl_dollars) AS total_combo_pnl_dollars,
    SUM(leg_total_fees) AS total_combo_fees,

    -- Predictor Signals
    MAX(strike) AS strike,
    MAX(short_leg_expiry) AS short_leg_expiry,
    MAX(long_leg_expiry) AS long_leg_expiry,
    MAX(vol_ratio) AS vol_ratio,
    MAX(slope) AS slope,
    MAX(ivrv_ratio) AS ivrv_ratio,
    MAX(earnings_date) AS earnings_date,
    MAX(raw_parameters_json) AS raw_parameters_json
  FROM enriched_legs
  GROUP BY 
    backtestId,
    backtest_name,
    underlying,
    engine_entry_time
  HAVING short_leg_symbol IS NOT NULL AND long_leg_symbol IS NOT NULL
)
SELECT
  CONCAT(backtestId, '_', underlying, '_', FORMAT_TIMESTAMP('%Y%m%d_%H%M%S', entry_time)) AS combo_trade_id,
  backtestId,
  backtest_name,
  underlying,
  entry_time,
  exit_time,
  TIMESTAMP_DIFF(exit_time, entry_time, HOUR) AS holding_hours,
  contracts_qty,
  short_leg_symbol,
  long_leg_symbol,
  short_leg_entry_price,
  long_leg_entry_price,
  
  -- Net Debit & Cost
  ROUND(long_leg_entry_price - short_leg_entry_price, 4) AS net_debit_paid_per_unit,
  ROUND((long_leg_entry_price - short_leg_entry_price) * contracts_qty * 100, 2) AS total_net_debit_paid,
  
  short_leg_exit_price,
  long_leg_exit_price,
  ROUND(long_leg_exit_price - short_leg_exit_price, 4) AS net_credit_received_at_exit,
  
  short_leg_pnl,
  long_leg_pnl,
  total_combo_pnl_dollars,
  total_combo_fees,
  
  -- Rentabilidad Porcentual (%) sobre el débito neto invertido
  CASE 
    WHEN (long_leg_entry_price - short_leg_entry_price) > 0 
    THEN ROUND((total_combo_pnl_dollars / ((long_leg_entry_price - short_leg_entry_price) * contracts_qty * 100)) * 100, 2)
    ELSE NULL 
  END AS combo_return_pct,
  
  (total_combo_pnl_dollars > 0) AS is_combo_win,
  
  -- Predictores
  strike,
  short_leg_expiry,
  long_leg_expiry,
  vol_ratio,
  slope,
  ivrv_ratio,
  earnings_date,
  raw_parameters_json
FROM paired_spreads;
