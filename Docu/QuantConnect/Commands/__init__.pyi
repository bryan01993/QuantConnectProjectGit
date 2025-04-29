from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect
import QuantConnect.Commands
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Packets
import System
import System.Collections.Generic
import System.IO

DynamicObject = typing.Any


class CommandResultPacket(QuantConnect.Packets.Packet):
    """Contains data held as the result of executing a command"""

    @property
    def command_name(self) -> str:
        """Gets or sets the command that produced this packet"""
        ...

    @property.setter
    def command_name(self, value: str) -> None:
        ...

    @property
    def success(self) -> typing.Optional[bool]:
        """Gets or sets whether or not the"""
        ...

    @property.setter
    def success(self, value: typing.Optional[bool]) -> None:
        ...

    def __init__(self, command: QuantConnect.Commands.ICommand, success: typing.Optional[bool]) -> None:
        """Initializes a new instance of the CommandResultPacket class"""
        ...


class ICommandHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Represents a command queue for the algorithm. This is an entry point
    for external messages to act upon the running algorithm instance.
    """

    def initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Initializes this command queue for the specified job
        
        :param job: The job that defines what queue to bind to
        :param algorithm: The algorithm instance
        """
        ...

    def process_commands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.CommandResultPacket]:
        """
        Process any commands in the queue
        
        :returns: The command result packet of each command executed if any.
        """
        ...


class ICommand(metaclass=abc.ABCMeta):
    """Represents a command that can be run against a single algorithm"""

    @property
    @abc.abstractmethod
    def id(self) -> str:
        """Unique command id"""
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class BaseCommandHandler(System.Object, QuantConnect.Commands.ICommandHandler, metaclass=abc.ABCMeta):
    """Base algorithm command handler"""

    SETTINGS: typing.Any = ...
    """
    Command json settings
    
    This field is protected.
    """

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

    def acknowledge(self, command: QuantConnect.Commands.ICommand, command_result_packet: QuantConnect.Commands.CommandResultPacket) -> None:
        """
        Acknowledge a command that has been executed
        
        This method is protected.
        
        :param command: The command that was executed
        :param command_result_packet: The result
        """
        ...

    def dispose(self) -> None:
        """Disposes of this instance"""
        ...

    def get_commands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.ICommand]:
        """
        Get the commands to run
        
        This method is protected.
        """
        ...

    def initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Initializes this command queue for the specified job
        
        :param job: The job that defines what queue to bind to
        :param algorithm: The algorithm instance
        """
        ...

    def process_commands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.CommandResultPacket]:
        """Will consumer and execute any command in the queue"""
        ...

    def try_get_callback_command(self, payload: str) -> QuantConnect.Commands.ICommand:
        """
        Helper method to create a callback command
        
        This method is protected.
        """
        ...


class FileCommandHandler(QuantConnect.Commands.BaseCommandHandler):
    """Represents a command handler that sources it's commands from a file on the local disk"""

    def __init__(self) -> None:
        """
        Initializes a new instance of the FileCommandHandler class
        using the 'command-json-file' configuration value for the command json file
        """
        ...

    def acknowledge(self, command: QuantConnect.Commands.ICommand, command_result_packet: QuantConnect.Commands.CommandResultPacket) -> None:
        """
        Acknowledge a command that has been executed
        
        This method is protected.
        
        :param command: The command that was executed
        :param command_result_packet: The result
        """
        ...

    @staticmethod
    def get_command_files() -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        """
        Gets all the available command files
        
        :returns: Sorted enumerator of all the available command files.
        """
        ...

    def get_commands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.ICommand]:
        """
        Gets the next command in the queue
        
        This method is protected.
        
        :returns: The next command in the queue, if present, null if no commands present.
        """
        ...


class BaseCommand(System.Object, QuantConnect.Commands.ICommand, metaclass=abc.ABCMeta):
    """Base command implementation"""

    @property
    def id(self) -> str:
        """Unique command id"""
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    def get_symbol(self, ticker: str, security_type: QuantConnect.SecurityType, market: str, symbol: typing.Union[QuantConnect.Symbol, str] = None) -> QuantConnect.Symbol:
        """
        Creats symbol using symbol properties.
        
        This method is protected.
        
        :param ticker: The string ticker symbol
        :param security_type: The security type of the ticker. If security_type == Option, then a canonical symbol is created
        :param market: The market the ticker resides in
        :param symbol: The algorithm to run this command against
        """
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class LiquidateCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command that will liquidate the entire algorithm"""

    @property
    def ticker(self) -> str:
        """Gets or sets the string ticker symbol"""
        ...

    @property.setter
    def ticker(self, value: str) -> None:
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets or sets the security type of the ticker."""
        ...

    @property.setter
    def security_type(self, value: QuantConnect.SecurityType) -> None:
        ...

    @property
    def market(self) -> str:
        """Gets or sets the market the ticker resides in"""
        ...

    @property.setter
    def market(self, value: str) -> None:
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Submits orders to liquidate all current holdings in the algorithm
        
        :param algorithm: The algorithm to be liquidated
        """
        ...


class CancelOrderCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to cancel a specific order by id"""

    class Result(QuantConnect.Commands.CommandResultPacket):
        """Result packet type for the CancelOrderCommand command"""

        @property
        def quantity_filled(self) -> float:
            """Gets or sets the quantity filled on the cancelled order"""
            ...

        @property.setter
        def quantity_filled(self, value: float) -> None:
            ...

        def __init__(self, command: QuantConnect.Commands.ICommand, success: bool, quantityFilled: float) -> None:
            """Initializes a new instance of the Result class"""
            ...

    @property
    def order_id(self) -> int:
        """Gets or sets the order id to be cancelled"""
        ...

    @property.setter
    def order_id(self, value: int) -> None:
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class AlgorithmStatusCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command that will change the algorithm's status"""

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Gets or sets the algorithm status"""
        ...

    @property.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AlgorithmStatusCommand"""
        ...

    @overload
    def __init__(self, status: QuantConnect.AlgorithmStatus) -> None:
        """
        Initializes a new instance of the AlgorithmStatusCommand with
        the specified status
        """
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Sets the algorithm's status to Status
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class AddSecurityCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to add a security to the algorithm"""

    class Result(QuantConnect.Commands.CommandResultPacket):
        """Result packet type for the AddSecurityCommand command"""

        @property
        def symbol(self) -> QuantConnect.Symbol:
            """The symbol result from the add security command"""
            ...

        @property.setter
        def symbol(self, value: QuantConnect.Symbol) -> None:
            ...

        def __init__(self, command: QuantConnect.Commands.AddSecurityCommand, success: bool, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
            """Initializes a new instance of the Result class"""
            ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """The security type of the security"""
        ...

    @property.setter
    def security_type(self, value: QuantConnect.SecurityType) -> None:
        ...

    @property
    def symbol(self) -> str:
        """The security's ticker symbol"""
        ...

    @property.setter
    def symbol(self, value: str) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """The requested resolution, defaults to Resolution.Minute"""
        ...

    @property.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def market(self) -> str:
        """The security's market, defaults to QuantConnect.Market.USA except for Forex, defaults to QuantConnect.Market.FXCM"""
        ...

    @property.setter
    def market(self, value: str) -> None:
        ...

    @property
    def fill_data_forward(self) -> bool:
        """The fill forward behavior, true to fill forward, false otherwise - defaults to true"""
        ...

    @property.setter
    def fill_data_forward(self, value: bool) -> None:
        ...

    @property
    def leverage(self) -> float:
        """The leverage for the security, defaults to 2 for equity, 50 for forex, and 1 for everything else"""
        ...

    @property.setter
    def leverage(self, value: float) -> None:
        ...

    @property
    def extended_market_hours(self) -> bool:
        """The extended market hours flag, true to allow pre/post market data, false for only in market data"""
        ...

    @property.setter
    def extended_market_hours(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        """Default construct that applies default values"""
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class Command(DynamicObject):
    """Base generic dynamic command class"""

    @property
    def payload_data(self) -> str:
        """
        Useful to string representation in python
        
        This property is protected.
        """
        ...

    @property.setter
    def payload_data(self, value: str) -> None:
        ...

    def get_meta_object(self, parameter: typing.Any) -> typing.Any:
        """Get the metaObject required for Dynamism."""
        ...

    def get_property(self, name: str) -> System.Object:
        """
        Gets the property's value with the specified name. This is a case-insensitve search.
        
        :param name: The property name to access
        :returns: object value of BaseData.
        """
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> typing.Optional[bool]:
        """
        Run this command using the target algorithm
        
        :param algorithm: The algorithm instance
        :returns: True if success, false otherwise. Returning null will disable command feedback.
        """
        ...

    def set_property(self, name: str, value: typing.Any) -> System.Object:
        """
        Sets the property with the specified name to the value. This is a case-insensitve search.
        
        :param name: The property name to set
        :param value: The new property value
        :returns: Returns the input value back to the caller.
        """
        ...

    def to_string(self) -> str:
        """The string representation of this command"""
        ...


class QuitCommand(QuantConnect.Commands.AlgorithmStatusCommand):
    """Represents a command that will terminate the algorithm"""

    def __init__(self) -> None:
        """Initializes a new instance of the QuitCommand"""
        ...


class CallbackCommand(QuantConnect.Commands.BaseCommand):
    """Algorithm callback command type"""

    @property
    def type(self) -> str:
        """The target command type to run, if empty or null will be the generic untyped command handler"""
        ...

    @property.setter
    def type(self, value: str) -> None:
        ...

    @property
    def payload(self) -> str:
        """The command payload"""
        ...

    @property.setter
    def payload(self, value: str) -> None:
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...

    def to_string(self) -> str:
        """The command string representation"""
        ...


class OrderCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to submit an order to the algorithm"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets or sets the symbol to be ordered"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def ticker(self) -> str:
        """Gets or sets the string ticker symbol"""
        ...

    @property.setter
    def ticker(self, value: str) -> None:
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets or sets the security type of the ticker."""
        ...

    @property.setter
    def security_type(self, value: QuantConnect.SecurityType) -> None:
        ...

    @property
    def market(self) -> str:
        """Gets or sets the market the ticker resides in"""
        ...

    @property.setter
    def market(self, value: str) -> None:
        ...

    @property
    def order_type(self) -> QuantConnect.Orders.OrderType:
        """Gets or sets the order type to be submted"""
        ...

    @property.setter
    def order_type(self, value: QuantConnect.Orders.OrderType) -> None:
        ...

    @property
    def quantity(self) -> float:
        """Gets or sets the number of units to be ordered (directional)"""
        ...

    @property.setter
    def quantity(self, value: float) -> None:
        ...

    @property
    def limit_price(self) -> float:
        """Gets or sets the limit price. Only applies to QuantConnect.Orders.OrderType.Limit and QuantConnect.Orders.OrderType.StopLimit"""
        ...

    @property.setter
    def limit_price(self, value: float) -> None:
        ...

    @property
    def stop_price(self) -> float:
        """Gets or sets the stop price. Only applies to QuantConnect.Orders.OrderType.StopLimit and QuantConnect.Orders.OrderType.StopMarket"""
        ...

    @property.setter
    def stop_price(self, value: float) -> None:
        ...

    @property
    def tag(self) -> str:
        """Gets or sets an arbitrary tag to be attached to the order"""
        ...

    @property.setter
    def tag(self, value: str) -> None:
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class UpdateOrderCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to update an order by id"""

    @property
    def order_id(self) -> int:
        """Gets or sets the id of the order to update"""
        ...

    @property.setter
    def order_id(self, value: int) -> None:
        ...

    @property
    def quantity(self) -> typing.Optional[float]:
        """Gets or sets the new quantity, specify null to not update the quantity"""
        ...

    @property.setter
    def quantity(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def limit_price(self) -> typing.Optional[float]:
        """
        Gets or sets the new limit price, specify null to not update the limit price.
        This will only be used if the order has a limit price (Limit/StopLimit orders)
        """
        ...

    @property.setter
    def limit_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def stop_price(self) -> typing.Optional[float]:
        """
        Gets or sets the new stop price, specify null to not update the stop price.
        This will onky be used if the order has a stop price (StopLimit/StopMarket orders)
        """
        ...

    @property.setter
    def stop_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def tag(self) -> str:
        """Gets or sets the new tag for the order, specify null to not update the tag"""
        ...

    @property.setter
    def tag(self, value: str) -> None:
        ...

    def run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


