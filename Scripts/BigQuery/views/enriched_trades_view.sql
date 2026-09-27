-- ============================================================================
-- VIEW DDL: v_4EVC_enriched_trades
-- ============================================================================
-- Description: Authoritative enriched trade view joining QuantConnect Lean engine
--              closed trade leg performance (entry/exit prices, PnL $, PnL %, fees,
--              MAE, MFE, win/loss status) with strategy log metadata (vol_ratio, slope,
--              ivrv_ratio, strike, expiries, earnings_date, and flattened parameters).
-- ============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_enriched_trades` AS
WITH closed_legs AS (
  SELECT 
    c.tradeId AS engine_trade_id,
    c.backtestId AS backtestId,
    COALESCE(c.backtest_name, r.name) AS backtest_name,
    COALESCE(c.symbol.underlying.value, REGEXP_EXTRACT(c.symbol.value, r'^([A-Z]+)')) AS underlying,
    c.symbol.value AS contract_symbol,
    c.symbol.id AS contract_symbol_id,
    c.entryTime AS engine_entry_time,
    c.exitTime AS engine_exit_time,
    TIMESTAMP_DIFF(c.exitTime, c.entryTime, HOUR) AS holding_hours,
    CASE WHEN c.direction = 0 THEN 'BUY_TO_OPEN' ELSE 'SELL_TO_OPEN' END AS leg_direction,
    c.quantity AS qty,
    c.entryPrice AS leg_entry_price,
    c.exitPrice AS leg_exit_price,
    c.profitLoss AS leg_pnl_dollars,
    CASE 
      WHEN c.entryPrice > 0 
      THEN ROUND((c.profitLoss / (c.entryPrice * c.quantity * 100)) * 100, 2)
      ELSE NULL 
    END AS leg_pnl_pct,
    c.totalFees AS leg_total_fees,
    c.mae AS leg_mae,
    c.mfe AS leg_mfe,
    c.duration AS leg_duration_str,
    c.endTradeDrawdown AS leg_end_drawdown,
    c.isWin AS is_win,
    c._ingested_at
  FROM `bav-personal-cloud.develop.BTOPTotalPerformanceClosedTrades` c
  LEFT JOIN `bav-personal-cloud.develop.BTOPResults` r ON c.backtestId = r.backtestId
  WHERE REGEXP_CONTAINS(c.symbol.value, r'\d{6}[CP]\d{8}')
),
strategy_params AS (
  SELECT 
    t.backtestId,
    t.trade_id,
    t.underlying,
    MIN(t.timestamp) AS strategy_entry_time,
    MAX(t.strike) AS strike,
    MAX(t.near_expiry) AS short_leg_expiry,
    MAX(t.far_expiry) AS long_leg_expiry,
    MAX(t.vol_ratio) AS vol_ratio,
    MAX(t.slope) AS slope,
    MAX(t.ivrv_ratio) AS ivrv_ratio,
    MAX(t.earnings_date) AS earnings_date,
    MAX(t.parameters) AS raw_parameters_json,
    -- Flatten key parameters from JSON string
    MAX(SAFE_CAST(JSON_VALUE(t.parameters, '$.alpha_spread') AS FLOAT64)) AS param_alpha_spread,
    MAX(SAFE_CAST(JSON_VALUE(t.parameters, '$.target_dte') AS INT64)) AS param_target_dte,
    MAX(SAFE_CAST(JSON_VALUE(t.parameters, '$.holding_days') AS INT64)) AS param_holding_days,
    MAX(SAFE_CAST(JSON_VALUE(t.parameters, '$.min_vol_ratio') AS FLOAT64)) AS param_min_vol_ratio,
    -- Per-leg IV Lifecycle Metrics (Supports long and compact JSON keys)
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.front_iv_entry'), JSON_VALUE(t.parameters, '$.fe'), JSON_VALUE(t.parameters, '$.front_iv')) AS FLOAT64)) AS short_leg_entry_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.front_iv_min'), JSON_VALUE(t.parameters, '$.fmin')) AS FLOAT64)) AS short_leg_min_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.front_iv_max'), JSON_VALUE(t.parameters, '$.fmax')) AS FLOAT64)) AS short_leg_max_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.front_iv_exit'), JSON_VALUE(t.parameters, '$.fx')) AS FLOAT64)) AS short_leg_exit_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.front_iv_change_pct'), JSON_VALUE(t.parameters, '$.fchg')) AS FLOAT64)) AS short_leg_iv_change_pct,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.back_iv_entry'), JSON_VALUE(t.parameters, '$.be'), JSON_VALUE(t.parameters, '$.back_iv')) AS FLOAT64)) AS long_leg_entry_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.back_iv_min'), JSON_VALUE(t.parameters, '$.bmin')) AS FLOAT64)) AS long_leg_min_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.back_iv_max'), JSON_VALUE(t.parameters, '$.bmax')) AS FLOAT64)) AS long_leg_max_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.back_iv_exit'), JSON_VALUE(t.parameters, '$.bx')) AS FLOAT64)) AS long_leg_exit_iv,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.back_iv_change_pct'), JSON_VALUE(t.parameters, '$.bchg')) AS FLOAT64)) AS long_leg_iv_change_pct,
    MAX(SAFE_CAST(COALESCE(JSON_VALUE(t.parameters, '$.net_iv_crush_diff'), JSON_VALUE(t.parameters, '$.net')) AS FLOAT64)) AS net_iv_crush_diff
  FROM `bav-personal-cloud.develop.BTOPTrades` t
  WHERE t.action IN ('OPEN', 'CLOSE')
  GROUP BY t.backtestId, t.trade_id, t.underlying
),
matched AS (
  SELECT 
    c.*,
    s.strike,
    s.short_leg_expiry,
    s.long_leg_expiry,
    s.vol_ratio,
    s.slope,
    s.ivrv_ratio,
    s.earnings_date,
    s.param_alpha_spread,
    s.param_target_dte,
    s.param_holding_days,
    s.param_min_vol_ratio,
    s.short_leg_entry_iv,
    s.short_leg_min_iv,
    s.short_leg_max_iv,
    s.short_leg_exit_iv,
    s.short_leg_iv_change_pct,
    s.long_leg_entry_iv,
    s.long_leg_min_iv,
    s.long_leg_max_iv,
    s.long_leg_exit_iv,
    s.long_leg_iv_change_pct,
    s.net_iv_crush_diff,
    s.raw_parameters_json,
    ROW_NUMBER() OVER(
      PARTITION BY c.engine_trade_id 
      ORDER BY ABS(TIMESTAMP_DIFF(c.engine_entry_time, s.strategy_entry_time, SECOND)) ASC
    ) as match_rank
  FROM closed_legs c
  LEFT JOIN strategy_params s
    ON c.backtestId = s.backtestId
   AND (
     c.underlying = s.underlying 
     OR (c.underlying = 'UAA' AND s.underlying = 'UA')
     OR (c.underlying = 'UA' AND s.underlying = 'UAA')
   )
   AND ABS(TIMESTAMP_DIFF(c.engine_entry_time, s.strategy_entry_time, HOUR)) <= 48
)
SELECT 
  engine_trade_id,
  backtestId,
  backtest_name,
  underlying,
  contract_symbol,
  leg_direction,
  CASE 
    WHEN contract_symbol LIKE '%C%' THEN 'CALL'
    WHEN contract_symbol LIKE '%P%' THEN 'PUT'
    ELSE 'EQUITY'
  END AS option_type,
  qty,
  engine_entry_time,
  engine_exit_time,
  holding_hours,
  leg_entry_price,
  leg_exit_price,
  leg_pnl_dollars,
  leg_pnl_pct,
  leg_total_fees,
  leg_mae,
  leg_mfe,
  leg_end_drawdown,
  CASE WHEN is_win THEN 'WINNER' ELSE 'LOSER' END AS win_loss_status,
  -- Strategy Predictor & Parametry Attributes
  strike,
  short_leg_expiry,
  long_leg_expiry,
  ROUND(vol_ratio, 4) AS vol_ratio,
  ROUND(slope, 5) AS slope,
  ROUND(ivrv_ratio, 4) AS ivrv_ratio,
  earnings_date,
  param_alpha_spread,
  param_target_dte,
  param_holding_days,
  param_min_vol_ratio,
  -- Per-Leg IV Lifecycle Metrics
  short_leg_entry_iv,
  short_leg_min_iv,
  short_leg_max_iv,
  short_leg_exit_iv,
  short_leg_iv_change_pct,
  long_leg_entry_iv,
  long_leg_min_iv,
  long_leg_max_iv,
  long_leg_exit_iv,
  long_leg_iv_change_pct,
  net_iv_crush_diff,
  raw_parameters_json,
  _ingested_at
FROM matched
WHERE match_rank = 1;
