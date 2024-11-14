import subprocess


def launch_cloud_backtest(project_name: str, bt_number: int):
    """
    Launches a cloud backtest for the specified project using the QuantConnect Lean CLI.

    Args:
    project_name (str): The name of the project to backtest.
    """
    # Command to launch the cloud backtest
    #TODO take last serialnumber using bt_handler function to extract last report.
    #TODO take start and end_date from the algo at execution time
    pre_command = f"lean cloud push"
    command = f"lean cloud backtest {project_name} --name {project_name}_{bt_number}_start_end --push --verbose"

    try:
        # import importlib
        # module = importlib.import_module(project_name)
        # mod = importlib.import_module(project_name)
        # klass = getattr(module, project_name)
        # instance = klass()
        # print(f"StartDate {instance.StartDate}")
        # Execute the command in the terminal
        push_current_code_result = subprocess.run(pre_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
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
launch_cloud_backtest("BuyAndHoldOptions", 18)
