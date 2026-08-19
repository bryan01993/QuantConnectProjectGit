import os
import sys
import logging
import subprocess
from typing import List, Dict, Any

from db_operator import get_bigquery_client
import bt_handler
import log_trades_uploader

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SyncMissingTrades")

PROJECT_ID = "bav-personal-cloud"
DATASET_ID = "develop"


def get_backtests_missing_trades(client) -> List[Dict[str, Any]]:
    """Queries BigQuery for backtests in BTOPResults that have 0 trade records in BTOPTrades."""
    query = f"""
    SELECT r.backtestId, r.name, r.projectId 
    FROM `{PROJECT_ID}.{DATASET_ID}.BTOPResults` r
    LEFT JOIN `{PROJECT_ID}.{DATASET_ID}.BTOPTrades` t 
      ON r.backtestId = t.backtestId
    GROUP BY r.backtestId, r.name, r.projectId
    HAVING COUNT(t.pk) = 0
    ORDER BY r.backtestId
    """
    logger.info("Querying BigQuery for backtests missing trade records in BTOPTrades...")
    query_job = client.query(query)
    results = list(query_job.result())
    return [dict(row) for row in results]


def sync_missing_trades():
    """Identifies and backfills missing trade records for all backtests in BigQuery."""
    client = get_bigquery_client()
    missing_backtests = get_backtests_missing_trades(client)
    
    total_missing = len(missing_backtests)
    logger.info(f"Found {total_missing} backtests in BTOPResults missing trade records in BTOPTrades.")
    
    if total_missing == 0:
        logger.info("SUCCESS: All backtests in BigQuery already have trade records. Zero action needed!")
        return

    api_key, user_id = bt_handler.get_api_key()
    api_token = bt_handler.generate_api_token(api_key, user_id)
    
    processed = 0
    for idx, bt in enumerate(missing_backtests, 1):
        bt_id = bt["backtestId"]
        bt_name = bt.get("name", "UNKNOWN")
        proj_id = bt.get("projectId") or 22447448
        
        logger.info(f"[{idx}/{total_missing}] Processing missing trades for Backtest ID: {bt_id} (Name: {bt_name})...")
        
        # 1. Download orders & logs if not existing locally
        orders_path, orders = bt_handler.download_backtest_orders(
            backtest_id=bt_id,
            api_token=api_token,
            project_id=proj_id,
            chunk=100
        )
        logs_path = bt_handler.download_backtest_logs(
            backtest_id=bt_id,
            api_token=api_token,
            project_id=proj_id
        )
        
        # 2. Invoke log_trades_uploader.py for this backtest ID
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            uploader_script = os.path.join(script_dir, "log_trades_uploader.py")
            cmd = f'"{sys.executable}" "{uploader_script}" "{bt_id}"'
            subprocess.run(cmd, shell=True, check=True)
            processed += 1
        except Exception as e:
            logger.error(f"Failed to process trade uploader for {bt_id}: {e}")

    logger.info("=" * 70)
    logger.info(f"SYNCHRONIZATION COMPLETE: Processed {processed}/{total_missing} backtests.")
    logger.info("=" * 70)


if __name__ == "__main__":
    sync_missing_trades()
