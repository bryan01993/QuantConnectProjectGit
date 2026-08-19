"""
add_exit_reason_column.py
=========================
One-time migration script: adds the 'exit_reason' column to the existing
`bav-personal-cloud.develop.BTOPTrades` BigQuery table.

This column is populated for all future 4EVC CLOSE records logged by main.py
after the LogTradeRecord() update (exit_reason = 'Stop Loss' | 'Time Exit' |
'DTE Safety' | 'Other'). Existing rows will have NULL for this field.

Usage:
    poetry run python Scripts/BigQuery/add_exit_reason_column.py
"""

from __future__ import annotations

import os
import sys

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client  # noqa: E402

PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"
TABLE_NAME: str = "BTOPTrades"


def add_column(project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    """
    Add the exit_reason STRING column to BTOPTrades if it does not already exist.

    Args:
        project_id: GCP project that hosts the BigQuery dataset.
        dataset_id: BigQuery dataset containing BTOPTrades.
    """
    client = get_bigquery_client(project_id=project_id)
    full_table_id: str = f"{project_id}.{dataset_id}.{TABLE_NAME}"

    # Check if column already exists
    table = client.get_table(full_table_id)
    existing_fields = {field.name for field in table.schema}

    if "exit_reason" in existing_fields:
        print(f"[Migration] Column 'exit_reason' already exists in `{full_table_id}`. Nothing to do.")
        return

    print(f"[Migration] Adding 'exit_reason' STRING column to `{full_table_id}`...")

    # BigQuery DDL — ALTER TABLE ADD COLUMN is the safest approach for adding
    # a nullable column without affecting existing rows.
    alter_sql: str = f"""
        ALTER TABLE `{full_table_id}`
        ADD COLUMN exit_reason STRING
        OPTIONS (description = "Normalized exit category for CLOSE records. One of: Stop Loss, Time Exit, DTE Safety, Other. Empty string for OPEN records.")
    """

    job = client.query(alter_sql)
    job.result()

    print(f"[Migration] [OK] Column 'exit_reason' added successfully.")
    print(f"[Migration] Existing rows will have NULL for this field.")
    print(f"[Migration] Future 4EVC CLOSE records will carry the populated value.")


if __name__ == "__main__":
    add_column()
