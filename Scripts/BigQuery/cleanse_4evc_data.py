"""
cleanse_4evc_data.py
===================
Executes data cleanse deleting all 4EVC backtest data created prior to 2026-07-26 00:00:00 UTC
across all BigQuery tables in dataset `develop` and local storage directories.

Preserves:
- All 4EVC backtests created on or after 2026-07-26 00:00:00 UTC.
- All non-4EVC strategy backtests.
"""

from __future__ import annotations

import sys
import os
import glob
from datetime import datetime, timezone
from typing import List, Set, Tuple

# Ensure BigQuery script directory is in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from db_operator import get_bigquery_client
from google.cloud import bigquery


def run_cleanse() -> None:
    client = get_bigquery_client()
    cutoff_date = datetime(2026, 7, 26, 0, 0, 0, tzinfo=timezone.utc)

    print("==========================================================================")
    print("STEP 1: Identifying 4EVC Backtests Created Before 2026-07-26 00:00:00 UTC")
    print("==========================================================================")

    q_results = """
        SELECT backtestId, name, note, created
        FROM `develop.BTOPResults`
    """
    all_results = list(client.query(q_results).result())

    to_delete_bt_ids: Set[str] = set()
    to_keep_4evc_ids: Set[str] = set()
    non_4evc_ids: Set[str] = set()

    for r in all_results:
        bt_id = r.backtestId
        name = r.name or ""
        note = r.note or ""
        created = r.created

        is_4evc = ("4EVC" in name) or ("4EVC" in note)
        if is_4evc:
            if created < cutoff_date:
                to_delete_bt_ids.add(bt_id)
            else:
                to_keep_4evc_ids.add(bt_id)
        else:
            non_4evc_ids.add(bt_id)

    print(f"Targeting {len(to_delete_bt_ids)} 4EVC backtests created before 2026-07-26 for deletion.")
    print(f"Preserving {len(to_keep_4evc_ids)} 4EVC backtests created on/after 2026-07-26.")
    print(f"Preserving {len(non_4evc_ids)} NON-4EVC backtests.")

    if not to_delete_bt_ids:
        print("No backtests found matching deletion criteria. Exiting.")
        return

    del_ids_list = sorted(list(to_delete_bt_ids))

    print("\n==========================================================================")
    print("STEP 2: Deleting BigQuery Records Across Dataset `develop`")
    print("==========================================================================")

    bq_tables: List[Tuple[str, str]] = [
        ("BTOPResults", "backtestId"),
        ("BTOPOrders", "backtestId"),
        ("BTOPTrades", "backtestId"),
        ("BTOPCharts", "backtestId"),
        ("BTOPParameterSet", "backtestId"),
        ("BTOPResearchGuide", "backtestId"),
        ("BTOPRollingWindowPortfolioStats", "backtestId"),
        ("BTOPRollingWindowTradeStats", "backtestId"),
        ("BTOPRollingWindowClosedTrades", "backtestId"),
        ("BTOPRuntimeStatistics", "backtestId"),
        ("BTOPStatistics", "backtestId"),
        ("BTOPTotalPerformanceClosedTrades", "backtestId"),
        ("BTOPTotalPerformancePortfolioStats", "backtestId"),
        ("BTOPTotalPerformanceTradeStats", "backtestId"),
        ("BTOPBatchChunks", "backtest_id"),
        ("BTOPErrors", "backtestId")
    ]

    for table_name, key_col in bq_tables:
        delete_query = f"""
            DELETE FROM `develop.{table_name}`
            WHERE {key_col} IN UNNEST(@del_ids)
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("del_ids", "STRING", del_ids_list)
            ]
        )
        try:
            job = client.query(delete_query, job_config=job_config)
            job.result()  # Wait for job completion
            print(f"Successfully executed DELETE on develop.{table_name:35s} | Affected rows: {job.num_dml_affected_rows}")
        except Exception as e:
            print(f"Error executing DELETE on develop.{table_name}: {e}")

    print("\n==========================================================================")
    print("STEP 3: Cleaning Local Files")
    print("==========================================================================")

    scripts_dir = os.path.abspath(os.path.join(_THIS_DIR, ".."))
    local_dirs = [
        os.path.join(scripts_dir, "backtest_results"),
        os.path.join(scripts_dir, "orders_results"),
        os.path.join(scripts_dir, "already_uploaded_backtest_results"),
        os.path.join(scripts_dir, "already_uploaded_orders_results"),
        os.path.join(scripts_dir, "backtest_logs"),
        os.path.join(scripts_dir, "backtests"),
    ]

    total_deleted_files = 0
    for target_dir in local_dirs:
        if not os.path.exists(target_dir):
            continue
        folder_deleted = 0
        for fname in os.listdir(target_dir):
            fpath = os.path.join(target_dir, fname)
            if os.path.isfile(fpath):
                # Check if any target backtest ID is in the filename
                if any(bt_id in fname for bt_id in del_ids_list):
                    try:
                        os.remove(fpath)
                        folder_deleted += 1
                    except Exception as err:
                        print(f"Failed to remove local file {fpath}: {err}")
        print(f"Directory {os.path.basename(target_dir):35s}: Removed {folder_deleted} matching files")
        total_deleted_files += folder_deleted

    print(f"\nTotal local files removed: {total_deleted_files}")

    print("\n==========================================================================")
    print("STEP 4: Verification & Final Audit")
    print("==========================================================================")

    verification_failed = False
    for table_name, key_col in bq_tables:
        check_query = f"""
            SELECT COUNT(1) AS cnt
            FROM `develop.{table_name}`
            WHERE {key_col} IN UNNEST(@del_ids)
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("del_ids", "STRING", del_ids_list)
            ]
        )
        remaining_cnt = list(client.query(check_query, job_config=job_config).result())[0].cnt
        if remaining_cnt > 0:
            print(f"[FAIL] Table develop.{table_name} still has {remaining_cnt} deleted backtest rows!")
            verification_failed = True
        else:
            print(f"[PASS] Table develop.{table_name:35s}: 0 deleted backtest rows remaining.")

    # Check BTOPResults totals
    post_results = list(client.query(q_results).result())
    post_4evc_old = [r for r in post_results if ("4EVC" in (r.name or "") or "4EVC" in (r.note or "")) and r.created < cutoff_date]
    post_4evc_kept = [r for r in post_results if ("4EVC" in (r.name or "") or "4EVC" in (r.note or "")) and r.created >= cutoff_date]
    post_non_4evc = [r for r in post_results if not ("4EVC" in (r.name or "") or "4EVC" in (r.note or ""))]

    print(f"\nBTOPResults Post-Cleanse Audit:")
    print(f"  4EVC before 26/07/2026 remaining: {len(post_4evc_old)} (Expected: 0)")
    print(f"  4EVC on/after 26/07/2026 remaining: {len(post_4evc_kept)} (Expected: {len(to_keep_4evc_ids)})")
    print(f"  Non-4EVC backtests remaining:       {len(post_non_4evc)} (Expected: {len(non_4evc_ids)})")

    if len(post_4evc_old) == 0 and len(post_4evc_kept) == len(to_keep_4evc_ids) and not verification_failed:
        print("\n>>> DATA CLEANSE SUCCESSFULLY VERIFIED AND COMPLETE! <<<")
    else:
        print("\n>>> VERIFICATION FAILED! Please review audit logs above. <<<")


if __name__ == "__main__":
    run_cleanse()
