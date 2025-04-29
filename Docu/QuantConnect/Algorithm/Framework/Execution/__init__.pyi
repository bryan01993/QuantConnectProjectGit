from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework
import QuantConnect.Algorithm.Framework.Execution
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Data.Consolidators
import QuantConnect.Data.UniverseSelection
import QuantConnect.Indicators
import QuantConnect.Securities
import System


class IExecutionModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges, metaclass=abc.ABCMeta):
    """Algorithm framework model that executes portfolio targets"""

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Submit orders for the specified portfolio targets.
        This model is free to delay or spread out these orders as it sees fit
        
        :param algorithm: The algorithm instance
        :param targets: The portfolio targets just emitted by the portfolio construction model. These are always just the new/updated targets and not a complete set of targets
        """
        ...


class ExecutionModel(System.Object, QuantConnect.Algorithm.Framework.Execution.IExecutionModel):
    """Provides a base class for execution models"""

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Submit orders for the specified portfolio targets.
        This model is free to delay or spread out these orders as it sees fit
        
        :param algorithm: The algorithm instance
        :param targets: The portfolio targets just emitted by the portfolio construction model. These are always just the new/updated targets and not a complete set of targets
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class SpreadExecutionModel(QuantConnect.Algorithm.Framework.Execution.ExecutionModel):
    """Execution model that submits orders while the current spread is in desirably tight extent."""

    def __init__(self, acceptingSpreadPercent: float = 0.005) -> None:
        """
        Initializes a new instance of the SpreadExecutionModel class
        
        :param acceptingSpreadPercent: Maximum spread accepted comparing to current price in percentage.
        """
        ...

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Submit orders for the specified portfolio targets if the spread is tighter/equal to preset level
        
        :param algorithm: The algorithm instance
        :param targets: The portfolio targets to be ordered
        """
        ...

    def price_is_favorable(self, security: QuantConnect.Securities.Security) -> bool:
        """
        Determines if the current spread is equal or tighter than preset level
        
        This method is protected.
        """
        ...


class VolumeWeightedAveragePriceExecutionModel(QuantConnect.Algorithm.Framework.Execution.ExecutionModel):
    """Execution model that submits orders while the current market price is more favorable that the current volume weighted average price."""

    class SymbolData(System.Object):
        """
        Symbol data for this Execution Model
        
        This class is protected.
        """

        @property
        def security(self) -> QuantConnect.Securities.Security:
            """Security"""
            ...

        @property
        def vwap(self) -> QuantConnect.Indicators.IntradayVwap:
            """VWAP Indicator"""
            ...

        @property
        def consolidator(self) -> QuantConnect.Data.Consolidators.IDataConsolidator:
            """Data Consolidator"""
            ...

        def __init__(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, security: QuantConnect.Securities.Security) -> None:
            """Initialize a new instance of SymbolData"""
            ...

    @property
    def maximum_order_quantity_percent_volume(self) -> float:
        """
        Gets or sets the maximum order quantity as a percentage of the current bar's volume.
        This defaults to 0.01m = 1%. For example, if the current bar's volume is 100, then
        the maximum order size would equal 1 share.
        """
        ...

    @property.setter
    def maximum_order_quantity_percent_volume(self, value: float) -> None:
        ...

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Submit orders for the specified portfolio targets.
        This model is free to delay or spread out these orders as it sees fit
        
        :param algorithm: The algorithm instance
        :param targets: The portfolio targets to be ordered
        """
        ...

    def is_safe_to_remove(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines if it's safe to remove the associated symbol data
        
        This method is protected.
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...

    def price_is_favorable(self, data: QuantConnect.Algorithm.Framework.Execution.VolumeWeightedAveragePriceExecutionModel.SymbolData, unordered_quantity: float) -> bool:
        """
        Determines if the current price is better than VWAP
        
        This method is protected.
        """
        ...


class StandardDeviationExecutionModel(QuantConnect.Algorithm.Framework.Execution.ExecutionModel):
    """
    Execution model that submits orders while the current market prices is at least the configured number of standard
    deviations away from the mean in the favorable direction (below/above for buy/sell respectively)
    """

    class SymbolData(System.Object):
        """
        Symbol Data for this Execution Model
        
        This class is protected.
        """

        @property
        def security(self) -> QuantConnect.Securities.Security:
            """Security"""
            ...

        @property
        def std(self) -> QuantConnect.Indicators.StandardDeviation:
            """Standard Deviation"""
            ...

        @property
        def sma(self) -> QuantConnect.Indicators.SimpleMovingAverage:
            """Simple Moving Average"""
            ...

        @property
        def consolidator(self) -> QuantConnect.Data.Consolidators.IDataConsolidator:
            """Data Consolidator"""
            ...

        def __init__(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, security: QuantConnect.Securities.Security, period: int, resolution: QuantConnect.Resolution) -> None:
            """
            Initialize an instance of SymbolData
            
            :param algorithm: Algorithm for this security
            :param security: The security we are using
            :param period: Period of the SMA and STD
            :param resolution: Resolution for this symbol
            """
            ...

    @property
    def maximum_order_value(self) -> float:
        """
        Gets or sets the maximum order value in units of the account currency.
        This defaults to $20,000. For example, if purchasing a stock with a price
        of $100, then the maximum order size would be 200 shares.
        """
        ...

    @property.setter
    def maximum_order_value(self, value: float) -> None:
        ...

    def __init__(self, period: int = 60, deviations: float = 2, resolution: QuantConnect.Resolution = ...) -> None:
        """
        Initializes a new instance of the StandardDeviationExecutionModel class
        
        :param period: Period of the standard deviation indicator
        :param deviations: The number of deviations away from the mean before submitting an order
        :param resolution: The resolution of the STD and SMA indicators
        """
        ...

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Executes market orders if the standard deviation of price is more than the configured number of deviations
        in the favorable direction.
        
        :param algorithm: The algorithm instance
        :param targets: The portfolio targets
        """
        ...

    def is_safe_to_remove(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines if it's safe to remove the associated symbol data
        
        This method is protected.
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...

    def price_is_favorable(self, data: QuantConnect.Algorithm.Framework.Execution.StandardDeviationExecutionModel.SymbolData, unordered_quantity: float) -> bool:
        """
        Determines if the current price is more than the configured number of standard deviations
        away from the mean in the favorable direction.
        
        This method is protected.
        """
        ...


class ImmediateExecutionModel(QuantConnect.Algorithm.Framework.Execution.ExecutionModel):
    """
    Provides an implementation of IExecutionModel that immediately submits
    market orders to achieve the desired portfolio targets
    """

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Immediately submits orders for the specified portfolio targets.
        
        :param algorithm: The algorithm instance
        :param targets: The portfolio targets to be ordered
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class NullExecutionModel(QuantConnect.Algorithm.Framework.Execution.ExecutionModel):
    """Provides an implementation of IExecutionModel that does nothing"""

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Execute the ExecutionModel
        
        :param algorithm: The Algorithm to execute this model on
        :param targets: The portfolio targets
        """
        ...


class ExecutionModelPythonWrapper(QuantConnect.Algorithm.Framework.Execution.ExecutionModel):
    """Provides an implementation of IExecutionModel that wraps a PyObject object"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the IExecutionModel class with wrapped PyObject object
        
        :param model: Model defining how to execute trades to reach a portfolio target
        """
        ...

    def execute(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> None:
        """
        Submit orders for the specified portfolio targets.
        This model is free to delay or spread out these orders as it sees fit
        
        :param algorithm: The algorithm instance
        :param targets: The portfolio targets to be ordered
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


