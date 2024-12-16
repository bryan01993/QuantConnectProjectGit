import json
from google.cloud import bigquery

def load_json_to_bigquery(json_file_path, dataset_id):
    """
    Load a backtest JSON file into respective BigQuery tables.

    Args:
        json_file_path (str): Path to the JSON file.
        dataset_id (str): BigQuery dataset ID where the tables are located.
    """
    client = bigquery.Client(project='bav-personal-cloud')

    # Load JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Parse and insert data into tables
    load_backtest(data, client, dataset_id)
    load_research_guide(data, client, dataset_id)
    load_charts(data, client, dataset_id)
    load_parameter_set(data, client, dataset_id)
    load_rolling_window_stats(data, client, dataset_id)
    load_runtime_statistics(data, client, dataset_id)
    load_total_performance(data, client, dataset_id)
    load_errors(data, client, dataset_id)

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
    } for bt in data.get("backtest", [])]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_research_guide(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPResearchGuide"
    rows_to_insert = [{
        "guideId": f"{bt.get('backtestId')}_guide",
        "backtestId": bt.get("backtestId"),
        "minutes": bt["researchGuide"].get("minutes"),
        "backtestCount": bt["researchGuide"].get("backtestCount"),
        "parameters": bt["researchGuide"].get("parameters")
    } for bt in data.get("backtest", []) if bt.get("researchGuide")]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_charts(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPCharts"
    rows_to_insert = [{
        "chartId": f"{bt.get('backtestId')}_chart",
        "backtestId": bt.get("backtestId"),
        "name": bt["charts"].get("name")
    } for bt in data.get("backtest", []) if bt.get("charts")]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_parameter_set(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPParameterSet"
    rows_to_insert = [{
        "parameterId": f"{bt.get('backtestId')}_param",
        "backtestId": bt.get("backtestId"),
        "name": bt["parameterSet"].get("name"),
        "value": bt["parameterSet"].get("value")
    } for bt in data.get("backtest", []) if bt.get("parameterSet")]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_rolling_window_stats(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPRollingWindowTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPRollingWindowPortfolioStats"

    trade_rows = [{
        "tradeStatId": f"{bt.get('backtestId')}_rw_trade",
        "backtestId": bt.get("backtestId"),
        "startDateTime": bt["rollingWindow"]["tradeStatistics"].get("startDateTime"),
        "endDateTime": bt["rollingWindow"]["tradeStatistics"].get("endDateTime"),
        "totalNumberOfTrades": bt["rollingWindow"]["tradeStatistics"].get("totalNumberOfTrades"),
        "totalProfitLoss": bt["rollingWindow"]["tradeStatistics"].get("totalProfitLoss")
    } for bt in data.get("backtest", []) if bt.get("rollingWindow")]

    portfolio_rows = [{
        "portfolioStatId": f"{bt.get('backtestId')}_rw_portfolio",
        "backtestId": bt.get("backtestId"),
        "averageWinRate": bt["rollingWindow"]["portfolioStatistics"].get("averageWinRate"),
        "profitLossRatio": bt["rollingWindow"]["portfolioStatistics"].get("profitLossRatio")
    } for bt in data.get("backtest", []) if bt.get("rollingWindow")]

    if trade_rows:
        client.insert_rows_json(trade_table_id, trade_rows)

    if portfolio_rows:
        client.insert_rows_json(portfolio_table_id, portfolio_rows)

def load_runtime_statistics(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPRuntimeStatistics"
    rows_to_insert = [{
        "runtimeStatId": f"{bt.get('backtestId')}_runtime",
        "backtestId": bt.get("backtestId"),
        "equity": bt["runtimeStatistics"].get("Equity"),
        "fees": bt["runtimeStatistics"].get("Fees")
    } for bt in data.get("backtest", []) if bt.get("runtimeStatistics")]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

def load_total_performance(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPTotalPerformanceTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPTotalPerformancePortfolioStats"

    trade_rows = [{
        "tradeStatId": f"{bt.get('backtestId')}_tp_trade",
        "backtestId": bt.get("backtestId"),
        "totalNumberOfTrades": bt["totalPerformance"]["tradeStatistics"].get("totalNumberOfTrades"),
        "totalProfitLoss": bt["totalPerformance"]["tradeStatistics"].get("totalProfitLoss")
    } for bt in data.get("backtest", []) if bt.get("totalPerformance")]

    portfolio_rows = [{
        "portfolioStatId": f"{bt.get('backtestId')}_tp_portfolio",
        "backtestId": bt.get("backtestId"),
        "averageWinRate": bt["totalPerformance"]["portfolioStatistics"].get("averageWinRate"),
        "profitLossRatio": bt["totalPerformance"]["portfolioStatistics"].get("profitLossRatio")
    } for bt in data.get("backtest", []) if bt.get("totalPerformance")]

    if trade_rows:
        client.insert_rows_json(trade_table_id, trade_rows)

    if portfolio_rows:
        client.insert_rows_json(portfolio_table_id, portfolio_rows)

def load_errors(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPErrors"
    rows_to_insert = [{
        "errorId": f"{bt.get('backtestId')}_error_{i}",
        "backtestId": bt.get("backtestId"),
        "errorMessage": error
    } for bt in data.get("backtest", []) for i, error in enumerate(data.get("errors", []))]

    if rows_to_insert:
        client.insert_rows_json(table_id, rows_to_insert)

if __name__ == "__main__":
    # Example usage
    json_file = "Scripts/backtest_results/e0f96f651d79bc4463c2c255bcae4e00.json"
    dataset = "your_dataset"
    load_json_to_bigquery(json_file, dataset)
