import requests

def list_backtests(api_key, project_id):
    """List all backtests for a given project ID using the QuantConnect API.

    Args:
    api_key (str): Your QuantConnect API key.
    project_id (int): The project ID whose backtests you want to list.
    """
    # QuantConnect API endpoint to list backtests for a project
    url = f"https://www.quantconnect.com/api/v2/backtests/read?projectId={project_id}"

    # Headers to authenticate your API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.get(url, headers=headers)
    #TODO Fix api_key is not recognized response = {'errorCode': 10002, 'errors': ['The API token hash is not valid. This could be due to an old hash, invalid API token, or an invalid timestamp.'], 'success': False}
    """ Esta parte va dirigida hacia la logica que lleva los backtests en un orden especifico, por lo que es es necesario implementarlo como una libreria para todos los algoritmos desarrollados"""
    #
    # ### List backtests objects in cloud TODO get the names of the files rather than their place in memory
    # list_projects = api.ListBacktests(16037541)  # Takes a project ID
    # print(list_projects.Backtests)
    # backtest = api.ReadBacktest(16037541, "Creative Fluorescent Orange Ant")
    # print(backtest.BacktestId)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        if data.get("success"):
            # Iterate through backtests and print their names and IDs
            for backtest in data["backtests"]:
                print(f"Name: {backtest['name']}, ID: {backtest['backtestId']}")
        else:
            print("Failed to list backtests. Check your project ID and API key.")
    else:
        print(f"Error: {response.status_code}, Message: {response.text}")

# Example usage:
api_key = "2d3f90f3268688177d95e83731b898974f4f9b7dda2e9f065aeb15ab9fee4f28"
project_id = "16037541"  # Replace with your actual project ID
list_backtests(api_key, project_id)
