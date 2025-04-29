from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Algorithm.Framework.Portfolio.SignalExports
import QuantConnect.Api
import QuantConnect.Benchmarks
import QuantConnect.Brokerages
import QuantConnect.Commands
import QuantConnect.Data
import QuantConnect.Data.Auxiliary
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Future
import QuantConnect.Securities.Option
import QuantConnect.Statistics
import QuantConnect.Storage
import System
import System.Collections.Concurrent
import System.Collections.Generic
import System.IO
import System.Threading

QuantConnect_Interfaces_IBusyCollection_T = typing.TypeVar("QuantConnect_Interfaces_IBusyCollection_T")
QuantConnect_Interfaces_IExtendedDictionary_TValue = typing.TypeVar("QuantConnect_Interfaces_IExtendedDictionary_TValue")
QuantConnect_Interfaces_IExtendedDictionary_TKey = typing.TypeVar("QuantConnect_Interfaces_IExtendedDictionary_TKey")
QuantConnect_Interfaces__EventContainer_Callable = typing.TypeVar("QuantConnect_Interfaces__EventContainer_Callable")
QuantConnect_Interfaces__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Interfaces__EventContainer_ReturnType")


class IApi(System.IDisposable, metaclass=abc.ABCMeta):
    """API for QuantConnect.com"""

    def abort_optimization(self, optimization_id: str) -> QuantConnect.Api.RestResponse:
        """
        Abort an optimization
        
        :param optimization_id: Optimization id for the optimization we want to abort
        :returns: RestResponse.
        """
        ...

    def add_project_file(self, project_id: int, name: str, content: str) -> QuantConnect.Api.RestResponse:
        """
        Add a file to a project
        
        :param project_id: The project to which the file should be added
        :param name: The name of the new file
        :param content: The content of the new file
        :returns: ProjectFilesResponse that includes information about the newly created file.
        """
        ...

    def create_backtest(self, project_id: int, compile_id: str, backtest_name: str) -> QuantConnect.Api.Backtest:
        """Create a new backtest from a specified project_id and compile_id"""
        ...

    def create_compile(self, project_id: int) -> QuantConnect.Api.Compile:
        """
        Create a new compile job request for this project id.
        
        :param project_id: Project id we wish to compile.
        :returns: Compile object result.
        """
        ...

    def create_live_algorithm(self, project_id: int, compile_id: str, node_id: str, brokerage_settings: System.Collections.Generic.Dictionary[str, System.Object], version_id: str = "-1", data_providers: System.Collections.Generic.Dictionary[str, System.Object] = None) -> QuantConnect.Api.CreateLiveAlgorithmResponse:
        """
        Create a new live algorithm for a logged in user.
        
        :param project_id: Id of the project on QuantConnect
        :param compile_id: Id of the compilation on QuantConnect
        :param node_id: Id of the node that will run the algorithm
        :param brokerage_settings: Dictionary with Brokerage specific settings
        :param version_id: The version identifier
        :param data_providers: Dictionary with data providers and their corresponding credentials
        :returns: Information regarding the new algorithm CreateLiveAlgorithmResponse.
        """
        ...

    def create_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], estimated_cost: float, node_type: str, parallel_nodes: int) -> QuantConnect.Api.OptimizationSummary:
        ...

    def create_project(self, name: str, language: QuantConnect.Language, organization_id: str = None) -> QuantConnect.Api.ProjectResponse:
        """
        Create a project with the specified name and language via QuantConnect.com API
        
        :param name: Project name
        :param language: Programming language to use
        :param organization_id: Organization to create this project under
        :returns: ProjectResponse that includes information about the newly created project.
        """
        ...

    def delete_backtest(self, project_id: int, backtest_id: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a backtest from the specified project and backtest_id.
        
        :param project_id: Project for the backtest we want to delete
        :param backtest_id: Backtest id we want to delete
        :returns: RestResponse on success.
        """
        ...

    def delete_object_store(self, organization_id: str, key: str) -> QuantConnect.Api.RestResponse:
        """
        Request to delete Object Store metadata of a specific organization and key
        
        :param organization_id: Organization ID we would like to delete the Object Store file from
        :param key: Key to the Object Store file
        :returns: RestResponse.
        """
        ...

    def delete_optimization(self, optimization_id: str) -> QuantConnect.Api.RestResponse:
        """
        Delete an optimization
        
        :param optimization_id: Optimization id for the optimization we want to delete
        :returns: RestResponse.
        """
        ...

    def delete_project(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Delete a specific project owned by the user from QuantConnect.com
        
        :param project_id: Project id we own and wish to delete
        :returns: RestResponse indicating success.
        """
        ...

    def delete_project_file(self, project_id: int, name: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a file in a project
        
        :param project_id: Project id to which the file belongs
        :param name: The name of the file that should be deleted
        :returns: ProjectFilesResponse that includes the information about all files in the project.
        """
        ...

    def download(self, address: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]], user_name: str, password: str) -> str:
        """
        Local implementation for downloading data to algorithms
        
        :param address: URL to download
        :param headers: KVP headers
        :param user_name: Username for basic authentication
        :param password: Password for basic authentication
        """
        ...

    def download_bytes(self, address: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]], user_name: str, password: str) -> typing.List[int]:
        """
        Local implementation for downloading data to algorithms
        
        :param address: URL to download
        :param headers: KVP headers
        :param user_name: Username for basic authentication
        :param password: Password for basic authentication
        """
        ...

    def download_data(self, file_path: str, organization_id: str) -> bool:
        """
        Method to download and save the data purchased through QuantConnect
        
        :param file_path: File path representing the data requested
        :returns: A bool indicating whether the data was successfully downloaded or not.
        """
        ...

    def estimate_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]) -> QuantConnect.Api.Estimate:
        ...

    def get_algorithm_status(self, algorithm_id: str) -> QuantConnect.AlgorithmControl:
        """Get the algorithm current status, active or cancelled from the user"""
        ...

    def get_object_store(self, organization_id: str, keys: System.Collections.Generic.List[str], destination_folder: str = None) -> bool:
        """
        Download the object store associated with the given organization ID and key
        
        :param organization_id: Organization ID we would like to get the Object Store from
        :param keys: Keys for the Object Store files
        :param destination_folder: Folder in which the object will be stored
        :returns: True if the object was retrieved correctly, false otherwise.
        """
        ...

    def get_object_store_properties(self, organization_id: str, key: str) -> QuantConnect.Api.PropertiesObjectStoreResponse:
        """
        Get Object Store properties given the organization ID and the Object Store key
        
        :param organization_id: Organization ID we would like to get the Object Store from
        :param key: Key for the Object Store file
        :returns: PropertiesObjectStoreResponse.
        """
        ...

    def initialize(self, user_id: int, token: str, data_folder: str) -> None:
        """Initialize the control system"""
        ...

    def liquidate_live_algorithm(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Liquidate a live algorithm from the specified project.
        
        :param project_id: Project for the live instance we want to stop
        """
        ...

    def list_backtests(self, project_id: int, include_statistics: bool = False) -> QuantConnect.Api.BacktestSummaryList:
        """
        Get a list of backtest summaries for a specific project id
        
        :param project_id: Project id to search
        :param include_statistics: True for include statistics in the response, false otherwise
        :returns: BacktestList container for list of backtests.
        """
        ...

    def list_live_algorithms(self, status: typing.Optional[QuantConnect.AlgorithmStatus] = None, start_time: typing.Optional[datetime.datetime] = None, end_time: typing.Optional[datetime.datetime] = None) -> QuantConnect.Api.LiveList:
        """
        Get a list of live running algorithms for a logged in user.
        
        :param status: Filter the statuses of the algorithms returned from the api
        :param start_time: Earliest launched time of the algorithms returned by the Api
        :param end_time: Latest launched time of the algorithms returned by the Api
        :returns: List of live algorithm instances.
        """
        ...

    def list_optimizations(self, project_id: int) -> System.Collections.Generic.List[QuantConnect.Api.OptimizationSummary]:
        """
        List all the optimizations for a project
        
        :param project_id: Project id we'd like to get a list of optimizations for
        :returns: A list of BaseOptimization objects, BaseOptimization.
        """
        ...

    def list_projects(self) -> QuantConnect.Api.ProjectResponse:
        """
        Read back a list of all projects on the account for a user.
        
        :returns: Container for list of projects.
        """
        ...

    def read_account(self, organization_id: str = None) -> QuantConnect.Api.Account:
        """
        Will read the organization account status
        
        :param organization_id: The target organization id, if null will return default organization
        """
        ...

    def read_backtest(self, project_id: int, backtest_id: str, get_charts: bool = True) -> QuantConnect.Api.Backtest:
        """
        Read out the full result of a specific backtest
        
        :param project_id: Project id for the backtest we'd like to read
        :param backtest_id: Backtest id for the backtest we'd like to read
        :param get_charts: True will return backtest charts
        :returns: Backtest result object.
        """
        ...

    def read_backtest_chart(self, project_id: int, name: str, start: int, end: int, count: int, backtest_id: str) -> QuantConnect.Api.ReadChartResponse:
        """
        Returns a requested chart object from a backtest
        
        :param project_id: Project ID of the request
        :param name: The requested chart name
        :param start: The Utc start seconds timestamp of the request
        :param end: The Utc end seconds timestamp of the request
        :param count: The number of data points to request
        :param backtest_id: Associated Backtest ID for this chart request
        """
        ...

    def read_backtest_insights(self, project_id: int, backtest_id: str, start: int = 0, end: int = 0) -> QuantConnect.Api.InsightResponse:
        """
        Read out the insights of a backtest
        
        :param project_id: Id of the project from which to read the backtest
        :param backtest_id: Backtest id from which we want to get the insights
        :param start: Starting index of the insights to be fetched
        :param end: Last index of the insights to be fetched. Note that end - start must be less than 100
        :returns: InsightResponse.
        """
        ...

    def read_backtest_report(self, project_id: int, backtest_id: str) -> QuantConnect.Api.BacktestReport:
        """
        Read out the report of a backtest in the project id specified.
        
        :param project_id: Project id to read
        :param backtest_id: Specific backtest id to read
        :returns: BacktestReport.
        """
        ...

    def read_compile(self, project_id: int, compile_id: str) -> QuantConnect.Api.Compile:
        """
        Read a compile packet job result.
        
        :param project_id: Project id we sent for compile
        :param compile_id: Compile id return from the creation request
        :returns: Compile object result.
        """
        ...

    def read_data_directory(self, file_path: str) -> QuantConnect.Api.DataList:
        """Get valid data entries for a given filepath from data/list"""
        ...

    def read_data_link(self, file_path: str, organization_id: str) -> QuantConnect.Api.DataLink:
        """
        Gets the link to the downloadable data.
        
        :param file_path: File path representing the data requested
        :param organization_id: Organization to purchase this data with
        :returns: Link to the downloadable data.
        """
        ...

    def read_data_prices(self, organization_id: str) -> QuantConnect.Api.DataPricesList:
        """Gets data prices from data/prices"""
        ...

    def read_lean_versions(self) -> QuantConnect.Api.VersionsResponse:
        """Gets a list of LEAN versions with their corresponding basic descriptions"""
        ...

    def read_live_algorithm(self, project_id: int, deploy_id: str) -> QuantConnect.Api.LiveAlgorithmResults:
        """
        Read out a live algorithm in the project id specified.
        
        :param project_id: Project id to read
        :param deploy_id: Specific instance id to read
        :returns: Live object with the results.
        """
        ...

    def read_live_chart(self, project_id: int, name: str, start: int, end: int, count: int) -> QuantConnect.Api.ReadChartResponse:
        """
        Returns a chart object from a live algorithm
        
        :param project_id: Project ID of the request
        :param name: The requested chart name
        :param start: The Utc start seconds timestamp of the request
        :param end: The Utc end seconds timestamp of the request
        :param count: The number of data points to request
        """
        ...

    def read_live_insights(self, project_id: int, start: int = 0, end: int = 0) -> QuantConnect.Api.InsightResponse:
        """
        Read out the insights of a live algorithm
        
        :param project_id: Id of the project from which to read the live algorithm
        :param start: Starting index of the insights to be fetched
        :param end: Last index of the insights to be fetched. Note that end - start must be less than 100
        :returns: InsightResponse.
        """
        ...

    def read_live_logs(self, project_id: int, algorithm_id: str, start_line: int, end_line: int) -> QuantConnect.Api.LiveLog:
        """
        Gets the logs of a specific live algorithm
        
        :param project_id: Project Id of the live running algorithm
        :param algorithm_id: Algorithm Id of the live running algorithm
        :param start_line: Start line of logs to read
        :param end_line: End line of logs to read
        :returns: List of strings that represent the logs of the algorithm.
        """
        ...

    def read_live_portfolio(self, project_id: int) -> QuantConnect.Api.PortfolioResponse:
        """
        Read out the portfolio state of a live algorithm
        
        :param project_id: Id of the project from which to read the live algorithm
        :returns: PortfolioResponse.
        """
        ...

    def read_optimization(self, optimization_id: str) -> QuantConnect.Api.Optimization:
        """
        Read an optimization
        
        :param optimization_id: Optimization id for the optimization we want to read
        :returns: Optimization.
        """
        ...

    def read_organization(self, organization_id: str = None) -> QuantConnect.Api.Organization:
        """Fetch organization data from web API"""
        ...

    def read_project(self, project_id: int) -> QuantConnect.Api.ProjectResponse:
        """
        Read in a project from the QuantConnect.com API.
        
        :param project_id: Project id you own
        :returns: ProjectResponse about a specific project.
        """
        ...

    def read_project_file(self, project_id: int, file_name: str) -> QuantConnect.Api.ProjectFilesResponse:
        """
        Read a file in a project
        
        :param project_id: Project id to which the file belongs
        :param file_name: The name of the file
        :returns: ProjectFilesResponse that includes the file information.
        """
        ...

    def read_project_files(self, project_id: int) -> QuantConnect.Api.ProjectFilesResponse:
        """
        Read all files in a project
        
        :param project_id: Project id to which the file belongs
        :returns: ProjectFilesResponse that includes the information about all files in the project.
        """
        ...

    def read_project_nodes(self, project_id: int) -> QuantConnect.Api.ProjectNodesResponse:
        """
        Read all nodes in a project.
        
        :param project_id: Project id to which the nodes refer
        :returns: ProjectNodesResponse that includes the information about all nodes in the project.
        """
        ...

    def send_notification(self, notification: QuantConnect.Notifications.Notification, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Sends a notification
        
        :param notification: The notification to send
        :param project_id: The project id
        :returns: RestResponse containing success response and errors.
        """
        ...

    def send_statistics(self, algorithm_id: str, unrealized: float, fees: float, net_profit: float, holdings: float, equity: float, net_return: float, volume: float, trades: int, sharpe: float) -> None:
        """
        Send the statistics to storage for performance tracking.
        
        :param algorithm_id: Identifier for algorithm
        :param unrealized: Unrealized gainloss
        :param fees: Total fees
        :param net_profit: Net profi
        :param holdings: Algorithm holdings
        :param equity: Total equity
        :param net_return: Algorithm return
        :param volume: Volume traded
        :param trades: Total trades since inception
        :param sharpe: Sharpe ratio since inception
        """
        ...

    def send_user_email(self, algorithm_id: str, subject: str, body: str) -> None:
        """
        Send an email to the user associated with the specified algorithm id
        
        :param algorithm_id: The algorithm id
        :param subject: The email subject
        :param body: The email message body
        """
        ...

    def set_algorithm_status(self, algorithm_id: str, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """
        Set the algorithm status from the worker to update the UX e.g. if there was an error.
        
        :param algorithm_id: Algorithm id we're setting.
        :param status: Status enum of the current worker
        :param message: Message for the algorithm status event
        """
        ...

    def set_object_store(self, organization_id: str, key: str, object_data: typing.List[int]) -> QuantConnect.Api.RestResponse:
        """
        Upload files to the Object Store
        
        :param organization_id: Organization ID we would like to upload the file to
        :param key: Key to the Object Store file
        :param object_data: File to be uploaded
        :returns: RestResponse.
        """
        ...

    def stop_live_algorithm(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Stop a live algorithm from the specified project.
        
        :param project_id: Project for the live algo we want to delete
        """
        ...

    def update_backtest(self, project_id: int, backtest_id: str, name: str = ..., note: str = ...) -> QuantConnect.Api.RestResponse:
        """
        Update the backtest name
        
        :param project_id: Project id to update
        :param backtest_id: Backtest id to update
        :param name: New backtest name to set
        :param note: Note attached to the backtest
        :returns: Rest response on success.
        """
        ...

    def update_optimization(self, optimization_id: str, name: str = None) -> QuantConnect.Api.RestResponse:
        """
        Update an optimization
        
        :param optimization_id: Optimization id we want to update
        :param name: Name we'd like to assign to the optimization
        :returns: RestResponse.
        """
        ...

    def update_project_file_content(self, project_id: int, file_name: str, new_file_contents: str) -> QuantConnect.Api.RestResponse:
        """
        Update the contents of a file
        
        :param project_id: Project id to which the file belongs
        :param file_name: The name of the file that should be updated
        :param new_file_contents: The new contents of the file
        :returns: RestResponse indicating success.
        """
        ...

    def update_project_file_name(self, project_id: int, old_file_name: str, new_file_name: str) -> QuantConnect.Api.RestResponse:
        """
        Update the name of a file
        
        :param project_id: Project id to which the file belongs
        :param old_file_name: The current name of the file
        :param new_file_name: The new name for the file
        :returns: RestResponse indicating success.
        """
        ...

    def update_project_nodes(self, project_id: int, nodes: typing.List[str]) -> QuantConnect.Api.ProjectNodesResponse:
        """
        Update the active state of some nodes to true.
        If you don't provide any nodes, all the nodes become inactive and AutoSelectNode is true.
        
        :param project_id: Project id to which the nodes refer
        :param nodes: List of node ids to update
        :returns: ProjectNodesResponse that includes the information about all nodes in the project.
        """
        ...


class IJobQueueHandler(metaclass=abc.ABCMeta):
    """Task requestor interface with cloud system"""

    def acknowledge_job(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Signal task complete
        
        :param job: Work to do.
        """
        ...

    def initialize(self, api: QuantConnect.Interfaces.IApi) -> None:
        """Initialize the internal state"""
        ...

    def next_job(self, algorithm_path: typing.Optional[str]) -> typing.Union[QuantConnect.Packets.AlgorithmNodePacket, str]:
        """
        Request the next task to run through the engine:
        
        :returns: Algorithm job to process.
        """
        ...


class DataProviderNewDataRequestEventArgs(System.EventArgs):
    """Event arguments for the IDataProvider.NewDataRequest event"""

    @property
    def path(self) -> str:
        """Path to the fetched data"""
        ...

    @property
    def succeeded(self) -> bool:
        """Whether the data was fetched successfully"""
        ...

    @property
    def error_message(self) -> str:
        """Any error message that occurred during the fetch"""
        ...

    def __init__(self, path: str, succeeded: bool, errorMessage: str) -> None:
        """
        Initializes a new instance of the DataProviderNewDataRequestEventArgs class
        
        :param path: The path to the fetched data
        :param succeeded: Whether the data was fetched successfully
        :param errorMessage: Any error message that occured during the fetch
        """
        ...


class IDataMonitor(System.IDisposable, metaclass=abc.ABCMeta):
    """Monitors data requests and reports on missing data"""

    def exit(self) -> None:
        """Terminates the data monitor generating a final report"""
        ...

    def on_new_data_request(self, sender: typing.Any, e: QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs) -> None:
        """Event handler for the IDataProvider.NewDataRequest event"""
        ...


class ISecurityInitializerProvider(metaclass=abc.ABCMeta):
    """Reduced interface which provides an instance which implements ISecurityInitializer"""

    @property
    @abc.abstractmethod
    def security_initializer(self) -> QuantConnect.Securities.ISecurityInitializer:
        """Gets an instance that is to be used to initialize newly created securities."""
        ...


class IAccountCurrencyProvider(metaclass=abc.ABCMeta):
    """A reduced interface for an account currency provider"""

    @property
    @abc.abstractmethod
    def account_currency(self) -> str:
        """Gets the account currency"""
        ...


class ITimeKeeper(metaclass=abc.ABCMeta):
    """Interface implemented by TimeKeeper"""

    @property
    @abc.abstractmethod
    def utc_time(self) -> datetime.datetime:
        """Gets the current time in UTC"""
        ...

    def add_time_zone(self, time_zone: typing.Any) -> None:
        """Adds the specified time zone to this time keeper"""
        ...

    def get_local_time_keeper(self, time_zone: typing.Any) -> QuantConnect.LocalTimeKeeper:
        """
        Gets the LocalTimeKeeper instance for the specified time zone
        
        :param time_zone: The time zone whose LocalTimeKeeper we seek
        :returns: The LocalTimeKeeper instance for the specified time zone.
        """
        ...


class IDataProviderEvents(metaclass=abc.ABCMeta):
    """Events related to data providers"""

    @property
    @abc.abstractmethod
    def invalid_configuration_detected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.InvalidConfigurationDetectedEventArgs], None], None]:
        """Event fired when an invalid configuration has been detected"""
        ...

    @property
    @abc.abstractmethod
    def numerical_precision_limited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.NumericalPrecisionLimitedEventArgs], None], None]:
        """Event fired when the numerical precision in the factor file has been limited"""
        ...

    @property
    @abc.abstractmethod
    def download_failed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.DownloadFailedEventArgs], None], None]:
        """Event fired when there was an error downloading a remote file"""
        ...

    @property
    @abc.abstractmethod
    def reader_error_detected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.ReaderErrorDetectedEventArgs], None], None]:
        """Event fired when there was an error reading the data"""
        ...

    @property
    @abc.abstractmethod
    def start_date_limited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.StartDateLimitedEventArgs], None], None]:
        """Event fired when the start date has been limited"""
        ...


class IHistoryProvider(QuantConnect.Interfaces.IDataProviderEvents, metaclass=abc.ABCMeta):
    """Provides historical data to an algorithm at runtime"""

    @property
    @abc.abstractmethod
    def data_point_count(self) -> int:
        """Gets the total number of data points emitted by this history provider"""
        ...

    def get_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param slice_time_zone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
        """
        ...


class ITradeBuilder(metaclass=abc.ABCMeta):
    """Generates trades from executions and market price updates"""

    @property
    @abc.abstractmethod
    def closed_trades(self) -> System.Collections.Generic.List[QuantConnect.Statistics.Trade]:
        """The list of closed trades"""
        ...

    def apply_split(self, split: QuantConnect.Data.Market.Split, live_mode: bool, data_normalization_mode: QuantConnect.DataNormalizationMode) -> None:
        """
        Applies a split to the trade builder
        
        :param split: The split to be applied
        :param live_mode: True if live mode, false for backtest
        :param data_normalization_mode: The DataNormalizationMode for this security
        """
        ...

    def has_open_position(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Returns true if there is an open position for the symbol
        
        :param symbol: The symbol
        :returns: true if there is an open position for the symbol.
        """
        ...

    def process_fill(self, fill: QuantConnect.Orders.OrderEvent, security_conversion_rate: float, fee_in_account_currency: float, multiplier: float = 1.0) -> None:
        """
        Processes a new fill, eventually creating new trades
        
        :param fill: The new fill order event
        :param security_conversion_rate: The current security market conversion rate into the account currency
        :param fee_in_account_currency: The current order fee in the account currency
        :param multiplier: The contract multiplier
        """
        ...

    def set_live_mode(self, live: bool) -> None:
        """
        Sets the live mode flag
        
        :param live: The live mode flag
        """
        ...

    def set_market_price(self, symbol: typing.Union[QuantConnect.Symbol, str], price: float) -> None:
        """Sets the current market price for the symbol"""
        ...

    def set_security_manager(self, securities: QuantConnect.Securities.SecurityManager) -> None:
        """
        Sets the security manager instance
        
        :param securities: The security manager
        """
        ...


class IAlgorithmSettings(metaclass=abc.ABCMeta):
    """User settings for the algorithm which can be changed in the IAlgorithm.Initialize method"""

    @property
    @abc.abstractmethod
    def automatic_indicator_warm_up(self) -> bool:
        """Gets whether or not WarmUpIndicator is allowed to warm up indicators"""
        ...

    @property.setter
    def automatic_indicator_warm_up(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def rebalance_portfolio_on_security_changes(self) -> typing.Optional[bool]:
        """True if should rebalance portfolio on security changes. True by default"""
        ...

    @property.setter
    def rebalance_portfolio_on_security_changes(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    @abc.abstractmethod
    def rebalance_portfolio_on_insight_changes(self) -> typing.Optional[bool]:
        """True if should rebalance portfolio on new insights or expiration of insights. True by default"""
        ...

    @property.setter
    def rebalance_portfolio_on_insight_changes(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    @abc.abstractmethod
    def max_absolute_portfolio_target_percentage(self) -> float:
        """The absolute maximum valid total portfolio value target percentage"""
        ...

    @property.setter
    def max_absolute_portfolio_target_percentage(self, value: float) -> None:
        ...

    @property
    @abc.abstractmethod
    def min_absolute_portfolio_target_percentage(self) -> float:
        """The absolute minimum valid total portfolio value target percentage"""
        ...

    @property.setter
    def min_absolute_portfolio_target_percentage(self, value: float) -> None:
        ...

    @property
    @abc.abstractmethod
    def minimum_order_margin_portfolio_percentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, or orders with unrealistic sizes"""
        ...

    @property.setter
    def minimum_order_margin_portfolio_percentage(self, value: float) -> None:
        ...

    @property
    @abc.abstractmethod
    def free_portfolio_value(self) -> typing.Optional[float]:
        """
        Gets/sets the SetHoldings buffers value.
        The buffer is used for orders not to be rejected due to volatility when using SetHoldings and CalculateOrderQuantity
        """
        ...

    @property.setter
    def free_portfolio_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    @abc.abstractmethod
    def free_portfolio_value_percentage(self) -> float:
        """
        Gets/sets the SetHoldings buffers value percentage.
        This percentage will be used to set the FreePortfolioValue
        based on the SecurityPortfolioManager.TotalPortfolioValue
        """
        ...

    @property.setter
    def free_portfolio_value_percentage(self, value: float) -> None:
        ...

    @property
    @abc.abstractmethod
    def liquidate_enabled(self) -> bool:
        """Gets/sets if Liquidate() is enabled"""
        ...

    @property.setter
    def liquidate_enabled(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def daily_precise_end_time(self) -> bool:
        """True if daily strict end times are enabled"""
        ...

    @property.setter
    def daily_precise_end_time(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def daily_consolidation_use_extended_market_hours(self) -> bool:
        """True if extended market hours should be used for daily consolidation, when extended market hours is enabled"""
        ...

    @property.setter
    def daily_consolidation_use_extended_market_hours(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def data_subscription_limit(self) -> int:
        """
        Gets/sets the maximum number of concurrent market data subscriptions available
        
        This property is deprecated. Please observe data subscription limits set by your brokerage to avoid runtime errors.
        """
        warnings.warn("This property is deprecated. Please observe data subscription limits set by your brokerage to avoid runtime errors.", DeprecationWarning)

    @property.setter
    def data_subscription_limit(self, value: int) -> None:
        warnings.warn("This property is deprecated. Please observe data subscription limits set by your brokerage to avoid runtime errors.", DeprecationWarning)

    @property
    @abc.abstractmethod
    def stale_price_time_span(self) -> datetime.timedelta:
        """Gets the minimum time span elapsed to consider a market fill price as stale (defaults to one hour)"""
        ...

    @property.setter
    def stale_price_time_span(self, value: datetime.timedelta) -> None:
        ...

    @property
    @abc.abstractmethod
    def warmup_resolution(self) -> typing.Optional[QuantConnect.Resolution]:
        """The warmup resolution to use if any"""
        ...

    @property.setter
    def warmup_resolution(self, value: typing.Optional[QuantConnect.Resolution]) -> None:
        ...

    @property
    @abc.abstractmethod
    def trading_days_per_year(self) -> typing.Optional[int]:
        """Gets or sets the number of trading days per year for this Algorithm's portfolio statistics."""
        ...

    @property.setter
    def trading_days_per_year(self, value: typing.Optional[int]) -> None:
        ...

    @property
    @abc.abstractmethod
    def databases_refresh_period(self) -> datetime.timedelta:
        """Gets the time span used to refresh the market hours and symbol properties databases"""
        ...

    @property.setter
    def databases_refresh_period(self, value: datetime.timedelta) -> None:
        ...


class IOptionChainProvider(metaclass=abc.ABCMeta):
    """Provides the full option chain for a given underlying."""

    def get_option_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of option contracts for a given underlying symbol
        
        :param symbol: The option or the underlying symbol to get the option chain for. Providing the option allows targetting an option ticker different than the default e.g. SPXW
        :param date: The date for which to request the option chain (only used in backtesting)
        :returns: The list of option contracts.
        """
        ...


class IFutureChainProvider(metaclass=abc.ABCMeta):
    """Provides the full future chain for a given underlying."""

    def get_future_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...


class IOrderProperties(metaclass=abc.ABCMeta):
    """Contains additional properties and settings for an order"""

    @property
    @abc.abstractmethod
    def time_in_force(self) -> QuantConnect.Orders.TimeInForce:
        """Defines the length of time over which an order will continue working before it is cancelled"""
        ...

    @property.setter
    def time_in_force(self, value: QuantConnect.Orders.TimeInForce) -> None:
        ...

    def clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Returns a new instance clone of this object"""
        ...


class ObjectStoreErrorRaisedEventArgs(System.EventArgs):
    """Event arguments for the IObjectStore.ErrorRaised event"""

    @property
    def error(self) -> System.Exception:
        """Gets the Exception that was raised"""
        ...

    def __init__(self, error: System.Exception) -> None:
        """
        Initializes a new instance of the ObjectStoreErrorRaisedEventArgs class
        
        :param error: The error that was raised
        """
        ...


class IObjectStore(System.IDisposable, metaclass=abc.ABCMeta):
    """Provides object storage for data persistence."""

    @property
    @abc.abstractmethod
    def error_raised(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.ObjectStoreErrorRaisedEventArgs], None], None]:
        """Event raised each time there's an error"""
        ...

    @property
    @abc.abstractmethod
    def keys(self) -> System.Collections.Generic.ICollection[str]:
        """Returns the file paths present in the object store. This is specially useful not to load the object store into memory"""
        ...

    def clear(self) -> None:
        """Will clear the object store state cache. This is useful when the object store is used concurrently by nodes which want to share information"""
        ...

    def contains_key(self, path: str) -> bool:
        """
        Determines whether the store contains data for the specified path
        
        :param path: The object path
        :returns: True if the key was found.
        """
        ...

    def delete(self, path: str) -> bool:
        """
        Deletes the object data for the specified path
        
        :param path: The object path
        :returns: True if the delete operation was successful.
        """
        ...

    def get_file_path(self, path: str) -> str:
        """
        Returns the file path for the specified path
        
        :param path: The object path
        :returns: The path for the file.
        """
        ...

    def initialize(self, user_id: int, project_id: int, user_token: str, controls: QuantConnect.Packets.Controls) -> None:
        """
        Initializes the object store
        
        :param user_id: The user id
        :param project_id: The project id
        :param user_token: The user token
        :param controls: The job controls instance
        """
        ...

    def read_bytes(self, path: str) -> typing.List[int]:
        """
        Returns the object data for the specified key
        
        :param path: The object key
        :returns: A byte array containing the data.
        """
        ...

    def save_bytes(self, path: str, contents: typing.List[int]) -> bool:
        """
        Saves the object data for the specified path
        
        :param path: The object path
        :param contents: The object data
        :returns: True if the save operation was successful.
        """
        ...


class IAlgorithm(QuantConnect.Interfaces.ISecurityInitializerProvider, QuantConnect.Interfaces.IAccountCurrencyProvider, metaclass=abc.ABCMeta):
    """
    Interface for QuantConnect algorithm implementations. All algorithms must implement these
    basic members to allow interaction with the Lean Backtesting Engine.
    """

    @property
    @abc.abstractmethod
    def insights_generated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, QuantConnect.Algorithm.Framework.Alphas.GeneratedInsightsCollection], None], None]:
        """Event fired when an algorithm generates a insight"""
        ...

    @property
    @abc.abstractmethod
    def time_keeper(self) -> QuantConnect.Interfaces.ITimeKeeper:
        """Gets the time keeper instance"""
        ...

    @property
    @abc.abstractmethod
    def subscription_manager(self) -> QuantConnect.Data.SubscriptionManager:
        """
        Data subscription manager controls the information and subscriptions the algorithms recieves.
        Subscription configurations can be added through the Subscription Manager.
        """
        ...

    @property
    @abc.abstractmethod
    def project_id(self) -> int:
        """The project id associated with this algorithm if any"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    @abc.abstractmethod
    def securities(self) -> QuantConnect.Securities.SecurityManager:
        """
        Security object collection class stores an array of objects representing representing each security/asset
        we have a subscription for.
        """
        ...

    @property
    @abc.abstractmethod
    def universe_manager(self) -> QuantConnect.Securities.UniverseManager:
        """Gets the collection of universes for the algorithm"""
        ...

    @property
    @abc.abstractmethod
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """
        Security portfolio management class provides wrapper and helper methods for the Security.Holdings class such as
        IsLong, IsShort, TotalProfit
        """
        ...

    @property
    @abc.abstractmethod
    def transactions(self) -> QuantConnect.Securities.SecurityTransactionManager:
        """Security transaction manager class controls the store and processing of orders."""
        ...

    @property
    @abc.abstractmethod
    def brokerage_model(self) -> QuantConnect.Brokerages.IBrokerageModel:
        """Gets the brokerage model used to emulate a real brokerage"""
        ...

    @property
    @abc.abstractmethod
    def brokerage_name(self) -> QuantConnect.Brokerages.BrokerageName:
        """Gets the brokerage name."""
        ...

    @property
    @abc.abstractmethod
    def risk_free_interest_rate_model(self) -> QuantConnect.Data.IRiskFreeInterestRateModel:
        """Gets the risk free interest rate model used to get the interest rates"""
        ...

    @property
    @abc.abstractmethod
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
    @abc.abstractmethod
    def notify(self) -> QuantConnect.Notifications.NotificationManager:
        """Notification manager for storing and processing live event messages"""
        ...

    @property
    @abc.abstractmethod
    def schedule(self) -> QuantConnect.Scheduling.ScheduleManager:
        """Gets schedule manager for adding/removing scheduled events"""
        ...

    @property
    @abc.abstractmethod
    def history_provider(self) -> QuantConnect.Interfaces.IHistoryProvider:
        """Gets or sets the history provider for the algorithm"""
        ...

    @property.setter
    def history_provider(self, value: QuantConnect.Interfaces.IHistoryProvider) -> None:
        ...

    @property
    @abc.abstractmethod
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Gets or sets the current status of the algorithm"""
        ...

    @property.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    @abc.abstractmethod
    def is_warming_up(self) -> bool:
        """Gets whether or not this algorithm is still warming up"""
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Public name for the algorithm."""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    @abc.abstractmethod
    def tags(self) -> System.Collections.Generic.HashSet[str]:
        """A list of tags associated with the algorithm or the backtest, useful for categorization"""
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @property
    @abc.abstractmethod
    def name_updated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, str], None], None]:
        """Event fired algorithm's name is changed"""
        ...

    @property
    @abc.abstractmethod
    def tags_updated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, System.Collections.Generic.HashSet[str]], None], None]:
        """Event fired when the tag collection is updated"""
        ...

    @property
    @abc.abstractmethod
    def time(self) -> datetime.datetime:
        """Current date/time in the algorithm's local time zone"""
        ...

    @property
    @abc.abstractmethod
    def time_zone(self) -> typing.Any:
        """Gets the time zone of the algorithm"""
        ...

    @property
    @abc.abstractmethod
    def utc_time(self) -> datetime.datetime:
        """Current date/time in UTC."""
        ...

    @property
    @abc.abstractmethod
    def start_date(self) -> datetime.datetime:
        """Algorithm start date for backtesting, set by the SetStartDate methods."""
        ...

    @property
    @abc.abstractmethod
    def end_date(self) -> datetime.datetime:
        """Get Requested Backtest End Date"""
        ...

    @property
    @abc.abstractmethod
    def algorithm_id(self) -> str:
        """AlgorithmId for the backtest"""
        ...

    @property
    @abc.abstractmethod
    def live_mode(self) -> bool:
        """Algorithm is running on a live server."""
        ...

    @property
    @abc.abstractmethod
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    @property
    @abc.abstractmethod
    def deployment_target(self) -> QuantConnect.DeploymentTarget:
        """Deployment target, either local or cloud."""
        ...

    @property
    @abc.abstractmethod
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the subscription settings to be used when adding securities via universe selection"""
        ...

    @property
    @abc.abstractmethod
    def debug_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Debug messages from the strategy:"""
        ...

    @property
    @abc.abstractmethod
    def error_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Error messages from the strategy:"""
        ...

    @property
    @abc.abstractmethod
    def log_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Log messages from the strategy:"""
        ...

    @property
    @abc.abstractmethod
    def run_time_error(self) -> System.Exception:
        """Gets the run time error from the algorithm, or null if none was encountered."""
        ...

    @property.setter
    def run_time_error(self, value: System.Exception) -> None:
        ...

    @property
    @abc.abstractmethod
    def runtime_statistics(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, str]:
        """Customizable dynamic statistics displayed during live trading:"""
        ...

    @property
    @abc.abstractmethod
    def statistics(self) -> QuantConnect.Statistics.StatisticsResults:
        """The current algorithm statistics for the running algorithm."""
        ...

    @property
    @abc.abstractmethod
    def benchmark(self) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Gets the function used to define the benchmark. This function will return
        the value of the benchmark at a requested date/time
        """
        ...

    @property
    @abc.abstractmethod
    def trade_builder(self) -> QuantConnect.Interfaces.ITradeBuilder:
        """Gets the Trade Builder to generate trades from executions"""
        ...

    @property
    @abc.abstractmethod
    def settings(self) -> QuantConnect.Interfaces.IAlgorithmSettings:
        """Gets the user settings for the algorithm"""
        ...

    @property
    @abc.abstractmethod
    def option_chain_provider(self) -> QuantConnect.Interfaces.IOptionChainProvider:
        """Gets the option chain provider, used to get the list of option contracts for an underlying symbol"""
        ...

    @property
    @abc.abstractmethod
    def future_chain_provider(self) -> QuantConnect.Interfaces.IFutureChainProvider:
        """Gets the future chain provider, used to get the list of future contracts for an underlying symbol"""
        ...

    @property
    @abc.abstractmethod
    def insights(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightManager:
        """Gets the insight manager"""
        ...

    @property
    @abc.abstractmethod
    def object_store(self) -> QuantConnect.Storage.ObjectStore:
        """Gets the object store, used for persistence"""
        ...

    @property
    @abc.abstractmethod
    def current_slice(self) -> QuantConnect.Data.Slice:
        """Returns the current Slice object"""
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
        :param extended_market_hours: Show the after market data as well
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
        :param extended_market_hours: Show the after market data as well
        :returns: The new Option security.
        """
        ...

    @overload
    def add_security(self, security_type: QuantConnect.SecurityType, symbol: str, resolution: typing.Optional[QuantConnect.Resolution], market: str, fill_forward: bool, leverage: float, extended_market_hours: bool, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> QuantConnect.Securities.Security:
        """
        Set a required SecurityType-symbol and resolution for algorithm
        
        :param security_type: SecurityType Enum: Equity, Commodity, FOREX or Future
        :param symbol: Symbol Representation of the MarketType, e.g. AAPL
        :param resolution: Resolution of the MarketType required: MarketData, Second or Minute
        :param market: The market the requested security belongs to, such as 'usa' or 'fxcm'
        :param fill_forward: If true, returns the last available data even if none in that timeslice.
        :param leverage: leverage for this security
        :param extended_market_hours: ExtendedMarketHours send in data from 4am - 8pm, not used for FOREX
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
        """Send debug message"""
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
        
        :param symbol: Specific asset to liquidate, defaults to all.
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
        """Call this method at the end of each day of data."""
        ...

    @overload
    def on_end_of_day(self) -> None:
        """
        Call this method at the end of each day of data.
        
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
        Event fired each time that we add/remove securities from the data feed
        
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
        Sets the account currency cash symbol this algorithm is to manage, as well as
        the starting cash in this currency if given
        
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


class IBrokerageCashSynchronizer(metaclass=abc.ABCMeta):
    """Defines live brokerage cash synchronization operations."""

    @property
    @abc.abstractmethod
    def last_sync_date_time_utc(self) -> datetime.datetime:
        """Gets the datetime of the last sync (UTC)"""
        ...

    def perform_cash_sync(self, algorithm: QuantConnect.Interfaces.IAlgorithm, current_time_utc: typing.Union[datetime.datetime, datetime.date], get_time_since_last_fill: typing.Callable[[], datetime.timedelta]) -> bool:
        """
        Synchronizes the cashbook with the brokerage account
        
        :param algorithm: The algorithm instance
        :param current_time_utc: The current time (UTC)
        :param get_time_since_last_fill: A function which returns the time elapsed since the last fill
        :returns: True if the cash sync was performed successfully.
        """
        ...

    def should_perform_cash_sync(self, current_time_utc: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Returns whether the brokerage should perform the cash synchronization
        
        :param current_time_utc: The current time (UTC)
        :returns: True if the cash sync should be performed.
        """
        ...


class IRegressionResearchDefinition(metaclass=abc.ABCMeta):
    """Defines interface for research notebooks to be run as part of the research test suite."""

    @property
    @abc.abstractmethod
    def expected_output(self) -> str:
        ...


class IDataQueueHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Task requestor interface with cloud system"""

    @property
    @abc.abstractmethod
    def is_connected(self) -> bool:
        """Returns whether the data provider is connected"""
        ...

    def set_job(self, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Sets the job we're subscribing for
        
        :param job: Job we're subscribing for
        """
        ...

    def subscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig, new_data_available_handler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Subscribe to the specified configuration
        
        :param data_config: defines the parameters to subscribe to a data feed
        :param new_data_available_handler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def unsubscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Removes the specified configuration
        
        :param data_config: Subscription config to be removed
        """
        ...


class ITimeInForceHandler(metaclass=abc.ABCMeta):
    """Handles the time in force for an order"""

    def is_fill_valid(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> bool:
        """
        Checks if an order fill is valid
        
        :param security: The security matching the order
        :param order: The order to be checked
        :param fill: The order fill to be checked
        :returns: Returns true if the order fill can be emitted, false otherwise.
        """
        ...

    def is_order_expired(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Checks if an order is expired
        
        :param security: The security matching the order
        :param order: The order to be checked
        :returns: Returns true if the order has expired, false otherwise.
        """
        ...


class ISecurityPrice(metaclass=abc.ABCMeta):
    """
    Reduced interface which allows setting and accessing
    price properties for a Security
    """

    @property
    @abc.abstractmethod
    def price(self) -> float:
        """Get the current value of the security."""
        ...

    @property
    @abc.abstractmethod
    def close(self) -> float:
        """If this uses trade bar data, return the most recent close."""
        ...

    @property
    @abc.abstractmethod
    def volume(self) -> float:
        """Access to the volume of the equity today"""
        ...

    @property
    @abc.abstractmethod
    def bid_price(self) -> float:
        """Gets the most recent bid price if available"""
        ...

    @property
    @abc.abstractmethod
    def bid_size(self) -> float:
        """Gets the most recent bid size if available"""
        ...

    @property
    @abc.abstractmethod
    def ask_price(self) -> float:
        """Gets the most recent ask price if available"""
        ...

    @property
    @abc.abstractmethod
    def ask_size(self) -> float:
        """Gets the most recent ask size if available"""
        ...

    @property
    @abc.abstractmethod
    def open_interest(self) -> int:
        """Access to the open interest of the security today"""
        ...

    @property
    @abc.abstractmethod
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol for the asset."""
        ...

    @property
    @abc.abstractmethod
    def symbol_properties(self) -> QuantConnect.Securities.SymbolProperties:
        """SymbolProperties of the symbol"""
        ...

    def get_last_data(self) -> QuantConnect.Data.BaseData:
        """
        Get the last price update set to the security.
        
        :returns: BaseData object for this security.
        """
        ...

    def set_market_price(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Update any security properties based on the latest market data and time
        
        :param data: New data packet from LEAN
        """
        ...

    def update(self, data: System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData], data_type: typing.Type, contains_fill_forward_data: typing.Optional[bool]) -> None:
        """
        Updates all of the security properties, such as price/OHLCV/bid/ask based
        on the data provided. Data is also stored into the security's data cache
        
        :param data: The security update data
        :param data_type: The data type
        :param contains_fill_forward_data: Flag indicating whether  contains any fill forward bar or not
        """
        ...


class IBrokerage(QuantConnect.Interfaces.IBrokerageCashSynchronizer, System.IDisposable, metaclass=abc.ABCMeta):
    """
    Brokerage interface that defines the operations all brokerages must implement. The IBrokerage implementation
    must have a matching IBrokerageFactory implementation.
    """

    @property
    @abc.abstractmethod
    def order_id_changed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.BrokerageOrderIdChangedEvent], None], None]:
        """Event that fires each time the brokerage order id changes"""
        ...

    @property
    @abc.abstractmethod
    def orders_status_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]], None], None]:
        """Event that fires each time the status for a list of orders change"""
        ...

    @property
    @abc.abstractmethod
    def order_updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.OrderUpdateEvent], None], None]:
        """Event that fires each time an order is updated in the brokerage side"""
        ...

    @property
    @abc.abstractmethod
    def option_position_assigned(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.OrderEvent], None], None]:
        """Event that fires each time a short option position is assigned"""
        ...

    @property
    @abc.abstractmethod
    def option_notification(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.OptionNotificationEventArgs], None], None]:
        """Event that fires each time an option position has changed"""
        ...

    @property
    @abc.abstractmethod
    def new_brokerage_order_notification(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.NewBrokerageOrderNotificationEventArgs], None], None]:
        """Event that fires each time there's a brokerage side generated order"""
        ...

    @property
    @abc.abstractmethod
    def delisting_notification(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.DelistingNotificationEventArgs], None], None]:
        """Event that fires each time a delisting occurs"""
        ...

    @property
    @abc.abstractmethod
    def account_changed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Securities.AccountEvent], None], None]:
        """Event that fires each time a user's brokerage account is changed"""
        ...

    @property
    @abc.abstractmethod
    def message(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.BrokerageMessageEvent], None], None]:
        """Event that fires when a message is received from the brokerage"""
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Gets the name of the brokerage"""
        ...

    @property
    @abc.abstractmethod
    def is_connected(self) -> bool:
        """Returns true if we're currently connected to the broker"""
        ...

    @property
    @abc.abstractmethod
    def account_instantly_updated(self) -> bool:
        """Specifies whether the brokerage will instantly update account balances"""
        ...

    @property
    @abc.abstractmethod
    def account_base_currency(self) -> str:
        """Returns the brokerage account's base currency"""
        ...

    def cancel_order(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Cancels the order with the specified ID
        
        :param order: The order to cancel
        :returns: True if the request was made for the order to be canceled, false otherwise.
        """
        ...

    def connect(self) -> None:
        """Connects the client to the broker's remote servers"""
        ...

    def disconnect(self) -> None:
        """Disconnects the client from the broker's remote servers"""
        ...

    def get_account_holdings(self) -> System.Collections.Generic.List[QuantConnect.Holding]:
        """
        Gets all holdings for the account
        
        :returns: The current holdings from the account.
        """
        ...

    def get_cash_balance(self) -> System.Collections.Generic.List[QuantConnect.Securities.CashAmount]:
        """
        Gets the current cash balance for each currency held in the brokerage account
        
        :returns: The current cash balance for each currency available for trading.
        """
        ...

    def get_history(self, request: QuantConnect.Data.HistoryRequest) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Gets the history for the requested security
        
        :param request: The historical data request
        :returns: An enumerable of bars covering the span specified in the request.
        """
        ...

    def get_open_orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets all open orders on the account
        
        :returns: The open orders returned from IB.
        """
        ...

    def place_order(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Places a new order and assigns a new broker ID to the order
        
        :param order: The order to be placed
        :returns: True if the request for a new order has been placed, false otherwise.
        """
        ...

    def update_order(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Updates the order with the same id
        
        :param order: The new order information
        :returns: True if the request was made for the order to be updated, false otherwise.
        """
        ...


class IDataProvider(metaclass=abc.ABCMeta):
    """
    Fetches a remote file for a security.
    Must save the file to Globals.DataFolder.
    """

    @property
    @abc.abstractmethod
    def new_data_request(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], None], None]:
        """Event raised each time data fetch is finished (successfully or not)"""
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data to be used in an algorithm
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...


class IMapFileProvider(metaclass=abc.ABCMeta):
    """Provides instances of MapFileResolver at run time"""

    def get(self, auxiliary_data_key: QuantConnect.Data.Auxiliary.AuxiliaryDataKey) -> QuantConnect.Data.Auxiliary.MapFileResolver:
        """
        Gets a MapFileResolver representing all the map
        files for the specified market
        
        :param auxiliary_data_key: Key used to fetch a map file resolver. Specifying market and security type
        :returns: A MapFileResolver containing all map files for the specified market.
        """
        ...

    def initialize(self, data_provider: QuantConnect.Interfaces.IDataProvider) -> None:
        """
        Initializes our MapFileProvider by supplying our data_provider
        
        :param data_provider: DataProvider to use
        """
        ...


class IFactorFileProvider(metaclass=abc.ABCMeta):
    """Provides instances of FactorFile{T} at run time"""

    def get(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Auxiliary.IFactorProvider:
        """
        Gets a FactorFile{T} instance for the specified symbol, or null if not found
        
        :param symbol: The security's symbol whose factor file we seek
        :returns: The resolved factor file, or null if not found.
        """
        ...

    def initialize(self, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider) -> None:
        """
        Initializes our FactorFileProvider by supplying our map_file_provider
        and data_provider
        
        :param map_file_provider: MapFileProvider to use
        :param data_provider: DataProvider to use
        """
        ...


class ISubscriptionDataConfigProvider(metaclass=abc.ABCMeta):
    """Reduced interface which provides access to registered SubscriptionDataConfig"""

    def get_subscription_data_configs(self, symbol: typing.Union[QuantConnect.Symbol, str] = None, include_internal_configs: bool = False) -> System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Gets a list of all registered SubscriptionDataConfig for a given Symbol if any
        else will return the whole list of subscriptions
        """
        ...


class ISubscriptionDataConfigService(QuantConnect.Interfaces.ISubscriptionDataConfigProvider, metaclass=abc.ABCMeta):
    """
    This interface exposes methods for creating a list of SubscriptionDataConfig for a given
    configuration
    """

    @property
    @abc.abstractmethod
    def available_data_types(self) -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]:
        """Gets the available data types"""
        ...

    @overload
    def add(self, data_type: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, extended_market_hours: bool = False, is_filtered_subscription: bool = True, is_internal_feed: bool = False, is_custom_data: bool = False, data_normalization_mode: QuantConnect.DataNormalizationMode = ..., data_mapping_mode: QuantConnect.DataMappingMode = ..., contract_depth_offset: int = 0) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Creates and adds a list of SubscriptionDataConfig for a given symbol and configuration.
        Can optionally pass in desired subscription data type to use.
        If the config already existed will return existing instance instead
        """
        ...

    @overload
    def add(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, extended_market_hours: bool = False, is_filtered_subscription: bool = True, is_internal_feed: bool = False, is_custom_data: bool = False, subscription_data_types: System.Collections.Generic.List[System.Tuple[typing.Type, QuantConnect.TickType]] = None, data_normalization_mode: QuantConnect.DataNormalizationMode = ..., data_mapping_mode: QuantConnect.DataMappingMode = ..., contract_depth_offset: int = 0) -> System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Creates and adds a list of SubscriptionDataConfig for a given symbol and configuration.
        Can optionally pass in desired subscription data types to use.
        If the config already existed will return existing instance instead
        """
        ...

    def lookup_subscription_config_data_types(self, symbol_security_type: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, is_canonical: bool) -> System.Collections.Generic.List[System.Tuple[typing.Type, QuantConnect.TickType]]:
        """
        Get the data feed types for a given SecurityTypeResolution
        
        :param symbol_security_type: The SecurityType used to determine the types
        :param resolution: The resolution of the data requested
        :param is_canonical: Indicates whether the security is Canonical (future and options)
        :returns: Types that should be added to the SubscriptionDataConfig.
        """
        ...


class IShortableProvider(metaclass=abc.ABCMeta):
    """Defines a short list/easy-to-borrow provider"""

    def fee_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets interest rate charged on borrowed shares for a given asset.
        
        :param symbol: Symbol to lookup fee rate
        :param local_time: Time of the algorithm
        :returns: Fee rate. Zero if the data for the brokerage/date does not exist.
        """
        ...

    def rebate_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the Fed funds or other currency-relevant benchmark rate minus the interest rate charged on borrowed shares for a given asset.
        Interest rate - borrow fee rate = borrow rebate rate: 5.32% - 0.25% = 5.07%
        
        :param symbol: Symbol to lookup rebate rate
        :param local_time: Time of the algorithm
        :returns: Rebate fee. Zero if the data for the brokerage/date does not exist.
        """
        ...

    def shortable_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> typing.Optional[int]:
        """
        Gets the quantity shortable for a Symbol.
        
        :param symbol: Symbol to check shortable quantity
        :param local_time: Local time of the algorithm
        :returns: The quantity shortable for the given Symbol as a positive number. Null if the Symbol is shortable without restrictions.
        """
        ...


class IDataChannelProvider(metaclass=abc.ABCMeta):
    """Specifies data channel settings"""

    def initialize(self, packet: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Initializes the class with an algorithm node packet
        
        :param packet: Algorithm node packet
        """
        ...

    def should_stream_subscription(self, config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """True if this subscription configuration should be streamed"""
        ...


class IStreamReader(System.IDisposable, metaclass=abc.ABCMeta):
    """Defines a transport mechanism for data from its source into various reader methods"""

    @property
    @abc.abstractmethod
    def transport_medium(self) -> QuantConnect.SubscriptionTransportMedium:
        """Gets the transport medium of this stream reader"""
        ...

    @property
    @abc.abstractmethod
    def end_of_stream(self) -> bool:
        """Gets whether or not there's more data to be read in the stream"""
        ...

    @property
    @abc.abstractmethod
    def stream_reader(self) -> System.IO.StreamReader:
        """Direct access to the StreamReader instance"""
        ...

    @property
    @abc.abstractmethod
    def should_be_rate_limited(self) -> bool:
        """Gets whether or not this stream reader should be rate limited"""
        ...

    def read_line(self) -> str:
        """Gets the next line/batch of content from the stream"""
        ...


class IAlgorithmSubscriptionManager(QuantConnect.Interfaces.ISubscriptionDataConfigService, metaclass=abc.ABCMeta):
    """AlgorithmSubscriptionManager interface will manage the subscriptions for the SubscriptionManager"""

    @property
    @abc.abstractmethod
    def subscription_manager_subscriptions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]:
        """Gets all the current data config subscriptions that are being processed for the SubscriptionManager"""
        ...

    def subscription_manager_count(self) -> int:
        """Returns the amount of data config subscriptions processed for the SubscriptionManager"""
        ...


class IBusyCollection(typing.Generic[QuantConnect_Interfaces_IBusyCollection_T], System.IDisposable, metaclass=abc.ABCMeta):
    """Interface used to handle items being processed and communicate busy state"""

    @property
    @abc.abstractmethod
    def wait_handle(self) -> System.Threading.WaitHandle:
        """
        Gets a wait handle that can be used to wait until this instance is done
        processing all of it's item
        """
        ...

    @property
    @abc.abstractmethod
    def count(self) -> int:
        """Gets the number of items held within this collection"""
        ...

    @property
    @abc.abstractmethod
    def is_busy(self) -> bool:
        """Returns true if processing, false otherwise"""
        ...

    @overload
    def add(self, item: QuantConnect_Interfaces_IBusyCollection_T) -> None:
        """
        Adds the items to this collection
        
        :param item: The item to be added
        """
        ...

    @overload
    def add(self, item: QuantConnect_Interfaces_IBusyCollection_T, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Adds the items to this collection
        
        :param item: The item to be added
        :param cancellation_token: A cancellation token to observer
        """
        ...

    def complete_adding(self) -> None:
        """Marks the collection as not accepting any more additions"""
        ...

    @overload
    def get_consuming_enumerable(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Interfaces_IBusyCollection_T]:
        """
        Provides a consuming enumerable for items in this collection.
        
        :returns: An enumerable that removes and returns items from the collection.
        """
        ...

    @overload
    def get_consuming_enumerable(self, cancellation_token: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect_Interfaces_IBusyCollection_T]:
        """
        Provides a consuming enumerable for items in this collection.
        
        :param cancellation_token: A cancellation token to observer
        :returns: An enumerable that removes and returns items from the collection.
        """
        ...


class IDataPermissionManager(metaclass=abc.ABCMeta):
    """Entity in charge of handling data permissions"""

    @property
    @abc.abstractmethod
    def data_channel_provider(self) -> QuantConnect.Interfaces.IDataChannelProvider:
        """The data channel provider instance"""
        ...

    def assert_configuration(self, subscription_request: QuantConnect.Data.SubscriptionDataConfig, start_time_local: typing.Union[datetime.datetime, datetime.date], end_time_local: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Will assert the requested configuration is valid for the current job
        
        :param subscription_request: The data subscription configuration to assert
        :param start_time_local: The start time of this request
        :param end_time_local: The end time of this request
        """
        ...

    def initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Initialize the data permission manager
        
        :param job: The job packet
        """
        ...


class IDataCacheProvider(System.IDisposable, metaclass=abc.ABCMeta):
    """Defines a cache for data"""

    @property
    @abc.abstractmethod
    def is_data_ephemeral(self) -> bool:
        """Property indicating the data is temporary in nature and should not be cached"""
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Fetch data from the cache
        
        :param key: A string representing the key of the cached data
        :returns: An Stream of the cached data.
        """
        ...

    def get_zip_entries(self, zip_file: str) -> System.Collections.Generic.List[str]:
        """Returns a list of zip entries in a provided zip file"""
        ...

    def store(self, key: str, data: typing.List[int]) -> None:
        """
        Store the data in the cache
        
        :param key: The source of the data, used as a key to retrieve data in the cache
        :param data: The data to cache as a byte array
        """
        ...


class MessagingHandlerInitializeParameters(System.Object):
    """Parameters required to initialize a IMessagingHandler instance"""

    @property
    def api(self) -> QuantConnect.Interfaces.IApi:
        """The api instance to use"""
        ...

    def __init__(self, api: QuantConnect.Interfaces.IApi) -> None:
        """
        Creates a new instance
        
        :param api: The api instance to use
        """
        ...


class IExtendedDictionary(typing.Generic[QuantConnect_Interfaces_IExtendedDictionary_TKey, QuantConnect_Interfaces_IExtendedDictionary_TValue], metaclass=abc.ABCMeta):
    """Represents a generic collection of key/value pairs that implements python dictionary methods."""

    def clear(self) -> None:
        """Removes all keys and values from the IExtendedDictionary{TKey, TValue}."""
        ...

    def copy(self) -> typing.Any:
        """
        Creates a shallow copy of the IExtendedDictionary{TKey, TValue}.
        
        :returns: Returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
        """
        ...

    @overload
    def fromkeys(self, sequence: typing.List[QuantConnect_Interfaces_IExtendedDictionary_TKey]) -> typing.Any:
        """
        Creates a new dictionary from the given sequence of elements.
        
        :param sequence: Sequence of elements which is to be used as keys for the new dictionary
        :returns: Returns a new dictionary with the given sequence of elements as the keys of the dictionary.
        """
        ...

    @overload
    def fromkeys(self, sequence: typing.List[QuantConnect_Interfaces_IExtendedDictionary_TKey], value: QuantConnect_Interfaces_IExtendedDictionary_TValue) -> typing.Any:
        """
        Creates a new dictionary from the given sequence of elements with a value provided by the user.
        
        :param sequence: Sequence of elements which is to be used as keys for the new dictionary
        :param value: Value which is set to each each element of the dictionary
        :returns: Returns a new dictionary with the given sequence of elements as the keys of the dictionary. Each element of the newly created dictionary is set to the provided value.
        """
        ...

    @overload
    def get(self, key: QuantConnect_Interfaces_IExtendedDictionary_TKey) -> QuantConnect_Interfaces_IExtendedDictionary_TValue:
        """
        Returns the value for the specified key if key is in dictionary.
        
        :param key: Key to be searched in the dictionary
        :returns: The value for the specified key if key is in dictionary. None if the key is not found and value is not specified.
        """
        ...

    @overload
    def get(self, key: QuantConnect_Interfaces_IExtendedDictionary_TKey, value: QuantConnect_Interfaces_IExtendedDictionary_TValue) -> QuantConnect_Interfaces_IExtendedDictionary_TValue:
        """
        Returns the value for the specified key if key is in dictionary.
        
        :param key: Key to be searched in the dictionary
        :param value: Value to be returned if the key is not found. The default value is null.
        :returns: The value for the specified key if key is in dictionary. value if the key is not found and value is specified.
        """
        ...

    def items(self) -> typing.Any:
        """
        Returns a view object that displays a list of dictionary's (key, value) tuple pairs.
        
        :returns: Returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
        """
        ...

    def keys(self) -> typing.Any:
        """
        Returns a view object that displays a list of all the keys in the dictionary
        
        :returns: Returns a view object that displays a list of all the keys. When the dictionary is changed, the view object also reflect these changes.
        """
        ...

    @overload
    def pop(self, key: QuantConnect_Interfaces_IExtendedDictionary_TKey) -> QuantConnect_Interfaces_IExtendedDictionary_TValue:
        """
        Removes and returns an element from a dictionary having the given key.
        
        :param key: Key which is to be searched for removal
        :returns: If key is found - removed/popped element from the dictionary If key is not found - KeyError exception is raised.
        """
        ...

    @overload
    def pop(self, key: QuantConnect_Interfaces_IExtendedDictionary_TKey, default_value: QuantConnect_Interfaces_IExtendedDictionary_TValue) -> QuantConnect_Interfaces_IExtendedDictionary_TValue:
        """
        Removes and returns an element from a dictionary having the given key.
        
        :param key: Key which is to be searched for removal
        :param default_value: Value which is to be returned when the key is not in the dictionary
        :returns: If key is found - removed/popped element from the dictionary If key is not found - value specified as the second argument(default).
        """
        ...

    def popitem(self) -> typing.Any:
        """
        Returns and removes an arbitrary element (key, value) pair from the dictionary.
        
        :returns: Returns an arbitrary element (key, value) pair from the dictionary removes an arbitrary element(the same element which is returned) from the dictionary. Note: Arbitrary elements and random elements are not same.The popitem() doesn't return a random element.
        """
        ...

    @overload
    def setdefault(self, key: QuantConnect_Interfaces_IExtendedDictionary_TKey) -> QuantConnect_Interfaces_IExtendedDictionary_TValue:
        """
        Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
        
        :param key: Key with null/None value is inserted to the dictionary if key is not in the dictionary.
        :returns: The value of the key if it is in the dictionary None if key is not in the dictionary.
        """
        ...

    @overload
    def setdefault(self, key: QuantConnect_Interfaces_IExtendedDictionary_TKey, default_value: QuantConnect_Interfaces_IExtendedDictionary_TValue) -> QuantConnect_Interfaces_IExtendedDictionary_TValue:
        """
        Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
        
        :param key: Key with a value default_value is inserted to the dictionary if key is not in the dictionary.
        :param default_value: Default value
        :returns: The value of the key if it is in the dictionary default_value if key is not in the dictionary and default_value is specified.
        """
        ...

    def update(self, other: typing.Any) -> None:
        """
        Updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
        The update() method adds element(s) to the dictionary if the key is not in the dictionary.If the key is in the dictionary, it updates the key with the new value.
        
        :param other: Takes either a dictionary or an iterable object of key/value pairs (generally tuples).
        """
        ...

    def values(self) -> typing.Any:
        """
        Returns a view object that displays a list of all the values in the dictionary.
        
        :returns: Returns a view object that displays a list of all values in a given dictionary.
        """
        ...


class IOptionPrice(QuantConnect.Interfaces.ISecurityPrice, metaclass=abc.ABCMeta):
    """
    Reduced interface for accessing Option
    specific price properties and methods
    """

    @property
    @abc.abstractmethod
    def underlying(self) -> QuantConnect.Interfaces.ISecurityPrice:
        """Gets a reduced interface of the underlying security object."""
        ...

    def evaluate_price_model(self, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        """
        Evaluates the specified option contract to compute a theoretical price, IV and greeks
        
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: An instance of OptionPriceModelResult containing the theoretical price of the specified option contract.
        """
        ...


class IDataQueueUniverseProvider(metaclass=abc.ABCMeta):
    """
    This interface allows interested parties to lookup or enumerate the available symbols. Data source exposes it if this feature is available.
    Availability of a symbol doesn't imply that it is possible to trade it. This is a data source specific interface, not broker specific.
    """

    def can_perform_selection(self) -> bool:
        """
        Returns whether selection can take place or not.
        
        :returns: True if selection can take place.
        """
        ...

    def lookup_symbols(self, symbol: typing.Union[QuantConnect.Symbol, str], include_expired: bool, security_currency: str = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Method returns a collection of Symbols that are available at the data source.
        
        :param symbol: Symbol to lookup
        :param include_expired: Include expired contracts
        :param security_currency: Expected security currency(if any)
        :returns: Enumerable of Symbols, that are associated with the provided Symbol.
        """
        ...


class IDownloadProvider(metaclass=abc.ABCMeta):
    """Wrapper on the API for downloading data for an algorithm."""

    def download(self, address: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]], user_name: str, password: str) -> str:
        """
        Method for downloading data for an algorithm
        
        :param address: Source URL to download from
        :param headers: Headers to pass to the site
        :param user_name: Username for basic authentication
        :param password: Password for basic authentication
        :returns: String contents of file.
        """
        ...

    def download_bytes(self, address: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]], user_name: str, password: str) -> typing.List[int]:
        """
        Method for downloading data for an algorithm that can be read from a stream
        
        :param address: Source URL to download from
        :param headers: Headers to pass to the site
        :param user_name: Username for basic authentication
        :param password: Password for basic authentication
        :returns: String contents of file.
        """
        ...


class ISignalExportTarget(System.IDisposable, metaclass=abc.ABCMeta):
    """Interface to send positions holdings to different 3rd party API's"""

    def send(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters) -> bool:
        """
        Sends user's positions to certain 3rd party API
        
        :param parameters: Holdings the user have defined to be sent to certain 3rd party API and the algorithm being ran
        """
        ...


class IBrokerageFactory(System.IDisposable, metaclass=abc.ABCMeta):
    """Defines factory types for brokerages. Every IBrokerage is expected to also implement an IBrokerageFactory."""

    @property
    @abc.abstractmethod
    def brokerage_type(self) -> typing.Type:
        """Gets the type of brokerage produced by this factory"""
        ...

    @property
    @abc.abstractmethod
    def brokerage_data(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Gets the brokerage data required to run the brokerage from configuration/disk"""
        ...

    def create_brokerage(self, job: QuantConnect.Packets.LiveNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Interfaces.IBrokerage:
        """
        Creates a new IBrokerage instance
        
        :param job: The job packet to create the brokerage for
        :param algorithm: The algorithm instance
        :returns: A new brokerage instance.
        """
        ...

    def create_brokerage_message_handler(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi) -> QuantConnect.Brokerages.IBrokerageMessageHandler:
        """Gets a brokerage message handler"""
        ...

    def get_brokerage_model(self, order_provider: QuantConnect.Securities.IOrderProvider) -> QuantConnect.Brokerages.IBrokerageModel:
        """
        Gets a brokerage model that can be used to model this brokerage's unique behaviors
        
        :param order_provider: The order provider
        """
        ...


class IPrimaryExchangeProvider(metaclass=abc.ABCMeta):
    """Primary Exchange Provider interface"""

    def get_primary_exchange(self, security_identifier: QuantConnect.SecurityIdentifier) -> QuantConnect.Exchange:
        """
        Gets the primary exchange for a given security identifier
        
        :param security_identifier: The security identifier to get the primary exchange for
        :returns: Returns the primary exchange or null if not found.
        """
        ...


class ISecurityService(metaclass=abc.ABCMeta):
    """This interface exposes methods for creating a new Security"""

    def create_benchmark_security(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Security:
        """Creates a new benchmark security"""
        ...

    @overload
    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str], subscription_data_config_list: System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig], leverage: float = 0, add_to_symbol_cache: bool = True, underlying: QuantConnect.Securities.Security = None) -> QuantConnect.Securities.Security:
        """Creates a new security"""
        ...

    @overload
    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str], subscription_data_config: QuantConnect.Data.SubscriptionDataConfig, leverage: float = 0, add_to_symbol_cache: bool = True, underlying: QuantConnect.Securities.Security = None) -> QuantConnect.Securities.Security:
        """Creates a new security"""
        ...


class IMessagingHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Messaging System Plugin Interface.
    Provides a common messaging pattern between desktop and cloud implementations of QuantConnect.
    """

    @property
    @abc.abstractmethod
    def has_subscribers(self) -> bool:
        """
        Gets or sets whether this messaging handler has any current subscribers.
        When set to false, messages won't be sent.
        """
        ...

    @property.setter
    def has_subscribers(self, value: bool) -> None:
        ...

    def initialize(self, initialize_parameters: QuantConnect.Interfaces.MessagingHandlerInitializeParameters) -> None:
        """
        Initialize the Messaging System Plugin.
        
        :param initialize_parameters: The parameters required for initialization
        """
        ...

    def send(self, packet: QuantConnect.Packets.Packet) -> None:
        """
        Send any message with a base type of Packet.
        
        :param packet: Packet of data to send via the messaging system plugin
        """
        ...

    def send_notification(self, notification: QuantConnect.Notifications.Notification) -> None:
        """
        Send any notification with a base type of Notification.
        
        :param notification: The notification to be sent.
        """
        ...

    def set_authentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Set the user communication channel
        
        :param job: The job packet
        """
        ...


class IRegressionAlgorithmDefinition(metaclass=abc.ABCMeta):
    """
    Defines a C# algorithm as a regression algorithm to be run as part of the test suite.
    This interface also allows the algorithm to declare that it has versions in other languages
    that should yield identical results.
    """

    @property
    @abc.abstractmethod
    def algorithm_status(self) -> QuantConnect.AlgorithmStatus:
        """Final status of the algorithm"""
        ...

    @property
    @abc.abstractmethod
    def can_run_locally(self) -> bool:
        """This is used by the regression test system to indicate if the open source Lean repository has the required data to run this algorithm."""
        ...

    @property
    @abc.abstractmethod
    def languages(self) -> System.Collections.Generic.List[QuantConnect.Language]:
        """This is used by the regression test system to indicate which languages this algorithm is written in."""
        ...

    @property
    @abc.abstractmethod
    def data_points(self) -> int:
        """Data Points count of all timeslices of algorithm"""
        ...

    @property
    @abc.abstractmethod
    def algorithm_history_data_points(self) -> int:
        """Data Points count of the algorithm history"""
        ...

    @property
    @abc.abstractmethod
    def expected_statistics(self) -> System.Collections.Generic.Dictionary[str, str]:
        """This is used by the regression test system to indicate what the expected statistics are from running the algorithm"""
        ...


class _EventContainer(typing.Generic[QuantConnect_Interfaces__EventContainer_Callable, QuantConnect_Interfaces__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Interfaces__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Interfaces__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Interfaces__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


