import json
import os
import time
from google.cloud import bigquery

# If you run into cross-partition or cross-filesystem issues with os.rename, consider using shutil.move.
import shutil

def insert_rows_with_logging(client, table_id, rows_to_insert):
    """
    Inserts rows into the given BigQuery table and logs any errors.

    Args:
        client (bigquery.Client): The BigQuery client.
        table_id (str): The full table ID ("dataset.table").
        rows_to_insert (List[Dict]): The rows to insert.
    """
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        print(f"Errors inserting into {table_id}: {errors}")
    else:
        print(f"Successfully inserted rows into {table_id}")


def load_json_to_bigquery(json_file_path, dataset_id):
    """
    Load a backtest JSON file into respective BigQuery tables.

    If the file's backtestId is already in BigQuery, skip upload and move the file
    to the already_uploaded_backtest_results folder. If the file already exists
    at the destination, rename the new file by appending a timestamp.

    Args:
        json_file_path (str): Path to the JSON file.
        dataset_id (str): BigQuery dataset ID where the tables are located.
    """
    # Derive the script's absolute directory path
    current_dir = os.path.dirname(os.path.abspath(__file__))

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

    # Construct the folder for already-uploaded files
    already_uploaded_dir = os.path.join(current_dir, "../Scripts/already_uploaded_backtest_results")
    os.makedirs(already_uploaded_dir, exist_ok=True)
    destination_file = os.path.join(already_uploaded_dir, json_file_name)

    # Helper function to safely move the file (avoid collisions)
    def safe_move(src, dst):
        if os.path.exists(dst):
            base, ext = os.path.splitext(dst)
            dst = f"{base}_{int(time.time())}{ext}"
        shutil.move(src, dst)
        print(f"File moved to {dst}")

    # if count > 0:
    #     print(f"File {json_file_name} has already been uploaded. Moving file...")
    #     safe_move(json_file_path, destination_file)
    #     return

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

    # After successful insert, safely move the file
    safe_move(json_file_path, destination_file)


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
        insert_rows_with_logging(client, table_id, rows_to_insert)

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
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_charts(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPCharts"
    rows_to_insert = [{
        "chartId": f"{data['backtest'].get('backtestId')}_chart",
        "backtestId": data["backtest"].get("backtestId"),
        "name": chart_data["name"]
    } for chart_key, chart_data in data["backtest"].get("charts", {}).items()]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_parameter_set(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPParameterSet"
    param_dict = data["backtest"].get("parameterSet", {})

    if not param_dict:
        # If param_dict is empty or missing, we make 'parameters' = None
        parameters_value = [{
            "name": "empty",
            "value": "empty"
        }]
    else:
        # Build a list of { "name": <key>, "value": <value> } records
        parameters_value = []
        for key, val in param_dict.items():
            parameters_value.append({
                "name": key,
                "value": str(val)  # Convert to string if your schema expects STRING
            })

    # Insert exactly one row, containing all the key/value pairs (or None if empty)
    rows_to_insert = [{
        "parameterId": f"{data['backtest'].get('backtestId')}_param",
        "backtestId": data["backtest"].get("backtestId"),
        "parameters": parameters_value
    }]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_rolling_window_stats(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPRollingWindowTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPRollingWindowPortfolioStats"
#TODO
    #gotta make sure rolling windows data is getting uploaded correctly.
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
            insert_rows_with_logging(client, trade_table_id, trade_rows)

        if portfolio_rows:
            insert_rows_with_logging(client, portfolio_table_id, portfolio_rows)

def load_runtime_statistics(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPRuntimeStatistics"
    runtime_stats = data["backtest"].get("runtimeStatistics", {})

    rows_to_insert = [{
        "runtimeStatId": f"{data['backtest'].get('backtestId')}_runtime",
        "backtestId": data["backtest"].get("backtestId"),
        "equity": runtime_stats.get("Equity"),
        "fees": runtime_stats.get("Fees"),
        "holdings": runtime_stats.get("Holdings"),
        "netProfit": runtime_stats.get("Net Profit"),
        "probabilisticSharpeRatio": runtime_stats.get("Probabilistic Sharpe Ratio"),
        "return": runtime_stats.get("Return"),
        "unrealized": runtime_stats.get("Unrealized"),
        "volume": runtime_stats.get("Volume"),
    }]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

def load_backtest_statistics(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPStatistics"
    bt_stats = data["backtest"].get("statistics", {})

    rows_to_insert = [{
        "statisticId": f"{data['backtest'].get('backtestId')}_stat",
        "backtestId": data["backtest"].get("backtestId"),
        "totalOrders": bt_stats.get("Total Orders"),
        "averageWin": bt_stats.get("Average Win"),
        "averageLoss": bt_stats.get("Average Loss"),
        "compoundingAnnualReturn": bt_stats.get("Compounding Annual Return"),
        "drawdown": bt_stats.get("Drawdown"),
        "expectancy": bt_stats.get("Expectancy"),
        "startEquity": bt_stats.get("Start Equity"),
        "endEquity": bt_stats.get("End Equity"),
        "netProfit": bt_stats.get("Net Profit"),
        "sharpeRatio": bt_stats.get("Sharpe Ratio"),
        "sortinoRatio": bt_stats.get("Sortino Ratio"),
        "probabilisticSharpeRatio": bt_stats.get("Probabilistic Sharpe Ratio"),
        "lossRate": bt_stats.get("Loss Rate"),
        "winRate": bt_stats.get("Win Rate"),
        "profitLossRatio": bt_stats.get("Profit-Loss Ratio"),
        "alpha": bt_stats.get("Alpha"),
        "beta": bt_stats.get("Beta"),
        "annualStandardDeviation": bt_stats.get("Annual Standard Deviation"),
        "annualVariance": bt_stats.get("Annual Variance"),
        "informationRatio": bt_stats.get("Information Ratio"),
        "totalFees": bt_stats.get("Total Fees"),
        "estimatedStrategyCapacity": bt_stats.get("Estimated Strategy Capacity"),
        "lowestCapacityAsset": bt_stats.get("Lowest Capacity Asset"),
        "portfolioTurnover": bt_stats.get("Portfolio Turnover"),
    }]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)
def load_total_performance(data, client, dataset_id):
    trade_table_id = f"{dataset_id}.BTOPTotalPerformanceTradeStats"
    portfolio_table_id = f"{dataset_id}.BTOPTotalPerformancePortfolioStats"
    closed_trades_table_id = f"{dataset_id}.BTOPTotalPerformanceClosedTrades"

    total_performance = data["backtest"].get("totalPerformance")
    if total_performance:
        trade_rows = [{
            "tradeStatId": f"{data['backtest'].get('backtestId')}_tp_trade",
            "backtestId": data["backtest"].get("backtestId"),
            "startDateTime": total_performance["tradeStatistics"].get("startDateTime"),
            "endDateTime": total_performance["tradeStatistics"].get("endDateTime"),
            "totalNumberOfTrades": total_performance["tradeStatistics"].get("totalNumberOfTrades"),
            "numberOfWinningTrades": total_performance["tradeStatistics"].get("numberOfWinningTrades"),
            "numberOfLosingTrades": total_performance["tradeStatistics"].get("numberOfLosingTrades"),
            "totalProfitLoss": total_performance["tradeStatistics"].get("totalProfitLoss"),
            "totalProfit": total_performance["tradeStatistics"].get("totalProfit"),
            "totalLoss": total_performance["tradeStatistics"].get("totalLoss"),
            "largestProfit": total_performance["tradeStatistics"].get("largestProfit"),
            "largestLoss": total_performance["tradeStatistics"].get("largestLoss"),
            "averageProfitLoss": total_performance["tradeStatistics"].get("averageProfitLoss"),
            "averageProfit": total_performance["tradeStatistics"].get("averageProfit"),
            "averageLoss": total_performance["tradeStatistics"].get("averageLoss"),
            "averageTradeDuration": total_performance["tradeStatistics"].get("averageTradeDuration"),
            "averageWinningTradeDuration": total_performance["tradeStatistics"].get("averageWinningTradeDuration"),
            "averageLosingTradeDuration": total_performance["tradeStatistics"].get("averageLosingTradeDuration"),
            "medianTradeDuration": total_performance["tradeStatistics"].get("medianTradeDuration"),
            "medianWinningTradeDuration": total_performance["tradeStatistics"].get("medianWinningTradeDuration"),
            "medianLosingTradeDuration": total_performance["tradeStatistics"].get("medianLosingTradeDuration"),
            "maxConsecutiveWinningTrades": total_performance["tradeStatistics"].get("maxConsecutiveWinningTrades"),
            "maxConsecutiveLosingTrades": total_performance["tradeStatistics"].get("maxConsecutiveLosingTrades"),
            "profitLossRatio": total_performance["tradeStatistics"].get("profitLossRatio"),
            "winLossRatio": total_performance["tradeStatistics"].get("winLossRatio"),
            "winRate": total_performance["tradeStatistics"].get("winRate"),
            "lossRate": total_performance["tradeStatistics"].get("lossRate"),
            "averageMAE": total_performance["tradeStatistics"].get("averageMAE"),
            "averageMFE": total_performance["tradeStatistics"].get("averageMFE"),
            "largestMAE": total_performance["tradeStatistics"].get("largestMAE"),
            "largestMFE": total_performance["tradeStatistics"].get("largestMFE"),
            "maximumClosedTradeDrawdown": total_performance["tradeStatistics"].get("maximumClosedTradeDrawdown"),
            "maximumIntraTradeDrawdown": total_performance["tradeStatistics"].get("maximumIntraTradeDrawdown"),
            "profitLossStandardDeviation": total_performance["tradeStatistics"].get("profitLossStandardDeviation"),
            "profitLossDownsideDeviation": total_performance["tradeStatistics"].get("profitLossDownsideDeviation"),
            "profitFactor": total_performance["tradeStatistics"].get("profitFactor"),
            "sharpeRatio": total_performance["tradeStatistics"].get("sharpeRatio"),
            "sortinoRatio": total_performance["tradeStatistics"].get("sortinoRatio"),
            "profitToMaxDrawdownRatio": total_performance["tradeStatistics"].get("profitToMaxDrawdownRatio"),
            "maximumEndTradeDrawdown": total_performance["tradeStatistics"].get("maximumEndTradeDrawdown"),
            "averageEndTradeDrawdown": total_performance["tradeStatistics"].get("averageEndTradeDrawdown"),
            "maximumDrawdownDuration": total_performance["tradeStatistics"].get("maximumDrawdownDuration"),
            "totalFees": total_performance["tradeStatistics"].get("totalFees"),
        }] if total_performance.get("tradeStatistics") else []

        portfolio_rows = [{
            "portfolioStatId": f"{data['backtest'].get('backtestId')}_tp_portfolio",
            "backtestId": data["backtest"].get("backtestId"),
            "averageWinRate": total_performance["portfolioStatistics"].get("averageWinRate"),
            "averageLossRate": total_performance["portfolioStatistics"].get("averageLossRate"),
            "profitLossRatio": total_performance["portfolioStatistics"].get("profitLossRatio"),
            "winRate": total_performance["portfolioStatistics"].get("winRate"),
            "lossRate": total_performance["portfolioStatistics"].get("lossRate"),
            "expectancy": total_performance["portfolioStatistics"].get("expectancy"),
            "startEquity": total_performance["portfolioStatistics"].get("startEquity"),
            "endEquity": total_performance["portfolioStatistics"].get("endEquity"),
            "compoundingAnnualReturn": total_performance["portfolioStatistics"].get("compoundingAnnualReturn"),
            "drawdown": total_performance["portfolioStatistics"].get("drawdown"),
            "totalNetProfit": total_performance["portfolioStatistics"].get("totalNetProfit"),
            "sharpeRatio": total_performance["portfolioStatistics"].get("sharpeRatio"),
            "probabilisticSharpeRatio": total_performance["portfolioStatistics"].get("probabilisticSharpeRatio"),
            "sortinoRatio": total_performance["portfolioStatistics"].get("sortinoRatio"),
            "alpha": total_performance["portfolioStatistics"].get("alpha"),
            "beta": total_performance["portfolioStatistics"].get("beta"),
            "annualStandardDeviation": total_performance["portfolioStatistics"].get("annualStandardDeviation"),
            "annualVariance": total_performance["portfolioStatistics"].get("annualVariance"),
            "informationRatio": total_performance["portfolioStatistics"].get("informationRatio"),
            "trackingError": total_performance["portfolioStatistics"].get("trackingError"),
            "treynorRatio": total_performance["portfolioStatistics"].get("treynorRatio"),
            "portfolioTurnover": total_performance["portfolioStatistics"].get("portfolioTurnover"),
            "valueAtRisk99": total_performance["portfolioStatistics"].get("valueAtRisk99"),
            "valueAtRisk95": total_performance["portfolioStatistics"].get("valueAtRisk95"),
        }] if total_performance.get("portfolioStatistics") else []

        closed_trades = total_performance.get("closedTrades", [])
        closed_trades_rows = [
            {
                "tradeId": f"{data['backtest'].get('backtestId')}_ct_{i}",
                "backtestId": data["backtest"].get("backtestId"),

                # Symbol details
                "symbol": {
                    "value": t["symbol"].get("value") if t.get("symbol") else None,
                    "id": t["symbol"].get("id") if t.get("symbol") else None,
                    "permtick": t["symbol"].get("permtick") if t.get("symbol") else None,
                    "underlying": {
                        "value": t["symbol"]["underlying"].get("value") if t.get("symbol") and t["symbol"].get("underlying") else None,
                        "id": t["symbol"]["underlying"].get("id") if t.get("symbol") and t["symbol"].get("underlying") else None,
                        "permtick": t["symbol"]["underlying"].get("permtick") if t.get("symbol") and t["symbol"].get("underlying") else None,
                    } if t.get("symbol") and t["symbol"].get("underlying") else None
                } if t.get("symbol") else None,

                # Trade fields
                "entryTime": t.get("entryTime"),
                "entryPrice": t.get("entryPrice"),
                "direction": t.get("direction"),
                "quantity": t.get("quantity"),
                "exitTime": t.get("exitTime"),
                "exitPrice": t.get("exitPrice"),
                "profitLoss": t.get("profitLoss"),
                "totalFees": t.get("totalFees"),
                "mae": t.get("mae"),
                "mfe": t.get("mfe"),
                "duration": t.get("duration"),
                "endTradeDrawdown": t.get("endTradeDrawdown"),
                "isWin": t.get("isWin")
            }
            for i, t in enumerate(closed_trades)
        ]

        if trade_rows:
            insert_rows_with_logging(client, trade_table_id, trade_rows)

        if portfolio_rows:
            insert_rows_with_logging(client, portfolio_table_id, portfolio_rows)

        if closed_trades_rows:
            insert_rows_with_logging(client, closed_trades_table_id, closed_trades_rows)

def load_errors(data, client, dataset_id):
    table_id = f"{dataset_id}.BTOPErrors"
    errors = data.get("errors", [])
    rows_to_insert = [{
        "errorId": f"{data['backtest'].get('backtestId')}_error_{i}",
        "backtestId": data["backtest"].get("backtestId"),
        "errorMessage": error
    } for i, error in enumerate(errors)]

    if rows_to_insert:
        insert_rows_with_logging(client, table_id, rows_to_insert)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset = "develop"

    backtest_results_dir = os.path.join(current_dir, "../Scripts/backtest_results")
    # We remove the rename logic from here because it is now done inside load_json_to_bigquery
    # when the file is already present or after successful insertion.

    # Iterate over all JSON files in the backtest_results directory
    for file_name in os.listdir(backtest_results_dir):
        time.sleep(1)
        if file_name.endswith(".json"):
            json_file = os.path.join(backtest_results_dir, file_name)
            # Run the data load, which also moves the file appropriately
            load_json_to_bigquery(json_file, dataset)
