-- =============================================================================
-- View: bav-personal-cloud.develop.v_4EVC_batch_concatenated_trades
-- Purpose: Concatenates multi-period, chunked backtest runs (e.g. 2022, 2023, 2024)
--          by batch_id, re-sequencing all trade executions chronologically,
--          and computing multi-year running equity curves, cumulative PnL,
--          peak-to-trough drawdowns, and combined win rates in BigQuery.
-- =============================================================================

CREATE OR REPLACE VIEW `bav-personal-cloud.develop.v_4EVC_batch_concatenated_trades`
OPTIONS(
  description="Concatenates multi-period chunked backtests (2022, 2023, 2024) by batch_id into a single continuous time series, computing multi-year equity curves, cumulative PnL, drawdowns, and trade stats."
) AS

WITH open_trades AS (
    SELECT
        COALESCE(batch_id, backtestId) AS batch_id,
        chunk_index,
        backtestId,
        COALESCE(backtest_name, backtestId) AS backtest_name,
        algo_code,
        pk,
        COALESCE(trade_id, pk)               AS trade_id,
        underlying,
        timestamp                           AS open_time,
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
        o.batch_id,
        o.chunk_index,
        o.backtestId,
        o.backtest_name,
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
        COALESCE(c.pnl, 0.0)                            AS pnl,
        COALESCE(NULLIF(c.exit_reason, ''), 'Unknown') AS exit_reason,
        CASE
            WHEN c.pnl IS NULL THEN 'Open'
            WHEN c.pnl > 0     THEN 'Winner'
            ELSE                    'Loser'
        END AS outcome,
        ROW_NUMBER() OVER (
            PARTITION BY o.batch_id 
            ORDER BY o.open_time ASC
        ) AS batch_trade_seq
    FROM open_trades o
    LEFT JOIN close_trades c 
        ON o.trade_id = c.trade_id
),

cumulative_batch_stats AS (
    SELECT
        *,
        SUM(pnl) OVER (
            PARTITION BY batch_id 
            ORDER BY batch_trade_seq 
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS batch_running_pnl
    FROM paired_trades
)

SELECT
    pk,
    batch_id,
    chunk_index,
    backtestId,
    backtest_name,
    algo_code,
    batch_trade_seq,
    underlying,
    open_time,
    close_time,
    holding_duration_hours,
    qty,
    vol_ratio,
    slope,
    ivrv_ratio,
    entry_price,
    exit_price,
    pnl,
    exit_reason,
    outcome,
    ROUND(batch_running_pnl, 6) AS batch_running_pnl,
    ROUND(MAX(batch_running_pnl) OVER (
        PARTITION BY batch_id 
        ORDER BY batch_trade_seq 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ), 6) AS batch_running_max_pnl,
    ROUND(batch_running_pnl - MAX(batch_running_pnl) OVER (
        PARTITION BY batch_id 
        ORDER BY batch_trade_seq 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ), 6) AS batch_drawdown
FROM cumulative_batch_stats;
