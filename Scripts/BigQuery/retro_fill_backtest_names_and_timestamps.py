"""
retro_fill_backtest_names_and_timestamps.py
=============================================
1. Alters all BigQuery tables in `bav-personal-cloud.develop` to add:
   - `backtest_name` (STRING, NULLABLE)
   - `_ingested_at` (TIMESTAMP, NULLABLE, DEFAULT CURRENT_TIMESTAMP())
2. Populates `backtest_name` for all existing historical rows by joining `BTOPResults`.
3. Populates `_ingested_at = CURRENT_TIMESTAMP()` for all existing rows where `_ingested_at` is NULL.

Usage:
    poetry run python Scripts/BigQuery/retro_fill_backtest_names_and_timestamps.py
"""

from __future__ import annotations

import os
import sys
from typing import Dict, List, Tuple
from google.cloud import bigquery

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client  # noqa: E402

PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"

# Mapping of table_name -> foreign_key_column_name pointing to backtestId / backtest_run_id
TABLE_FK_MAP: Dict[str, str] = {
    "BTOPTrades": "backtest_run_id",
    "BTOPOrders": "backtestId",
    "BTOPCharts": "backtestId",
    "BTOPTotalPerformancePortfolioStats": "backtestId",
    "BTOPTotalPerformanceTradeStats": "backtestId",
    "BTOPTotalPerformanceClosedTrades": "backtestId",
    "BTOPRollingWindowPortfolioStats": "backtestId",
    "BTOPRollingWindowTradeStats": "backtestId",
    "BTOPRuntimeStatistics": "backtestId",
    "BTOPStatistics": "backtestId",
    "BTOPErrors": "backtestId",
    "BTOPParameterSet": "backtestId",
    "BTOPResearchGuide": "backtestId",
    "BTOPBatchChunks": "backtest_id",
}


def alter_and_fill_tables(project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    print(f"\n========================================================")
    print(f" Standardizing Columns & Retro-filling `{project_id}.{dataset_id}`")
    print(f"========================================================\n")
    client = get_bigquery_client(project_id=project_id)
    dataset_ref = f"{project_id}.{dataset_id}"

    # 1. Step 1: Alter tables to add backtest_name and _ingested_at if missing
    for table_name, fk_col in TABLE_FK_MAP.items():
        table_ref = f"{dataset_ref}.{table_name}"
        try:
            table = client.get_table(table_ref)
            existing_cols = {f.name for f in table.schema}
            new_fields = []

            if "backtest_name" not in existing_cols:
                new_fields.append(bigquery.SchemaField(
                    "backtest_name", "STRING", mode="NULLABLE",
                    description="Human-readable name assigned to the backtest (e.g. BT_4EVC_V1_20251127_210419)."
                ))

            if "_ingested_at" not in existing_cols:
                new_fields.append(bigquery.SchemaField(
                    "_ingested_at", "TIMESTAMP", mode="NULLABLE",
                    default_value_expression="CURRENT_TIMESTAMP()",
                    description="UTC timestamp tracking when the row was ingested into BigQuery."
                ))

            if new_fields:
                table.schema = list(table.schema) + new_fields
                client.update_table(table, ["schema"])
                print(f"[ALTER SUCCESS] Added {[f.name for f in new_fields]} to `{table_name}`.")
            else:
                print(f"[SCHEMA OK] `{table_name}` already contains target columns.")
        except Exception as e:
            print(f"[ERROR] Altering `{table_name}`: {e}")

    # 2. Step 2: Retro-fill backtest_name from BTOPResults
    print("\n--- Retro-filling `backtest_name` across all historical rows ---")
    for table_name, fk_col in TABLE_FK_MAP.items():
        table_ref = f"`{dataset_ref}.{table_name}`"
        results_ref = f"`{dataset_ref}.BTOPResults`"

        update_sql = f"""
        UPDATE {table_ref} t
        SET t.backtest_name = r.name
        FROM {results_ref} r
        WHERE t.{fk_col} = r.backtestId
          AND (t.backtest_name IS NULL OR t.backtest_name = '');
        """
        try:
            job = client.query(update_sql)
            job.result()
            print(f"[UPDATE SUCCESS] Retro-filled `backtest_name` for table `{table_name}`.")
        except Exception as e:
            print(f"[UPDATE NOTICE] Retro-filling `backtest_name` for `{table_name}`: {e}")

    # 3. Step 3: Retro-fill _ingested_at = CURRENT_TIMESTAMP() for existing NULL rows
    print("\n--- Setting default `_ingested_at` for historical rows ---")
    for table_name, fk_col in TABLE_FK_MAP.items():
        table_ref = f"`{dataset_ref}.{table_name}`"
        ts_sql = f"""
        UPDATE {table_ref}
        SET _ingested_at = CURRENT_TIMESTAMP()
        WHERE _ingested_at IS NULL;
        """
        try:
            job = client.query(ts_sql)
            job.result()
            print(f"[TIMESTAMP SUCCESS] Updated `_ingested_at` for table `{table_name}`.")
        except Exception as e:
            print(f"[TIMESTAMP NOTICE] Updating `_ingested_at` for `{table_name}`: {e}")

    print("\n[SUCCESS] Standardized backtest_name and _ingested_at across all BigQuery tables!")


if __name__ == "__main__":
    alter_and_fill_tables()
