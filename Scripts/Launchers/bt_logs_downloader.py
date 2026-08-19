"""
bt_logs_downloader.py
=====================
Downloads raw backtest execution log files from QuantConnect Cloud
and saves them into Scripts/backtest_logs/ for BigQuery ingestion.
"""

from __future__ import annotations

import os
import sys
import argparse
import subprocess
import logging

logging.basicConfig(level=logging.INFO)


def download_cloud_logs(backtest_name: str, project_name: str = "4_EarningsVolatilityCrunch") -> str:
    """
    Downloads log.txt from QuantConnect Cloud via Lean CLI.

    Args:
        backtest_name: Name or ID of the cloud backtest.
        project_name: Name of the project folder in QuantConnect.

    Returns:
        Path to the saved log file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.abspath(os.path.join(script_dir, "..", "backtest_logs"))
    os.makedirs(logs_dir, exist_ok=True)

    output_file = os.path.join(logs_dir, f"{backtest_name}_log.txt")

    cmd = f"lean cloud backtest logs --project \"{project_name}\" --name \"{backtest_name}\""
    logging.info(f"[Downloader] Executing: {cmd}")

    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        with open(output_file, "w", encoding="utf-8") as fh:
            fh.write(res.stdout)
        logging.info(f"[Downloader] [OK] Downloaded logs to: {output_file}")
        return output_file
    except subprocess.CalledProcessError as err:
        logging.error(f"[Downloader] Failed to download logs for {backtest_name}: {err}")
        if err.stderr:
            logging.error(f"Details: {err.stderr}")
        raise err


def main():
    parser = argparse.ArgumentParser(description="Download backtest logs from QuantConnect Cloud")
    parser.add_argument("backtest_name", type=str, help="Name or ID of the backtest")
    parser.add_argument("--project", type=str, default="4_EarningsVolatilityCrunch", help="QuantConnect project folder name")
    args = parser.parse_args()

    download_cloud_logs(args.backtest_name, args.project)


if __name__ == "__main__":
    main()
