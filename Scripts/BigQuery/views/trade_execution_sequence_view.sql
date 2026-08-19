-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_trade_execution_sequence
-- Purpose: Sequences 4EVC trade execution order (1..N) per backtest, computing
--          trade lifecycle KPIs, signal indicators, running cumulative PnL,
--          and peak-to-trough drawdowns from BTOPTrades, joining BTOPResults for backtest_name.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_trade_execution_sequence`
OPTIONS(
  description="Sequences 4EVC trade execution order (1..N) per backtest, computing trade lifecycle KPIs, signal indicators, running cumulative PnL, and drawdowns from BTOPTrades with backtest_name."
) AS

WITH open_trades AS (
    SELECT
        backtestId,
        algo_code,
        pk,
        COALESCE(trade_id, pk) AS trade_id,
        underlying,
        timestamp AS open_time,
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

paired_trades AS (
    SELECT
        o.backtestId,
        o.algo_code,
        o.trade_id,
        o.pk,
        o.underlying,
        o.open_time,
        c.close_time,
        TIMESTAMP_DIFF(c.close_time, o.open_time, HOUR) AS holding_duration_hours,
        o.qty,
        o.vol_ratio,
        o.slope,
        o.ivrv_ratio,
        o.entry_price,
        c.exit_price,
        COALESCE(c.pnl, 0.0) AS pnl,
        COALESCE(NULLIF(c.exit_reason, ''), 'Unknown') AS exit_reason,
        CASE
            WHEN c.pnl IS NULL THEN 'Open'
            WHEN c.pnl > 0    THEN 'Winner'
            ELSE                   'Loser'
        END AS outcome,
        ROW_NUMBER() OVER (
            PARTITION BY o.backtestId 
            ORDER BY o.open_time ASC
        ) AS trade_seq
    FROM open_trades o
    LEFT JOIN close_trades c 
        ON o.trade_id = c.trade_id
),

cumulative_stats AS (
    SELECT
        *,
        SUM(pnl) OVER (
            PARTITION BY backtestId 
            ORDER BY trade_seq 
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS running_pnl
    FROM paired_trades
)

SELECT
    cs.pk,
    cs.backtestId,
    COALESCE(r.name, cs.backtestId) AS backtest_name,
    cs.algo_code,
    cs.trade_seq,
    cs.underlying,
    cs.open_time,
    cs.close_time,
    cs.holding_duration_hours,
    cs.qty,
    cs.vol_ratio,
    cs.slope,
    cs.ivrv_ratio,
    cs.entry_price,
    cs.exit_price,
    cs.pnl,
    cs.exit_reason,
    cs.outcome,
    ROUND(cs.running_pnl, 6) AS running_pnl,
    ROUND(MAX(cs.running_pnl) OVER (
        PARTITION BY cs.backtestId 
        ORDER BY cs.trade_seq 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ), 6) AS running_max_pnl,
    ROUND(cs.running_pnl - MAX(cs.running_pnl) OVER (
        PARTITION BY cs.backtestId 
        ORDER BY cs.trade_seq 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ), 6) AS drawdown
FROM cumulative_stats cs
LEFT JOIN `bav-personal-cloud.develop.BTOPResults` r
    ON cs.backtestId = r.backtestId;
