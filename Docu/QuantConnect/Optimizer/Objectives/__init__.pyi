from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect.Optimizer.Objectives
import QuantConnect.Util
import System

QuantConnect_Optimizer_Objectives__EventContainer_Callable = typing.TypeVar("QuantConnect_Optimizer_Objectives__EventContainer_Callable")
QuantConnect_Optimizer_Objectives__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Optimizer_Objectives__EventContainer_ReturnType")


class Extremum(System.Object):
    """
    Define the way to compare current real-values and the new one (candidates).
    It's encapsulated in different abstraction to allow configure the direction of optimization, i.e. max or min.
    """

    def __init__(self, comparer: typing.Callable[[float, float], bool]) -> None:
        """
        Create an instance of Extremum to compare values.
        
        :param comparer: The way old and new values should be compared
        """
        ...

    def better(self, current: float, candidate: float) -> bool:
        """
        Compares two values; identifies whether condition is met or not.
        
        :param current: Left operand
        :param candidate: Right operand
        :returns: Returns the result of comparer with this arguments.
        """
        ...


class Objective(System.Object, metaclass=abc.ABCMeta):
    """Base class for optimization Objectives.Target and Constraint"""

    @property
    def target(self) -> str:
        """Target; property of json file we want to track"""
        ...

    @property.setter
    def target(self, value: str) -> None:
        ...

    @property
    def target_value(self) -> typing.Optional[float]:
        """Target value"""
        ...

    @property.setter
    def target_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def old_target_value(self) -> typing.Optional[float]:
        ...

    @property.setter
    def old_target_value(self, value: typing.Optional[float]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Creates a new instance of Objective class
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, target: str, targetValue: typing.Optional[float]) -> None:
        """
        Creates a new instance
        
        This method is protected.
        """
        ...


class Constraint(QuantConnect.Optimizer.Objectives.Objective):
    """
    A backtest optimization constraint.
    Allows specifying statistical constraints for the optimization, eg. a backtest can't have a DrawDown less than 10%
    """

    @property
    def operator(self) -> QuantConnect.Util.ComparisonOperatorTypes:
        """The target comparison operation, eg. 'Greater'"""
        ...

    @property.setter
    def operator(self, value: QuantConnect.Util.ComparisonOperatorTypes) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Empty Constraint constructor"""
        ...

    @overload
    def __init__(self, target: str, operator: QuantConnect.Util.ComparisonOperatorTypes, targetValue: typing.Optional[float]) -> None:
        """Creates a new instance"""
        ...

    def is_met(self, json_backtest_result: str) -> bool:
        """Asserts the constraint is met"""
        ...

    def to_string(self) -> str:
        """Pretty representation of a constraint"""
        ...


class Minimization(QuantConnect.Optimizer.Objectives.Extremum):
    """Defines standard minimization strategy, i.e. right operand is less than left"""

    def __init__(self) -> None:
        """Creates an instance of Minimization"""
        ...


class Target(QuantConnect.Optimizer.Objectives.Objective):
    """The optimization statistical target"""

    @property
    def extremum(self) -> QuantConnect.Optimizer.Objectives.Extremum:
        """Defines the direction of optimization, i.e. maximization or minimization"""
        ...

    @property.setter
    def extremum(self, value: QuantConnect.Optimizer.Objectives.Extremum) -> None:
        ...

    @property
    def current(self) -> typing.Optional[float]:
        """Current value"""
        ...

    @property
    def reached(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Fires when target complies specified value"""
        ...

    @overload
    def __init__(self, target: str, extremum: QuantConnect.Optimizer.Objectives.Extremum, targetValue: typing.Optional[float]) -> None:
        """Creates a new instance"""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    def check_compliance(self) -> None:
        """Try comply target value"""
        ...

    @staticmethod
    def get_token_in_json_backtest(json_backtest_result: str, target: str) -> typing.Any:
        ...

    def move_ahead(self, json_backtest_result: str) -> bool:
        """
        Check backtest result
        
        :param json_backtest_result: Backtest result json
        :returns: true if found a better solution; otherwise false.
        """
        ...

    def to_string(self) -> str:
        """Pretty representation of this optimization target"""
        ...


class ExtremumJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[QuantConnect.Optimizer.Objectives.Extremum, str]):
    """Class for converting string values to Maximization or Minimization strategy objects"""

    @property
    def populate_properties(self) -> bool:
        """
        Don't populate any property
        
        This property is protected.
        """
        ...

    @overload
    def convert(self, value: QuantConnect.Optimizer.Objectives.Extremum) -> str:
        """
        Converts a Extremum object into a string
        
        This method is protected.
        """
        ...

    @overload
    def convert(self, value: str) -> QuantConnect.Optimizer.Objectives.Extremum:
        """
        Converts a string into its corresponding Extremum object
        
        This method is protected.
        """
        ...


class Maximization(QuantConnect.Optimizer.Objectives.Extremum):
    """Defines standard maximization strategy, i.e. right operand is greater than left"""

    def __init__(self) -> None:
        """Creates an instance of Maximization"""
        ...


class _EventContainer(typing.Generic[QuantConnect_Optimizer_Objectives__EventContainer_Callable, QuantConnect_Optimizer_Objectives__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Optimizer_Objectives__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Optimizer_Objectives__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Optimizer_Objectives__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


