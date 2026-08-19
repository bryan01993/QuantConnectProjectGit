"""
batch_manager.py
================
Manages BigQuery table `BTOPBatchChunks` for tracking multi-period, chunked
QuantConnect backtests (e.g. 2015..2021) and their serverless ingestion state.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
from typing import Any, Dict, List, Optional
from google.cloud import bigquery

# Ensure current BigQuery directory is in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client  # noqa: E402

PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"
BATCH_TABLE_NAME: str = "BTOPBatchChunks"

BATCH_SCHEMA = [
    bigquery.SchemaField(
        "batch_id", "STRING", mode="REQUIRED",
        description="Unique Primary Key identifier for the multi-period batch execution (e.g., BATCH_4EVC_V1_2015_2021)."
    ),
    bigquery.SchemaField(
        "backtest_id", "STRING", mode="REQUIRED",
        description="Foreign Key identifying the specific QuantConnect Cloud backtest run ID for this chunk."
    ),
    bigquery.SchemaField(
        "algo_code", "STRING", mode="REQUIRED",
        description="Short code identifying the strategy algorithm (e.g., 4EVC, 0AT)."
    ),
    bigquery.SchemaField(
        "chunk_index", "INTEGER", mode="REQUIRED",
        description="Sequential index of the date chunk within the batch run (1..N)."
    ),
    bigquery.SchemaField(
        "start_date", "DATE", mode="NULLABLE",
        description="Start date boundary for this backtest chunk."
    ),
    bigquery.SchemaField(
        "end_date", "DATE", mode="NULLABLE",
        description="End date boundary for this backtest chunk."
    ),
    bigquery.SchemaField(
        "status", "STRING", mode="REQUIRED",
        description="Status of chunk execution and ingestion: PENDING, RUNNING, COMPLETED, FAILED."
    ),
    bigquery.SchemaField(
        "compile_id", "STRING", mode="NULLABLE",
        description="QuantConnect Cloud compile ID associated with the batch run."
    ),
    bigquery.SchemaField(
        "created_at", "TIMESTAMP", mode="REQUIRED",
        description="UTC timestamp when the chunk was queued."
    ),
    bigquery.SchemaField(
        "updated_at", "TIMESTAMP", mode="NULLABLE",
        description="UTC timestamp when chunk status was last updated."
    ),
]


def ensure_batch_table_exists(client: bigquery.Client, project_id: str = PROJECT_ID, dataset_id: str = DATASET_ID) -> None:
    table_id = f"{project_id}.{dataset_id}.{BATCH_TABLE_NAME}"
    try:
        client.get_table(table_id)
    except Exception:
        print(f"Table {BATCH_TABLE_NAME} does not exist. Creating...")
        table = bigquery.Table(table_id, schema=BATCH_SCHEMA)
        client.create_table(table)
        print(f"Created table {table_id}.")
        import time
        time.sleep(3)


def register_batch_chunks(
    client: bigquery.Client,
    batch_id: str,
    algo_code: str,
    chunks: List[Dict[str, Any]],
    project_id: str = PROJECT_ID,
    dataset_id: str = DATASET_ID,
) -> None:
    ensure_batch_table_exists(client, project_id, dataset_id)
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()

    rows = []
        start_yr = str(c.get("start_date", ""))[:4]
        default_name = f"{batch_id}_Y{start_yr}" if start_yr else batch_id
        rows.append({
            "batch_id": batch_id,
            "backtest_id": c["backtest_id"],
            "algo_code": algo_code,
            "chunk_index": int(c["chunk_index"]),
            "start_date": c.get("start_date"),
            "end_date": c.get("end_date"),
            "status": c.get("status", "PENDING"),
            "compile_id": c.get("compile_id"),
            "backtest_name": c.get("backtest_name") or default_name,
            "created_at": now_ts,
            "updated_at": now_ts,
        })

    table_id = f"{project_id}.{dataset_id}.{BATCH_TABLE_NAME}"
    job_config = bigquery.LoadJobConfig(
        schema=BATCH_SCHEMA,
        write_disposition="WRITE_APPEND"
    )
    try:
        load_job = client.load_table_from_json(rows, table_id, job_config=job_config)
        load_job.result()
        print(f"[Batch Manager] Registered {len(rows)} chunks for batch '{batch_id}' via batch load job.")
    except Exception as err:
        print(f"[Batch Manager] Error registering chunks via batch load: {err}")


def get_pending_batch_chunks(
    client: bigquery.Client,
    project_id: str = PROJECT_ID,
    dataset_id: str = DATASET_ID,
) -> List[Dict[str, Any]]:
    """Returns the latest state of batch chunks that are PENDING or RUNNING."""
    ensure_batch_table_exists(client, project_id, dataset_id)
    query = f"""
    WITH latest_chunks AS (
        SELECT
            batch_id,
            backtest_id,
            algo_code,
            chunk_index,
            CAST(start_date AS STRING) as start_date,
            CAST(end_date AS STRING) as end_date,
            status,
            compile_id,
            created_at,
            updated_at,
            ROW_NUMBER() OVER (PARTITION BY batch_id, chunk_index ORDER BY updated_at DESC, created_at DESC) as rn
        FROM `{project_id}.{dataset_id}.{BATCH_TABLE_NAME}`
    )
    SELECT batch_id, backtest_id, algo_code, chunk_index, start_date, end_date, status, compile_id
    FROM latest_chunks
    WHERE rn = 1 AND status IN ('PENDING', 'RUNNING')
    ORDER BY created_at ASC, chunk_index ASC
    """

    results = client.query(query).result()
    return [dict(r) for r in results]


def update_chunk_status(
    client: bigquery.Client,
    batch_id: str,
    backtest_id: str,
    new_status: str,
    new_backtest_id: Optional[str] = None,
    project_id: str = PROJECT_ID,
    dataset_id: str = DATASET_ID,
) -> None:
    now_ts = dt.datetime.now(dt.timezone.utc).isoformat()
    target_bt_id = new_backtest_id or backtest_id

    query = f"""
    UPDATE `{project_id}.{dataset_id}.{BATCH_TABLE_NAME}`
    SET status = @new_status, backtest_id = @target_bt_id, updated_at = @now_ts
    WHERE batch_id = @batch_id AND (backtest_id = @backtest_id OR backtest_id = @target_bt_id)
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("new_status", "STRING", new_status),
            bigquery.ScalarQueryParameter("target_bt_id", "STRING", target_bt_id),
            bigquery.ScalarQueryParameter("now_ts", "TIMESTAMP", now_ts),
            bigquery.ScalarQueryParameter("batch_id", "STRING", batch_id),
            bigquery.ScalarQueryParameter("backtest_id", "STRING", backtest_id),
        ]
    )
    try:
        client.query(query, job_config=job_config).result()
        print(f"[Batch Manager] Updated chunk ({batch_id}, {target_bt_id}) -> {new_status}")
    except Exception as err:
        if "streaming buffer" in str(err).lower():
            print(f"[Batch Manager] Streaming buffer active for ({batch_id}, {target_bt_id}). Inserting updated status row via batch load...")
            row_query = f"""
            SELECT algo_code, chunk_index, start_date, end_date, compile_id, created_at
            FROM `{project_id}.{dataset_id}.{BATCH_TABLE_NAME}`
            WHERE batch_id = '{batch_id}' AND (backtest_id = '{backtest_id}' OR backtest_id = '{target_bt_id}')
            LIMIT 1
            """
            res = list(client.query(row_query).result())
            if res:
                r = dict(res[0])
                new_row = [{
                    "batch_id": batch_id,
                    "backtest_id": target_bt_id,
                    "algo_code": r["algo_code"],
                    "chunk_index": int(r["chunk_index"]),
                    "start_date": str(r["start_date"]),
                    "end_date": str(r["end_date"]),
                    "status": new_status,
                    "compile_id": r.get("compile_id"),
                    "created_at": str(r["created_at"]),
                    "updated_at": now_ts,
                }]
                table_ref = f"{project_id}.{dataset_id}.{BATCH_TABLE_NAME}"
                load_cfg = bigquery.LoadJobConfig(schema=BATCH_SCHEMA, write_disposition="WRITE_APPEND")
                client.load_table_from_json(new_row, table_ref, job_config=load_cfg).result()
                print(f"[Batch Manager] [FALLBACK SUCCESS] Streamed status update via batch load: {new_status}")
        else:
            print(f"[Batch Manager] Error updating chunk status: {err}")


if __name__ == "__main__":
    bq_client = get_bigquery_client()
    ensure_batch_table_exists(bq_client)
