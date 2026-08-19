-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_backtest_execution_comparison
-- Purpose: Summary execution KPIs comparing 1:N backtests for 4EVC strategy
--          in Looker scorecards and comparison matrices, integrating official
--          QuantConnect platform stats with order execution metrics.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_backtest_execution_comparison`
OPTIONS(
  description="Summary execution KPIs comparing 1:N backtests for 4EVC strategy in Looker scorecards and comparison matrices."
) AS

WITH exec_stats AS (
    SELECT
        backtestId,
        algo_code,
        COUNT(*)                                                     AS total_execution_records,
        COUNTIF(outcome = 'Winner')                                  AS winning_legs,
        COUNTIF(outcome = 'Loser')                                   AS losing_legs,
        ROUND(AVG(holding_duration_hours), 2)                        AS avg_holding_hours,
        ROUND(AVG(vol_ratio), 4)                                     AS avg_vol_ratio_at_entry,
        ROUND(AVG(slope), 4)                                         AS avg_slope_at_entry,
        ROUND(AVG(ivrv_ratio), 4)                                    AS avg_ivrv_ratio_at_entry
    FROM `bav-personal-cloud.develop.v_4EVC_trade_execution_sequence`
    GROUP BY backtestId, algo_code
)

SELECT
    r.backtestId                                                 AS backtestId,
    r.name                                                       AS backtest_name,
    COALESCE(e.algo_code, '4EVC')                                AS algo_code,
    r.backtestStart,
    r.backtestEnd,
    t.totalNumberOfTrades                                        AS total_completed_trades,
    ROUND(p.winRate, 4)                                          AS platform_win_rate,
    ROUND(p.lossRate, 4)                                         AS platform_loss_rate,
    ROUND(p.totalNetProfit, 6)                                   AS platform_net_profit,
    ROUND(p.compoundingAnnualReturn, 6)                          AS compounding_annual_return,
    ROUND(p.drawdown, 6)                                         AS platform_max_drawdown,
    ROUND(p.sharpeRatio, 4)                                      AS platform_sharpe_ratio,
    ROUND(p.sortinoRatio, 4)                                     AS platform_sortino_ratio,
    e.total_execution_records,
    e.avg_holding_hours,
    e.avg_vol_ratio_at_entry,
    e.avg_slope_at_entry,
    e.avg_ivrv_ratio_at_entry
FROM `bav-personal-cloud.develop.BTOPResults` r
LEFT JOIN `bav-personal-cloud.develop.BTOPTotalPerformancePortfolioStats` p ON r.backtestId = p.backtestId
LEFT JOIN `bav-personal-cloud.develop.BTOPTotalPerformanceTradeStats` t ON r.backtestId = t.backtestId
LEFT JOIN exec_stats e ON r.backtestId = e.backtestId
WHERE r.name LIKE '%4EVC%' OR e.algo_code = '4EVC';
