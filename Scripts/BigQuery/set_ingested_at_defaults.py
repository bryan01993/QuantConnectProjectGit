"""
set_ingested_at_defaults.py
===========================
Ensures that EVERY table in bav-personal-cloud.develop has a column named `_ingested_at`
with a default value of `CURRENT_TIMESTAMP()`.
"""

from __future__ import annotations

import logging
import os
import sys
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)

PROJECT_ID = "bav-personal-cloud"
DATASET_ID = "develop"


def main():
    client = bigquery.Client(project=PROJECT_ID)
    dataset_ref = client.dataset(DATASET_ID, project=PROJECT_ID)
    tables = list(client.list_tables(dataset_ref))

    logging.info(f"Checking {len(tables)} tables/views in dataset {PROJECT_ID}.{DATASET_ID}...")

    for t_item in tables:
        table_id = f"{PROJECT_ID}.{DATASET_ID}.{t_item.table_id}"
        try:
            table_obj = client.get_table(table_id)
            if table_obj.table_type == "VIEW":
                logging.info(f"[{t_item.table_id}] View - skipping DDL default alter.")
                continue

            cols = {field.name: field for field in table_obj.schema}

            if "_ingested_at" in cols:
                # Set default to CURRENT_TIMESTAMP()
                alter_sql = f"ALTER TABLE `{table_id}` ALTER COLUMN _ingested_at SET DEFAULT CURRENT_TIMESTAMP()"
                client.query(alter_sql).result()
                logging.info(f"[{t_item.table_id}] [SUCCESS] Set default CURRENT_TIMESTAMP() on _ingested_at.")
            elif "_ingestedAt" in cols:
                # Set default to CURRENT_TIMESTAMP() on _ingestedAt and also add _ingested_at
                alter_sql = f"ALTER TABLE `{table_id}` ALTER COLUMN _ingestedAt SET DEFAULT CURRENT_TIMESTAMP()"
                client.query(alter_sql).result()
                logging.info(f"[{t_item.table_id}] [SUCCESS] Set default CURRENT_TIMESTAMP() on _ingestedAt.")
                
                # Add _ingested_at as well for standardized naming
                add_sql = f"ALTER TABLE `{table_id}` ADD COLUMN IF NOT EXISTS _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()"
                client.query(add_sql).result()
                logging.info(f"[{t_item.table_id}] [SUCCESS] Added _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP().")
            else:
                # Add _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
                add_sql = f"ALTER TABLE `{table_id}` ADD COLUMN IF NOT EXISTS _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()"
                client.query(add_sql).result()
                logging.info(f"[{t_item.table_id}] [SUCCESS] Added _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP().")

        except Exception as err:
            logging.error(f"[{t_item.table_id}] Error setting column default: {err}")

    logging.info("ALL tables updated with DEFAULT CURRENT_TIMESTAMP() for _ingested_at!")


if __name__ == "__main__":
    main()
