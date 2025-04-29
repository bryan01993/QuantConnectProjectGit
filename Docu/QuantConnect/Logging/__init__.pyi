from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect.Logging
import System
import System.Collections.Concurrent

QuantConnect_Logging__EventContainer_Callable = typing.TypeVar("QuantConnect_Logging__EventContainer_Callable")
QuantConnect_Logging__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Logging__EventContainer_ReturnType")


class LogType(Enum):
    """Error level"""

    DEBUG = 0
    """Debug log level"""

    TRACE = 1
    """Trace log level"""

    ERROR = 2
    """Error log level"""


class LogEntry(System.Object):
    """Log entry wrapper to make logging simpler:"""

    @property
    def time(self) -> datetime.datetime:
        """Time of the log entry"""
        ...

    @property.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def message(self) -> str:
        """Message of the log entry"""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def message_type(self) -> QuantConnect.Logging.LogType:
        """Descriptor of the message type."""
        ...

    @property.setter
    def message_type(self, value: QuantConnect.Logging.LogType) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Create a default log message with the current time."""
        ...

    @overload
    def __init__(self, message: str, time: typing.Union[datetime.datetime, datetime.date], type: QuantConnect.Logging.LogType = ...) -> None:
        """
        Create a log entry at a specific time in the analysis (for a backtest).
        
        :param message: Message for log
        :param time: Utc time of the message
        :param type: Type of the log entry
        """
        ...

    def to_string(self) -> str:
        """Helper override on the log entry."""
        ...


class WhoCalledMe(System.Object):
    """Provides methods for determining higher stack frames"""

    @staticmethod
    def get_method_name(frame: int = 1) -> str:
        """
        Gets the method name of the caller
        
        :param frame: The number of stack frames to retrace from the caller's position
        :returns: The method name of the containing scope 'frame' stack frames above the caller.
        """
        ...


class ILogHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Interface for redirecting log output"""

    def debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class FileLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """Provides an implementation of ILogHandler that writes all log messages to a file on disk."""

    @overload
    def __init__(self, filepath: str, useTimestampPrefix: bool = True) -> None:
        """
        Initializes a new instance of the FileLogHandler class to write messages to the specified file path.
        The file will be opened using FileMode.Append
        
        :param filepath: The file path use to save the log messages
        :param useTimestampPrefix: True to prefix each line in the log which the UTC timestamp, false otherwise
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the FileLogHandler class using 'log.txt' for the filepath."""
        ...

    def create_message(self, text: str, level: str) -> str:
        """
        Creates the message to be logged
        
        This method is protected.
        
        :param text: The text to be logged
        :param level: The logging leel
        """
        ...

    def debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class Log(System.Object):
    """Logging management class."""

    log_handler: QuantConnect.Logging.ILogHandler
    """Gets or sets the ILogHandler instance used as the global logging implementation."""

    debugging_enabled: bool
    """Global flag whether to enable debugging logging:"""

    file_path: str
    """Global flag to specify file based log path"""

    debugging_level: int
    """Set the minimum message level:"""

    @staticmethod
    def clear_lean_paths(error: str) -> str:
        """
        Helper method to clear undesired paths from stack traces
        
        :param error: The error to cleanup
        :returns: The sanitized error.
        """
        ...

    @staticmethod
    def debug(text: str, level: int = 1) -> None:
        """
        Output to the console
        
        :param text: The message to show
        :param level: debug level
        """
        ...

    @staticmethod
    @overload
    def error(error: str, override_message_flood_protection: bool = False) -> None:
        """
        Log error
        
        :param error: String Error
        :param override_message_flood_protection: Force sending a message, overriding the "do not flood" directive
        """
        ...

    @staticmethod
    @overload
    def error(exception: System.Exception, message: str = None, override_message_flood_protection: bool = False) -> None:
        """
        Log error
        
        :param exception: The exception to be logged
        :param message: An optional message to be logged, if null/whitespace the messge text will be extracted
        :param override_message_flood_protection: Force sending a message, overriding the "do not flood" directive
        """
        ...

    @staticmethod
    @overload
    def error(format: str, *args: typing.Any) -> None:
        """Writes the message in red"""
        ...

    @staticmethod
    @overload
    def trace(trace_text: str, override_message_flood_protection: bool = False) -> None:
        """Log trace"""
        ...

    @staticmethod
    @overload
    def trace(format: str, *args: typing.Any) -> None:
        """Writes the message in normal text"""
        ...

    @staticmethod
    def var_dump(obj: typing.Any, recursion: int = 0) -> str:
        """C# Equivalent of Print_r in PHP:"""
        ...


class ConsoleLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """ILogHandler implementation that writes log output to console."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the QuantConnect.Logging.ConsoleLogHandler class."""
        ...

    @overload
    def __init__(self, dateFormat: str = ...) -> None:
        """
        Initializes a new instance of the QuantConnect.Logging.ConsoleLogHandler class.
        
        :param dateFormat: Specifies the date format to use when writing log messages to the console window
        """
        ...

    def debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class QueueLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """ILogHandler implementation that queues all logs and writes them when instructed."""

    @property
    def logs(self) -> System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Logging.LogEntry]:
        """Public access to the queue for log processing."""
        ...

    @property
    def log_event(self) -> _EventContainer[typing.Callable[[QuantConnect.Logging.LogEntry], None], None]:
        """Logging Event Handler"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the QueueLogHandler class."""
        ...

    def debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def log_event_raised(self, log: QuantConnect.Logging.LogEntry) -> None:
        """LOgging event delegate"""
        ...

    def on_log_event(self, log: QuantConnect.Logging.LogEntry) -> None:
        """
        Raise a log event safely
        
        This method is protected.
        """
        ...

    def trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class ConsoleErrorLogHandler(QuantConnect.Logging.ConsoleLogHandler):
    """Subclass of ConsoleLogHandler that only logs error messages"""

    def debug(self, text: str) -> None:
        """
        Hide debug messages from log
        
        :param text: The debug text to log
        """
        ...

    def trace(self, text: str) -> None:
        """
        Hide trace messages from log
        
        :param text: The trace text to log
        """
        ...


class RegressionFileLogHandler(QuantConnect.Logging.FileLogHandler):
    """
    Provides an implementation of ILogHandler that writes all log messages to a file on disk
    without timestamps.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the RegressionFileLogHandler class
        that will write to a 'regression.log' file in the executing directory
        """
        ...


class LogHandlerExtensions(System.Object):
    """Logging extensions."""

    @staticmethod
    def debug(log_handler: QuantConnect.Logging.ILogHandler, text: str, *args: typing.Any) -> None:
        """
        Write debug message to log
        
        :param text: Message
        :param args: Arguments to format.
        """
        ...

    @staticmethod
    def error(log_handler: QuantConnect.Logging.ILogHandler, text: str, *args: typing.Any) -> None:
        """
        Write error message to log
        
        :param text: Message
        :param args: Arguments to format.
        """
        ...

    @staticmethod
    def trace(log_handler: QuantConnect.Logging.ILogHandler, text: str, *args: typing.Any) -> None:
        """
        Write debug message to log
        
        :param text: Message
        :param args: Arguments to format.
        """
        ...


class CompositeLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """Provides an ILogHandler implementation that composes multiple handlers"""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the CompositeLogHandler that pipes log messages to the console and log.txt"""
        ...

    @overload
    def __init__(self, *handlers: QuantConnect.Logging.ILogHandler) -> None:
        """
        Initializes a new instance of the CompositeLogHandler class from the specified handlers
        
        :param handlers: The implementations to compose
        """
        ...

    def debug(self, text: str) -> None:
        """Write debug message to log"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def error(self, text: str) -> None:
        """Write error message to log"""
        ...

    def trace(self, text: str) -> None:
        """Write debug message to log"""
        ...


class FunctionalLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """ILogHandler implementation that writes log output to result handler"""

    @overload
    def __init__(self) -> None:
        """Default constructor to handle MEF."""
        ...

    @overload
    def __init__(self, debug: typing.Callable[[str], None], trace: typing.Callable[[str], None], error: typing.Callable[[str], None]) -> None:
        """Initializes a new instance of the QuantConnect.Logging.FunctionalLogHandler class."""
        ...

    def debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Logging__EventContainer_Callable, QuantConnect_Logging__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Logging__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Logging__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Logging__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


