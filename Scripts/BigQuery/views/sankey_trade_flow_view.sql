-- ============================================================================
-- VIEW DDL: v_4EVC_sankey_trade_flow
-- ============================================================================
-- Description: Standardized Sankey diagram edge list capturing the complete
--              order lifecycle: Total Orders Sent -> Orders Accepted / Cancelled
--              -> Total Entered Trades -> Winners / Losers / Still Open -> Exit Outcomes.
--              Features COALESCE(o.backtest_name, r.name) to guarantee order flow
--              rows match backtest_name filtering even if BTOPOrders.backtest_name is NULL.
-- ============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_sankey_trade_flow` AS
WITH order_stats AS (
  -- 1. Granular order stats from BTOPOrders with COALESCE to BTOPResults
  SELECT 
    o.backtestId,
    COALESCE(o.backtest_name, r.name) AS backtest_name,
    COUNT(*) AS total_orders_sent,
    COUNTIF(CAST(o.status AS STRING) IN ('5', '6', '2', '1', 'Filled', 'PartiallyFilled', 'OptionAssignment', 'Submitted')) AS orders_accepted,
    COUNTIF(CAST(o.status AS STRING) IN ('3', '4', '7', '8', '9', 'Canceled', 'Invalid', 'CancelPending', 'Error')) AS orders_cancelled
  FROM `bav-personal-cloud.develop.BTOPOrders` o
  LEFT JOIN `bav-personal-cloud.develop.BTOPResults` r ON o.backtestId = r.backtestId
  GROUP BY o.backtestId, COALESCE(o.backtest_name, r.name)

  UNION DISTINCT

  -- 2. Fallback for legacy backtests missing BTOPOrders using BTOPStatistics
  SELECT 
    r.backtestId,
    r.name AS backtest_name,
    CAST(s.totalOrders AS INT64) AS total_orders_sent,
    CAST(s.totalOrders AS INT64) AS orders_accepted,
    0 AS orders_cancelled
  FROM `bav-personal-cloud.develop.BTOPResults` r
  JOIN `bav-personal-cloud.develop.BTOPStatistics` s ON r.backtestId = s.backtestId
  WHERE r.backtestId NOT IN (SELECT DISTINCT backtestId FROM `bav-personal-cloud.develop.BTOPOrders`)
    AND s.totalOrders IS NOT NULL
    AND CAST(s.totalOrders AS INT64) > 0
),
closed_positions AS (
  SELECT 
    c.backtestId AS backtestId,
    COALESCE(c.backtest_name, r.name) AS backtest_name,
    COUNT(*) AS entered_trades,
    0 AS still_open_trades,
    COUNTIF(c.isWin = true) AS winners_count,
    COUNTIF(c.isWin = false) AS losers_count
  FROM `bav-personal-cloud.develop.BTOPTotalPerformanceClosedTrades` c
  LEFT JOIN `bav-personal-cloud.develop.BTOPResults` r ON c.backtestId = r.backtestId
  GROUP BY c.backtestId, COALESCE(c.backtest_name, r.name)
),
trade_exit_reasons AS (
  SELECT 
    t.backtestId,
    -- Winner Exit Paths
    COUNTIF(t.action = 'CLOSE' AND t.pnl > 0 AND t.exit_reason LIKE '%Take Profit%') AS winner_take_profit,
    COUNTIF(t.action = 'CLOSE' AND t.pnl > 0 AND t.exit_reason LIKE '%Stop Loss%') AS winner_stop_loss,
    COUNTIF(t.action = 'CLOSE' AND t.pnl > 0 AND (t.exit_reason LIKE '%DTE%' OR t.exit_reason LIKE '%Expiry Safety%')) AS winner_expire_protection,
    COUNTIF(t.action = 'CLOSE' AND t.pnl > 0 AND (t.exit_reason LIKE '%Time%' OR t.exit_reason LIKE '%Post-Market%')) AS winner_time_exit,
    
    -- Loser Exit Paths
    COUNTIF(t.action = 'CLOSE' AND t.pnl <= 0 AND t.exit_reason LIKE '%Take Profit%') AS loser_take_profit,
    COUNTIF(t.action = 'CLOSE' AND t.pnl <= 0 AND t.exit_reason LIKE '%Stop Loss%') AS loser_stop_loss,
    COUNTIF(t.action = 'CLOSE' AND t.pnl <= 0 AND (t.exit_reason LIKE '%DTE%' OR t.exit_reason LIKE '%Expiry Safety%' OR t.exit_reason LIKE '%Margin Call%')) AS loser_expire_protection,
    COUNTIF(t.action = 'CLOSE' AND t.pnl <= 0 AND (t.exit_reason LIKE '%Time%' OR t.exit_reason LIKE '%Post-Market%')) AS loser_time_exit
  FROM `bav-personal-cloud.develop.BTOPTrades` t
  GROUP BY t.backtestId
),
trade_exits AS (
  SELECT 
    cp.backtestId,
    cp.backtest_name,
    cp.entered_trades,
    cp.still_open_trades,
    cp.winners_count,
    cp.losers_count,
    COALESCE(te.winner_take_profit, cp.winners_count) AS winner_take_profit,
    COALESCE(te.winner_stop_loss, 0) AS winner_stop_loss,
    COALESCE(te.winner_expire_protection, 0) AS winner_expire_protection,
    COALESCE(te.winner_time_exit, 0) AS winner_time_exit,
    COALESCE(te.loser_stop_loss, cp.losers_count) AS loser_stop_loss,
    COALESCE(te.loser_expire_protection, 0) AS loser_expire_protection,
    COALESCE(te.loser_take_profit, 0) AS loser_take_profit,
    COALESCE(te.loser_time_exit, 0) AS loser_time_exit
  FROM closed_positions cp
  LEFT JOIN trade_exit_reasons te ON cp.backtestId = te.backtestId
)
-- Edge List for Sankey Diagram
SELECT backtestId, backtest_name, 'Total Orders Sent' AS source, 'Total Orders Accepted' AS target, orders_accepted AS flow_value FROM order_stats WHERE orders_accepted > 0
UNION ALL
SELECT backtestId, backtest_name, 'Total Orders Sent' AS source, 'Total Orders Cancelled/Rejected' AS target, orders_cancelled AS flow_value FROM order_stats WHERE orders_cancelled > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Total Orders Accepted' AS source, 'Total Entered Trades' AS target, entered_trades AS flow_value FROM trade_exits WHERE entered_trades > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Total Entered Trades' AS source, 'Still Open' AS target, still_open_trades AS flow_value FROM trade_exits WHERE still_open_trades > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Total Entered Trades' AS source, 'Winners' AS target, winners_count AS flow_value FROM trade_exits WHERE winners_count > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Total Entered Trades' AS source, 'Losers' AS target, losers_count AS flow_value FROM trade_exits WHERE losers_count > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Winners' AS source, 'Take Profit' AS target, winner_take_profit AS flow_value FROM trade_exits WHERE winner_take_profit > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Winners' AS source, 'Stop Loss' AS target, winner_stop_loss AS flow_value FROM trade_exits WHERE winner_stop_loss > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Winners' AS source, 'Expire Protection' AS target, winner_expire_protection AS flow_value FROM trade_exits WHERE winner_expire_protection > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Winners' AS source, 'Time Based Exit' AS target, winner_time_exit AS flow_value FROM trade_exits WHERE winner_time_exit > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Losers' AS source, 'Take Profit' AS target, loser_take_profit AS flow_value FROM trade_exits WHERE loser_take_profit > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Losers' AS source, 'Stop Loss' AS target, loser_stop_loss AS flow_value FROM trade_exits WHERE loser_stop_loss > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Losers' AS source, 'Expire Protection' AS target, loser_expire_protection AS flow_value FROM trade_exits WHERE loser_expire_protection > 0
UNION ALL
SELECT backtestId AS backtestId, backtest_name, 'Losers' AS source, 'Time Based Exit' AS target, loser_time_exit AS flow_value FROM trade_exits WHERE loser_time_exit > 0;
