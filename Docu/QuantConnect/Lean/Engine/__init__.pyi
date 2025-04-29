from typing import overload
from enum import Enum
import datetime

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.RealTime
import QuantConnect.Lean.Engine.Results
import QuantConnect.Lean.Engine.Server
import QuantConnect.Lean.Engine.Setup
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Packets
import QuantConnect.Util
import QuantConnect.Util.RateLimit
import System
import System.Threading


class LeanEngineSystemHandlers(System.Object, System.IDisposable):
    """Provides a container for the system level handlers"""

    @property
    def api(self) -> QuantConnect.Interfaces.IApi:
        """Gets the api instance used for communicating algorithm limits, status, and storing of log data"""
        ...

    @property
    def notify(self) -> QuantConnect.Interfaces.IMessagingHandler:
        """
        Gets the messaging handler instance used for communicating various packets to listeners, including
        debug/log messages, email/sms/web messages, as well as results and run time errors
        """
        ...

    @property
    def job_queue(self) -> QuantConnect.Interfaces.IJobQueueHandler:
        """Gets the job queue responsible for acquiring and acknowledging an algorithm job"""
        ...

    @property
    def lean_manager(self) -> QuantConnect.Lean.Engine.Server.ILeanManager:
        """Gets the ILeanManager implementation using to enhance the hosting environment"""
        ...

    def __init__(self, jobQueue: QuantConnect.Interfaces.IJobQueueHandler, api: QuantConnect.Interfaces.IApi, notify: QuantConnect.Interfaces.IMessagingHandler, leanManager: QuantConnect.Lean.Engine.Server.ILeanManager) -> None:
        """
        Initializes a new instance of the LeanEngineSystemHandlers class with the specified handles
        
        :param jobQueue: The job queue used to acquire algorithm jobs
        :param api: The api instance used for communicating limits and status
        :param notify: The messaging handler user for passing messages from the algorithm to listeners
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @staticmethod
    def from_configuration(composer: QuantConnect.Util.Composer) -> QuantConnect.Lean.Engine.LeanEngineSystemHandlers:
        """
        Creates a new instance of the LeanEngineSystemHandlers class from the specified composer using type names from configuration
        
        :param composer: The composer instance to obtain implementations from
        :returns: A fully hydrates LeanEngineSystemHandlers instance.
        """
        ...

    def initialize(self) -> None:
        """Initializes the Api, Messaging, and JobQueue components"""
        ...


class LeanEngineAlgorithmHandlers(System.Object, System.IDisposable):
    """Provides a container for the algorithm specific handlers"""

    @property
    def results(self) -> QuantConnect.Lean.Engine.Results.IResultHandler:
        """Gets the result handler used to communicate results from the algorithm"""
        ...

    @property
    def setup(self) -> QuantConnect.Lean.Engine.Setup.ISetupHandler:
        """Gets the setup handler used to initialize the algorithm state"""
        ...

    @property
    def data_feed(self) -> QuantConnect.Lean.Engine.DataFeeds.IDataFeed:
        """Gets the data feed handler used to provide data to the algorithm"""
        ...

    @property
    def transactions(self) -> QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler:
        """Gets the transaction handler used to process orders from the algorithm"""
        ...

    @property
    def real_time(self) -> QuantConnect.Lean.Engine.RealTime.IRealTimeHandler:
        """Gets the real time handler used to process real time events"""
        ...

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """Gets the map file provider used as a map file source for the data feed"""
        ...

    @property
    def factor_file_provider(self) -> QuantConnect.Interfaces.IFactorFileProvider:
        """Gets the map file provider used as a map file source for the data feed"""
        ...

    @property
    def data_provider(self) -> QuantConnect.Interfaces.IDataProvider:
        """Gets the data file provider used to retrieve security data if it is not on the file system"""
        ...

    @property
    def data_cache_provider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """Gets the data file provider used to retrieve security data if it is not on the file system"""
        ...

    @property
    def object_store(self) -> QuantConnect.Interfaces.IObjectStore:
        """Gets the object store used for persistence"""
        ...

    @property
    def data_permissions_manager(self) -> QuantConnect.Interfaces.IDataPermissionManager:
        """Entity in charge of handling data permissions"""
        ...

    @property
    def data_monitor(self) -> QuantConnect.Interfaces.IDataMonitor:
        """Monitors data requests and reports on missing data"""
        ...

    def __init__(self, results: QuantConnect.Lean.Engine.Results.IResultHandler, setup: QuantConnect.Lean.Engine.Setup.ISetupHandler, dataFeed: QuantConnect.Lean.Engine.DataFeeds.IDataFeed, transactions: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, realTime: QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, dataProvider: QuantConnect.Interfaces.IDataProvider, objectStore: QuantConnect.Interfaces.IObjectStore, dataPermissionsManager: QuantConnect.Interfaces.IDataPermissionManager, liveMode: bool, researchMode: bool = False) -> None:
        """
        Initializes a new instance of the LeanEngineAlgorithmHandlers class from the specified handlers
        
        :param results: The result handler for communicating results from the algorithm
        :param setup: The setup handler used to initialize algorithm state
        :param dataFeed: The data feed handler used to pump data to the algorithm
        :param transactions: The transaction handler used to process orders from the algorithm
        :param realTime: The real time handler used to process real time events
        :param mapFileProvider: The map file provider used to retrieve map files for the data feed
        :param factorFileProvider: Map file provider used as a map file source for the data feed
        :param dataProvider: file provider used to retrieve security data if it is not on the file system
        :param objectStore: The object store used for persistence
        :param dataPermissionsManager: The data permission manager to use
        :param liveMode: True for live mode, false otherwise
        :param researchMode: True for research mode, false otherwise. This has less priority than liveMode
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @staticmethod
    def from_configuration(composer: QuantConnect.Util.Composer, research_mode: bool = False) -> QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers:
        """
        Creates a new instance of the LeanEngineAlgorithmHandlers class from the specified composer using type names from configuration
        
        :param composer: The composer instance to obtain implementations from
        :param research_mode: True for research mode, false otherwise
        :returns: A fully hydrates LeanEngineSystemHandlers instance.
        """
        ...


class AlgorithmTimeLimitManager(System.Object, QuantConnect.IIsolatorLimitResultProvider):
    """
    Provides an implementation of IIsolatorLimitResultProvider that tracks the algorithm
    manager's time loops and enforces a maximum amount of time that each time loop may take to execute.
    The isolator uses the result provided by IsWithinLimit to determine if it should
    terminate the algorithm for violation of the imposed limits.
    """

    @property
    def additional_time_bucket(self) -> QuantConnect.Util.RateLimit.ITokenBucket:
        """
        Gets the additional time bucket which is responsible for tracking additional time requested
        for processing via long-running scheduled events. In LEAN, we use the LeakyBucket
        """
        ...

    def __init__(self, additionalTimeBucket: QuantConnect.Util.RateLimit.ITokenBucket, timeLoopMaximum: datetime.timedelta) -> None:
        """
        Initializes a new instance of AlgorithmTimeLimitManager to manage the
        creation of IsolatorLimitResult instances as it pertains to the
        algorithm manager's time loop
        
        :param additionalTimeBucket: Provides a bucket of additional time that can be requested to be spent to give execution time for things such as training scheduled events
        :param timeLoopMaximum: Specifies the maximum amount of time the algorithm is permitted to spend in a single time loop. This value can be overriden if certain actions are taken by the algorithm, such as invoking the training methods.
        """
        ...

    def is_within_limit(self) -> QuantConnect.IsolatorLimitResult:
        """Determines whether or not the algorithm time loop is considered within the limits"""
        ...

    def request_additional_time(self, minutes: int) -> None:
        """
        Requests additional time to continue executing the current time step.
        At time of writing, this is intended to be used to provide training scheduled events
        additional time to allow complex training models time to execute while also preventing
        abuse by enforcing certain control parameters set via the job packet.
        
        Each time this method is invoked, this time limit manager will increase the allowable
        execution time by the specified number of whole minutes
        """
        ...

    def start_new_time_step(self) -> None:
        """
        Invoked by the algorithm at the start of each time loop. This resets the current time step
        elapsed time.
        """
        ...

    def try_request_additional_time(self, minutes: int) -> bool:
        """
        Attempts to requests additional time to continue executing the current time step.
        At time of writing, this is intended to be used to provide training scheduled events
        additional time to allow complex training models time to execute while also preventing
        abuse by enforcing certain control parameters set via the job packet.
        
        Each time this method is invoked, this time limit manager will increase the allowable
        execution time by the specified number of whole minutes
        """
        ...


class AlgorithmManager(System.Object):
    """Algorithm manager class executes the algorithm and generates and passes through the algorithm events."""

    @property
    def state(self) -> QuantConnect.AlgorithmStatus:
        """Publicly accessible algorithm status"""
        ...

    @property
    def algorithm_id(self) -> str:
        """Public access to the currently running algorithm id."""
        ...

    @property
    def time_limit(self) -> QuantConnect.Lean.Engine.AlgorithmTimeLimitManager:
        """
        Provides the isolator with a function for verifying that we're not spending too much time in each
        algorithm manager time loop
        """
        ...

    @property
    def quit_state(self) -> bool:
        """Quit state flag for the running algorithm. When true the user has requested the backtest stops through a Quit() method."""
        ...

    @property
    def data_points(self) -> int:
        """Gets the number of data points processed per second"""
        ...

    @property
    def algorithm_history_data_points(self) -> int:
        """Gets the number of data points of algorithm history provider"""
        ...

    def __init__(self, liveMode: bool, job: QuantConnect.Packets.AlgorithmNodePacket = None) -> None:
        """
        Initializes a new instance of the AlgorithmManager class
        
        :param liveMode: True if we're running in live mode, false for backtest mode
        :param job: Provided by LEAN when creating a new algo manager. This is the job that the algo manager is about to execute. Research and other consumers can provide the default value of null
        """
        ...

    @staticmethod
    def handle_dividends(time_slice: QuantConnect.Lean.Engine.DataFeeds.TimeSlice, algorithm: QuantConnect.Interfaces.IAlgorithm, live_mode: bool) -> None:
        """Helper method to apply a dividend to an algorithm instance"""
        ...

    @staticmethod
    def handle_splits(time_slice: QuantConnect.Lean.Engine.DataFeeds.TimeSlice, algorithm: QuantConnect.Interfaces.IAlgorithm, live_mode: bool) -> None:
        """Helper method to apply a split to an algorithm instance"""
        ...

    @staticmethod
    def process_volatility_history_requirements(algorithm: QuantConnect.Interfaces.IAlgorithm, live_mode: bool) -> None:
        """
        Helper method used to process securities volatility history requirements
        
        :param algorithm: The algorithm instance
        :param live_mode: Whether the algorithm is in live mode
        """
        ...

    def run(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm, synchronizer: QuantConnect.Lean.Engine.DataFeeds.ISynchronizer, transactions: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, results: QuantConnect.Lean.Engine.Results.IResultHandler, realtime: QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, lean_manager: QuantConnect.Lean.Engine.Server.ILeanManager, cancellation_token_source: System.Threading.CancellationTokenSource) -> None:
        """
        Launch the algorithm manager to run this strategy
        
        :param job: Algorithm job
        :param algorithm: Algorithm instance
        :param synchronizer: Instance which implements ISynchronizer. Used to stream the data
        :param transactions: Transaction manager object
        :param results: Result handler object
        :param realtime: Realtime processing object
        :param lean_manager: ILeanManager implementation that is updated periodically with the IAlgorithm instance
        :param cancellation_token_source: Cancellation token source to monitor
        """
        ...

    def set_status(self, state: QuantConnect.AlgorithmStatus) -> None:
        """Set the quit state."""
        ...


class Engine(System.Object):
    """
    LEAN ALGORITHMIC TRADING ENGINE: ENTRY POINT.
    
    The engine loads new tasks, create the algorithms and threads, and sends them
    to Algorithm Manager to be executed. It is the primary operating loop.
    """

    @property
    def system_handlers(self) -> QuantConnect.Lean.Engine.LeanEngineSystemHandlers:
        """Gets the configured system handlers for this engine instance"""
        ...

    @property
    def algorithm_handlers(self) -> QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers:
        """Gets the configured algorithm handlers for this engine instance"""
        ...

    def __init__(self, systemHandlers: QuantConnect.Lean.Engine.LeanEngineSystemHandlers, algorithmHandlers: QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers, liveMode: bool) -> None:
        """
        Initializes a new instance of the Engine class using the specified handlers
        
        :param systemHandlers: The system handlers for controlling acquisition of jobs, messaging, and api calls
        :param algorithmHandlers: The algorithm handlers for managing algorithm initialization, data, results, transaction, and real time events
        :param liveMode: True when running in live mode, false otherwise
        """
        ...

    def run(self, job: QuantConnect.Packets.AlgorithmNodePacket, manager: QuantConnect.Lean.Engine.AlgorithmManager, assembly_path: str, worker_thread: QuantConnect.Util.WorkerThread) -> None:
        """
        Runs a single backtest/live job from the job queue
        
        :param job: The algorithm job to be processed
        :param manager: The algorithm manager instance
        :param assembly_path: The path to the algorithm's assembly
        :param worker_thread: The worker thread instance
        """
        ...


class Initializer(System.Object):
    """Helper class to initialize a Lean engine"""

    @staticmethod
    def get_algorithm_handlers(research_mode: bool = False) -> QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers:
        """Get and initializes Algorithm Handler"""
        ...

    @staticmethod
    def get_system_handlers() -> QuantConnect.Lean.Engine.LeanEngineSystemHandlers:
        """Get and initializes System Handler"""
        ...

    @staticmethod
    def start() -> None:
        """Basic common Lean initialization"""
        ...


