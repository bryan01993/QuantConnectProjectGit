# Import necessary packages
import os
import yaml  # For loading YAML files
import subprocess  # For running command-line operations
import logging  # For error handling and logging
import argparse  # For parsing command-line arguments
import datetime  # For timestamp formatting

# Setup logging configuration
logging.basicConfig(level=logging.DEBUG)


# Define main function
def main():
    # Parse command-line arguments
    args = parse_arguments()
    algorithm_name = args.algorithm_name

    # Resolve absolute path for Resources directory relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resources_path = os.path.join(script_dir, "..", "Resources")
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

    # Placeholder for formatting backtesting command
    command_string = format_command(cmd_vars)

    # Optionally run the formatted command (if needed)
    run_command(command_string)


# Define function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Backtesting Launcher for QuantConnect")
    parser.add_argument("algorithm_name", type=str, nargs="?", default="StatisticalArbitrageOptionsPair",
                        help="Name or shortname of the algorithm to backtest")
    return parser.parse_args()


# Define function to load YAML files from a directory
def load_yaml_files(path):
    # Placeholder for loading all YAML files from the specified directory
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
    # Parse the loaded YAML data and find the matching algorithm by name or shortname
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
    # Validate the parsed configuration
    if parsed_data is None:
        return False
    # Additional validation logic can be added here
    return True


# Define function to extract parsed data into individual variables
def extract_parsed_data(parsed_data):
    cmd_algo_code = parsed_data.get("ALGO_CODE")
    cmd_algo_name = parsed_data.get("ALGO_NAME")
    cmd_algo_proyect = f"{cmd_algo_code}_{cmd_algo_name}"
    cmd_algo_mayus_letters = parsed_data.get("ALGO_MAYUS_LETTERS")
    cmd_algo_public_name = parsed_data.get("ALGO_PUBLIC_NAME")
    cmd_algo_version = parsed_data.get("ALGO_VERSION")
    cmd_algo_short_name = parsed_data.get("ALGO_SHORT_NAME")
    cmd_algo_parametry = parsed_data.get("ALGO_PARAMETRY")
    return {
        "cmd_algo_code": cmd_algo_code,
        "cmd_algo_name": cmd_algo_name,
        "cmd_algo_proyect": cmd_algo_proyect,
        "cmd_algo_mayus_letters": cmd_algo_mayus_letters,
        "cmd_algo_public_name": cmd_algo_public_name,
        "cmd_algo_version": cmd_algo_version,
        "cmd_algo_short_name": cmd_algo_short_name,
        "cmd_algo_parametry": cmd_algo_parametry
    }


# Define function to format the backtesting command
def format_command(cmd_vars):
    # Generate sequential identifier for backtest
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backtest_id = f"V{cmd_vars['cmd_algo_version']}_{cmd_vars['cmd_algo_proyect']}_{timestamp}"
    # Format the command used for cloud backtesting based on cmd_vars
    command = f"lean cloud backtest {cmd_vars['cmd_algo_proyect']} --name {backtest_id}"
    return command


# Define function to run the command in the terminal
def run_command(command_string):
    # Run the command in a subprocess
    try:
        subprocess.run(command_string, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e}")


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
