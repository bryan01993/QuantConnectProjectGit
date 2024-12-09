# Import necessary packages
import os
import requests
import logging
import argparse
import yaml
import subprocess
import time
import hashlib
import base64
import json

# Setup logging configuration
logging.basicConfig(level=logging.DEBUG)

# Define main function
def main():
    # Parse command-line arguments
    args = parse_arguments()
    backtest_id = args.backtest_id

    # Retrieve API key and user ID from configuration
    api_key, user_id = get_api_key()

    # Generate API token with timestamp and hash
    api_token = generate_api_token(api_key, user_id)

    # Download the results of the backtest
    results_path, response_data = download_backtest_results(backtest_id, api_token)

    if results_path:
        # Log the structure of the API response
        inspect_api_response(response_data)

        # Call the database writer script with the downloaded results
        write_results_to_database(results_path, backtest_id)

# Define function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Backtest Handler for Downloading Results and Storing in Database")
    parser.add_argument("backtest_id", type=str, nargs="?", default="04cee94468156ad207fc43329f697139", help="ID of the backtest to handle")
    return parser.parse_args()

# Define function to retrieve API key and user ID from UserConfig.yaml
def get_api_key():
    try:
        # Resolve absolute path to UserConfig.yaml relative to script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "..", "Resources", "UserConfig.yaml")
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            defaults = config.get("defaults", {})
            api_key = defaults.get("LOGIN_API_KEY")
            user_id = defaults.get("USER_ID")
            if not api_key or not user_id:
                raise ValueError("API key or User ID not found in configuration file.")
            logging.info("API key and User ID successfully retrieved from configuration.")
            return api_key, user_id
    except Exception as e:
        logging.error(f"Failed to retrieve API key: {e}")
        raise

# Define function to generate API token with timestamp and hash
def generate_api_token(api_key, user_id):
    try:
        # Get the current timestamp
        timestamp = str(int(time.time()))

        # Combine the API key and timestamp, then hash them using SHA256
        time_stamped_token = f"{api_key}:{timestamp}"
        hashed_token = hashlib.sha256(time_stamped_token.encode('utf-8')).hexdigest()

        # Format the authentication string and encode it in base64
        authentication = f"{user_id}:{hashed_token}"
        api_token = base64.b64encode(authentication.encode('utf-8')).decode('ascii')

        # Log the generated token for debugging (masked for security)
        logging.debug(f"Generated token hash: {hashed_token[:6]}... (truncated for security)")
        logging.debug(f"Generated timestamp: {timestamp}")

        # Return the encoded API token and timestamp
        logging.info("API token successfully generated.")
        return {"api_token": api_token, "timestamp": timestamp}
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
        api_url = f"https://www.quantconnect.com/api/v2/backtests/{backtest_id}/statistics"
        headers = {
            "Authorization": f"Basic {api_token['api_token']}",
            "Timestamp": api_token['timestamp']
        }

        # Log headers for debugging
        logging.debug(f"Request headers: {headers}")

        # Make the API request
        logging.info(f"Fetching results for backtest ID: {backtest_id} from QuantConnect API.")
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        # Parse the JSON response
        response_data = response.json()

        # Save the results to a JSON file
        with open(results_path, "w") as file:
            json.dump(response_data, file, indent=4)

        logging.info(f"Backtest results downloaded to: {results_path}")
        return results_path, response_data

    except requests.RequestException as e:
        logging.error(f"Failed to fetch backtest results for ID {backtest_id}: {e}")
        return None, None

# Define function to inspect the structure of the API response
def inspect_api_response(response_data):
    try:
        if response_data:
            logging.info("Inspecting API response structure...")
            logging.info(json.dumps(response_data, indent=4))
        else:
            logging.warning("No response data to inspect.")
    except Exception as e:
        logging.error(f"Failed to inspect API response: {e}")

# Define function to call the database writer script
def write_results_to_database(results_path, backtest_id):
    try:
        # Resolve absolute path to the db_operator script relative to script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        database_writer_script = os.path.join(script_dir, "db_operator.py")

        # Construct the command to call the database writer script
        db_write_command = f"python {database_writer_script} --results-path {results_path} --backtest-id {backtest_id}"

        logging.info(f"Calling database writer script for backtest ID: {backtest_id}")
        subprocess.run(db_write_command, shell=True, check=True)

        logging.info(f"Results successfully written to the database for backtest ID: {backtest_id}")

    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to write results to the database for ID {backtest_id}: {e}")

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
