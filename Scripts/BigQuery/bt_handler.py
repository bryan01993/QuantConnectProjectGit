import argparse
import base64
import hashlib
import json
import logging
import os
import subprocess
import time
import sys
from pathlib import Path
from typing import Dict, Tuple, Optional, List, Any

import requests
import yaml

logging.basicConfig(level=logging.DEBUG)


def main():
    """Coordinate download of backtest results and database persistence."""
    args = parse_arguments()
    backtest_id = args.backtest_id

    api_key, user_id = get_api_key()
    project_id = get_project_id(args)

    api_token = generate_api_token(api_key, user_id)

    # Resolve human-readable backtest name (e.g. BT_4EVC_...) to 32-character hex ID if needed
    real_backtest_id = resolve_backtest_id(backtest_id, api_token, project_id)

    results_path, response_data = download_backtest_results(
        backtest_id=real_backtest_id,
        api_token=api_token,
        project_id=project_id
    )

    orders_path, orders = download_backtest_orders(
        backtest_id=real_backtest_id,
        api_token=api_token,
        project_id=project_id,
        chunk=100
    )
    if orders_path:
        logging.info(f"Orders saved to: {orders_path} (count={len(orders)})")
        try:
            from db_operator import get_bigquery_client, load_orders
            client = get_bigquery_client()
            load_orders({"orders": orders}, client, "develop", real_backtest_id)
            logging.info(f"Successfully ingested {len(orders)} orders into BTOPOrders for backtest ID: {real_backtest_id}")
        except Exception as e:
            logging.error(f"Failed to ingest BTOPOrders for {real_backtest_id}: {e}")

    if results_path:
        inspect_api_response(response_data)
        write_results_to_database(results_path, real_backtest_id)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=("Backtest Handler for Downloading Results and Storing in Database")
    )
    parser.add_argument(
        "backtest_id",
        type=str,
        nargs="?",
        default="b7b782f844c4459e5090b5b5144c2183",
        help="ID of the backtest to handle",
    )
    parser.add_argument(
        "--project-id",
        type=int,
        default=None,
        help="QuantConnect Project ID (overrides config/env if provided)",
    )
    return parser.parse_args()


def _resolve_config_path() -> str:
    """Internal helper: absolute path to Resources/UserConfig.yaml."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(script_dir, "..", "..", "Resources", "UserConfig.yaml"))


def get_api_key() -> Tuple[str, str]:
    try:
        config_path = _resolve_config_path()
        with open(config_path, "r") as file:
            config = yaml.safe_load(file) or {}
            defaults = config.get("defaults", {})
            api_key = defaults.get("LOGIN_API_KEY")
            user_id = defaults.get("USER_ID")
            if not api_key or not user_id:
                raise ValueError("API key or User ID not found in configuration file.")
            logging.info("API key and User ID successfully retrieved.")
            return api_key, str(user_id)
    except Exception as e:
        logging.error(f"Failed to retrieve API key: {e}")
        raise


def get_project_id(args) -> int:
    if getattr(args, "project_id", None):
        logging.info(f"Using Project ID from CLI: {args.project_id}")
        return int(args.project_id)

    env_pid = os.getenv("QC_PROJECT_ID")
    if env_pid:
        logging.info(f"Using Project ID from env QC_PROJECT_ID: {env_pid}")
        return int(env_pid)

    try:
        config_path = _resolve_config_path()
        with open(config_path, "r") as file:
            config = yaml.safe_load(file) or {}
            defaults = config.get("defaults", {})
            pid = defaults.get("PROJECT_ID")
            if pid is None:
                raise ValueError("PROJECT_ID missing in YAML defaults.")
            logging.info(f"Using Project ID from YAML: {pid}")
            return int(pid)
    except Exception as e:
        logging.error(f"Failed to resolve Project ID: {e}")
        raise


def generate_api_token(api_key: str, user_id: str) -> Dict[str, str]:
    try:
        timestamp = str(int(time.time()))
        time_stamped_token = f"{api_key}:{timestamp}"
        hashed_token = hashlib.sha256(time_stamped_token.encode("utf-8")).hexdigest()
        authentication = f"{user_id}:{hashed_token}"
        api_token = base64.b64encode(authentication.encode("utf-8")).decode("ascii")
        logging.debug(f"Generated token hash: {hashed_token[:6]}... (truncated)")
        logging.debug(f"Generated timestamp: {timestamp}")
        logging.info("API token successfully generated.")
        return {"api_token": api_token, "timestamp": timestamp}
    except Exception as e:
        logging.error(f"Failed to generate API token: {e}")
        raise


def _auth_headers(api_token: Dict[str, str]) -> Dict[str, str]:
    return {
        "Authorization": f"Basic {api_token['api_token']}",
        "Timestamp": api_token["timestamp"],
    }


def resolve_backtest_id(backtest_id_or_name: str, api_token: Dict[str, str], project_id: int) -> str:
    """
    Resolves a backtest ID or human-readable backtest name to a real 32-character hex ID.
    If backtest_id_or_name is already a 32-char hex ID, returns it directly.
    Otherwise queries QC API /api/v2/backtests/list to resolve.
    """
    if len(backtest_id_or_name) == 32 and all(c in "0123456789abcdefABCDEF" for c in backtest_id_or_name):
        return backtest_id_or_name

    logging.info(f"Resolving human-readable backtest name '{backtest_id_or_name}' to real hex backtest ID...")
    url_list = "https://www.quantconnect.com/api/v2/backtests/list"
    headers = _auth_headers(api_token)
    try:
        resp = requests.post(url_list, headers=headers, json={"projectId": project_id}, timeout=30)
        if resp.status_code == 200:
            for bt in resp.json().get("backtests", []):
                hex_id = bt.get("backtestId") or bt.get("id")
                name_str = bt.get("name")
                if name_str == backtest_id_or_name or hex_id == backtest_id_or_name:
                    logging.info(f"Resolved '{backtest_id_or_name}' -> hex ID: {hex_id}")
                    return str(hex_id)
    except Exception as e:
        logging.warning(f"Could not resolve backtest name '{backtest_id_or_name}' via QC API list: {e}")

    return backtest_id_or_name


def download_backtest_results(backtest_id: str, api_token: Dict[str, str], project_id: int) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.abspath(os.path.join(script_dir, "..", "backtest_results"))
        os.makedirs(results_dir, exist_ok=True)
        results_path = os.path.join(results_dir, f"{backtest_id}.json")

        api_url = "https://www.quantconnect.com/api/v2/backtests/read"
        headers = _auth_headers(api_token)

        logging.info(f"Fetching results for backtest ID: {backtest_id} from API.")
        payload = {"projectId": project_id, "backtestId": backtest_id}
        response = requests.post(api_url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        response_data = response.json()

        with open(results_path, "w", encoding="utf-8") as file:
            json.dump(response_data, file, indent=4, ensure_ascii=False)

        logging.info(f"Backtest results downloaded to: {results_path}")
        return results_path, response_data
    except requests.RequestException as e:
        logging.error(f"Failed to fetch backtest results for ID {backtest_id}: {e}")
        return None, None


def download_backtest_orders(
    backtest_id: str,
    api_token: Dict[str, str],
    project_id: int,
    chunk: int = 100
) -> Tuple[Optional[str], List[Dict[str, Any]]]:
    try:
        assert 1 <= chunk <= 100, "chunk must be within 1..100"

        script_dir = os.path.dirname(os.path.abspath(__file__))
        orders_dir = os.path.abspath(os.path.join(script_dir, "..", "orders_results"))
        os.makedirs(orders_dir, exist_ok=True)
        orders_path = os.path.join(orders_dir, f"{backtest_id}_orders.json")

        api_url = "https://www.quantconnect.com/api/v2/backtests/orders/read"
        api_key, user_id = get_api_key()
        all_orders: List[Dict[str, Any]] = []
        start = 0
        while True:
            max_retries = 15
            page = None
            for attempt in range(max_retries):
                try:
                    fresh_token = generate_api_token(api_key, user_id)
                    headers = _auth_headers(fresh_token)
                    payload = {
                        "start": start,
                        "end": start + chunk,
                        "projectId": project_id,
                        "backtestId": backtest_id,
                    }
                    r = requests.post(api_url, headers=headers, json=payload, timeout=60)
                    r.raise_for_status()
                    page = r.json()
                    if page.get("status") == "loading":
                        logging.info(f"QC Orders API status is 'loading' for backtest {backtest_id}. Waiting 3s... (attempt {attempt + 1}/{max_retries})")
                        time.sleep(3)
                        continue
                    break
                except Exception as req_err:
                    if attempt == max_retries - 1:
                        logging.error(f"QC Orders API request failed after {max_retries} attempts at start {start}: {req_err}")
                        raise
                    time.sleep(1.5 * (attempt + 1))

            if not page or not page.get("success", False):
                logging.warning(f"QC Orders API returned error at start {start}: {page.get('errors') if page else 'No response'}")
                break

            raw_orders = page.get("orders", {})
            length = int(page.get("length", 0)) if page.get("length") is not None else 0

            if isinstance(raw_orders, dict):
                batch = list(raw_orders.values())
            elif isinstance(raw_orders, list):
                batch = raw_orders
            else:
                batch = []

            if length == 0 or not batch:
                break

            all_orders.extend(batch)
            start += chunk

        with open(orders_path, "w", encoding="utf-8") as f:
            json.dump(all_orders, f, indent=4, ensure_ascii=False)

        logging.info(f"Downloaded {len(all_orders)} orders to: {orders_path}")
        return orders_path, all_orders

    except Exception as e:
        logging.error(f"Failed to fetch orders for backtest {backtest_id}: {e}")
        return None, []


def download_backtest_logs(backtest_id: str, api_token: Dict[str, str], project_id: int) -> Optional[str]:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        logs_dir = os.path.abspath(os.path.join(script_dir, "..", "backtest_logs"))
        os.makedirs(logs_dir, exist_ok=True)
        log_path = os.path.join(logs_dir, f"{backtest_id}_log.txt")

        api_url = "https://www.quantconnect.com/api/v2/backtests/read/log"
        headers = _auth_headers(api_token)

        start = 0
        chunk = 100
        all_logs: List[str] = []

        while True:
            payload = {
                "projectId": project_id,
                "backtestId": backtest_id,
                "start": start,
                "end": start + chunk,
                "query": "BIGQUERY_TRADE_RECORD"
            }
            r = requests.post(api_url, headers=headers, json=payload, timeout=60)
            r.raise_for_status()
            data = r.json()
            logs = data.get("logs", [])
            if not data.get("success") or not logs:
                break
            all_logs.extend(logs)
            start += chunk
            if len(logs) < chunk:
                break

        with open(log_path, "w", encoding="utf-8") as f:
            for l in all_logs:
                f.write(l + "\n")

        logging.info(f"Downloaded {len(all_logs)} log lines to: {log_path}")
        return log_path
    except Exception as e:
        logging.error(f"Failed to fetch logs for backtest {backtest_id}: {e}")
        return None


def inspect_api_response(response_data):
    try:
        if response_data:
            logging.info("Inspecting API response structure...")
            logging.info(json.dumps(response_data, indent=4))
        else:
            logging.warning("No response data to inspect.")
    except Exception as e:
        logging.error(f"Failed to inspect API response: {e}")


def write_results_to_database(results_path, backtest_id):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        database_writer_script = os.path.join(script_dir, "db_operator.py")
        trade_uploader_script = os.path.join(script_dir, "log_trades_uploader.py")
        
        db_write_command = (
            f'"{sys.executable}" "{database_writer_script}" '
            f'--results-path "{results_path}" --backtest-id {backtest_id}'
        )
        logging.info(f"Calling database writer script for backtest ID: {backtest_id}")
        subprocess.run(db_write_command, shell=True, check=True)
        logging.info(f"Results successfully written to database for backtest ID: {backtest_id}")

        # Automatically chain log_trades_uploader.py to stream detailed trade records into BTOPTrades
        trade_upload_command = f'"{sys.executable}" "{trade_uploader_script}" "{backtest_id}"'
        logging.info(f"Auto-chaining trade uploader script for backtest ID: {backtest_id}")
        subprocess.run(trade_upload_command, shell=True, check=True)
        logging.info(f"Trades successfully uploaded for backtest ID: {backtest_id}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to write results/trades to database for ID {backtest_id}: {e}")


if __name__ == "__main__":
    main()
