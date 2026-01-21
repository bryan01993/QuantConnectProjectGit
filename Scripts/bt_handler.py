import argparse
import base64
import hashlib
import json
import logging
import os
import subprocess
import time
from pathlib import Path
from typing import Dict, Tuple, Optional, List, Any

import requests
import yaml

logging.basicConfig(level=logging.DEBUG)


def main():
    """Coordinate download of backtest results and database persistence.

    Steps:
        1. Parse command-line arguments.
        2. Retrieve API credentials (+ project id).
        3. Generate an API token.
        4. Download backtest results JSON.
        5. Download ALL orders (with tags) → orders_results/<backtestId>_orders.json.
        6. Inspect and store results (existing flow).
    """
    args = parse_arguments()
    backtest_id = args.backtest_id

    api_key, user_id = get_api_key()
    project_id = get_project_id(args)

    api_token = generate_api_token(api_key, user_id)

    results_path, response_data = download_backtest_results(
        backtest_id=backtest_id,
        api_token=api_token,
        project_id=project_id
    )

    # NEW: always fetch & persist orders for this backtest
    orders_path, orders = download_backtest_orders(
        backtest_id=backtest_id,
        api_token=api_token,
        project_id=project_id,
        chunk=100
    )
    if orders_path:
        logging.info(f"Orders saved to: {orders_path} (count={len(orders)})")

    if results_path:
        inspect_api_response(response_data)
        write_results_to_database(results_path, backtest_id)


def parse_arguments():
    """Return command-line arguments for the script."""
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
    # Optional override if you prefer to pass it via CLI instead of YAML/env
    parser.add_argument(
        "--project-id",
        type=int,
        default=None,
        help="QuantConnect Project ID (overrides config/env if provided)",
    )
    return parser.parse_args()


def _resolve_config_path() -> str:
    """Internal helper: absolute path to Resources/UserConfig.yaml (relative to this file)."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "..", "Resources", "UserConfig.yaml")


def get_api_key() -> Tuple[str, str]:
    """Load API key and user ID from Resources/UserConfig.yaml.

    Returns:
        (api_key, user_id)
    """
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
    """Resolve QuantConnect Project ID from CLI → env → YAML (in that order)."""
    if getattr(args, "project_id", None):
        logging.info(f"Using Project ID from CLI: {args.project_id}")
        return int(args.project_id)

    env_pid = os.getenv("QC_PROJECT_ID")
    if env_pid:
        logging.info(f"Using Project ID from env QC_PROJECT_ID: {env_pid}")
        return int(env_pid)

    # YAML fallback
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
    """Create encoded token for QuantConnect API.

    Returns:
        {"api_token": "<base64(user_id:sha256(api_key:timestamp))>", "timestamp": "<unix>"}
    """
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
    """Build API headers from the generated token dict."""
    return {
        "Authorization": f"Basic {api_token['api_token']}",
        "Timestamp": api_token["timestamp"],
    }


def download_backtest_results(backtest_id: str, api_token: Dict[str, str], project_id: int) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    """Fetch backtest results via QuantConnect API and save JSON to backtest_results/<id>.json."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(script_dir, "backtest_results")
        os.makedirs(results_dir, exist_ok=True)
        results_path = os.path.join(results_dir, f"{backtest_id}.json")

        api_url = "https://www.quantconnect.com/api/v2/backtests/read"
        headers = _auth_headers(api_token)
        logging.debug(f"Request headers: {headers}")

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
    """Fetch ALL orders for a backtest (paginated) and save to orders_results/<id>_orders.json.

    Returns:
        (orders_path, orders_list)
    """
    try:
        assert 1 <= chunk <= 100, "chunk must be within 1..100"

        script_dir = os.path.dirname(os.path.abspath(__file__))
        orders_dir = os.path.join(script_dir, "orders_results")
        os.makedirs(orders_dir, exist_ok=True)
        orders_path = os.path.join(orders_dir, f"{backtest_id}_orders.json")

        api_url = "https://www.quantconnect.com/api/v2/backtests/orders/read"
        headers = _auth_headers(api_token)

        all_orders: List[Dict[str, Any]] = []
        start = 0
        while True:
            payload = {
                "start": start,
                "end": start + chunk,
                "projectId": project_id,
                "backtestId": backtest_id,
            }
            logging.debug(f"Orders page request payload: {payload}")
            r = requests.post(api_url, headers=headers, json=payload, timeout=60)
            r.raise_for_status()
            page = r.json()

            # Normalize orders (can be dict keyed by id or a list)
            raw_orders = page.get("orders", {})
            length = int(page.get("length", 0)) if page.get("length") is not None else 0

            if isinstance(raw_orders, dict):
                batch = list(raw_orders.values())
            elif isinstance(raw_orders, list):
                batch = raw_orders
            else:
                batch = []

            logging.debug(f"Received {len(batch)} orders on this page (length={length}).")

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


def inspect_api_response(response_data):
    """Log the structure of the API response for debugging."""
    try:
        if response_data:
            logging.info("Inspecting API response structure...")
            logging.info(json.dumps(response_data, indent=4))
        else:
            logging.warning("No response data to inspect.")
    except Exception as e:
        logging.error(f"Failed to inspect API response: {e}")


def write_results_to_database(results_path, backtest_id):
    """Invoke db_operator script to store results in database."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        database_writer_script = os.path.join(script_dir, "db_operator.py")
        
        # Use sys.executable to ensure we use the same python interpreter (Poetry env)
        import sys
        
        db_write_command = (
            f'"{sys.executable}" "{database_writer_script}" '
            f"--results-path \"{results_path}\" --backtest-id {backtest_id}"
        )
        logging.info(f"Calling database writer script for backtest ID: {backtest_id}")
        subprocess.run(db_write_command, shell=True, check=True)
        logging.info(
            "Results successfully written to the database for "
            f"backtest ID: {backtest_id}"
        )
    except subprocess.CalledProcessError as e:
        logging.error(
            f"Failed to write results to the database for ID {backtest_id}: {e}"
        )


if __name__ == "__main__":
    main()
