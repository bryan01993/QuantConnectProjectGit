import argparse
import base64
import hashlib
import json
import os
import time
import requests
import yaml
from typing import Dict, Any, Optional
from google.cloud import bigquery
from google.oauth2 import service_account


def load_user_config() -> Dict[str, Any]:
    """Load defaults from Resources/UserConfig.yaml."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(script_dir, "..", "..", "Resources", "UserConfig.yaml"))
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as file:
                config = yaml.safe_load(file) or {}
                return config.get("defaults", {})
        except Exception as e:
            print(f"Warning: Failed to load UserConfig.yaml: {e}")
    return {}


def generate_api_token(api_key: str, user_id: str) -> Dict[str, str]:
    """Create encoded token for QuantConnect API."""
    timestamp = str(int(time.time()))
    time_stamped_token = f"{api_key}:{timestamp}"
    hashed_token = hashlib.sha256(time_stamped_token.encode("utf-8")).hexdigest()
    authentication = f"{user_id}:{hashed_token}"
    api_token = base64.b64encode(authentication.encode("utf-8")).decode("ascii")
    return {"api_token": api_token, "timestamp": timestamp}


from db_operator import get_bigquery_client


def list_backtests(api_token: Dict[str, str], project_id: int):
    """Fetches a list of all backtests from QuantConnect for a specific project."""
    url = "https://www.quantconnect.com/api/v2/backtests/list"
    headers = {
        "Authorization": f"Basic {api_token['api_token']}",
        "Timestamp": api_token["timestamp"],
    }
    payload = {
        "projectId": int(project_id),
        "includeStatistics": True
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("backtests", [])
    else:
        raise Exception(f"Failed to fetch backtests: {response.status_code} {response.text}")


def download_backtest(backtest_id: str, api_token: Dict[str, str], project_id: int, download_folder: str):
    """Downloads a backtest JSON file by its ID using the official read endpoint."""
    url = "https://www.quantconnect.com/api/v2/backtests/read"
    headers = {
        "Authorization": f"Basic {api_token['api_token']}",
        "Timestamp": api_token["timestamp"],
    }
    payload = {
        "projectId": project_id,
        "backtestId": backtest_id
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        file_path = os.path.join(download_folder, f"{backtest_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(response.json(), f, indent=4, ensure_ascii=False)
        return file_path
    else:
        raise Exception(f"Failed to download backtest {backtest_id}: {response.status_code} {response.text}")


def check_backtest_in_bigquery(
    client: bigquery.Client,
    backtest_id: str,
    bq_project: str,
    bq_dataset: str,
    bq_table: str,
    bq_column: str
) -> bool:
    """Checks if a backtest ID already exists in BigQuery."""
    query = f"""
        SELECT COUNT(1) as count
        FROM `{bq_project}.{bq_dataset}.{bq_table}`
        WHERE {bq_column} = @backtest_id
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("backtest_id", "STRING", backtest_id)]
    )
    query_job = client.query(query, job_config=job_config)
    results = query_job.result()
    return next(results).count > 0


def parse_args():
    parser = argparse.ArgumentParser(description="Synchronize QuantConnect backtest files with BigQuery.")
    parser.add_argument(
        "--project-id",
        type=int,
        help="QuantConnect Project ID. Defaults to env QC_PROJECT_ID or PROJECT_ID in Resources/UserConfig.yaml.",
    )
    parser.add_argument(
        "--bq-project",
        type=str,
        default=os.getenv("BIGQUERY_PROJECT", "bav-personal-cloud"),
        help="BigQuery Project ID.",
    )
    parser.add_argument(
        "--bq-dataset",
        type=str,
        default=os.getenv("BIGQUERY_DATASET", "develop"),
        help="BigQuery Dataset ID.",
    )
    parser.add_argument(
        "--bq-table",
        type=str,
        default=os.getenv("BIGQUERY_TABLE", "BTOPResults"),
        help="BigQuery table to check (default: 'BTOPResults').",
    )
    parser.add_argument(
        "--bq-column",
        type=str,
        default=os.getenv("BIGQUERY_COLUMN", "backtestId"),
        help="BigQuery column to check (default: 'backtestId').",
    )
    parser.add_argument(
        "--download-folder",
        type=str,
        default="backtests",
        help="Folder where downloaded backtests will be saved.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    # Load configuration from UserConfig.yaml
    defaults = load_user_config()
    
    # Resolve QC API credentials
    api_key = os.getenv("QUANTCONNECT_API_TOKEN") or defaults.get("LOGIN_API_KEY")
    user_id = os.getenv("QUANTCONNECT_USER_ID") or str(defaults.get("USER_ID") or "")
    
    # Resolve QC Project ID
    project_id = args.project_id
    if not project_id:
        env_pid = os.getenv("QC_PROJECT_ID")
        project_id = int(env_pid) if env_pid else defaults.get("PROJECT_ID")
        
    if not api_key or not user_id or not project_id:
        raise ValueError(
            "Missing QuantConnect credentials or Project ID. "
            "Please ensure they are defined in environment variables or Resources/UserConfig.yaml."
        )

    # Resolve download folder relative to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    download_folder = os.path.abspath(os.path.join(script_dir, "..", args.download_folder))
    os.makedirs(download_folder, exist_ok=True)

    # Initialize BigQuery client
    bq_client = get_bigquery_client(args.bq_project)

    # Generate QC API token
    api_token = generate_api_token(api_key, user_id)

    # Fetch all backtests
    print(f"Fetching backtests for project {project_id}...")
    backtests = list_backtests(api_token, project_id)
    print(f"Found {len(backtests)} backtests.")

    for backtest in backtests:
        backtest_id = backtest.get("id")
        if not backtest_id:
            print("Skipping backtest with missing ID.")
            continue

        # Check if the backtest already exists in BigQuery
        try:
            exists = check_backtest_in_bigquery(
                bq_client,
                backtest_id,
                args.bq_project,
                args.bq_dataset,
                args.bq_table,
                args.bq_column
            )
            if exists:
                print(f"Backtest {backtest_id} already exists in BigQuery. Skipping download.")
                continue
        except Exception as e:
            print(f"Error checking BigQuery for backtest {backtest_id}: {e}. Proceeding to download.")

        # Download the backtest
        try:
            file_path = download_backtest(backtest_id, api_token, project_id, download_folder)
            print(f"Downloaded backtest {backtest_id} to {file_path}.")
        except Exception as e:
            print(f"Error downloading backtest {backtest_id}: {e}")


if __name__ == "__main__":
    main()
