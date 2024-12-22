import os
import requests
from google.cloud import bigquery

# Configuration
QUANTCONNECT_API_URL = "https://www.quantconnect.com/api/v2/backtests/list"
QUANTCONNECT_API_TOKEN = os.getenv("QUANTCONNECT_API_TOKEN")
QUANTCONNECT_PROJECT_ID = 20428472
BIGQUERY_PROJECT = os.getenv("BIGQUERY_PROJECT")
BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")
BIGQUERY_TABLE = "backtests"
DOWNLOAD_FOLDER = "backtests"

# Ensure the download folder exists
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def list_backtests():
    """Fetches a list of all backtests from QuantConnect for a specific project."""
    headers = {"Authorization": f"Bearer {QUANTCONNECT_API_TOKEN}"}
    payload = {
        "projectId": int(QUANTCONNECT_PROJECT_ID),
        "includeStatistics": True
    }
    response = requests.post(QUANTCONNECT_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("backtests", [])
    else:
        raise Exception(f"Failed to fetch backtests: {response.status_code} {response.text}")

def download_backtest(backtest_id):
    """Downloads a backtest JSON file by its ID."""
    headers = {"Authorization": f"Bearer {QUANTCONNECT_API_TOKEN}"}
    url = f"https://www.quantconnect.com/api/v2/backtests/{backtest_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_path = os.path.join(DOWNLOAD_FOLDER, f"{backtest_id}.json")
        with open(file_path, "w") as f:
            f.write(response.text)
        return file_path
    else:
        raise Exception(f"Failed to download backtest {backtest_id}: {response.status_code} {response.text}")

def check_backtest_in_bigquery(client, backtest_id):
    """Checks if a backtest ID already exists in BigQuery."""
    query = f"""
        SELECT COUNT(1) as count
        FROM `{BIGQUERY_PROJECT}.{BIGQUERY_DATASET}.{BIGQUERY_TABLE}`
        WHERE backtest_id = @backtest_id
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("backtest_id", "STRING", backtest_id)]
    )
    query_job = client.query(query, job_config=job_config)
    results = query_job.result()
    return next(results).count > 0

def main():
    """Main synchronization function."""
    client = bigquery.Client(project=BIGQUERY_PROJECT)

    # Fetch all backtests
    backtests = list_backtests()
    print(f"Found {len(backtests)} backtests.")

    for backtest in backtests:
        backtest_id = backtest.get("id")
        if not backtest_id:
            print("Skipping backtest with missing ID.")
            continue

        # Check if the backtest already exists in BigQuery
        if check_backtest_in_bigquery(client, backtest_id):
            print(f"Backtest {backtest_id} already exists in BigQuery. Skipping download.")
            continue

        # Download the backtest
        try:
            file_path = download_backtest(backtest_id)
            print(f"Downloaded backtest {backtest_id} to {file_path}.")
        except Exception as e:
            print(f"Error downloading backtest {backtest_id}: {e}")

if __name__ == "__main__":
    main()
