# Import necessary packages
import os
import yaml  # For loading YAML files
import subprocess  # For running command-line operations
import logging  # For error handling and logging
import argparse  # For parsing command-line arguments
import datetime  # For timestamp formatting
import time
import urllib.request
import email.utils

def sync_clock_skew_time():
    try:
        with urllib.request.urlopen("https://www.google.com", timeout=3) as resp:
            date_hdr = resp.headers.get("date")
        if date_hdr:
            server_dt = email.utils.parsedate_to_datetime(date_hdr)
            local_dt = datetime.datetime.now(datetime.timezone.utc)
            skew = (server_dt - local_dt).total_seconds()
            if abs(skew) > 5:
                if not hasattr(time, "_unpatched_time"):
                    time._unpatched_time = time.time
                time.time = lambda: time._unpatched_time() + skew
                logging.info(f"[TIME SYNC] Successfully compensated system clock skew: {skew:.1f}s")
    except Exception as e:
        logging.warning(f"[TIME SYNC WARN] {e}")

# Setup logging configuration
logging.basicConfig(level=logging.INFO)

# Define main function
def main():
    sync_clock_skew_time()
    # Parse command-line arguments
    args = parse_arguments()
    algorithm_name = args.algorithm_name

    # Resolve absolute path for Resources directory relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    resources_path = os.path.join(project_root, "Resources")
    logging.debug(f"Resolved Resources path: {resources_path}")

    # Check if Resources directory exists
    if not os.path.exists(resources_path):
        logging.error(f"Resources directory not found at path: {resources_path}")
        return

    # Placeholder for loading YAML files from a given path
    yaml_files = load_yaml_files(resources_path)

    # Placeholder for parsing the loaded YAML files
    parsed_data = parse_yaml_data(yaml_files, algorithm_name)

    # Placeholder for validating parsed information
    if not validate_config(parsed_data):
        logging.error("Validation failed. Exiting.")
        return

    # Extract parsed data into variables for easier access
    cmd_vars = extract_parsed_data(parsed_data)

    # Push project to cloud before executing the backtest
    push_project_to_cloud(cmd_vars)

    # Placeholder for formatting backtesting command
    command_string, backtest_id = format_command(cmd_vars)

    # Run the formatted command and check for success
    if run_command(command_string):
        logging.info("Backtest triggered successfully.")
        
        # Chain the handler execution
        handler_command = f"poetry run python Scripts/BigQuery/bt_handler.py {backtest_id}"
        logging.info(f"Triggering handler: {handler_command}")
        run_command(handler_command)
    else:
        logging.error("Backtest failed to start or complete successfully. Handler will not be triggered.")


# Define function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Backtesting Launcher for QuantConnect")
    parser.add_argument("algorithm_name", type=str, nargs="?", default="AlgoTester",
                        help="Name or shortname of the algorithm to backtest")
    return parser.parse_args()


# Define function to load YAML files from a directory
def load_yaml_files(path):
    yaml_files = []
    for root, _, files in os.walk(path):
        for file_name in files:
            if file_name.endswith(".yaml"):
                try:
                    file_path = os.path.join(root, file_name)
                    logging.debug(f"Loading YAML file: {file_path}")
                    with open(file_path, 'r') as file:
                        yaml_data = yaml.safe_load(file)
                        if yaml_data:
                            yaml_files.append(yaml_data)
                except yaml.YAMLError as e:
                    logging.error(f"Error loading YAML file {file_name}: {e}")
    if not yaml_files:
        logging.warning(f"No YAML files found in directory: {path}")
    return yaml_files


# Define function to parse YAML data
def parse_yaml_data(yaml_files, algorithm_name):
    for yaml_data in yaml_files:
        logging.debug(f"Checking YAML data: {yaml_data}")
        if "ALGOS" in yaml_data:
            for algo in yaml_data["ALGOS"]:
                if algo.get("ALGO_NAME") == algorithm_name or algo.get("ALGO_SHORT_NAME") == algorithm_name:
                    logging.info(f"Found matching algorithm: {algorithm_name}")
                    return algo
    logging.error(f"Algorithm {algorithm_name} not found in YAML files.")
    return None


# Define function to validate the parsed configuration
def validate_config(parsed_data):
    if parsed_data is None:
        return False
    return True


# Define function to extract parsed_data into individual variables
def extract_parsed_data(parsed_data):
    cmd_algo_code = parsed_data.get("ALGO_CODE")
    cmd_algo_name = parsed_data.get("ALGO_NAME")
    cmd_algo_short_name = parsed_data.get("ALGO_SHORT_NAME")
    cmd_algo_proyect = f"{cmd_algo_short_name}"

    cmd_algo_mayus_letters = parsed_data.get("ALGO_MAYUS_LETTERS")
    cmd_algo_public_name = parsed_data.get("ALGO_PUBLIC_NAME")
    cmd_algo_version = parsed_data.get("ALGO_VERSION")
    cmd_algo_parametry = parsed_data.get("ALGO_PARAMETRY")
    cmd_algo_start_date = parsed_data.get("START_DATE")
    cmd_algo_end_date = parsed_data.get("END_DATE")
    return {
        "cmd_algo_code": cmd_algo_code,
        "cmd_algo_name": cmd_algo_name,
        "cmd_algo_short_name": cmd_algo_short_name,
        "cmd_algo_proyect": cmd_algo_proyect,
        "cmd_algo_mayus_letters": cmd_algo_mayus_letters,
        "cmd_algo_public_name": cmd_algo_public_name,
        "cmd_algo_version": cmd_algo_version,
        "cmd_algo_parametry": cmd_algo_parametry,
        "cmd_algo_start_date": cmd_algo_start_date,
        "cmd_algo_end_date": cmd_algo_end_date
    }


# Define function to format the backtesting command
def format_command(cmd_vars):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backtest_id = f"BT_{cmd_vars['cmd_algo_proyect']}_V{cmd_vars['cmd_algo_version']}_{timestamp}"
    command = f"lean cloud backtest {cmd_vars['cmd_algo_code']}_{cmd_vars['cmd_algo_name']} --name {backtest_id}"
    print(f"{command}")
    return command, backtest_id


# Define function to push the project to the cloud
def push_project_to_cloud(cmd_vars):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))

    project_folder_name = f"{cmd_vars['cmd_algo_code']}_{cmd_vars['cmd_algo_name']}"
    push_command = f"lean cloud push --project {project_folder_name}"
    try:
        logging.info(f"Pushing project to cloud: {cmd_vars['cmd_algo_name']}")
        subprocess.run(push_command, shell=True, check=True, cwd=project_root)
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to push project to cloud with error: {e}")


# Define function to run the command in the terminal
def run_command(command_string):
    try:
        subprocess.run(command_string, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e}")
        return False


if __name__ == "__main__":
    main()
