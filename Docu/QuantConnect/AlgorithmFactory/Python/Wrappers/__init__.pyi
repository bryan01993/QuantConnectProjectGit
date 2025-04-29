from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.AlgorithmFactory.Python.Wrappers
import QuantConnect.Benchmarks
import QuantConnect.Brokerages
import QuantConnect.Commands
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Orders
import QuantConnect.Python
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Future
import QuantConnect.Securities.Option
import QuantConnect.Statistics
import QuantConnect.Storage
import System
import System.Collections.Concurrent
import System.Collections.Generic

QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable = typing.TypeVar("QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable")
QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType = typing.TypeVar("QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType")


class AlgorithmPythonWrapper(QuantConnect.Python.BasePythonWrapper[QuantConnect.Interfaces.IAlgorithm], QuantConnect.Interfaces.IAlgorithm):
    """Creates and wraps the algorithm written in python."""

    @property
    def is_on_end_of_day_implemented(self) -> bool:
        """True if the underlying python algorithm implements "OnEndOfDay\""""
        ...

    @property
    def is_on_end_of_day_symbol_implemented(self) -> bool:
        """True if the underlying python algorithm implements "OnEndOfDay(symbol)\""""
        ...

    @property
    def algorithm_id(self) -> str:
        """AlgorithmId for the backtest"""
        ...

    @property
    def benchmark(self) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Gets the function used to define the benchmark. This function will return
        the value of the benchmark at a requested date/time
        """
        ...

    @property
    def brokerage_message_handler(self) -> QuantConnect.Brokerages.IBrokerageMessageHandler:
        """
        Gets the brokerage message handler used to decide what to do
        with each message sent from the brokerage
        """
        ...

    @property.setter
    def brokerage_message_handler(self, value: QuantConnect.Brokerages.IBrokerageMessageHandler) -> None:
        ...

    @property
    def brokerage_model(self) -> QuantConnect.Brokerages.IBrokerageModel:
        """Gets the brokerage model used to emulate a real brokerage"""
        ...

    @property
    def brokerage_name(self) -> QuantConnect.Brokerages.BrokerageName:
        """Gets the brokerage name."""
        ...

    @property
    def risk_free_interest_rate_model(self) -> QuantConnect.Data.IRiskFreeInterestRateModel:
        """Gets the risk free interest rate model used to get the interest rates"""
        ...

    @property
    def debug_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Debug messages from the strategy:"""
        ...

    @property
    def end_date(self) -> datetime.datetime:
        """Get Requested Backtest End Date"""
        ...

    @property
    def error_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Error messages from the strategy:"""
        ...

    @property
    def history_provider(self) -> QuantConnect.Interfaces.IHistoryProvider:
        """Gets or sets the history provider for the algorithm"""
        ...

    @property.setter
    def history_provider(self, value: QuantConnect.Interfaces.IHistoryProvider) -> None:
        ...

    @property
    def is_warming_up(self) -> bool:
        """Gets whether or not this algorithm is still warming up"""
        ...

    @property
    def live_mode(self) -> bool:
        """Algorithm is running on a live server."""
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    @property
    def deployment_target(self) -> QuantConnect.DeploymentTarget:
        """Deployment target, either local or cloud."""
        ...

    @property
    def log_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Log messages from the strategy:"""
        ...

    @property
    def name(self) -> str:
        """Public name for the algorithm."""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.HashSet[str]:
        """A list of tags associated with the algorithm or the backtest, useful for categorization"""
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @property
    def name_updated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, str], None], None]:
        """Event fired algorithm's name is changed"""
        ...

    @property
    def tags_updated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, System.Collections.Generic.HashSet[str]], None], None]:
        """Event fired when the tag collection is updated"""
        ...

    @property
    def notify(self) -> QuantConnect.Notifications.NotificationManager:
        """Notification manager for storing and processing live event messages"""
        ...

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """
        Security portfolio management class provides wrapper and helper methods for the Security.Holdings class such as
        IsLong, IsShort, TotalProfit
        """
        ...

    @property
    def run_time_error(self) -> System.Exception:
        """Gets the run time error from the algorithm, or null if none was encountered."""
        ...

    @property.setter
    def run_time_error(self, value: System.Exception) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, str]:
        """Customizable dynamic statistics displayed during live trading:"""
        ...

    @property
    def schedule(self) -> QuantConnect.Scheduling.ScheduleManager:
        """Gets schedule manager for adding/removing scheduled events"""
        ...

    @property
    def securities(self) -> QuantConnect.Securities.SecurityManager:
        """
        Security object collection class stores an array of objects representing representing each security/asset
        we have a subscription for.
        """
        ...

    @property
    def security_initializer(self) -> QuantConnect.Securities.ISecurityInitializer:
        """Gets an instance that is to be used to initialize newly created securities."""
        ...

    @property
    def trade_builder(self) -> QuantConnect.Interfaces.ITradeBuilder:
        """Gets the Trade Builder to generate trades from executions"""
        ...

    @property
    def settings(self) -> QuantConnect.Interfaces.IAlgorithmSettings:
        """Gets the user settings for the algorithm"""
        ...

    @property
    def option_chain_provider(self) -> QuantConnect.Interfaces.IOptionChainProvider:
        """Gets the option chain provider, used to get the list of option contracts for an underlying symbol"""
        ...

    @property
    def future_chain_provider(self) -> QuantConnect.Interfaces.IFutureChainProvider:
        """Gets the future chain provider, used to get the list of future contracts for an underlying symbol"""
        ...

    @property
    def object_store(self) -> QuantConnect.Storage.ObjectStore:
        """Gets the object store, used for persistence"""
        ...

    @property
    def current_slice(self) -> QuantConnect.Data.Slice:
        """Returns the current Slice object"""
        ...

    @property
    def start_date(self) -> datetime.datetime:
        """Algorithm start date for backtesting, set by the SetStartDate methods."""
        ...

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Gets or sets the current status of the algorithm"""
        ...

    @property.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    def insights_generated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, QuantConnect.Algorithm.Framework.Alphas.GeneratedInsightsCollection], None], None]:
        """Event fired when an algorithm generates a insight"""
        ...

    @property
    def time_keeper(self) -> QuantConnect.Interfaces.ITimeKeeper:
        """Gets the time keeper instance"""
        ...

    @property
    def subscription_manager(self) -> QuantConnect.Data.SubscriptionManager:
        """
        Data subscription manager controls the information and subscriptions the algorithms recieves.
        Subscription configurations can be added through the Subscription Manager.
        """
        ...

    @property
    def project_id(self) -> int:
        """The project id associated with this algorithm if any"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def time(self) -> datetime.datetime:
        """Current date/time in the algorithm's local time zone"""
        ...

    @property
    def time_zone(self) -> typing.Any:
        """Gets the time zone of the algorithm"""
        ...

    @property
    def transactions(self) -> QuantConnect.Securities.SecurityTransactionManager:
        """Security transaction manager class controls the store and processing of orders."""
        ...

    @property
    def universe_manager(self) -> QuantConnect.Securities.UniverseManager:
        """Gets the collection of universes for the algorithm"""
        ...

    @property
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the subscription settings to be used when adding securities via universe selection"""
        ...

    @property
    def utc_time(self) -> datetime.datetime:
        """Current date/time in UTC."""
        ...

    @property
    def account_currency(self) -> str:
        """Gets the account currency"""
        ...

    @property
    def insights(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightManager:
        """Gets the insight manager"""
        ...

    @property
    def statistics(self) -> QuantConnect.Statistics.StatisticsResults:
        """The current statistics for the running algorithm."""
        ...

    def __init__(self, moduleName: str) -> None:
        """
        AlgorithmPythonWrapper constructor.
        Creates and wraps the algorithm written in python.
        
        :param moduleName: Name of the module that can be found in the PYTHONPATH
        """
        ...

    def add_chart(self, chart: QuantConnect.Chart) -> None:
        """
        Add a Chart object to algorithm collection
        
        :param chart: Chart object to add to collection.
        """
        ...

    def add_future_contract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, leverage: float = 0, extended_market_hours: bool = False) -> QuantConnect.Securities.Future.Future:
        """
        Creates and adds a new single Future contract to the algorithm
        
        :param symbol: The futures contract symbol
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extended_market_hours: Use extended market hours data
        :returns: The new Future security.
        """
        ...

    def add_option_contract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, leverage: float = 0, extended_market_hours: bool = False) -> QuantConnect.Securities.Option.Option:
        """
        Creates and adds a new single Option contract to the algorithm
        
        :param symbol: The option contract symbol
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extended_market_hours: Use extended market hours data
        :returns: The new Option security.
        """
        ...

    @overload
    def add_security(self, security_type: QuantConnect.SecurityType, symbol: str, resolution: typing.Optional[QuantConnect.Resolution], market: str, fill_forward: bool, leverage: float, extended_market_hours: bool, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> QuantConnect.Securities.Security:
        """
        Set a required SecurityType-symbol and resolution for algorithm
        
        :param security_type: SecurityType Enum: Equity, Commodity, FOREX or Future
        :param symbol: Symbol Representation of the MarketType, e.g. AAPL
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily.
        :param market: The market the requested security belongs to, such as 'usa' or 'fxcm'
        :param fill_forward: If true, returns the last available data even if none in that timeslice.
        :param leverage: leverage for this security
        :param extended_market_hours: Use extended market hours data
        :param data_mapping_mode: The contract mapping mode to use for the security
        :param data_normalization_mode: The price scaling mode to use for the security
        """
        ...

    @overload
    def add_security(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, leverage: float = ..., extended_market_hours: bool = False, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: int = 0) -> QuantConnect.Securities.Security:
        """
        Set a required SecurityType-symbol and resolution for algorithm
        
        :param symbol: The security Symbol
        :param resolution: Resolution of the MarketType required: MarketData, Second or Minute
        :param fill_forward: If true, returns the last available data even if none in that timeslice.
        :param leverage: leverage for this security
        :param extended_market_hours: Use extended market hours data
        :param data_mapping_mode: The contract mapping mode to use for the security
        :param data_normalization_mode: The price scaling mode to use for the security
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        :returns: The new Security that was added to the algorithm.
        """
        ...

    def add_tag(self, tag: str) -> None:
        """
        Adds a tag to the algorithm
        
        :param tag: The tag to add
        """
        ...

    def debug(self, message: str) -> None:
        """
        Send debug message
        
        :param message: String message
        """
        ...

    def error(self, message: str) -> None:
        """
        Send an error message for the algorithm
        
        :param message: String message
        """
        ...

    def get_chart_updates(self, clear_chart_data: bool = False) -> System.Collections.Generic.IEnumerable[QuantConnect.Chart]:
        """
        Get the chart updates since the last request:
        
        :returns: List of Chart Updates.
        """
        ...

    def get_last_known_price(self, security: QuantConnect.Securities.Security) -> QuantConnect.Data.BaseData:
        """
        Get the last known price using the history provider.
        Useful for seeding securities with the correct price
        
        :param security: Security object for which to retrieve historical data
        :returns: A single BaseData object with the last known price.
        """
        ...

    def get_locked(self) -> bool:
        """Gets whether or not this algorithm has been locked and fully initialized"""
        ...

    @overload
    def get_parameter(self, name: str, default_value: str = None) -> str:
        """
        Gets the parameter with the specified name. If a parameter with the specified name does not exist,
        the given default value is returned if any, else null
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    @overload
    def get_parameter(self, name: str, default_value: int) -> int:
        """
        Gets the parameter with the specified name parsed as an integer. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    @overload
    def get_parameter(self, name: str, default_value: float) -> float:
        """
        Gets the parameter with the specified name parsed as a double. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    @overload
    def get_parameter(self, name: str, default_value: float) -> float:
        """
        Gets the parameter with the specified name parsed as a decimal. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    def get_parameters(self) -> System.Collections.Generic.IReadOnlyDictionary[str, str]:
        """Gets a read-only dictionary with all current parameters"""
        ...

    def initialize(self) -> None:
        """Initialise the Algorithm and Prepare Required Data:"""
        ...

    def liquidate(self, symbol: typing.Union[QuantConnect.Symbol, str] = None, asynchronous: bool = False, tag: str = "Liquidated", order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Liquidate your portfolio holdings
        
        :param symbol: Specific asset to liquidate, defaults to all
        :param asynchronous: Flag to indicate if the symbols should be liquidated asynchronously
        :param tag: Custom tag to know who is calling this
        :param order_properties: Order properties to use
        """
        ...

    def log(self, message: str) -> None:
        """
        Save entry to the Log
        
        :param message: String message
        """
        ...

    def on_assignment_order_event(self, assignment_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Option assignment event handler. On an option assignment event for short legs the resulting information is passed to this method.
        
        :param assignment_event: Option exercise event details containing details of the assignment
        """
        ...

    def on_brokerage_disconnect(self) -> None:
        """Brokerage disconnected event handler. This method is called when the brokerage connection is lost."""
        ...

    def on_brokerage_message(self, message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """Brokerage message event handler. This method is called for all types of brokerage messages."""
        ...

    def on_brokerage_reconnect(self) -> None:
        """Brokerage reconnected event handler. This method is called when the brokerage connection is restored after a disconnection."""
        ...

    def on_command(self, data: typing.Any) -> typing.Optional[bool]:
        """
        Generic untyped command call handler
        
        :param data: The associated data
        :returns: True if success, false otherwise. Returning null will disable command feedback.
        """
        ...

    def on_data(self, slice: QuantConnect.Data.Slice) -> None:
        """
        v3.0 Handler for all data types
        
        :param slice: The current slice of data
        """
        ...

    def on_delistings(self, delistings: QuantConnect.Data.Market.Delistings) -> None:
        """
        Event handler to be called when there's been a delistings event
        
        :param delistings: The current time slice delistings
        """
        ...

    def on_dividends(self, dividends: QuantConnect.Data.Market.Dividends) -> None:
        """
        Event handler to be called when there's been a dividend event
        
        :param dividends: The current time slice dividends
        """
        ...

    def on_end_of_algorithm(self) -> None:
        """Call this event at the end of the algorithm running."""
        ...

    @overload
    def on_end_of_day(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        End of a trading day event handler. This method is called at the end of the algorithm day (or multiple times if trading multiple assets).
        
        :param symbol: Asset symbol for this end of day event. Forex and equities have different closing hours.
        """
        ...

    @overload
    def on_end_of_day(self) -> None:
        """
        End of a trading day event handler. This method is called at the end of the algorithm day (or multiple times if trading multiple assets).
        
        This method is deprecated. Please use this overload: OnEndOfDay(Symbol symbol)
        """
        ...

    def on_end_of_time_step(self) -> None:
        """
        Invoked at the end of every time step. This allows the algorithm
        to process events before advancing to the next time step.
        """
        ...

    def on_framework_data(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Used to send data updates to algorithm framework models
        
        :param slice: The current data slice
        """
        ...

    def on_framework_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Used to send security changes to algorithm framework models
        
        :param changes: Security additions/removals for this time step
        """
        ...

    def on_margin_call(self, requests: System.Collections.Generic.List[QuantConnect.Orders.SubmitOrderRequest]) -> None:
        """
        Margin call event handler. This method is called right before the margin call orders are placed in the market.
        
        :param requests: The orders to be executed to bring this algorithm within margin limits
        """
        ...

    def on_margin_call_warning(self) -> None:
        """Margin call warning event handler. This method is called when Portfolio.MarginRemaining is under 5% of your Portfolio.TotalPortfolioValue"""
        ...

    def on_order_event(self, new_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        EXPERTS ONLY:: [-!-Async Code-!-]
        New order event handler: on order status changes (filled, partially filled, cancelled etc).
        
        :param new_event: Event information
        """
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param changes: Security additions/removals for this time step
        """
        ...

    def on_splits(self, splits: QuantConnect.Data.Market.Splits) -> None:
        """
        Event handler to be called when there's been a split event
        
        :param splits: The current time slice splits
        """
        ...

    def on_symbol_changed_events(self, symbols_changed: QuantConnect.Data.Market.SymbolChangedEvents) -> None:
        """
        Event handler to be called when there's been a symbol changed event
        
        :param symbols_changed: The current time slice symbol changed events
        """
        ...

    def on_warmup_finished(self) -> None:
        """Called when the algorithm has completed initialization and warm up."""
        ...

    def post_initialize(self) -> None:
        """
        Called by setup handlers after Initialize and allows the algorithm a chance to organize
        the data gather in the Initialize method
        """
        ...

    def remove_security(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Removes the security with the specified symbol. This will cancel all
        open orders and then liquidate any existing holdings
        
        :param symbol: The symbol of the security to be removed
        """
        ...

    def run_command(self, command: QuantConnect.Commands.CallbackCommand) -> QuantConnect.Commands.CommandResultPacket:
        """
        Run a callback command instance
        
        :param command: The callback command instance
        :returns: The command result.
        """
        ...

    def set_account_currency(self, account_currency: str, starting_cash: typing.Optional[float] = None) -> None:
        """
        Sets the account currency cash symbol this algorithm is to manage, as well
        as the starting cash in this currency if given
        
        :param account_currency: The account currency cash symbol to set
        :param starting_cash: The account currency starting cash to set
        """
        ...

    def set_algorithm_id(self, algorithm_id: str) -> None:
        """
        Set the algorithm Id for this backtest or live run. This can be used to identify the order and equity records.
        
        :param algorithm_id: unique 32 character identifier for backtest or live server
        """
        ...

    def set_algorithm_mode(self, algorithm_mode: QuantConnect.AlgorithmMode) -> None:
        """
        Sets the algorithm running mode
        
        :param algorithm_mode: Algorithm mode
        """
        ...

    def set_api(self, api: QuantConnect.Interfaces.IApi) -> None:
        """
        Provide the API for the algorithm.
        
        :param api: Initiated API
        """
        ...

    def set_available_data_types(self, available_data_types: System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]) -> None:
        """
        Set the available TickType supported by each SecurityType in SecurityManager
        
        :param available_data_types: >The different TickType each Security supports
        """
        ...

    def set_brokerage_message_handler(self, handler: QuantConnect.Brokerages.IBrokerageMessageHandler) -> None:
        """
        Sets the implementation used to handle messages from the brokerage.
        The default implementation will forward messages to debug or error
        and when a BrokerageMessageType.Error occurs, the algorithm
        is stopped.
        
        :param handler: The message handler to use
        """
        ...

    def set_brokerage_model(self, brokerage_model: QuantConnect.Brokerages.IBrokerageModel) -> None:
        """
        Sets the brokerage model used to resolve transaction models, settlement models,
        and brokerage specified ordering behaviors.
        
        :param brokerage_model: The brokerage model used to emulate the real brokerage
        """
        ...

    @overload
    def set_cash(self, starting_cash: float) -> None:
        """
        Set the starting capital for the strategy
        
        :param starting_cash: decimal starting capital, default $100,000
        """
        ...

    @overload
    def set_cash(self, symbol: str, starting_cash: float, conversion_rate: float = 0) -> None:
        """
        Set the cash for the specified symbol
        
        :param symbol: The cash symbol to set
        :param starting_cash: Decimal cash value of portfolio
        :param conversion_rate: The current conversion rate for the
        """
        ...

    def set_current_slice(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Sets the current slice
        
        :param slice: The Slice object
        """
        ...

    def set_date_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Set the DateTime Frontier: This is the master time and is"""
        ...

    def set_deployment_target(self, deployment_target: QuantConnect.DeploymentTarget) -> None:
        """
        Sets the algorithm deployment target
        
        :param deployment_target: Deployment target
        """
        ...

    def set_end_date(self, end: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the end date for a backtest.
        
        :param end: Datetime value for end date
        """
        ...

    def set_finished_warming_up(self) -> None:
        """Sets IsWarmingUp to false to indicate this algorithm has finished its warm up"""
        ...

    def set_future_chain_provider(self, future_chain_provider: QuantConnect.Interfaces.IFutureChainProvider) -> None:
        """
        Sets the future chain provider, used to get the list of future contracts for an underlying symbol
        
        :param future_chain_provider: The future chain provider
        """
        ...

    def set_history_provider(self, history_provider: QuantConnect.Interfaces.IHistoryProvider) -> None:
        """
        Set the historical data provider
        
        :param history_provider: Historical data provider
        """
        ...

    def set_live_mode(self, live: bool) -> None:
        """
        Set live mode state of the algorithm run: Public setter for the algorithm property LiveMode.
        
        :param live: Bool live mode flag
        """
        ...

    def set_locked(self) -> None:
        """Set the algorithm as initialized and locked. No more cash or security changes."""
        ...

    def set_maximum_orders(self, max: int) -> None:
        """
        Set the maximum number of orders the algorithm is allowed to process.
        
        :param max: Maximum order count int
        """
        ...

    def set_name(self, name: str) -> None:
        """
        Sets name to the currently running backtest
        
        :param name: The name for the backtest
        """
        ...

    def set_object_store(self, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Sets the object store
        
        :param object_store: The object store
        """
        ...

    def set_option_chain_provider(self, option_chain_provider: QuantConnect.Interfaces.IOptionChainProvider) -> None:
        """
        Sets the option chain provider, used to get the list of option contracts for an underlying symbol
        
        :param option_chain_provider: The option chain provider
        """
        ...

    def set_parameters(self, parameters: System.Collections.Generic.Dictionary[str, str]) -> None:
        """
        Sets the parameters from the dictionary
        
        :param parameters: Dictionary containing the parameter names to values
        """
        ...

    def set_run_time_error(self, exception: System.Exception) -> None:
        """
        Set the runtime error
        
        :param exception: Represents error that occur during execution
        """
        ...

    def set_start_date(self, start: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the start date for the backtest
        
        :param start: Datetime Start date for backtest
        """
        ...

    def set_statistics_service(self, statistics_service: QuantConnect.Statistics.IStatisticsService) -> None:
        """
        Sets the statistics service instance to be used by the algorithm
        
        :param statistics_service: The statistics service instance
        """
        ...

    def set_status(self, status: QuantConnect.AlgorithmStatus) -> None:
        """
        Set the state of a live deployment
        
        :param status: Live deployment status
        """
        ...

    def set_tags(self, tags: System.Collections.Generic.HashSet[str]) -> None:
        """
        Sets the tags for the algorithm
        
        :param tags: The tags
        """
        ...

    def shortable(self, symbol: typing.Union[QuantConnect.Symbol, str], short_quantity: float, update_order_id: typing.Optional[int] = None) -> bool:
        """
        Determines if the Symbol is shortable at the brokerage
        
        :param symbol: Symbol to check if shortable
        :param short_quantity: Order's quantity to check if it is currently shortable, taking into account current holdings and open orders
        :param update_order_id: Optionally the id of the order being updated. When updating an order we want to ignore it's submitted short quantity and use the new provided quantity to determine if we can perform the update
        :returns: True if the symbol can be shorted by the requested quantity.
        """
        ...

    def shortable_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> int:
        """
        Gets the quantity shortable for the given asset
        
        :returns: Quantity shortable for the given asset. Zero if not shortable, or a number greater than zero if shortable.
        """
        ...

    def submit_order_request(self, request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Will submit an order request to the algorithm
        
        :param request: The request to submit
        :returns: The order ticket.
        """
        ...

    def symbol(self, ticker: str) -> QuantConnect.Symbol:
        """
        Converts the string 'ticker' symbol into a full Symbol object
        This requires that the string 'ticker' has been added to the algorithm
        
        :param ticker: The ticker symbol. This should be the ticker symbol as it was added to the algorithm
        :returns: The symbol object mapped to the specified ticker.
        """
        ...

    def ticker(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        For the given symbol will resolve the ticker it used at the current algorithm date
        
        :param symbol: The symbol to get the ticker for
        :returns: The mapped ticker for a symbol.
        """
        ...

    def to_string(self) -> str:
        """Returns a string that represents the current AlgorithmPythonWrapper object."""
        ...


class _EventContainer(typing.Generic[QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable, QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


