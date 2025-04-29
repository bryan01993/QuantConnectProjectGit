from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import QuantConnect.Securities.Interfaces
import System
import System.Collections.Generic


class AdjustmentType(Enum):
    """Enum defines types of possible price adjustments in continuous contract modeling."""

    FORWARD_ADJUSTED = 0

    BACK_ADJUSTED = 1


class IContinuousContractModel(metaclass=abc.ABCMeta):
    """
    Continuous contract model interface. Interfaces is implemented by different classes
    realizing various methods for modeling continuous security series. Primarily, modeling of continuous futures.
    Continuous contracts are used in backtesting of otherwise expiring derivative contracts.
    Continuous contracts are not traded, and are not products traded on exchanges.
    """

    @property
    @abc.abstractmethod
    def adjustment_type(self) -> QuantConnect.Securities.Interfaces.AdjustmentType:
        """Adjustment type, implemented by the model"""
        ...

    @property.setter
    def adjustment_type(self, value: QuantConnect.Securities.Interfaces.AdjustmentType) -> None:
        ...

    @property
    @abc.abstractmethod
    def input_series(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        List of current and historical data series for one root symbol.
        e.g. 6BH16, 6BM16, 6BU16, 6BZ16
        """
        ...

    @property.setter
    def input_series(self, value: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]) -> None:
        ...

    def get_continuous_data(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Method returns continuous prices from the list of current and historical data series for one root symbol.
        It returns enumerator of stitched continuous quotes, produced by the model.
        e.g. 6BH15, 6BM15, 6BU15, 6BZ15 will result in one 6B continuous historical series for 2015
        
        :returns: Continuous prices.
        """
        ...

    def get_current_symbol(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Symbol:
        """
        Returns current symbol name that corresponds to the current continuous model,
        or null if none.
        
        :returns: Current symbol name.
        """
        ...

    def get_roll_dates(self) -> System.Collections.Generic.IEnumerator[datetime.datetime]:
        """
        Returns the list of roll dates for the contract.
        
        :returns: The list of roll dates.
        """
        ...


class ISecurityDataFilter(metaclass=abc.ABCMeta):
    """Security data filter interface. Defines pattern for the user defined data filter techniques."""

    def filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Filter out a tick from this security, with this new data:
        
        :param vehicle: Security of this filter.
        :param data: New data packet we're checking
        """
        ...


