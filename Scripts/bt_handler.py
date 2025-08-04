import argparse
import base64
import hashlib
import json
import logging
import os
import subprocess
import time

import requests
import yaml

logging.basicConfig(level=logging.DEBUG)


def main():
    """Coordinate download of backtest results and database persistence.

    Steps:
        1. Parse command-line arguments.
        2. Retrieve API credentials.
        3. Generate an API token.
        4. Download backtest results.
        5. Inspect and store results.
    """
    args = parse_arguments()
    backtest_id = args.backtest_id
    api_key, user_id = get_api_key()
    api_token = generate_api_token(api_key, user_id)
    results_path, response_data = download_backtest_results(
        backtest_id, api_token
    )
    if results_path:
        inspect_api_response(response_data)
        write_results_to_database(results_path, backtest_id)


def parse_arguments():
    """Return command-line arguments for the script."""
    parser = argparse.ArgumentParser(
        description=(
            "Backtest Handler for Downloading Results and Storing in Database"
        )
    )
    parser.add_argument(
        "backtest_id",
        type=str,
        nargs="?",
        default="0cb0c5993da6a9c89e72f718e610cdef",
        help="ID of the backtest to handle",
    )
    return parser.parse_args()


def get_api_key():
    """Load API key and user ID from Resources/UserConfig.yaml.

    Pseudocode:
        resolve configuration path relative to script
        open YAML file and parse
        extract LOGIN_API_KEY and USER_ID
        return credentials
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(
            script_dir, "..", "Resources", "UserConfig.yaml"
        )
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            defaults = config.get("defaults", {})
            api_key = defaults.get("LOGIN_API_KEY")
            user_id = defaults.get("USER_ID")
            if not api_key or not user_id:
                raise ValueError(
                    "API key or User ID not found in configuration file."
                )
            logging.info("API key and User ID successfully retrieved.")
            return api_key, user_id
    except Exception as e:
        logging.error(f"Failed to retrieve API key: {e}")
        raise


def generate_api_token(api_key, user_id):
    """Create encoded token for QuantConnect API.

    Pseudocode:
        get current timestamp
        combine API key and timestamp then hash with SHA256
        base64 encode user ID and hashed token
        return token and timestamp
    """
    try:
        timestamp = str(int(time.time()))
        time_stamped_token = f"{api_key}:{timestamp}"
        hashed_token = hashlib.sha256(
            time_stamped_token.encode("utf-8")
        ).hexdigest()
        authentication = f"{user_id}:{hashed_token}"
        api_token = base64.b64encode(
            authentication.encode("utf-8")
        ).decode("ascii")
        logging.debug(
            f"Generated token hash: {hashed_token[:6]}... "
            "(truncated for security)"
        )
        logging.debug(f"Generated timestamp: {timestamp}")
        logging.info("API token successfully generated.")
        return {"api_token": api_token, "timestamp": timestamp}
    except Exception as e:
        logging.error(f"Failed to generate API token: {e}")
        raise


def download_backtest_results(backtest_id, api_token):
    """Fetch backtest results via QuantConnect API.

    Pseudocode:
        create results directory
        build API request headers and payload
        post request to API endpoint
        write JSON response to file
        return file path and response data
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(script_dir, "backtest_results")
        os.makedirs(results_dir, exist_ok=True)
        results_path = os.path.join(results_dir, f"{backtest_id}.json")

        api_url = "https://www.quantconnect.com/api/v2/backtests/read"
        headers = {
            "Authorization": f"Basic {api_token['api_token']}",
            "Timestamp": api_token["timestamp"],
        }
        logging.debug(f"Request headers: {headers}")

        logging.info(
            f"Fetching results for backtest ID: {backtest_id} from API."
        )
        payload = {
            "projectId": 0,  # Replace with actual project ID
            "backtestId": backtest_id,
        }
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()

        with open(results_path, "w") as file:
            json.dump(response_data, file, indent=4)

        logging.info(f"Backtest results downloaded to: {results_path}")
        return results_path, response_data
    except requests.RequestException as e:
        logging.error(
            f"Failed to fetch backtest results for ID {backtest_id}: {e}"
        )
        return None, None


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
    """Invoke db_operator script to store results in database.

    Pseudocode:
        resolve path to db_operator.py
        build command with results path and backtest ID
        run command with subprocess
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        database_writer_script = os.path.join(script_dir, "db_operator.py")
        db_write_command = (
            f"python {database_writer_script} "
            f"--results-path {results_path} --backtest-id {backtest_id}"
        )
        logging.info(
            f"Calling database writer script for backtest ID: {backtest_id}"
        )
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
