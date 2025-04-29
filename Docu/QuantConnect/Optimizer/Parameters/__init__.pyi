from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect.Optimizer.Parameters
import System
import System.Collections.Generic

JsonConverter = typing.Any

QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T = typing.TypeVar("QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T")


class OptimizationParameterEnumerator(typing.Generic[QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T], System.Object, metaclass=abc.ABCMeta):
    """Enumerates all possible values for specific optimization parameter"""

    @property
    def optimization_parameter(self) -> QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T:
        """
        The target optimization parameter to enumerate
        
        This property is protected.
        """
        ...

    @property
    def index(self) -> int:
        """
        The current enumeration state
        
        This property is protected.
        """
        ...

    @property.setter
    def index(self, value: int) -> None:
        ...

    @property
    @abc.abstractmethod
    def current(self) -> str:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, optimizationParameter: QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T) -> None:
        """This method is protected."""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def move_next(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class OptimizationParameter(System.Object, metaclass=abc.ABCMeta):
    """Defines the optimization parameter meta information"""

    @property
    def name(self) -> str:
        """Name of optimization parameter"""
        ...

    def __init__(self, name: str) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        This method is protected.
        
        :param name: parameter name
        """
        ...

    @overload
    def equals(self, other: QuantConnect.Optimizer.Parameters.OptimizationParameter) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...


class OptimizationStepParameter(QuantConnect.Optimizer.Parameters.OptimizationParameter):
    """Defines the step based optimization parameter"""

    @property
    def min_value(self) -> float:
        """Minimum value of optimization parameter, applicable for boundary conditions"""
        ...

    @property
    def max_value(self) -> float:
        """Maximum value of optimization parameter, applicable for boundary conditions"""
        ...

    @property
    def step(self) -> typing.Optional[float]:
        """Movement, should be positive"""
        ...

    @property.setter
    def step(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def min_step(self) -> typing.Optional[float]:
        ...

    @property.setter
    def min_step(self, value: typing.Optional[float]) -> None:
        ...

    @overload
    def __init__(self, name: str, min: float, max: float) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        :param name: parameter name
        :param min: minimal value
        :param max: maximal value
        """
        ...

    @overload
    def __init__(self, name: str, min: float, max: float, step: float) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        :param name: parameter name
        :param min: minimal value
        :param max: maximal value
        :param step: movement
        """
        ...

    @overload
    def __init__(self, name: str, min: float, max: float, step: float, minStep: float) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        :param name: parameter name
        :param min: minimal value
        :param max: maximal value
        :param step: movement
        :param minStep: minimal possible movement
        """
        ...


class OptimizationStepParameterEnumerator(QuantConnect.Optimizer.Parameters.OptimizationParameterEnumerator[QuantConnect.Optimizer.Parameters.OptimizationStepParameter]):
    """Enumerates all possible values for specific optimization parameter"""

    @property
    def current(self) -> str:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, optimizationParameter: QuantConnect.Optimizer.Parameters.OptimizationStepParameter) -> None:
        """
        Creates an instance of OptimizationStepParameterEnumerator
        
        :param optimizationParameter: Step-based optimization parameter
        """
        ...

    def move_next(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...


class OptimizationParameterJsonConverter(JsonConverter):
    """
    Override OptimizationParameter deserialization method.
    Can handle OptimizationStepParameter instances
    """

    def can_convert(self, object_type: typing.Type) -> bool:
        """Determines if an OptimizationParameter is assignable from the given object type"""
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """Creates a Optimization Parameter object from a JSON object"""
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Writes a JSON object from a OptimizationParameter object"""
        ...


class ParameterSet(System.Object):
    """Represents a single combination of optimization parameters"""

    @property
    def id(self) -> int:
        """The unique identifier within scope (current optimization job)"""
        ...

    @property
    def value(self) -> System.Collections.Generic.IReadOnlyDictionary[str, str]:
        """Represent a combination as key value of parameters, i.e. order doesn't matter"""
        ...

    def __init__(self, id: int, value: System.Collections.Generic.IReadOnlyDictionary[str, str]) -> None:
        """
        Creates an instance of ParameterSet based on new combination of optimization parameters
        
        :param id: Unique identifier
        :param value: Combination of optimization parameters
        """
        ...

    def to_string(self) -> str:
        """String representation of this parameter set"""
        ...


class StaticOptimizationParameter(QuantConnect.Optimizer.Parameters.OptimizationParameter):
    """Defines the step based optimization parameter"""

    @property
    def value(self) -> str:
        """Minimum value of optimization parameter, applicable for boundary conditions"""
        ...

    def __init__(self, name: str, value: str) -> None:
        """
        Creates a new instance
        
        :param name: The name of the parameter
        :param value: The fixed value of this parameter
        """
        ...


