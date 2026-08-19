-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_trade_flow
-- Purpose: Produces a Sankey-ready edge list from BTOPTrades for all algorithms
--          (0AT, 4EVC, 1SAOP, etc.) trade-flow visualization with backtest_name.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_trade_flow` AS

WITH

open_trades AS (
    SELECT
        backtestId,
        algo_code,
        pk,
        COALESCE(trade_id, pk) AS trade_id,
        underlying,
        timestamp         AS open_time,
        qty,
        vol_ratio,
        slope,
        ivrv_ratio,
        entry_price
    FROM `bav-personal-cloud.develop.BTOPTrades`
    WHERE action = 'OPEN'
),

close_trades AS (
    SELECT
        pk,
        COALESCE(trade_id, pk) AS trade_id,
        pnl,
        exit_price,
        exit_reason,
        timestamp AS close_time
    FROM `bav-personal-cloud.develop.BTOPTrades`
    WHERE action = 'CLOSE'
),

full_trades AS (
    SELECT
        o.backtestId,
        COALESCE(r.name, o.backtestId) AS backtest_name,
        o.algo_code,
        o.trade_id,
        o.pk,
        o.underlying,
        o.open_time,
        o.qty,
        o.vol_ratio,
        o.slope,
        o.ivrv_ratio,
        o.entry_price,
        c.pnl,
        c.exit_price,
        c.close_time,
        COALESCE(NULLIF(c.exit_reason, ''), 'Unknown') AS exit_reason,
        CASE
            WHEN c.pnl IS NULL     THEN 'Still Open'
            WHEN c.pnl > 0         THEN 'Winners'
            ELSE                        'Losers'
        END AS outcome
    FROM open_trades o
    LEFT JOIN close_trades c
        ON o.trade_id = c.trade_id
    LEFT JOIN `bav-personal-cloud.develop.BTOPResults` r
        ON o.backtestId = r.backtestId
),

edge_a AS (
    SELECT
        backtestId,
        backtest_name,
        algo_code,
        'All Entered Trades'    AS source_node,
        outcome                 AS target_node,
        COUNT(*)                AS trade_count,
        ROUND(AVG(pnl), 6)     AS avg_pnl,
        ROUND(SUM(pnl), 6)     AS total_pnl
    FROM full_trades
    GROUP BY backtestId, backtest_name, algo_code, outcome
),

edge_b AS (
    SELECT
        backtestId,
        backtest_name,
        algo_code,
        outcome                 AS source_node,
        exit_reason             AS target_node,
        COUNT(*)                AS trade_count,
        ROUND(AVG(pnl), 6)     AS avg_pnl,
        ROUND(SUM(pnl), 6)     AS total_pnl
    FROM full_trades
    WHERE outcome IN ('Winners', 'Losers')
    GROUP BY backtestId, backtest_name, algo_code, outcome, exit_reason
)

SELECT * FROM edge_a
UNION ALL
SELECT * FROM edge_b
ORDER BY backtest_name, source_node, target_node;
