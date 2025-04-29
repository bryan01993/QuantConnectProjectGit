from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Api
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Optimizer
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Generic
import System.Collections.Specialized
import System.Text.RegularExpressions
import System.Threading.Tasks

JsonConverter = typing.Any

QuantConnect_Api_ApiConnection_TryRequest_T = typing.TypeVar("QuantConnect_Api_ApiConnection_TryRequest_T")
QuantConnect_Api_ApiConnection_TryRequestAsync_T = typing.TypeVar("QuantConnect_Api_ApiConnection_TryRequestAsync_T")


class ApiConnection(System.Object):
    """API Connection and Hash Manager"""

    @property
    def client(self) -> typing.Any:
        """Authorized client to use for requests."""
        ...

    @property.setter
    def client(self, value: typing.Any) -> None:
        ...

    @property
    def connected(self) -> bool:
        """Return true if connected successfully."""
        ...

    def __init__(self, userId: int, token: str) -> None:
        """
        Create a new Api Connection Class.
        
        :param userId: User Id number from QuantConnect.com account. Found at www.quantconnect.com/account
        :param token: Access token for the QuantConnect account. Found at www.quantconnect.com/account
        """
        ...

    def try_request(self, request: typing.Any, result: typing.Optional[QuantConnect_Api_ApiConnection_TryRequest_T]) -> typing.Union[bool, QuantConnect_Api_ApiConnection_TryRequest_T]:
        """
        Place a secure request and get back an object of type T.
        
        :param result: Result object from the
        :returns: T typed object response.
        """
        ...

    def try_request_async(self, request: typing.Any) -> System.Threading.Tasks.Task[System.Tuple[bool, QuantConnect_Api_ApiConnection_TryRequestAsync_T]]:
        """
        Place a secure request and get back an object of type T.
        
        :returns: T typed object response.
        """
        ...


class StringRepresentation(System.Object):
    """Class to return the string representation of an API response class"""

    def to_string(self) -> str:
        """Returns the string representation of this object"""
        ...


class RestResponse(QuantConnect.Api.StringRepresentation):
    """Base API response class for the QuantConnect API."""

    @property
    def success(self) -> bool:
        """Indicate if the API request was successful."""
        ...

    @property.setter
    def success(self, value: bool) -> None:
        ...

    @property
    def errors(self) -> System.Collections.Generic.List[str]:
        """List of errors with the API call."""
        ...

    @property.setter
    def errors(self, value: System.Collections.Generic.List[str]) -> None:
        ...

    def __init__(self) -> None:
        """JSON Constructor"""
        ...


class Version(System.Object):
    """API response for version"""

    @property
    def id(self) -> int:
        """ID of the LEAN version"""
        ...

    @property.setter
    def id(self, value: int) -> None:
        ...

    @property
    def created(self) -> typing.Optional[datetime.datetime]:
        """Date when this version was created"""
        ...

    @property.setter
    def created(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def description(self) -> str:
        """Description of the LEAN version"""
        ...

    @property.setter
    def description(self, value: str) -> None:
        ...

    @property
    def lean_hash(self) -> str:
        """Commit Hash in the LEAN repository"""
        ...

    @property.setter
    def lean_hash(self, value: str) -> None:
        ...

    @property
    def lean_cloud_hash(self) -> str:
        """Commit Hash in the LEAN Cloud repository"""
        ...

    @property.setter
    def lean_cloud_hash(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the branch where the commit is"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def ref(self) -> str:
        """Reference to the branch where the commit is"""
        ...

    @property.setter
    def ref(self, value: str) -> None:
        ...

    @property
    def public(self) -> bool:
        """Indicates if the version is available for the public (1) or not (0)"""
        ...

    @property.setter
    def public(self, value: bool) -> None:
        ...


class VersionsResponse(QuantConnect.Api.RestResponse):
    """Read versions response"""

    @property
    def versions(self) -> System.Collections.Generic.List[QuantConnect.Api.Version]:
        """List of LEAN versions"""
        ...

    @property.setter
    def versions(self, value: System.Collections.Generic.List[QuantConnect.Api.Version]) -> None:
        ...


class GridChart(System.Object):
    """The chart display properties"""

    @property
    def chart_name(self) -> str:
        """The chart name"""
        ...

    @property.setter
    def chart_name(self, value: str) -> None:
        ...

    @property
    def width(self) -> int:
        """Width of the chart"""
        ...

    @property.setter
    def width(self, value: int) -> None:
        ...

    @property
    def height(self) -> int:
        """Height of the chart"""
        ...

    @property.setter
    def height(self, value: int) -> None:
        ...

    @property
    def row(self) -> int:
        """Number of rows of the chart"""
        ...

    @property.setter
    def row(self, value: int) -> None:
        ...

    @property
    def column(self) -> int:
        """Number of columns of the chart"""
        ...

    @property.setter
    def column(self, value: int) -> None:
        ...

    @property
    def sort(self) -> int:
        """Sort of the chart"""
        ...

    @property.setter
    def sort(self, value: int) -> None:
        ...

    @property
    def definition(self) -> System.Collections.Generic.List[str]:
        """Optionally related definition"""
        ...

    @property.setter
    def definition(self, value: System.Collections.Generic.List[str]) -> None:
        ...


class Grid(System.Object):
    """The grid arrangement of charts"""

    @property
    def xs(self) -> System.Collections.Generic.List[QuantConnect.Api.GridChart]:
        """List of chart in the xs (Extra small) position"""
        ...

    @property.setter
    def xs(self, value: System.Collections.Generic.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def sm(self) -> System.Collections.Generic.List[QuantConnect.Api.GridChart]:
        """List of chart in the sm (Small) position"""
        ...

    @property.setter
    def sm(self, value: System.Collections.Generic.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def md(self) -> System.Collections.Generic.List[QuantConnect.Api.GridChart]:
        """List of chart in the md (Medium) position"""
        ...

    @property.setter
    def md(self, value: System.Collections.Generic.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def lg(self) -> System.Collections.Generic.List[QuantConnect.Api.GridChart]:
        """List of chart in the lg (Large) position"""
        ...

    @property.setter
    def lg(self, value: System.Collections.Generic.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def xl(self) -> System.Collections.Generic.List[QuantConnect.Api.GridChart]:
        """List of chart in the xl (Extra large) position"""
        ...

    @property.setter
    def xl(self, value: System.Collections.Generic.List[QuantConnect.Api.GridChart]) -> None:
        ...


class EncryptionKey(System.Object):
    """Encryption key details"""

    @property
    def id(self) -> str:
        """Encryption key id"""
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the encryption key"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...


class Collaborator(System.Object):
    """Collaborator responses"""

    @property
    def uid(self) -> int:
        """User ID"""
        ...

    @property.setter
    def uid(self, value: int) -> None:
        ...

    @property
    def live_control(self) -> bool:
        """Indicate if the user have live control"""
        ...

    @property.setter
    def live_control(self, value: bool) -> None:
        ...

    @property
    def permission(self) -> str:
        """
        The permission this user is given. Can be "read"
        or "write"
        """
        ...

    @property.setter
    def permission(self, value: str) -> None:
        ...

    @property
    def public_id(self) -> str:
        """The user public ID"""
        ...

    @property.setter
    def public_id(self, value: str) -> None:
        ...

    @property
    def profile_image(self) -> str:
        """The url of the user profile image"""
        ...

    @property.setter
    def profile_image(self, value: str) -> None:
        ...

    @property
    def email(self) -> str:
        """The registered email of the user"""
        ...

    @property.setter
    def email(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """The display name of the user"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def bio(self) -> str:
        """The biography of the user"""
        ...

    @property.setter
    def bio(self, value: str) -> None:
        ...

    @property
    def owner(self) -> bool:
        """Indicate if the user is the owner of the project"""
        ...

    @property.setter
    def owner(self, value: bool) -> None:
        ...


class Parameter(System.Object):
    """Parameter set"""

    @property
    def name(self) -> str:
        """Name of parameter"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def value(self) -> str:
        """Value of parameter"""
        ...

    @property.setter
    def value(self, value: str) -> None:
        ...


class Library(System.Object):
    """Library response"""

    @property
    def projectid(self) -> int:
        """Project Id of the library project"""
        ...

    @property.setter
    def projectid(self, value: int) -> None:
        ...

    @property
    def library_name(self) -> str:
        """Name of the library project"""
        ...

    @property.setter
    def library_name(self, value: str) -> None:
        ...

    @property
    def owner_name(self) -> str:
        """Name of the library project owner"""
        ...

    @property.setter
    def owner_name(self, value: str) -> None:
        ...

    @property
    def access(self) -> bool:
        """Indicate if the library project can be accessed"""
        ...

    @property.setter
    def access(self, value: bool) -> None:
        ...


class Project(QuantConnect.Api.RestResponse):
    """Response from reading a project by id."""

    @property
    def project_id(self) -> int:
        """Project id"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the project"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def created(self) -> datetime.datetime:
        """Date the project was created"""
        ...

    @property.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def modified(self) -> datetime.datetime:
        """Modified date for the project"""
        ...

    @property.setter
    def modified(self, value: datetime.datetime) -> None:
        ...

    @property
    def language(self) -> QuantConnect.Language:
        """Programming language of the project"""
        ...

    @property.setter
    def language(self, value: QuantConnect.Language) -> None:
        ...

    @property
    def owner_id(self) -> int:
        """The projects owner id"""
        ...

    @property.setter
    def owner_id(self, value: int) -> None:
        ...

    @property
    def organization_id(self) -> str:
        """The organization ID"""
        ...

    @property.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def collaborators(self) -> System.Collections.Generic.List[QuantConnect.Api.Collaborator]:
        """List of collaborators"""
        ...

    @property.setter
    def collaborators(self, value: System.Collections.Generic.List[QuantConnect.Api.Collaborator]) -> None:
        ...

    @property
    def lean_version_id(self) -> int:
        """The version of LEAN this project is running on"""
        ...

    @property.setter
    def lean_version_id(self, value: int) -> None:
        ...

    @property
    def lean_pinned_to_master(self) -> bool:
        """Indicate if the project is pinned to the master branch of LEAN"""
        ...

    @property.setter
    def lean_pinned_to_master(self, value: bool) -> None:
        ...

    @property
    def owner(self) -> bool:
        """Indicate if you are the owner of the project"""
        ...

    @property.setter
    def owner(self, value: bool) -> None:
        ...

    @property
    def description(self) -> str:
        """The project description"""
        ...

    @property.setter
    def description(self, value: str) -> None:
        ...

    @property
    def channel_id(self) -> str:
        """Channel id"""
        ...

    @property.setter
    def channel_id(self, value: str) -> None:
        ...

    @property
    def parameters(self) -> System.Collections.Generic.List[QuantConnect.Api.Parameter]:
        """Optimization parameters"""
        ...

    @property.setter
    def parameters(self, value: System.Collections.Generic.List[QuantConnect.Api.Parameter]) -> None:
        ...

    @property
    def libraries(self) -> System.Collections.Generic.List[QuantConnect.Api.Library]:
        """The library projects"""
        ...

    @property.setter
    def libraries(self, value: System.Collections.Generic.List[QuantConnect.Api.Library]) -> None:
        ...

    @property
    def grid(self) -> QuantConnect.Api.Grid:
        """Configuration of the backtest view grid"""
        ...

    @property.setter
    def grid(self, value: QuantConnect.Api.Grid) -> None:
        ...

    @property
    def live_grid(self) -> QuantConnect.Api.Grid:
        """Configuration of the live view grid"""
        ...

    @property.setter
    def live_grid(self, value: QuantConnect.Api.Grid) -> None:
        ...

    @property
    def paper_equity(self) -> typing.Optional[float]:
        """The equity value of the last paper trading instance"""
        ...

    @property.setter
    def paper_equity(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def last_live_deployment(self) -> typing.Optional[datetime.datetime]:
        """The last live deployment active time"""
        ...

    @property.setter
    def last_live_deployment(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def live_form(self) -> System.Object:
        """The last live wizard content used"""
        ...

    @property.setter
    def live_form(self, value: System.Object) -> None:
        ...

    @property
    def encrypted(self) -> typing.Optional[bool]:
        """Indicates if the project is encrypted"""
        ...

    @property.setter
    def encrypted(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    def code_running(self) -> bool:
        """Indicates if the project is running or not"""
        ...

    @property.setter
    def code_running(self, value: bool) -> None:
        ...

    @property
    def lean_environment(self) -> int:
        """LEAN environment of the project running on"""
        ...

    @property.setter
    def lean_environment(self, value: int) -> None:
        ...

    @property
    def encryption_key(self) -> QuantConnect.Api.EncryptionKey:
        """Text file with at least 32 characters to be used to encrypt the project"""
        ...

    @property.setter
    def encryption_key(self, value: QuantConnect.Api.EncryptionKey) -> None:
        ...


class ProjectResponse(QuantConnect.Api.VersionsResponse):
    """Project list response"""

    @property
    def projects(self) -> System.Collections.Generic.List[QuantConnect.Api.Project]:
        """List of projects for the authenticated user"""
        ...

    @property.setter
    def projects(self, value: System.Collections.Generic.List[QuantConnect.Api.Project]) -> None:
        ...


class ProjectFile(System.Object):
    """File for a project"""

    @property
    def name(self) -> str:
        """Name of a project file"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def code(self) -> str:
        """Contents of the project file"""
        ...

    @property.setter
    def code(self, value: str) -> None:
        ...

    @property
    def date_modified(self) -> datetime.datetime:
        """DateTime project file was modified"""
        ...

    @property.setter
    def date_modified(self, value: datetime.datetime) -> None:
        ...

    @property
    def is_library(self) -> bool:
        """Indicates if the project file is a library or not"""
        ...

    @property.setter
    def is_library(self, value: bool) -> None:
        ...

    @property
    def open(self) -> bool:
        """Indicates if the project file is open or not"""
        ...

    @property.setter
    def open(self, value: bool) -> None:
        ...

    @property
    def project_id(self) -> int:
        """ID of the project"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def id(self) -> typing.Optional[int]:
        """ID of the project file, can be null"""
        ...

    @property.setter
    def id(self, value: typing.Optional[int]) -> None:
        ...


class ProjectFilesResponse(QuantConnect.Api.RestResponse):
    """Response received when creating a file or reading one file or more in a project"""

    @property
    def files(self) -> System.Collections.Generic.List[QuantConnect.Api.ProjectFile]:
        """List of project file information"""
        ...

    @property.setter
    def files(self, value: System.Collections.Generic.List[QuantConnect.Api.ProjectFile]) -> None:
        ...


class NodePrices(System.Object):
    """Class for deserializing node prices from node object"""

    @property
    def monthly(self) -> int:
        """The monthly price of the node in US dollars"""
        ...

    @property.setter
    def monthly(self, value: int) -> None:
        ...

    @property
    def yearly(self) -> int:
        """The yearly prices of the node in US dollars"""
        ...

    @property.setter
    def yearly(self, value: int) -> None:
        ...


class Node(System.Object):
    """
    Node class built for API endpoints nodes/read and nodes/create.
    Converts JSON properties from API response into data members for the class.
    Contains all relevant information on a Node to interact through API endpoints.
    """

    @property
    def speed(self) -> float:
        """The nodes cpu clock speed in GHz."""
        ...

    @property.setter
    def speed(self, value: float) -> None:
        ...

    @property
    def prices(self) -> QuantConnect.Api.NodePrices:
        """
        The monthly and yearly prices of the node in US dollars,
        see NodePrices for type.
        """
        ...

    @property.setter
    def prices(self, value: QuantConnect.Api.NodePrices) -> None:
        ...

    @property
    def cpu_count(self) -> int:
        """CPU core count of node."""
        ...

    @property.setter
    def cpu_count(self, value: int) -> None:
        ...

    @property
    def has_gpu(self) -> int:
        """Indicate if the node has GPU (1) or not (0)"""
        ...

    @property.setter
    def has_gpu(self, value: int) -> None:
        ...

    @property
    def ram(self) -> float:
        """Size of RAM in Gigabytes."""
        ...

    @property.setter
    def ram(self, value: float) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the node."""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def sku(self) -> str:
        """Node type identifier for configuration."""
        ...

    @property.setter
    def sku(self, value: str) -> None:
        ...

    @property
    def description(self) -> str:
        """Description of the node."""
        ...

    @property.setter
    def description(self, value: str) -> None:
        ...

    @property
    def used_by(self) -> str:
        """User currently using the node."""
        ...

    @property.setter
    def used_by(self, value: str) -> None:
        ...

    @property
    def user_profile(self) -> str:
        """URL of the user using the node"""
        ...

    @property.setter
    def user_profile(self, value: str) -> None:
        ...

    @property
    def project_name(self) -> str:
        """Project the node is being used for."""
        ...

    @property.setter
    def project_name(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> typing.Optional[int]:
        """Id of the project the node is being used for."""
        ...

    @property.setter
    def project_id(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def busy(self) -> bool:
        """Indicates if the node is currently busy."""
        ...

    @property.setter
    def busy(self, value: bool) -> None:
        ...

    @property
    def id(self) -> str:
        """Full ID of node."""
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    @property
    def assets(self) -> int:
        """Maximum number of assets recommended for this node."""
        ...

    @property.setter
    def assets(self, value: int) -> None:
        ...

    @property
    def host(self) -> str:
        """Node host."""
        ...

    @property.setter
    def host(self, value: str) -> None:
        ...

    @property
    def active(self) -> bool:
        """Indicate if this is the active node. The project will use this node if it's not busy."""
        ...

    @property.setter
    def active(self, value: bool) -> None:
        ...


class NodeList(QuantConnect.Api.RestResponse):
    """Collection of Node objects for each target environment."""

    @property
    def backtest_nodes(self) -> System.Collections.Generic.List[QuantConnect.Api.Node]:
        """Collection of backtest nodes"""
        ...

    @property.setter
    def backtest_nodes(self, value: System.Collections.Generic.List[QuantConnect.Api.Node]) -> None:
        ...

    @property
    def research_nodes(self) -> System.Collections.Generic.List[QuantConnect.Api.Node]:
        """Collection of research nodes"""
        ...

    @property.setter
    def research_nodes(self, value: System.Collections.Generic.List[QuantConnect.Api.Node]) -> None:
        ...

    @property
    def live_nodes(self) -> System.Collections.Generic.List[QuantConnect.Api.Node]:
        """Collection of live nodes"""
        ...

    @property.setter
    def live_nodes(self, value: System.Collections.Generic.List[QuantConnect.Api.Node]) -> None:
        ...


class ProjectNodesResponse(QuantConnect.Api.RestResponse):
    """Response received when reading or updating some nodes of a project"""

    @property
    def nodes(self) -> QuantConnect.Api.NodeList:
        """List of project nodes."""
        ...

    @property.setter
    def nodes(self, value: QuantConnect.Api.NodeList) -> None:
        ...

    @property
    def auto_select_node(self) -> bool:
        """Indicate if the node is automatically selected"""
        ...

    @property.setter
    def auto_select_node(self, value: bool) -> None:
        ...


class CompileState(Enum):
    """State of the compilation request"""

    IN_QUEUE = 0
    """Compile waiting in the queue to be processed."""

    BUILD_SUCCESS = 1
    """Compile was built successfully"""

    BUILD_ERROR = 2
    """Build error, check logs for more information"""


class Compile(QuantConnect.Api.RestResponse):
    """Response from the compiler on a build event"""

    @property
    def compile_id(self) -> str:
        """Compile Id for a sucessful build"""
        ...

    @property.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def state(self) -> QuantConnect.Api.CompileState:
        """True on successful compile"""
        ...

    @property.setter
    def state(self, value: QuantConnect.Api.CompileState) -> None:
        ...

    @property
    def logs(self) -> System.Collections.Generic.List[str]:
        """Logs of the compilation request"""
        ...

    @property.setter
    def logs(self, value: System.Collections.Generic.List[str]) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id we sent for compile"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def signature(self) -> str:
        """Signature key of compilation"""
        ...

    @property.setter
    def signature(self, value: str) -> None:
        ...

    @property
    def signature_order(self) -> System.Collections.Generic.List[str]:
        """Signature order of files to be compiled"""
        ...

    @property.setter
    def signature_order(self, value: System.Collections.Generic.List[str]) -> None:
        ...


class BasicBacktest(QuantConnect.Api.RestResponse):
    """Base class for backtest result object response"""

    @property
    def error(self) -> str:
        """Backtest error message"""
        ...

    @property.setter
    def error(self, value: str) -> None:
        ...

    @property
    def stacktrace(self) -> str:
        """Backtest error stacktrace"""
        ...

    @property.setter
    def stacktrace(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """Assigned backtest Id"""
        ...

    @property.setter
    def backtest_id(self, value: str) -> None:
        ...

    @property
    def status(self) -> str:
        """Status of the backtest"""
        ...

    @property.setter
    def status(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the backtest"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def created(self) -> datetime.datetime:
        """Backtest creation date and time"""
        ...

    @property.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def progress(self) -> float:
        """Progress of the backtest in percent 0-1."""
        ...

    @property.setter
    def progress(self, value: float) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """Optimization task ID, if the backtest is part of an optimization"""
        ...

    @property.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def tradeable_dates(self) -> int:
        """Number of tradeable days"""
        ...

    @property.setter
    def tradeable_dates(self, value: int) -> None:
        ...

    @property
    def parameter_set(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """Optimization parameters"""
        ...

    @property.setter
    def parameter_set(self, value: QuantConnect.Optimizer.Parameters.ParameterSet) -> None:
        ...

    @property
    def snap_shot_id(self) -> int:
        """Snapshot id of this backtest result"""
        ...

    @property.setter
    def snap_shot_id(self, value: int) -> None:
        ...


class ResearchGuide(System.Object):
    """A power gauge for backtests, time and parameters to estimate the overfitting risk"""

    @property
    def minutes(self) -> int:
        """Number of minutes used in developing the current backtest"""
        ...

    @property.setter
    def minutes(self, value: int) -> None:
        ...

    @property
    def backtest_count(self) -> int:
        """The quantity of backtests run in the project"""
        ...

    @property.setter
    def backtest_count(self, value: int) -> None:
        ...

    @property
    def parameters(self) -> int:
        """Number of parameters detected"""
        ...

    @property.setter
    def parameters(self, value: int) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project ID"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...


class Backtest(QuantConnect.Api.BasicBacktest):
    """Results object class. Results are exhaust from backtest or live algorithms running in LEAN"""

    @property
    def note(self) -> str:
        """Note on the backtest attached by the user"""
        ...

    @property.setter
    def note(self, value: str) -> None:
        ...

    @property
    def completed(self) -> bool:
        """Boolean true when the backtest is completed."""
        ...

    @property.setter
    def completed(self, value: bool) -> None:
        ...

    @property
    def organization_id(self) -> int:
        """Organization ID"""
        ...

    @property.setter
    def organization_id(self, value: int) -> None:
        ...

    @property
    def rolling_window(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @property.setter
    def rolling_window(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]) -> None:
        ...

    @property
    def total_performance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Total algorithm performance statistics."""
        ...

    @property.setter
    def total_performance(self, value: QuantConnect.Statistics.AlgorithmPerformance) -> None:
        ...

    @property
    def charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @property.setter
    def charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]) -> None:
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
    def research_guide(self) -> QuantConnect.Api.ResearchGuide:
        """A power gauge for backtests, time and parameters to estimate the overfitting risk"""
        ...

    @property.setter
    def research_guide(self, value: QuantConnect.Api.ResearchGuide) -> None:
        ...

    @property
    def backtest_start(self) -> typing.Optional[datetime.datetime]:
        """The starting time of the backtest"""
        ...

    @property.setter
    def backtest_start(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def backtest_end(self) -> typing.Optional[datetime.datetime]:
        """The ending time of the backtest"""
        ...

    @property.setter
    def backtest_end(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def has_initialize_error(self) -> bool:
        """Indicates if the backtest has error during initialization"""
        ...

    @property.setter
    def has_initialize_error(self, value: bool) -> None:
        ...

    @property
    def node_name(self) -> str:
        """The backtest node name"""
        ...

    @property.setter
    def node_name(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """The associated project id"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """End date of out of sample data"""
        ...

    @property.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_days(self) -> typing.Optional[int]:
        """Number of days of out of sample days"""
        ...

    @property.setter
    def out_of_sample_days(self, value: typing.Optional[int]) -> None:
        ...


class ReadChartResponse(QuantConnect.Api.RestResponse):
    """Class for wrapping Read Chart response"""

    @property
    def chart(self) -> QuantConnect.Chart:
        """Chart object from the ReadChart response"""
        ...

    @property.setter
    def chart(self, value: QuantConnect.Chart) -> None:
        ...


class BacktestSummary(QuantConnect.Api.BasicBacktest):
    """Result object class for the List Backtest response from the API"""

    @property
    def sharpe_ratio(self) -> typing.Optional[float]:
        """Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk"""
        ...

    @property.setter
    def sharpe_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def alpha(self) -> typing.Optional[float]:
        """Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns"""
        ...

    @property.setter
    def alpha(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def beta(self) -> typing.Optional[float]:
        """Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance"""
        ...

    @property.setter
    def beta(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def compounding_annual_return(self) -> typing.Optional[float]:
        """Annual compounded returns statistic based on the final-starting capital and years"""
        ...

    @property.setter
    def compounding_annual_return(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def drawdown(self) -> typing.Optional[float]:
        """Drawdown maximum percentage"""
        ...

    @property.setter
    def drawdown(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def loss_rate(self) -> typing.Optional[float]:
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @property.setter
    def loss_rate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def net_profit(self) -> typing.Optional[float]:
        """Net profit percentage"""
        ...

    @property.setter
    def net_profit(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def parameters(self) -> typing.Optional[int]:
        """Number of parameters in the backtest"""
        ...

    @property.setter
    def parameters(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def psr(self) -> typing.Optional[float]:
        """Price-to-sales ratio"""
        ...

    @property.setter
    def psr(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def security_types(self) -> str:
        """SecurityTypes present in the backtest"""
        ...

    @property.setter
    def security_types(self, value: str) -> None:
        ...

    @property
    def sortino_ratio(self) -> typing.Optional[float]:
        """Sortino ratio with respect to risk free rate: measures excess of return per unit of downside risk"""
        ...

    @property.setter
    def sortino_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trades(self) -> typing.Optional[int]:
        """Number of trades in the backtest"""
        ...

    @property.setter
    def trades(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def treynor_ratio(self) -> typing.Optional[float]:
        """Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk"""
        ...

    @property.setter
    def treynor_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def win_rate(self) -> typing.Optional[float]:
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @property.setter
    def win_rate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.List[str]:
        """Collection of tags for the backtest"""
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.List[str]) -> None:
        ...


class BacktestSummaryList(QuantConnect.Api.RestResponse):
    """Collection container for a list of backtest summaries for a project"""

    @property
    def backtests(self) -> System.Collections.Generic.List[QuantConnect.Api.BacktestSummary]:
        """Collection of summarized backtest summary objects"""
        ...

    @property.setter
    def backtests(self, value: System.Collections.Generic.List[QuantConnect.Api.BacktestSummary]) -> None:
        ...

    @property
    def count(self) -> int:
        """Number of backtest summaries retrieved in the response"""
        ...

    @property.setter
    def count(self, value: int) -> None:
        ...


class InsightResponse(QuantConnect.Api.RestResponse):
    """Class containing insights and the number of insights of the live algorithm in the request criteria"""

    @property
    def insights(self) -> System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Collection of insights"""
        ...

    @property.setter
    def insights(self, value: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> None:
        ...

    @property
    def length(self) -> int:
        """Total number of returned insights"""
        ...

    @property.setter
    def length(self, value: int) -> None:
        ...


class BaseLiveAlgorithm(QuantConnect.Api.RestResponse):
    """Class representing the REST response from QC API when creating or reading a live algorithm"""

    @property
    def project_id(self) -> int:
        """Project id for the live instance"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def deploy_id(self) -> str:
        """Unique live algorithm deployment identifier (similar to a backtest id)."""
        ...

    @property.setter
    def deploy_id(self, value: str) -> None:
        ...


class CreateLiveAlgorithmResponse(QuantConnect.Api.BaseLiveAlgorithm):
    """Class representing the REST response from QC API when creating a live algorithm"""

    @property
    def version_id(self) -> int:
        """The version of the Lean used to run the algorithm"""
        ...

    @property.setter
    def version_id(self, value: int) -> None:
        ...

    @property
    def source(self) -> str:
        """Id of the node that will run the algorithm"""
        ...

    @property.setter
    def source(self, value: str) -> None:
        ...

    @property
    def response_code(self) -> str:
        """HTTP status response code"""
        ...

    @property.setter
    def response_code(self, value: str) -> None:
        ...


class LiveAlgorithmSummary(QuantConnect.Api.BaseLiveAlgorithm):
    """Response from List Live Algorithms request to QuantConnect Rest API."""

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Algorithm status: running, stopped or runtime error."""
        ...

    @property.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    def launched(self) -> datetime.datetime:
        """Datetime the algorithm was launched in UTC."""
        ...

    @property.setter
    def launched(self, value: datetime.datetime) -> None:
        ...

    @property
    def stopped(self) -> typing.Optional[datetime.datetime]:
        """Datetime the algorithm was stopped in UTC, null if its still running."""
        ...

    @property.setter
    def stopped(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def brokerage(self) -> str:
        """Brokerage"""
        ...

    @property.setter
    def brokerage(self, value: str) -> None:
        ...

    @property
    def subscription(self) -> str:
        """Chart we're subscribed to"""
        ...

    @property.setter
    def subscription(self, value: str) -> None:
        ...

    @property
    def error(self) -> str:
        """Live algorithm error message from a crash or algorithm runtime error."""
        ...

    @property.setter
    def error(self, value: str) -> None:
        ...


class LiveList(QuantConnect.Api.RestResponse):
    """List of the live algorithms running which match the requested status"""

    @property
    def algorithms(self) -> System.Collections.Generic.List[QuantConnect.Api.LiveAlgorithmSummary]:
        """Algorithm list matching the requested status."""
        ...

    @property.setter
    def algorithms(self, value: System.Collections.Generic.List[QuantConnect.Api.LiveAlgorithmSummary]) -> None:
        ...


class LiveAlgorithmResults(QuantConnect.Api.RestResponse):
    """Details a live algorithm from the "live/read" Api endpoint"""

    @property
    def message(self) -> str:
        """Error message"""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def status(self) -> str:
        """Indicates the status of the algorihtm, i.e. 'Running', 'Stopped'"""
        ...

    @property.setter
    def status(self, value: str) -> None:
        ...

    @property
    def deploy_id(self) -> str:
        """Algorithm deployment ID"""
        ...

    @property.setter
    def deploy_id(self, value: str) -> None:
        ...

    @property
    def clone_id(self) -> int:
        """The snapshot project ID for cloning the live development's source code."""
        ...

    @property.setter
    def clone_id(self, value: int) -> None:
        ...

    @property
    def launched(self) -> datetime.datetime:
        """Date the live algorithm was launched"""
        ...

    @property.setter
    def launched(self, value: datetime.datetime) -> None:
        ...

    @property
    def stopped(self) -> typing.Optional[datetime.datetime]:
        """Date the live algorithm was stopped"""
        ...

    @property.setter
    def stopped(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def brokerage(self) -> str:
        """Brokerage used in the live algorithm"""
        ...

    @property.setter
    def brokerage(self, value: str) -> None:
        ...

    @property
    def security_types(self) -> str:
        """Security types present in the live algorithm"""
        ...

    @property.setter
    def security_types(self, value: str) -> None:
        ...

    @property
    def project_name(self) -> str:
        """Name of the project the live algorithm is in"""
        ...

    @property.setter
    def project_name(self, value: str) -> None:
        ...

    @property
    def datacenter(self) -> str:
        """Name of the data center where the algorithm is physically located."""
        ...

    @property.setter
    def datacenter(self, value: str) -> None:
        ...

    @property
    def public(self) -> bool:
        """Indicates if the algorithm is being live shared"""
        ...

    @property.setter
    def public(self, value: bool) -> None:
        ...

    @property
    def files(self) -> System.Collections.Generic.List[QuantConnect.Api.ProjectFile]:
        """Files present in the project in which the algorithm is"""
        ...

    @property.setter
    def files(self, value: System.Collections.Generic.List[QuantConnect.Api.ProjectFile]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @property.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @property.setter
    def charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]) -> None:
        ...


class Portfolio(System.Object):
    """Class containing the basic portfolio information of a live algorithm"""

    @property
    def holdings(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Holding]:
        """Dictionary of algorithm holdings information"""
        ...

    @property.setter
    def holdings(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Holding]) -> None:
        ...

    @property
    def cash(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Dictionary of algorithm cash currencies information"""
        ...

    @property.setter
    def cash(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]) -> None:
        ...


class PortfolioResponse(QuantConnect.Api.RestResponse):
    """Response class for reading the portfolio of a live algorithm"""

    @property
    def portfolio(self) -> QuantConnect.Api.Portfolio:
        """Object containing the basic portfolio information of a live algorithm"""
        ...

    @property.setter
    def portfolio(self, value: QuantConnect.Api.Portfolio) -> None:
        ...


class LiveLog(QuantConnect.Api.RestResponse):
    """Logs from a live algorithm"""

    @property
    def logs(self) -> System.Collections.Generic.List[str]:
        """List of logs from the live algorithm"""
        ...

    @property.setter
    def logs(self, value: System.Collections.Generic.List[str]) -> None:
        ...

    @property
    def length(self) -> int:
        """Total amount of rows in the logs"""
        ...

    @property.setter
    def length(self, value: int) -> None:
        ...

    @property
    def deployment_offset(self) -> int:
        """Amount of log rows before the current deployment"""
        ...

    @property.setter
    def deployment_offset(self, value: int) -> None:
        ...


class DataLink(QuantConnect.Api.RestResponse):
    """Data/Read response wrapper, contains link to requested data"""

    @property
    def link(self) -> str:
        """Url to the data requested"""
        ...

    @property.setter
    def link(self, value: str) -> None:
        ...

    @property
    def balance(self) -> float:
        """Remaining QCC balance on account after this transaction"""
        ...

    @property.setter
    def balance(self, value: float) -> None:
        ...

    @property
    def cost(self) -> float:
        """QCC Cost for this data link"""
        ...

    @property.setter
    def cost(self, value: float) -> None:
        ...


class DataList(QuantConnect.Api.RestResponse):
    """Data/List response wrapper for available data"""

    @property
    def available_data(self) -> System.Collections.Generic.List[str]:
        """List of all available data from this request"""
        ...

    @property.setter
    def available_data(self, value: System.Collections.Generic.List[str]) -> None:
        ...


class PriceEntry(System.Object):
    """Prices entry for Data/Prices response"""

    @property
    def vendor(self) -> str:
        """Vendor for this price"""
        ...

    @property.setter
    def vendor(self, value: str) -> None:
        ...

    @property
    def reg_ex(self) -> System.Text.RegularExpressions.Regex:
        """
        Regex for this data price entry
        Trims regex open, close, and multiline flag
        because it won't match otherwise
        """
        ...

    @property
    def raw_reg_ex(self) -> str:
        """RegEx directly from response"""
        ...

    @property.setter
    def raw_reg_ex(self, value: str) -> None:
        ...

    @property
    def price(self) -> typing.Optional[int]:
        """The price for this entry in QCC"""
        ...

    @property.setter
    def price(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def type(self) -> str:
        """The type associated to this price entry if any"""
        ...

    @property.setter
    def type(self, value: str) -> None:
        ...

    @property
    def subscribed(self) -> typing.Optional[bool]:
        """True if the user is subscribed"""
        ...

    @property.setter
    def subscribed(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    def product_id(self) -> int:
        """The associated product id"""
        ...

    @property.setter
    def product_id(self, value: int) -> None:
        ...

    @property
    def paths(self) -> System.Collections.Generic.HashSet[str]:
        """The associated data paths"""
        ...

    @property.setter
    def paths(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...


class DataPricesList(QuantConnect.Api.RestResponse):
    """Data/Prices response wrapper for prices by vendor"""

    @property
    def prices(self) -> System.Collections.Generic.List[QuantConnect.Api.PriceEntry]:
        """Collection of prices objects"""
        ...

    @property.setter
    def prices(self, value: System.Collections.Generic.List[QuantConnect.Api.PriceEntry]) -> None:
        ...

    @property
    def agreement_url(self) -> str:
        """The Agreement URL for this Organization"""
        ...

    @property.setter
    def agreement_url(self, value: str) -> None:
        ...

    def get_price(self, path: str) -> int:
        """
        Get the price in QCC for a given data file
        
        :param path: Lean data path of the file
        :returns: QCC price for data, -1 if no entry found.
        """
        ...


class BacktestReport(QuantConnect.Api.RestResponse):
    """Backtest Report Response wrapper"""

    @property
    def report(self) -> str:
        """HTML data of the report with embedded base64 images"""
        ...

    @property.setter
    def report(self, value: str) -> None:
        ...


class Card(System.Object):
    """Credit card"""

    @property
    def brand(self) -> str:
        """Credit card brand"""
        ...

    @property.setter
    def brand(self, value: str) -> None:
        ...

    @property
    def expiration(self) -> datetime.datetime:
        """The credit card expiration"""
        ...

    @property.setter
    def expiration(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_four_digits(self) -> float:
        """The last 4 digits of the card"""
        ...

    @property.setter
    def last_four_digits(self, value: float) -> None:
        ...


class Account(QuantConnect.Api.RestResponse):
    """Account information for an organization"""

    @property
    def organization_id(self) -> str:
        """The organization Id"""
        ...

    @property.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def credit_balance(self) -> float:
        """The current account balance"""
        ...

    @property.setter
    def credit_balance(self, value: float) -> None:
        ...

    @property
    def card(self) -> QuantConnect.Api.Card:
        """The current organizations credit card"""
        ...

    @property.setter
    def card(self, value: QuantConnect.Api.Card) -> None:
        ...


class DataAgreement(System.Object):
    """Organization Data Agreement"""

    @property
    def epoch_signed_time(self) -> typing.Optional[int]:
        """Epoch time the Data Agreement was Signed"""
        ...

    @property.setter
    def epoch_signed_time(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def signed_time(self) -> typing.Optional[datetime.datetime]:
        """
        DateTime the agreement was signed.
        Uses EpochSignedTime converted to a standard datetime.
        """
        ...

    @property
    def signed(self) -> bool:
        """True/False if it is currently signed"""
        ...

    @property.setter
    def signed(self, value: bool) -> None:
        ...


class Credit(System.Object):
    """Organization Credit Object"""

    @property
    def balance(self) -> float:
        """QCC Current Balance"""
        ...

    @property.setter
    def balance(self, value: float) -> None:
        ...


class ProductType(Enum):
    """
    Product types offered by QuantConnect
    Used by Product class
    """

    PROFESSIONAL_SEATS = 0
    """Professional Seats Subscriptions"""

    BACKTEST_NODE = 1
    """Backtest Nodes Subscriptions"""

    RESEARCH_NODE = 2
    """Research Nodes Subscriptions"""

    LIVE_NODE = 3
    """Live Trading Nodes Subscriptions"""

    SUPPORT = 4
    """Support Subscriptions"""

    DATA = 5
    """Data Subscriptions"""

    MODULES = 6
    """Modules Subscriptions"""


class ProductItem(System.Object):
    """QuantConnect ProductItem"""

    @property
    def id(self) -> int:
        """ID for this product"""
        ...

    @property.setter
    def id(self, value: int) -> None:
        ...

    @property
    def quantity(self) -> int:
        """Quantity for this product"""
        ...

    @property.setter
    def quantity(self, value: int) -> None:
        ...


class Product(System.Object):
    """QuantConnect Products"""

    @property
    def type(self) -> QuantConnect.Api.ProductType:
        """Product Type"""
        ...

    @property.setter
    def type(self, value: QuantConnect.Api.ProductType) -> None:
        ...

    @property
    def items(self) -> System.Collections.Generic.List[QuantConnect.Api.ProductItem]:
        """
        Collection of item subscriptions
        Nodes/Data/Seats/etc
        """
        ...

    @property.setter
    def items(self, value: System.Collections.Generic.List[QuantConnect.Api.ProductItem]) -> None:
        ...


class Organization(QuantConnect.Api.StringRepresentation):
    """Object representation of Organization from QuantConnect Api"""

    @property
    def data_agreement(self) -> QuantConnect.Api.DataAgreement:
        """Data Agreement information"""
        ...

    @property.setter
    def data_agreement(self, value: QuantConnect.Api.DataAgreement) -> None:
        ...

    @property
    def products(self) -> System.Collections.Generic.List[QuantConnect.Api.Product]:
        """Organization Product Subscriptions"""
        ...

    @property.setter
    def products(self, value: System.Collections.Generic.List[QuantConnect.Api.Product]) -> None:
        ...

    @property
    def credit(self) -> QuantConnect.Api.Credit:
        """Organization Credit Balance and Transactions"""
        ...

    @property.setter
    def credit(self, value: QuantConnect.Api.Credit) -> None:
        ...


class Estimate(QuantConnect.Api.StringRepresentation):
    """Estimate response packet from the QuantConnect.com API."""

    @property
    def estimate_id(self) -> str:
        """Estimate id"""
        ...

    @property.setter
    def estimate_id(self, value: str) -> None:
        ...

    @property
    def time(self) -> int:
        """Estimate time in seconds"""
        ...

    @property.setter
    def time(self, value: int) -> None:
        ...

    @property
    def balance(self) -> int:
        """Estimate balance in QCC"""
        ...

    @property.setter
    def balance(self, value: int) -> None:
        ...


class BaseOptimization(QuantConnect.Api.RestResponse):
    """BaseOptimization item from the QuantConnect.com API."""

    @property
    def optimization_id(self) -> str:
        """Optimization ID"""
        ...

    @property.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project ID of the project the optimization belongs to"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the optimization"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def status(self) -> QuantConnect.Optimizer.OptimizationStatus:
        """Status of the optimization"""
        ...

    @property.setter
    def status(self, value: QuantConnect.Optimizer.OptimizationStatus) -> None:
        ...

    @property
    def node_type(self) -> str:
        """Optimization node type"""
        ...

    @property.setter
    def node_type(self, value: str) -> None:
        ...

    @property
    def out_of_sample_days(self) -> int:
        """Number of days of out of sample days"""
        ...

    @property.setter
    def out_of_sample_days(self, value: int) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """End date of out of sample data"""
        ...

    @property.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def parameters(self) -> System.Collections.Generic.List[QuantConnect.Optimizer.Parameters.OptimizationParameter]:
        """Parameters used in this optimization"""
        ...

    @property.setter
    def parameters(self, value: System.Collections.Generic.List[QuantConnect.Optimizer.Parameters.OptimizationParameter]) -> None:
        ...

    @property
    def criterion(self) -> QuantConnect.Optimizer.Objectives.Target:
        """Optimization statistical target"""
        ...

    @property.setter
    def criterion(self, value: QuantConnect.Optimizer.Objectives.Target) -> None:
        ...


class OptimizationSummary(QuantConnect.Api.BaseOptimization):
    """Optimization summary response for creating an optimization"""

    @property
    def created(self) -> datetime.datetime:
        """Date when this optimization was created"""
        ...

    @property.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def psr(self) -> typing.Optional[float]:
        """Price-sales ratio stastic"""
        ...

    @property.setter
    def psr(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sharpe_ratio(self) -> typing.Optional[float]:
        """Sharpe ratio statistic"""
        ...

    @property.setter
    def sharpe_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trades(self) -> typing.Optional[int]:
        """Number of trades"""
        ...

    @property.setter
    def trades(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def clone_id(self) -> typing.Optional[int]:
        """ID of project, were this current project was originally cloned"""
        ...

    @property.setter
    def clone_id(self, value: typing.Optional[int]) -> None:
        ...


class OptimizationBacktest(System.Object):
    """OptimizationBacktest object from the QuantConnect.com API."""

    @property
    def progress(self) -> float:
        """Progress of the backtest as a percentage from 0-1 based on the days lapsed from start-finish."""
        ...

    @property.setter
    def progress(self, value: float) -> None:
        ...

    @property
    def name(self) -> str:
        """The backtest name"""
        ...

    @property
    def host_name(self) -> str:
        """The backtest host name"""
        ...

    @property.setter
    def host_name(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """The backtest id"""
        ...

    @property
    def parameter_set(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """Represent a combination as key value of parameters, i.e. order doesn't matter"""
        ...

    @property
    def statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """The backtest statistics results"""
        ...

    @property.setter
    def statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def equity(self) -> QuantConnect.CandlestickSeries:
        """The backtest equity chart series"""
        ...

    @property.setter
    def equity(self, value: QuantConnect.CandlestickSeries) -> None:
        ...

    @property
    def exit_code(self) -> int:
        """The exit code of this backtest"""
        ...

    @property.setter
    def exit_code(self, value: int) -> None:
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
    def start_date(self) -> datetime.datetime:
        """The backtest start date"""
        ...

    @property.setter
    def start_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_date(self) -> datetime.datetime:
        """The backtest end date"""
        ...

    @property.setter
    def end_date(self, value: datetime.datetime) -> None:
        ...

    def __init__(self, parameterSet: QuantConnect.Optimizer.Parameters.ParameterSet, backtestId: str, name: str) -> None:
        """
        Creates a new instance
        
        :param parameterSet: The parameter set
        :param backtestId: The backtest id if any
        :param name: The backtest name
        """
        ...


class Optimization(QuantConnect.Api.BaseOptimization):
    """Optimization response packet from the QuantConnect.com API."""

    @property
    def snapshot_id(self) -> typing.Optional[int]:
        """Snapshot ID of this optimization"""
        ...

    @property.setter
    def snapshot_id(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def optimization_target(self) -> str:
        """Statistic to be optimized"""
        ...

    @property.setter
    def optimization_target(self, value: str) -> None:
        ...

    @property
    def grid_layout(self) -> System.Collections.Generic.List[QuantConnect.Api.GridChart]:
        """List with grid charts representing the grid layout"""
        ...

    @property.setter
    def grid_layout(self, value: System.Collections.Generic.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics for the optimization"""
        ...

    @property.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def constraints(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]:
        """Optimization constraints"""
        ...

    @property.setter
    def constraints(self, value: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]) -> None:
        ...

    @property
    def parallel_nodes(self) -> int:
        """Number of parallel nodes for optimization"""
        ...

    @property.setter
    def parallel_nodes(self, value: int) -> None:
        ...

    @property
    def backtests(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Api.OptimizationBacktest]:
        """Optimization constraints"""
        ...

    @property.setter
    def backtests(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Api.OptimizationBacktest]) -> None:
        ...

    @property
    def strategy(self) -> str:
        """Optimization strategy"""
        ...

    @property.setter
    def strategy(self, value: str) -> None:
        ...

    @property
    def requested(self) -> datetime.datetime:
        """Optimization requested date and time"""
        ...

    @property.setter
    def requested(self, value: datetime.datetime) -> None:
        ...


class BasicObjectStore(System.Object):
    """Class contining basic store properties present in the REST response from QC API"""

    @property
    def key(self) -> str:
        """Object store key"""
        ...

    @property.setter
    def key(self, value: str) -> None:
        ...

    @property
    def modified(self) -> typing.Optional[datetime.datetime]:
        """Last time it was modified"""
        ...

    @property.setter
    def modified(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def mime(self) -> str:
        """MIME type"""
        ...

    @property.setter
    def mime(self, value: str) -> None:
        ...

    @property
    def size(self) -> typing.Optional[float]:
        """File size"""
        ...

    @property.setter
    def size(self, value: typing.Optional[float]) -> None:
        ...


class PropertiesObjectStore(QuantConnect.Api.BasicObjectStore):
    """Object Store file properties"""

    @property
    def created(self) -> datetime.datetime:
        """Date this object was created"""
        ...

    @property.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def md_5(self) -> str:
        """MD5 (hashing algorithm) hash authentication code"""
        ...

    @property.setter
    def md_5(self, value: str) -> None:
        ...

    @property
    def preview(self) -> str:
        """Preview of the Object Store file content"""
        ...

    @property.setter
    def preview(self, value: str) -> None:
        ...


class PropertiesObjectStoreResponse(QuantConnect.Api.RestResponse):
    """Response received containing the properties of the requested Object Store"""

    @property
    def properties(self) -> QuantConnect.Api.PropertiesObjectStore:
        """Object Store properties"""
        ...

    @property.setter
    def properties(self, value: QuantConnect.Api.PropertiesObjectStore) -> None:
        ...


class SummaryObjectStore(QuantConnect.Api.BasicObjectStore):
    """Summary information of the Object Store"""

    @property
    def name(self) -> str:
        """File or folder name"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def is_folder(self) -> bool:
        """True if it is a folder, false otherwise"""
        ...

    @property.setter
    def is_folder(self, value: bool) -> None:
        ...


class ListObjectStoreResponse(QuantConnect.Api.RestResponse):
    """Response received containing a list of stored objects metadata, as well as the total size of all of them."""

    @property
    def path(self) -> str:
        """Path to the files in the Object Store"""
        ...

    @property.setter
    def path(self, value: str) -> None:
        ...

    @property
    def objects(self) -> System.Collections.Generic.List[QuantConnect.Api.SummaryObjectStore]:
        """List of objects stored"""
        ...

    @property.setter
    def objects(self, value: System.Collections.Generic.List[QuantConnect.Api.SummaryObjectStore]) -> None:
        ...

    @property
    def object_storage_used(self) -> int:
        """Size of all objects stored in bytes"""
        ...

    @property.setter
    def object_storage_used(self, value: int) -> None:
        ...

    @property
    def object_storage_used_human(self) -> str:
        """Size of all the objects stored in human-readable format"""
        ...

    @property.setter
    def object_storage_used_human(self, value: str) -> None:
        ...


class Api(System.Object, QuantConnect.Interfaces.IApi, QuantConnect.Interfaces.IDownloadProvider):
    """QuantConnect.com Interaction Via API."""

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
    def api_connection(self) -> QuantConnect.Api.ApiConnection:
        """
        Returns the underlying API connection
        
        This property is protected.
        """
        ...

    @property
    def connected(self) -> bool:
        """Check if Api is successfully connected with correct credentials"""
        ...

    def __init__(self) -> None:
        """Creates a new instance of Api"""
        ...

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
        """
        Create a new backtest request and get the id.
        
        :param project_id: Id for the project to backtest
        :param compile_id: Compile id for the project
        :param backtest_name: Name for the new backtest
        :returns: Backtestt.
        """
        ...

    def create_compile(self, project_id: int) -> QuantConnect.Api.Compile:
        """
        Create a new compile job request for this project id.
        
        :param project_id: Project id we wish to compile.
        :returns: Compile object result.
        """
        ...

    @overload
    def create_live_algorithm(self, project_id: int, compile_id: str, node_id: str, brokerage_settings: System.Collections.Generic.Dictionary[str, System.Object], version_id: str = "-1", data_providers: System.Collections.Generic.Dictionary[str, System.Object] = None) -> QuantConnect.Api.CreateLiveAlgorithmResponse:
        """
        Create a live algorithm.
        
        :param project_id: Id of the project on QuantConnect
        :param compile_id: Id of the compilation on QuantConnect
        :param node_id: Id of the node that will run the algorithm
        :param brokerage_settings: Dictionary with brokerage specific settings. Each brokerage requires certain specific credentials                         in order to process the given orders. Each key in this dictionary represents a required field/credential                         to provide to the brokerage API and its value represents the value of that field. For example: "brokerage_settings: {                         "id": "Binance", "binance-api-secret": "123ABC", "binance-api-key": "ABC123"}. It is worth saying,                         that this dictionary must always contain an entry whose key is "id" and its value is the name of the brokerage                         (see Brokerages.BrokerageName)
        :param version_id: The version of the Lean used to run the algorithm.                         -1 is master, however, sometimes this can create problems with live deployments.                         If you experience problems using, try specifying the version of Lean you would like to use.
        :param data_providers: Dictionary with data providers credentials. Each data provider requires certain credentials                         in order to retrieve data from their API. Each key in this dictionary describes a data provider name                         and its corresponding value is another dictionary with the required key-value pairs of credential                         names and values. For example: "data_providers: { "InteractiveBrokersBrokerage" : { "id": 12345, "environment" : "paper",                         "username": "testUsername", "password": "testPassword"}}"
        :returns: Information regarding the new algorithm CreateLiveAlgorithmResponse.
        """
        ...

    @overload
    def create_live_algorithm(self, project_id: int, compile_id: str, node_id: str, brokerage_settings: typing.Any, version_id: str = "-1", data_providers: typing.Any = None) -> QuantConnect.Api.CreateLiveAlgorithmResponse:
        """
        Create a live algorithm.
        
        :param project_id: Id of the project on QuantConnect
        :param compile_id: Id of the compilation on QuantConnect
        :param node_id: Id of the node that will run the algorithm
        :param brokerage_settings: Python Dictionary with brokerage specific settings. Each brokerage requires certain specific credentials                         in order to process the given orders. Each key in this dictionary represents a required field/credential                         to provide to the brokerage API and its value represents the value of that field. For example: "brokerage_settings: {                         "id": "Binance", "binance-api-secret": "123ABC", "binance-api-key": "ABC123"}. It is worth saying,                         that this dictionary must always contain an entry whose key is "id" and its value is the name of the brokerage                         (see Brokerages.BrokerageName)
        :param version_id: The version of the Lean used to run the algorithm.                         -1 is master, however, sometimes this can create problems with live deployments.                         If you experience problems using, try specifying the version of Lean you would like to use.
        :param data_providers: Python Dictionary with data providers credentials. Each data provider requires certain credentials                         in order to retrieve data from their API. Each key in this dictionary describes a data provider name                         and its corresponding value is another dictionary with the required key-value pairs of credential                         names and values. For example: "data_providers: { "InteractiveBrokersBrokerage" : { "id": 12345, "environment" : "paper",                         "username": "testUsername", "password": "testPassword"}}"
        :returns: Information regarding the new algorithm CreateLiveAlgorithmResponse.
        """
        ...

    def create_live_command(self, project_id: int, command: typing.Any) -> QuantConnect.Api.RestResponse:
        """
        Create a live command
        
        :param project_id: Project for the live instance we want to run the command against
        :param command: The command to run
        :returns: RestResponse.
        """
        ...

    def create_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], estimated_cost: float, node_type: str, parallel_nodes: int) -> QuantConnect.Api.OptimizationSummary:
        """
        Create an optimization with the specified parameters via QuantConnect.com API
        
        :param project_id: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param target_to: Target extremum of the optimization, for example "max" or "min"
        :param target_value: Optimization target value
        :param strategy: Optimization strategy, QuantConnect.Optimizer.Strategies.GridSearchOptimizationStrategy
        :param compile_id: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :param estimated_cost: Estimated cost for optimization
        :param node_type: Optimization node type OptimizationNodes
        :param parallel_nodes: Number of parallel nodes for optimization
        :returns: BaseOptimization object from the API.
        """
        ...

    def create_project(self, name: str, language: QuantConnect.Language, organization_id: str = None) -> QuantConnect.Api.ProjectResponse:
        """
        Create a project with the specified name and language via QuantConnect.com API
        
        :param name: Project name
        :param language: Programming language to use
        :param organization_id: Optional param for specifying organization to create project under. If none provided web defaults to preferred.
        :returns: Project object from the API.
        """
        ...

    @staticmethod
    def create_secure_hash(timestamp: int, token: str) -> str:
        """
        Generate a secure hash for the authorization headers.
        
        :returns: Time based hash of user token and timestamp.
        """
        ...

    def delete_backtest(self, project_id: int, backtest_id: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a backtest from the specified project and backtest_id.
        
        :param project_id: Project for the backtest we want to delete
        :param backtest_id: Backtest id we want to delete
        :returns: RestResponse.
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
        Delete a project
        
        :param project_id: Project id we own and wish to delete
        :returns: RestResponse indicating success.
        """
        ...

    def delete_project_file(self, project_id: int, name: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a file in a project
        
        :param project_id: Project id to which the file belongs
        :param name: The name of the file that should be deleted
        :returns: RestResponse that includes the information about all files in the project.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
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
        :returns: A stream from which the data can be read.
        """
        ...

    def download_data(self, file_path: str, organization_id: str) -> bool:
        """
        Method to purchase and download data from QuantConnect
        
        :param file_path: File path representing the data requested
        :param organization_id: Organization to buy the data with
        :returns: A bool indicating whether the data was successfully downloaded or not.
        """
        ...

    def estimate_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]) -> QuantConnect.Api.Estimate:
        """
        Estimate optimization with the specified parameters via QuantConnect.com API
        
        :param project_id: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param target_to: Target extremum of the optimization, for example "max" or "min"
        :param target_value: Optimization target value
        :param strategy: Optimization strategy, QuantConnect.Optimizer.Strategies.GridSearchOptimizationStrategy
        :param compile_id: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :returns: Estimate object from the API.
        """
        ...

    @staticmethod
    def format_path_for_data_request(file_path: str, data_folder: str = None) -> str:
        """
        Helper method to normalize path for api data requests
        
        :param file_path: Filepath to format
        :param data_folder: The data folder to use
        :returns: Normalized path.
        """
        ...

    def get_algorithm_status(self, algorithm_id: str) -> QuantConnect.AlgorithmControl:
        """
        Get the algorithm status from the user with this algorithm id.
        
        :param algorithm_id: String algorithm id we're searching for.
        :returns: Algorithm status enum.
        """
        ...

    def get_object_store(self, organization_id: str, keys: System.Collections.Generic.List[str], destination_folder: str = None) -> bool:
        """
        Download the object store files associated with the given organization ID and key
        
        :param organization_id: Organization ID we would like to get the Object Store files from
        :param keys: Keys for the Object Store files
        :param destination_folder: Folder in which the object store files will be stored
        :returns: True if the object store files were retrieved correctly, false otherwise.
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
        """Initialize the API with the given variables"""
        ...

    def liquidate_live_algorithm(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Liquidate a live algorithm from the specified project and deployId.
        
        :param project_id: Project for the live instance we want to stop
        :returns: RestResponse.
        """
        ...

    def list_backtests(self, project_id: int, include_statistics: bool = True) -> QuantConnect.Api.BacktestSummaryList:
        """
        List all the backtest summaries for a project
        
        :param project_id: Project id we'd like to get a list of backtest for
        :param include_statistics: True for include statistics in the response, false otherwise
        :returns: BacktestList.
        """
        ...

    def list_live_algorithms(self, status: typing.Optional[QuantConnect.AlgorithmStatus] = None, start_time: typing.Optional[datetime.datetime] = None, end_time: typing.Optional[datetime.datetime] = None) -> QuantConnect.Api.LiveList:
        """
        Get a list of live running algorithms for user
        
        :param status: Filter the statuses of the algorithms returned from the api
        :param start_time: Earliest launched time of the algorithms returned by the Api
        :param end_time: Latest launched time of the algorithms returned by the Api
        :returns: LiveList.
        """
        ...

    def list_object_store(self, organization_id: str, path: str) -> QuantConnect.Api.ListObjectStoreResponse:
        """
        Request to list Object Store files of a specific organization and path
        
        :param organization_id: Organization ID we would like to list the Object Store files from
        :param path: Path to the Object Store files
        :returns: ListObjectStoreResponse.
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
        List details of all projects
        
        :returns: ProjectResponse that contains information regarding the project.
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
        Read out a backtest in the project id specified.
        
        :param project_id: Project id to read
        :param backtest_id: Specific backtest id to read
        :param get_charts: True will return backtest charts
        :returns: Backtest.
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
        :returns: The chart.
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

    def read_backtest_orders(self, project_id: int, backtest_id: str, start: int = 0, end: int = 100) -> System.Collections.Generic.List[QuantConnect.Orders.ApiOrderResponse]:
        """
        Returns the orders of the specified backtest and project id.
        
        :param project_id: Id of the project from which to read the orders
        :param backtest_id: Id of the backtest from which to read the orders
        :param start: Starting index of the orders to be fetched. Required if end > 100
        :param end: Last index of the orders to be fetched. Note that end - start must be less than 100
        :returns: The list of Order.
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
        :returns: Compile.
        """
        ...

    def read_data_directory(self, file_path: str) -> QuantConnect.Api.DataList:
        """Get valid data entries for a given filepath from data/list"""
        ...

    def read_data_link(self, file_path: str, organization_id: str) -> QuantConnect.Api.DataLink:
        """
        Gets the link to the downloadable data.
        
        :param file_path: File path representing the data requested
        :param organization_id: Organization to download from
        :returns: DataLink to the downloadable data.
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
        :returns: LiveAlgorithmResults.
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
        :returns: The chart.
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
        :returns: LiveLog List of strings that represent the logs of the algorithm.
        """
        ...

    def read_live_orders(self, project_id: int, start: int = 0, end: int = 100) -> System.Collections.Generic.List[QuantConnect.Orders.ApiOrderResponse]:
        """
        Returns the orders of the specified project id live algorithm.
        
        :param project_id: Id of the project from which to read the live orders
        :param start: Starting index of the orders to be fetched. Required if end > 100
        :param end: Last index of the orders to be fetched. Note that end - start must be less than 100
        :returns: The list of Order.
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
        Get details about a single project
        
        :param project_id: Id of the project
        :returns: ProjectResponse that contains information regarding the project.
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
        :param net_return: Net return for the deployment
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
        Algorithm passes back its current status to the UX.
        
        :param algorithm_id: String algorithm id we're setting.
        :param status: Status of the current algorithm
        :param message: Message for the algorithm status event
        :returns: Algorithm status enum.
        """
        ...

    def set_object_store(self, organization_id: str, key: str, object_data: typing.List[int]) -> QuantConnect.Api.RestResponse:
        """
        Upload files to the Object Store
        
        :param organization_id: Organization ID we would like to upload the file to
        :param key: Key to the Object Store file
        :param object_data: File (as an array of bytes) to be uploaded
        :returns: RestResponse.
        """
        ...

    def stop_live_algorithm(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Stop a live algorithm from the specified project and deployId.
        
        :param project_id: Project for the live instance we want to stop
        :returns: RestResponse.
        """
        ...

    def update_backtest(self, project_id: int, backtest_id: str, name: str = ..., note: str = ...) -> QuantConnect.Api.RestResponse:
        """
        Update a backtest name
        
        :param project_id: Project for the backtest we want to update
        :param backtest_id: Backtest id we want to update
        :param name: Name we'd like to assign to the backtest
        :param note: Note attached to the backtest
        :returns: RestResponse.
        """
        ...

    def update_backtest_tags(self, project_id: int, backtest_id: str, tags: System.Collections.Generic.IReadOnlyCollection[str]) -> QuantConnect.Api.RestResponse:
        """
        Updates the tags collection for a backtest
        
        :param project_id: Project for the backtest we want to update
        :param backtest_id: Backtest id we want to update
        :param tags: The new backtest tags
        :returns: RestResponse.
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


class OptimizationResponseWrapper(QuantConnect.Api.RestResponse):
    """Wrapper class for Optimizations/Read endpoint JSON response"""

    @property
    def optimization(self) -> QuantConnect.Api.Optimization:
        """Optimization object"""
        ...

    @property.setter
    def optimization(self, value: QuantConnect.Api.Optimization) -> None:
        ...


class OptimizationList(QuantConnect.Api.RestResponse):
    """Collection container for a list of summarized optimizations for a project"""

    @property
    def optimizations(self) -> System.Collections.Generic.List[QuantConnect.Api.OptimizationSummary]:
        """Collection of summarized optimization objects"""
        ...

    @property.setter
    def optimizations(self, value: System.Collections.Generic.List[QuantConnect.Api.OptimizationSummary]) -> None:
        ...

    @property
    def count(self) -> int:
        """The optimization count"""
        ...


class LiveAlgorithmResultsJsonConverter(JsonConverter):
    """Custom JsonConverter for LiveResults data for live algorithms"""

    @property
    def can_write(self) -> bool:
        """Gets a value indicating whether this Newtonsoft.Json.JsonConverter can write JSON."""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class CreatedNode(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/create, reads in the nodes information into a
    node object
    """

    @property
    def node(self) -> QuantConnect.Api.Node:
        """The created node from node/create"""
        ...

    @property.setter
    def node(self, value: QuantConnect.Api.Node) -> None:
        ...


class NodeType(Enum):
    """
    NodeTypes enum for all possible options of target environments
    Used in conjuction with SKU class as a NodeType is a required parameter for SKU
    """

    BACKTEST = 0

    RESEARCH = 1

    LIVE = 2


class SKU(System.Object):
    """
    Class for generating a SKU for a node with a given configuration
    Every SKU is made up of 3 variables:
    - Target environment (L for live, B for Backtest, R for Research)
    - CPU core count
    - Dedicated RAM (GB)
    """

    @property
    def cores(self) -> int:
        """The number of CPU cores in the node"""
        ...

    @property.setter
    def cores(self, value: int) -> None:
        ...

    @property
    def memory(self) -> int:
        """Size of RAM in GB of the Node"""
        ...

    @property.setter
    def memory(self, value: int) -> None:
        ...

    @property
    def target(self) -> QuantConnect.Api.NodeType:
        """Target environment for the node"""
        ...

    @property.setter
    def target(self, value: QuantConnect.Api.NodeType) -> None:
        ...

    def __init__(self, cores: int, memory: int, target: QuantConnect.Api.NodeType) -> None:
        """
        Constructs a SKU object out of the provided node configuration
        
        :param cores: Number of cores
        :param memory: Size of RAM in GBs
        :param target: Target Environment Live/Backtest/Research
        """
        ...

    def to_string(self) -> str:
        """
        Generates the SKU string for API calls based on the specifications of the node
        
        :returns: String representation of the SKU.
        """
        ...


class OptimizationNodes(System.Object):
    """Supported optimization nodes"""

    O_2_8: str
    """2 CPUs 8 GB ram"""

    O_4_12: str
    """4 CPUs 12 GB ram"""

    O_8_16: str
    """8 CPUs 16 GB ram"""


class AuthenticationResponse(QuantConnect.Api.RestResponse):
    """Verify if the credentials are OK."""


class GetObjectStoreResponse(QuantConnect.Api.RestResponse):
    """Response received when fetching Object Store"""

    @property
    def job_id(self) -> str:
        """Job ID which can be used for querying state or packaging"""
        ...

    @property.setter
    def job_id(self, value: str) -> None:
        ...

    @property
    def url(self) -> str:
        """The URL to download the object. This can also be null"""
        ...

    @property.setter
    def url(self, value: str) -> None:
        ...


class LiveResultsData(System.Object):
    """Holds information about the state and operation of the live running algorithm"""

    @property
    def version(self) -> int:
        """Results version"""
        ...

    @property.setter
    def version(self, value: int) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """Temporal resolution of the results returned from the Api"""
        ...

    @property.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def results(self) -> QuantConnect.Packets.LiveResult:
        """Class to represent the data groups results return from the Api"""
        ...

    @property.setter
    def results(self, value: QuantConnect.Packets.LiveResult) -> None:
        ...


class OrganizationResponse(QuantConnect.Api.RestResponse):
    """Response wrapper for Organizations/Read"""

    @property
    def organization(self) -> QuantConnect.Api.Organization:
        """Organization read from the response"""
        ...

    @property.setter
    def organization(self, value: QuantConnect.Api.Organization) -> None:
        ...


class Authentication(System.Object):
    """Helper methods for api authentication and interaction"""

    @staticmethod
    @overload
    def hash(timestamp: int) -> str:
        """
        Generate a secure hash for the authorization headers.
        
        :returns: Time based hash of user token and timestamp.
        """
        ...

    @staticmethod
    @overload
    def hash(timestamp: int, token: str) -> str:
        """
        Generate a secure hash for the authorization headers.
        
        :returns: Time based hash of user token and timestamp.
        """
        ...

    @staticmethod
    def link(endpoint: str, payload: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, System.Object]] = None) -> str:
        """
        Create an authenticated link for the target endpoint using the optional given payload
        
        :param endpoint: The endpoint
        :param payload: The payload
        :returns: The authenticated link to trigger the request.
        """
        ...

    @staticmethod
    def populate_query_string(query_string: System.Collections.Specialized.NameValueCollection, payload: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, System.Object]] = None) -> None:
        """Helper method to populate a query string with the given payload"""
        ...


class EstimateResponseWrapper(QuantConnect.Api.RestResponse):
    """
    Wrapper class for Optimizations/* endpoints JSON response
    Currently used by Optimizations/Estimate
    """

    @property
    def estimate(self) -> QuantConnect.Api.Estimate:
        """Estimate object"""
        ...

    @property.setter
    def estimate(self, value: QuantConnect.Api.Estimate) -> None:
        ...


class ParameterSetJsonConverter(JsonConverter):
    """Json converter for ParameterSet which creates a light weight easy to consume serialized version"""

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Writes a JSON object from a Parameter set"""
        ...


class LiveAlgorithmApiSettingsWrapper(System.Object):
    """Helper class to put BaseLiveAlgorithmSettings in proper format."""

    @property
    def version_id(self) -> str:
        """-1 is master"""
        ...

    @property.setter
    def version_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project id for the live instance"""
        ...

    @property
    def compile_id(self) -> str:
        """Compile Id for the live algorithm"""
        ...

    @property
    def node_id(self) -> str:
        """Id of the node being used to run live algorithm"""
        ...

    @property
    def signature(self) -> str:
        """Signature of the live algorithm"""
        ...

    @property
    def automatic_redeploy(self) -> bool:
        """
        True to enable Automatic Re-Deploy of the live algorithm,
        false otherwise
        """
        ...

    @property
    def brokerage(self) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """The API expects the settings as part of a brokerage object"""
        ...

    @property
    def data_providers(self) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Dictionary with the data providers and their corresponding credentials"""
        ...

    @property
    def parameters(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Dictionary with the parameters to be used in the live algorithm"""
        ...

    @property
    def notification(self) -> System.Collections.Generic.Dictionary[str, System.Collections.Generic.List[str]]:
        """Dictionary with the lists of events and targets"""
        ...

    def __init__(self, projectId: int, compileId: str, nodeId: str, settings: System.Collections.Generic.Dictionary[str, System.Object], version: str = "-1", dataProviders: System.Collections.Generic.Dictionary[str, System.Object] = None, parameters: System.Collections.Generic.Dictionary[str, str] = None, notification: System.Collections.Generic.Dictionary[str, System.Collections.Generic.List[str]] = None) -> None:
        """
        Constructor for LiveAlgorithmApiSettingsWrapper
        
        :param projectId: Id of project from QuantConnect
        :param compileId: Id of compilation of project from QuantConnect
        :param nodeId: Server type to run live Algorithm
        :param settings: Dictionary with brokerage specific settings. Each brokerage requires certain specific credentials                         in order to process the given orders. Each key in this dictionary represents a required field/credential                         to provide to the brokerage API and its value represents the value of that field. For example: "brokerageSettings: {                         "id": "Binance", "binance-api-secret": "123ABC", "binance-api-key": "ABC123"}. It is worth saying,                         that this dictionary must always contain an entry whose key is "id" and its value is the name of the brokerage                         (see Brokerages.BrokerageName)
        :param version: The version identifier
        :param dataProviders: Dictionary with data providers credentials. Each data provider requires certain credentials                         in order to retrieve data from their API. Each key in this dictionary describes a data provider name                         and its corresponding value is another dictionary with the required key-value pairs of credential                         names and values. For example: "dataProviders: {InteractiveBrokersBrokerage : { "id": 12345, "environement" : "paper",                         "username": "testUsername", "password": "testPassword"}}"
        :param parameters: Dictionary to specify the parameters for the live algorithm
        :param notification: Dictionary with the lists of events and targets
        """
        ...


class BacktestResponseWrapper(QuantConnect.Api.RestResponse):
    """
    Wrapper class for Backtest/* endpoints JSON response
    Currently used by Backtest/Read and Backtest/Create
    """

    @property
    def backtest(self) -> QuantConnect.Api.Backtest:
        """Backtest Object"""
        ...

    @property.setter
    def backtest(self, value: QuantConnect.Api.Backtest) -> None:
        ...

    @property
    def debugging(self) -> bool:
        """Indicates if the backtest is run under debugging mode"""
        ...

    @property.setter
    def debugging(self, value: bool) -> None:
        ...


class BacktestList(QuantConnect.Api.RestResponse):
    """Collection container for a list of backtests for a project"""

    @property
    def backtests(self) -> System.Collections.Generic.List[QuantConnect.Api.Backtest]:
        """Collection of summarized backtest objects"""
        ...

    @property.setter
    def backtests(self, value: System.Collections.Generic.List[QuantConnect.Api.Backtest]) -> None:
        ...


class BacktestTags(QuantConnect.Api.RestResponse):
    """Collection container for a list of backtest tags"""

    @property
    def tags(self) -> System.Collections.Generic.List[str]:
        """Collection of tags for a backtest"""
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.List[str]) -> None:
        ...


class OptimizationBacktestJsonConverter(JsonConverter):
    """Json converter for OptimizationBacktest which creates a light weight easy to consume serialized version"""

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


