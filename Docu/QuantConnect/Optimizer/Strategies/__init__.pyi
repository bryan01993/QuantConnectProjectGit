from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect.Optimizer
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Optimizer.Strategies
import System
import System.Collections.Generic

QuantConnect_Optimizer_Strategies__EventContainer_Callable = typing.TypeVar("QuantConnect_Optimizer_Strategies__EventContainer_Callable")
QuantConnect_Optimizer_Strategies__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Optimizer_Strategies__EventContainer_ReturnType")


class OptimizationStrategySettings(System.Object):
    """Defines the specific optimization strategy settings"""

    @property
    def max_runtime(self) -> datetime.timedelta:
        """TODO: implement"""
        ...

    @property.setter
    def max_runtime(self, value: datetime.timedelta) -> None:
        ...


class IOptimizationStrategy(metaclass=abc.ABCMeta):
    """Defines the optimization settings, direction, solution and exit, i.e. optimization strategy"""

    @property
    @abc.abstractmethod
    def new_parameter_set(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.Parameters.ParameterSet], None], None]:
        """Fires when new parameter set is retrieved"""
        ...

    @property
    @abc.abstractmethod
    def solution(self) -> QuantConnect.Optimizer.OptimizationResult:
        """Best found solution, its value and parameter set"""
        ...

    def get_total_backtest_estimate(self) -> int:
        """Estimates amount of parameter sets that can be run"""
        ...

    def initialize(self, target: QuantConnect.Optimizer.Objectives.Target, constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], settings: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings) -> None:
        """
        Initializes the strategy using generator, extremum settings and optimization parameters
        
        :param target: The optimization target
        :param constraints: The optimization constraints to apply on backtest results
        :param parameters: optimization parameters
        :param settings: optimization strategy advanced settings
        """
        ...

    def push_new_results(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Callback when lean compute job completed.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...


class StepBaseOptimizationStrategy(System.Object, QuantConnect.Optimizer.Strategies.IOptimizationStrategy, typing.Iterable[str], metaclass=abc.ABCMeta):
    """Base class for any optimization built on top of brute force optimization method"""

    @property
    def initialized(self) -> bool:
        """
        Indicates was strategy initialized or no
        
        This property is protected.
        """
        ...

    @property.setter
    def initialized(self, value: bool) -> None:
        ...

    @property
    def optimization_parameters(self) -> System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]:
        """
        Optimization parameters
        
        This property is protected.
        """
        ...

    @property.setter
    def optimization_parameters(self, value: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]) -> None:
        ...

    @property
    def target(self) -> QuantConnect.Optimizer.Objectives.Target:
        """
        Optimization target, i.e. maximize or minimize
        
        This property is protected.
        """
        ...

    @property.setter
    def target(self, value: QuantConnect.Optimizer.Objectives.Target) -> None:
        ...

    @property
    def constraints(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Optimizer.Objectives.Constraint]:
        """
        Optimization constraints; if it doesn't comply just drop the backtest
        
        This property is protected.
        """
        ...

    @property.setter
    def constraints(self, value: System.Collections.Generic.IEnumerable[QuantConnect.Optimizer.Objectives.Constraint]) -> None:
        ...

    @property
    def solution(self) -> QuantConnect.Optimizer.OptimizationResult:
        """Keep the best found solution - lean computed job result and corresponding  parameter set"""
        ...

    @property
    def settings(self) -> QuantConnect.Optimizer.Strategies.OptimizationStrategySettings:
        """Advanced strategy settings"""
        ...

    @property
    def new_parameter_set(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.Parameters.ParameterSet], None], None]:
        """Fires when new parameter set is generated"""
        ...

    def get_total_backtest_estimate(self) -> int:
        """
        Calculate number of parameter sets within grid
        
        :returns: Number of parameter sets for given optimization parameters.
        """
        ...

    def initialize(self, target: QuantConnect.Optimizer.Objectives.Target, constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], settings: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings) -> None:
        """
        Initializes the strategy using generator, extremum settings and optimization parameters
        
        :param target: The optimization target
        :param constraints: The optimization constraints to apply on backtest results
        :param parameters: Optimization parameters
        :param settings: Optimization strategy settings
        """
        ...

    def on_new_parameter_set(self, parameter_set: QuantConnect.Optimizer.Parameters.ParameterSet) -> None:
        """
        Handles new parameter set
        
        This method is protected.
        
        :param parameter_set: New parameter set
        """
        ...

    def process_new_result(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """This method is protected."""
        ...

    def push_new_results(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Checks whether new lean compute job better than previous and run new iteration if necessary.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...

    def step(self, args: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]) -> System.Collections.Generic.IEnumerable[QuantConnect.Optimizer.Parameters.ParameterSet]:
        """
        Enumerate all possible arrangements
        
        This method is protected.
        
        :returns: Collection of possible combinations for given optimization parameters settings.
        """
        ...


class EulerSearchOptimizationStrategy(QuantConnect.Optimizer.Strategies.StepBaseOptimizationStrategy):
    """Advanced brute-force strategy with search in-depth for best solution on previous step"""

    def initialize(self, target: QuantConnect.Optimizer.Objectives.Target, constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], settings: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings) -> None:
        """
        Initializes the strategy using generator, extremum settings and optimization parameters
        
        :param target: The optimization target
        :param constraints: The optimization constraints to apply on backtest results
        :param parameters: Optimization parameters
        :param settings: Optimization strategy settings
        """
        ...

    def on_new_parameter_set(self, parameter_set: QuantConnect.Optimizer.Parameters.ParameterSet) -> None:
        """
        Handles new parameter set
        
        This method is protected.
        
        :param parameter_set: New parameter set
        """
        ...

    def push_new_results(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Checks whether new lean compute job better than previous and run new iteration if necessary.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...


class StepBaseOptimizationStrategySettings(QuantConnect.Optimizer.Strategies.OptimizationStrategySettings):
    """Defines the specific optimization strategy settings"""

    @property
    def default_segment_amount(self) -> int:
        """Defines the default number of segments for the next step"""
        ...

    @property.setter
    def default_segment_amount(self, value: int) -> None:
        ...


class GridSearchOptimizationStrategy(QuantConnect.Optimizer.Strategies.StepBaseOptimizationStrategy):
    """Find the best solution in first generation"""

    def push_new_results(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Checks whether new lean compute job better than previous and run new iteration if necessary.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Optimizer_Strategies__EventContainer_Callable, QuantConnect_Optimizer_Strategies__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Optimizer_Strategies__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Optimizer_Strategies__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Optimizer_Strategies__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


