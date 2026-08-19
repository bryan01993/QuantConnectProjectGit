"""
set_default_ingested_at.py
===========================
Alters all existing BigQuery tables in `bav-personal-cloud.develop` (and log trades dataset if applicable)
so that the `_ingested_at` column defaults to `CURRENT_TIMESTAMP()` upon row insertion.

Usage:
    poetry run python Scripts/BigQuery/migrations/set_default_ingested_at.py
"""

from __future__ import annotations

import os
import sys
from google.cloud import bigquery

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PARENT_DIR = os.path.abspath(os.path.join(_THIS_DIR, ".."))
if _PARENT_DIR not in sys.path:
    sys.path.insert(0, _PARENT_DIR)

from db_operator import get_bigquery_client  # noqa: E402

PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"


def set_default_ingested_at(project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    client = get_bigquery_client(project_id=project_id)
    dataset_ref = client.get_dataset(f"{project_id}.{dataset_id}")
    tables = list(client.list_tables(dataset_ref))

    print(f"\n========================================================")
    print(f" Setting DEFAULT CURRENT_TIMESTAMP() for `_ingested_at` in `{project_id}.{dataset_id}`")
    print(f"========================================================\n")

    for table_item in tables:
        table_name = table_item.table_id
        # Skip views (which start with 'v_')
        if table_item.table_type == "VIEW" or table_name.startswith("v_"):
            continue

        full_table_id = f"{project_id}.{dataset_id}.{table_name}"
        try:
            table = client.get_table(full_table_id)
            col_names = [f.name for f in table.schema]
            if "_ingested_at" in col_names:
                alter_query = f"""
                ALTER TABLE `{full_table_id}`
                ALTER COLUMN `_ingested_at` SET DEFAULT CURRENT_TIMESTAMP();
                """
                job = client.query(alter_query)
                job.result()
                print(f"[SUCCESS] Set default CURRENT_TIMESTAMP() on `{table_name}._ingested_at`.")
            else:
                alter_query = f"""
                ALTER TABLE `{full_table_id}`
                ADD COLUMN `_ingested_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP();
                """
                job = client.query(alter_query)
                job.result()
                print(f"[SUCCESS] Added `_ingested_at` with default CURRENT_TIMESTAMP() to `{table_name}`.")
        except Exception as e:
            print(f"[ERROR] Failed setting default on `{table_name}`: {e}")

    print("\n[SUCCESS] Completed updating default `_ingested_at` across all BigQuery tables.")


if __name__ == "__main__":
    set_default_ingested_at()
