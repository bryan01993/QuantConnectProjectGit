from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.Results
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Logging
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Concurrent
import System.Collections.Generic
import System.Threading


class BacktestProgressMonitor(System.Object):
    """Monitors and reports the progress of a backtest"""

    @property
    def total_days(self) -> int:
        """Gets the total days the algorithm will run"""
        ...

    @property
    def processed_days(self) -> int:
        """Gets the current days the algorithm has been running for"""
        ...

    @property
    def progress(self) -> float:
        """Gets the current progress of the backtest"""
        ...

    def __init__(self, timeKeeper: QuantConnect.Interfaces.ITimeKeeper, endUtcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Creates a new instance
        
        :param timeKeeper: The time keeper to use
        :param endUtcTime: The end UTC time
        """
        ...

    def invalidate_processed_days(self) -> None:
        """Invalidates the processed days count value so it gets recalculated next time it is needed"""
        ...


class ResultHandlerInitializeParameters(System.Object):
    """DTO parameters class to initialize a result handler"""

    @property
    def job(self) -> QuantConnect.Packets.AlgorithmNodePacket:
        """The algorithm job"""
        ...

    @property.setter
    def job(self, value: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        ...

    @property
    def messaging_handler(self) -> QuantConnect.Interfaces.IMessagingHandler:
        """The messaging handler"""
        ...

    @property.setter
    def messaging_handler(self, value: QuantConnect.Interfaces.IMessagingHandler) -> None:
        ...

    @property
    def api(self) -> QuantConnect.Interfaces.IApi:
        """The Api instance"""
        ...

    @property.setter
    def api(self, value: QuantConnect.Interfaces.IApi) -> None:
        ...

    @property
    def transaction_handler(self) -> QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler:
        """The transaction handler"""
        ...

    @property.setter
    def transaction_handler(self, value: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler) -> None:
        ...

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """The map file provider instance to use"""
        ...

    @property.setter
    def map_file_provider(self, value: QuantConnect.Interfaces.IMapFileProvider) -> None:
        ...

    def __init__(self, job: QuantConnect.Packets.AlgorithmNodePacket, messagingHandler: QuantConnect.Interfaces.IMessagingHandler, api: QuantConnect.Interfaces.IApi, transactionHandler: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider) -> None:
        """Creates a new instance"""
        ...


class BaseResultsHandler(System.Object, metaclass=abc.ABCMeta):
    """Provides base functionality to the implementations of IResultHandler"""

    STRATEGY_EQUITY_KEY: str = "Strategy Equity"
    """String message saying: Strategy Equity"""

    EQUITY_KEY: str = "Equity"
    """String message saying: Equity"""

    RETURN_KEY: str = "Return"
    """String message saying: Return"""

    BENCHMARK_KEY: str = "Benchmark"
    """String message saying: Benchmark"""

    DRAWDOWN_KEY: str = "Drawdown"
    """String message saying: Drawdown"""

    PORTFOLIO_TURNOVER_KEY: str = "Portfolio Turnover"
    """String message saying: PortfolioTurnover"""

    PORTFOLIO_MARGIN_KEY: str = "Portfolio Margin"
    """String message saying: Portfolio Margin"""

    ASSETS_SALES_VOLUME_KEY: str = "Assets Sales Volume"
    """String message saying: Portfolio Margin"""

    @property
    def main_update_interval(self) -> datetime.timedelta:
        """
        The main loop update interval
        
        This property is protected.
        """
        ...

    @property
    def chart_update_interval(self) -> datetime.timedelta:
        """
        The chart update interval
        
        This property is protected.
        """
        ...

    @property.setter
    def chart_update_interval(self, value: datetime.timedelta) -> None:
        ...

    @property
    def last_delta_order_position(self) -> int:
        """
        The last position consumed from the ITransactionHandler.OrderEvents by GetDeltaOrders
        
        This property is protected.
        """
        ...

    @property.setter
    def last_delta_order_position(self, value: int) -> None:
        ...

    @property
    def last_delta_order_events_position(self) -> int:
        """
        The last position consumed from the ITransactionHandler.OrderEvents while determining delta order events
        
        This property is protected.
        """
        ...

    @property.setter
    def last_delta_order_events_position(self, value: int) -> None:
        ...

    @property
    def serializer_settings(self) -> typing.Any:
        """
        Serializer settings to use
        
        This property is protected.
        """
        ...

    @property.setter
    def serializer_settings(self, value: typing.Any) -> None:
        ...

    @property
    def current_algorithm_equity(self) -> QuantConnect.Data.Market.Bar:
        """
        The current aggregated equity bar for sampling.
        It will be aggregated with values from the GetPortfolioValue
        
        This property is protected.
        """
        ...

    @property.setter
    def current_algorithm_equity(self, value: QuantConnect.Data.Market.Bar) -> None:
        ...

    @property
    def is_active(self) -> bool:
        """Boolean flag indicating the thread is still active."""
        ...

    @property
    def messages(self) -> System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Packets.Packet]:
        """Live packet messaging queue. Queue the messages here and send when the result queue is ready."""
        ...

    @property.setter
    def messages(self, value: System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Packets.Packet]) -> None:
        ...

    @property
    def charts(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, QuantConnect.Chart]:
        """Storage for the price and equity charts of the live results."""
        ...

    @property.setter
    def charts(self, value: System.Collections.Concurrent.ConcurrentDictionary[str, QuantConnect.Chart]) -> None:
        ...

    @property
    def exit_triggered(self) -> bool:
        """
        True if the exit has been triggered
        
        This field is protected.
        """
        ...

    @property
    def exit_event(self) -> System.Threading.ManualResetEvent:
        """
        Event set when exit is triggered
        
        This property is protected.
        """
        ...

    @property
    def log_store(self) -> System.Collections.Generic.List[QuantConnect.Logging.LogEntry]:
        """
        The log store instance
        
        This property is protected.
        """
        ...

    @property
    def algorithm_performance_charts(self) -> System.Collections.Generic.List[str]:
        """
        Algorithms performance related chart names
        
        This property is protected.
        """
        ...

    @property
    def chart_lock(self) -> System.Object:
        """
        Lock to be used when accessing the chart collection
        
        This property is protected.
        """
        ...

    @property
    def project_id(self) -> int:
        """
        The algorithm project id
        
        This property is protected.
        """
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def ram_allocation(self) -> str:
        """
        The maximum amount of RAM (in MB) this algorithm is allowed to utilize
        
        This property is protected.
        """
        ...

    @property.setter
    def ram_allocation(self, value: str) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """
        The algorithm unique compilation id
        
        This property is protected.
        """
        ...

    @property.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """
        The algorithm job id.
        This is the deploy id for live, backtesting id for backtesting
        
        This property is protected.
        """
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def start_time(self) -> datetime.datetime:
        """
        The result handler start time
        
        This property is protected.
        """
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.Dictionary[str, str]:
        """
        Customizable dynamic statistics IAlgorithm.RuntimeStatistics
        
        This property is protected.
        """
        ...

    @property
    def state(self) -> System.Collections.Generic.Dictionary[str, str]:
        """
        State of the algorithm
        
        This property is protected.
        """
        ...

    @property.setter
    def state(self, value: System.Collections.Generic.Dictionary[str, str]) -> None:
        ...

    @property
    def messaging_handler(self) -> QuantConnect.Interfaces.IMessagingHandler:
        """
        The handler responsible for communicating messages to listeners
        
        This property is protected.
        """
        ...

    @property.setter
    def messaging_handler(self, value: QuantConnect.Interfaces.IMessagingHandler) -> None:
        ...

    @property
    def transaction_handler(self) -> QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler:
        """
        The transaction handler used to get the algorithms Orders information
        
        This property is protected.
        """
        ...

    @property.setter
    def transaction_handler(self, value: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler) -> None:
        ...

    @property
    def starting_portfolio_value(self) -> float:
        """
        The algorithms starting portfolio value.
        Used to calculate the portfolio return
        
        This property is protected.
        """
        ...

    @property.setter
    def starting_portfolio_value(self, value: float) -> None:
        ...

    @property
    def algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        The algorithm instance
        
        This property is protected.
        """
        ...

    @property.setter
    def algorithm(self, value: QuantConnect.Interfaces.IAlgorithm) -> None:
        ...

    @property
    def algorithm_currency_symbol(self) -> str:
        """
        Algorithm currency symbol, used in charting
        
        This property is protected.
        """
        ...

    @property.setter
    def algorithm_currency_symbol(self, value: str) -> None:
        ...

    @property
    def daily_portfolio_value(self) -> float:
        """
        Closing portfolio value. Used to calculate daily performance.
        
        This property is protected.
        """
        ...

    @property.setter
    def daily_portfolio_value(self, value: float) -> None:
        ...

    @property
    def cumulative_max_portfolio_value(self) -> float:
        """
        Cumulative max portfolio value. Used to calculate drawdown underwater.
        
        This property is protected.
        """
        ...

    @property.setter
    def cumulative_max_portfolio_value(self, value: float) -> None:
        ...

    @property
    def resample_period(self) -> datetime.timedelta:
        """
        Sampling period for timespans between resamples of the charting equity.
        
        This property is protected.
        """
        ...

    @property.setter
    def resample_period(self, value: datetime.timedelta) -> None:
        ...

    @property
    def notification_period(self) -> datetime.timedelta:
        """
        How frequently the backtests push messages to the browser.
        
        This property is protected.
        """
        ...

    @property.setter
    def notification_period(self, value: datetime.timedelta) -> None:
        ...

    @property
    def results_destination_folder(self) -> str:
        """
        Directory location to store results
        
        This property is protected.
        """
        ...

    @property.setter
    def results_destination_folder(self, value: str) -> None:
        ...

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """
        The map file provider instance to use
        
        This property is protected.
        """
        ...

    @property.setter
    def map_file_provider(self, value: QuantConnect.Interfaces.IMapFileProvider) -> None:
        ...

    def __init__(self) -> None:
        """
        Creates a new instance
        
        This method is protected.
        """
        ...

    def add_to_log_store(self, message: str) -> None:
        """
        Save an algorithm message to the log store. Uses a different timestamped method of adding messaging to interweve debug and logging messages.
        
        This method is protected.
        
        :param message: String message to store
        """
        ...

    def exit(self) -> None:
        """Terminate the result thread and apply any required exit procedures like sending final results"""
        ...

    @overload
    def generate_statistics_results(self, charts: System.Collections.Generic.Dictionary[str, QuantConnect.Chart], profit_loss: System.Collections.Generic.SortedDictionary[datetime.datetime, float] = None, estimated_strategy_capacity: QuantConnect.CapacityEstimate = None) -> QuantConnect.Statistics.StatisticsResults:
        """
        Will generate the statistics results and update the provided runtime statistics
        
        This method is protected.
        """
        ...

    @overload
    def generate_statistics_results(self, estimated_strategy_capacity: QuantConnect.CapacityEstimate = None) -> QuantConnect.Statistics.StatisticsResults:
        """
        Calculates and gets the current statistics for the algorithm.
        It will use the current Charts and profit loss information calculated from the current transaction record
        to generate the results.
        
        This method is protected.
        
        :returns: The current statistics.
        """
        ...

    def get_algorithm_runtime_statistics(self, summary: System.Collections.Generic.Dictionary[str, str], capacity_estimate: QuantConnect.CapacityEstimate = None) -> System.Collections.Generic.SortedDictionary[str, str]:
        """
        Gets the algorithm runtime statistics
        
        This method is protected.
        """
        ...

    def get_algorithm_state(self, end_time: typing.Optional[datetime.datetime] = None) -> System.Collections.Generic.Dictionary[str, str]:
        """
        Gets the algorithm state data
        
        This method is protected.
        """
        ...

    def get_benchmark_value(self, time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the current benchmark value
        
        This method is protected.
        
        :param time: Time to resolve benchmark value at
        """
        ...

    def get_delta_orders(self, order_events_start_position: int, should_stop: typing.Callable[[int], bool]) -> System.Collections.Generic.Dictionary[int, QuantConnect.Orders.Order]:
        """
        Gets the orders generated starting from the provided ITransactionHandler.OrderEvents position
        
        This method is protected.
        
        :returns: The delta orders.
        """
        ...

    def get_net_return(self) -> float:
        """
        Gets the algorithm net return
        
        This method is protected.
        """
        ...

    def get_portfolio_value(self) -> float:
        """
        Gets the current portfolio value
        
        This method is protected.
        """
        ...

    def get_results_path(self, filename: str) -> str:
        """
        Gets the full path for a results file
        
        This method is protected.
        
        :param filename: The filename to add to the path
        :returns: The full path, including the filename.
        """
        ...

    def get_server_statistics(self, utc_now: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.Dictionary[str, str]:
        """
        Gets the current Server statistics
        
        This method is protected.
        """
        ...

    def initialize(self, parameters: QuantConnect.Lean.Engine.Results.ResultHandlerInitializeParameters) -> None:
        """
        Initialize the result handler with this result packet.
        
        :param parameters: DTO parameters class to initialize a result handler
        """
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Event fired each time that we add/remove securities from the data feed"""
        ...

    def order_event(self, new_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        New order event for the algorithm
        
        :param new_event: New event details
        """
        ...

    def process_algorithm_logs(self, message_queue_limit: typing.Optional[int] = None) -> None:
        """
        Processes algorithm logs.
        Logs of the same type are batched together one per line and are sent out
        
        This method is protected.
        """
        ...

    def purge_queue(self) -> None:
        """
        Purge/clear any outstanding messages in message queue.
        
        This method is protected.
        """
        ...

    def run(self) -> None:
        """
        Result handler update method
        
        This method is protected.
        """
        ...

    @overload
    def sample(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Samples portfolio equity, benchmark, and daily performance
        Called by scheduled event every night at midnight algorithm time
        
        :param time: Current UTC time in the AlgorithmManager loop
        """
        ...

    @overload
    def sample(self, chart_name: str, series_name: str, series_index: int, series_type: QuantConnect.SeriesType, value: QuantConnect.ISeriesPoint, unit: str = "$") -> None:
        """
        Add a sample to the chart specified by the chart_name, and series_name.
        
        This method is protected.
        
        :param chart_name: String chart name to place the sample.
        :param series_name: Series name for the chart.
        :param series_index: Series chart index - which chart should this series belong
        :param series_type: Series type for the chart.
        :param value: Value for the chart sample.
        :param unit: Unit for the chart axis
        """
        ...

    def sample_benchmark(self, time: typing.Union[datetime.datetime, datetime.date], value: float) -> None:
        """
        Sample the current benchmark performance directly with a time-value pair.
        
        This method is protected.
        
        :param time: Time of the sample.
        :param value: Current benchmark value.
        """
        ...

    def sample_capacity(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sample estimated strategy capacity
        
        This method is protected.
        
        :param time: Time of the sample
        """
        ...

    def sample_drawdown(self, time: typing.Union[datetime.datetime, datetime.date], current_portfolio_value: float) -> None:
        """
        Sample drawdown of equity of the strategy
        
        This method is protected.
        
        :param time: Time of the sample
        :param current_portfolio_value: Current equity value
        """
        ...

    def sample_equity(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sample the current equity of the strategy directly with time and using
        the current algorithm equity value in CurrentAlgorithmEquity
        
        This method is protected.
        
        :param time: Equity candlestick end time
        """
        ...

    def sample_exposure(self, time: typing.Union[datetime.datetime, datetime.date], current_portfolio_value: float) -> None:
        """
        Sample portfolio exposure long/short ratios by security type
        
        This method is protected.
        
        :param time: Time of the sample
        :param current_portfolio_value: Current value of the portfolio
        """
        ...

    def sample_performance(self, time: typing.Union[datetime.datetime, datetime.date], value: float) -> None:
        """
        Sample the current daily performance directly with a time-value pair.
        
        This method is protected.
        
        :param time: Time of the sample.
        :param value: Current daily performance value.
        """
        ...

    def sample_portfolio_turnover(self, time: typing.Union[datetime.datetime, datetime.date], current_portfolio_value: float) -> None:
        """
        Sample portfolio turn over of the strategy
        
        This method is protected.
        
        :param time: Time of the sample
        :param current_portfolio_value: Current equity value
        """
        ...

    def sample_sales_volume(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sample assets sales volume
        
        This method is protected.
        
        :param time: Time of the sample
        """
        ...

    def save_logs(self, id: str, logs: System.Collections.Generic.List[QuantConnect.Logging.LogEntry]) -> str:
        """
        Returns the location of the logs
        
        :param id: Id that will be incorporated into the algorithm log name
        :param logs: The logs to save
        :returns: The path to the logs.
        """
        ...

    def save_results(self, name: str, result: QuantConnect.Result) -> None:
        """
        Save the results to disk
        
        :param name: The name of the results
        :param result: The results to save
        """
        ...

    def set_algorithm_state(self, error: str, stack: str) -> None:
        """
        Sets the algorithm state data
        
        This method is protected.
        """
        ...

    def stop_update_runner(self) -> None:
        """
        Stops the update runner task
        
        This method is protected.
        """
        ...

    def store_insights(self) -> None:
        """
        Save insight results to persistent storage
        
        This method is protected.
        """
        ...

    def store_order_events(self, utc_time: typing.Union[datetime.datetime, datetime.date], order_events: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]) -> None:
        """
        Stores the order events
        
        This method is protected.
        
        :param utc_time: The utc date associated with these order events
        :param order_events: The order events to store
        """
        ...

    def store_result(self, packet: QuantConnect.Packets.Packet) -> None:
        """
        Save the snapshot of the total results to storage.
        
        This method is protected.
        
        :param packet: Packet to store.
        """
        ...

    def summary_statistic(self, name: str, value: str) -> None:
        """
        Sets or updates a custom summary statistic
        
        This method is protected.
        
        :param name: The statistic name
        :param value: The statistic value
        """
        ...

    def total_trades_count(self) -> int:
        """
        Helper method to get the total trade count statistic
        
        This method is protected.
        """
        ...

    def update_algorithm_equity(self) -> None:
        """
        Updates the current equity bar with the current equity value from GetPortfolioValue
        
        This method is protected.
        """
        ...


class IResultHandler(QuantConnect.Statistics.IStatisticsService, metaclass=abc.ABCMeta):
    """
    Handle the results of the backtest: where should we send the profit, portfolio updates:
    Backtester or the Live trading platform:
    """

    @property
    @abc.abstractmethod
    def messages(self) -> System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Packets.Packet]:
        """Put messages to process into the queue so they are processed by this thread."""
        ...

    @property.setter
    def messages(self, value: System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Packets.Packet]) -> None:
        ...

    @property
    @abc.abstractmethod
    def is_active(self) -> bool:
        """
        Boolean flag indicating the result hander thread is busy.
        False means it has completely finished and ready to dispose.
        """
        ...

    def algorithm_name_updated(self, name: str) -> None:
        """
        Handles updates to the algorithm's name
        
        :param name: The new name
        """
        ...

    def algorithm_tags_updated(self, tags: System.Collections.Generic.HashSet[str]) -> None:
        """
        Handles updates to the algorithm's tags
        
        :param tags: The new tags
        """
        ...

    def brokerage_message(self, brokerage_message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Process brokerage message events
        
        :param brokerage_message_event: The brokerage message event
        """
        ...

    def debug_message(self, message: str) -> None:
        """
        Process debug messages with the preconfigured settings.
        
        :param message: String debug message
        """
        ...

    def error_message(self, error: str, stacktrace: str = ...) -> None:
        """
        Send an error message back to the browser highlighted in red with a stacktrace.
        
        :param error: Error message we'd like shown in console.
        :param stacktrace: Stacktrace information string
        """
        ...

    def exit(self) -> None:
        """Terminate the result thread and apply any required exit procedures like sending final results."""
        ...

    def initialize(self, parameters: QuantConnect.Lean.Engine.Results.ResultHandlerInitializeParameters) -> None:
        """
        Initialize the result handler with this result packet.
        
        :param parameters: DTO parameters class to initialize a result handler
        """
        ...

    def log_message(self, message: str) -> None:
        """
        Send a logging message to the log list for storage.
        
        :param message: Message we'd in the log.
        """
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Event fired each time that we add/remove securities from the data feed"""
        ...

    def order_event(self, new_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Send a new order event.
        
        :param new_event: Update, processing or cancellation of an order, update the IDE in live mode or ignore in backtesting.
        """
        ...

    def process_synchronous_events(self, force_process: bool = False) -> None:
        """Process any synchronous events in here that are primarily triggered from the algorithm loop"""
        ...

    def runtime_error(self, message: str, stacktrace: str = ...) -> None:
        """
        Send a runtime error message back to the browser highlighted with in red
        
        :param message: Error message.
        :param stacktrace: Stacktrace information string
        """
        ...

    def runtime_statistic(self, key: str, value: str) -> None:
        """
        Set a dynamic runtime statistic to show in the (live) algorithm header
        
        :param key: Runtime headline statistic name
        :param value: Runtime headline statistic value
        """
        ...

    def sample(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Method to update the IResultHandler with various performance metrics.
        Called once a day by scheduled event in AlgorithmManager
        
        :param time: Current time
        """
        ...

    def save_results(self, name: str, result: QuantConnect.Result) -> None:
        """
        Save the results
        
        :param name: The name of the results
        :param result: The results to save
        """
        ...

    def security_type(self, types: System.Collections.Generic.List[QuantConnect.SecurityType]) -> None:
        """
        Send a list of security types to the browser
        
        :param types: Security types list inside algorithm
        """
        ...

    def send_status_update(self, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """
        Send a algorithm status update to the user of the algorithms running state.
        
        :param status: Status enum of the algorithm.
        :param message: Optional string message describing reason for status change.
        """
        ...

    def set_algorithm(self, algorithm: QuantConnect.Interfaces.IAlgorithm, starting_portfolio_value: float) -> None:
        """
        Set the algorithm of the result handler after its been initialized.
        
        :param algorithm: Algorithm object matching IAlgorithm interface
        :param starting_portfolio_value: Algorithm starting capital for statistics calculations
        """
        ...

    def system_debug_message(self, message: str) -> None:
        """
        Process system debug messages with the preconfigured settings.
        
        :param message: String debug message
        """
        ...


class BacktestingResultHandler(QuantConnect.Lean.Engine.Results.BaseResultsHandler, QuantConnect.Lean.Engine.Results.IResultHandler):
    """Backtesting result handler passes messages back from the Lean to the User."""

    @property
    def final_statistics(self) -> System.Collections.Generic.Dictionary[str, str]:
        """A dictionary containing summary statistics"""
        ...

    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    def add_to_log_store(self, message: str) -> None:
        """
        Add message to LogStore
        
        This method is protected.
        
        :param message: Message to add
        """
        ...

    def algorithm_name_updated(self, name: str) -> None:
        """
        Handles updates to the algorithm's name
        
        :param name: The new name
        """
        ...

    def algorithm_tags_updated(self, tags: System.Collections.Generic.HashSet[str]) -> None:
        """
        Sends a packet communicating an update to the algorithm's tags
        
        :param tags: The new tags
        """
        ...

    def brokerage_message(self, brokerage_message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Process brokerage message events
        
        :param brokerage_message_event: The brokerage message event
        """
        ...

    def configure_console_text_writer(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Configures the Console.Out and Console.ErrorTextWriter
        instances. By default, we forward Console.WriteLine(string) to IAlgorithm.Debug.
        This is perfect for running in the cloud, but since they're processed asynchronously, the ordering of these
        messages with respect to Log messages is broken. This can lead to differences in regression
        test logs based solely on the ordering of messages. To disable this forwarding, set "forward-console-messages"
        to false in the configuration.
        
        This method is protected.
        """
        ...

    def debug_message(self, message: str) -> None:
        """
        Send a debug message back to the browser console.
        
        :param message: Message we'd like shown in console.
        """
        ...

    def error_message(self, message: str, stacktrace: str = ...) -> None:
        """
        Send an error message back to the browser highlighted in red with a stacktrace.
        
        :param message: Error message we'd like shown in console.
        :param stacktrace: Stacktrace information string
        """
        ...

    def exit(self) -> None:
        """Terminate the result thread and apply any required exit procedures like sending final results."""
        ...

    def initialize(self, parameters: QuantConnect.Lean.Engine.Results.ResultHandlerInitializeParameters) -> None:
        """Initialize the result handler with this result packet."""
        ...

    def log_message(self, message: str) -> None:
        """
        Send a logging message to the log list for storage.
        
        :param message: Message we'd in the log.
        """
        ...

    def order_event(self, new_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Handle order event
        
        :param new_event: Event to process
        """
        ...

    def process_synchronous_events(self, force_process: bool = False) -> None:
        """
        Process the synchronous result events, sampling and message reading.
        This method is triggered from the algorithm manager thread.
        """
        ...

    def run(self) -> None:
        """
        The main processing method steps through the messaging queue and processes the messages one by one.
        
        This method is protected.
        """
        ...

    def runtime_error(self, message: str, stacktrace: str = ...) -> None:
        """
        Send a runtime error message back to the browser highlighted with in red
        
        :param message: Error message.
        :param stacktrace: Stacktrace information string
        """
        ...

    def runtime_statistic(self, key: str, value: str) -> None:
        """
        Set the current runtime statistics of the algorithm.
        These are banner/title statistics which show at the top of the live trading results.
        
        :param key: Runtime headline statistic name
        :param value: Runtime headline statistic value
        """
        ...

    def sample(self, chart_name: str, series_name: str, series_index: int, series_type: QuantConnect.SeriesType, value: QuantConnect.ISeriesPoint, unit: str = "$") -> None:
        """
        Add a sample to the chart specified by the chart_name, and series_name.
        
        This method is protected.
        
        :param chart_name: String chart name to place the sample.
        :param series_name: Series name for the chart.
        :param series_index: Type of chart we should create if it doesn't already exist.
        :param series_type: Series type for the chart.
        :param value: Value for the chart sample.
        :param unit: Unit of the sample
        """
        ...

    def sample_capacity(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sample estimated strategy capacity
        
        This method is protected.
        
        :param time: Time of the sample
        """
        ...

    def sample_range(self, updates: System.Collections.Generic.IEnumerable[QuantConnect.Chart]) -> None:
        """
        Add a range of samples from the users algorithms to the end of our current list.
        
        This method is protected.
        
        :param updates: Chart updates since the last request.
        """
        ...

    def security_type(self, types: System.Collections.Generic.List[QuantConnect.SecurityType]) -> None:
        """Send list of security asset types the algorithm uses to browser."""
        ...

    def send_final_result(self) -> None:
        """
        Send a final analysis result back to the IDE.
        
        This method is protected.
        """
        ...

    def send_status_update(self, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """
        Send an algorithm status update to the browser.
        
        :param status: Status enum value.
        :param message: Additional optional status message.
        """
        ...

    def set_algorithm(self, algorithm: QuantConnect.Interfaces.IAlgorithm, starting_portfolio_value: float) -> None:
        """
        Set the Algorithm instance for ths result.
        
        :param algorithm: Algorithm we're working on.
        :param starting_portfolio_value: Algorithm starting capital for statistics calculations
        """
        ...

    def set_summary_statistic(self, name: str, value: str) -> None:
        """
        Sets or updates a custom summary statistic
        
        :param name: The statistic name
        :param value: The statistic value
        """
        ...

    def split_packets(self, delta_charts: System.Collections.Generic.Dictionary[str, QuantConnect.Chart], delta_orders: System.Collections.Generic.Dictionary[int, QuantConnect.Orders.Order], runtime_statistics: System.Collections.Generic.SortedDictionary[str, str], progress: float, server_statistics: System.Collections.Generic.Dictionary[str, str]) -> System.Collections.Generic.IEnumerable[QuantConnect.Packets.BacktestResultPacket]:
        """Run over all the data and break it into smaller packets to ensure they all arrive at the terminal"""
        ...

    def statistics_results(self) -> QuantConnect.Statistics.StatisticsResults:
        """
        Calculates and gets the current statistics for the algorithm
        
        :returns: The current statistics.
        """
        ...

    def store_result(self, packet: QuantConnect.Packets.Packet) -> None:
        """
        Save the snapshot of the total results to storage.
        
        This method is protected.
        
        :param packet: Packet to store.
        """
        ...

    def system_debug_message(self, message: str) -> None:
        """
        Send a system debug message back to the browser console.
        
        :param message: Message we'd like shown in console.
        """
        ...


class RegressionResultHandler(QuantConnect.Lean.Engine.Results.BacktestingResultHandler):
    """
    Provides a wrapper over the BacktestingResultHandler that logs all order events
    to a separate file
    """

    @property
    def log_file_path(self) -> str:
        """Gets the path used for logging all portfolio changing events, such as orders, TPV, daily holdings values"""
        ...

    @property
    def has_runtime_error(self) -> bool:
        """True if there was a runtime error running the algorithm"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the RegressionResultHandler class"""
        ...

    def add_to_log_store(self, message: str) -> None:
        """
        Save an algorithm message to the log store. Uses a different timestamped method of adding messaging to interweve debug and logging messages.
        
        This method is protected.
        
        :param message: String message to store
        """
        ...

    def configure_console_text_writer(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        We want to make algorithm messages end up in both the standard regression log file {algorithm}.{language}.log
        as well as the details log {algorithm}.{language}.details.log. The details log is focused on providing a log
        dedicated solely to the algorithm's behavior, void of all QuantConnect.Logging.Log messages
        
        This method is protected.
        """
        ...

    def debug_message(self, message: str) -> None:
        """
        Send a debug message back to the browser console.
        
        :param message: Message we'd like shown in console.
        """
        ...

    def error_message(self, message: str, stacktrace: str = ...) -> None:
        """
        Send an error message back to the browser highlighted in red with a stacktrace.
        
        :param message: Error message we'd like shown in console.
        :param stacktrace: Stacktrace information string
        """
        ...

    def exit(self) -> None:
        """
        Terminate the result thread and apply any required exit procedures.
        Save orders log files to disk.
        """
        ...

    def log_message(self, message: str) -> None:
        """
        Send a logging message to the log list for storage.
        
        :param message: Message we'd in the log.
        """
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Event fired each time that we add/remove securities from the data feed"""
        ...

    def order_event(self, new_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Log the order and order event to the dedicated log file for this regression algorithm
        
        :param new_event: New order event details
        """
        ...

    def process_synchronous_events(self, force_process: bool = False) -> None:
        """
        Runs at the end of each time loop. When HighFidelityLogging is enabled, we'll
        log each piece of data to allow for faster determination of regression causes
        """
        ...

    def runtime_error(self, message: str, stacktrace: str = ...) -> None:
        """
        Send a runtime error message back to the browser highlighted with in red
        
        :param message: Error message.
        :param stacktrace: Stacktrace information string
        """
        ...

    def runtime_statistic(self, key: str, value: str) -> None:
        """
        Set the current runtime statistics of the algorithm.
        These are banner/title statistics which show at the top of the live trading results.
        
        :param key: Runtime headline statistic name
        :param value: Runtime headline statistic value
        """
        ...

    def sample_performance(self, time: typing.Union[datetime.datetime, datetime.date], value: float) -> None:
        """
        Runs on date changes, use this to log TPV and holdings values each day
        
        This method is protected.
        """
        ...

    def save_results(self, name: str, result: QuantConnect.Result) -> None:
        """Save the results to disk"""
        ...

    def security_type(self, types: System.Collections.Generic.List[QuantConnect.SecurityType]) -> None:
        """Send list of security asset types the algortihm uses to browser."""
        ...

    def set_algorithm(self, algorithm: QuantConnect.Interfaces.IAlgorithm, starting_portfolio_value: float) -> None:
        """Initializes the stream writer using the algorithm's id (name) in the file path"""
        ...

    def system_debug_message(self, message: str) -> None:
        """
        Send a system debug message back to the browser console.
        
        :param message: Message we'd like shown in console.
        """
        ...


class LiveTradingResultHandler(QuantConnect.Lean.Engine.Results.BaseResultsHandler, QuantConnect.Lean.Engine.Results.IResultHandler):
    """Live trading result handler implementation passes the messages to the QC live trading interface."""

    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    def add_to_log_store(self, message: str) -> None:
        """
        Save an algorithm message to the log store. Uses a different timestamped method of adding messaging to interweve debug and logging messages.
        
        This method is protected.
        
        :param message: String message to send to browser.
        """
        ...

    def algorithm_name_updated(self, name: str) -> None:
        """
        Handles updates to the algorithm's name
        
        :param name: The new name
        """
        ...

    def algorithm_tags_updated(self, tags: System.Collections.Generic.HashSet[str]) -> None:
        """
        Handles updates to the algorithm's tags
        
        :param tags: The new tags
        """
        ...

    def brokerage_message(self, brokerage_message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Process brokerage message events
        
        :param brokerage_message_event: The brokerage message event
        """
        ...

    def create_safe_chart_name(self, chart_name: str) -> str:
        """
        Escape the chartname so that it can be saved to a file system
        
        This method is protected.
        
        :param chart_name: The name of a chart
        :returns: The name of the chart will all escape all characters except RFC 2396 unreserved characters.
        """
        ...

    def debug_message(self, message: str) -> None:
        """
        Send a live trading debug message to the live console.
        
        :param message: Message we'd like shown in console.
        """
        ...

    def error_message(self, message: str, stacktrace: str = ...) -> None:
        """
        Send an error message back to the browser console and highlight it read.
        
        :param message: Message we'd like shown in console.
        :param stacktrace: Stacktrace to show in the console.
        """
        ...

    def exit(self) -> None:
        """Terminate the result thread and apply any required exit procedures like sending final results"""
        ...

    def get_benchmark_value(self, time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the current benchmark value
        
        This method is protected.
        
        :param time: Time to resolve benchmark value at
        """
        ...

    @staticmethod
    def get_holdings(securities: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security], subscription_data_config_service: QuantConnect.Interfaces.ISubscriptionDataConfigService, only_invested: bool = False) -> System.Collections.Generic.Dictionary[str, QuantConnect.Holding]:
        """Helper method to fetch the algorithm holdings"""
        ...

    def get_portfolio_value(self) -> float:
        """
        Gets the current portfolio value
        
        This method is protected.
        """
        ...

    def initialize(self, parameters: QuantConnect.Lean.Engine.Results.ResultHandlerInitializeParameters) -> None:
        """
        Initialize the result handler with this result packet.
        
        :param parameters: DTO parameters class to initialize a result handler
        """
        ...

    def log_message(self, message: str) -> None:
        """
        Log string messages and send them to the console.
        
        :param message: String message wed like logged.
        """
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time that we add/remove securities from the data feed.
        On Security change we re determine when should we sample charts, if the user added Crypto, Forex or an extended market hours subscription
        we will always sample charts. Else, we will keep the exchange per market to query later on demand
        """
        ...

    def order_event(self, new_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        New order event for the algorithm
        
        :param new_event: New event details
        """
        ...

    def process_synchronous_events(self, force_process: bool = False) -> None:
        """
        Process the synchronous result events, sampling and message reading.
        This method is triggered from the algorithm manager thread.
        """
        ...

    def run(self) -> None:
        """
        Live trading result handler thread.
        
        This method is protected.
        """
        ...

    def runtime_error(self, message: str, stacktrace: str = ...) -> None:
        """
        Send a runtime error back to the users browser and highlight it red.
        
        :param message: Runtime error message
        :param stacktrace: Associated error stack trace.
        """
        ...

    def runtime_statistic(self, key: str, value: str) -> None:
        """
        Set a dynamic runtime statistic to show in the (live) algorithm header
        
        :param key: Runtime headline statistic name
        :param value: Runtime headline statistic value
        """
        ...

    @overload
    def sample(self, chart_name: str, series_name: str, series_index: int, series_type: QuantConnect.SeriesType, value: QuantConnect.ISeriesPoint, unit: str = "$") -> None:
        """
        Add a sample to the chart specified by the chart_name, and series_name.
        
        This method is protected.
        
        :param chart_name: String chart name to place the sample.
        :param series_name: Series name for the chart.
        :param series_index: Series chart index - which chart should this series belong
        :param series_type: Series type for the chart.
        :param value: Value for the chart sample.
        :param unit: Unit for the chart axis
        """
        ...

    @overload
    def sample(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Samples portfolio equity, benchmark, and daily performance
        
        :param time: Current UTC time in the AlgorithmManager loop
        """
        ...

    def sample_range(self, updates: System.Collections.Generic.IEnumerable[QuantConnect.Chart]) -> None:
        """
        Add a range of samples from the users algorithms to the end of our current list.
        
        This method is protected.
        
        :param updates: Chart updates since the last request.
        """
        ...

    def save_logs(self, id: str, logs: System.Collections.Generic.List[QuantConnect.Logging.LogEntry]) -> str:
        """
        Process the log entries and save it to permanent storage
        
        :param id: Id that will be incorporated into the algorithm log name
        :param logs: Log list
        :returns: Returns the location of the logs.
        """
        ...

    def security_type(self, types: System.Collections.Generic.List[QuantConnect.SecurityType]) -> None:
        """
        Send a list of secutity types that the algorithm trades to the browser to show the market clock - is this market open or closed!
        
        :param types: List of security types
        """
        ...

    def send_final_result(self) -> None:
        """
        Send a final analysis result back to the IDE.
        
        This method is protected.
        """
        ...

    def send_status_update(self, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """
        Send a algorithm status update to the user of the algorithms running state.
        
        :param status: Status enum of the algorithm.
        :param message: Optional string message describing reason for status change.
        """
        ...

    def set_algorithm(self, algorithm: QuantConnect.Interfaces.IAlgorithm, starting_portfolio_value: float) -> None:
        """
        Set the algorithm of the result handler after its been initialized.
        
        :param algorithm: Algorithm object matching IAlgorithm interface
        :param starting_portfolio_value: Algorithm starting capital for statistics calculations
        """
        ...

    def set_next_status_update(self) -> None:
        """
        Assigns the next earliest status update time
        
        This method is protected.
        """
        ...

    def set_summary_statistic(self, name: str, value: str) -> None:
        """
        Sets or updates a custom summary statistic
        
        :param name: The statistic name
        :param value: The statistic value
        """
        ...

    def statistics_results(self) -> QuantConnect.Statistics.StatisticsResults:
        """
        Calculates and gets the current statistics for the algorithm
        
        :returns: The current statistics.
        """
        ...

    def store_order_events(self, utc_time: typing.Union[datetime.datetime, datetime.date], order_events: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]) -> None:
        """
        Stores the order events
        
        This method is protected.
        
        :param utc_time: The utc date associated with these order events
        :param order_events: The order events to store
        """
        ...

    def store_result(self, packet: QuantConnect.Packets.Packet) -> None:
        """
        Save the snapshot of the total results to storage.
        
        This method is protected.
        
        :param packet: Packet to store.
        """
        ...

    def system_debug_message(self, message: str) -> None:
        """
        Send a live trading system debug message to the live console.
        
        :param message: Message we'd like shown in console.
        """
        ...


