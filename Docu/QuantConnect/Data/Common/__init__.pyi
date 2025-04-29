from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Common
import QuantConnect.Data.Consolidators
import QuantConnect.Securities
import System

QuantConnect_Data_Common__EventContainer_Callable = typing.TypeVar("QuantConnect_Data_Common__EventContainer_Callable")
QuantConnect_Data_Common__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Data_Common__EventContainer_ReturnType")


class MarketHourAwareConsolidator(System.Object, QuantConnect.Data.Consolidators.IDataConsolidator):
    """Consolidator for open markets bar only, extended hours bar are not consolidated."""

    @property
    def period(self) -> datetime.timedelta:
        """
        The consolidation period requested
        
        This property is protected.
        """
        ...

    @property
    def consolidator(self) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        The consolidator instance
        
        This property is protected.
        """
        ...

    @property
    def exchange_hours(self) -> QuantConnect.Securities.SecurityExchangeHours:
        """
        The associated security exchange hours instance
        
        This property is protected.
        """
        ...

    @property.setter
    def exchange_hours(self, value: QuantConnect.Securities.SecurityExchangeHours) -> None:
        ...

    @property
    def data_time_zone(self) -> typing.Any:
        """
        The associated data time zone
        
        This property is protected.
        """
        ...

    @property.setter
    def data_time_zone(self, value: typing.Any) -> None:
        ...

    @property
    def consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @property
    def input_type(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    @property
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    def __init__(self, dailyStrictEndTimeEnabled: bool, resolution: QuantConnect.Resolution, dataType: typing.Type, tickType: QuantConnect.TickType, extendedMarketHours: bool) -> None:
        """
        Initializes a new instance of the MarketHourAwareConsolidator class.
        
        :param resolution: The resolution.
        :param dataType: The target data type
        :param tickType: The target tick type
        :param extendedMarketHours: True if extended market hours should be consolidated
        """
        ...

    def daily_strict_end_time(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Consolidators.CalendarInfo:
        """
        Determines a bar start time and period
        
        This method is protected.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def forward_consolidated_bar(self, sender: typing.Any, consolidated: QuantConnect.Data.IBaseData) -> None:
        """
        Will forward the underlying consolidated bar to consumers on this object
        
        This method is protected.
        """
        ...

    def initialize(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Perform late initialization based on the datas symbol
        
        This method is protected.
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as QuantConnect.Data.BaseData.Time)
        """
        ...

    def update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...

    def use_strict_end_time(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Useful for testing
        
        This method is protected.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Data_Common__EventContainer_Callable, QuantConnect_Data_Common__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Data_Common__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Data_Common__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Data_Common__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


