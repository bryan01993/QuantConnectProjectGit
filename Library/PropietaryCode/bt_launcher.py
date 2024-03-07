import subprocess


def launch_cloud_backtest(project_name):
    """
    Launches a cloud backtest for the specified project using the QuantConnect Lean CLI.

    Args:
    project_name (str): The name of the project to backtest.
    """
    # Command to launch the cloud backtest
    command = f"lean cloud backtest {project_name} --name {project_name}_serialnumber_start_end --push"

    try:
        # Execute the command in the terminal
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)

        # Print the output of the command
        print("Backtest launched successfully.")
        print(result.stdout)
    except Exception as e:
        # Print any errors that occur
        print("Error launching backtest:")
        print(e)

# Example usage:
launch_cloud_backtest("BuyAndHoldOptions")