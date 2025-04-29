from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect.Orders
import QuantConnect.Orders.OptionExercise
import QuantConnect.Python
import QuantConnect.Securities.Option
import System
import System.Collections.Generic


class IOptionExerciseModel(metaclass=abc.ABCMeta):
    """Represents a model that simulates option exercise and lapse events"""

    def option_exercise(self, option: QuantConnect.Securities.Option.Option, order: QuantConnect.Orders.OptionExerciseOrder) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderEvent]:
        """
        Model the option exercise
        
        :param option: Option we're trading this order
        :param order: Order to update
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...


class DefaultExerciseModel(System.Object, QuantConnect.Orders.OptionExercise.IOptionExerciseModel):
    """Represents the default option exercise model (physical, cash settlement)"""

    def option_exercise(self, option: QuantConnect.Securities.Option.Option, order: QuantConnect.Orders.OptionExerciseOrder) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderEvent]:
        """
        Default option exercise model for the basic equity/index option security class.
        
        :param option: Option we're trading this order
        :param order: Order to update
        """
        ...


class OptionExerciseModelPythonWrapper(QuantConnect.Python.BasePythonWrapper[QuantConnect.Orders.OptionExercise.IOptionExerciseModel], QuantConnect.Orders.OptionExercise.IOptionExerciseModel):
    """Python wrapper for custom option exercise models"""

    def __init__(self, model: typing.Any) -> None:
        """
        Creates a new instance
        
        :param model: The python model to wrapp
        """
        ...

    def option_exercise(self, option: QuantConnect.Securities.Option.Option, order: QuantConnect.Orders.OptionExerciseOrder) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderEvent]:
        """
        Performs option exercise for the option security class.
        
        :param option: Option we're trading this order
        :param order: Order to update
        """
        ...


