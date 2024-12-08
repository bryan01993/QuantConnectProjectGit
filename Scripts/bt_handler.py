# Import necessary packages
import os
import requests
import logging
import argparse
import yaml
import subprocess
import time
import hashlib

# Setup logging configuration
logging.basicConfig(level=logging.DEBUG)

# Define main function
def main():
    # Parse command-line arguments
    args = parse_arguments()
    backtest_id = args.backtest_id

    # Retrieve API key from configuration
    api_key = get_api_key()

    # Generate API token with timestamp and hash
    api_token = generate_api_token(api_key)

    # Download the results of the backtest
    results_path = download_backtest_results(backtest_id, api_token)

    if results_path:
        # Call the database writer script with the downloaded results
        write_results_to_database(results_path, backtest_id)

# Define function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Backtest Handler for Downloading Results and Storing in Database")
    parser.add_argument("backtest_id", type=str, nargs="?", default="test_backtest_id", help="ID of the backtest to handle")
    return parser.parse_args()

# Define function to retrieve API key from UserConfig.yaml
def get_api_key():
    try:
        # Resolve absolute path to UserConfig.yaml relative to script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "..", "Resources", "UserConfig.yaml")
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            defaults = config.get("defaults", {})
            api_key = defaults.get("LOGIN_API_KEY")
            if not api_key:
                raise ValueError("API key not found in configuration file.")
            logging.info("API key successfully retrieved from configuration.")
            return api_key
    except Exception as e:
        logging.error(f"Failed to retrieve API key: {e}")
        raise

# Define function to generate API token with timestamp and hash
def generate_api_token(api_key):
    try:
        # Get the current timestamp
        timestamp = str(int(time.time()))

        # Combine the API key and timestamp, then hash them using SHA256
        token_string = f"{api_key}:{timestamp}"
        hashed_token = hashlib.sha256(token_string.encode()).hexdigest()

        # Return the hashed token and timestamp as required by the API
        logging.info("API token successfully generated.")
        return {"hashed_token": hashed_token, "timestamp": timestamp}
    except Exception as e:
        logging.error(f"Failed to generate API token: {e}")
        raise

# Define function to download backtest results via QuantConnect API
def download_backtest_results(backtest_id, api_token):
    try:
        results_dir = "backtest_results"
        os.makedirs(results_dir, exist_ok=True)
        results_path = os.path.join(results_dir, f"{backtest_id}.json")

        # Define the API endpoint and headers
        api_url = f"https://www.quantconnect.com/api/v2/backtests/{backtest_id}/results"
        headers = {
            "Authorization": f"Bearer {api_token['hashed_token']}",
            "Timestamp": api_token['timestamp']
        }

        # Make the API request
        logging.info(f"Fetching results for backtest ID: {backtest_id} from QuantConnect API.")
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        # Save the results to a JSON file
        with open(results_path, "w") as file:
            file.write(response.text)

        logging.info(f"Backtest results downloaded to: {results_path}")
        return results_path

    except requests.RequestException as e:
        logging.error(f"Failed to fetch backtest results for ID {backtest_id}: {e}")
        return None

# Define function to call the database writer script
def write_results_to_database(results_path, backtest_id):
    try:
        # Construct the command to call the database writer script
        database_writer_script = "db_operator.py"

        db_write_command = f"python {database_writer_script} --results-path {results_path} --backtest-id {backtest_id}"

        logging.info(f"Calling database writer script for backtest ID: {backtest_id}")
        subprocess.run(db_write_command, shell=True, check=True)

        logging.info(f"Results successfully written to the database for backtest ID: {backtest_id}")

    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to write results to the database for ID {backtest_id}: {e}")

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
