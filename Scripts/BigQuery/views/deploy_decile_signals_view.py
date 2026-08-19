"""
deploy_decile_signals_view.py
=============================
Deploys the BigQuery view `bav-personal-cloud.develop.v_4EVC_decile_signals`
which performs per-backtest NTILE(10) decile binning for 4EVC entry signals.

Usage:
    poetry run python Scripts/BigQuery/views/deploy_decile_signals_view.py
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
VIEW_NAME:  str = "v_4EVC_decile_signals"
SQL_FILE:   str = os.path.join(_THIS_DIR, "decile_signals_view.sql")


def load_sql(sql_path: str) -> str:
    with open(sql_path, "r", encoding="utf-8") as fh:
        return fh.read()


def deploy_view(project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    print(f"[Decile View] Deploying view '{VIEW_NAME}' to `{project_id}.{dataset_id}`...")
    client = get_bigquery_client(project_id=project_id)

    sql: str = load_sql(SQL_FILE)
    print(f"[Decile View] Loaded SQL from: {SQL_FILE}")

    job = client.query(sql)
    job.result()

    full_view_id: str = f"{project_id}.{dataset_id}.{VIEW_NAME}"
    validation_sql: str = (
        f"SELECT metric_name, decile_bucket, SUM(trade_count) AS total_trades, "
        f"ROUND(AVG(mean_pnl), 6) AS avg_pnl "
        f"FROM `{full_view_id}` "
        f"GROUP BY metric_name, decile_bucket "
        f"ORDER BY metric_name, decile_bucket "
        f"LIMIT 30"
    )
    print(f"\n[Decile View] View created. Running validation query...")
    validation_job = client.query(validation_sql)
    results = list(validation_job.result())

    if results:
        print(f"\n[Decile View] [OK] View is populated. Summary:")
        for row in results:
            print(
                f"    Metric: {row.metric_name:12s} | Decile: {row.decile_bucket:2d} | "
                f"Trades: {row.total_trades:4d} | Mean PnL: {row.avg_pnl:+.4%}"
            )
    else:
        print(
            f"\n[Decile View] [WARN] View created but returned no rows. "
            f"Run log_trades_uploader.py to populate 4EVC trade logs."
        )

    print(f"\n[Decile View] Done. Project: {project_id} | Dataset: {dataset_id} | View: {VIEW_NAME}\n")


if __name__ == "__main__":
    deploy_view()
