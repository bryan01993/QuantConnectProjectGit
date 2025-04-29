from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Indicators
import System
import System.Collections.Generic
import System.Reflection

PyObject = typing.Any
QuantConnect_Indicators_IndicatorBase = typing.Any
QuantConnect_Indicators_IndicatorDataPoint = typing.Any
QuantConnect_Indicators_IIndicator = typing.Any

QuantConnect_Indicators_IndicatorExtensions_Of_T = typing.TypeVar("QuantConnect_Indicators_IndicatorExtensions_Of_T")
QuantConnect_Indicators_IndicatorExtensions_WeightedBy_TWeight = typing.TypeVar("QuantConnect_Indicators_IndicatorExtensions_WeightedBy_TWeight")
QuantConnect_Indicators_IndicatorExtensions_WeightedBy_T = typing.TypeVar("QuantConnect_Indicators_IndicatorExtensions_WeightedBy_T")
QuantConnect_Indicators_IndicatorExtensions_EMA_T = typing.TypeVar("QuantConnect_Indicators_IndicatorExtensions_EMA_T")
QuantConnect_Indicators_IndicatorExtensions_MIN_T = typing.TypeVar("QuantConnect_Indicators_IndicatorExtensions_MIN_T")
QuantConnect_Indicators_IndicatorExtensions_SMA_T = typing.TypeVar("QuantConnect_Indicators_IndicatorExtensions_SMA_T")
QuantConnect_Indicators_ConstantIndicator_T = typing.TypeVar("QuantConnect_Indicators_ConstantIndicator_T")
QuantConnect_Indicators_WindowIndicator_T = typing.TypeVar("QuantConnect_Indicators_WindowIndicator_T")
QuantConnect_Indicators_IndicatorBase_T = typing.TypeVar("QuantConnect_Indicators_IndicatorBase_T")
QuantConnect_Indicators_DualSymbolIndicator_TInput = typing.TypeVar("QuantConnect_Indicators_DualSymbolIndicator_TInput")
QuantConnect_Indicators_MultiSymbolIndicator_TInput = typing.TypeVar("QuantConnect_Indicators_MultiSymbolIndicator_TInput")
QuantConnect_Indicators_FunctionalIndicator_T = typing.TypeVar("QuantConnect_Indicators_FunctionalIndicator_T")
QuantConnect_Indicators_RollingWindow_T = typing.TypeVar("QuantConnect_Indicators_RollingWindow_T")
QuantConnect_Indicators_IReadOnlyWindow_T = typing.TypeVar("QuantConnect_Indicators_IReadOnlyWindow_T")
QuantConnect_Indicators_IIndicator_T = typing.TypeVar("QuantConnect_Indicators_IIndicator_T")
QuantConnect_Indicators__EventContainer_Callable = typing.TypeVar("QuantConnect_Indicators__EventContainer_Callable")
QuantConnect_Indicators__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Indicators__EventContainer_ReturnType")


class IndicatorDataPoint(QuantConnect.Data.BaseData, System.IEquatable[QuantConnect_Indicators_IndicatorDataPoint], System.IComparable[QuantConnect_Indicators_IndicatorDataPoint]):
    """Represents a piece of data at a specific time"""

    @overload
    def __init__(self) -> None:
        """
        Initializes a new default instance of IndicatorDataPoint with a time of
        DateTime.MinValue and a Value of 0m.
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], value: float) -> None:
        """
        Initializes a new instance of the DataPoint type using the specified time/data
        
        :param time: The time this data was produced
        :param value: The data
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], value: float) -> None:
        """
        Initializes a new instance of the DataPoint type using the specified time/data
        
        :param symbol: The symbol associated with this data
        :param time: The time this data was produced
        :param value: The data
        """
        ...

    @overload
    def compare_to(self, other: QuantConnect.Indicators.IndicatorDataPoint) -> int:
        """
        Compares the current object with another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: A value that indicates the relative order of the objects being compared. The return value has the following meanings: Value Meaning Less than zero This object is less than the  parameter.Zero This object is equal to . Greater than zero This object is greater than .
        """
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        """
        Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
        
        :param obj: An object to compare with this instance.
        :returns: A value that indicates the relative order of the objects being compared. The return value has these meanings: Value Meaning Less than zero This instance precedes  in the sort order. Zero This instance occurs in the same position in the sort order as . Greater than zero This instance follows  in the sort order.
        """
        ...

    @overload
    def equals(self, other: QuantConnect.Indicators.IndicatorDataPoint) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Indicates whether this instance and a specified object are equal.
        
        :param obj: Another object to compare to.
        :returns: true if  and this instance are the same type and represent the same value; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer that is the hash code for this instance.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """This function is purposefully not implemented."""
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """This function is purposefully not implemented."""
        ...

    def to_string(self) -> str:
        """
        Returns a string representation of this DataPoint instance using ISO8601 formatting for the date
        
        :returns: A System.String containing a fully qualified type name.
        """
        ...


class IReadOnlyWindow(typing.Generic[QuantConnect_Indicators_IReadOnlyWindow_T], metaclass=abc.ABCMeta):
    """Interface type used to pass windows around without worry of external modification"""

    @property
    @abc.abstractmethod
    def size(self) -> int:
        """Gets the size of this window"""
        ...

    @property
    @abc.abstractmethod
    def count(self) -> int:
        """Gets the current number of elements in this window"""
        ...

    @property
    @abc.abstractmethod
    def samples(self) -> int:
        """Gets the number of samples that have been added to this window over its lifetime"""
        ...

    @property
    @abc.abstractmethod
    def is_ready(self) -> bool:
        """
        Gets a value indicating whether or not this window is ready, i.e,
            it has been filled to its capacity, this is when the Size==Count
        """
        ...

    @property
    @abc.abstractmethod
    def most_recently_removed(self) -> QuantConnect_Indicators_IReadOnlyWindow_T:
        """
        Gets the most recently removed item from the window. This is the
            piece of data that just 'fell off' as a result of the most recent
            add. If no items have been removed, this will throw an exception.
        """
        ...

    def __getitem__(self, i: int) -> QuantConnect_Indicators_IReadOnlyWindow_T:
        """
        Indexes into this window, where index 0 is the most recently
            entered value
        
        :param i: the index, i
        :returns: the ith most recent entry.
        """
        ...


class RollingWindow(typing.Generic[QuantConnect_Indicators_RollingWindow_T], System.Object, QuantConnect.Indicators.IReadOnlyWindow[QuantConnect_Indicators_RollingWindow_T], typing.Iterable[QuantConnect_Indicators_RollingWindow_T]):
    """
    This is a window that allows for list access semantics,
        where this[0] refers to the most recent item in the
        window and this[Count-1] refers to the last item in the window
    """

    @property
    def size(self) -> int:
        """Gets the size of this window"""
        ...

    @property.setter
    def size(self, value: int) -> None:
        ...

    @property
    def count(self) -> int:
        """Gets the current number of elements in this window"""
        ...

    @property
    def samples(self) -> int:
        """Gets the number of samples that have been added to this window over its lifetime"""
        ...

    @property
    def most_recently_removed(self) -> QuantConnect_Indicators_RollingWindow_T:
        """
        Gets the most recently removed item from the window. This is the
            piece of data that just 'fell off' as a result of the most recent
            add. If no items have been removed, this will throw an exception.
        """
        ...

    @property
    def is_ready(self) -> bool:
        """
        Gets a value indicating whether or not this window is ready, i.e,
            it has been filled to its capacity
        """
        ...

    def __getitem__(self, i: int) -> QuantConnect_Indicators_RollingWindow_T:
        """
        Indexes into this window, where index 0 is the most recently
            entered value
        
        :param i: the index, i
        :returns: the ith most recent entry.
        """
        ...

    def __init__(self, size: int) -> None:
        """
        Initializes a new instance of the RollwingWindow class with the specified window size.
        
        :param size: The number of items to hold in the window
        """
        ...

    def __setitem__(self, i: int, value: QuantConnect_Indicators_RollingWindow_T) -> None:
        """
        Indexes into this window, where index 0 is the most recently
            entered value
        
        :param i: the index, i
        :returns: the ith most recent entry.
        """
        ...

    def add(self, item: QuantConnect_Indicators_RollingWindow_T) -> None:
        """
        Adds an item to this window and shifts all other elements
        
        :param item: The item to be added
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect_Indicators_RollingWindow_T]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    def reset(self) -> None:
        """Clears this window of all data"""
        ...


class IIndicator(typing.Generic[QuantConnect_Indicators_IIndicator_T], QuantConnect_Indicators_IIndicator, metaclass=abc.ABCMeta):
    """
    KEEPING THIS INTERFACE FOR BACKWARDS COMPATIBILITY.
    Represents an indicator that can receive data updates and emit events when the value of
    the indicator has changed.
    """

    @property
    @abc.abstractmethod
    def updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Indicators.IndicatorDataPoint], None], None]:
        """Event handler that fires after this indicator is updated"""
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Gets a name for this indicator"""
        ...

    @property
    @abc.abstractmethod
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    @abc.abstractmethod
    def current(self) -> QuantConnect.Indicators.IndicatorDataPoint:
        """
        Gets the current state of this indicator. If the state has not been updated
        then the time on the value will equal DateTime.MinValue.
        """
        ...

    @property
    @abc.abstractmethod
    def samples(self) -> int:
        """Gets the number of samples processed by this indicator"""
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...

    def update(self, input: QuantConnect.Data.IBaseData) -> bool:
        """
        Updates the state of this indicator with the given value and returns true
        if this indicator is ready, false otherwise
        
        :param input: The value to use to update this indicator
        :returns: True if this indicator is ready, false otherwise.
        """
        ...


class IndicatorStatus(Enum):
    """The possible states returned by IndicatorBase{T}.ComputeNextValue"""

    SUCCESS = 0
    """The indicator successfully calculated a value for the input data (0)"""

    INVALID_INPUT = 1
    """The indicator detected an invalid input data point or tradebar (1)"""

    MATH_ERROR = 2
    """The indicator encountered a math error during calculations (2)"""

    VALUE_NOT_READY = 3
    """The indicator value is not ready (3)"""


class IndicatorResult(System.Object):
    """Represents the result of an indicator's calculations"""

    @property
    def value(self) -> float:
        """The indicator output value"""
        ...

    @property
    def status(self) -> QuantConnect.Indicators.IndicatorStatus:
        """The indicator status"""
        ...

    def __init__(self, value: float, status: QuantConnect.Indicators.IndicatorStatus = ...) -> None:
        """
        Initializes a new instance of the IndicatorResult class
        
        :param value: The value output by the indicator
        :param status: The status returned by the indicator
        """
        ...


class IndicatorBase(typing.Generic[QuantConnect_Indicators_IndicatorBase_T], QuantConnect_Indicators_IndicatorBase, typing.Iterable[QuantConnect.Indicators.IndicatorDataPoint], metaclass=abc.ABCMeta):
    """Provides a base type for all indicators"""

    @property
    def consolidators(self) -> System.Collections.Generic.ISet[QuantConnect.Data.Consolidators.IDataConsolidator]:
        """The data consolidators associated with this indicator if any"""
        ...

    @property
    def current(self) -> QuantConnect.Indicators.IndicatorDataPoint:
        """
        Gets the current state of this indicator. If the state has not been updated
        then the time on the value will equal DateTime.MinValue.
        """
        ...

    @property
    def previous(self) -> QuantConnect.Indicators.IndicatorDataPoint:
        """
        Gets the previous state of this indicator. If the state has not been updated
        then the time on the value will equal DateTime.MinValue.
        """
        ...

    @property
    def name(self) -> str:
        """Gets a name for this indicator"""
        ...

    @property
    def samples(self) -> int:
        """Gets the number of samples processed by this indicator"""
        ...

    @property
    @abc.abstractmethod
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Indicators.IndicatorDataPoint], None], None]:
        """Event handler that fires after this indicator is updated"""
        ...

    @property
    def window(self) -> QuantConnect.Indicators.RollingWindow[QuantConnect.Indicators.IndicatorDataPoint]:
        """A rolling window keeping a history of the indicator values of a given period"""
        ...

    def __getitem__(self, i: int) -> QuantConnect.Indicators.IndicatorDataPoint:
        """
        Indexes the history windows, where index 0 is the most recent indicator value.
        If index is greater or equal than the current count, it returns null.
        If the index is greater or equal than the window size, it returns null and resizes the windows to i + 1.
        
        :param i: The index
        :returns: the ith most recent indicator value.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the Indicator class.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Indicator class using the specified name.
        
        This method is protected.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Indicator class using the specified name.
        
        This method is protected.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def compare_to(self, other: QuantConnect.Indicators.IIndicator) -> int:
        """
        Compares the current object with another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: A value that indicates the relative order of the objects being compared. The return value has the following meanings: Value Meaning Less than zero This object is less than the  parameter.Zero This object is equal to . Greater than zero This object is greater than .
        """
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        """
        Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
        
        :param obj: An object to compare with this instance.
        :returns: A value that indicates the relative order of the objects being compared. The return value has these meanings: Value Meaning Less than zero This instance precedes  in the sort order. Zero This instance occurs in the same position in the sort order as . Greater than zero This instance follows  in the sort order.
        """
        ...

    def compute_next_value(self, input: QuantConnect_Indicators_IndicatorBase_T) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Returns an enumerator that iterates through the history window.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the history window.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Get Hash Code for this Object
        
        :returns: Integer Hash Code.
        """
        ...

    def on_updated(self, consolidated: QuantConnect.Indicators.IndicatorDataPoint) -> None:
        """
        Event invocator for the Updated event
        
        This method is protected.
        
        :param consolidated: This is the new piece of data produced by this indicator
        """
        ...

    @overload
    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...

    @overload
    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...

    def to_detailed_string(self) -> str:
        """
        Provides a more detailed string of this indicator in the form of {Name} - {Value}
        
        :returns: A detailed string of this indicator's current state.
        """
        ...

    def to_string(self) -> str:
        """
        ToString Overload for Indicator Base
        
        :returns: String representation of the indicator.
        """
        ...

    @overload
    def update(self, input: QuantConnect.Data.IBaseData) -> bool:
        """
        Updates the state of this indicator with the given value and returns true
        if this indicator is ready, false otherwise
        
        :param input: The value to use to update this indicator
        :returns: True if this indicator is ready, false otherwise.
        """
        ...

    @overload
    def update(self, input: QuantConnect.Data.IBaseData) -> bool:
        """
        Updates the state of this indicator with the given value and returns true
        if this indicator is ready, false otherwise
        
        :param input: The value to use to update this indicator
        :returns: True if this indicator is ready, false otherwise.
        """
        ...

    @overload
    def update(self, time: typing.Union[datetime.datetime, datetime.date], value: float) -> bool:
        """
        Updates the state of this indicator with the given value and returns true
        if this indicator is ready, false otherwise
        
        :param time: The time associated with the value
        :param value: The value to use to update this indicator
        :returns: True if this indicator is ready, false otherwise.
        """
        ...

    def validate_and_compute_next_value(self, input: QuantConnect_Indicators_IndicatorBase_T) -> QuantConnect.Indicators.IndicatorResult:
        """
        Computes the next value of this indicator from the given state
        and returns an instance of the IndicatorResult class
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: An IndicatorResult object including the status of the indicator.
        """
        ...


class BarIndicator(QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar], metaclass=abc.ABCMeta):
    """
    The BarIndicator is an indicator that accepts IBaseDataBar data as its input.
    
    This type is more of a shim/typedef to reduce the need to refer to things as IndicatorBase<IBaseDataBar>
    """

    def __init__(self, name: str) -> None:
        """
        Creates a new TradeBarIndicator with the specified name
        
        This method is protected.
        
        :param name: The name of this indicator
        """
        ...


class IIndicatorWarmUpPeriodProvider(metaclass=abc.ABCMeta):
    """Represents an indicator with a warm up period provider."""

    @property
    @abc.abstractmethod
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...


class NormalizedAverageTrueRange(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Normalized Average True Range (NATR).
    The Normalized Average True Range is calculated with the following formula:
    NATR = (ATR(period) / Close) * 100
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the NormalizedAverageTrueRange class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the NATR
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the NormalizedAverageTrueRange class using the specified period.
        
        :param period: The period of the NATR
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class T3MovingAverage(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the T3 Moving Average (T3).
    The T3 Moving Average is calculated with the following formula:
    EMA1(x, Period) = EMA(x, Period)
    EMA2(x, Period) = EMA(EMA1(x, Period),Period)
    GD(x, Period, volumeFactor) = (EMA1(x, Period)*(1+volumeFactor)) - (EMA2(x, Period)* volumeFactor)
    T3 = GD(GD(GD(t, Period, volumeFactor), Period, volumeFactor), Period, volumeFactor);
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, volumeFactor: float = 0.7) -> None:
        """
        Initializes a new instance of the T3MovingAverage class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the T3MovingAverage
        :param volumeFactor: The volume factor of the T3MovingAverage (value must be in the [0,1] range, defaults to 0.7)
        """
        ...

    @overload
    def __init__(self, period: int, volumeFactor: float = 0.7) -> None:
        """
        Initializes a new instance of the T3MovingAverage class using the specified period.
        
        :param period: The period of the T3MovingAverage
        :param volumeFactor: The volume factor of the T3MovingAverage (value must be in the [0,1] range, defaults to 0.7)
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class TradeBarIndicator(QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.TradeBar], metaclass=abc.ABCMeta):
    """
    The TradeBarIndicator is an indicator that accepts TradeBar data as its input.
    
    This type is more of a shim/typedef to reduce the need to refer to things as IndicatorBase<TradeBar>
    """

    def __init__(self, name: str) -> None:
        """
        Creates a new TradeBarIndicator with the specified name
        
        This method is protected.
        
        :param name: The name of this indicator
        """
        ...


class MoneyFlowIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Money Flow Index (MFI) is an oscillator that uses both price and volume to
    measure buying and selling pressure
    
    Typical Price = (High + Low + Close)/3
    Money Flow = Typical Price x Volume
    Positive Money Flow = Sum of the money flows of all days where the typical
        price is greater than the previous day's typical price
    Negative Money Flow = Sum of the money flows of all days where the typical
        price is less than the previous day's typical price
    Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)
    
    Money Flow Index = 100 x  Positive Money Flow / ( Positive Money Flow + Negative Money Flow)
    """

    @property
    def positive_money_flow(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The sum of positive money flow to compute money flow ratio"""
        ...

    @property
    def negative_money_flow(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The sum of negative money flow to compute money flow ratio"""
        ...

    @property
    def previous_typical_price(self) -> float:
        """The current and previous typical price is used to determine positive or negative money flow"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the MoneyFlowIndex class
        
        :param period: The period of the negative and positive money flow
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the MoneyFlowIndex class
        
        :param name: The name of this indicator
        :param period: The period of the negative and positive money flow
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class WindowIndicator(typing.Generic[QuantConnect_Indicators_WindowIndicator_T], QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_WindowIndicator_T], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider, metaclass=abc.ABCMeta):
    """Represents an indicator that acts on a rolling window of data"""

    @property
    def period(self) -> int:
        """Gets the period of this window indicator"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, to the indicator to be ready and fully initialized"""
        ...

    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the WindowIndicator class
        
        This method is protected.
        
        :param name: The name of this indicator
        :param period: The number of data points to hold in the window
        """
        ...

    @overload
    def compute_next_value(self, input: QuantConnect_Indicators_WindowIndicator_T) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    @overload
    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect_Indicators_WindowIndicator_T], input: QuantConnect_Indicators_WindowIndicator_T) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class LogReturn(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the LogReturn indicator (LOGR)
    - log returns are useful for identifying price convergence/divergence in a given period
    - logr = log (current price / last price in period)
    """

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the LogReturn class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the LOGR
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the LogReturn class with the default name and period
        
        :param period: The period of the SMA
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        - logr = log (current price / last price in period)
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class TimeSeriesIndicator(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider, metaclass=abc.ABCMeta):
    """The base class for any Time Series-type indicator, containing methods common to most of such models."""

    @property
    def _diff_heads(self) -> typing.List[float]:
        """
        "Integration" constants
        
        This property is protected.
        """
        ...

    @property.setter
    def _diff_heads(self, value: typing.List[float]) -> None:
        ...

    @property
    @abc.abstractmethod
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    def __init__(self, name: str) -> None:
        """
        A constructor for a basic Time Series indicator.
        
        This method is protected.
        
        :param name: The name of this indicator
        """
        ...

    @staticmethod
    def cumulative_sum(series: System.Collections.Generic.List[float], reverse: bool = False) -> System.Collections.Generic.List[float]:
        """
        Returns a series where each spot is taken by the cumulative sum of all points up to and including
        the value at that spot in the original series.
        
        :param series: Series to cumulatively sum over.
        :param reverse: Whether to reverse the series before applying the cumulative sum.
        :returns: Cumulatively summed series.
        """
        ...

    @staticmethod
    def difference_series(d: int, series: typing.List[float], diff_heads: typing.Optional[typing.List[float]]) -> typing.Union[typing.List[float], typing.List[float]]:
        """
        Differences a time series d times.
        
        :param d: The differencing order
        :param series: Series to difference
        :param diff_heads: "Integration" constants
        """
        ...

    @staticmethod
    def inverse_differenced_series(series: typing.List[float], diff_heads: typing.List[float]) -> typing.List[float]:
        """
        Undoes the differencing of a time series which has been differenced using DifferenceSeries.
        https://github.com/statsmodels/statsmodels/blob/04f00006a7aeb1c93d6894caa420698400da6c33/statsmodels/tsa/tsatools.py#L758
        
        :param series: Series to un-difference
        :param diff_heads: Series of "integration" constants for un-differencing
        """
        ...

    @staticmethod
    def lagged_series(p: int, series: typing.List[float], include_t: bool = False) -> typing.List[typing.List[float]]:
        """
        Returns an array of lagged series for each of {1,...,p} lags.
        
        :param p: Max lag order
        :param series: Series to calculate the lags of
        :param include_t: Whether or not to include t with its lags in the output array
        :returns: A list such that index i returns the series for i+1 lags.
        """
        ...


class AutoRegressiveIntegratedMovingAverage(QuantConnect.Indicators.TimeSeriesIndicator):
    """
    An Autoregressive Intergrated Moving Average (ARIMA) is a time series model which can be used to describe a set of data.
    In particular,with Xₜ representing the series, the model assumes the data are of form
    (after differencing _diffOrder times):
    
        Xₜ = c + εₜ + ΣᵢφᵢXₜ₋ᵢ +  Σᵢθᵢεₜ₋ᵢ
    
    where the first sum has an upper limit of _arOrder and the second _maOrder.
    """

    @property
    def handle_exceptions(self) -> bool:
        """
        Whether or not to handle potential exceptions, returning a zero value. I.e, the values
        provided as input are not valid by the Normal Equations direct regression method
        """
        ...

    @property.setter
    def handle_exceptions(self, value: bool) -> None:
        ...

    @property
    def ar_parameters(self) -> typing.List[float]:
        """Fitted AR parameters (φ terms)."""
        ...

    @property
    def ma_parameters(self) -> typing.List[float]:
        """Fitted MA parameters (θ terms)."""
        ...

    @property
    def intercept(self) -> float:
        """Fitted intercept (c term)."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def ar_residual_error(self) -> float:
        """The variance of the residuals (Var(ε)) from the first step of TwoStepFit."""
        ...

    @property
    def ma_residual_error(self) -> float:
        """The variance of the residuals (Var(ε)) from the second step of TwoStepFit."""
        ...

    @overload
    def __init__(self, name: str, arOrder: int, diffOrder: int, maOrder: int, period: int, intercept: bool = True) -> None:
        """
        Fits an ARIMA(arOrder,diffOrder,maOrder) model of form (after differencing it _diffOrder times):
        
            Xₜ = c + εₜ + ΣᵢφᵢXₜ₋ᵢ +  Σᵢθᵢεₜ₋ᵢ
        
        where the first sum has an upper limit of _arOrder and the second _maOrder.
        This particular constructor fits the model by means of TwoStepFit for a specified name.
        
        :param name: The name of the indicator
        :param arOrder: AR order (p) -- defines the number of past values to consider in the AR component of the model.
        :param diffOrder: Difference order (d) -- defines how many times to difference the model before fitting parameters.
        :param maOrder: MA order -- defines the number of past values to consider in the MA component of the model.
        :param period: Size of the rolling series to fit onto
        :param intercept: Whether or not to include the intercept term
        """
        ...

    @overload
    def __init__(self, arOrder: int, diffOrder: int, maOrder: int, period: int, intercept: bool) -> None:
        """
        Fits an ARIMA(arOrder,diffOrder,maOrder) model of form (after differencing it _diffOrder times):
        
            Xₜ = c + εₜ + ΣᵢφᵢXₜ₋ᵢ +  Σᵢθᵢεₜ₋ᵢ
        
        where the first sum has an upper limit of _arOrder and the second _maOrder.
        This particular constructor fits the model by means of TwoStepFit using ordinary least squares.
        
        :param arOrder: AR order (p) -- defines the number of past values to consider in the AR component of the model.
        :param diffOrder: Difference order (d) -- defines how many times to difference the model before fitting parameters.
        :param maOrder: MA order (q) -- defines the number of past values to consider in the MA component of the model.
        :param period: Size of the rolling series to fit onto
        :param intercept: Whether to include an intercept term (c)
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Forecasts the series of the fitted model one point ahead.
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class SimpleMovingAverage(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """Represents the traditional simple moving average indicator (SMA)"""

    @property
    def rolling_sum(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """A rolling sum for computing the average for the given period"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the SimpleMovingAverage class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the SMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the SimpleMovingAverage class with the default name and period
        
        :param period: The period of the SMA
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Indicator(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], metaclass=abc.ABCMeta):
    """
    Represents a type capable of ingesting a piece of data and producing a new piece of data.
    Indicators can be used to filter and transform data into a new, more informative form.
    """

    DEFAULT_WINDOW_SIZE: int
    """The default size of the history window for the indicator"""

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Indicator class using the specified name.
        
        This method is protected.
        
        :param name: The name of this indicator
        """
        ...


class HilbertTransform(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Hilbert Transform Indicator by John Ehlers.
    By using present and prior price differences, and some feedback, price values are split into their complex number components
    of real (inPhase) and imaginary (quadrature) parts.
    Source: http://www.technicalanalysis.org.uk/moving-averages/Ehle.pdf
    """

    @property
    def in_phase(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Real (inPhase) part of complex number component of price values"""
        ...

    @property
    def quadrature(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Imaginary (quadrature) part of complex number component of price values"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, length: int, inPhaseMultiplicationFactor: float, quadratureMultiplicationFactor: float) -> None:
        """
        Creates a new Hilbert Transform indicator
        
        :param name: The name of this indicator
        :param length: The length of the FIR filter used in the calculation of the Hilbert Transform. This parameter determines the number of filter coefficients in the FIR filter.
        :param inPhaseMultiplicationFactor: The multiplication factor used in the calculation of the in-phase component of the Hilbert Transform. This parameter adjusts the sensitivity and responsiveness of the transform to changes in the input signal.
        :param quadratureMultiplicationFactor: The multiplication factor used in the calculation of the quadrature component of the Hilbert Transform. This parameter also adjusts the sensitivity and responsiveness of the transform to changes in the input signal.
        """
        ...

    @overload
    def __init__(self, length: int = 7, inPhaseMultiplicationFactor: float = 0.635, quadratureMultiplicationFactor: float = 0.338) -> None:
        """
        Creates a new Hilbert Transform indicator with default name and default params
        
        :param length: The length of the FIR filter used in the calculation of the Hilbert Transform. This parameter determines the number of filter coefficients in the FIR filter.
        :param inPhaseMultiplicationFactor: The multiplication factor used in the calculation of the in-phase component of the Hilbert Transform. This parameter adjusts the sensitivity and responsiveness of the transform to changes in the input signal.
        :param quadratureMultiplicationFactor: The multiplication factor used in the calculation of the quadrature component of the Hilbert Transform. This parameter also adjusts the sensitivity and responsiveness of the transform to changes in the input signal.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MovingAverageType(Enum):
    """Defines the different types of moving averages"""

    SIMPLE = 0
    """An unweighted, arithmetic mean (0)"""

    EXPONENTIAL = 1
    """The standard exponential moving average, using a smoothing factor of 2/(n+1) (1)"""

    WILDERS = 2
    """An exponential moving average, using a smoothing factor of 1/n and simple moving average as seeding (2)"""

    LINEAR_WEIGHTED_MOVING_AVERAGE = 3
    """A weighted moving average type (3)"""

    DOUBLE_EXPONENTIAL = 4
    """The double exponential moving average (4)"""

    TRIPLE_EXPONENTIAL = 5
    """The triple exponential moving average (5)"""

    TRIANGULAR = 6
    """The triangular moving average (6)"""

    T_3 = 7
    """The T3 moving average (7)"""

    KAMA = 8
    """The Kaufman Adaptive Moving Average (8)"""

    HULL = 9
    """The Hull Moving Average (9)"""

    ALMA = 10
    """The Arnaud Legoux Moving Average (10)"""

    ZLEMA = 11
    """The Zero Lag Exponential Moving Average (11)"""

    MGD = 12
    """The McGinley Dynamic moving average (12)"""


class MovingAverageConvergenceDivergence(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates two moving averages defined on a base indicator and produces the difference
    between the fast and slow averages.
    """

    @property
    def fast(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the fast average indicator"""
        ...

    @property
    def slow(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the slow average indicator"""
        ...

    @property
    def signal(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the signal of the MACD"""
        ...

    @property
    def histogram(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Developed by Thomas Aspray in 1986, the MACD-Histogram measures the distance between MACD and its signal line,
        is an oscillator that fluctuates above and below the zero line.
        Bullish or bearish divergences in the MACD-Histogram can alert chartists to an imminent signal line crossover in MACD.
        """
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, fastPeriod: int, slowPeriod: int, signalPeriod: int, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new MACD with the specified parameters
        
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param signalPeriod: The signal period
        :param type: The type of moving averages to use
        """
        ...

    @overload
    def __init__(self, name: str, fastPeriod: int, slowPeriod: int, signalPeriod: int, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new MACD with the specified parameters
        
        :param name: The name of this indicator
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param signalPeriod: The signal period
        :param type: The type of moving averages to use
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AbsolutePriceOscillator(QuantConnect.Indicators.MovingAverageConvergenceDivergence):
    """
    This indicator computes the Absolute Price Oscillator (APO)
    The Absolute Price Oscillator is calculated using the following formula:
    APO[i] = FastMA[i] - SlowMA[i]
    """

    @overload
    def __init__(self, name: str, fastPeriod: int, slowPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the AbsolutePriceOscillator class using the specified name and parameters.
        
        :param name: The name of this indicator
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param movingAverageType: The type of moving average to use
        """
        ...

    @overload
    def __init__(self, fastPeriod: int, slowPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the AbsolutePriceOscillator class using the specified parameters.
        
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param movingAverageType: The type of moving average to use
        """
        ...


class Maximum(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """Represents an indicator capable of tracking the maximum value and how many periods ago it occurred"""

    @property
    def periods_since_maximum(self) -> int:
        """The number of periods since the maximum value was encountered"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new Maximum indicator with the specified period
        
        :param period: The period over which to look back
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new Maximum indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to look back
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """This method is protected."""
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class TripleExponentialMovingAverage(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Triple Exponential Moving Average (TEMA).
    The Triple Exponential Moving Average is calculated with the following formula:
    EMA1 = EMA(t,period)
    EMA2 = EMA(EMA(t,period),period)
    EMA3 = EMA(EMA(EMA(t,period),period),period)
    TEMA = 3 * EMA1 - 3 * EMA2 + EMA3
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the TripleExponentialMovingAverage class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the TEMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the TripleExponentialMovingAverage class using the specified period.
        
        :param period: The period of the TEMA
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AwesomeOscillator(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Awesome Oscillator Indicator tracks the price midpoint-movement of a security. Specifically,
    
    AO = MAfast[(H+L)/2] - MAslow[(H+L)/2]
    
    where MAfast and MAslow denote simple moving averages wherein fast has a shorter period.
    https://www.barchart.com/education/technical-indicators/awesome_oscillator
    """

    @property
    def slow_ao(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the indicators slow period moving average."""
        ...

    @property
    def fast_ao(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the indicators fast period moving average."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, fastPeriod: int, slowPeriod: int, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new Awesome Oscillator from the specified periods.
        
        :param fastPeriod: The period of the fast moving average associated with the AO
        :param slowPeriod: The period of the slow moving average associated with the AO
        :param type: The type of moving average used when computing the fast and slow term. Defaults to simple moving average.
        """
        ...

    @overload
    def __init__(self, name: str, fastPeriod: int, slowPeriod: int, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new Awesome Oscillator from the specified periods.
        
        :param name: The name of this indicator
        :param fastPeriod: The period of the fast moving average associated with the AO
        :param slowPeriod: The period of the slow moving average associated with the AO
        :param type: The type of moving average used when computing the fast and slow term. Defaults to simple moving average.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state.
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator"""
        ...


class ConnorsRelativeStrengthIndex(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the Connors Relative Strength Index (CRSI), a combination of
    the traditional Relative Strength Index (RSI), a Streak RSI (SRSI), and
    Percent Rank.
    This index is designed to provide a more robust measure of market strength
    by combining momentum, streak behavior, and price change.
    """

    @property
    def is_ready(self) -> bool:
        """
        Gets a value indicating whether the indicator is ready for use.
        The indicator is ready when all its components (RSI, SRSI, and PriceChangeRatios) are ready.
        """
        ...

    @property
    def warm_up_period(self) -> int:
        """
        Gets the warm-up period required for the indicator to be ready.
        This is the maximum period of all components (RSI, SRSI, and PriceChangeRatios).
        """
        ...

    @overload
    def __init__(self, name: str, rsiPeriod: int, rsiPeriodStreak: int, lookBackPeriod: int) -> None:
        """
        Initializes a new instance of the ConnorsRelativeStrengthIndex class.
        
        :param name: The name of the indicator instance.
        :param rsiPeriod: The period for the RSI calculation.
        :param rsiPeriodStreak: The period for the Streak RSI calculation.
        :param lookBackPeriod: The period for calculating the Percent Rank.
        """
        ...

    @overload
    def __init__(self, rsiPeriod: int, rsiPeriodStreak: int, rocPeriod: int) -> None:
        """
        Initializes a new instance of the ConnorsRelativeStrengthIndex with specified RSI, Streak RSI,
        and lookBack periods, using a default name format based on the provided parameters.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for the Connors Relative Strength Index (CRSI) based on the latest input data point.
        The CRSI is calculated as the average of the traditional RSI, Streak RSI, and Percent Rank.
        
        This method is protected.
        
        :param input: The current input data point (typically the price data for the current period).
        :returns: The computed CRSI value, which combines the RSI, Streak RSI, and Percent Rank into a single value. Returns zero if the indicator is not yet ready.
        """
        ...

    def reset(self) -> None:
        """
        Resets the indicator to its initial state. This clears all internal data and resets
        the RSI, Streak RSI, and PriceChangeRatios, as well as the trend streak counter.
        """
        ...


class VolumeWeightedMovingAverage(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Volume Weighted Moving Average (VWMA)
    It is a technical analysis indicator used by traders to determine the average price of an asset over a given period of time,
    taking into account both price and volume.
    """

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the VolumeWeightedMovingAverage class using the specified name.
        
        :param name: The name of this indicator
        :param period: The period of the SMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the VolumeWeightedMovingAverage class using the specified name.
        
        :param period: The period of the SMA
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class HullMovingAverage(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Produces a Hull Moving Average as explained at http://www.alanhull.com/hull-moving-average/
    and derived from the instructions for the Excel VBA code at http://finance4traders.blogspot.com/2009/06/how-to-calculate-hull-moving-average.html
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        A Hull Moving Average
        
        :param name: string - a name for the indicator
        :param period: int - the number of periods to calculate the HMA - the period of the slower LWMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        A Hull Moving Average.
        
        :param period: int - the number of periods over which to calculate the HMA - the length of the slower LWMA
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RogersSatchellVolatility(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Rogers-Satchell Volatility
    It is an estimator for measuring the volatility of securities
    with an average return not equal to zero.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the RogersSatchellVolatility class using the specified parameters
        
        :param period: The period of moving window
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the RogersSatchellVolatility class using the specified parameters
        
        :param name: The name of this indicator
        :param period: The period of moving window
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class CompositeIndicator(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]):
    """
    This indicator is capable of wiring up two separate indicators into a single indicator
    such that the output of each will be sent to a user specified function.
    """

    @property
    def left(self) -> QuantConnect.Indicators.IndicatorBase:
        """Gets the 'left' indicator for the delegate"""
        ...

    @property
    def right(self) -> QuantConnect.Indicators.IndicatorBase:
        """Gets the 'right' indicator for the delegate"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, composer: typing.Callable[[QuantConnect.Indicators.IndicatorBase, QuantConnect.Indicators.IndicatorBase], QuantConnect.Indicators.IndicatorResult]) -> None:
        """
        Creates a new CompositeIndicator capable of taking the output from the left and right indicators
        and producing a new value via the composer delegate specified
        
        :param name: The name of this indicator
        :param left: The left indicator for the 'composer'
        :param right: The right indicator for the 'composer'
        :param composer: Function used to compose the left and right indicators
        """
        ...

    @overload
    def __init__(self, left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, composer: typing.Callable[[QuantConnect.Indicators.IndicatorBase, QuantConnect.Indicators.IndicatorBase], QuantConnect.Indicators.IndicatorResult]) -> None:
        """
        Creates a new CompositeIndicator capable of taking the output from the left and right indicators
        and producing a new value via the composer delegate specified
        
        :param left: The left indicator for the 'composer'
        :param right: The right indicator for the 'composer'
        :param composer: Function used to compose the left and right indicators
        """
        ...

    @overload
    def __init__(self, name: str, left: typing.Any, right: typing.Any, handler: typing.Any) -> None:
        """
        Initializes a new instance of CompositeIndicator using two indicators
        and a custom function.
        
        :param name: The name of the composite indicator.
        :param left: The first indicator in the composition.
        :param right: The second indicator in the composition.
        :param handler: A Python function that processes the indicator values.
        """
        ...

    @overload
    def __init__(self, left: typing.Any, right: typing.Any, handler: typing.Any) -> None:
        """
        Initializes a new instance of CompositeIndicator using two indicators
        and a custom function.
        
        :param left: The first indicator in the composition.
        :param right: The second indicator in the composition.
        :param handler: A Python function that processes the indicator values.
        """
        ...

    def compute_next_value(self, _: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param _: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def indicator_composer(self, left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase) -> QuantConnect.Indicators.IndicatorResult:
        """
        Delegate type used to compose the output of two indicators into a new value.
        
        :param left: The left indicator
        :param right: The right indicator
        :returns: And indicator result representing the composition of the two indicators.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...

    def validate_and_compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> QuantConnect.Indicators.IndicatorResult:
        """
        Computes the next value of this indicator from the given state
        and returns an instance of the IndicatorResult class
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: An IndicatorResult object including the status of the indicator.
        """
        ...


class ResetCompositeIndicator(QuantConnect.Indicators.CompositeIndicator):
    """Class that extends CompositeIndicator to execute a given action once is reset"""

    @overload
    def __init__(self, left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, composer: typing.Callable[[QuantConnect.Indicators.IndicatorBase, QuantConnect.Indicators.IndicatorBase], QuantConnect.Indicators.IndicatorResult], extraResetAction: typing.Callable[[], None]) -> None:
        """
        Creates a new ResetCompositeIndicator capable of taking the output from the left and right indicators
        and producing a new value via the composer delegate specified
        
        :param left: The left indicator for the 'composer'
        :param right: The right indicator for the 'composer'
        :param composer: Function used to compose the left and right indicators
        :param extraResetAction: Action to execute once the composite indicator is reset
        """
        ...

    @overload
    def __init__(self, name: str, left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, composer: typing.Callable[[QuantConnect.Indicators.IndicatorBase, QuantConnect.Indicators.IndicatorBase], QuantConnect.Indicators.IndicatorResult], extraResetAction: typing.Callable[[], None]) -> None:
        """
        Creates a new CompositeIndicator capable of taking the output from the left and right indicators
        and producing a new value via the composer delegate specified
        
        :param name: The name of this indicator
        :param left: The left indicator for the 'composer'
        :param right: The right indicator for the 'composer'
        :param composer: Function used to compose the left and right indicators
        :param extraResetAction: Action to execute once the indicator is reset
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and invokes the given reset action"""
        ...


class Sum(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """Represents an indicator capable of tracking the sum for the given period"""

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the Sum class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the SMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the Sum class with the default name and period
        
        :param period: The period of the SMA
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MultiSymbolIndicator(typing.Generic[QuantConnect_Indicators_MultiSymbolIndicator_TInput], QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_MultiSymbolIndicator_TInput], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider, metaclass=abc.ABCMeta):
    """Base class for indicators that work with multiple different symbols."""

    class SymbolData(System.Object):
        """
        Contains the data points, the current input and other relevant indicator data for a symbol.
        
        This class is protected.
        """

        @property
        def exchange_time_zone(self) -> typing.Any:
            """The exchange time zone for the security represented by this symbol."""
            ...

        @property
        def data_points(self) -> QuantConnect.Indicators.RollingWindow[QuantConnect_Indicators_MultiSymbolIndicator_TInput]:
            """
            Data points for the symbol.
            This only hold the data points that have been used to calculate the indicator,
            which are those that had matching end times for every symbol.
            """
            ...

        @property
        def current_input(self) -> QuantConnect_Indicators_MultiSymbolIndicator_TInput:
            """The last input data point for the symbol."""
            ...

        @property.setter
        def current_input(self, value: QuantConnect_Indicators_MultiSymbolIndicator_TInput) -> None:
            ...

        @property
        def new_input(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect_Indicators_MultiSymbolIndicator_TInput], None], None]:
            """Event that fires when a new input data point is set for the symbol."""
            ...

        @property
        def current_input_end_time_utc(self) -> datetime.datetime:
            """The end time of the last input data point for the symbol in UTC."""
            ...

        def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int) -> None:
            """Initializes a new instance of the SymbolData class."""
            ...

        def reset(self) -> None:
            """Resets this symbol data to its initial state"""
            ...

        def set_resolution(self, resolution: QuantConnect.Resolution) -> None:
            """Sets the resolution for this symbol data, to be used for time alignment."""
            ...

    @property
    def data_by_symbol(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Indicators.MultiSymbolIndicator.SymbolData]:
        """
        Relevant data for each symbol the indicator works on, including all inputs
        and actual data points used for calculation.
        
        This property is protected.
        """
        ...

    @property
    def indicator_value(self) -> float:
        """
        The most recently computed value of the indicator.
        
        This property is protected.
        """
        ...

    @property.setter
    def indicator_value(self, value: float) -> None:
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property.setter
    def warm_up_period(self, value: int) -> None:
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    def __init__(self, name: str, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], period: int) -> None:
        """
        Initializes the dual symbol indicator.
        
        The constructor accepts a target symbol and a reference symbol. It also initializes
        the time zones for both symbols and checks if they are different.
        
        This method is protected.
        
        :param name: The name of the indicator.
        :param symbols: The symbols the indicator works on .
        :param period: The period (number of data points) over which to calculate the indicator.
        """
        ...

    def compute_indicator(self) -> float:
        """
        Computes the next value of this indicator from the given state.
        This will be called only when the indicator is ready, that is,
        when data for all symbols at a given time is available.
        
        This method is protected.
        """
        ...

    def compute_next_value(self, input: QuantConnect_Indicators_MultiSymbolIndicator_TInput) -> float:
        """
        Checks and computes the indicator if the input data matches.
        This method ensures the input data points are from matching time periods and different symbols.
        
        This method is protected.
        
        :param input: The input data point (e.g., TradeBar for a symbol).
        :returns: The most recently computed value of the indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class OptionPricingModelType(Enum):
    """Defines different types of option pricing model"""

    BLACK_SCHOLES = 0
    """Vanilla Black Scholes Model"""

    BINOMIAL_COX_ROSS_RUBINSTEIN = 1
    """The Cox-Ross-Rubinstein binomial tree model (CRR model)"""

    FORWARD_TREE = 2
    """The forward binomial tree model, or Cox-Ross-Rubinstein with drift model"""


class Identity(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator that is a ready after ingesting a single sample and
        always returns the same value as it is given.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized"""
        ...

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Identity indicator with the specified name
        
        :param name: The name of the indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class OptionIndicatorBase(QuantConnect.Indicators.MultiSymbolIndicator[QuantConnect.Data.IBaseData], metaclass=abc.ABCMeta):
    """To provide a base class for option indicator"""

    @property
    def option_symbol(self) -> QuantConnect.Symbol:
        """Option's symbol object"""
        ...

    @property
    def _opposite_option_symbol(self) -> QuantConnect.Symbol:
        """
        Mirror option symbol (by option right), for implied volatility
        
        This property is protected.
        """
        ...

    @property
    def _underlying_symbol(self) -> QuantConnect.Symbol:
        """
        Underlying security's symbol object
        
        This property is protected.
        """
        ...

    @property
    def _option_model(self) -> QuantConnect.Indicators.OptionPricingModelType:
        """
        Option pricing model used to calculate indicator
        
        This property is protected.
        """
        ...

    @property.setter
    def _option_model(self, value: QuantConnect.Indicators.OptionPricingModelType) -> None:
        ...

    @property
    def _risk_free_interest_rate_model(self) -> QuantConnect.Data.IRiskFreeInterestRateModel:
        """
        Risk-free rate model
        
        This property is protected.
        """
        ...

    @property
    def _dividend_yield_model(self) -> QuantConnect.Data.IDividendYieldModel:
        """
        Dividend yield model, for continuous dividend yield
        
        This property is protected.
        """
        ...

    @property
    def expiry(self) -> datetime.datetime:
        """Gets the expiration time of the option"""
        ...

    @property
    def right(self) -> QuantConnect.OptionRight:
        """Gets the option right (call/put) of the option"""
        ...

    @property
    def strike(self) -> float:
        """Gets the strike price of the option"""
        ...

    @property
    def style(self) -> QuantConnect.OptionStyle:
        """Gets the option style (European/American) of the option"""
        ...

    @property
    def risk_free_rate(self) -> QuantConnect.Indicators.Identity:
        """Risk Free Rate"""
        ...

    @property.setter
    def risk_free_rate(self, value: QuantConnect.Indicators.Identity) -> None:
        ...

    @property
    def dividend_yield(self) -> QuantConnect.Indicators.Identity:
        """Dividend Yield"""
        ...

    @property.setter
    def dividend_yield(self, value: QuantConnect.Indicators.Identity) -> None:
        ...

    @property
    def price(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the option price level"""
        ...

    @property
    def opposite_price(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the mirror option price level, for implied volatility"""
        ...

    @property
    def underlying_price(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the underlying's price level"""
        ...

    @property
    def use_mirror_contract(self) -> bool:
        """Flag if mirror option is implemented for parity type calculation"""
        ...

    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, period: int = 1) -> None:
        """
        Initializes a new instance of the OptionIndicatorBase class
        
        This method is protected.
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate the Greek/IV
        :param period: The lookback period of volatility
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.IBaseData) -> float:
        """
        Computes the next value of this indicator from the given state.
        This will round the result to 7 decimal places.
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    @staticmethod
    def get_option_model(option_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType], option_style: QuantConnect.OptionStyle) -> QuantConnect.Indicators.OptionPricingModelType:
        """
        Gets the option pricing model based on the option style, if not specified
        
        :param option_model: The optional option pricing model, which will be returned if not null
        :param option_style: The option style
        :returns: The option pricing model based on the option style, if not specified.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and all sub-indicators"""
        ...


class ImpliedVolatility(QuantConnect.Indicators.OptionIndicatorBase):
    """Implied Volatility indicator that calculate the IV of an option using Black-Scholes Model"""

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the ImpliedVolatility class
        
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate IV
        """
        ...

    def calculate_iv(self, time_till_expiry: float) -> float:
        """
        Computes the IV of the option
        
        This method is protected.
        
        :param time_till_expiry: the time until expiration in years
        :returns: Smoothened IV of the option.
        """
        ...

    def compute_indicator(self) -> float:
        """
        Computes the next value
        
        This method is protected.
        
        :returns: The input is returned unmodified.
        """
        ...

    @overload
    def set_smoothing_function(self, function: typing.Callable[[float, float], float]) -> None:
        """
        Set the smoothing function of IV, using both call and put IV value
        
        :param function: the smoothing function
        """
        ...

    @overload
    def set_smoothing_function(self, function: typing.Any) -> None:
        """
        Set the smoothing function of IV, using both call and put IV value
        
        :param function: the smoothing function
        """
        ...


class TriangularMovingAverage(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Triangular Moving Average (TRIMA).
    The Triangular Moving Average is calculated with the following formula:
    (1) When the period is even, TRIMA(x,period)=SMA(SMA(x,period/2),(period/2)+1)
    (2) When the period is odd,  TRIMA(x,period)=SMA(SMA(x,(period+1)/2),(period+1)/2)
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the TriangularMovingAverage class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the indicator
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the TriangularMovingAverage class using the specified period.
        
        :param period: The period of the indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class DetrendedPriceOscillator(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Detrended Price Oscillator is an indicator designed to remove trend from price
    and make it easier to identify cycles.
    DPO does not extend to the last date because it is based on a displaced moving average.
    Is estimated as Price {X/2 + 1} periods ago less the X-period simple moving average.
    E.g.DPO(20) equals price 11 days ago less the 20-day SMA.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the DetrendedPriceOscillator class.
        
        :param name: The name for the indicator.
        :param period: The number of periods to calculate the DPO.
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the DetrendedPriceOscillator class.
        
        :param period: The number of periods to calculate the DPO.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class StochasticRelativeStrengthIndex(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Stochastic RSI, or simply StochRSI, is a technical analysis indicator used to determine whether
    an asset is overbought or oversold, as well as to identify current market trends.
    As the name suggests, the StochRSI is a derivative of the standard Relative Strength Index (RSI) and,
    as such, is considered an indicator of an indicator.
    It is a type of oscillator, meaning that it fluctuates above and below a center line.
    """

    @property
    def k(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the %K output"""
        ...

    @property
    def d(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the %D output"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, rsiPeriod: int, stochPeriod: int, kSmoothingPeriod: int, dSmoothingPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the StochasticRelativeStrengthIndex class
        
        :param rsiPeriod: The period of the relative strength index
        :param stochPeriod: The period of the stochastic indicator
        :param kSmoothingPeriod: The smoothing period of K output (aka %K)
        :param dSmoothingPeriod: The smoothing period of D output (aka %D)
        :param movingAverageType: The type of moving average to be used for k and d
        """
        ...

    @overload
    def __init__(self, name: str, rsiPeriod: int, stochPeriod: int, kSmoothingPeriod: int, dSmoothingPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the StochasticRelativeStrengthIndex class
        
        :param name: The name of this indicator
        :param rsiPeriod: The period of the relative strength index
        :param stochPeriod: The period of the stochastic indicator
        :param kSmoothingPeriod: The smoothing period of K output
        :param dSmoothingPeriod: The smoothing period of D output
        :param movingAverageType: The type of moving average to be used
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of the following sub-indicators from the given state:
        K (%K) and D (%D)
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: The input is returned unmodified.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and all sub-indicators"""
        ...


class WindowIdentity(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]):
    """
    Represents an indicator that is a ready after ingesting enough samples (# samples > period)
    and always returns the same value as it is given.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the WindowIdentity class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the WindowIdentity
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the WindowIdentity class with the default name and period
        
        :param period: The period of the WindowIdentity
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class WilderSwingIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator calculates the Swing Index (SI) as defined by Welles Wilder
    in his book 'New Concepts in Technical Trading Systems'.
    
    SIₜ = 50 * ( N / R ) * ( K / T )
    
      Where:
      N
            Equals: Cₜ - Cₜ₋₁ + 0.5 * (Cₜ - Oₜ) + 0.25 * (Cₜ₋₁ - Oₜ₋₁)
            See R
            Found by selecting the expression with the largest value and
            then using the corresponding formula.
            
              Expression => Formula
              
                    |Hₜ - Cₜ₋₁| => |Hₜ - Cₜ| - 0.5 * |Lₜ - Cₜ₋₁| + 0.25 * |Cₜ₋₁ - Oₜ₋₁|
                  
                    |Lₜ - Cₜ₋₁| => |Lₜ - Cₜ| - 0.5 * |Hₜ - Cₜ₋₁| + 0.25 * |Cₜ₋₁ - Oₜ₋₁|
                  
                    |Hₜ - Lₜ| => |Hₜ - Lₜ₋₁| + 0.25 * |Cₜ₋₁ - Oₜ₋₁|
                  See K
            Found by selecting the larger of the two expressions:
            |Hₜ - Cₜ₋₁|, |Lₜ - Cₜ₋₁|
            See T
            The limit move, or the maximum change in price during the time
            period for the bar. Passed as limitMove via the constructor.
            See
    """

    @property
    def _current_input(self) -> QuantConnect.Data.Market.IBaseDataBar:
        """
        Holds the bar for the current period.
        
        This property is protected.
        """
        ...

    @property
    def _previous_input(self) -> QuantConnect.Data.Market.IBaseDataBar:
        """
        Holds the bar for the previous period.
        
        This property is protected.
        """
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized."""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, limitMove: float) -> None:
        """
        Initializes a new instance of the WilderSwingIndex class using the specified name.
        
        :param name: A string for the name of this indicator.
        :param limitMove: A decimal representing the limit move value for the period.
        """
        ...

    @overload
    def __init__(self, limitMove: float) -> None:
        """
        Initializes a new instance of the WilderSwingIndex class using the default name.
        
        :param limitMove: A decimal representing the limit move value for the period.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state.
        
        This method is protected.
        
        :param input: The input given to the indicator.
        :returns: A new value for this indicator.
        """
        ...


class IchimokuKinkoHyo(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ichimoku Kinko Hyo indicator. It consists of the following main indicators:
    Tenkan-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 9)
    Kijun-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 26)
    Senkou A Span: (Tenkan-sen + Kijun-sen )/ 2 from a specific number of periods ago (normally 26)
    Senkou B Span: (Highest High + Lowest Low) / 2 for the specific period (normally 52), from a specific number of periods ago (normally 26)
    """

    @property
    def tenkan(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Tenkan-sen component of the Ichimoku indicator"""
        ...

    @property
    def kijun(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Kijun-sen component of the Ichimoku indicator"""
        ...

    @property
    def senkou_a(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Senkou A Span component of the Ichimoku indicator"""
        ...

    @property
    def senkou_b(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Senkou B Span component of the Ichimoku indicator"""
        ...

    @property
    def chikou(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Chikou Span component of the Ichimoku indicator"""
        ...

    @property
    def tenkan_maximum(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Tenkan-sen Maximum component of the Ichimoku indicator"""
        ...

    @property
    def tenkan_minimum(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Tenkan-sen Minimum component of the Ichimoku indicator"""
        ...

    @property
    def kijun_maximum(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Kijun-sen Maximum component of the Ichimoku indicator"""
        ...

    @property
    def kijun_minimum(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Kijun-sen Minimum component of the Ichimoku indicator"""
        ...

    @property
    def senkou_b_maximum(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Senkou B Maximum component of the Ichimoku indicator"""
        ...

    @property
    def senkou_b_minimum(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Senkou B Minimum component of the Ichimoku indicator"""
        ...

    @property
    def delayed_tenkan_senkou_a(self) -> QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Delayed Tenkan Senkou A component of the Ichimoku indicator"""
        ...

    @property
    def delayed_kijun_senkou_a(self) -> QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Delayed Kijun Senkou A component of the Ichimoku indicator"""
        ...

    @property
    def delayed_maximum_senkou_b(self) -> QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Delayed Maximum Senkou B component of the Ichimoku indicator"""
        ...

    @property
    def delayed_minimum_senkou_b(self) -> QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]:
        """The Delayed Minimum Senkou B component of the Ichimoku indicator"""
        ...

    @property
    def is_ready(self) -> bool:
        """Returns true if all of the sub-components of the Ichimoku indicator is ready"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, tenkanPeriod: int = 9, kijunPeriod: int = 26, senkouAPeriod: int = 26, senkouBPeriod: int = 52, senkouADelayPeriod: int = 26, senkouBDelayPeriod: int = 26) -> None:
        """
        Creates a new IchimokuKinkoHyo indicator from the specific periods
        
        :param tenkanPeriod: The Tenkan-sen period
        :param kijunPeriod: The Kijun-sen period
        :param senkouAPeriod: The Senkou A Span period
        :param senkouBPeriod: The Senkou B Span period
        :param senkouADelayPeriod: The Senkou A Span delay
        :param senkouBDelayPeriod: The Senkou B Span delay
        """
        ...

    @overload
    def __init__(self, name: str, tenkanPeriod: int = 9, kijunPeriod: int = 26, senkouAPeriod: int = 26, senkouBPeriod: int = 52, senkouADelayPeriod: int = 26, senkouBDelayPeriod: int = 26) -> None:
        """
        Creates a new IchimokuKinkoHyo indicator from the specific periods
        
        :param name: The name of this indicator
        :param tenkanPeriod: The Tenkan-sen period
        :param kijunPeriod: The Kijun-sen period
        :param senkouAPeriod: The Senkou A Span period
        :param senkouBPeriod: The Senkou B Span period
        :param senkouADelayPeriod: The Senkou A Span delay
        :param senkouBDelayPeriod: The Senkou B Span delay
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class DerivativeOscillator(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the Derivative Oscillator Indicator, utilizing
    a moving average convergence-divergence (MACD) histogram to a double-smoothed relative strength index (RSI).
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    def __init__(self, name: str, rsiPeriod: int, smoothingRsiPeriod: int, doubleSmoothingRsiPeriod: int, signalLinePeriod: int) -> None:
        """
        Initializes a new instance of the IndicatorDerivativeOscillator class with the specified name and periods.
        
        :param name: The name of the indicator
        :param rsiPeriod: The period for the RSI calculation
        :param smoothingRsiPeriod: The period for the smoothing RSI
        :param doubleSmoothingRsiPeriod: The period for the double smoothing RSI
        :param signalLinePeriod: The period for the signal line
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for the derivative oscillator indicator from the given state
        
        This method is protected.
        
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class CorrelationType(Enum):
    """Defines the different types of Correlation"""

    PEARSON = 0
    """
    Pearson Correlation (Product-Moment Correlation):
    Measures the linear relationship between two datasets. The coefficient ranges from -1 to 1.
    A value of 1 indicates a perfect positive linear relationship, -1 indicates a perfect
    negative linear relationship, and 0 indicates no linear relationship.
    It assumes that both datasets are normally distributed and the relationship is linear.
    It is sensitive to outliers which can affect the correlation significantly.
    """

    SPEARMAN = 1
    """
    Spearman Correlation (Rank Correlation):
    Measures the strength and direction of the monotonic relationship between two datasets.
    Instead of calculating the coefficient using raw data, it uses the rank of the data points.
    This method is non-parametric and does not assume a normal distribution of the datasets.
    It's useful when the data is not normally distributed or when the relationship is not linear.
    Spearman's correlation is less sensitive to outliers than Pearson's correlation.
    The coefficient also ranges from -1 to 1 with similar interpretations for the values,
    but it reflects monotonic relationships rather than only linear ones.
    """


class VariableIndexDynamicAverage(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period adaptive weighted moving average indicator.
    VIDYAi = Pricei x F x ABS(CMOi) + VIDYAi-1 x (1 - F x ABS(CMOi))
    where:
    VIDYAi - is the value of the current period.
    Pricei - is the source price of the period being calculated.
    F = 2/(Period_EMA+1) - is a smoothing factor.
    ABS(CMOi) - is the absolute current value of CMO.
    VIDYAi-1 - is the value of the period immediately preceding the period being calculated.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the VariableIndexDynamicAverage class using the specified period.
        
        :param period: The period of the indicator
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the VariableIndexDynamicAverage class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the indicator
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AdvanceDeclineIndicator(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider, metaclass=abc.ABCMeta):
    """
    The advance-decline indicator compares the number of stocks
    that closed higher against the number of stocks
    that closed lower than their previous day's closing prices.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    def __init__(self, name: str, computeSub: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.TradeBar]], float], computeMain: typing.Callable[[float, float], float]) -> None:
        """Initializes a new instance of the AdvanceDeclineRatio class"""
        ...

    def add(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Add tracking asset issue
        
        :param asset: tracking asset issue
        """
        ...

    def add_stock(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Deprecated
        
        Please use Add(asset)
        """
        warnings.warn("Please use Add(asset)", DeprecationWarning)

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def remove(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Remove tracking asset issue
        
        :param asset: tracking asset issue
        """
        ...

    def remove_stock(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Deprecated
        
        Please use Remove(asset)
        """
        warnings.warn("Please use Remove(asset)", DeprecationWarning)

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...

    def validate_and_compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> QuantConnect.Indicators.IndicatorResult:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class ValueAtRisk(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """This indicator computes 1-day VaR for a specified confidence level and lookback period"""

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when the indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, period: int, confidenceLevel: float) -> None:
        """
        Creates a new ValueAtRisk indicator with a specified period and confidence level
        
        :param name: The name of this indicator
        :param period: Historical lookback period in days
        :param confidenceLevel: Confidence level for VaR calculation
        """
        ...

    @overload
    def __init__(self, period: int, confidenceLevel: float) -> None:
        """
        Creates a new ValueAtRisk indicator with a specified period and confidence level
        
        :param period: Historical lookback period in days
        :param confidenceLevel: Confidence level for VaR calculation
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class CommodityChannelIndex(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional commodity channel index (CCI)
    
    CCI = (Typical Price - 20-period SMA of TP) / (.015 * Mean Deviation)
    Typical Price (TP) = (High + Low + Close)/3
    Constant = 0.015
    
    There are four steps to calculating the Mean Deviation, first, subtract
    the most recent 20-period average of the typical price from each period's
    typical price. Second, take the absolute values of these numbers. Third,
    sum the absolute values. Fourth, divide by the total number of periods (20).
    """

    @property
    def moving_average_type(self) -> QuantConnect.Indicators.MovingAverageType:
        """Gets the type of moving average"""
        ...

    @property
    def typical_price_average(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Keep track of the simple moving average of the typical price"""
        ...

    @property
    def typical_price_mean_deviation(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Keep track of the mean absolute deviation of the typical price"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the CommodityChannelIndex class
        
        :param period: The period of the standard deviation and moving average (middle band)
        :param movingAverageType: The type of moving average to be used
        """
        ...

    @overload
    def __init__(self, name: str, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the CommodityChannelIndex class
        
        :param name: The name of this indicator
        :param period: The period of the standard deviation and moving average (middle band)
        :param movingAverageType: The type of moving average to be used
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RelativeVigorIndexSignal(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """The signal for the Relative Vigor Index, itself an indicator."""

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Resets this indicator to its initial state"""
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RelativeDailyVolume(QuantConnect.Indicators.TradeBarIndicator):
    """
    The Relative Daily Volume indicator is an indicator that compares current
    cumulative volume to the cumulative volume for a given
    time of day, measured as a ratio.
    
    Current volume from open to current time of day / Average over the past x days from open to current time of day
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when the indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, period: int = 2) -> None:
        """
        Initializes a new instance of the RelativeDailyVolume class using the specified period
        
        :param period: The period over which to perform the computation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new RelativeDailyVolume indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period of this indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The input value to this indicator on this time step
        :returns: A a value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class TrueStrengthIndex(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the True Strength Index (TSI).
    The True Strength Index is calculated as explained here:
    https://school.stockcharts.com/doku.php?id=technical_indicators:true_strength_index
    
    Briefly, the calculation has three steps:
      1. Smooth the momentum and the absolute momentum by getting an EMA of them (typically of period 25)
      2. Double smooth the momentum and the absolute momentum by getting an EMA of their EMA (typically of period 13)
      3. The TSI formula itself: divide the double-smoothed momentum over the double-smoothed absolute momentum and multiply by 100
    
    The signal is typically a 7-to-12-EMA of the TSI.
    """

    @property
    def signal(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the signal line for the TSI indicator"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, longTermPeriod: int = 25, shortTermPeriod: int = 13, signalPeriod: int = 7, signalType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the TrueStrengthIndex class using the specified short and long term smoothing periods, and the signal period and type.
        
        :param longTermPeriod: Period used for the second (double) price change smoothing
        :param shortTermPeriod: Period used for the first price change smoothing
        :param signalPeriod: The signal period
        :param signalType: The type of moving average to use for the signal
        """
        ...

    @overload
    def __init__(self, name: str, longTermPeriod: int = 25, shortTermPeriod: int = 13, signalPeriod: int = 7, signalType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the TrueStrengthIndex class using the specified name, the short and long term smoothing periods, and the signal period and type.
        
        :param name: The name of the indicator
        :param longTermPeriod: Period used for the second (double) price change smoothing
        :param shortTermPeriod: Period used for the first price change smoothing
        :param signalPeriod: The signal period
        :param signalType: The type of moving average to use for the signal
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class IntradayVwap(QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.BaseData]):
    """Defines the canonical intraday VWAP indicator"""

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the IntradayVwap class
        
        :param name: The name of the indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.BaseData) -> float:
        """
        Computes the next value of this indicator from the given state.
        NOTE: This must be overriden since it's abstract in the base, but
        will never be invoked since we've override the validate method above.
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def try_get_volume_and_average_price(self, input: QuantConnect.Data.BaseData, volume: typing.Optional[float], average_price: typing.Optional[float]) -> typing.Union[bool, float, float]:
        """
        Determines the volume and price to be used for the current input in the VWAP computation
        
        This method is protected.
        """
        ...

    def validate_and_compute_next_value(self, input: QuantConnect.Data.BaseData) -> QuantConnect.Indicators.IndicatorResult:
        """
        Computes the new VWAP
        
        This method is protected.
        """
        ...


class ZeroLagExponentialMovingAverage(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the zero lag moving average indicator (ZLEMA)
    ie a technical indicator that aims is to eliminate the inherent lag associated to all trend
    following indicators which average a price over time.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the ZeroLagMovingAverage class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the ZLEMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the ZeroLagMovingAverage class with the default name and period
        
        :param period: The period of the ZLEMA
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Vortex(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the Vortex Indicator, which identifies the start and continuation of market trends.
    It includes components that capture positive (upward) and negative (downward) trend movements.
    This indicator compares the ranges within the current period to previous periods to calculate
    upward and downward movement trends.
    """

    @property
    def plus_vortex(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Positive Vortex Indicator, which reflects positive trend movements."""
        ...

    @property
    def minus_vortex(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Negative Vortex Indicator, which reflects negative trend movements."""
        ...

    @property
    def is_ready(self) -> bool:
        """Indicates whether this indicator is fully ready and all buffers have been filled."""
        ...

    @property
    def warm_up_period(self) -> int:
        """The minimum number of samples needed for the indicator to be ready and provide reliable values."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the Vortex class using the specified period.
        
        :param period: The number of periods used to construct the Vortex Indicator.
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the Vortex class with a custom name and period.
        
        :param name: The custom name for this instance of the Vortex Indicator.
        :param period: The number of periods used to construct the Vortex Indicator.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of the Vortex Indicator based on the provided input.
        
        This method is protected.
        
        :param input: The input data used to compute the indicator value.
        :returns: The computed value of the indicator.
        """
        ...

    def reset(self) -> None:
        """Resets all indicators and internal state."""
        ...


class MovingAverageTypeExtensions(System.Object):
    """Provides extension methods for the MovingAverageType enumeration"""

    @staticmethod
    @overload
    def as_indicator(moving_average_type: QuantConnect.Indicators.MovingAverageType, period: int) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Creates a new indicator from the specified MovingAverageType. So if MovingAverageType.Simple
        is specified, then a new SimpleMovingAverage will be returned.
        
        :param moving_average_type: The type of averaging indicator to create
        :param period: The smoothing period
        :returns: A new indicator that matches the MovingAverageType.
        """
        ...

    @staticmethod
    @overload
    def as_indicator(moving_average_type: QuantConnect.Indicators.MovingAverageType, name: str, period: int) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Creates a new indicator from the specified MovingAverageType. So if MovingAverageType.Simple
        is specified, then a new SimpleMovingAverage will be returned.
        
        :param moving_average_type: The type of averaging indicator to create
        :param name: The name of the new indicator
        :param period: The smoothing period
        :returns: A new indicator that matches the MovingAverageType.
        """
        ...


class SuperTrend(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Super trend indicator.
    Formula can be found here via the excel file:
    https://tradingtuitions.com/supertrend-indicator-excel-sheet-with-realtime-buy-sell-signals/
    """

    @property
    def basic_upper_band(self) -> float:
        """Basic Upper Band"""
        ...

    @property
    def basic_lower_band(self) -> float:
        """Basic Lower band"""
        ...

    @property
    def current_trailing_upper_band(self) -> float:
        """Current Trailing Upper Band"""
        ...

    @property
    def current_trailing_lower_band(self) -> float:
        """Current Trailing Lower Band"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, multiplier: float, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new SuperTrend indicator using the specified name, period, multiplier and moving average type
        
        :param name: The name of this indicator
        :param period: The smoothing period used by average true range
        :param multiplier: The coefficient used in calculations of basic upper and lower bands
        :param movingAverageType: The type of smoothing used to smooth the true range values
        """
        ...

    @overload
    def __init__(self, period: int, multiplier: float, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new SuperTrend indicator using the specified period, multiplier and moving average type
        
        :param period: The smoothing period used in average true range
        :param multiplier: The coefficient used in calculations of basic upper and lower bands
        :param movingAverageType: The type of smoothing used to smooth the true range values
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Minimum(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """Represents an indicator capable of tracking the minimum value and how many periods ago it occurred"""

    @property
    def periods_since_minimum(self) -> int:
        """The number of periods since the minimum value was encountered"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new Minimum indicator with the specified period
        
        :param period: The period over which to look back
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new Minimum indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to look back
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """This method is protected."""
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class DeMarkerIndicator(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    In the DeMarker strategy, for some period of size N, set:
    
    DeMax = High - Previous High, and
    DeMin = Previous Low - Low
    
    where, in the prior, if either term is less than zero (DeMax or DeMin), set it to zero.
    We can now define the indicator itself, DEM, as:
    
    DEM = MA(DeMax)/(MA(DeMax)+MA(DeMin))
    
    where MA denotes a Moving Average of period N.
    
    https://www.investopedia.com/terms/d/demarkerindicator.asp
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the DeMarkerIndicator class with the specified period
        
        :param period: The period of the  DeMarker Indicator
        :param type: The type of moving average to use in calculations
        """
        ...

    @overload
    def __init__(self, name: str, period: int, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the DeMarkerIndicator class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the  DeMarker Indicator
        :param type: The type of moving average to use in calculations
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AdvanceDeclineRatio(QuantConnect.Indicators.AdvanceDeclineIndicator):
    """
    The advance-decline ratio (ADR) compares the number of stocks
    that closed higher against the number of stocks
    that closed lower than their previous day's closing prices.
    """

    def __init__(self, name: str) -> None:
        """Initializes a new instance of the AdvanceDeclineRatio class"""
        ...


class AdvanceDeclineVolumeRatio(QuantConnect.Indicators.AdvanceDeclineIndicator):
    """
    The Advance Decline Volume Ratio is a Breadth indicator calculated as ratio of
    summary volume of advancing stocks to summary volume of declining stocks.
    AD Volume Ratio is used in technical analysis to see where the main trading activity is focused.
    """

    def __init__(self, name: str) -> None:
        """Initializes a new instance of the AdvanceDeclineVolumeRatio class"""
        ...


class ArmsIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Arms Index, also called the Short-Term Trading Index (TRIN)
    is a technical analysis indicator that compares the number of advancing
    and declining stocks (AD Ratio) to advancing and declining volume (AD volume).
    """

    @property
    def ad_ratio(self) -> QuantConnect.Indicators.AdvanceDeclineRatio:
        """Gets the Advance/Decline Ratio (ADR) indicator"""
        ...

    @property
    def adv_ratio(self) -> QuantConnect.Indicators.AdvanceDeclineVolumeRatio:
        """Gets the Advance/Decline Volume Ratio (ADVR) indicator"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    def __init__(self, name: str) -> None:
        """Initializes a new instance of the ArmsIndex class"""
        ...

    def add(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Add Tracking stock issue
        
        :param asset: the tracking stock issue
        """
        ...

    def add_stock(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Deprecated
        
        Please use Add(asset)
        """
        warnings.warn("Please use Add(asset)", DeprecationWarning)

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def remove(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Remove Tracking stock issue
        
        :param asset: the tracking stock issue
        """
        ...

    def remove_stock(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Deprecated
        
        Please use Remove(asset)
        """
        warnings.warn("Please use Remove(asset)", DeprecationWarning)

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AugenPriceSpike(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Augen Price Spike indicator is an indicator that measures price
    changes in terms of standard deviations. In the book, The
    Volatility Edge in Options Trading, Jeff Augen describes a
    method for tracking absolute price changes in terms of recent
    volatility, using the standard deviation.
    
    length = x
    closes = closeArray
    closes1 = closeArray shifted right by 1
    closes2 = closeArray shifted right by 2
    closeLog = np.log(np.divide(closes1, closes2))
    SDev = np.std(closeLog)
    m = SDev * closes1[-1]
    spike = (closes[-1]-closes1[-1])/m
    return spike
    
    Augen Price Spike from TradingView
    https://www.tradingview.com/script/fC7Pn2X2-Price-Spike-Jeff-Augen/
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when the indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int = 3) -> None:
        """
        Initializes a new instance of the AugenPriceSpike class using the specified period
        
        :param period: The period over which to perform to computation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new AugenPriceSpike indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period of this indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The input value to this indicator on this time step
        :returns: A a value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RateOfChange(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period rate of change in a value using the following:
    (value_0 - value_n) / value_n
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized."""
        ...

    @property
    def warm_up_period(self) -> int:
        """
        Required period, in data points, for the indicator to be ready and fully initialized.
        Our formula is Period + 1 because we need to fill the window and have one removed before
        it is ready.
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new RateOfChange indicator with the specified period
        
        :param period: The period over which to perform to computation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new RateOfChange indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to perform to computation
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class SharpeRatio(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Calculation of the Sharpe Ratio (SR) developed by William F. Sharpe.
    
    Reference: https://www.investopedia.com/articles/07/sharpe_ratio.asp
    Formula: S(x) = (Rx - Rf) / stdDev(Rx)
    Where:
    S(x) - sharpe ratio of x
    Rx - average rate of return for x
    Rf - risk-free rate
    """

    @property
    def rate_of_change(self) -> QuantConnect.Indicators.RateOfChange:
        """
        RateOfChange indicator for calculating the sharpe ratio
        
        This property is protected.
        """
        ...

    @property
    def risk_free_rate(self) -> QuantConnect.Indicators.Identity:
        """
        RiskFreeRate indicator for calculating the sharpe ratio
        
        This property is protected.
        """
        ...

    @property
    def ratio(self) -> QuantConnect.Indicators.IndicatorBase:
        """
        Indicator to store the calculation of the sharpe ratio
        
        This property is protected.
        """
        ...

    @property.setter
    def ratio(self, value: QuantConnect.Indicators.IndicatorBase) -> None:
        ...

    @property
    def numerator(self) -> QuantConnect.Indicators.IndicatorBase:
        """
        Indicator to store the numerator of the Sharpe ratio calculation
        
        This property is protected.
        """
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Returns whether the indicator is properly initialized with data"""
        ...

    @overload
    def __init__(self, name: str, period: int, riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel) -> None:
        """
        Creates a new Sharpe Ratio indicator using the specified periods
        
        :param name: The name of this indicator
        :param period: Period of historical observation for sharpe ratio calculation
        :param riskFreeRateModel: Risk-free rate model
        """
        ...

    @overload
    def __init__(self, period: int, riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel) -> None:
        """
        Creates a new Sharpe Ratio indicator using the specified periods
        
        :param period: Period of historical observation for sharpe ratio calculation
        :param riskFreeRateModel: Risk-free rate model
        """
        ...

    @overload
    def __init__(self, name: str, period: int, riskFreeRateModel: typing.Any) -> None:
        """
        Creates a new Sharpe Ratio indicator using the specified period using a Python risk free rate model
        
        :param period: Period of historical observation for sharpe ratio calculation
        :param riskFreeRateModel: Risk-free rate model
        """
        ...

    @overload
    def __init__(self, period: int, riskFreeRateModel: typing.Any) -> None:
        """
        Creates a new Sharpe Ratio indicator using the specified period using a Python risk free rate model
        
        :param period: Period of historical observation for sharpe ratio calculation
        :param riskFreeRateModel: Risk-free rate model
        """
        ...

    @overload
    def __init__(self, name: str, period: int, riskFreeRate: float = 0.0) -> None:
        """
        Creates a new Sharpe Ratio indicator using the specified periods
        
        :param name: The name of this indicator
        :param period: Period of historical observation for sharpe ratio calculation
        :param riskFreeRate: Risk-free rate for sharpe ratio calculation
        """
        ...

    @overload
    def __init__(self, period: int, riskFreeRate: float = 0.0) -> None:
        """
        Creates a new SharpeRatio indicator using the specified periods
        
        :param period: Period of historical observation for sharpe ratio calculation
        :param riskFreeRate: Risk-free rate for sharpe ratio calculation
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class SortinoRatio(QuantConnect.Indicators.SharpeRatio):
    """
    Calculation of the Sortino Ratio, a modification of the SharpeRatio.
    
    Reference: https://www.cmegroup.com/education/files/rr-sortino-a-sharper-ratio.pdf
    Formula: S(x) = (R - T) / TDD
    Where:
    S(x) - Sortino ratio of x
    R - the average period return
    T - the target or required rate of return for the investment strategy under consideration. In
    Sortino’s early work, T was originally known as the minimum acceptable return, or MAR. In his
    more recent work, MAR is now referred to as the Desired Target Return.
    TDD - the target downside deviation. TargetDownsideDeviation
    """

    @overload
    def __init__(self, name: str, period: int, minimumAcceptableReturn: float = 0) -> None:
        """
        Creates a new Sortino Ratio indicator using the specified periods
        
        :param name: The name of this indicator
        :param period: Period of historical observation for Sortino ratio calculation
        :param minimumAcceptableReturn: Minimum acceptable return for Sortino ratio calculation
        """
        ...

    @overload
    def __init__(self, period: int, minimumAcceptableReturn: float = 0) -> None:
        """
        Creates a new SortinoRatio indicator using the specified periods
        
        :param period: Period of historical observation for Sortino ratio calculation
        :param minimumAcceptableReturn: Minimum acceptable return for Sortino ratio calculation
        """
        ...


class ChandeMomentumOscillator(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Chande Momentum Oscillator (CMO).
    CMO calculation is mostly identical to RSI.
    The only difference is in the last step of calculation:
    RSI = gain / (gain+loss)
    CMO = (gain-loss) / (gain+loss)
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the ChandeMomentumOscillator class using the specified period.
        
        :param period: The period of the indicator
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the ChandeMomentumOscillator class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the indicator
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ExponentialMovingAverage(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional exponential moving average indicator (EMA).
    When the indicator is ready, the first value of the EMA is equivalent to the simple moving average.
    After the first EMA value, the EMA value is a function of the previous EMA value.
    Therefore, depending on the number of samples
    you feed into the indicator, it can provide different EMA values for a single
    security and lookback period. To make the indicator values consistent
    across time, warm up the indicator with all the trailing security price history.
    """

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the ExponentialMovingAverage class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the EMA
        """
        ...

    @overload
    def __init__(self, name: str, period: int, smoothingFactor: float) -> None:
        """
        Initializes a new instance of the ExponentialMovingAverage class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the EMA
        :param smoothingFactor: The percentage of data from the previous value to be carried into the next value
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the ExponentialMovingAverage class with the default name and period
        
        :param period: The period of the EMA
        """
        ...

    @overload
    def __init__(self, period: int, smoothingFactor: float) -> None:
        """
        Initializes a new instance of the ExponentialMovingAverage class with the default name and period
        
        :param period: The period of the EMA
        :param smoothingFactor: The percentage of data from the previous value to be carried into the next value
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...

    @staticmethod
    def smoothing_factor_default(period: int) -> float:
        """
        Calculates the default smoothing factor for an ExponentialMovingAverage indicator
        
        :param period: The period of the EMA
        :returns: The default smoothing factor.
        """
        ...


class IndicatorExtensions(System.Object):
    """Provides extension methods for Indicator"""

    @staticmethod
    @overload
    def ema(left: QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_IndicatorExtensions_EMA_T], period: int, smoothing_factor: typing.Optional[float] = None, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.ExponentialMovingAverage:
        """
        Creates a new ExponentialMovingAverage indicator with the specified period and smoothing_factor from the left indicator
        
        :param left: The ExponentialMovingAverage indicator will be created using the data from left
        :param period: The period of the ExponentialMovingAverage indicators
        :param smoothing_factor: The percentage of data from the previous value to be carried into the next value
        :param wait_for_first_to_ready: True to only send updates to the second if left.IsReady returns true, false to always send updates
        :returns: A reference to the ExponentialMovingAverage indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def ema(left: typing.Any, period: int, smoothing_factor: typing.Optional[float] = None, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.ExponentialMovingAverage:
        """
        Creates a new ExponentialMovingAverage indicator with the specified period and smoothing_factor from the left indicator
        
        :param left: The ExponentialMovingAverage indicator will be created using the data from left
        :param period: The period of the ExponentialMovingAverage indicators
        :param smoothing_factor: The percentage of data from the previous value to be carried into the next value
        :param wait_for_first_to_ready: True to only send updates to the second if left.IsReady returns true, false to always send updates
        :returns: A reference to the ExponentialMovingAverage indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def max(left: QuantConnect.Indicators.IIndicator, period: int, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.Maximum:
        """
        Creates a new Maximum indicator with the specified period from the left indicator
        
        :param left: The Maximum indicator will be created using the data from left
        :param period: The period of the Maximum indicator
        :param wait_for_first_to_ready: True to only send updates to the second if left.IsReady returns true, false to always send updates
        :returns: A reference to the Maximum indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def max(left: typing.Any, period: int, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.Maximum:
        """
        Creates a new Maximum indicator with the specified period from the left indicator
        
        :param left: The Maximum indicator will be created using the data from left
        :param period: The period of the Maximum indicator
        :param wait_for_first_to_ready: True to only send updates to the second if left.IsReady returns true, false to always send updates
        :returns: A reference to the Maximum indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def min(left: QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_IndicatorExtensions_MIN_T], period: int, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.Minimum:
        """
        Creates a new Minimum indicator with the specified period from the left indicator
        
        :param left: The Minimum indicator will be created using the data from left
        :param period: The period of the Minimum indicator
        :param wait_for_first_to_ready: True to only send updates to the second if left.IsReady returns true, false to always send updates
        :returns: A reference to the Minimum indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def min(left: typing.Any, period: int, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.Minimum:
        """
        Creates a new Minimum indicator with the specified period from the left indicator
        
        :param left: The Minimum indicator will be created using the data from left
        :param period: The period of the Minimum indicator
        :param wait_for_first_to_ready: True to only send updates to the second if left.IsReady returns true, false to always send updates
        :returns: A reference to the Minimum indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def minus(left: QuantConnect.Indicators.IndicatorBase, constant: float) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the difference of the left and constant
        
        :param left: The left indicator
        :param constant: The subtrahend
        :returns: The difference of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def minus(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the difference of the left and right
        
        :param left: The left indicator
        :param right: The right indicator
        :returns: The difference of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def minus(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, name: str) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the difference of the left and right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The difference of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def minus(left: typing.Any, constant: float) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the difference of the left and constant
        
        :param left: The left indicator
        :param constant: The subtrahend
        :returns: The difference of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def minus(left: typing.Any, right: typing.Any, name: str = ...) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the difference of the left and right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The difference of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def of(second: QuantConnect_Indicators_IndicatorExtensions_Of_T, first: QuantConnect.Indicators.IIndicator, wait_for_first_to_ready: bool = True) -> QuantConnect_Indicators_IndicatorExtensions_Of_T:
        """
        Configures the second indicator to receive automatic updates from the first by attaching an event handler
        to first.DataConsolidated
        
        :param second: The indicator that receives data from the first
        :param first: The indicator that sends data via DataConsolidated even to the second
        :param wait_for_first_to_ready: True to only send updates to the second if first.IsReady returns true, false to always send updates to second
        :returns: The reference to the second indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def of(second: typing.Any, first: typing.Any, wait_for_first_to_ready: bool = True) -> System.Object:
        """
        Configures the second indicator to receive automatic updates from the first by attaching an event handler
        to first.DataConsolidated
        
        :param second: The indicator that receives data from the first
        :param first: The indicator that sends data via DataConsolidated even to the second
        :param wait_for_first_to_ready: True to only send updates to the second if first.IsReady returns true, false to always send updates to second
        :returns: The reference to the second indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def over(left: QuantConnect.Indicators.IndicatorBase, constant: float) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the ratio of the left to the constant
        
        :param left: The left indicator
        :param constant: The constant value denominator
        :returns: The ratio of the left to the right indicator.
        """
        ...

    @staticmethod
    @overload
    def over(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the ratio of the left to the right
        
        :param left: The left indicator
        :param right: The right indicator
        :returns: The ratio of the left to the right indicator.
        """
        ...

    @staticmethod
    @overload
    def over(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, name: str) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the ratio of the left to the right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The ratio of the left to the right indicator.
        """
        ...

    @staticmethod
    @overload
    def over(left: typing.Any, constant: float) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the ratio of the left to the constant
        
        :param left: The left indicator
        :param constant: The constant value denominator
        :returns: The ratio of the left to the right indicator.
        """
        ...

    @staticmethod
    @overload
    def over(left: typing.Any, right: typing.Any, name: str = ...) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the ratio of the left to the right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The ratio of the left to the right indicator.
        """
        ...

    @staticmethod
    @overload
    def plus(left: QuantConnect.Indicators.IndicatorBase, constant: float) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the sum of the left and the constant
        
        :param left: The left indicator
        :param constant: The addend
        :returns: The sum of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def plus(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the sum of the left and right
        
        :param left: The left indicator
        :param right: The right indicator
        :returns: The sum of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def plus(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, name: str) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the sum of the left and right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The sum of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def plus(left: typing.Any, constant: float) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the sum of the left and the constant
        
        :param left: The left indicator
        :param constant: The addend
        :returns: The sum of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def plus(left: typing.Any, right: typing.Any, name: str = ...) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the sum of the left and right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The sum of the left and right indicators.
        """
        ...

    @staticmethod
    @overload
    def sma(left: QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_IndicatorExtensions_SMA_T], period: int, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.SimpleMovingAverage:
        """
        Initializes a new instance of the SimpleMovingAverage class with the specified name and period from the left indicator
        
        :param left: The SimpleMovingAverage indicator will be created using the data from left
        :param period: The period of the SMA
        :param wait_for_first_to_ready: True to only send updates to the second if first.IsReady returns true, false to always send updates to second
        :returns: The reference to the SimpleMovingAverage indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def sma(left: typing.Any, period: int, wait_for_first_to_ready: bool = True) -> QuantConnect.Indicators.SimpleMovingAverage:
        """
        Initializes a new instance of the SimpleMovingAverage class with the specified name and period from the left indicator
        
        :param left: The SimpleMovingAverage indicator will be created using the data from left
        :param period: The period of the SMA
        :param wait_for_first_to_ready: True to only send updates to the second if first.IsReady returns true, false to always send updates to second
        :returns: The reference to the SimpleMovingAverage indicator to allow for method chaining.
        """
        ...

    @staticmethod
    @overload
    def times(left: QuantConnect.Indicators.IndicatorBase, constant: float) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the product of the left and the constant
        
        :param left: The left indicator
        :param constant: The constant value to multiple by
        :returns: The product of the left to the right indicators.
        """
        ...

    @staticmethod
    @overload
    def times(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the product of the left to the right
        
        :param left: The left indicator
        :param right: The right indicator
        :returns: The product of the left to the right indicators.
        """
        ...

    @staticmethod
    @overload
    def times(left: QuantConnect.Indicators.IndicatorBase, right: QuantConnect.Indicators.IndicatorBase, name: str) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be the product of the left to the right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The product of the left to the right indicators.
        """
        ...

    @staticmethod
    @overload
    def times(left: typing.Any, constant: float) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the product of the left and the constant
        
        :param left: The left indicator
        :param constant: The constant value to multiple by
        :returns: The product of the left to the right indicators.
        """
        ...

    @staticmethod
    @overload
    def times(left: typing.Any, right: typing.Any, name: str = ...) -> System.Object:
        """
        Creates a new CompositeIndicator such that the result will be the product of the left to the right
        
        :param left: The left indicator
        :param right: The right indicator
        :param name: The name of this indicator
        :returns: The product of the left to the right indicators.
        """
        ...

    @staticmethod
    def update(indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], time: typing.Union[datetime.datetime, datetime.date], value: float) -> bool:
        """
        Updates the state of this indicator with the given value and returns true
        if this indicator is ready, false otherwise
        
        :param indicator: The indicator to be updated
        :param time: The time associated with the value
        :param value: The value to use to update this indicator
        :returns: True if this indicator is ready, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def weighted_by(value: QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_IndicatorExtensions_WeightedBy_T], weight: QuantConnect_Indicators_IndicatorExtensions_WeightedBy_TWeight, period: int) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be average of a first indicator weighted by a second one
        
        :param value: Indicator that will be averaged
        :param weight: Indicator that provides the average weights
        :param period: Average period
        :returns: Indicator that results of the average of first by weights given by second.
        """
        ...

    @staticmethod
    @overload
    def weighted_by(value: typing.Any, weight: typing.Any, period: int) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Creates a new CompositeIndicator such that the result will be average of a first indicator weighted by a second one
        
        :param value: Indicator that will be averaged
        :param weight: Indicator that provides the average weights
        :param period: Average period
        :returns: Indicator that results of the average of first by weights given by second.
        """
        ...


class TrueRange(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the True Range (TR).
    The True Range is the greatest of the following values:
    value1 = distance from today's high to today's low.
    value2 = distance from yesterday's close to today's high.
    value3 = distance from yesterday's close to today's low.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the TrueRange class using the specified name."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the TrueRange class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class ForceIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Force Index is calculated by comparing the current market price with the previous market price
    and multiplying its difference with the traded volume during a specific time period.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new ForceIndex indicator using the specified period and moving average type
        
        :param name: The name of this indicator
        :param period: The smoothing period used to smooth the instantaneous force index values
        :param movingAverageType: The type of smoothing used to smooth the true range values
        """
        ...

    @overload
    def __init__(self, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new ForceIndex indicator using the specified period and moving average type
        
        :param period: The smoothing period used to smooth the instantenous force index values
        :param movingAverageType: The type of smoothing used to smooth the instantenous force index values
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RelativeMovingAverage(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the relative moving average indicator (RMA).
    RMA = SMA(3 x Period) - SMA(2 x Period) + SMA(1 x Period) per formula:
    https://www.hybrid-solutions.com/plugins/client-vtl-plugins/free/rma.html
    """

    @property
    def short_average(self) -> QuantConnect.Indicators.SimpleMovingAverage:
        """Gets the Short Term SMA with 1 x Period of RMA"""
        ...

    @property
    def medium_average(self) -> QuantConnect.Indicators.SimpleMovingAverage:
        """Gets the Medium Term SMA with 2 x Period of RMA"""
        ...

    @property
    def long_average(self) -> QuantConnect.Indicators.SimpleMovingAverage:
        """Gets the Long Term SMA with 3 x Period of RMA"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the RelativeMovingAverage class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the RMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """Initializes a new instance of the SimpleMovingAverage class with the default name and period"""
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Copmutes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RateOfChangePercent(QuantConnect.Indicators.RateOfChange):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:
    100 * (value_0 - value_n) / value_n
    """

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new RateOfChangePercent indicator with the specified period
        
        :param period: The period over which to perform to computation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new RateOfChangePercent indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to perform to computation
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class MomentumPercent(QuantConnect.Indicators.RateOfChangePercent):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:
    100 * (value_0 - value_n) / value_n
    
    This indicator yields the same results of RateOfChangePercent
    """

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new MomentumPercent indicator with the specified period
        
        :param period: The period over which to perform to computation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new MomentumPercent indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to perform to computation
        """
        ...


class OptionGreeksIndicatorBase(QuantConnect.Indicators.OptionIndicatorBase, metaclass=abc.ABCMeta):
    """To provide a base class for option greeks indicator"""

    @property
    def implied_volatility(self) -> QuantConnect.Indicators.ImpliedVolatility:
        """Gets the implied volatility of the option"""
        ...

    @property.setter
    def implied_volatility(self, value: QuantConnect.Indicators.ImpliedVolatility) -> None:
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the OptionGreeksIndicatorBase class
        
        This method is protected.
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate the Greek
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the OptionGreeksIndicatorBase class
        
        This method is protected.
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate the Greek
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the OptionGreeksIndicatorBase class
        
        This method is protected.
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate the Greek
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the OptionGreeksIndicatorBase class
        
        This method is protected.
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate the Greek
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the OptionGreeksIndicatorBase class
        
        This method is protected.
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate the Greek
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    def calculate_greek(self, time_till_expiry: float) -> float:
        """
        Calculate the greek of the option
        
        This method is protected.
        """
        ...

    def compute_indicator(self) -> float:
        """
        Computes the next value of the option greek indicator
        
        This method is protected.
        
        :returns: The input is returned unmodified.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and all sub-indicators"""
        ...


class Delta(QuantConnect.Indicators.OptionGreeksIndicatorBase):
    """Option Delta indicator that calculate the delta of an option"""

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Delta class
        
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Delta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    def calculate_greek(self, time_till_expiry: float) -> float:
        """
        Calculate the Delta of the option
        
        This method is protected.
        """
        ...


class ConstantIndicator(typing.Generic[QuantConnect_Indicators_ConstantIndicator_T], QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_ConstantIndicator_T]):
    """An indicator that will always return the same value."""

    @property
    def is_ready(self) -> bool:
        """Gets true since the ConstantIndicator is always ready to return the same value"""
        ...

    def __init__(self, name: str, value: float) -> None:
        """
        Creates a new ConstantIndicator that will always return the specified value
        
        :param name: The name of this indicator
        :param value: The constant value to be returned
        """
        ...

    def compute_next_value(self, input: QuantConnect_Indicators_ConstantIndicator_T) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class FisherTransform(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Fisher transform is a mathematical process which is used to convert any data set to a modified
    data set whose Probability Distribution Function is approximately Gaussian. Once the Fisher transform
    is computed, the transformed data can then be analyzed in terms of it's deviation from the mean.
    
    The equation is y = .5 * ln [ 1 + x / 1 - x ] where
    x is the input
    y is the output
    ln is the natural logarithm
    
    The Fisher transform has much sharper turning points than other indicators such as MACD
    
    For more info, read chapter 1 of Cybernetic Analysis for Stocks and Futures by John F. Ehlers
    
    We are implementing the latest version of this indicator found at Fig. 4 of
    http://www.mesasoftware.com/papers/UsingTheFisherTransform.pdf
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the FisherTransform class with the default name and period
        
        :param period: The period of the WMA
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        A Fisher Transform of Prices
        
        :param name: string - the name of the indicator
        :param period: The number of periods for the indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value in the transform.
        value1 is a function used to normalize price withing the last _period day range.
        value1 is centered on its midpoint and then doubled so that value1 wil swing between -1 and +1.
        value1 is also smoothed with an exponential moving average whose alpha is 0.33.
        
        Since the smoothing may allow value1 to exceed the _period day price range, limits are introduced to
        preclude the transform from blowing up by having an input larger than unity.
        
        This method is protected.
        
        :param input: IndicatorDataPoint - the time and value of the next price
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Momentum(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period change in a value using the following:
    value_0 - value_n
    """

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new Momentum indicator with the specified period
        
        :param period: The period over which to perform to computation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new Momentum indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to perform to computation
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class PythonIndicator(QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.IBaseData], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """Provides a wrapper for IndicatorBase{IBaseData} implementations written in python"""

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the PythonIndicator class using the specified name."""
        ...

    @overload
    def __init__(self, *args: PyObject) -> None:
        """Initializes a new instance of the PythonIndicator class using the specified name."""
        ...

    @overload
    def __init__(self, indicator: typing.Any) -> None:
        """
        Initializes a new instance of the PythonIndicator class using the specified name.
        
        :param indicator: The python implementation of IndicatorBase{IBaseDataBar}
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.IBaseData) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def set_indicator(self, indicator: typing.Any) -> None:
        """
        Sets the python implementation of the indicator
        
        :param indicator: The python implementation of IndicatorBase{IBaseDataBar}
        """
        ...


class Alpha(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    In financial analysis, the Alpha indicator is used to measure the performance of an investment (such as a stock or ETF)
    relative to a benchmark index, often representing the broader market. Alpha indicates the excess return of the investment
    compared to the return of the benchmark index.
    
    The S P 500 index is frequently used as a benchmark in Alpha calculations to represent the overall market performance.
    Alpha is an essential tool for investors to understand the idiosyncratic returns of their investment that aren't caused
    by movement in the underlying benchmark.
    """

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when the indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], alphaPeriod: int, betaPeriod: int, riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel) -> None:
        """
        Creates a new Alpha indicator with the specified name, target, reference, and period values
        
        :param name: The name of this indicator
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param alphaPeriod: Period of the indicator - alpha
        :param betaPeriod: Period of the indicator - beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], alphaPeriod: int, betaPeriod: int, riskFreeRate: typing.Optional[float] = None) -> None:
        """
        Creates a new Alpha indicator with the specified name, target, reference, and period values
        
        :param name: The name of this indicator
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param alphaPeriod: Period of the indicator - alpha
        :param betaPeriod: Period of the indicator - beta
        :param riskFreeRate: The risk free rate of this indicator for given period
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], alphaPeriod: int, betaPeriod: int, riskFreeRate: typing.Optional[float] = None) -> None:
        """
        Creates a new Alpha indicator with the specified target, reference, and period values
        
        :param alphaPeriod: Period of the indicator - alpha
        :param betaPeriod: Period of the indicator - beta
        :param riskFreeRate: The risk free rate of this indicator for given period
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, riskFreeRate: typing.Optional[float] = None) -> None:
        """
        Creates a new Alpha indicator with the specified target, reference, and period value
        
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param period: Period of the indicator - alpha and beta
        :param riskFreeRate: The risk free rate of this indicator for given period
        """
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, riskFreeRate: typing.Optional[float] = None) -> None:
        """
        Creates a new Alpha indicator with the specified name, target, reference, and period value
        
        :param period: Period of the indicator - alpha and beta
        :param riskFreeRate: The risk free rate of this indicator for given period
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], alphaPeriod: int, betaPeriod: int, riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel) -> None:
        """
        Creates a new Alpha indicator with the specified target, reference, and period values
        
        :param alphaPeriod: Period of the indicator - alpha
        :param betaPeriod: Period of the indicator - beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel) -> None:
        """
        Creates a new Alpha indicator with the specified target, reference, and period value
        
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param period: Period of the indicator - alpha and beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel) -> None:
        """
        Creates a new Alpha indicator with the specified name, target, reference, and period value
        
        :param period: Period of the indicator - alpha and beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], alphaPeriod: int, betaPeriod: int, riskFreeRateModel: typing.Any) -> None:
        """
        Creates a new Alpha indicator with the specified name, target, reference, and period values
        
        :param name: The name of this indicator
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param alphaPeriod: Period of the indicator - alpha
        :param betaPeriod: Period of the indicator - beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], alphaPeriod: int, betaPeriod: int, riskFreeRateModel: typing.Any) -> None:
        """
        Creates a new Alpha indicator with the specified target, reference, and period values
        
        :param alphaPeriod: Period of the indicator - alpha
        :param betaPeriod: Period of the indicator - beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, riskFreeRateModel: typing.Any) -> None:
        """
        Creates a new Alpha indicator with the specified target, reference, and period value
        
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param period: Period of the indicator - alpha and beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, riskFreeRateModel: typing.Any) -> None:
        """
        Creates a new Alpha indicator with the specified name, target, reference, and period value
        
        :param period: Period of the indicator - alpha and beta
        :param riskFreeRateModel: The risk free rate model of this indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ParabolicStopAndReverse(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Parabolic SAR Indicator
    Based on TA-Lib implementation
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, afStart: float = 0.02, afIncrement: float = 0.02, afMax: float = 0.2) -> None:
        """
        Create new Parabolic SAR
        
        :param name: The name of this indicator
        :param afStart: Acceleration factor start value
        :param afIncrement: Acceleration factor increment value
        :param afMax: Acceleration factor max value
        """
        ...

    @overload
    def __init__(self, afStart: float = 0.02, afIncrement: float = 0.02, afMax: float = 0.2) -> None:
        """
        Create new Parabolic SAR
        
        :param afStart: Acceleration factor start value
        :param afIncrement: Acceleration factor increment value
        :param afMax: Acceleration factor max value
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The trade bar input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ArnaudLegouxMovingAverage(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Smooth and high sensitive moving Average. This moving average reduce lag of the information
    but still being smooth to reduce noises.
    Is a weighted moving average, which weights have a Normal shape;
    the parameters Sigma and Offset affect the kurtosis and skewness of the weights respectively.
    Source: https://www.cjournal.cz/files/308.pdf
    """

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, sigma: int = 6, offset: float = 0.85) -> None:
        """
        Initializes a new instance of the ArnaudLegouxMovingAverage class.
        
        :param name: string - a name for the indicator
        :param period: int - the number of periods to calculate the ALMA
        :param sigma: int - this parameter is responsible for the shape of the curve coefficients. It affects the weight vector kurtosis.
        :param offset: decimal - This parameter allows regulating the smoothness and high sensitivity of the Moving Average. The range for this parameter is [0, 1]. It affects the weight vector skewness.
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the ArnaudLegouxMovingAverage class.
        
        :param name: string - a name for the indicator
        :param period: int - the number of periods to calculate the ALMA.
        """
        ...

    @overload
    def __init__(self, period: int, sigma: int, offset: float = 0.85) -> None:
        """
        Initializes a new instance of the ArnaudLegouxMovingAverage class.
        
        :param period: int - the number of periods to calculate the ALMA
        :param sigma: int - this parameter is responsible for the shape of the curve coefficients. It affects the weight vector kurtosis.
        :param offset: decimal -  This parameter allows regulating the smoothness and high sensitivity of the Moving Average. The range for this parameter is [0, 1]. It affects the weight vector skewness.
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the ArnaudLegouxMovingAverage class.
        
        :param period: int - the number of periods to calculate the ALMA.
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class HeikinAshi(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Heikin-Ashi bar (HA)
    The Heikin-Ashi bar is calculated using the following formulas:
    HA_Close[0] = (Open[0] + High[0] + Low[0] + Close[0]) / 4
    HA_Open[0] = (HA_Open[1] + HA_Close[1]) / 2
    HA_High[0] = MAX(High[0], HA_Open[0], HA_Close[0])
    HA_Low[0] = MIN(Low[0], HA_Open[0], HA_Close[0])
    """

    @property
    def open(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Heikin-Ashi Open"""
        ...

    @property
    def high(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Heikin-Ashi High"""
        ...

    @property
    def low(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Heikin-Ashi Low"""
        ...

    @property
    def close(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Heikin-Ashi Close"""
        ...

    @property
    def volume(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Heikin-Ashi Volume"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the HeikinAshi class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the HeikinAshi class."""
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class SchaffTrendCycle(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """This indicator creates the Schaff Trend Cycle"""

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, cyclePeriod: int = 10, fastPeriod: int = 23, slowPeriod: int = 50, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates the name string and calls on the indicator constructor with given parameters
        https://www.tradingpedia.com/forex-trading-indicators/schaff-trend-cycle
        
        :param cyclePeriod: The signal period
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param type: The type of moving averages to use
        """
        ...

    @overload
    def __init__(self, name: str, cyclePeriod: int, fastPeriod: int, slowPeriod: int, type: QuantConnect.Indicators.MovingAverageType) -> None:
        """
        Creates a new schaff trend cycle with the specified parameters
        
        :param name: The name of this indicator
        :param cyclePeriod: The signal period
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param type: The type of moving averages to use
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MassIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Mass Index uses the high-low range to identify trend reversals based on range expansions.
    In this sense, the Mass Index is a volatility indicator that does not have a directional
    bias. Instead, the Mass Index identifies range bulges that can foreshadow a reversal of the
    current trend. Developed by Donald Dorsey.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, emaPeriod: int, sumPeriod: int) -> None:
        """
        Initializes a new instance of the MassIndex class.
        
        :param name: The name for this instance.
        :param emaPeriod: The period used by both EMA.
        :param sumPeriod: The sum period.
        """
        ...

    @overload
    def __init__(self, emaPeriod: int = 9, sumPeriod: int = 25) -> None:
        """
        Initializes a new instance of the MassIndex class.
        
        :param emaPeriod: The period used by both EMA.
        :param sumPeriod: The sum period.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class WilliamsPercentR(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Williams %R, or just %R, is the current closing price in relation to the high and low of
    the past N days (for a given N). The value of this indicator fluctuates between -100 and 0.
    The symbol is said to be oversold when the oscillator is below -80%,
    and overbought when the oscillator is above -20%.
    """

    @property
    def maximum(self) -> QuantConnect.Indicators.Maximum:
        """Gets the Maximum indicator"""
        ...

    @property
    def minimum(self) -> QuantConnect.Indicators.Minimum:
        """Gets the Minimum indicator"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new Williams %R.
        
        :param period: The look-back period to determine the Williams %R
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new Williams %R.
        
        :param name: The name of this indicator
        :param period: The look-back period to determine the Williams %R
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and both sub-indicators (Max and Min)"""
        ...


class MidPrice(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPrice (MIDPRICE).
    The MidPrice is calculated using the following formula:
    MIDPRICE = (Highest High + Lowest Low) / 2
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the MidPrice class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the MIDPRICE
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the MidPrice class using the specified period.
        
        :param period: The period of the MIDPRICE
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class MarketProfile(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider, metaclass=abc.ABCMeta):
    """
    Represents an Indicator of the Market Profile and its attributes
    
    The concept of Market Profile stems from the idea that
    markets have a form of organization determined by time,
    price, and volume.Each day, the market will develop a range
    for the day and a value area, which represents an equilibrium
    point where there are an equal number of buyers and sellers.
    In this area, prices never stay stagnant. They are constantly
    diverging, and Market Profile records this activity for traders
    to interpret.
    
    It can be computed in two modes: TPO (Time Price Opportunity) or VOL (Volume Profile)
    A discussion on the difference between TPO (Time Price Opportunity)
    and VOL (Volume Profile) chart types: https://jimdaltontrading.com/tpo-vs-volume-profile
    """

    @property
    def volume_per_price(self) -> System.Collections.Generic.SortedList[float, float]:
        """Get a copy of the _volumePerPrice field"""
        ...

    @property
    def profile_high(self) -> float:
        """
        The highest reached close price level during the period.
        That value is called Profile High
        """
        ...

    @property
    def profile_low(self) -> float:
        """
        The lowest reached close price level during the period.
        That value is called Profile Low
        """
        ...

    @property
    def poc_price(self) -> float:
        """
        Price where the most trading occured (Point of Control(POC))
        This price is MarketProfile.Current.Value
        """
        ...

    @property
    def poc_volume(self) -> float:
        """Volume where the most tradding occured (Point of Control(POC))"""
        ...

    @property
    def value_area_volume(self) -> float:
        """
        The range of price levels in which a specified percentage of all volume
        was traded during the time period. Typically, this percentage is set
        to 70% however it is up to the trader’s discretion.
        """
        ...

    @property
    def value_area_high(self) -> float:
        """The highest close price level within the value area"""
        ...

    @property
    def value_area_low(self) -> float:
        """The lowest close price level within the value area"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when the indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    def __init__(self, name: str, period: int, valueAreaVolumePercentage: float = 0.70, priceRangeRoundOff: float = 0.05) -> None:
        """
        Creates a new MarkProfile indicator with the specified period
        
        This method is protected.
        
        :param name: The name of this indicator
        :param period: The period of this indicator
        :param valueAreaVolumePercentage: The percentage of volume contained in the value area
        :param priceRangeRoundOff: How many digits you want to round and the precision. i.e 0.01 round to two digits exactly. 0.05 by default.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The input value to this indicator on this time step
        :returns: A a value for this indicator, Point of Control (POC) price.
        """
        ...

    def get_volume(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Get the Volume value that's going to be used
        
        This method is protected.
        
        :param input: Data
        :returns: The Volume value it's going to be used.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ChoppinessIndex(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The ChoppinessIndex indicator is an indicator designed to determine if the market is choppy (trading sideways)
    or not choppy (trading within a trend in either direction)
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new ChoppinessIndex indicator using the specified period and moving average type
        
        :param name: The name of this indicator
        :param period: The period used for rolling windows for highs and lows
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new ChoppinessIndex indicator using the specified period
        
        :param period: The period used for rolling windows for highs and lows
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AccumulationDistributionOscillator(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Accumulation/Distribution Oscillator (ADOSC)
    The Accumulation/Distribution Oscillator is calculated using the following formula:
    ADOSC = EMA(fast,AD) - EMA(slow,AD)
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, fastPeriod: int, slowPeriod: int) -> None:
        """
        Initializes a new instance of the AccumulationDistributionOscillator class using the specified parameters
        
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        """
        ...

    @overload
    def __init__(self, name: str, fastPeriod: int, slowPeriod: int) -> None:
        """
        Initializes a new instance of the AccumulationDistributionOscillator class using the specified parameters
        
        :param name: The name of this indicator
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RateOfChangeRatio(QuantConnect.Indicators.RateOfChange):
    """
    This indicator computes the Rate Of Change Ratio (ROCR).
    The Rate Of Change Ratio is calculated with the following formula:
    ROCR = price / prevPrice
    """

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the RateOfChangeRatio class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the ROCR
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the RateOfChangeRatio class using the specified period.
        
        :param period: The period of the ROCR
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class UltimateOscillator(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ultimate Oscillator (ULTOSC)
    The Ultimate Oscillator is calculated as explained here:
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ultimate_oscillator
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period1: int, period2: int, period3: int) -> None:
        """
        Initializes a new instance of the UltimateOscillator class using the specified parameters
        
        :param period1: The first period
        :param period2: The second period
        :param period3: The third period
        """
        ...

    @overload
    def __init__(self, name: str, period1: int, period2: int, period3: int) -> None:
        """
        Initializes a new instance of the UltimateOscillator class using the specified parameters
        
        :param name: The name of this indicator
        :param period1: The first period
        :param period2: The second period
        :param period3: The third period
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class LeastSquaresMovingAverage(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Least Squares Moving Average (LSMA) first calculates a least squares regression line
    over the preceding time periods, and then projects it forward to the current period. In
    essence, it calculates what the value would be if the regression line continued.
    Source: https://rtmath.net/assets/docs/finanalysis/html/b3fab79c-f4b2-40fb-8709-fdba43cdb363.htm
    """

    @property
    def intercept(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The point where the regression line crosses the y-axis (price-axis)"""
        ...

    @property
    def slope(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The regression line slope"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the LeastSquaresMovingAverage class.
        
        :param name: The name of this indicator
        :param period: The number of data points to hold in the window
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the LeastSquaresMovingAverage class.
        
        :param period: The number of data points to hold in the window.
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and all sub-indicators (Intercept, Slope)"""
        ...


class RegressionChannel(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Regression Channel indicator extends the LeastSquaresMovingAverage
    with the inclusion of two (upper and lower) channel lines that are distanced from
    the linear regression line by a user defined number of standard deviations.
    Reference: http://www.onlinetradingconcepts.com/TechnicalAnalysis/LinRegChannel.html
    """

    @property
    def linear_regression(self) -> QuantConnect.Indicators.LeastSquaresMovingAverage:
        """Gets the linear regression"""
        ...

    @property
    def upper_channel(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the upper channel (linear regression + k * stdDev)"""
        ...

    @property
    def lower_channel(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the lower channel (linear regression - k * stdDev)"""
        ...

    @property
    def intercept(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The point where the regression line crosses the y-axis (price-axis)"""
        ...

    @property
    def slope(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """The regression line slope"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, k: float) -> None:
        """
        Initializes a new instance of the RegressionChannel class.
        
        :param name: The name of this indicator
        :param period: The number of data points to hold in the window
        :param k: The number of standard deviations specifying the distance between the linear regression and upper or lower channel lines
        """
        ...

    @overload
    def __init__(self, period: int, k: float) -> None:
        """
        Initializes a new instance of the LeastSquaresMovingAverage class.
        
        :param period: The number of data points to hold in the window.
        :param k: The number of standard deviations specifying the distance between the linear regression and upper or lower channel lines
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and all sub-indicators (StandardDeviation, LowerBand, MiddleBand, UpperBand)"""
        ...


class BollingerBands(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band
    fixed at k standard deviations above and below the moving average.
    """

    @property
    def moving_average_type(self) -> QuantConnect.Indicators.MovingAverageType:
        """Gets the type of moving average"""
        ...

    @property
    def standard_deviation(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the standard deviation"""
        ...

    @property
    def middle_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the middle Bollinger band (moving average)"""
        ...

    @property
    def upper_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the upper Bollinger band (middleBand + k * stdDev)"""
        ...

    @property
    def lower_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the lower Bollinger band (middleBand - k * stdDev)"""
        ...

    @property
    def band_width(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Gets the Bollinger BandWidth indicator
        BandWidth = ((Upper Band - Lower Band) / Middle Band) * 100
        """
        ...

    @property
    def percent_b(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Gets the Bollinger %B
        %B = (Price - Lower Band)/(Upper Band - Lower Band)
        """
        ...

    @property
    def price(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the Price level"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int, k: float, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the BollingerBands class
        
        :param period: The period of the standard deviation and moving average (middle band)
        :param k: The number of standard deviations specifying the distance between the middle band and upper or lower bands
        :param movingAverageType: The type of moving average to be used
        """
        ...

    @overload
    def __init__(self, name: str, period: int, k: float, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the BollingerBands class
        
        :param name: The name of this indicator
        :param period: The period of the standard deviation and moving average (middle band)
        :param k: The number of standard deviations specifying the distance between the middle band and upper or lower bands
        :param movingAverageType: The type of moving average to be used
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of the following sub-indicators from the given state:
        StandardDeviation, MiddleBand, UpperBand, LowerBand, BandWidth, %B
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: The input is returned unmodified.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and all sub-indicators (StandardDeviation, LowerBand, MiddleBand, UpperBand, BandWidth, %B)"""
        ...

    def validate_and_compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> QuantConnect.Indicators.IndicatorResult:
        """
        Validate and Compute the next value for this indicator
        
        This method is protected.
        
        :param input: Input for this indicator
        :returns: IndicatorResult of this update.
        """
        ...


class TimeSeriesForecast(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of predicting new values given previous data from a window.
    Source: https://tulipindicators.org/tsf
    """

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new TimeSeriesForecast indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to look back
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new TimeSeriesForecast indicator with the specified period
        
        :param period: The period over which to look back
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class ChaikinMoneyFlow(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Chaikin Money Flow Index (CMF) is a volume-weighted average of accumulation and distribution over
    a specified period.
    
    CMF = n-day Sum of [(((C - L) - (H - C)) / (H - L)) x Vol] / n-day Sum of Vol
    
    Where:
    n = number of periods, typically 21
    H = high
    L = low
    C = close
    Vol = volume
    
    https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/cmf
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the ChaikinMoneyFlow class
        
        :param name: A name for the indicator
        :param period: The period over which to perform computation
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MeanAbsoluteDeviation(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """This indicator computes the n-period mean absolute deviation."""

    @property
    def mean(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the mean used to compute the deviation"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the MeanAbsoluteDeviation class with the specified period.
        
        Evaluates the mean absolute deviation of samples in the lookback period.
        
        :param period: The sample size of the standard deviation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the MeanAbsoluteDeviation class with the specified period.
        
        Evaluates the mean absolute deviation of samples in the look-back period.
        
        :param name: The name of this indicator
        :param period: The sample size of the mean absolute deviation
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and its sub-indicator Mean to their initial state"""
        ...


class WilderAccumulativeSwingIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator calculates the Accumulative Swing Index (ASI) as defined by
    Welles Wilder in his book 'New Concepts in Technical Trading Systems'.
    
    ASIₜ = ASIₜ₋₁ + SIₜ
    
      Where:
      ASIₜ₋₁
            The  for the previous period.
          SIₜ
            The  calculated for the current period.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized."""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, limitMove: float) -> None:
        """
        Initializes a new instance of the WilderAccumulativeSwingIndex class using the specified name.
        
        :param limitMove: A decimal representing the limit move value for the period.
        """
        ...

    @overload
    def __init__(self, name: str, limitMove: float) -> None:
        """
        Initializes a new instance of the WilderAccumulativeSwingIndex class using the specified name.
        
        :param name: The name of this indicator
        :param limitMove: A decimal representing the limit move value for the period.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state."""
        ...


class McGinleyDynamic(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the McGinley Dynamic (MGD)
    It is a type of moving average that was designed to track the market better
    than existing moving average indicators.
    It is a technical indicator that improves upon moving average lines by adjusting
    for shifts in market speed.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the McGinleyDynamic class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the McGinley Dynamic
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the McGinleyDynamic class with the default name and period
        
        :param period: The period of the McGinley Dynamic
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class OnBalanceVolume(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the On Balance Volume (OBV).
    The On Balance Volume is calculated by determining the price of the current close price and previous close price.
    If the current close price is equivalent to the previous price the OBV remains the same,
    If the current close price is higher the volume of that day is added to the OBV, while a lower close price will
    result in negative value.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Indicator class using the specified name."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Indicator class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class SmoothedOnBalanceVolume(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """This class has no documentation."""

    @property
    def on_balance_volume(self) -> QuantConnect.Indicators.OnBalanceVolume:
        """Gets the OnBalanceVolume which is the more volatile calculation to be smoothed by this indicator"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new SmoothedOnBalanceVolume indicator using the specified period and moving average type
        
        :param name: The name of this indicator
        :param period: The smoothing period used to smooth the OnBalanceVolume values
        :param movingAverageType: The type of smoothing used to smooth the OnBalanceVolume values
        """
        ...

    @overload
    def __init__(self, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new SmoothedOnBalanceVolume indicator using the specified period and moving average type
        
        :param period: The smoothing period used to smooth the OnBalanceVolume values
        :param movingAverageType: The type of smoothing used to smooth the OnBalanceVolume values
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class LinearWeightedMovingAverage(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional Weighted Moving Average indicator. The weight are linearly
    distributed according to the number of periods in the indicator.
    
    For example, a 4 period indicator will have a numerator of (4 * window[0]) + (3 * window[1]) + (2 * window[2]) + window[3]
    and a denominator of 4 + 3 + 2 + 1 = 10
    
    During the warm up period, IsReady will return false, but the LWMA will still be computed correctly because
    the denominator will be the minimum of Samples factorial or Size factorial and
    the computation iterates over that minimum value.
    
    The RollingWindow of inputs is created when the indicator is created.
    A RollingWindow of LWMAs is not saved.  That is up to the caller.
    """

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the LinearWeightedMovingAverage class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the LWMA
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the LinearWeightedMovingAverage class with the default name and period
        
        :param period: The period of the LWMA
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class Trix(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the TRIX (1-period ROC of a Triple EMA)
    The TRIX is calculated as explained here:
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:trix
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """
        Required period, in data points, for the indicator to be ready and fully initialized.
        We have 3 EMAs chained on base period so every _period points starts the next EMA,
        hence -1 on the multiplication, and finally the last ema updates our _roc which needs
        to be warmed up before this indicator is warmed up.
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the Trix class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the indicator
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the Trix class using the specified period.
        
        :param period: The period of the indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Variance(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """This indicator computes the n-period population variance."""

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the Variance class using the specified period.
        
        :param period: The period of the indicator
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the Variance class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the indicator
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class KaufmanEfficiencyRatio(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint]):
    """
    This indicator computes the Kaufman Efficiency Ratio (KER).
    The Kaufman Efficiency Ratio is calculated as explained here:
    https://www.marketvolume.com/technicalanalysis/efficiencyratio.asp
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the KaufmanEfficiencyRatio class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the Efficiency Ratio (ER)
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the KaufmanEfficiencyRatio class using the specified period.
        
        :param period: The period of the Efficiency Ratio (ER)
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class KaufmanAdaptiveMovingAverage(QuantConnect.Indicators.KaufmanEfficiencyRatio):
    """
    This indicator computes the Kaufman Adaptive Moving Average (KAMA).
    The Kaufman Adaptive Moving Average is calculated as explained here:
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:kaufman_s_adaptive_moving_average
    """

    @overload
    def __init__(self, name: str, period: int, fastEmaPeriod: int = 2, slowEmaPeriod: int = 30) -> None:
        """
        Initializes a new instance of the KaufmanAdaptiveMovingAverage class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the Efficiency Ratio (ER)
        :param fastEmaPeriod: The period of the fast EMA used to calculate the Smoothing Constant (SC)
        :param slowEmaPeriod: The period of the slow EMA used to calculate the Smoothing Constant (SC)
        """
        ...

    @overload
    def __init__(self, period: int, fastEmaPeriod: int = 2, slowEmaPeriod: int = 30) -> None:
        """
        Initializes a new instance of the KaufmanAdaptiveMovingAverage class using the specified period.
        
        :param period: The period of the Efficiency Ratio (ER)
        :param fastEmaPeriod: The period of the fast EMA used to calculate the Smoothing Constant (SC)
        :param slowEmaPeriod: The period of the slow EMA used to calculate the Smoothing Constant (SC)
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class DualSymbolIndicator(typing.Generic[QuantConnect_Indicators_DualSymbolIndicator_TInput], QuantConnect.Indicators.MultiSymbolIndicator[QuantConnect_Indicators_DualSymbolIndicator_TInput], metaclass=abc.ABCMeta):
    """Base class for indicators that work with two different symbols and calculate an indicator based on them."""

    @property
    def target_data_points(self) -> QuantConnect.Indicators.IReadOnlyWindow[QuantConnect_Indicators_DualSymbolIndicator_TInput]:
        """
        RollingWindow to store the data points of the target symbol
        
        This property is protected.
        """
        ...

    @property
    def reference_data_points(self) -> QuantConnect.Indicators.IReadOnlyWindow[QuantConnect_Indicators_DualSymbolIndicator_TInput]:
        """
        RollingWindow to store the data points of the reference symbol
        
        This property is protected.
        """
        ...

    @property
    def reference_symbol(self) -> QuantConnect.Symbol:
        """
        Symbol of the reference used
        
        This property is protected.
        """
        ...

    @property
    def target_symbol(self) -> QuantConnect.Symbol:
        """
        Symbol of the target used
        
        This property is protected.
        """
        ...

    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int) -> None:
        """
        Initializes the dual symbol indicator.
        
        The constructor accepts a target symbol and a reference symbol. It also initializes
        the time zones for both symbols and checks if they are different.
        
        This method is protected.
        
        :param name: The name of the indicator.
        :param targetSymbol: The symbol of the target asset.
        :param referenceSymbol: The symbol of the reference asset.
        :param period: The period (number of data points) over which to calculate the indicator.
        """
        ...


class Correlation(QuantConnect.Indicators.DualSymbolIndicator[QuantConnect.Data.Market.IBaseDataBar]):
    """
    The Correlation Indicator is a valuable tool in technical analysis, designed to quantify the degree of
    relationship between the price movements of a target security (e.g., a stock or ETF) and a reference
    market index. It measures how closely the target’s price changes are aligned with the fluctuations of
    the index over a specific period of time, providing insights into the target’s susceptibility to market
    movements.
    A positive correlation indicates that the target tends to move in the same direction as the market index,
    while a negative correlation suggests an inverse relationship. A correlation close to 0 implies a weak or
    no linear relationship.
    Commonly, the SPX index is employed as the benchmark for the overall market when calculating correlation,
    ensuring a consistent and reliable reference point. This helps traders and investors make informed decisions
    regarding the risk and behavior of the target security in relation to market trends.
    
    The indicator only updates when both assets have a price for a time step. When a bar is missing for one of the assets,
    the indicator value fills forward to improve the accuracy of the indicator.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when the indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, correlationType: QuantConnect.Indicators.CorrelationType = ...) -> None:
        """
        Creates a new Correlation indicator with the specified name, target, reference,
        and period values
        
        :param name: The name of this indicator
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param period: The period of this indicator
        :param correlationType: Correlation type
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int, correlationType: QuantConnect.Indicators.CorrelationType = ...) -> None:
        """
        Creates a new Correlation indicator with the specified target, reference,
        and period values
        
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param period: The period of this indicator
        :param correlationType: Correlation type
        """
        ...

    def compute_indicator(self) -> float:
        """
        Computes the correlation value usuing symbols values
        correlation values assing into _correlation property
        
        This method is protected.
        """
        ...


class Delay(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """An indicator that delays its input for a certain period"""

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Creates a new Delay indicator that delays its input by the specified period
        
        :param period: The period to delay input, must be greater than zero
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new Delay indicator that delays its input by the specified period
        
        :param name: Name of the delay window indicator
        :param period: The period to delay input, must be greater than zero
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input value to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...


class OptionGreekIndicatorsHelper(System.Object):
    """Helper class for option greeks related indicators"""

    STEPS: int = 200
    """Number of steps in binomial tree simulation to obtain Greeks/IV"""

    @staticmethod
    def black_theoretical_price(volatility: float, spot_price: float, strike_price: float, time_to_expiration: float, risk_free_rate: float, dividend_yield: float, option_type: QuantConnect.OptionRight) -> float:
        """Returns the Black theoretical price for the given arguments"""
        ...

    @staticmethod
    def crr_theoretical_price(volatility: float, spot_price: float, strike_price: float, time_to_expiration: float, risk_free_rate: float, dividend_yield: float, option_type: QuantConnect.OptionRight, steps: int = ...) -> float:
        """Creates a Binomial Theoretical Price Tree from the given parameters"""
        ...

    @staticmethod
    def forward_tree_theoretical_price(volatility: float, spot_price: float, strike_price: float, time_to_expiration: float, risk_free_rate: float, dividend_yield: float, option_type: QuantConnect.OptionRight, steps: int = ...) -> float:
        """Creates the Forward Binomial Theoretical Price Tree from the given parameters"""
        ...

    @staticmethod
    def time_till_expiry(expiry: typing.Union[datetime.datetime, datetime.date], reference_date: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...


class AdvanceDeclineDifference(QuantConnect.Indicators.AdvanceDeclineIndicator):
    """
    The Advance Decline Difference compute the difference between the number of stocks
    that closed higher and the number of stocks that closed lower than their previous day's closing prices.
    """

    def __init__(self, name: str) -> None:
        """Initializes a new instance of the AdvanceDeclineDifference class"""
        ...


class DonchianChannel(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the upper and lower band of the Donchian Channel.
    The upper band is computed by finding the highest high over the given period.
    The lower band is computed by finding the lowest low over the given period.
    The primary output value of the indicator is the mean of the upper and lower band for
    the given timeframe.
    """

    @property
    def upper_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the upper band of the Donchian Channel."""
        ...

    @property
    def lower_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the lower band of the Donchian Channel."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the DonchianChannel class.
        
        :param period: The period for both the upper and lower channels.
        """
        ...

    @overload
    def __init__(self, upperPeriod: int, lowerPeriod: int) -> None:
        """
        Initializes a new instance of the DonchianChannel class.
        
        :param upperPeriod: The period for the upper channel.
        :param lowerPeriod: The period for the lower channel
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the DonchianChannel class.
        
        :param name: The name.
        :param period: The period for both the upper and lower channels.
        """
        ...

    @overload
    def __init__(self, name: str, upperPeriod: int, lowerPeriod: int) -> None:
        """
        Initializes a new instance of the DonchianChannel class.
        
        :param name: The name.
        :param upperPeriod: The period for the upper channel.
        :param lowerPeriod: The period for the lower channel
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator, which by convention is the mean value of the upper band and lower band.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class TargetDownsideDeviation(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period target downside deviation. The target downside deviation is defined as the
    root-mean-square, or RMS, of the deviations of the realized return’s underperformance from the target return
    where all returns above the target return are treated as underperformance of 0.
    
    Reference: https://www.cmegroup.com/education/files/rr-sortino-a-sharper-ratio.pdf
    """

    @overload
    def __init__(self, period: int, minimumAcceptableReturn: float = 0) -> None:
        """
        Initializes a new instance of the TargetDownsideDeviation class with the specified period and
        minimum acceptable return.
        
        The target downside deviation is defined as the root-mean-square, or RMS, of the deviations of
        the realized return’s underperformance from the target return where all returns above the target
        return are treated as underperformance of 0.
        
        :param period: The sample size of the target downside deviation
        :param minimumAcceptableReturn: Minimum acceptable return (MAR) for target downside deviation calculation
        """
        ...

    @overload
    def __init__(self, name: str, period: int, minimumAcceptableReturn: float = 0) -> None:
        """
        Initializes a new instance of the TargetDownsideDeviation class with the specified period and
        minimum acceptable return.
        
        The target downside deviation is defined as the root-mean-square, or RMS, of the deviations of
        the realized return’s underperformance from the target return where all returns above the target
        return are treated as underperformance of 0.
        
        :param name: The name of this indicator
        :param period: The sample size of the target downside deviation
        :param minimumAcceptableReturn: Minimum acceptable return (MAR) for target downside deviation calculation
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class AroonOscillator(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Aroon Oscillator is the difference between AroonUp and AroonDown. The value of this
    indicator fluctuates between -100 and +100. An upward trend bias is present when the oscillator
    is positive, and a negative trend bias is present when the oscillator is negative. AroonUp/Down
    values over 75 identify strong trends in their respective direction.
    """

    @property
    def aroon_up(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the AroonUp indicator"""
        ...

    @property
    def aroon_down(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the AroonDown indicator"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, upPeriod: int, downPeriod: int) -> None:
        """
        Creates a new AroonOscillator from the specified up/down periods.
        
        :param upPeriod: The lookback period to determine the highest high for the AroonDown
        :param downPeriod: The lookback period to determine the lowest low for the AroonUp
        """
        ...

    @overload
    def __init__(self, name: str, upPeriod: int, downPeriod: int) -> None:
        """
        Creates a new AroonOscillator from the specified up/down periods.
        
        :param name: The name of this indicator
        :param upPeriod: The lookback period to determine the highest high for the AroonDown
        :param downPeriod: The lookback period to determine the lowest low for the AroonUp
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator and both sub-indicators (AroonUp and AroonDown)"""
        ...


class WilderMovingAverage(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the moving average indicator defined by Welles Wilder in his book:
    New Concepts in Technical Trading Systems.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the WilderMovingAverage class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period of the Wilder Moving Average
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the WilderMovingAverage class with the default name and period
        
        :param period: The period of the Wilder Moving Average
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AverageTrueRange(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The AverageTrueRange indicator is a measure of volatility introduced by Welles Wilder in his
    book: New Concepts in Technical Trading Systems. This indicator computes the TrueRange and then
    smoothes the TrueRange over a given period.
    
    TrueRange is defined as the maximum of the following:
      High - Low
      ABS(High - PreviousClose)
      ABS(Low - PreviousClose)
    """

    @property
    def true_range(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]:
        """Gets the true range which is the more volatile calculation to be smoothed by this indicator"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new AverageTrueRange indicator using the specified period and moving average type
        
        :param name: The name of this indicator
        :param period: The smoothing period used to smooth the true range values
        :param movingAverageType: The type of smoothing used to smooth the true range values
        """
        ...

    @overload
    def __init__(self, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Creates a new AverageTrueRange indicator using the specified period and moving average type
        
        :param period: The smoothing period used to smooth the true range values
        :param movingAverageType: The type of smoothing used to smooth the true range values
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    @staticmethod
    def compute_true_range(previous: QuantConnect.Data.Market.IBaseDataBar, current: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the TrueRange from the current and previous trade bars
        
        TrueRange is defined as the maximum of the following:
          High - Low
          ABS(High - PreviousClose)
          ABS(Low - PreviousClose)
        
        :param previous: The previous trade bar
        :param current: The current trade bar
        :returns: The true range.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AverageDirectionalIndex(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes Average Directional Index which measures trend strength without regard to trend direction.
    Firstly, it calculates the Directional Movement and the True Range value, and then the values are accumulated and smoothed
    using a custom smoothing method proposed by Wilder. For an n period smoothing, 1/n of each period's value is added to the total period.
    From these accumulated values we are therefore able to derived the 'Positive Directional Index' (+DI) and 'Negative Directional Index' (-DI)
    which is used to calculate the Average Directional Index.
    Computation source:
    https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def positive_directional_index(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the index of the Plus Directional Indicator"""
        ...

    @property
    def negative_directional_index(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the index of the Minus Directional Indicator"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the AverageDirectionalIndex class.
        
        :param period: The period.
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the AverageDirectionalIndex class.
        
        :param name: The name.
        :param period: The period.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class EaseOfMovementValue(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period Ease of Movement Value using the following:
    MID = (high_1 + low_1)/2 - (high_0 + low_0)/2
    RATIO = (currentVolume/10000) / (high_1 - low_1)
    EMV = MID/RATIO
    _SMA = n-period of EMV
    Returns _SMA
    Source: https://www.investopedia.com/terms/e/easeofmovement.asp
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int = 1, scale: int = 10000) -> None:
        """
        Initializeds a new instance of the EaseOfMovement class using the specufued period
        
        :param period: The period over which to perform to computation
        :param scale: The size of the number outputed by EMV
        """
        ...

    @overload
    def __init__(self, name: str, period: int, scale: int) -> None:
        """
        Creates a new EaseOfMovement indicator with the specified period
        
        :param name: The name of this indicator
        :param period: The period over which to perform to computation
        :param scale: The size of the number outputed by EMV
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The input value to this indicator on this time step
        :returns: A a value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class PivotPointType(Enum):
    """Pivot point direction"""

    LOW = -1
    """Low pivot point (-1)"""

    NONE = 0
    """No pivot point (0)"""

    HIGH = 1
    """High pivot point (1)"""

    BOTH = 2
    """Both high and low pivot point (2)"""


class ZigZag(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The ZigZag indicator identifies significant turning points in price movements,
    filtering out noise using a sensitivity threshold and a minimum trend length.
    It alternates between high and low pivots to determine market trends.
    """

    @property
    def high_pivot(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Stores the most recent high pivot value in the ZigZag calculation.
        Updated whenever a valid high pivot is identified.
        """
        ...

    @property
    def low_pivot(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """
        Stores the most recent low pivot value in the ZigZag calculation.
        Updated whenever a valid low pivot is identified.
        """
        ...

    @property
    def pivot_type(self) -> QuantConnect.Indicators.PivotPointType:
        """
        Represents the current type of pivot (High or Low) in the ZigZag calculation.
        The value is updated based on the most recent pivot identified:
        """
        ...

    @property
    def is_ready(self) -> bool:
        """
        Indicates whether the indicator has enough data to produce meaningful output.
        The indicator is considered "ready" when the number of samples exceeds the minimum trend length.
        """
        ...

    @property
    def warm_up_period(self) -> int:
        """
        Gets the number of periods required for the indicator to warm up.
        This is equal to the minimum trend length plus one additional bar for initialization.
        """
        ...

    @overload
    def __init__(self, name: str, sensitivity: float = 0.05, minTrendLength: int = 1) -> None:
        """
        Initializes a new instance of the ZigZag class with the specified parameters.
        
        :param name: The name of the indicator.
        :param sensitivity: The sensitivity threshold as a decimal value between 0 and 1.
        :param minTrendLength: The minimum number of bars required to form a valid trend.
        """
        ...

    @overload
    def __init__(self, sensitivity: float = 0.05, minTrendLength: int = 1) -> None:
        """
        Initializes a new instance of the ZigZag class using default parameters.
        
        :param sensitivity: The sensitivity threshold as a decimal value between 0 and 1.
        :param minTrendLength: The minimum number of bars required to form a valid trend.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of the ZigZag indicator based on the input bar.
        Determines whether the input bar forms a new pivot or updates the current trend.
        
        This method is protected.
        
        :param input: The current bar of market data used for the calculation.
        :returns: The value of the most recent pivot, either a high or low, depending on the current trend.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class TimeProfile(QuantConnect.Indicators.MarketProfile):
    """Represents an Indicator of the Market Profile with Time Price Opportunity (TPO) mode and its attributes"""

    @overload
    def __init__(self, period: int = 2) -> None:
        """
        Creates a new TimeProfile indicator with the specified period
        
        :param period: The period of this indicator
        """
        ...

    @overload
    def __init__(self, name: str, period: int, valueAreaVolumePercentage: float = 0.70, priceRangeRoundOff: float = 0.05) -> None:
        """
        Creates a new TimeProfile indicator with the specified name, period and priceRangeRoundOff
        
        :param name: The name of this indicator
        :param period: The period of this indicator
        :param valueAreaVolumePercentage: The percentage of volume contained in the value area
        :param priceRangeRoundOff: How many digits you want to round and the precision. i.e 0.01 round to two digits exactly.
        """
        ...

    def get_volume(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Define the Volume in Time Profile mode
        
        This method is protected.
        
        :returns: 1.
        """
        ...


class Theta(QuantConnect.Indicators.OptionGreeksIndicatorBase):
    """Option Theta indicator that calculate the theta of an option"""

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Theta class
        
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Theta
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    def calculate_greek(self, time_till_expiry: float) -> float:
        """
        Calculate the Theta of the option
        
        This method is protected.
        """
        ...


class KeltnerChannels(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band
    fixed at k average true range multiples away from the middle band.
    """

    @property
    def middle_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the middle band of the channel"""
        ...

    @property
    def upper_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]:
        """Gets the upper band of the channel"""
        ...

    @property
    def lower_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]:
        """Gets the lower band of the channel"""
        ...

    @property
    def average_true_range(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]:
        """Gets the average true range"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int, k: float, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the KeltnerChannels class
        
        :param period: The period of the average true range and moving average (middle band)
        :param k: The number of multiplies specifying the distance between the middle band and upper or lower bands
        :param movingAverageType: The type of moving average to be used
        """
        ...

    @overload
    def __init__(self, name: str, period: int, k: float, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the KeltnerChannels class
        
        :param name: The name of this indicator
        :param period: The period of the average true range and moving average (middle band)
        :param k: The number of multiples specifying the distance between the middle band and upper or lower bands
        :param movingAverageType: The type of moving average to be used
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value for this indicator from the given state.
        
        This method is protected.
        
        :param input: The TradeBar to this indicator on this time step
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Stochastic(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Slow Stochastics %K and %D. The Fast Stochastics %K is is computed by
    (Current Close Price - Lowest Price of given Period) / (Highest Price of given Period - Lowest Price of given Period)
    multiplied by 100. Once the Fast Stochastics %K is calculated the Slow Stochastic %K is calculated by the average/smoothed price of
    of the Fast %K with the given period. The Slow Stochastics %D is then derived from the Slow Stochastics %K with the given period.
    """

    @property
    def fast_stoch(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]:
        """Gets the value of the Fast Stochastics %K given Period."""
        ...

    @property
    def stoch_k(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]:
        """Gets the value of the Slow Stochastics given Period K."""
        ...

    @property
    def stoch_d(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar]:
        """Gets the value of the Slow Stochastics given Period D."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, kPeriod: int, dPeriod: int) -> None:
        """
        Creates a new Stochastics Indicator from the specified periods.
        
        :param name: The name of this indicator.
        :param period: The period given to calculate the Fast %K
        :param kPeriod: The K period given to calculated the Slow %K
        :param dPeriod: The D period given to calculated the Slow %D
        """
        ...

    @overload
    def __init__(self, period: int, kPeriod: int, dPeriod: int) -> None:
        """
        Creates a new Stochastic indicator from the specified inputs.
        
        :param period: The period given to calculate the Fast %K
        :param kPeriod: The K period given to calculated the Slow %K
        :param dPeriod: The D period given to calculated the Slow %D
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Vega(QuantConnect.Indicators.OptionGreeksIndicatorBase):
    """Option Vega indicator that calculate the Vega of an option"""

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Vega class
        
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Vega
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    def calculate_greek(self, time_till_expiry: float) -> float:
        """
        Calculate the Vega of the option
        
        This method is protected.
        """
        ...


class HurstExponent(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the Hurst Exponent indicator, which is used to measure the long-term memory of a time series.
    - H less than 0.5: Mean-reverting; high values followed by low ones, stronger as H approaches 0.
    - H equal to 0.5: Random walk (geometric).
    - H greater than 0.5: Trending; high values followed by higher ones, stronger as H approaches 1.
    """

    @property
    def warm_up_period(self) -> int:
        """Gets the period over which the indicator is calculated."""
        ...

    @property
    def is_ready(self) -> bool:
        """Indicates whether the indicator has enough data to produce a valid result."""
        ...

    @overload
    def __init__(self, name: str, period: int, maxLag: int = 20) -> None:
        """
        Initializes a new instance of the HurstExponent class.
        The default maxLag value of 20 is chosen for reliable and accurate results, but using a higher lag may reduce precision.
        
        :param name: The name of the indicator.
        :param period: The period over which to calculate the Hurst Exponent.
        :param maxLag: The maximum lag to consider for time series analysis.
        """
        ...

    @overload
    def __init__(self, period: int, maxLag: int = 20) -> None:
        """
        Initializes a new instance of the HurstExponent class with the specified period and maxLag.
        The default maxLag value of 20 is chosen for reliable and accurate results, but using a higher lag may reduce precision.
        
        :param period: The period over which to calculate the Hurst Exponent.
        :param maxLag: The maximum lag to consider for time series analysis.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of the Hurst Exponent indicator.
        
        This method is protected.
        
        :param input: The input data point to use for the next value computation.
        :returns: The computed Hurst Exponent value, or zero if insufficient data is available.
        """
        ...

    def reset(self) -> None:
        """Resets the indicator to its initial state. This clears all internal data and resets"""
        ...


class SqueezeMomentum(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The SqueezeMomentum indicator calculates whether the market is in a "squeeze" condition,
    determined by comparing Bollinger Bands to Keltner Channels. When the Bollinger Bands are
    inside the Keltner Channels, the indicator returns 1 (squeeze on). Otherwise, it returns -1 (squeeze off).
    """

    @property
    def bollinger_bands(self) -> QuantConnect.Indicators.BollingerBands:
        """The Bollinger Bands indicator used to calculate the upper, lower, and middle bands."""
        ...

    @property
    def keltner_channels(self) -> QuantConnect.Indicators.KeltnerChannels:
        """The Keltner Channels indicator used to calculate the upper, lower, and middle channels."""
        ...

    @property
    def warm_up_period(self) -> int:
        """
        Gets the warm-up period required for the indicator to be ready.
        This is determined by the warm-up period of the Bollinger Bands indicator.
        """
        ...

    @property
    def is_ready(self) -> bool:
        """
        Indicates whether the indicator is ready and has enough data for computation.
        The indicator is ready when both the Bollinger Bands and the Average True Range are ready.
        """
        ...

    def __init__(self, name: str, bollingerPeriod: int, bollingerMultiplier: float, keltnerPeriod: int, keltnerMultiplier: float) -> None:
        """
        Initializes a new instance of the SqueezeMomentum class.
        
        :param name: The name of the indicator.
        :param bollingerPeriod: The period used for the Bollinger Bands calculation.
        :param bollingerMultiplier: The multiplier for the Bollinger Bands width.
        :param keltnerPeriod: The period used for the Average True Range (ATR) calculation in Keltner Channels.
        :param keltnerMultiplier: The multiplier applied to the ATR for calculating Keltner Channels.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of the indicator based on the input data bar.
        
        This method is protected.
        
        :param input: The input data bar.
        :returns: Returns 1 if the Bollinger Bands are inside the Keltner Channels (squeeze on), or -1 if the Bollinger Bands are outside the Keltner Channels (squeeze off).
        """
        ...

    def reset(self) -> None:
        """Resets the state of the indicator, including all sub-indicators."""
        ...


class AverageDirectionalMovementIndexRating(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Average Directional Movement Index Rating (ADXR).
    The Average Directional Movement Index Rating is calculated with the following formula:
    ADXR[i] = (ADX[i] + ADX[i - period + 1]) / 2
    """

    @property
    def adx(self) -> QuantConnect.Indicators.AverageDirectionalIndex:
        """The Average Directional Index indicator instance being used"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the AverageDirectionalMovementIndexRating class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the ADXR
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the AverageDirectionalMovementIndexRating class using the specified period.
        
        :param period: The period of the ADXR
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class PivotPoint(QuantConnect.Data.BaseData):
    """Represents the points identified by Pivot Point High/Low Indicator."""

    @property
    def pivot_point_type(self) -> QuantConnect.Indicators.PivotPointType:
        """Represents pivot point type : High or Low"""
        ...

    @property.setter
    def pivot_point_type(self, value: QuantConnect.Indicators.PivotPointType) -> None:
        ...

    @property
    def value(self) -> float:
        """Peak value"""
        ...

    @property.setter
    def value(self, value: float) -> None:
        ...

    def __init__(self, type: QuantConnect.Indicators.PivotPointType, price: float, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of PivotPoint"""
        ...


class PivotPointsEventArgs(System.EventArgs):
    """Event arguments class for the PivotPointsHighLow.NewPivotPointFormed event"""

    @property
    def pivot_point(self) -> QuantConnect.Indicators.PivotPoint:
        """New pivot point"""
        ...

    def __init__(self, pivotPoint: QuantConnect.Indicators.PivotPoint) -> None:
        """Creates a new instance of PivotPointsEventArgs"""
        ...


class PivotPointsHighLow(QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Pivot Points (High/Low), also known as Bar Count Reversals, indicator.
    https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/pivot-points-high-low
    """

    @property
    def new_pivot_point_formed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Indicators.PivotPointsEventArgs], None], None]:
        """Event informs of new pivot point formed with new data update"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, surroundingBarsCount: int, lastStoredValues: int = 100) -> None:
        """
        Creates a new instance of PivotPointsHighLow indicator with an equal high and low length
        
        :param surroundingBarsCount: The length parameter here defines the number of surrounding bars that we compare against the current bar high and lows for the max/min
        :param lastStoredValues: The number of last stored indicator values
        """
        ...

    @overload
    def __init__(self, surroundingBarsCountForHighPoint: int, surroundingBarsCountForLowPoint: int, lastStoredValues: int = 100) -> None:
        """
        Creates a new instance of PivotPointsHighLow indicator
        
        :param surroundingBarsCountForHighPoint: The number of surrounding bars whose high values should be less than the current bar's for the bar high to be marked as high pivot point
        :param surroundingBarsCountForLowPoint: The number of surrounding bars whose low values should be more than the current bar's for the bar low to be marked as low pivot point
        :param lastStoredValues: The number of last stored indicator values
        """
        ...

    @overload
    def __init__(self, name: str, surroundingBarsCountForHighPoint: int, surroundingBarsCountForLowPoint: int, lastStoredValues: int = 100) -> None:
        """
        Creates a new instance of PivotPointsHighLow indicator
        
        :param name: The name of an indicator
        :param surroundingBarsCountForHighPoint: The number of surrounding bars whose high values should be less than the current bar's for the bar high to be marked as high pivot point
        :param surroundingBarsCountForLowPoint: The number of surrounding bars whose low values should be more than the current bar's for the bar low to be marked as low pivot point
        :param lastStoredValues: The number of last stored indicator values
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def convert_to_computed_value(self, high_point: QuantConnect.Indicators.PivotPoint, low_point: QuantConnect.Indicators.PivotPoint) -> float:
        """
        Method for converting high and low pivot points to a decimal value.
        
        This method is protected.
        
        :param high_point: new high point or null
        :param low_point: new low point or null
        :returns: a decimal value representing the values of high and low pivot points.
        """
        ...

    def find_next_high_pivot_point(self, window_highs: QuantConnect.Indicators.RollingWindow[QuantConnect.Data.Market.IBaseDataBar], mid_point_index_or_surrounding_bars_count: int) -> QuantConnect.Indicators.PivotPoint:
        """
        Looks for the next high pivot point.
        
        This method is protected.
        
        :param window_highs: rolling window that tracks the highs
        :param mid_point_index_or_surrounding_bars_count: The midpoint index or surrounding bars count for highs
        :returns: pivot point if found else null.
        """
        ...

    def find_next_low_pivot_point(self, window_lows: QuantConnect.Indicators.RollingWindow[QuantConnect.Data.Market.IBaseDataBar], mid_point_index_or_surrounding_bars_count: int) -> QuantConnect.Indicators.PivotPoint:
        """
        Looks for the next low pivot point.
        
        This method is protected.
        
        :param window_lows: rolling window that tracks the lows
        :param mid_point_index_or_surrounding_bars_count: The midpoint index or surrounding bars count for lows
        :returns: pivot point if found else null.
        """
        ...

    def get_all_pivot_points_array(self) -> typing.List[QuantConnect.Indicators.PivotPoint]:
        """
        Get all pivot points, in the order such that first element in collection is the nearest to the present date
        
        :returns: An array of low and high pivot points. Ordered by time in descending order.
        """
        ...

    def get_high_pivot_points_array(self) -> typing.List[QuantConnect.Indicators.PivotPoint]:
        """
        Get current high pivot points, in the order such that first element in collection is the nearest to the present date
        
        :returns: An array of high pivot points.
        """
        ...

    def get_low_pivot_points_array(self) -> typing.List[QuantConnect.Indicators.PivotPoint]:
        """
        Get current low pivot points, in the order such that first element in collection is the nearest to the present date
        
        :returns: An array of low pivot points.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ChandeKrollStop(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the short stop and lower stop values of the Chande Kroll Stop Indicator.
    It is used to determine the optimal placement of a stop-loss order.
    """

    @property
    def short_stop(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the short stop of ChandeKrollStop."""
        ...

    @property
    def long_stop(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the long stop of ChandeKrollStop."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, atrPeriod: int, atrMult: float, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the ChandeKrollStop class.
        
        :param atrPeriod: The period over which to compute the average true range.
        :param atrMult: The ATR multiplier to be used to compute stops distance.
        :param period: The period over which to compute the max of high stop and min of low stop.
        :param movingAverageType: The type of smoothing used to smooth the true range values
        """
        ...

    @overload
    def __init__(self, name: str, atrPeriod: int, atrMult: float, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the ChandeKrollStop class.
        
        :param name: The name.
        :param atrPeriod: The period over which to compute the average true range.
        :param atrMult: The ATR multiplier to be used to compute stops distance.
        :param period: The period over which to compute the max of high stop and min of low stop.
        :param movingAverageType: The type of smoothing used to smooth the true range values
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: The input is returned unmodified.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AccumulationDistribution(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Accumulation/Distribution (AD)
    The Accumulation/Distribution is calculated using the following formula:
    AD = AD + ((Close - Low) - (High - Close)) / (High - Low) * Volume
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AccumulationDistribution class using the specified name."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the AccumulationDistribution class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class Rho(QuantConnect.Indicators.OptionGreeksIndicatorBase):
    """Option Rho indicator that calculate the rho of an option"""

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Rho class
        
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    def calculate_greek(self, time_till_expiry: float) -> float:
        """
        Calculate the Rho of the option
        
        This method is protected.
        """
        ...


class PercentagePriceOscillator(QuantConnect.Indicators.AbsolutePriceOscillator):
    """
    This indicator computes the Percentage Price Oscillator (PPO)
    The Percentage Price Oscillator is calculated using the following formula:
    PPO[i] = 100 * (FastMA[i] - SlowMA[i]) / SlowMA[i]
    """

    @overload
    def __init__(self, name: str, fastPeriod: int, slowPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the PercentagePriceOscillator class using the specified name and parameters.
        
        :param name: The name of this indicator
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param movingAverageType: The type of moving average to use
        """
        ...

    @overload
    def __init__(self, fastPeriod: int, slowPeriod: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the PercentagePriceOscillator class using the specified parameters.
        
        :param fastPeriod: The fast moving average period
        :param slowPeriod: The slow moving average period
        :param movingAverageType: The type of moving average to use
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class VolumeProfile(QuantConnect.Indicators.MarketProfile):
    """Represents an Indicator of the Market Profile with Volume Profile mode and its attributes"""

    @overload
    def __init__(self, period: int = 2) -> None:
        """
        Creates a new VolumeProfile indicator with the specified period
        
        :param period: The period of the indicator
        """
        ...

    @overload
    def __init__(self, name: str, period: int, valueAreaVolumePercentage: float = 0.70, priceRangeRoundOff: float = 0.05) -> None:
        """
        Creates a new VolumeProfile indicator with the specified name, period and priceRangeRoundOff
        
        :param name: The name of this indicator
        :param period: The period of this indicator
        :param valueAreaVolumePercentage: The percentage of volume contained in the value area
        :param priceRangeRoundOff: How many digits you want to round and the precision. i.e 0.01 round to two digits exactly.
        """
        ...

    def get_volume(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Define the Volume for the Volume Profile mode
        
        This method is protected.
        
        :returns: The volume of the input Data Point.
        """
        ...


class MomersionIndicator(QuantConnect.Indicators.WindowIndicator[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Oscillator indicator that measures momentum and mean-reversion over a specified
    period n.
    Source: Harris, Michael. "Momersion Indicator." Price Action Lab.,
                13 Aug. 2015. Web. http://www.priceactionlab.com/Blog/2015/08/momersion-indicator/.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, minPeriod: typing.Optional[int], fullPeriod: int) -> None:
        """
        Initializes a new instance of the MomersionIndicator class.
        
        :param name: The name.
        :param minPeriod: The minimum period.
        :param fullPeriod: The full period.
        """
        ...

    @overload
    def __init__(self, minPeriod: typing.Optional[int], fullPeriod: int) -> None:
        """
        Initializes a new instance of the MomersionIndicator class.
        
        :param minPeriod: The minimum period.
        :param fullPeriod: The full period.
        """
        ...

    @overload
    def __init__(self, fullPeriod: int) -> None:
        """
        Initializes a new instance of the MomersionIndicator class.
        
        :param fullPeriod: The full period.
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MidPoint(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPoint (MIDPOINT)
    The MidPoint is calculated using the following formula:
    MIDPOINT = (Highest Value + Lowest Value) / 2
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the MidPoint class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the MIDPOINT
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the MidPoint class using the specified period.
        
        :param period: The period of the MIDPOINT
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Gamma(QuantConnect.Indicators.OptionGreeksIndicatorBase):
    """Option Gamma indicator that calculate the gamma of an option"""

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYieldModel: QuantConnect.Data.IDividendYieldModel, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYieldModel: typing.Any, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYieldModel: Dividend yield model
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRateModel: typing.Any, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param option: The option to be tracked
        :param riskFreeRateModel: Risk-free rate model
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, name: str, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param name: The name of this indicator
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    @overload
    def __init__(self, option: typing.Union[QuantConnect.Symbol, str], riskFreeRate: float = 0.05, dividendYield: float = 0.0, mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, optionModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None) -> None:
        """
        Initializes a new instance of the Gamma class
        
        :param option: The option to be tracked
        :param riskFreeRate: Risk-free rate, as a constant
        :param dividendYield: Dividend yield, as a constant
        :param mirrorOption: The mirror option for parity calculation
        :param optionModel: The option pricing model used to estimate Gamma
        :param ivModel: The option pricing model used to estimate IV
        """
        ...

    def calculate_greek(self, time_till_expiry: float) -> float:
        """
        Calculate the Gamma of the option
        
        This method is protected.
        """
        ...


class InternalBarStrength(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The InternalBarStrenght indicator is a measure of the relative position of a period's closing price
    to the same period's high and low.
    The IBS can be interpreted to predict a bullish signal when displaying a low value and a bearish signal when presenting a high value.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Creates a new InternalBarStrenght indicator using the specified period and moving average type
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new InternalBarStrenght indicator using the specified period and moving average type"""
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class DoubleExponentialMovingAverage(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Double Exponential Moving Average (DEMA).
    The Double Exponential Moving Average is calculated with the following formula:
    EMA2 = EMA(EMA(t,period),period)
    DEMA = 2 * EMA(t,period) - EMA2
    The Generalized DEMA (GD) is calculated with the following formula:
    GD = (volumeFactor+1) * EMA(t,period) - volumeFactor * EMA2
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, volumeFactor: float = 1) -> None:
        """
        Initializes a new instance of the DoubleExponentialMovingAverage class using the specified name and period.
        
        :param name: The name of this indicator
        :param period: The period of the DEMA
        :param volumeFactor: The volume factor of the DEMA (value must be in the [0,1] range, set to 1 for standard DEMA)
        """
        ...

    @overload
    def __init__(self, period: int, volumeFactor: float = 1) -> None:
        """
        Initializes a new instance of the DoubleExponentialMovingAverage class using the specified period.
        
        :param period: The period of the DEMA
        :param volumeFactor: The volume factor of the DEMA (value must be in the [0,1] range, set to 1 for standard DEMA)
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RelativeVigorIndex(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The Relative Vigor Index (RVI) compares the ratio of the closing price of a security to its trading range.
    For illustration, let:
    a = Close−Openb = Close−Open of One Bar Prior to ac = Close−Open of One Bar Prior to bd = Close−Open of One Bar Prior to ce = High−Low of Bar af = High−Low of Bar bg = High−Low of Bar ch = High−Low of Bar d
    
    Then let (a+2*(b+c)+d)/6 be NUM and (e+2*(f+g)+h)/6 be DENOM.
    RVI = SMA(NUM)/SMA(DENOM)
    for a specified period.
    
    https://www.investopedia.com/terms/r/relative_vigor_index.asp
    """

    @property
    def signal(self) -> QuantConnect.Indicators.RelativeVigorIndexSignal:
        """A signal line which behaves like a slowed version of the RVI."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int, type: QuantConnect.Indicators.MovingAverageType) -> None:
        """
        Initializes a new instance of the RelativeVigorIndex (RVI) class.
        
        :param period: The period for the RelativeVigorIndex.
        :param type: The type of Moving Average to use
        """
        ...

    @overload
    def __init__(self, name: str, period: int, type: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the RelativeVigorIndex (RVI) class.
        
        :param name: The name of this indicator.
        :param period: The period for the RelativeVigorIndex.
        :param type: The type of Moving Average to use
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AccelerationBands(QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.Market.IBaseDataBar], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """The Acceleration Bands created by Price Headley plots upper and lower envelope bands around a moving average."""

    @property
    def moving_average_type(self) -> QuantConnect.Indicators.MovingAverageType:
        """Gets the type of moving average"""
        ...

    @property
    def middle_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the middle acceleration band (moving average)"""
        ...

    @property
    def upper_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the upper acceleration band  (High * ( 1 + Width * (High - Low) / (High + Low)))"""
        ...

    @property
    def lower_band(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the lower acceleration band  (Low * (1 - Width * (High - Low)/ (High + Low)))"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, period: int, width: float, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the AccelerationBands class.
        
        :param name: The name of this indicator.
        :param period: The period of the three moving average (middle, upper and lower band).
        :param width: A coefficient specifying the distance between the middle band and upper or lower bands.
        :param movingAverageType: Type of the moving average.
        """
        ...

    @overload
    def __init__(self, period: int, width: float) -> None:
        """
        Initializes a new instance of the AccelerationBands class.
        
        :param period: The period of the three moving average (middle, upper and lower band).
        :param width: A coefficient specifying the distance between the middle band and upper or lower bands.
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the AccelerationBands class.
        
        :param period: The period of the three moving average (middle, upper and lower band).
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class StandardDeviation(QuantConnect.Indicators.Variance):
    """This indicator computes the n-period population standard deviation."""

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the StandardDeviation class with the specified period.
        
        Evaluates the standard deviation of samples in the look-back period.
        On a data set of size N will use an N normalizer and would thus be biased if applied to a subset.
        
        :param period: The sample size of the standard deviation
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the StandardDeviation class with the specified name and period.
        
        Evaluates the standard deviation of samples in the look-back period.
        On a data set of size N will use an N normalizer and would thus be biased if applied to a subset.
        
        :param name: The name of this indicator
        :param period: The sample size of the standard deviation
        """
        ...

    def compute_next_value(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Indicators.IndicatorDataPoint], input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window for the input history
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class FractalAdaptiveMovingAverage(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """The Fractal Adaptive Moving Average (FRAMA) by John Ehlers"""

    @property
    def is_ready(self) -> bool:
        """Returns whether the indicator will return valid results"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, n: int, longPeriod: int) -> None:
        """
        Initializes a new instance of the average class
        
        :param name: The name of the indicator instance
        :param n: The window period (must be even). Example value: 16
        :param longPeriod: The average period. Example value: 198
        """
        ...

    @overload
    def __init__(self, n: int, longPeriod: int) -> None:
        """
        Initializes a new instance of the average class
        
        :param n: The window period (must be even). Example value: 16
        :param longPeriod: The average period. Example value: 198
        """
        ...

    @overload
    def __init__(self, n: int) -> None:
        """
        Initializes a new instance of the average class
        
        :param n: The window period (must be even). Example value: 16
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the average value
        
        This method is protected.
        
        :param input: The data for the calculation
        :returns: The average value.
        """
        ...

    def reset(self) -> None:
        """Resets the average to its initial state"""
        ...


class SwissArmyKnifeTool(Enum):
    """The tools of the Swiss Army Knife. Some of the tools lend well to chaining with the "Of" Method, others may be treated as moving averages"""

    GAUSS = 0
    """Two Pole Gaussian Filter (0)"""

    BUTTER = 1
    """Two Pole Butterworth Filter (1)"""

    HIGH_PASS = 2
    """High Pass Filter (2)"""

    TWO_POLE_HIGH_PASS = 3
    """Two Pole High Pass Filter (3)"""

    BAND_PASS = 4
    """BandPass Filter (4)"""


class SwissArmyKnife(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """Swiss Army Knife indicator by John Ehlers"""

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int, delta: float, tool: QuantConnect.Indicators.SwissArmyKnifeTool) -> None:
        """Swiss Army Knife indicator by John Ehlers"""
        ...

    @overload
    def __init__(self, name: str, period: int, delta: float, tool: QuantConnect.Indicators.SwissArmyKnifeTool) -> None:
        """Swiss Army Knife indicator by John Ehlers"""
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets to the initial state"""
        ...


class PremierStochasticOscillator(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Premier Stochastic Oscillator (PSO) Indicator implementation.
    This indicator combines a stochastic oscillator with exponential moving averages to provide
    a normalized output between -1 and 1, which can be useful for identifying trends and
    potential reversal points in the market.
    """

    @property
    def warm_up_period(self) -> int:
        """The warm-up period necessary before the PSO indicator is considered ready."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, period: int, emaPeriod: int) -> None:
        """
        Constructor for the Premier Stochastic Oscillator.
        Initializes the Stochastic and EMA indicators and calculates the warm-up period.
        
        :param name: The name of the indicator.
        :param period: The period given to calculate FastK.
        :param emaPeriod: The period for EMA calculations.
        """
        ...

    @overload
    def __init__(self, period: int, emaPeriod: int) -> None:
        """
        Overloaded constructor to facilitate instantiation with a default name format.
        
        :param period: The period given to calculate FastK.
        :param emaPeriod: The period for EMA calculations.
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the Premier Stochastic Oscillator (PSO) based on the current input.
        This calculation involves updating the stochastic oscillator and the EMAs,
        followed by calculating the PSO using the formula:
        PSO = (exp(EMA2) - 1) / (exp(EMA2) + 1)
        
        This method is protected.
        
        :param input: The current input bar containing market data.
        :returns: The computed value of the PSO.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class FunctionalIndicator(typing.Generic[QuantConnect_Indicators_FunctionalIndicator_T], QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_FunctionalIndicator_T]):
    """
    The functional indicator is used to lift any function into an indicator. This can be very useful
    when trying to combine output of several indicators, or for expression a mathematical equation
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, computeNextValue: typing.Callable[[QuantConnect_Indicators_FunctionalIndicator_T], float], isReady: typing.Callable[[QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_FunctionalIndicator_T]], bool]) -> None:
        """
        Creates a new FunctionalIndicator using the specified functions as its implementation.
        
        :param name: The name of this indicator
        :param computeNextValue: A function accepting the input value and returning this indicator's output value
        :param isReady: A function accepting this indicator and returning true if the indicator is ready, false otherwise
        """
        ...

    @overload
    def __init__(self, name: str, computeNextValue: typing.Callable[[QuantConnect_Indicators_FunctionalIndicator_T], float], isReady: typing.Callable[[QuantConnect.Indicators.IndicatorBase[QuantConnect_Indicators_FunctionalIndicator_T]], bool], reset: typing.Callable[[], None]) -> None:
        """
        Creates a new FunctionalIndicator using the specified functions as its implementation.
        
        :param name: The name of this indicator
        :param computeNextValue: A function accepting the input value and returning this indicator's output value
        :param isReady: A function accepting this indicator and returning true if the indicator is ready, false otherwise
        :param reset: Function called to reset this indicator and any indicators this is dependent on
        """
        ...

    def compute_next_value(self, input: QuantConnect_Indicators_FunctionalIndicator_T) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state, optionally using the reset action passed via the constructor"""
        ...


class VolumeWeightedAveragePriceIndicator(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Volume Weighted Average Price (VWAP) Indicator:
    It is calculated by adding up the dollars traded for every transaction (price multiplied
    by number of shares traded) and then dividing by the total shares traded for the day.
    """

    @property
    def price(self) -> QuantConnect.Indicators.Identity:
        """
        Indentity indicator for price
        
        This property is protected.
        """
        ...

    @property
    def volume(self) -> QuantConnect.Indicators.Identity:
        """
        Identity indicator for volume
        
        This property is protected.
        """
        ...

    @property
    def vwap(self) -> QuantConnect.Indicators.CompositeIndicator:
        """
        Volume Weighted Average Price
        
        This property is protected.
        """
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int) -> None:
        """
        Initializes a new instance of the VWAP class with the default name and period
        
        :param period: The period of the VWAP
        """
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the VWAP class with a given name and period
        
        :param name: string - the name of the indicator
        :param period: The period of the VWAP
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def get_time_weighted_average_price(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Gets an estimated average price to use for the interval covered by the input trade bar.
        
        This method is protected.
        
        :param input: The current trade bar input
        :returns: An estimated average price over the trade bar's interval.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Beta(QuantConnect.Indicators.DualSymbolIndicator[QuantConnect.Data.Market.IBaseDataBar]):
    """
    In technical analysis Beta indicator is used to measure volatility or risk of a target (ETF) relative to the overall
    risk (volatility) of the reference (market indexes). The Beta indicators compares target's price movement to the
    movements of the indexes over the same period of time.
    
    It is common practice to use the SPX index as a benchmark of the overall reference market when it comes to Beta
    calculations.
    
    The indicator only updates when both assets have a price for a time step. When a bar is missing for one of the assets,
    the indicator value fills forward to improve the accuracy of the indicator.
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when the indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int) -> None:
        """
        Creates a new Beta indicator with the specified name, target, reference,
        and period values
        
        :param name: The name of this indicator
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param period: The period of this indicator
        """
        ...

    @overload
    def __init__(self, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str], period: int) -> None:
        """
        Creates a new Beta indicator with the specified target, reference,
        and period values
        
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        :param period: The period of this indicator
        """
        ...

    @overload
    def __init__(self, name: str, period: int, targetSymbol: typing.Union[QuantConnect.Symbol, str], referenceSymbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Creates a new Beta indicator with the specified name, period, target and
        reference values
        
        :param name: The name of this indicator
        :param period: The period of this indicator
        :param targetSymbol: The target symbol of this indicator
        :param referenceSymbol: The reference symbol of this indicator
        """
        ...

    def compute_indicator(self) -> float:
        """
        Computes the beta value of the target in relation with the reference
        using the target and reference returns
        
        This method is protected.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class FilteredIdentity(QuantConnect.Indicators.IndicatorBase[QuantConnect.Data.IBaseData]):
    """
    Represents an indicator that is a ready after ingesting a single sample and
    always returns the same value as it is given if it passes a filter condition
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    def __init__(self, name: str, filter: typing.Callable[[QuantConnect.Data.IBaseData], bool]) -> None:
        """
        Initializes a new instance of the FilteredIdentity indicator with the specified name
        
        :param name: The name of the indicator
        :param filter: Filters the IBaseData send into the indicator, if null defaults to true (x => true) which means no filter
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.IBaseData) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class RelativeStrengthIndex(QuantConnect.Indicators.Indicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Represents the  Relative Strength Index (RSI) developed by K. Welles Wilder.
    You can optionally specified a different moving average type to be used in the computation
    """

    @property
    def moving_average_type(self) -> QuantConnect.Indicators.MovingAverageType:
        """Gets the type of indicator used to compute AverageGain and AverageLoss"""
        ...

    @property
    def average_loss(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the EMA for the down days"""
        ...

    @property
    def average_gain(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the indicator for average gain"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the RelativeStrengthIndex class with the specified name and period
        
        :param period: The period used for up and down days
        :param movingAverageType: The type of moving average to be used for computing the average gain/loss values
        """
        ...

    @overload
    def __init__(self, name: str, period: int, movingAverageType: QuantConnect.Indicators.MovingAverageType = ...) -> None:
        """
        Initializes a new instance of the RelativeStrengthIndex class with the specified name and period
        
        :param name: The name of this indicator
        :param period: The period used for up and down days
        :param movingAverageType: The type of moving average to be used for computing the average gain/loss values
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AverageRange(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """Represents the Average Range (AR) indicator, which calculates the average price range"""

    @property
    def is_ready(self) -> bool:
        """Indicates whether the indicator has enough data to start producing valid results."""
        ...

    @property
    def warm_up_period(self) -> int:
        """The number of periods needed to fully initialize the AR indicator."""
        ...

    @overload
    def __init__(self, name: str, period: int) -> None:
        """
        Initializes a new instance of the AverageRange class with the specified name and period.
        
        :param name: The name of the AR indicator.
        :param period: The number of periods over which to compute the average range.
        """
        ...

    @overload
    def __init__(self, period: int) -> None:
        """Initializes the AR indicator with the default name format and period."""
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of the Average Range (AR) by calculating the price range (high - low)
        and passing it to the SMA to get the smoothed value.
        
        This method is protected.
        
        :param input: The input data for the current bar, including open, high, low, close values.
        :returns: The computed AR value, which is the smoothed average of price ranges.
        """
        ...

    def reset(self) -> None:
        """Resets the indicator and clears the internal state, including the SMA."""
        ...


class McClellanOscillator(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The McClellan Oscillator is a market breadth indicator which was
    developed by Sherman and Marian McClellan. It is based on the
    difference between the number of advancing and declining periods.
    """

    @property
    def ema_fast(self) -> QuantConnect.Indicators.ExponentialMovingAverage:
        """Fast period EMA of advance decline difference"""
        ...

    @property
    def ema_slow(self) -> QuantConnect.Indicators.ExponentialMovingAverage:
        """Slow period EMA of advance decline difference"""
        ...

    @property
    def ad_difference(self) -> QuantConnect.Indicators.AdvanceDeclineDifference:
        """The number of advance assets minus the number of decline assets"""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, fastPeriod: int = 19, slowPeriod: int = 39) -> None:
        """
        Initializes a new instance of the McClellanOscillator class
        The name of the indicatorThe fast period of EMA of advance decline differenceThe slow period of EMA of advance decline difference
        
        :param name: The name of the indicator
        :param fastPeriod: The fast period of EMA of advance decline difference
        :param slowPeriod: The slow period of EMA of advance decline difference
        """
        ...

    @overload
    def __init__(self, fastPeriod: int = 19, slowPeriod: int = 39) -> None:
        """
        Initializes a new instance of the McClellanOscillator class
        The fast period of EMA of advance decline differenceThe slow period of EMA of advance decline difference
        
        :param fastPeriod: The fast period of EMA of advance decline difference
        :param slowPeriod: The slow period of EMA of advance decline difference
        """
        ...

    def add(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Add Tracking asset issue
        
        :param asset: the tracking asset issue
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def remove(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Remove Tracking asset issue
        
        :param asset: the tracking asset issue
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class McClellanSummationIndex(QuantConnect.Indicators.TradeBarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    The McClellan Summation Index (MSI) is a market breadth indicator that is based on the rolling average of difference
    between the number of advancing and declining issues on a stock exchange. It is generally considered as is
    a long-term version of the McClellanOscillator
    """

    @property
    def summation(self) -> QuantConnect.Indicators.IndicatorDataPoint:
        """
        The McClellan Summation Index value
        
        This property is protected.
        """
        ...

    @property
    def mc_clellan_oscillator(self) -> QuantConnect.Indicators.McClellanOscillator:
        """The McClellan Oscillator is a market breadth indicator which was developed by Sherman and Marian McClellan. It is based on the difference between the number of advancing and declining periods."""
        ...

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self, name: str, fastPeriod: int = 19, slowPeriod: int = 39) -> None:
        """
        Initializes a new instance of the McClellanSummationIndex class
        The name of the indicatorThe fast period of EMA of advance decline differenceThe slow period of EMA of advance decline difference
        
        :param name: The name of the indicator
        :param fastPeriod: The fast period of EMA of advance decline difference
        :param slowPeriod: The slow period of EMA of advance decline difference
        """
        ...

    @overload
    def __init__(self, fastPeriod: int = 19, slowPeriod: int = 39) -> None:
        """
        Initializes a new instance of the McClellanSummationIndex class
        The fast period of EMA of advance decline differenceThe slow period of EMA of advance decline difference
        
        :param fastPeriod: The fast period of EMA of advance decline difference
        :param slowPeriod: The slow period of EMA of advance decline difference
        """
        ...

    def add(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Add Tracking asset issue
        
        :param asset: the tracking asset issue
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.TradeBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def remove(self, asset: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Remove Tracking asset issue
        
        :param asset: the tracking asset issue
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MesaAdaptiveMovingAverage(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    Implements the Mesa Adaptive Moving Average (MAMA) indicator along with the following FAMA (Following Adaptive Moving Average) as a secondary indicator.
    The MAMA adjusts its smoothing factor based on the market's volatility, making it more adaptive than a simple moving average.
    """

    @property
    def fama(self) -> QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint]:
        """Gets the FAMA (Following Adaptive Moving Average) indicator value."""
        ...

    @property
    def is_ready(self) -> bool:
        """Returns whether the indicator has enough data to be used (ready to calculate values)."""
        ...

    @property
    def warm_up_period(self) -> int:
        """
        Gets the number of periods required for warming up the indicator.
        33 periods are sufficient for the MAMA to provide stable and accurate results,
        """
        ...

    @overload
    def __init__(self, name: str, fastLimit: float = 0.5, slowLimit: float = 0.05) -> None:
        """
        Initializes a new instance of the MesaAdaptiveMovingAverage class.
        
        :param name: The name of the indicator.
        :param fastLimit: The fast limit for the adaptive moving average (default is 0.5).
        :param slowLimit: The slow limit for the adaptive moving average (default is 0.05).
        """
        ...

    @overload
    def __init__(self, fastLimit: float = 0.5, slowLimit: float = 0.05) -> None:
        """
        Initializes a new instance of the MesaAdaptiveMovingAverage class with default name ("MAMA")
        and the specified fast and slow limits for the adaptive moving average calculation.
        
        :param fastLimit: The fast limit for the adaptive moving average (default is 0.5).
        :param slowLimit: The slow limit for the adaptive moving average (default is 0.05).
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value for the Mesa Adaptive Moving Average (MAMA).
        It calculates the MAMA by applying a series of steps including smoothing, detrending, and phase adjustments.
        
        This method is protected.
        
        :param input: The input bar (price data).
        :returns: The calculated MAMA value.
        """
        ...

    def reset(self) -> None:
        """Resets the indicator's state, clearing history and resetting internal values."""
        ...


class CoppockCurve(QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    A momentum indicator developed by Edwin “Sedge” Coppock in October 1965.
    The goal of this indicator is to identify long-term buying opportunities in the S&P500 and Dow Industrials.
    Source: http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:coppock_curve
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the CoppockCurve indicator with its default values."""
        ...

    @overload
    def __init__(self, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int) -> None:
        """
        Initializes a new instance of the CoppockCurve indicator
        
        :param shortRocPeriod: The period for the short ROC
        :param longRocPeriod: The period for the long ROC
        :param lwmaPeriod: The period for the LWMA
        """
        ...

    @overload
    def __init__(self, name: str, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int) -> None:
        """
        Initializes a new instance of the CoppockCurve indicator
        
        :param name: A name for the indicator
        :param shortRocPeriod: The period for the short ROC
        :param longRocPeriod: The period for the long ROC
        :param lwmaPeriod: The period for the LWMA
        """
        ...

    def compute_next_value(self, input: QuantConnect.Indicators.IndicatorDataPoint) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class BalanceOfPower(QuantConnect.Indicators.BarIndicator, QuantConnect.Indicators.IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Balance Of Power (BOP).
    The Balance Of Power is calculated with the following formula:
    BOP = (Close - Open) / (High - Low)
    """

    @property
    def is_ready(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @property
    def warm_up_period(self) -> int:
        """Required period, in data points, for the indicator to be ready and fully initialized."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the BalanceOfPower class using the specified name."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the BalanceOfPower class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    def compute_next_value(self, input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class IndicatorDataPoints(QuantConnect.Data.DynamicData):
    """Collection of indicator data points for a given time"""

    @property
    def current(self) -> QuantConnect.Indicators.IndicatorDataPoint:
        """The indicator value at a given point"""
        ...

    @property
    def value(self) -> float:
        """The indicator value at a given point"""
        ...

    def __getitem__(self, name: str) -> QuantConnect.Indicators.IndicatorDataPoint:
        """Access the historical indicator values per indicator property name"""
        ...

    def to_string(self) -> str:
        """String representation"""
        ...


class InternalIndicatorValues(System.Object, typing.Iterable[QuantConnect.Indicators.IndicatorDataPoint]):
    """Internal carrier of an indicator values by property name"""

    @property
    def name(self) -> str:
        """The name of the values associated to this dto"""
        ...

    @property
    def values(self) -> System.Collections.Generic.List[QuantConnect.Indicators.IndicatorDataPoint]:
        """The indicator values"""
        ...

    @property
    def indicator(self) -> QuantConnect.Indicators.IIndicator:
        """
        The target indicator
        
        This property is protected.
        """
        ...

    def __init__(self, indicator: QuantConnect.Indicators.IIndicator, name: str) -> None:
        """Creates a new instance"""
        ...

    @staticmethod
    @overload
    def create(indicator: QuantConnect.Indicators.IIndicator, name: str) -> QuantConnect.Indicators.InternalIndicatorValues:
        """Creates a new instance"""
        ...

    @staticmethod
    @overload
    def create(indicator: QuantConnect.Indicators.IIndicator, property_info: System.Reflection.PropertyInfo) -> QuantConnect.Indicators.InternalIndicatorValues:
        """Creates a new instance"""
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Indicators.IndicatorDataPoint]:
        """Returns an enumerator for the indicator values"""
        ...

    def to_string(self) -> str:
        """String representation"""
        ...

    def update_value(self) -> QuantConnect.Indicators.IndicatorDataPoint:
        """Update with a new indicator point"""
        ...


class _EventContainer(typing.Generic[QuantConnect_Indicators__EventContainer_Callable, QuantConnect_Indicators__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Indicators__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Indicators__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Indicators__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


