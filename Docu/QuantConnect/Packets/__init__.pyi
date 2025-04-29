from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Notifications
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Generic
import System.IO


class LeakyBucketControlParameters(System.Object):
    """
    Provides parameters that control the behavior of a leaky bucket rate limiting algorithm. The
    parameter names below are phrased in the positive, such that the bucket is filled up over time
    vs leaking out over time.
    """

    default_capacity: int

    default_time_interval: int
    """Default time interval"""

    default_refill_amount: int
    """Default refill amount"""

    @property
    def capacity(self) -> int:
        """
        Sets the total capacity of the bucket in a leaky bucket algorithm. This is the maximum
        number of 'units' the bucket can hold and also defines the maximum burst rate, assuming
        instantaneous usage of 'units'. In reality, the usage of 'units' takes times, and so it
        is possible for the bucket to incrementally refill while consuming from the bucket.
        """
        ...

    @property.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def refill_amount(self) -> int:
        """
        Sets the refill amount of the bucket. This defines the quantity of 'units' that become available
        to a consuming entity after the time interval has elapsed. For example, if the refill amount is
        equal to one, then each time interval one new 'unit' will be made available for a consumer that is
        throttled by the leaky bucket.
        """
        ...

    @property.setter
    def refill_amount(self, value: int) -> None:
        ...

    @property
    def time_interval_minutes(self) -> int:
        """
        Sets the time interval for the refill amount of the bucket, in minutes. After this amount of wall-clock
        time has passed, the bucket will refill the refill amount, thereby making more 'units' available
        for a consumer. For example, if the refill amount equals 10 and the time interval is 30 minutes, then
        every 30 minutes, 10 more 'units' become available for a consumer. The available 'units' will
        continue to increase until the bucket capacity is reached.
        """
        ...

    @property.setter
    def time_interval_minutes(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the LeakyBucketControlParameters using default values"""
        ...

    @overload
    def __init__(self, capacity: int, refillAmount: int, timeIntervalMinutes: int) -> None:
        """
        Initializes a new instance of the LeakyBucketControlParameters with the specified value
        
        :param capacity: The total capacity of the bucket in minutes
        :param refillAmount: The number of additional minutes to add to the bucket after  has elapsed
        :param timeIntervalMinutes: The interval, in minutes, that must pass before the  is added back to the bucket for reuse
        """
        ...


class PacketType(Enum):
    """Classifications of internal packet system"""

    NONE = 0

    ALGORITHM_NODE = 1

    AUTOCOMPLETE_WORK = 2

    AUTOCOMPLETE_RESULT = 3

    BACKTEST_NODE = 4

    BACKTEST_RESULT = 5

    BACKTEST_WORK = 6

    LIVE_NODE = 7

    LIVE_RESULT = 8

    LIVE_WORK = 9

    SECURITY_TYPES = 10

    BACKTEST_ERROR = 11

    ALGORITHM_STATUS = 12

    BUILD_WORK = 13

    BUILD_SUCCESS = 14

    BUILD_ERROR = 15

    RUNTIME_ERROR = 16

    HANDLED_ERROR = 17

    LOG = 18

    DEBUG = 19

    ORDER_EVENT = 20

    SUCCESS = 21

    HISTORY = 22

    COMMAND_RESULT = 23

    GIT_HUB_HOOK = 24

    DOCUMENTATION_RESULT = 25

    DOCUMENTATION = 26

    SYSTEM_DEBUG = 27

    ALPHA_RESULT = 28

    ALPHA_WORK = 29

    ALPHA_NODE = 30

    REGRESSION_ALGORITHM = 31

    ALPHA_HEARTBEAT = 32

    DEBUGGING_STATUS = 33

    OPTIMIZATION_NODE = 34

    OPTIMIZATION_ESTIMATE = 35

    OPTIMIZATION_STATUS = 36

    OPTIMIZATION_RESULT = 37

    AGGREGATED = 38

    LANGUAGE_MODEL_QUERY = 39

    LANGUAGE_MODEL_FEEDBACK = 40

    LANGUAGE_MODEL_RESPONSE = 41

    LANGUAGE_MODEL_CODE_ANALYSIS = 42

    LANGUAGE_MODEL_CHAT_WORK = 43

    LANGUAGE_MODEL_CHAT_RESPONSE = 44

    ALGORITHM_NAME_UPDATE = 45

    ALGORITHM_TAGS_UPDATE = 46

    RESEARCH_NODE = 47

    ORGANIZATION_UPDATE = 48


class Packet(System.Object):
    """Base class for packet messaging system"""

    @property
    def type(self) -> QuantConnect.Packets.PacketType:
        """Packet type defined by a string enum"""
        ...

    @property.setter
    def type(self, value: QuantConnect.Packets.PacketType) -> None:
        ...

    @property
    def channel(self) -> str:
        """User unique specific channel endpoint to send the packets"""
        ...

    @property.setter
    def channel(self, value: str) -> None:
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """
        Initialize the base class and setup the packet type.
        
        :param type: PacketType for the class.
        """
        ...


class AlphaResultPacket(QuantConnect.Packets.Packet):
    """Provides a packet type for transmitting alpha insights data"""

    @property
    def user_id(self) -> int:
        """The user's id that deployed the alpha stream"""
        ...

    @property.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def alpha_id(self) -> str:
        """
        The deployed alpha id. This is the id generated upon submssion to the alpha marketplace.
        If this is a user backtest or live algo then this will not be specified
        """
        ...

    @property.setter
    def alpha_id(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """The algorithm's unique identifier"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def insights(self) -> System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """The generated insights"""
        ...

    @property.setter
    def insights(self, value: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> None:
        ...

    @property
    def order_events(self) -> System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]:
        """The generated OrderEvents"""
        ...

    @property.setter
    def order_events(self, value: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]) -> None:
        ...

    @property
    def orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """The new or updated Orders"""
        ...

    @property.setter
    def orders(self, value: System.Collections.Generic.List[QuantConnect.Orders.Order]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AlphaResultPacket class"""
        ...

    @overload
    def __init__(self, algorithmId: str, userId: int, insights: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight] = None, orderEvents: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent] = None, orders: System.Collections.Generic.List[QuantConnect.Orders.Order] = None) -> None:
        """
        Initializes a new instance of the AlphaResultPacket class
        
        :param algorithmId: The algorithm's unique identifier
        :param userId: The user's id
        :param insights: Alphas generated by the algorithm
        :param orderEvents: OrderEvents generated by the algorithm
        :param orders: Orders generated or updated by the algorithm
        """
        ...


class BaseResultParameters(System.Object):
    """Base parameters used by LiveResultParameters and BacktestResultParameters"""

    @property
    def profit_loss(self) -> System.Collections.Generic.IDictionary[datetime.datetime, float]:
        """Trade profit and loss information since the last algorithm result packet"""
        ...

    @property.setter
    def profit_loss(self, value: System.Collections.Generic.IDictionary[datetime.datetime, float]) -> None:
        ...

    @property
    def charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @property.setter
    def charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]) -> None:
        ...

    @property
    def orders(self) -> System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]:
        """Order updates since the last result packet"""
        ...

    @property.setter
    def orders(self, value: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]) -> None:
        ...

    @property
    def order_events(self) -> System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]:
        """Order events updates since the last result packet"""
        ...

    @property.setter
    def order_events(self, value: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]) -> None:
        ...

    @property
    def statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Statistics information sent during the algorithm operations."""
        ...

    @property.setter
    def statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @property.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def state(self) -> System.Collections.Generic.IDictionary[str, str]:
        """State information of the algorithm."""
        ...

    @property.setter
    def state(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def algorithm_configuration(self) -> QuantConnect.AlgorithmConfiguration:
        """The algorithm's configuration required for report generation"""
        ...

    @property.setter
    def algorithm_configuration(self, value: QuantConnect.AlgorithmConfiguration) -> None:
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float], statistics: System.Collections.Generic.IDictionary[str, str], runtimeStatistics: System.Collections.Generic.IDictionary[str, str], orderEvents: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent], algorithmConfiguration: QuantConnect.AlgorithmConfiguration = None, state: System.Collections.Generic.IDictionary[str, str] = None) -> None:
        """Creates a new instance"""
        ...


class BacktestResultParameters(QuantConnect.Packets.BaseResultParameters):
    """Defines the parameters for BacktestResult"""

    @property
    def rolling_window(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @property.setter
    def rolling_window(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]) -> None:
        ...

    @property
    def total_performance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Rolling window detailed statistics."""
        ...

    @property.setter
    def total_performance(self, value: QuantConnect.Statistics.AlgorithmPerformance) -> None:
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float], statistics: System.Collections.Generic.IDictionary[str, str], runtimeStatistics: System.Collections.Generic.IDictionary[str, str], rollingWindow: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance], orderEvents: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent], totalPerformance: QuantConnect.Statistics.AlgorithmPerformance = None, algorithmConfiguration: QuantConnect.AlgorithmConfiguration = None, state: System.Collections.Generic.IDictionary[str, str] = None) -> None:
        """Creates a new instance"""
        ...


class BacktestResult(QuantConnect.Result):
    """Backtest results object class - result specific items from the packet."""

    @property
    def rolling_window(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @property.setter
    def rolling_window(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]) -> None:
        ...

    @property
    def total_performance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Rolling window detailed statistics."""
        ...

    @property.setter
    def total_performance(self, value: QuantConnect.Statistics.AlgorithmPerformance) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default Constructor"""
        ...

    @overload
    def __init__(self, parameters: QuantConnect.Packets.BacktestResultParameters) -> None:
        """Constructor for the result class using dictionary objects."""
        ...


class PythonEnvironmentPacket(QuantConnect.Packets.Packet, metaclass=abc.ABCMeta):
    """
    Python Environment Packet is an abstract packet that contains a PythonVirtualEnvironment
    definition. Intended to be used by inheriting classes that may use a PythonVirtualEnvironment
    """

    @property
    def python_virtual_environment(self) -> str:
        """
        Virtual environment ID used to find PythonEvironments
        Ideally MD5, but environment names work as well.
        """
        ...

    @property.setter
    def python_virtual_environment(self, value: str) -> None:
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """
        Default constructor for a PythonEnvironmentPacket
        
        This method is protected.
        """
        ...


class Controls(System.Object):
    """Specifies values used to control algorithm limits"""

    @property
    def maximum_runtime_minutes(self) -> int:
        """The maximum runtime in minutes"""
        ...

    @property.setter
    def maximum_runtime_minutes(self, value: int) -> None:
        ...

    @property
    def minute_limit(self) -> int:
        """The maximum number of minute symbols"""
        ...

    @property.setter
    def minute_limit(self, value: int) -> None:
        ...

    @property
    def second_limit(self) -> int:
        """The maximum number of second symbols"""
        ...

    @property.setter
    def second_limit(self, value: int) -> None:
        ...

    @property
    def tick_limit(self) -> int:
        """The maximum number of tick symbol"""
        ...

    @property.setter
    def tick_limit(self, value: int) -> None:
        ...

    @property
    def ram_allocation(self) -> int:
        """Ram allocation for this algorithm in MB"""
        ...

    @property.setter
    def ram_allocation(self, value: int) -> None:
        ...

    @property
    def cpu_allocation(self) -> float:
        """CPU allocation for this algorithm"""
        ...

    @property.setter
    def cpu_allocation(self, value: float) -> None:
        ...

    @property
    def live_log_limit(self) -> int:
        """The user live log limit"""
        ...

    @property.setter
    def live_log_limit(self, value: int) -> None:
        ...

    @property
    def backtest_log_limit(self) -> int:
        """The user backtesting log limit"""
        ...

    @property.setter
    def backtest_log_limit(self, value: int) -> None:
        ...

    @property
    def daily_log_limit(self) -> int:
        """The daily log limit of a user"""
        ...

    @property.setter
    def daily_log_limit(self, value: int) -> None:
        ...

    @property
    def remaining_log_allowance(self) -> int:
        """The remaining log allowance for a user"""
        ...

    @property.setter
    def remaining_log_allowance(self, value: int) -> None:
        ...

    @property
    def backtesting_max_insights(self) -> int:
        """Maximimum number of insights we'll store and score in a single backtest"""
        ...

    @property.setter
    def backtesting_max_insights(self, value: int) -> None:
        ...

    @property
    def backtesting_max_orders(self) -> int:
        """Maximimum number of orders we'll allow in a backtest."""
        ...

    @property.setter
    def backtesting_max_orders(self, value: int) -> None:
        ...

    @property
    def maximum_data_points_per_chart_series(self) -> int:
        """Limits the amount of data points per chart series. Applies only for backtesting"""
        ...

    @property.setter
    def maximum_data_points_per_chart_series(self, value: int) -> None:
        ...

    @property
    def maximum_chart_series(self) -> int:
        """Limits the amount of chart series. Applies only for backtesting"""
        ...

    @property.setter
    def maximum_chart_series(self, value: int) -> None:
        ...

    @property
    def second_time_out(self) -> int:
        """The amount seconds used for timeout limits"""
        ...

    @property.setter
    def second_time_out(self, value: int) -> None:
        ...

    @property
    def training_limits(self) -> QuantConnect.Packets.LeakyBucketControlParameters:
        """
        Sets parameters used for determining the behavior of the leaky bucket algorithm that
        controls how much time is available for an algorithm to use the training feature.
        """
        ...

    @property.setter
    def training_limits(self, value: QuantConnect.Packets.LeakyBucketControlParameters) -> None:
        ...

    @property
    def storage_limit(self) -> int:
        """Limits the total size of storage used by IObjectStore"""
        ...

    @property.setter
    def storage_limit(self, value: int) -> None:
        ...

    @property
    def storage_file_count(self) -> int:
        """Limits the number of files to be held under the IObjectStore"""
        ...

    @property.setter
    def storage_file_count(self, value: int) -> None:
        ...

    @property
    def storage_permissions(self) -> System.IO.FileAccess:
        """Holds the permissions for the object store"""
        ...

    @property.setter
    def storage_permissions(self, value: System.IO.FileAccess) -> None:
        ...

    @property
    def persistence_interval_seconds(self) -> int:
        """
        The interval over which the IObjectStore will persistence the contents of
        the object store
        """
        ...

    @property.setter
    def persistence_interval_seconds(self, value: int) -> None:
        ...

    @property
    def credit_cost(self) -> float:
        """The cost associated with running this job"""
        ...

    @property.setter
    def credit_cost(self, value: float) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new default instance of the Controls class"""
        ...


class AlgorithmNodePacket(QuantConnect.Packets.PythonEnvironmentPacket):
    """Algorithm Node Packet is a work task for the Lean Engine"""

    @property
    def host_name(self) -> str:
        """The host name to use if any"""
        ...

    @property.setter
    def host_name(self, value: str) -> None:
        ...

    @property
    def user_id(self) -> int:
        """User Id placing request"""
        ...

    @property.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def user_token(self) -> str:
        ...

    @property.setter
    def user_token(self, value: str) -> None:
        ...

    @property
    def organization_id(self) -> str:
        ...

    @property.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id of the request"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def project_name(self) -> str:
        """Project name of the request"""
        ...

    @property.setter
    def project_name(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm Id - BacktestId or DeployId - Common Id property between packets."""
        ...

    @property
    def session_id(self) -> str:
        """User session Id for authentication"""
        ...

    @property.setter
    def session_id(self, value: str) -> None:
        ...

    @property
    def language(self) -> QuantConnect.Language:
        """Language flag: Currently represents IL code or Dynamic Scripted Types."""
        ...

    @property.setter
    def language(self, value: QuantConnect.Language) -> None:
        ...

    @property
    def server_type(self) -> QuantConnect.ServerType:
        """Server type for the deployment (512, 1024, 2048)"""
        ...

    @property.setter
    def server_type(self, value: QuantConnect.ServerType) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """Unique compile id of this backtest"""
        ...

    @property.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def version(self) -> str:
        """Version number identifier for the lean engine."""
        ...

    @property.setter
    def version(self, value: str) -> None:
        ...

    @property
    def redelivered(self) -> bool:
        """
        An algorithm packet which has already been run and is being redelivered on this node.
        In this event we don't want to relaunch the task as it may result in unexpected behaviour for user.
        """
        ...

    @property.setter
    def redelivered(self, value: bool) -> None:
        ...

    @property
    def algorithm(self) -> typing.List[int]:
        """Algorithm binary with zip of contents"""
        ...

    @property.setter
    def algorithm(self, value: typing.List[int]) -> None:
        ...

    @property
    def request_source(self) -> str:
        """Request source - Web IDE or API - for controling result handler behaviour"""
        ...

    @property.setter
    def request_source(self, value: str) -> None:
        ...

    @property
    def ram_allocation(self) -> int:
        """The maximum amount of RAM (in MB) this algorithm is allowed to utilize"""
        ...

    @property
    def controls(self) -> QuantConnect.Packets.Controls:
        """Specifies values to control algorithm limits"""
        ...

    @property.setter
    def controls(self, value: QuantConnect.Packets.Controls) -> None:
        ...

    @property
    def parameters(self) -> System.Collections.Generic.Dictionary[str, str]:
        """The parameter values used to set algorithm parameters"""
        ...

    @property.setter
    def parameters(self, value: System.Collections.Generic.Dictionary[str, str]) -> None:
        ...

    @property
    def history_provider(self) -> str:
        """String name of the HistoryProvider we're running with"""
        ...

    @property.setter
    def history_provider(self, value: str) -> None:
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    @property
    def deployment_target(self) -> QuantConnect.DeploymentTarget:
        """Deployment target, either local or cloud."""
        ...

    @property.setter
    def deployment_target(self, value: QuantConnect.DeploymentTarget) -> None:
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """Default constructor for the algorithm node:"""
        ...

    def get_algorithm_name(self) -> str:
        """Gets a unique name for the algorithm defined by this packet"""
        ...


class BacktestNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Algorithm backtest task information packet."""

    @property
    def name(self) -> str:
        """Name of the backtest as randomly defined in the IDE."""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """BacktestId / Algorithm Id for this task"""
        ...

    @property.setter
    def backtest_id(self, value: str) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """Optimization Id for this task"""
        ...

    @property.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def period_start(self) -> typing.Optional[datetime.datetime]:
        """Backtest start-date as defined in the Initialize() method."""
        ...

    @property.setter
    def period_start(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def period_finish(self) -> typing.Optional[datetime.datetime]:
        """Backtest end date as defined in the Initialize() method."""
        ...

    @property.setter
    def period_finish(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """Backtest maximum end date"""
        ...

    @property.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_days(self) -> int:
        """The backtest out of sample day count"""
        ...

    @property.setter
    def out_of_sample_days(self, value: int) -> None:
        ...

    @property
    def tradeable_dates(self) -> int:
        """Estimated number of trading days in this backtest task based on the start-end dates."""
        ...

    @property.setter
    def tradeable_dates(self, value: int) -> None:
        ...

    @property
    def debugging(self) -> bool:
        """True, if this is a debugging backtest"""
        ...

    @property.setter
    def debugging(self, value: bool) -> None:
        ...

    @property
    def cash_amount(self) -> typing.Optional[QuantConnect.Securities.CashAmount]:
        """Optional initial cash amount if set"""
        ...

    @property.setter
    def cash_amount(self, value: typing.Optional[QuantConnect.Securities.CashAmount]) -> None:
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, userId: int, projectId: int, sessionId: str, algorithmData: typing.List[int], startingCapital: float, name: str) -> None:
        """Initialize the backtest task packet."""
        ...

    @overload
    def __init__(self, userId: int, projectId: int, sessionId: str, algorithmData: typing.List[int], name: str, startingCapital: typing.Optional[QuantConnect.Securities.CashAmount] = None) -> None:
        """Initialize the backtest task packet."""
        ...


class BacktestResultPacket(QuantConnect.Packets.Packet):
    """Backtest result packet: send backtest information to GUI for user consumption."""

    @property
    def user_id(self) -> int:
        """User Id placing this task"""
        ...

    @property.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id of the this task."""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def session_id(self) -> str:
        """User Session Id"""
        ...

    @property.setter
    def session_id(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """BacktestId for this result packet"""
        ...

    @property.setter
    def backtest_id(self, value: str) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """OptimizationId for this result packet if any"""
        ...

    @property.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """Compile Id for the algorithm which generated this result packet."""
        ...

    @property.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def period_start(self) -> datetime.datetime:
        """Start of the backtest period as defined in Initialize() method."""
        ...

    @property.setter
    def period_start(self, value: datetime.datetime) -> None:
        ...

    @property
    def period_finish(self) -> datetime.datetime:
        """End of the backtest period as defined in the Initialize() method."""
        ...

    @property.setter
    def period_finish(self, value: datetime.datetime) -> None:
        ...

    @property
    def date_requested(self) -> datetime.datetime:
        """DateTime (EST) the user requested this backtest."""
        ...

    @property.setter
    def date_requested(self, value: datetime.datetime) -> None:
        ...

    @property
    def date_finished(self) -> datetime.datetime:
        """DateTime (EST) when the backtest was completed."""
        ...

    @property.setter
    def date_finished(self, value: datetime.datetime) -> None:
        ...

    @property
    def progress(self) -> float:
        """Progress of the backtest as a percentage from 0-1 based on the days lapsed from start-finish."""
        ...

    @property.setter
    def progress(self, value: float) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of this backtest."""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def results(self) -> QuantConnect.Packets.BacktestResult:
        """Result data object for this backtest"""
        ...

    @property.setter
    def results(self, value: QuantConnect.Packets.BacktestResult) -> None:
        ...

    @property
    def processing_time(self) -> float:
        """Processing time of the algorithm (from moment the algorithm arrived on the algorithm node)"""
        ...

    @property.setter
    def processing_time(self, value: float) -> None:
        ...

    @property
    def tradeable_dates(self) -> int:
        """Estimated number of tradeable days in the backtest based on the start and end date or the backtest"""
        ...

    @property.setter
    def tradeable_dates(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Serialization"""
        ...

    @overload
    def __init__(self, json: str) -> None:
        """Compose the packet from a JSON string:"""
        ...

    @overload
    def __init__(self, job: QuantConnect.Packets.BacktestNodePacket, results: QuantConnect.Packets.BacktestResult, endDate: typing.Union[datetime.datetime, datetime.date], startDate: typing.Union[datetime.datetime, datetime.date], progress: float = 1) -> None:
        """
        Compose result data packet - with tradable dates from the backtest job task and the partial result packet.
        
        :param job: Job that started this request
        :param results: Results class for the Backtest job
        :param endDate: The algorithms backtest end date
        :param startDate: The algorithms backtest start date
        :param progress: Progress of the packet. For the packet we assume progess of 100%.
        """
        ...

    @staticmethod
    def create_empty(job: QuantConnect.Packets.BacktestNodePacket) -> QuantConnect.Packets.BacktestResultPacket:
        """
        Creates an empty result packet, useful when the algorithm fails to initialize
        
        :param job: The associated job packet
        :returns: An empty result packet.
        """
        ...


class OrderEventPacket(QuantConnect.Packets.Packet):
    """Order event packet for passing updates on the state of an order to the portfolio."""

    @property
    def event(self) -> QuantConnect.Orders.OrderEvent:
        """Order event object"""
        ...

    @property.setter
    def event(self, value: QuantConnect.Orders.OrderEvent) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm id for this order event"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, eventOrder: QuantConnect.Orders.OrderEvent) -> None:
        """Create a new instance of the order event packet"""
        ...


class LogPacket(QuantConnect.Packets.Packet):
    """Simple log message instruction from the lean engine."""

    @property
    def message(self) -> str:
        """Log message to the users console:"""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm Id requesting this logging"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, message: str) -> None:
        """Create a new instance of the notify Log packet:"""
        ...


class AlgorithmNameUpdatePacket(QuantConnect.Packets.Packet):
    """Packet to communicate updates to the algorithm's name"""

    @property
    def algorithm_id(self) -> str:
        """Algorithm id for this order event"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """The new name"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, name: str) -> None:
        """Create a new instance of the algorithm tags up[date packet"""
        ...


class AlgorithmStatusPacket(QuantConnect.Packets.Packet):
    """Algorithm status update information packet"""

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Current algorithm status"""
        ...

    @property.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    def chart_subscription(self) -> str:
        """Chart we're subscribed to for live trading."""
        ...

    @property.setter
    def chart_subscription(self, value: str) -> None:
        ...

    @property
    def message(self) -> str:
        """Optional message or reason for state change."""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm Id associated with this status packet"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """OptimizationId for this result packet if any"""
        ...

    @property.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id associated with this status packet"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def channel_status(self) -> str:
        """The current state of the channel"""
        ...

    @property.setter
    def channel_status(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, projectId: int, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """Initialize algorithm state packet:"""
        ...


class LiveNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Live job task packet: container for any live specific job variables"""

    @property
    def deploy_id(self) -> str:
        """Deploy Id for this live algorithm."""
        ...

    @property.setter
    def deploy_id(self, value: str) -> None:
        ...

    @property
    def brokerage(self) -> str:
        """String name of the brokerage we're trading with"""
        ...

    @property.setter
    def brokerage(self, value: str) -> None:
        ...

    @property
    def brokerage_data(self) -> System.Collections.Generic.Dictionary[str, str]:
        """String-String Dictionary of Brokerage Data for this Live Job"""
        ...

    @property.setter
    def brokerage_data(self, value: System.Collections.Generic.Dictionary[str, str]) -> None:
        ...

    @property
    def data_queue_handler(self) -> str:
        """String name of the DataQueueHandler or LiveDataProvider we're running with"""
        ...

    @property.setter
    def data_queue_handler(self, value: str) -> None:
        ...

    @property
    def data_channel_provider(self) -> str:
        """String name of the DataChannelProvider we're running with"""
        ...

    @property.setter
    def data_channel_provider(self, value: str) -> None:
        ...

    @property
    def disable_acknowledgement(self) -> bool:
        """Gets flag indicating whether or not the message should be acknowledged and removed from the queue"""
        ...

    @property.setter
    def disable_acknowledgement(self, value: bool) -> None:
        ...

    @property
    def notification_events(self) -> System.Collections.Generic.HashSet[str]:
        """A list of event types to generate notifications for, which will use NotificationTargets"""
        ...

    @property.setter
    def notification_events(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @property
    def notification_targets(self) -> System.Collections.Generic.List[QuantConnect.Notifications.Notification]:
        """A list of notification targets to use"""
        ...

    @property.setter
    def notification_targets(self, value: System.Collections.Generic.List[QuantConnect.Notifications.Notification]) -> None:
        ...

    @property
    def live_data_types(self) -> System.Collections.Generic.HashSet[str]:
        """List of real time data types available in the live trading environment"""
        ...

    @property.setter
    def live_data_types(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    def __init__(self) -> None:
        """Default constructor for JSON of the Live Task Packet"""
        ...


class AlphaNodePacket(QuantConnect.Packets.LiveNodePacket):
    """Alpha job packet"""

    @property
    def alpha_id(self) -> str:
        """Gets or sets the alpha id"""
        ...

    @property.setter
    def alpha_id(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new default instance of the AlgorithmNodePacket class"""
        ...


class SecurityTypesPacket(QuantConnect.Packets.Packet):
    """Security types packet contains information on the markets the user data has requested."""

    @property
    def types(self) -> System.Collections.Generic.List[QuantConnect.SecurityType]:
        """List of Security Type the user has requested (Equity, Forex, Futures etc)."""
        ...

    @property.setter
    def types(self, value: System.Collections.Generic.List[QuantConnect.SecurityType]) -> None:
        ...

    @property
    def types_csv(self) -> str:
        """CSV formatted, lower case list of SecurityTypes for the web API."""
        ...

    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...


class RuntimeErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine.
    This is a managed error which stops the algorithm execution.
    """

    @property
    def message(self) -> str:
        """Runtime error message from the exception"""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm id which generated this runtime error"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def stack_trace(self) -> str:
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @property.setter
    def stack_trace(self, value: str) -> None:
        ...

    @property
    def user_id(self) -> int:
        """User Id associated with the backtest that threw the error"""
        ...

    @property.setter
    def user_id(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, userId: int, algorithmId: str, message: str, stacktrace: str = ...) -> None:
        """Create a new runtime error packet"""
        ...


class ResearchNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Represents a research node packet"""

    @property
    def research_id(self) -> str:
        """The research id"""
        ...

    @property.setter
    def research_id(self, value: str) -> None:
        ...

    @property
    def research_token(self) -> str:
        """Associated research token"""
        ...

    @property.setter
    def research_token(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        """Creates a new instance"""
        ...


class LiveResultParameters(QuantConnect.Packets.BaseResultParameters):
    """Defines the parameters for LiveResult"""

    @property
    def holdings(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Holding]:
        """Holdings dictionary of algorithm holdings information"""
        ...

    @property.setter
    def holdings(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]) -> None:
        ...

    @property
    def cash_book(self) -> QuantConnect.Securities.CashBook:
        """Cashbook for the algorithm's live results."""
        ...

    @property.setter
    def cash_book(self, value: QuantConnect.Securities.CashBook) -> None:
        ...

    @property
    def server_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Server status information, including CPU/RAM usage, ect..."""
        ...

    @property.setter
    def server_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float], holdings: System.Collections.Generic.IDictionary[str, QuantConnect.Holding], cashBook: QuantConnect.Securities.CashBook, statistics: System.Collections.Generic.IDictionary[str, str], runtimeStatistics: System.Collections.Generic.IDictionary[str, str], orderEvents: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent], serverStatistics: System.Collections.Generic.IDictionary[str, str] = None, algorithmConfiguration: QuantConnect.AlgorithmConfiguration = None, state: System.Collections.Generic.IDictionary[str, str] = None) -> None:
        """Creates a new instance"""
        ...


class LiveResult(QuantConnect.Result):
    """Live results object class for packaging live result data."""

    @property
    def holdings(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Holding]:
        """Holdings dictionary of algorithm holdings information"""
        ...

    @property.setter
    def holdings(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]) -> None:
        ...

    @property
    def cash_book(self) -> QuantConnect.Securities.CashBook:
        """Cashbook for the algorithm's live results."""
        ...

    @property.setter
    def cash_book(self, value: QuantConnect.Securities.CashBook) -> None:
        ...

    @property
    def cash(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Cash for the algorithm's live results."""
        ...

    @property.setter
    def cash(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]) -> None:
        ...

    @property
    def account_currency(self) -> str:
        """The algorithm's account currency"""
        ...

    @property.setter
    def account_currency(self, value: str) -> None:
        ...

    @property
    def account_currency_symbol(self) -> str:
        """The algorithm's account currency"""
        ...

    @property.setter
    def account_currency_symbol(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default Constructor"""
        ...

    @overload
    def __init__(self, parameters: QuantConnect.Packets.LiveResultParameters) -> None:
        """Constructor for the result class for dictionary objects"""
        ...


class LiveResultPacket(QuantConnect.Packets.Packet):
    """Live result packet from a lean engine algorithm."""

    @property
    def user_id(self) -> int:
        """User Id sending result packet"""
        ...

    @property.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id of the result packet"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def deploy_id(self) -> str:
        """Live Algorithm Id (DeployId) for this result packet"""
        ...

    @property.setter
    def deploy_id(self, value: str) -> None:
        ...

    @property
    def results(self) -> QuantConnect.Packets.LiveResult:
        """Result data object for this result packet"""
        ...

    @property.setter
    def results(self, value: QuantConnect.Packets.LiveResult) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Serialization"""
        ...

    @overload
    def __init__(self, json: str) -> None:
        """Compose the packet from a JSON string:"""
        ...

    @overload
    def __init__(self, job: QuantConnect.Packets.LiveNodePacket, results: QuantConnect.Packets.LiveResult) -> None:
        """
        Compose Live Result Data Packet - With tradable dates
        
        :param job: Job that started this request
        :param results: Results class for the Backtest job
        """
        ...

    @staticmethod
    def create_empty(job: QuantConnect.Packets.LiveNodePacket) -> QuantConnect.Packets.LiveResultPacket:
        """
        Creates an empty result packet, useful when the algorithm fails to initialize
        
        :param job: The associated job packet
        :returns: An empty result packet.
        """
        ...


class MarketHours(System.Object):
    """Market open hours model for pre, normal and post market hour definitions."""

    @property
    def start(self) -> datetime.datetime:
        """Start time for this market hour category"""
        ...

    @property.setter
    def start(self, value: datetime.datetime) -> None:
        ...

    @property
    def end(self) -> datetime.datetime:
        """End time for this market hour category"""
        ...

    @property.setter
    def end(self, value: datetime.datetime) -> None:
        ...

    def __init__(self, referenceDate: typing.Union[datetime.datetime, datetime.date], defaultStart: float, defaultEnd: float) -> None:
        """
        Market hours initializer given an hours since midnight measure for the market hours today
        
        :param referenceDate: Reference date used for as base date from the specified hour offsets
        :param defaultStart: Time in hours since midnight to start this open period.
        :param defaultEnd: Time in hours since midnight to end this open period.
        """
        ...


class MarketToday(System.Object):
    """Market today information class"""

    @property
    def date(self) -> datetime.datetime:
        """Date this packet was generated."""
        ...

    @property.setter
    def date(self, value: datetime.datetime) -> None:
        ...

    @property
    def status(self) -> str:
        """Given the dates and times above, what is the current market status - open or closed."""
        ...

    @property.setter
    def status(self, value: str) -> None:
        ...

    @property
    def pre_market(self) -> QuantConnect.Packets.MarketHours:
        """Premarket hours for today"""
        ...

    @property.setter
    def pre_market(self, value: QuantConnect.Packets.MarketHours) -> None:
        ...

    @property
    def open(self) -> QuantConnect.Packets.MarketHours:
        """Normal trading market hours for today"""
        ...

    @property.setter
    def open(self, value: QuantConnect.Packets.MarketHours) -> None:
        ...

    @property
    def post_market(self) -> QuantConnect.Packets.MarketHours:
        """Post market hours for today"""
        ...

    @property.setter
    def post_market(self, value: QuantConnect.Packets.MarketHours) -> None:
        ...

    def __init__(self) -> None:
        """Default constructor (required for JSON serialization)"""
        ...


class DebugPacket(QuantConnect.Packets.Packet):
    """Send a simple debug message from the users algorithm to the console."""

    @property
    def message(self) -> str:
        """String debug message to send to the users console"""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Associated algorithm Id."""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """Compile id of the algorithm sending this message"""
        ...

    @property.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id for this message"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def toast(self) -> bool:
        """
        True to emit message as a popup notification (toast),
        false to emit message in console as text
        """
        ...

    @property.setter
    def toast(self, value: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, packetType: QuantConnect.Packets.PacketType) -> None:
        """
        Constructor for inherited types
        
        This method is protected.
        
        :param packetType: The type of packet to create
        """
        ...

    @overload
    def __init__(self, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool = False) -> None:
        """Create a new instance of the notify debug packet:"""
        ...


class SystemDebugPacket(QuantConnect.Packets.DebugPacket):
    """Debug packets generated by Lean"""

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool = False) -> None:
        """Create a new instance of the system debug packet"""
        ...


class AlgorithmTagsUpdatePacket(QuantConnect.Packets.Packet):
    """Packet to communicate updates to the algorithm tags"""

    @property
    def algorithm_id(self) -> str:
        """Algorithm id for this order event"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.HashSet[str]:
        """The new tags"""
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, tags: System.Collections.Generic.HashSet[str]) -> None:
        """Create a new instance of the algorithm tags up[date packet"""
        ...


class HistoryRequest(System.Object):
    """
    Specifies request parameters for a single historical request.
    A HistoryPacket is made of multiple requests for data. These
    are used to request data during live mode from a data server
    """

    @property
    def start_time_utc(self) -> datetime.datetime:
        """The start time to request data in UTC"""
        ...

    @property.setter
    def start_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_time_utc(self) -> datetime.datetime:
        """The end time to request data in UTC"""
        ...

    @property.setter
    def end_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """The symbol to request data for"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """The requested resolution"""
        ...

    @property.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """The type of data to retrieve"""
        ...

    @property.setter
    def tick_type(self, value: QuantConnect.TickType) -> None:
        ...


class HistoryPacket(QuantConnect.Packets.Packet):
    """Packet for history jobs"""

    @property
    def queue_name(self) -> str:
        """The queue where the data should be sent"""
        ...

    @property.setter
    def queue_name(self, value: str) -> None:
        ...

    @property
    def requests(self) -> System.Collections.Generic.List[QuantConnect.Packets.HistoryRequest]:
        """The individual requests to be processed"""
        ...

    @property.setter
    def requests(self, value: System.Collections.Generic.List[QuantConnect.Packets.HistoryRequest]) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the HistoryPacket class"""
        ...


class HistoryResultType(Enum):
    """Specifies various types of history results"""

    FILE = 0
    """The requested file data"""

    STATUS = 1
    """The request's status"""

    COMPLETED = 2
    """The request is completed"""

    ERROR = 3
    """The request had an error"""


class HistoryResult(System.Object, metaclass=abc.ABCMeta):
    """
    Provides a container for results from history requests. This contains
    the file path relative to the /Data folder where the data can be written
    """

    @property
    def type(self) -> QuantConnect.Packets.HistoryResultType:
        """Gets the type of history result"""
        ...

    def __init__(self, type: QuantConnect.Packets.HistoryResultType) -> None:
        """
        Initializes a new instance of the HistoryResult class
        
        This method is protected.
        
        :param type: The type of history result
        """
        ...


class FileHistoryResult(QuantConnect.Packets.HistoryResult):
    """Defines requested file data for a history request"""

    @property
    def filepath(self) -> str:
        """The relative file path where the data should be written"""
        ...

    @property.setter
    def filepath(self, value: str) -> None:
        ...

    @property
    def file(self) -> typing.List[int]:
        """The file's contents, this is a zipped csv file"""
        ...

    @property.setter
    def file(self, value: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, filepath: str, file: typing.List[int]) -> None:
        """
        Initializes a new instance of the HistoryResult class
        
        :param filepath: The relative file path where the file should be written, rooted in /Data, so for example ./forex/fxcm/daily/eurusd.zip
        :param file: The zipped csv file content in bytes
        """
        ...


class CompletedHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specifies the completed message from a history result"""

    def __init__(self) -> None:
        """Initializes a new instance of CompletedHistoryResult class"""
        ...


class ErrorHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specfies an error message in a history result"""

    @property
    def message(self) -> str:
        """Gets the error that was encountered"""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the ErrorHistoryResult class
        
        :param message: The error message
        """
        ...


class StatusHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specifies the progress of a request"""

    @property
    def progress(self) -> int:
        """Gets the progress of the request"""
        ...

    @property.setter
    def progress(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, progress: int) -> None:
        """
        Initializes a new instance of the StatusHistoryResult class
        
        :param progress: The progress, from 0 to 100
        """
        ...


class HandledErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine.
    This is a managed error which stops the algorithm execution.
    """

    @property
    def message(self) -> str:
        """Runtime error message from the exception"""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm id which generated this runtime error"""
        ...

    @property.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def stack_trace(self) -> str:
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @property.setter
    def stack_trace(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, message: str, stacktrace: str = ...) -> None:
        """Create a new handled error packet"""
        ...


