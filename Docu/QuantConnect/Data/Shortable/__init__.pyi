from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Data.Shortable
import QuantConnect.Interfaces
import QuantConnect.Python
import System


class LocalDiskShortableProvider(System.Object, QuantConnect.Interfaces.IShortableProvider):
    """Sources short availability data from the local disk for the given brokerage"""

    data_provider: QuantConnect.Interfaces.IDataProvider = ...
    """
    The data provider instance to use
    
    This field is protected.
    """

    @property
    def brokerage(self) -> str:
        """
        The short availability provider
        
        This property is protected.
        """
        ...

    @property.setter
    def brokerage(self, value: str) -> None:
        ...

    def __init__(self, brokerage: str) -> None:
        """
        Creates an instance of the class. Establishes the directory to read from.
        
        :param brokerage: Brokerage to read the short availability data
        """
        ...

    def fee_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets interest rate charged on borrowed shares for a given asset.
        
        :param symbol: Symbol to lookup fee rate
        :param local_time: Time of the algorithm
        :returns: Fee rate. Zero if the data for the brokerage/date does not exist.
        """
        ...

    def rebate_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the Fed funds or other currency-relevant benchmark rate minus the interest rate charged on borrowed shares for a given asset.
        E.g.: Interest rate - borrow fee rate = borrow rebate rate: 5.32% - 0.25% = 5.07%.
        
        :param symbol: Symbol to lookup rebate rate
        :param local_time: Time of the algorithm
        :returns: Rebate fee. Zero if the data for the brokerage/date does not exist.
        """
        ...

    def shortable_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> typing.Optional[int]:
        """
        Gets the quantity shortable for the Symbol at the given date.
        
        :param symbol: Symbol to lookup shortable quantity
        :param local_time: Time of the algorithm
        :returns: Quantity shortable. Null if the data for the brokerage/date does not exist.
        """
        ...


class InteractiveBrokersShortableProvider(QuantConnect.Data.Shortable.LocalDiskShortableProvider):
    """Sources the InteractiveBrokers short availability data from the local disk for the given brokerage"""

    def __init__(self) -> None:
        """Creates a new instance"""
        ...


class NullShortableProvider(System.Object, QuantConnect.Interfaces.IShortableProvider):
    """
    Defines the default shortable provider in the case that no local data exists.
    This will allow for all assets to be infinitely shortable, with no restrictions.
    """

    INSTANCE: QuantConnect.Data.Shortable.NullShortableProvider
    """The null shortable provider instance"""

    def fee_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets interest rate charged on borrowed shares for a given asset.
        
        :param symbol: Symbol to lookup fee rate
        :param local_time: Time of the algorithm
        :returns: zero indicating that it is does have borrowing costs.
        """
        ...

    def rebate_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the Fed funds or other currency-relevant benchmark rate minus the interest rate charged on borrowed shares for a given asset.
        E.g.: Interest rate - borrow fee rate = borrow rebate rate: 5.32% - 0.25% = 5.07%.
        
        :param symbol: Symbol to lookup rebate rate
        :param local_time: Time of the algorithm
        :returns: zero indicating that it is does have borrowing costs.
        """
        ...

    def shortable_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> typing.Optional[int]:
        """
        Gets the quantity shortable for the Symbol at the given time.
        
        :param symbol: Symbol to check
        :param local_time: Local time of the algorithm
        :returns: null, indicating that it is infinitely shortable.
        """
        ...


class ShortableProviderPythonWrapper(QuantConnect.Python.BasePythonWrapper[QuantConnect.Interfaces.IShortableProvider], QuantConnect.Interfaces.IShortableProvider):
    """Python wrapper for custom shortable providers"""

    def __init__(self, shortableProvider: typing.Any) -> None:
        """
        Creates a new instance
        
        :param shortableProvider: The python custom shortable provider
        """
        ...

    def fee_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the fee rate for the Symbol at the given date.
        
        :param symbol: Symbol to lookup fee rate
        :param local_time: Time of the algorithm
        :returns: zero indicating that it is does have borrowing costs.
        """
        ...

    def rebate_rate(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the Fed funds or other currency-relevant benchmark rate minus the interest rate charged on borrowed shares for a given asset.
        E.g.: Interest rate - borrow fee rate = borrow rebate rate: 5.32% - 0.25% = 5.07%.
        
        :param symbol: Symbol to lookup rebate rate
        :param local_time: Time of the algorithm
        :returns: zero indicating that it is does have borrowing costs.
        """
        ...

    def shortable_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str], local_time: typing.Union[datetime.datetime, datetime.date]) -> typing.Optional[int]:
        """
        Gets the quantity shortable for a Symbol, from python custom shortable provider
        
        :param symbol: Symbol to check shortable quantity
        :param local_time: Local time of the algorithm
        :returns: The quantity shortable for the given Symbol as a positive number. Null if the Symbol is shortable without restrictions.
        """
        ...


