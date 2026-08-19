"""
deploy_all_views.py
===================
Deploys all 4EVC BigQuery views for Looker research dashboards:
1. v_4EVC_trade_execution_sequence
2. v_4EVC_trade_flow
3. v_4EVC_decile_signals
4. v_4EVC_backtest_execution_comparison

Usage:
    poetry run python Scripts/BigQuery/views/deploy_all_views.py
"""

from __future__ import annotations

import os
import sys

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_BQ_DIR = os.path.abspath(os.path.join(_THIS_DIR, ".."))
if _BQ_DIR not in sys.path:
    sys.path.insert(0, _BQ_DIR)

from db_operator import get_bigquery_client  # noqa: E402

PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"

VIEWS = [
    ("v_4EVC_enriched_trades", "enriched_trades_view.sql"),
    ("v_4EVC_consolidated_spread_trades", "consolidated_spread_trades_view.sql"),
    ("v_4EVC_trade_execution_sequence", "trade_execution_sequence_view.sql"),
    ("v_4EVC_trade_flow", "trade_flow_view.sql"),
    ("v_4EVC_decile_signals", "decile_signals_view.sql"),
    ("v_4EVC_backtest_execution_comparison", "backtest_execution_comparison_view.sql"),
    ("v_4EVC_batch_concatenated_trades", "batch_concatenated_trades_view.sql"),
    ("v_4EVC_trade_return_distribution", "trade_return_distribution_view.sql"),
    ("v_4EVC_trade_duration_distribution", "trade_duration_distribution_view.sql"),
    ("v_4EVC_trade_return_summary_stats", "trade_return_summary_stats_view.sql"),
    ("v_4EVC_sankey_trade_flow", "sankey_trade_flow_view.sql"),
    ("v_4EVC_flattened_trade_details", "flattened_trade_details_view.sql"),
    ("v_4EVC_trade_duration_return_summary", "trade_duration_return_summary_view.sql"),
]





def load_sql(sql_filename: str) -> str:
    sql_path = os.path.join(_THIS_DIR, sql_filename)
    with open(sql_path, "r", encoding="utf-8") as fh:
        return fh.read()


def deploy_all(project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    print(f"\n========================================================")
    print(f" Deploying All 4EVC BigQuery Views to `{project_id}.{dataset_id}`")
    print(f"========================================================\n")
    client = get_bigquery_client(project_id=project_id)

    for view_name, sql_file in VIEWS:
        print(f"[Deploying] View '{view_name}' from {sql_file}...")
        sql = load_sql(sql_file)
        job = client.query(sql)
        job.result()
        print(f"[SUCCESS] View `{project_id}.{dataset_id}.{view_name}` successfully deployed.")

    print(f"\n[SUCCESS] All 4EVC BigQuery views deployed successfully!\n")


if __name__ == "__main__":
    deploy_all()
