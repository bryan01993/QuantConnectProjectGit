from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.RealTime
import QuantConnect.Lean.Engine.Results
import QuantConnect.Lean.Engine.Setup
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Packets
import QuantConnect.Util
import System
import System.Collections.Generic


class SetupHandlerParameters(System.Object):
    """Defines the parameters for ISetupHandler"""

    @property
    def universe_selection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        """Gets the universe selection"""
        ...

    @property
    def algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """Gets the algorithm"""
        ...

    @property
    def brokerage(self) -> QuantConnect.Interfaces.IBrokerage:
        """Gets the Brokerage"""
        ...

    @property
    def algorithm_node_packet(self) -> QuantConnect.Packets.AlgorithmNodePacket:
        """Gets the algorithm node packet"""
        ...

    @property
    def result_handler(self) -> QuantConnect.Lean.Engine.Results.IResultHandler:
        """Gets the algorithm node packet"""
        ...

    @property
    def transaction_handler(self) -> QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler:
        """Gets the TransactionHandler"""
        ...

    @property
    def real_time_handler(self) -> QuantConnect.Lean.Engine.RealTime.IRealTimeHandler:
        """Gets the RealTimeHandler"""
        ...

    @property
    def data_cache_provider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """Gets the DataCacheProvider"""
        ...

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """The map file provider instance of the algorithm"""
        ...

    def __init__(self, universeSelection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection, algorithm: QuantConnect.Interfaces.IAlgorithm, brokerage: QuantConnect.Interfaces.IBrokerage, algorithmNodePacket: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, transactionHandler: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, realTimeHandler: QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider) -> None:
        """
        Creates a new instance
        
        :param universeSelection: The universe selection instance
        :param algorithm: Algorithm instance
        :param brokerage: New brokerage output instance
        :param algorithmNodePacket: Algorithm job task
        :param resultHandler: The configured result handler
        :param transactionHandler: The configured transaction handler
        :param realTimeHandler: The configured real time handler
        :param dataCacheProvider: The configured data cache provider
        :param mapFileProvider: The map file provider
        """
        ...


class BaseSetupHandler(System.Object):
    """
    Base class that provides shared code for
    the ISetupHandler implementations
    """

    ALGORITHM_CREATION_TIMEOUT: datetime.timedelta
    """Get the maximum time that the creation of an algorithm can take"""

    @staticmethod
    def get_configured_data_feeds() -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]:
        """Get the available data feeds from config.json,"""
        ...

    @staticmethod
    def initialize_debugging(algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, worker_thread: QuantConnect.Util.WorkerThread) -> bool:
        """
        Initialize the debugger
        
        :param algorithm_node_packet: The algorithm node packet
        :param worker_thread: The worker thread instance to use
        """
        ...

    @staticmethod
    def load_backtest_job_account_currency(algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.BacktestNodePacket) -> None:
        """Sets the account currency the algorithm should use if set in the job packet"""
        ...

    @staticmethod
    def load_backtest_job_cash_amount(algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.BacktestNodePacket) -> None:
        """Sets the initial cash for the algorithm if set in the job packet."""
        ...

    @staticmethod
    def set_brokerage_trading_day_per_year(algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Set the number of trading days per year based on the specified brokerage model.
        
        :param algorithm: The algorithm instance
        :returns: The number of trading days per year. For specific brokerages (Coinbase, Binance, Bitfinex, Bybit, FTX, Kraken), the value is 365. For other brokerages, the default value is 252.
        """
        ...

    @staticmethod
    def setup(parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Primary entry point to setup a new algorithm
        
        :param parameters: The parameters object to use
        :returns: True on successfully setting up the algorithm state, or false on error.
        """
        ...

    @staticmethod
    def setup_currency_conversions(algorithm: QuantConnect.Interfaces.IAlgorithm, universe_selection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection, currencies_to_update_white_list: System.Collections.Generic.IReadOnlyCollection[str] = None) -> None:
        """
        Will first check and add all the required conversion rate securities
        and later will seed an initial value to them.
        
        :param algorithm: The algorithm instance
        :param universe_selection: The universe selection instance
        :param currencies_to_update_white_list: If passed, the currencies in the CashBook that are contained in this list will be updated. By default, if not passed (null), all currencies in the cashbook without a properly set up currency conversion will be updated. This is not intended for actual algorithms but for tests or for this method to be used as a helper.
        """
        ...


class ISetupHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Interface to setup the algorithm. Pass in a raw algorithm, return one with portfolio, cash, etc already preset."""

    @property
    @abc.abstractmethod
    def worker_thread(self) -> QuantConnect.Util.WorkerThread:
        """The worker thread instance the setup handler should use"""
        ...

    @property.setter
    def worker_thread(self, value: QuantConnect.Util.WorkerThread) -> None:
        ...

    @property
    @abc.abstractmethod
    def errors(self) -> System.Collections.Generic.List[System.Exception]:
        """Any errors from the initialization stored here:"""
        ...

    @property.setter
    def errors(self, value: System.Collections.Generic.List[System.Exception]) -> None:
        ...

    @property
    @abc.abstractmethod
    def maximum_runtime(self) -> datetime.timedelta:
        """Get the maximum runtime for this algorithm job."""
        ...

    @property
    @abc.abstractmethod
    def starting_portfolio_value(self) -> float:
        """Algorithm starting capital for statistics calculations"""
        ...

    @property
    @abc.abstractmethod
    def starting_date(self) -> datetime.datetime:
        """Start date for analysis loops to search for data."""
        ...

    @property
    @abc.abstractmethod
    def max_orders(self) -> int:
        """Maximum number of orders for the algorithm run -- applicable for backtests only."""
        ...

    def create_algorithm_instance(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, assembly_path: str) -> QuantConnect.Interfaces.IAlgorithm:
        """
        Create a new instance of an algorithm from a physical dll path.
        
        :param algorithm_node_packet: Details of the task required
        :param assembly_path: The path to the assembly's location
        :returns: A new instance of IAlgorithm, or throws an exception if there was an error.
        """
        ...

    def create_brokerage(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, uninitialized_algorithm: QuantConnect.Interfaces.IAlgorithm, factory: typing.Optional[QuantConnect.Interfaces.IBrokerageFactory]) -> typing.Union[QuantConnect.Interfaces.IBrokerage, QuantConnect.Interfaces.IBrokerageFactory]:
        """
        Creates the brokerage as specified by the job packet
        
        :param algorithm_node_packet: Job packet
        :param uninitialized_algorithm: The algorithm instance before Initialize has been called
        :param factory: The brokerage factory
        :returns: The brokerage instance, or throws if error creating instance.
        """
        ...

    def setup(self, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Primary entry point to setup a new algorithm
        
        :param parameters: The parameters object to use
        :returns: True on successfully setting up the algorithm state, or false on error.
        """
        ...


class BacktestingSetupHandler(System.Object, QuantConnect.Lean.Engine.Setup.ISetupHandler):
    """Backtesting setup handler processes the algorithm initialize method and sets up the internal state of the algorithm class."""

    @property
    def worker_thread(self) -> QuantConnect.Util.WorkerThread:
        """The worker thread instance the setup handler should use"""
        ...

    @property.setter
    def worker_thread(self, value: QuantConnect.Util.WorkerThread) -> None:
        ...

    @property
    def errors(self) -> System.Collections.Generic.List[System.Exception]:
        """Internal errors list from running the setup procedures."""
        ...

    @property.setter
    def errors(self, value: System.Collections.Generic.List[System.Exception]) -> None:
        ...

    @property
    def maximum_runtime(self) -> datetime.timedelta:
        """Maximum runtime of the algorithm in seconds."""
        ...

    @property
    def starting_portfolio_value(self) -> float:
        """Starting capital according to the users initialize routine."""
        ...

    @property
    def starting_date(self) -> datetime.datetime:
        """Start date for analysis loops to search for data."""
        ...

    @property
    def max_orders(self) -> int:
        """Maximum number of orders for this backtest."""
        ...

    def __init__(self) -> None:
        """Initialize the backtest setup handler."""
        ...

    def create_algorithm_instance(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, assembly_path: str) -> QuantConnect.Interfaces.IAlgorithm:
        """
        Create a new instance of an algorithm from a physical dll path.
        
        :param algorithm_node_packet: Details of the task required
        :param assembly_path: The path to the assembly's location
        :returns: A new instance of IAlgorithm, or throws an exception if there was an error.
        """
        ...

    def create_brokerage(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, uninitialized_algorithm: QuantConnect.Interfaces.IAlgorithm, factory: typing.Optional[QuantConnect.Interfaces.IBrokerageFactory]) -> typing.Union[QuantConnect.Interfaces.IBrokerage, QuantConnect.Interfaces.IBrokerageFactory]:
        """
        Creates a new BacktestingBrokerage instance
        
        :param algorithm_node_packet: Job packet
        :param uninitialized_algorithm: The algorithm instance before Initialize has been called
        :param factory: The brokerage factory
        :returns: The brokerage instance, or throws if error creating instance.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def setup(self, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Setup the algorithm cash, dates and data subscriptions as desired.
        
        :param parameters: The parameters object to use
        :returns: Boolean true on successfully initializing the algorithm.
        """
        ...


class ConsoleSetupHandler(QuantConnect.Lean.Engine.Setup.BacktestingSetupHandler):
    """
    Kept for backwards compatibility-
    
    Should use BacktestingSetupHandler instead
    """


class AlgorithmSetupException(System.Exception):
    """Defines an exception generated in the course of invoking ISetupHandler.Setup"""

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the AlgorithmSetupException class
        
        :param message: The error message
        """
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        """
        Initializes a new instance of the AlgorithmSetupException class
        
        :param message: The error message
        :param inner: The inner exception being wrapped
        """
        ...


class BrokerageSetupHandler(System.Object, QuantConnect.Lean.Engine.Setup.ISetupHandler):
    """Defines a set up handler that initializes the algorithm instance using values retrieved from the user's brokerage account"""

    max_allocation_limit_config: str = "max-allocation-limit"
    """Max allocation limit configuration variable name"""

    @property
    def worker_thread(self) -> QuantConnect.Util.WorkerThread:
        """The worker thread instance the setup handler should use"""
        ...

    @property.setter
    def worker_thread(self, value: QuantConnect.Util.WorkerThread) -> None:
        ...

    @property
    def errors(self) -> System.Collections.Generic.List[System.Exception]:
        """Any errors from the initialization stored here:"""
        ...

    @property.setter
    def errors(self, value: System.Collections.Generic.List[System.Exception]) -> None:
        ...

    @property
    def maximum_runtime(self) -> datetime.timedelta:
        """Get the maximum runtime for this algorithm job."""
        ...

    @property
    def starting_portfolio_value(self) -> float:
        """Algorithm starting capital for statistics calculations"""
        ...

    @property
    def starting_date(self) -> datetime.datetime:
        """Start date for analysis loops to search for data."""
        ...

    @property
    def max_orders(self) -> int:
        """Maximum number of orders for the algorithm run -- applicable for backtests only."""
        ...

    def __init__(self) -> None:
        """Initializes a new BrokerageSetupHandler"""
        ...

    def create_algorithm_instance(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, assembly_path: str) -> QuantConnect.Interfaces.IAlgorithm:
        """
        Create a new instance of an algorithm from a physical dll path.
        
        :param algorithm_node_packet: Details of the task required
        :param assembly_path: The path to the assembly's location
        :returns: A new instance of IAlgorithm, or throws an exception if there was an error.
        """
        ...

    def create_brokerage(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, uninitialized_algorithm: QuantConnect.Interfaces.IAlgorithm, factory: typing.Optional[QuantConnect.Interfaces.IBrokerageFactory]) -> typing.Union[QuantConnect.Interfaces.IBrokerage, QuantConnect.Interfaces.IBrokerageFactory]:
        """
        Creates the brokerage as specified by the job packet
        
        :param algorithm_node_packet: Job packet
        :param uninitialized_algorithm: The algorithm instance before Initialize has been called
        :param factory: The brokerage factory
        :returns: The brokerage instance, or throws if error creating instance.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def get_open_orders(self, algorithm: QuantConnect.Interfaces.IAlgorithm, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, transaction_handler: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, brokerage: QuantConnect.Interfaces.IBrokerage) -> None:
        """
        Get the open orders from a brokerage. Adds Orders.Order and Orders.OrderTicket to the transaction handler
        
        This method is protected.
        
        :param algorithm: Algorithm instance
        :param result_handler: The configured result handler
        :param transaction_handler: The configurated transaction handler
        :param brokerage: Brokerage output instance
        """
        ...

    def load_existing_holdings_and_orders(self, brokerage: QuantConnect.Interfaces.IBrokerage, algorithm: QuantConnect.Interfaces.IAlgorithm, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Loads existing holdings and orders
        
        This method is protected.
        """
        ...

    def setup(self, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Primary entry point to setup a new algorithm
        
        :param parameters: The parameters object to use
        :returns: True on successfully setting up the algorithm state, or false on error.
        """
        ...


