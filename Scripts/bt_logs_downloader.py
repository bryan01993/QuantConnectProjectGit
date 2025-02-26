import base64
import hashlib
import time
import json
import requests

# === Configuration ===
USER_ID = "116616"         # Replace with your QuantConnect user ID (integer as string).
API_TOKEN = "2d3f90f3268688177d95e83731b898974f4f9b7dda2e9f065aeb15ab9fee4f28"     # Replace with your QuantConnect API token (string).
PROJECT_ID = 21565345              # Replace with your project ID (integer).
BACKTEST_ID = "e14d5a59e013217a053fd67dd70f666c" # Replace with your backtest ID (string).

# === 1. Generate timestamped API token hash for authentication ===
timestamp = str(int(time.time()))
# Create the time-stamped token string "<API_TOKEN>:<timestamp>"
token_with_timestamp = f"{API_TOKEN}:{timestamp}"
# Compute SHA-256 hash of the time-stamped token
hashed_bytes = hashlib.sha256(token_with_timestamp.encode('utf-8')).digest()
hashed_token = hashed_bytes.hex()  # hex string representation of the hash

# Combine User ID and hashed token, then Base64 encode for Basic Auth
auth_string = f"{USER_ID}:{hashed_token}"
auth_bytes = auth_string.encode('utf-8')
base64_auth = base64.b64encode(auth_bytes).decode('ascii')

# Prepare the request headers with authentication
headers = {
    "Authorization": f"Basic {base64_auth}",  # Basic auth with Base64(UserID:hashed_token)
    "Timestamp": timestamp                    # Timestamp header (required by API)
}

# === 2. Make API request to retrieve backtest logs ===
url = "https://www.quantconnect.com/api/v2/backtests/read"
# Build the request payload with project and backtest identifiers
payload = {
    "projectId": PROJECT_ID,
    "backtestId": BACKTEST_ID
}
try:
    # Send POST request to QuantConnect API
    response = requests.post(url, json=payload, headers=headers)
except Exception as e:
    print(f"Failed to send request: {e}")
    exit(1)

# Check for HTTP 200 OK status
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}: {response.text}")
    exit(1)

# Parse the JSON response
data = response.json()
if not data.get("success", False):
    # The API returns a 'success' field in JSON to indicate if the call was successful
    errors = data.get("errors", [])
    print(f"API call reported failure. Errors: {errors}")
    exit(1)

# The 'backtest' field contains a list of backtest result(s). We expect one result here.
backtests = data.get("backtest", [])
if not backtests:
    print("No backtest data found in response.")
    exit(1)
######## IT STILL CAN'T EXTRACT LOGS #######
backtest_result = backtests[0]  # get the first (and only) backtest result
# Extract the logs from the backtest result. Assuming logs are under key 'logs' as a list of strings.
logs = backtest_result.get("logs", [])
# If the logs field is not present or empty, handle accordingly.
if not logs:
    print("No logs found for the specified backtest (logs may be empty or not included).")
    # You can still proceed to write an empty list or handle as needed.

# === 3. Save the logs to a JSON file ===
output_filename = "backtest_logs.json"
try:
    with open(output_filename, "w") as f:
        # Save logs inside a JSON object for clarity (could also save the entire backtest_result if needed)
        json.dump({"logs": logs}, f, indent=4)
    print(f"Backtest logs have been saved to {output_filename}")
except Exception as e:
    print(f"Failed to write logs to file: {e}")
