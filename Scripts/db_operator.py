import json
import os
from google.cloud import bigquery

def load_json_to_bigquery(json_file_path, dataset_id):
    """
    Load a backtest JSON file into respective BigQuery tables.

    Args:
        json_file_path (str): Path to the JSON file.
        dataset_id (str): BigQuery dataset ID where the tables are located.
    """
    client = bigquery.Client(project='bav-personal-cloud')

    # Check if the file has already been uploaded
    uploaded_files_table = f"{dataset_id}.BTOPResults"
    json_file_name = os.path.basename(json_file_path)

    query = f"""
        SELECT COUNT(backtestId) as count
        FROM `{uploaded_files_table}`
        WHERE backtestId = '{json_file_name.strip(".json")}'
    """
    query_job = client.query(query)
    results = query_job.result()
    count = [row.count for row in results][0]

    if count > 0:
        print(f"File {json_file_name} has already been uploaded. Skipping upload.")
        return

    # Load JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Parse and insert data into tables
    print("Loading backtest data...")
    load_backtest(data, client, dataset_id)
    print("Loading research guide data...")
    load_research_guide(data, client, dataset_id)
    print("Loading charts data...")
    load_charts(data, client, dataset_id)
    print("Loading parameter set data...")
    load_parameter_set(data, client, dataset_id)
    print("Loading rolling window stats data...")
    load_rolling_window_stats(data, client, dataset_id)
    print("Loading runtime statistics data...")
    load_runtime_statistics(data, client, dataset_id)
    print("Loading total performance data...")
    load_total_performance(data, client, dataset_id)
    print("Loading errors data...")
    load_errors(data, client, dataset_id)
    print("Data loading complete.")

def load_backtest(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPResults"
    rows_to_insert = [{
        "backtestId": bt.get("backtestId"),
        "name": bt.get("name"),
        "note": bt.get("note"),
        "organizationId": bt.get("organizationId"),
        "projectId": bt.get("projectId"),
        "completed": bt.get("completed"),
        "optimizationId": bt.get("optimizationId"),
        "tradeableDates": bt.get("tradeableDates"),
        "backtestStart": bt.get("backtestStart"),
        "backtestEnd": bt.get("backtestEnd"),
        "created": bt.get("created"),
        "snapshotId": bt.get("snapshotId"),
        "status": bt.get("status"),
        "error": bt.get("error"),
        "stacktrace": bt.get("stacktrace"),
        "progress": bt.get("progress"),
        "hasInitializeError": bt.get("hasInitializeError"),
        "nodeName": bt.get("nodeName"),
        "outOfSampleMaxEndDate": bt.get("outOfSampleMaxEndDate"),
        "outOfSampleDays": bt.get("outOfSampleDays")
    } for bt in [data.get("backtest", {})]]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_research_guide(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPResearchGuide"
    rows_to_insert = [{
        "guideId": f"{data['backtest'].get('backtestId')}_guide",
        "backtestId": data["backtest"].get("backtestId"),
        "minutes": data["backtest"]["researchGuide"].get("minutes"),
        "backtestCount": data["backtest"]["researchGuide"].get("backtestCount"),
        "parameters": data["backtest"]["researchGuide"].get("parameters")
    }] if data.get("backtest") and data["backtest"].get("researchGuide") else []

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_charts(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPCharts"
    rows_to_insert = [{
        "chartId": f"{data['backtest'].get('backtestId')}_chart",
        "backtestId": data["backtest"].get("backtestId"),
        "name": chart_data["name"]
    } for chart_key, chart_data in data["backtest"].get("charts", {}).items()]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_parameter_set(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPParameterSet"
    rows_to_insert = [{
        "parameterId": f"{data['backtest'].get('backtestId')}_param",
        "backtestId": data["backtest"].get("backtestId"),
        "name": param.get("name"),
        "value": param.get("value")
    } for param in data["backtest"].get("parameterSet", [])]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_rolling_window_stats(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPRollingWindowTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPRollingWindowPortfolioStats"

    rolling_window = data["backtest"].get("rollingWindow")
    if rolling_window:
        trade_rows = [{
            "tradeStatId": f"{data['backtest'].get('backtestId')}_rw_trade",
            "backtestId": data["backtest"].get("backtestId"),
            "startDateTime": rolling_window["tradeStatistics"].get("startDateTime"),
            "endDateTime": rolling_window["tradeStatistics"].get("endDateTime"),
            "totalNumberOfTrades": rolling_window["tradeStatistics"].get("totalNumberOfTrades"),
            "totalProfitLoss": rolling_window["tradeStatistics"].get("totalProfitLoss")
        }] if rolling_window.get("tradeStatistics") else []

        portfolio_rows = [{
            "portfolioStatId": f"{data['backtest'].get('backtestId')}_rw_portfolio",
            "backtestId": data["backtest"].get("backtestId"),
            "averageWinRate": rolling_window["portfolioStatistics"].get("averageWinRate"),
            "profitLossRatio": rolling_window["portfolioStatistics"].get("profitLossRatio")
        }] if rolling_window.get("portfolioStatistics") else []

        if trade_rows:
            client.insert_rows_json(trade_table_id, trade_rows)

        if portfolio_rows:
            client.insert_rows_json(portfolio_table_id, portfolio_rows)

def load_runtime_statistics(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPRuntimeStatistics"
    runtime_stats = data["backtest"].get("runtimeStatistics", {})

    rows_to_insert = [{
        "runtimeStatId": f"{data['backtest'].get('backtestId')}_runtime",
        "backtestId": data["backtest"].get("backtestId"),
        "equity": runtime_stats.get("Equity"),
        "fees": runtime_stats.get("Fees")
    }]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_total_performance(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPTotalPerformanceTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPTotalPerformancePortfolioStats"

    total_performance = data["backtest"].get("totalPerformance")
    if total_performance:
        trade_rows = [{
            "tradeStatId": f"{data['backtest'].get('backtestId')}_tp_trade",
            "backtestId": data["backtest"].get("backtestId"),
            "totalNumberOfTrades": total_performance["tradeStatistics"].get("totalNumberOfTrades"),
            "totalProfitLoss": total_performance["tradeStatistics"].get("totalProfitLoss")
        }] if total_performance.get("tradeStatistics") else []

        portfolio_rows = [{
            "portfolioStatId": f"{data['backtest'].get('backtestId')}_tp_portfolio",
            "backtestId": data["backtest"].get("backtestId"),
            "averageWinRate": total_performance["portfolioStatistics"].get("averageWinRate"),
            "profitLossRatio": total_performance["portfolioStatistics"].get("profitLossRatio")
        }] if total_performance.get("portfolioStatistics") else []

        if trade_rows:
            client.insert_rows_json(trade_table_id, trade_rows)

        if portfolio_rows:
            client.insert_rows_json(portfolio_table_id, portfolio_rows)

def load_errors(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPErrors"
    errors = data.get("errors", [])
    rows_to_insert = [{
        "errorId": f"{data['backtest'].get('backtestId')}_error_{i}",
        "backtestId": data["backtest"].get("backtestId"),
        "errorMessage": error
    } for i, error in enumerate(errors)]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(current_dir, "../Scripts/backtest_results/e0f96f651d79bc4463c2c255bcae4e00.json")
    dataset = "develop"

    # Run the data load
    load_json_to_bigquery(json_file, dataset)

    # Move the file after successful execution
    destination_dir = os.path.join(current_dir, "../Scripts/already_uploaded_backtest_results")
    os.makedirs(destination_dir, exist_ok=True)
    destination_file = os.path.join(destination_dir, os.path.basename(json_file))
    os.rename(json_file, destination_file)
    print(f"File moved to {destination_file}")
