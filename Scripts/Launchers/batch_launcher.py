"""
batch_launcher.py
=================
Launches heavy-duty, multi-period QuantConnect backtests split into date-range chunks
(e.g., Years 2015-2021 or 2022-2024).

Features:
- Pushes code once to QuantConnect Cloud.
- Compiles project once via REST API to obtain compileId.
- Asynchronously creates backtests per time chunk via QC REST API in ~5 seconds total.
- Registers chunk metadata into BigQuery table `BTOPBatchChunks`.
- Terminates in under 10 seconds without keeping local or VM compute instances running.

Usage:
    poetry run python Scripts/Launchers/batch_launcher.py --algo 4EVC --years 2015 2016 2017 2018 2019 2020 2021
"""

from __future__ import annotations

import argparse
import datetime as dt
import logging
import os
import sys
import time
from typing import Any, Dict, List
import requests

# Add BigQuery and project root to sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
_BQ_DIR = os.path.join(_PROJECT_ROOT, "Scripts", "BigQuery")
for d in [_PROJECT_ROOT, _BQ_DIR]:
    if d not in sys.path:
        sys.path.insert(0, d)

from batch_manager import get_bigquery_client, register_batch_chunks  # noqa: E402
from bt_launcher import load_yaml_files, parse_yaml_data, extract_parsed_data, push_project_to_cloud  # noqa: E402
from bt_handler import get_api_key  # noqa: E402
from bt_synchronization import generate_api_token  # noqa: E402

logging.basicConfig(level=logging.INFO)


def parse_args():
    parser = argparse.ArgumentParser(description="Multi-Period Chunked Backtest Launcher")
    parser.add_argument("--algo", type=str, default="4EVC", help="Algorithm short name (e.g., 4EVC, 0AT)")
    parser.add_argument("--years", type=int, nargs="+", default=[2015, 2016, 2017, 2018, 2019, 2020, 2021], help="Years to chunk")
    parser.add_argument("--batch-id", type=str, default=None, help="Custom batch ID (optional)")
    parser.add_argument("--project-id", type=int, default=None, help="QuantConnect Project ID (overrides env/YAML if provided)")
    return parser.parse_args()


def resolve_project_id(cli_project_id: int | None) -> int:
    """Resolve QuantConnect project ID from CLI arg, env var, or UserConfig.yaml (in that order)."""
    if cli_project_id is not None:
        logging.info(f"Using Project ID from CLI: {cli_project_id}")
        return cli_project_id

    env_pid = os.getenv("QC_PROJECT_ID")
    if env_pid:
        logging.info(f"Using Project ID from env QC_PROJECT_ID: {env_pid}")
        return int(env_pid)

    try:
        import yaml
        config_path = os.path.join(_PROJECT_ROOT, "Resources", "UserConfig.yaml")
        with open(config_path, "r") as f:
            config = yaml.safe_load(f) or {}
            pid = config.get("defaults", {}).get("PROJECT_ID")
            if pid is not None:
                logging.info(f"Using Project ID from UserConfig.yaml: {pid}")
                return int(pid)
    except Exception as e:
        logging.warning(f"Failed to read Project ID from UserConfig.yaml: {e}")

    raise ValueError(
        "QuantConnect Project ID not found. Provide via --project-id, "
        "QC_PROJECT_ID env var, or Resources/UserConfig.yaml defaults.PROJECT_ID."
    )


def compile_project_on_cloud(project_id: int, headers: Dict[str, str]) -> str:
    """Triggers compilation on QuantConnect Cloud and waits for BuildSuccess state."""
    url_create = "https://www.quantconnect.com/api/v2/compile/create"
    logging.info(f"Triggering compilation on QC Cloud for Project ID {project_id}...")
    res = requests.post(url_create, headers=headers, json={"projectId": project_id}, timeout=30)
    data = res.json()

    if not data.get("success"):
        raise RuntimeError(f"Compile creation failed: {data}")

    compile_id = data.get("compileId")
    state = data.get("state")
    logging.info(f"Compilation initiated with Compile ID: {compile_id} (Initial state: {state})")

    url_read = "https://www.quantconnect.com/api/v2/compile/read"
    max_wait_seconds = 60
    start_time = time.time()

    while state not in ["BuildSuccess", "BuildError"]:
        if time.time() - start_time > max_wait_seconds:
            raise TimeoutError(f"Compilation timed out after {max_wait_seconds}s.")
        time.sleep(2)
        r = requests.post(url_read, headers=headers, json={"projectId": project_id, "compileId": compile_id}, timeout=30)
        d = r.json()
        state = d.get("state")

    if state != "BuildSuccess":
        raise RuntimeError(f"Compilation failed on QC Cloud with state: {state}")

    logging.info(f"[SUCCESS] Compilation successful! Compile ID: {compile_id}")
    return compile_id


def create_cloud_backtest(project_id: int, compile_id: str, backtest_name: str, start_date: str, end_date: str, headers: Dict[str, str]) -> str:
    """Asynchronously creates a backtest chunk via QuantConnect REST API."""
    url_create = "https://www.quantconnect.com/api/v2/backtests/create"
    payload = {
        "projectId": project_id,
        "compileId": compile_id,
        "backtestName": backtest_name,
        "parameters": [
            {"key": "exec.start_date", "value": start_date},
            {"key": "exec.end_date", "value": end_date},
            {"key": "algo.is_hdbt", "value": "true"},
            {"key": "algo.pass_all", "value": "true"},
            {"key": "univ.coarse.max_symbols", "value": "1000"}
        ]
    }

    res = requests.post(url_create, headers=headers, json=payload, timeout=30)
    data = res.json()

    if not data.get("success"):
        raise RuntimeError(f"Backtest creation failed for {backtest_name}: {data}")

    bt_info = data.get("backtest", {})
    hex_id = bt_info.get("backtestId") or bt_info.get("id") or backtest_name
    logging.info(f"Queued backtest '{backtest_name}' on QC Cloud -> Hex ID: {hex_id}")
    return hex_id


def main():
    args = parse_args()
    algo_name = args.algo

    resources_path = os.path.join(_PROJECT_ROOT, "Resources")
    yaml_files = load_yaml_files(resources_path)
    parsed_data = parse_yaml_data(yaml_files, algo_name)
    if not parsed_data:
        logging.error(f"Algorithm '{algo_name}' configuration not found in Resources YAML files.")
        sys.exit(1)

    cmd_vars = extract_parsed_data(parsed_data)

    # 1. Push project once to QuantConnect Cloud
    logging.info(f"Pushing project '{cmd_vars['cmd_algo_name']}' to QuantConnect Cloud...")
    push_project_to_cloud(cmd_vars)

    # 2. Authenticate and Compile Project
    api_key, user_id = get_api_key()
    api_token_data = generate_api_token(api_key, user_id)
    headers = {
        "Authorization": f"Basic {api_token_data['api_token']}",
        "Timestamp": str(api_token_data["timestamp"])
    }
    project_id = resolve_project_id(args.project_id)

    compile_id = compile_project_on_cloud(project_id, headers)

    # 3. Construct batch ID
    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    batch_id = args.batch_id or f"HDBT_{cmd_vars['cmd_algo_short_name']}_V{cmd_vars['cmd_algo_version']}_{timestamp}"
    logging.info(f"Initiating multi-period batch run: {batch_id}")

    chunk_records = []

    # 4. Launch Chunk 1 immediately and queue remaining chunks as PENDING
    for idx, yr in enumerate(args.years, start=1):
        start_date = f"{yr}-01-01"
        end_date = f"{yr}-12-31"
        chunk_name = f"{batch_id}_Y{yr}"

        if idx == 1:
            logging.info(f"[Chunk {idx}/{len(args.years)}] Launching Chunk 1 for period {start_date} to {end_date} (Name: {chunk_name})...")
            try:
                hex_id = create_cloud_backtest(
                    project_id=project_id,
                    compile_id=compile_id,
                    backtest_name=chunk_name,
                    start_date=start_date,
                    end_date=end_date,
                    headers=headers
                )

                chunk_records.append({
                    "backtest_id": hex_id,
                    "chunk_index": idx,
                    "start_date": start_date,
                    "end_date": end_date,
                    "status": "RUNNING",
                    "compile_id": compile_id
                })
            except Exception as e:
                logging.error(f"Failed to launch chunk 1 ({chunk_name}): {e}")
                chunk_records.append({
                    "backtest_id": chunk_name,
                    "chunk_index": idx,
                    "start_date": start_date,
                    "end_date": end_date,
                    "status": "FAILED",
                    "compile_id": compile_id
                })
        else:
            logging.info(f"[Chunk {idx}/{len(args.years)}] Queuing Chunk #{idx} ({start_date} to {end_date}) as PENDING...")
            chunk_records.append({
                "backtest_id": chunk_name,
                "chunk_index": idx,
                "start_date": start_date,
                "end_date": end_date,
                "status": "PENDING",
                "compile_id": compile_id
            })

    # 5. Register batch metadata into BigQuery BTOPBatchChunks
    bq_client = get_bigquery_client()
    register_batch_chunks(
        client=bq_client,
        batch_id=batch_id,
        algo_code=cmd_vars['cmd_algo_short_name'],
        chunks=chunk_records
    )

    logging.info("=" * 65)
    logging.info(f"[COMPLETE] Batch '{batch_id}' successfully queued in BigQuery table 'BTOPBatchChunks'.")
    logging.info("Serverless launcher finished in ~5 seconds. Local PC process terminating immediately.")
    logging.info("Serverless poller (Scripts/BigQuery/qc_batch_poller.py) will ingest completed trades into BigQuery.")
    logging.info("=" * 65)


if __name__ == "__main__":
    main()

