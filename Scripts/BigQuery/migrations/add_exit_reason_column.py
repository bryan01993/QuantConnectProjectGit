"""
add_exit_reason_column.py
=========================
One-time migration script: adds the 'exit_reason' column to the existing
`bav-personal-cloud.develop.BTOPTrades` BigQuery table.

Usage:
    poetry run python Scripts/BigQuery/migrations/add_exit_reason_column.py
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
TABLE_NAME: str = "BTOPTrades"


def add_column(project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    client = get_bigquery_client(project_id=project_id)
    full_table_id: str = f"{project_id}.{dataset_id}.{TABLE_NAME}"

    table = client.get_table(full_table_id)
    existing_fields = {field.name for field in table.schema}

    if "exit_reason" in existing_fields:
        print(f"[Migration] Column 'exit_reason' already exists in `{full_table_id}`. Nothing to do.")
        return

    print(f"[Migration] Adding 'exit_reason' STRING column to `{full_table_id}`...")

    alter_sql: str = f"""
        ALTER TABLE `{full_table_id}`
        ADD COLUMN exit_reason STRING
        OPTIONS (description = "Normalized exit category for CLOSE records. One of: Stop Loss, Take Profit, Time Exit, DTE Safety, Signal Exit, Risk Exit, Other.")
    """

    job = client.query(alter_sql)
    job.result()

    print(f"[Migration] [OK] Column 'exit_reason' added successfully to `{full_table_id}`.")


if __name__ == "__main__":
    add_column()
