"""
deploy_trade_flow_view.py
=========================
Deploys the BigQuery view `bav-personal-cloud.develop.v_4EVC_trade_flow`
which produces a Sankey-ready edge list for all algorithms in BTOPTrades.

Usage:
    poetry run python Scripts/BigQuery/views/deploy_trade_flow_view.py
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
VIEW_NAME:  str = "v_4EVC_trade_flow"
SQL_FILE:   str = os.path.join(_THIS_DIR, "trade_flow_view.sql")


def load_sql(sql_path: str) -> str:
    with open(sql_path, "r", encoding="utf-8") as fh:
        return fh.read()


def deploy_view(project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    print(f"[Trade Flow View] Deploying view '{VIEW_NAME}' to `{project_id}.{dataset_id}`...")
    client = get_bigquery_client(project_id=project_id)

    sql: str = load_sql(SQL_FILE)
    print(f"[Trade Flow View] Loaded SQL from: {SQL_FILE}")

    job = client.query(sql)
    job.result()

    full_view_id: str = f"{project_id}.{dataset_id}.{VIEW_NAME}"
    validation_sql: str = (
        f"SELECT source_node, target_node, SUM(trade_count) AS total_trades "
        f"FROM `{full_view_id}` "
        f"GROUP BY source_node, target_node "
        f"ORDER BY source_node, target_node "
        f"LIMIT 20"
    )
    print(f"\n[Trade Flow View] View created. Running validation query...")
    validation_job = client.query(validation_sql)
    results = list(validation_job.result())

    if results:
        print(f"\n[Trade Flow View] [OK] View is populated. Edge summary:")
        for row in results:
            print(
                f"    {row.source_node!r:28s} -> {row.target_node!r:15s}  "
                f"trades={row.total_trades}"
            )
    else:
        print(
            f"\n[Trade Flow View] [WARN] View created but returned no rows. "
            f"Run log_trades_uploader.py to populate trade logs."
        )

    print(f"\n[Trade Flow View] Done. Project: {project_id} | Dataset: {dataset_id} | View: {VIEW_NAME}\n")


if __name__ == "__main__":
    deploy_view()
