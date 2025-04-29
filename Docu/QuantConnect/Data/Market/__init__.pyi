from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Securities
import System
import System.Collections.Generic
import System.IO

QuantConnect_Data_Market_DataDictionary_T = typing.TypeVar("QuantConnect_Data_Market_DataDictionary_T")
QuantConnect_Data_Market_DataDictionaryExtensions_Add_T = typing.TypeVar("QuantConnect_Data_Market_DataDictionaryExtensions_Add_T")
QuantConnect_Data_Market_TradeBar_ParseEquity_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseEquity_T")
QuantConnect_Data_Market_TradeBar_ParseForex_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseForex_T")
QuantConnect_Data_Market_TradeBar_ParseCrypto_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseCrypto_T")
QuantConnect_Data_Market_TradeBar_ParseCfd_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseCfd_T")
QuantConnect_Data_Market_TradeBar_ParseOption_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseOption_T")
QuantConnect_Data_Market_TradeBar_ParseFuture_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseFuture_T")
QuantConnect_Data_Market_FuturesChain_GetAux_T = typing.TypeVar("QuantConnect_Data_Market_FuturesChain_GetAux_T")
QuantConnect_Data_Market_FuturesChain_GetAuxList_T = typing.TypeVar("QuantConnect_Data_Market_FuturesChain_GetAuxList_T")
QuantConnect_Data_Market_OptionChain_GetAux_T = typing.TypeVar("QuantConnect_Data_Market_OptionChain_GetAux_T")
QuantConnect_Data_Market_OptionChain_GetAuxList_T = typing.TypeVar("QuantConnect_Data_Market_OptionChain_GetAuxList_T")


class DataDictionary(typing.Generic[QuantConnect_Data_Market_DataDictionary_T], QuantConnect.ExtendedDictionary[QuantConnect_Data_Market_DataDictionary_T], System.Collections.Generic.IDictionary[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T], typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]]):
    """Provides a base class for types holding base data instances keyed by symbol"""

    @property
    def time(self) -> datetime.datetime:
        """Gets or sets the time associated with this collection of data"""
        ...

    @property.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def count(self) -> int:
        """Gets the number of elements contained in the System.Collections.Generic.ICollection`1."""
        ...

    @property
    def is_read_only(self) -> bool:
        """Gets a value indicating whether the System.Collections.Generic.ICollection`1 is read-only."""
        ...

    @property
    def keys(self) -> System.Collections.Generic.ICollection[QuantConnect.Symbol]:
        """Gets an System.Collections.Generic.ICollection`1 containing the keys of the System.Collections.Generic.IDictionary`2."""
        ...

    @property
    def values(self) -> System.Collections.Generic.ICollection[QuantConnect_Data_Market_DataDictionary_T]:
        """Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2."""
        ...

    @property
    def get_keys(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the Symbol objects of the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    @property
    def get_values(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Data_Market_DataDictionary_T]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_DataDictionary_T:
        """
        Gets or sets the element with the specified key.
        
        :param symbol: The key of the element to get or set.
        :returns: The element with the specified key.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the QuantConnect.Data.Market.DataDictionary{T} class."""
        ...

    @overload
    def __init__(self, data: System.Collections.Generic.IEnumerable[QuantConnect_Data_Market_DataDictionary_T], keySelector: typing.Callable[[QuantConnect_Data_Market_DataDictionary_T], QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the QuantConnect.Data.Market.DataDictionary{T} class
        using the specified  as a data source
        
        :param data: The data source for this data dictionary
        :param keySelector: Delegate used to select a key from the value
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the QuantConnect.Data.Market.DataDictionary{T} class.
        
        :param time: The time this data was emitted.
        """
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect_Data_Market_DataDictionary_T) -> None:
        """
        Gets or sets the element with the specified key.
        
        :param symbol: The key of the element to get or set.
        :returns: The element with the specified key.
        """
        ...

    @overload
    def add(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]) -> None:
        """
        Adds an item to the System.Collections.Generic.ICollection`1.
        
        :param item: The object to add to the System.Collections.Generic.ICollection`1.
        """
        ...

    @overload
    def add(self, key: typing.Union[QuantConnect.Symbol, str], value: QuantConnect_Data_Market_DataDictionary_T) -> None:
        """
        Adds an element with the provided key and value to the System.Collections.Generic.IDictionary{TKey, TValue}.
        
        :param key: The object to use as the key of the element to add.
        :param value: The object to use as the value of the element to add.
        """
        ...

    def clear(self) -> None:
        """Removes all items from the System.Collections.Generic.ICollection`1."""
        ...

    def contains(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]) -> bool:
        """
        Determines whether the System.Collections.Generic.ICollection`1 contains a specific value.
        
        :param item: The object to locate in the System.Collections.Generic.ICollection`1.
        :returns: true if  is found in the System.Collections.Generic.ICollection`1; otherwise, false.
        """
        ...

    def contains_key(self, key: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines whether the System.Collections.Generic.IDictionary{TKey, TValue} contains an element with the specified key.
        
        :param key: The key to locate in the System.Collections.Generic.IDictionary{TKey, TValue}.
        :returns: true if the System.Collections.Generic.IDictionary{TKey, TValue} contains an element with the key; otherwise, false.
        """
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]], array_index: int) -> None:
        """
        Copies the elements of the System.Collections.Generic.ICollection`1 to an System.Array, starting at a particular System.Array index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection`1. The System.Array must have zero-based indexing.
        :param array_index: The zero-based index in  at which copying begins.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    def get_value(self, key: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_DataDictionary_T:
        """
        Gets the value associated with the specified key.
        
        :param key: The key whose value to get.
        :returns: The value associated with the specified key, if the key is found; otherwise, the default value for the type of the T parameter.
        """
        ...

    @overload
    def remove(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]) -> bool:
        """
        Removes the first occurrence of a specific object from the System.Collections.Generic.ICollection`1.
        
        :param item: The object to remove from the System.Collections.Generic.ICollection`1.
        :returns: true if  was successfully removed from the System.Collections.Generic.ICollection`1; otherwise, false. This method also returns false if  is not found in the original System.Collections.Generic.ICollection`1.
        """
        ...

    @overload
    def remove(self, key: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Removes the element with the specified key from the System.Collections.Generic.IDictionary{TKey, TValue}.
        
        :param key: The key of the element to remove.
        :returns: true if the element is successfully removed; otherwise, false.  This method also returns false if  was not found in the original System.Collections.Generic.IDictionary{TKey, TValue}.
        """
        ...

    def try_get_value(self, key: typing.Union[QuantConnect.Symbol, str], value: typing.Optional[QuantConnect_Data_Market_DataDictionary_T]) -> typing.Union[bool, QuantConnect_Data_Market_DataDictionary_T]:
        """
        Gets the value associated with the specified key.
        
        :param key: The key whose value to get.
        :param value: When this method returns, the value associated with the specified key, if the key is found; otherwise, the default value for the type of the  parameter. This parameter is passed uninitialized.
        :returns: true if the object that implements System.Collections.Generic.IDictionary{TKey, TValue} contains an element with the specified key; otherwise, false.
        """
        ...


class MarginInterestRate(QuantConnect.Data.BaseData):
    """Margin interest rate data source"""

    @property
    def interest_rate(self) -> float:
        """The interest rate value"""
        ...

    @property.setter
    def interest_rate(self, value: float) -> None:
        ...

    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    def data_time_zone(self) -> typing.Any:
        """Specifies the data time zone for this data type. This is useful for custom data types"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param stream: The data stream
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the symbol and value."""
        ...


class MarginInterestRates(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.MarginInterestRate]):
    """Collection of dividends keyed by Symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.MarginInterestRate:
        """
        Gets or sets the Dividend with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Dividend with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.MarginInterestRate:
        """
        Gets or sets the Dividend with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Dividend with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the MarginInterestRate dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the MarginInterestRate dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.MarginInterestRate) -> None:
        """
        Gets or sets the Dividend with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Dividend with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.MarginInterestRate) -> None:
        """
        Gets or sets the Dividend with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Dividend with the specified Symbol.
        """
        ...


class SymbolChangedEvent(QuantConnect.Data.BaseData):
    """
    Symbol changed event of a security. This is generated when a symbol is remapped for a given
    security, for example, at EOD 2014.04.02 GOOG turned into GOOGL, but are the same
    """

    @property
    def old_symbol(self) -> str:
        """Gets the symbol before the change"""
        ...

    @property
    def new_symbol(self) -> str:
        """Gets the symbol after the change"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the SymbolChangedEvent class"""
        ...

    @overload
    def __init__(self, requestedSymbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], oldSymbol: str, newSymbol: str) -> None:
        """
        Initializes a new instance of the SymbolChangedEvent
        
        :param requestedSymbol: The symbol that was originally requested
        :param date: The date/time this symbol remapping took place
        :param oldSymbol: The old symbol mapping
        :param newSymbol: The new symbol mapping
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def to_string(self) -> str:
        """Friendly string representation of this symbol changed event"""
        ...


class Delisting(QuantConnect.Data.BaseData):
    """Delisting event of a security"""

    @property
    def type(self) -> QuantConnect.DelistingType:
        """
        Gets the type of delisting, warning or delisted
        A DelistingType.Warning is sent
        """
        ...

    @property
    def ticket(self) -> QuantConnect.Orders.OrderTicket:
        """Gets the OrderTicket that was submitted to liquidate this position"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Delisting class"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], price: float, type: QuantConnect.DelistingType) -> None:
        """
        Initializes a new instance of the Delisting class
        
        :param symbol: The delisted symbol
        :param date: The date the symbol was delisted
        :param price: The final price before delisting
        :param type: The type of delisting event
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def set_order_ticket(self, ticket: QuantConnect.Orders.OrderTicket) -> None:
        """
        Sets the OrderTicket used to liquidate this position
        
        :param ticket: The ticket that represents the order to liquidate this position
        """
        ...

    def to_string(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...


class RenkoType(Enum):
    """
    The type of the RenkoBar being created.
    Used by RenkoConsolidator, ClassicRenkoConsolidator and VolumeRenkoConsolidator
    """

    CLASSIC = 0
    """
    Indicates that the RenkoConsolidator works in its
    original implementation; Specifically:
    - It only returns a single bar, at most, irrespective of tick movement
    - It will emit consecutive bars side by side
    - By default even bars are created
    (0)
    """

    WICKED = 1
    """
    Indicates that the RenkoConsolidator works properly;
    Specifically:
    - returns zero or more bars per tick, as appropriate.
    - Will not emit consecutive bars side by side
    - Creates
    (1)
    """


class IBar(metaclass=abc.ABCMeta):
    """Generic bar interface with Open, High, Low and Close."""

    @property
    @abc.abstractmethod
    def open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property
    @abc.abstractmethod
    def high(self) -> float:
        """High price of the bar during the time period."""
        ...

    @property
    @abc.abstractmethod
    def low(self) -> float:
        """Low price of the bar during the time period."""
        ...

    @property
    @abc.abstractmethod
    def close(self) -> float:
        """Closing price of the bar. Defined as the price at Start Time + TimeSpan."""
        ...


class IBaseDataBar(QuantConnect.Data.IBaseData, QuantConnect.Data.Market.IBar, metaclass=abc.ABCMeta):
    """Represents a type that is both a bar and base data"""


class TradeBar(QuantConnect.Data.BaseData, QuantConnect.Data.Market.IBaseDataBar):
    """
    TradeBar class for second and minute resolution data:
    An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    """

    @property
    def volume(self) -> float:
        """Volume:"""
        ...

    @property.setter
    def volume(self, value: float) -> None:
        ...

    @property
    def open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property.setter
    def open(self, value: float) -> None:
        ...

    @property
    def high(self) -> float:
        """High price of the TradeBar during the time period."""
        ...

    @property.setter
    def high(self, value: float) -> None:
        ...

    @property
    def low(self) -> float:
        """Low price of the TradeBar during the time period."""
        ...

    @property.setter
    def low(self, value: float) -> None:
        ...

    @property
    def close(self) -> float:
        """Closing price of the TradeBar. Defined as the price at Start Time + TimeSpan."""
        ...

    @property.setter
    def close(self, value: float) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The closing time of this bar, computed via the Time and Period"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def period(self) -> datetime.timedelta:
        """The period of this trade bar, (second, minute, daily, ect...)"""
        ...

    @property.setter
    def period(self, value: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default initializer to setup an empty tradebar."""
        ...

    @overload
    def __init__(self, original: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Cloner constructor for implementing fill forward.
        Return a new instance with the same values as this original.
        
        :param original: Original tradebar object we seek to clone
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], open: float, high: float, low: float, close: float, volume: float, period: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initialize Trade Bar with OHLC Values:
        
        :param time: DateTime Timestamp of the bar
        :param symbol: Market MarketType Symbol
        :param open: Decimal Opening Price
        :param high: Decimal High Price of this bar
        :param low: Decimal Low Price of this bar
        :param close: Decimal Close price of this bar
        :param volume: Volume sum over day
        :param period: The period of this bar, specify null for default of 1 minute
        """
        ...

    @overload
    def clone(self, fill_forward: bool) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :param fill_forward: True if this is a fill forward clone
        :returns: A clone of the current object.
        """
        ...

    @overload
    def clone(self) -> QuantConnect.Data.BaseData:
        """Return a new instance clone of this object"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get Source for Custom Data File
        >> What source file location would you prefer for each type of usage:
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file.
        """
        ...

    @staticmethod
    def parse(config: QuantConnect.Data.SubscriptionDataConfig, line: str, base_date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """Parses the trade bar data line assuming QC data formats"""
        ...

    @staticmethod
    @overload
    def parse_cfd(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseCfd_T:
        """
        Parses CFD trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_cfd(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses CFD trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_cfd(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses CFD trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_crypto(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseCrypto_T:
        """
        Parses crypto trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_crypto(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses crypto trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_crypto(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses crypto trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_equity(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseEquity_T:
        """
        Parses equity trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        """
        ...

    @staticmethod
    @overload
    def parse_equity(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses equity trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: Date of this reader request
        """
        ...

    @staticmethod
    @overload
    def parse_equity(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses equity trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        """
        ...

    @staticmethod
    @overload
    def parse_forex(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseForex_T:
        """
        Parses forex trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_forex(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses forex trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_forex(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses forex trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_future(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseFuture_T:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_future(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseFuture_T:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_future(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_future(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_index(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """Parse an index bar from the LEAN disk format"""
        ...

    @staticmethod
    @overload
    def parse_index(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """Parse an index bar from the LEAN disk format"""
        ...

    @staticmethod
    @overload
    def parse_option(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseOption_T:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_option(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseOption_T:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_option(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def parse_option(config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param stream_reader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        TradeBar Reader: Fetch the data from the QC storage and feed it line by line into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        TradeBar Reader: Fetch the data from the QC storage and feed it directly from the stream into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param stream: The file data stream
        :param date: Date of this reader request
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    def to_string(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...

    def update(self, last_trade: float, bid_price: float, ask_price: float, volume: float, bid_size: float, ask_size: float) -> None:
        """
        Update the tradebar - build the bar from this pricing information:
        
        :param last_trade: This trade price
        :param bid_price: Current bid price (not used)
        :param ask_price: Current asking price (not used)
        :param volume: Volume of this trade
        :param bid_size: The size of the current bid, if available
        :param ask_size: The size of the current ask, if available
        """
        ...


class RangeBar(QuantConnect.Data.Market.TradeBar):
    """Represents a bar sectioned not by time, but by some amount of movement in a value (for example, Closing price moving in $10 bar sizes)"""

    @property
    def range_size(self) -> float:
        """Gets the range of the bar."""
        ...

    @property
    def is_closed(self) -> bool:
        """Gets whether or not this bar is considered closed."""
        ...

    @overload
    def __init__(self) -> None:
        """Initialize a new default instance of RangeBar class."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], endTime: typing.Union[datetime.datetime, datetime.date], rangeSize: float, open: float, high: typing.Optional[float] = None, low: typing.Optional[float] = None, close: typing.Optional[float] = None, volume: float = 0) -> None:
        """
        Initializes a new instance of the RangeBar class with the specified values
        
        :param symbol: The symbol of this data
        :param endTime: The end time of the bar
        :param rangeSize: The size of each range bar
        :param open: The opening price for the new bar
        :param high: The high price for the new bar
        :param low: The low price for the new bar
        :param close: The closing price for the new bar
        :param volume: The volume value for the new bar
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def update(self, time: typing.Union[datetime.datetime, datetime.date], current_value: float, volume_since_last_update: float) -> None:
        """
        Updates this RangeBar with the specified values
        
        :param time: The current time
        :param current_value: The current value
        :param volume_since_last_update: The volume since the last update called on this instance
        """
        ...


class SymbolChangedEvents(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.SymbolChangedEvent]):
    """Collection of SymbolChangedEvent keyed by the original, requested symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.SymbolChangedEvent:
        """
        Gets or sets the SymbolChangedEvent with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The SymbolChangedEvent with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.SymbolChangedEvent:
        """
        Gets or sets the SymbolChangedEvent with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The SymbolChangedEvent with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the SymbolChangedEvent dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the SymbolChangedEvent dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.SymbolChangedEvent) -> None:
        """
        Gets or sets the SymbolChangedEvent with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The SymbolChangedEvent with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.SymbolChangedEvent) -> None:
        """
        Gets or sets the SymbolChangedEvent with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The SymbolChangedEvent with the specified Symbol.
        """
        ...


class Tick(QuantConnect.Data.BaseData):
    """
    Tick class is the base representation for tick data. It is grouped into a Ticks object
    which implements IDictionary and passed into an OnData event handler.
    """

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """Type of the Tick: Trade or Quote."""
        ...

    @property.setter
    def tick_type(self, value: QuantConnect.TickType) -> None:
        ...

    @property
    def quantity(self) -> float:
        """Quantity exchanged in a trade."""
        ...

    @property.setter
    def quantity(self, value: float) -> None:
        ...

    @property
    def exchange_code(self) -> str:
        """Exchange code this tick came from Exchanges"""
        ...

    @property.setter
    def exchange_code(self, value: str) -> None:
        ...

    @property
    def exchange(self) -> str:
        """Exchange name this tick came from Exchanges"""
        ...

    @property.setter
    def exchange(self, value: str) -> None:
        ...

    @property
    def sale_condition(self) -> str:
        """Sale condition for the tick."""
        ...

    @property.setter
    def sale_condition(self, value: str) -> None:
        ...

    @property
    def parsed_sale_condition(self) -> int:
        """For performance parsed sale condition for the tick."""
        ...

    @property.setter
    def parsed_sale_condition(self, value: int) -> None:
        ...

    @property
    def suspicious(self) -> bool:
        """Bool whether this is a suspicious tick"""
        ...

    @property.setter
    def suspicious(self, value: bool) -> None:
        ...

    @property
    def bid_price(self) -> float:
        """Bid Price for Tick"""
        ...

    @property.setter
    def bid_price(self, value: float) -> None:
        ...

    @property
    def ask_price(self) -> float:
        """Asking price for the Tick quote."""
        ...

    @property.setter
    def ask_price(self, value: float) -> None:
        ...

    @property
    def last_price(self) -> float:
        """Alias for "Value" - the last sale for this asset."""
        ...

    @property
    def bid_size(self) -> float:
        """Size of bid quote."""
        ...

    @property.setter
    def bid_size(self, value: float) -> None:
        ...

    @property
    def ask_size(self) -> float:
        """Size of ask quote."""
        ...

    @property.setter
    def ask_size(self, value: float) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initialize tick class with a default constructor."""
        ...

    @overload
    def __init__(self, original: QuantConnect.Data.Market.Tick) -> None:
        """
        Cloner constructor for fill forward engine implementation. Clone the original tick into this new tick:
        
        :param original: Original tick we're cloning
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], bid: float, ask: float) -> None:
        """
        Constructor for a FOREX tick where there is no last sale price. The volume in FX is so high its rare to find FX trade data.
        To fake this the tick contains bid-ask prices and the last price is the midpoint.
        
        :param time: Full date and time
        :param symbol: Underlying currency pair we're trading
        :param bid: FX tick bid value
        :param ask: FX tick ask value
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], openInterest: float) -> None:
        """
        Initializes a new instance of the Tick class to TickType.OpenInterest.
        
        :param time: The time at which the open interest tick occurred.
        :param symbol: The symbol associated with the open interest tick.
        :param openInterest: The value of the open interest for the specified symbol.
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], last: float, bid: float, ask: float) -> None:
        """
        Initializer for a last-trade equity tick with bid or ask prices.
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param last: Last trade price
        :param bid: Bid value
        :param ask: Ask value
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], saleCondition: str, exchange: str, quantity: float, price: float) -> None:
        """
        Trade tick type constructor
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param saleCondition: The ticks sale condition
        :param exchange: The ticks exchange
        :param quantity: The quantity traded
        :param price: The price of the trade
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], saleCondition: str, exchange: QuantConnect.Exchange, quantity: float, price: float) -> None:
        """
        Trade tick type constructor
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param saleCondition: The ticks sale condition
        :param exchange: The ticks exchange
        :param quantity: The quantity traded
        :param price: The price of the trade
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], saleCondition: str, exchange: str, bidSize: float, bidPrice: float, askSize: float, askPrice: float) -> None:
        """
        Quote tick type constructor
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param saleCondition: The ticks sale condition
        :param exchange: The ticks exchange
        :param bidSize: The bid size
        :param bidPrice: The bid price
        :param askSize: The ask size
        :param askPrice: The ask price
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], saleCondition: str, exchange: QuantConnect.Exchange, bidSize: float, bidPrice: float, askSize: float, askPrice: float) -> None:
        """
        Quote tick type constructor
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param saleCondition: The ticks sale condition
        :param exchange: The ticks exchange
        :param bidSize: The bid size
        :param bidPrice: The bid price
        :param askSize: The ask size
        :param askPrice: The ask price
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], line: str) -> None:
        """
        Constructor for QuantConnect FXCM Data source:
        
        :param symbol: Symbol for underlying asset
        :param line: CSV line of data from FXCM
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], line: str, baseDate: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Constructor for QuantConnect tick data
        
        :param symbol: Symbol for underlying asset
        :param line: CSV line of data from QC tick csv
        :param baseDate: The base date of the tick
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Parse a tick data line from quantconnect zip source files.
        
        :param config: Subscription configuration object
        :param reader: The source stream reader
        :param date: Base date for the tick (ticks date is stored as int milliseconds since midnight)
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Parse a tick data line from quantconnect zip source files.
        
        :param config: Subscription configuration object
        :param line: CSV source line of the compressed source
        :param date: Base date for the tick (ticks date is stored as int milliseconds since midnight)
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clone implementation for tick class:
        
        :returns: New tick object clone of the current class values.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get source for tick data feed - not used with QuantConnect data sources implementation.
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file to be opened with a stream.
        """
        ...

    def is_valid(self) -> bool:
        """Check if tick contains valid data (either a trade, or a bid or ask)"""
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Tick implementation of reader method: read a line of data from the source and convert it to a tick object.
        
        :param config: Subscription configuration object for algorithm
        :param line: Line from the datafeed source
        :param date: Date of this reader request
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: New Initialized tick.
        """
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Tick implementation of reader method: read a line of data from the source and convert it to a tick object.
        
        :param config: Subscription configuration object for algorithm
        :param stream: The source stream reader
        :param date: Date of this reader request
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: New Initialized tick.
        """
        ...

    def set_value(self) -> None:
        """Sets the tick Value based on ask and bid price"""
        ...

    def to_string(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...

    def update(self, last_trade: float, bid_price: float, ask_price: float, volume: float, bid_size: float, ask_size: float) -> None:
        """
        Update the tick price information - not used.
        
        :param last_trade: This trade price
        :param bid_price: Current bid price
        :param ask_price: Current asking price
        :param volume: Volume of this trade
        :param bid_size: The size of the current bid, if available
        :param ask_size: The size of the current ask, if available
        """
        ...


class OpenInterest(QuantConnect.Data.Market.Tick):
    """Defines a data type that represents open interest for given security"""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the OpenInterest class"""
        ...

    @overload
    def __init__(self, original: QuantConnect.Data.Market.OpenInterest) -> None:
        """
        Cloner constructor for fill forward engine implementation. Clone the original OI into this new one:
        
        :param original: Original OI we're cloning
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], openInterest: float) -> None:
        """
        Initializes a new instance of the OpenInterest class with data
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param openInterest: Open Interest value
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, symbol: typing.Union[QuantConnect.Symbol, str], line: str, baseDate: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Constructor for QuantConnect open interest data
        
        :param config: Subscription configuration
        :param symbol: Symbol for underlying asset
        :param line: CSV line of data from QC OI csv
        :param baseDate: The base date of the OI
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Parse an open interest data line from quantconnect zip source files.
        
        :param config: Subscription configuration object
        :param line: CSV source line of the compressed source
        :param date: Base date for the open interest (date is stored as int milliseconds since midnight)
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clone implementation for open interest class:
        
        :returns: New tick object clone of the current class values.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get source for OI data feed - not used with QuantConnect data sources implementation.
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file to be opened with a stream.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Tick implementation of reader method: read a line of data from the source and convert it to an open interest object.
        
        :param config: Subscription configuration object for algorithm
        :param line: Line from the datafeed source
        :param date: Date of this reader request
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: New initialized open interest object.
        """
        ...


class DataDictionaryExtensions(System.Object):
    """Provides extension methods for the DataDictionary class"""

    @staticmethod
    def add(dictionary: QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Market_DataDictionaryExtensions_Add_T], data: QuantConnect_Data_Market_DataDictionaryExtensions_Add_T) -> None:
        """Provides a convenience method for adding a base data instance to our data dictionary"""
        ...


class Ticks(QuantConnect.Data.Market.DataDictionary[System.Collections.Generic.List[QuantConnect.Data.Market.Tick]]):
    """Ticks collection which implements an IDictionary-string-list of ticks. This way users can iterate over the string indexed ticks of the requested symbol."""

    @overload
    def __getitem__(self, ticker: str) -> System.Collections.Generic.List[QuantConnect.Data.Market.Tick]:
        """
        Gets or sets the list of Tick with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The list of Tick with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect.Data.Market.Tick]:
        """
        Gets or sets the list of Tick with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The list of Tick with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Ticks dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Ticks dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: System.Collections.Generic.List[QuantConnect.Data.Market.Tick]) -> None:
        """
        Gets or sets the list of Tick with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The list of Tick with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: System.Collections.Generic.List[QuantConnect.Data.Market.Tick]) -> None:
        """
        Gets or sets the list of Tick with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The list of Tick with the specified Symbol.
        """
        ...


class TradeBars(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.TradeBar]):
    """Collection of TradeBars to create a data type for generic data handler:"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.TradeBar:
        """
        Gets or sets the TradeBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The TradeBar with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.TradeBar:
        """
        Gets or sets the TradeBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The TradeBar with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the TradeBars dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Creates a new instance of the TradeBars dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Gets or sets the TradeBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The TradeBar with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Gets or sets the TradeBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The TradeBar with the specified Symbol.
        """
        ...


class Bar(System.Object, QuantConnect.Data.Market.IBar):
    """Base Bar Class: Open, High, Low, Close and Period."""

    @property
    def open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property.setter
    def open(self, value: float) -> None:
        ...

    @property
    def high(self) -> float:
        """High price of the bar during the time period."""
        ...

    @property.setter
    def high(self, value: float) -> None:
        ...

    @property
    def low(self) -> float:
        """Low price of the bar during the time period."""
        ...

    @property.setter
    def low(self, value: float) -> None:
        ...

    @property
    def close(self) -> float:
        """Closing price of the bar. Defined as the price at Start Time + TimeSpan."""
        ...

    @property.setter
    def close(self, value: float) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default initializer to setup an empty bar."""
        ...

    @overload
    def __init__(self, open: float, high: float, low: float, close: float) -> None:
        """
        Initializer to setup a bar with a given information.
        
        :param open: Decimal Opening Price
        :param high: Decimal High Price of this bar
        :param low: Decimal Low Price of this bar
        :param close: Decimal Close price of this bar
        """
        ...

    def clone(self) -> QuantConnect.Data.Market.Bar:
        """Returns a clone of this bar"""
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    @overload
    def update(self, value: float) -> None:
        """
        Updates the bar with a new value. This will aggregate the OHLC bar
        
        :param value: The new value
        """
        ...

    @overload
    def update(self, value: float) -> None:
        """
        Updates the bar with a new value. This will aggregate the OHLC bar
        
        :param value: The new value
        """
        ...


class QuoteBar(QuantConnect.Data.BaseData, QuantConnect.Data.Market.IBaseDataBar):
    """
    QuoteBar class for second and minute resolution data:
    An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    """

    @property
    def last_bid_size(self) -> float:
        """Average bid size"""
        ...

    @property.setter
    def last_bid_size(self, value: float) -> None:
        ...

    @property
    def last_ask_size(self) -> float:
        """Average ask size"""
        ...

    @property.setter
    def last_ask_size(self, value: float) -> None:
        ...

    @property
    def bid(self) -> QuantConnect.Data.Market.Bar:
        """Bid OHLC"""
        ...

    @property.setter
    def bid(self, value: QuantConnect.Data.Market.Bar) -> None:
        ...

    @property
    def ask(self) -> QuantConnect.Data.Market.Bar:
        """Ask OHLC"""
        ...

    @property.setter
    def ask(self, value: QuantConnect.Data.Market.Bar) -> None:
        ...

    @property
    def open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property
    def high(self) -> float:
        """High price of the QuoteBar during the time period."""
        ...

    @property
    def low(self) -> float:
        """Low price of the QuoteBar during the time period."""
        ...

    @property
    def close(self) -> float:
        """Closing price of the QuoteBar. Defined as the price at Start Time + TimeSpan."""
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The closing time of this bar, computed via the Time and Period"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def period(self) -> datetime.timedelta:
        """The period of this quote bar, (second, minute, daily, ect...)"""
        ...

    @property.setter
    def period(self, value: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default initializer to setup an empty quotebar."""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], bid: QuantConnect.Data.Market.IBar, lastBidSize: float, ask: QuantConnect.Data.Market.IBar, lastAskSize: float, period: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initialize Quote Bar with Bid(OHLC) and Ask(OHLC) Values:
        
        :param time: DateTime Timestamp of the bar
        :param symbol: Market MarketType Symbol
        :param bid: Bid OLHC bar
        :param lastBidSize: Average bid size over period
        :param ask: Ask OLHC bar
        :param lastAskSize: Average ask size over period
        :param period: The period of this bar, specify null for default of 1 minute
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this quote bar, used in fill forward
        
        :returns: A clone of the current quote bar.
        """
        ...

    def collapse(self) -> QuantConnect.Data.Market.TradeBar:
        """
        Collapses QuoteBars into TradeBars object when
         algorithm requires FX data, but calls OnData(TradeBars)
        TODO: (2017) Remove this method in favor of using OnData(Slice)
        
        :returns: TradeBars.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get Source for Custom Data File
        >> What source file location would you prefer for each type of usage:
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file.
        """
        ...

    @overload
    def parse_cfd(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a cfd without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_cfd(self, config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a cfd without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param stream_reader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_equity(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an equity with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_equity(self, config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an equity with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param stream_reader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_forex(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a forex without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_forex(self, config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a forex without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param stream_reader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_future(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a future with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_future(self, config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a future with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param stream_reader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_option(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an option with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def parse_option(self, config: QuantConnect.Data.SubscriptionDataConfig, stream_reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an option with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param stream_reader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        QuoteBar Reader: Fetch the data from the QC storage and feed it line by line into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param stream: The file data stream
        :param date: Date of this reader request
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        QuoteBar Reader: Fetch the data from the QC storage and feed it line by line into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    def to_string(self) -> str:
        """
        Convert this QuoteBar to string form.
        
        :returns: String representation of the QuoteBar.
        """
        ...

    def update(self, last_trade: float, bid_price: float, ask_price: float, volume: float, bid_size: float, ask_size: float) -> None:
        """
        Update the quotebar - build the bar from this pricing information:
        
        :param last_trade: The last trade price
        :param bid_price: Current bid price
        :param ask_price: Current asking price
        :param volume: Volume of this trade
        :param bid_size: The size of the current bid, if available, if not, pass 0
        :param ask_size: The size of the current ask, if available, if not, pass 0
        """
        ...


class QuoteBars(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.QuoteBar]):
    """Collection of QuoteBar keyed by symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.QuoteBar:
        """
        Gets or sets the QuoteBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The QuoteBar with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Gets or sets the QuoteBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The QuoteBar with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the QuoteBars dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the QuoteBars dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Gets or sets the QuoteBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The QuoteBar with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Gets or sets the QuoteBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The QuoteBar with the specified Symbol.
        """
        ...


class FuturesContract(System.Object):
    """Defines a single futures contract at a specific expiration"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the futures contract's symbol"""
        ...

    @property
    def underlying_symbol(self) -> QuantConnect.Symbol:
        """Gets the underlying security's symbol"""
        ...

    @property
    def expiry(self) -> datetime.datetime:
        """Gets the expiration date"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Gets the local date time this contract's data was last updated"""
        ...

    @property.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def open_interest(self) -> float:
        """Gets the open interest"""
        ...

    @property.setter
    def open_interest(self, value: float) -> None:
        ...

    @property
    def last_price(self) -> float:
        """Gets the last price this contract traded at"""
        ...

    @property.setter
    def last_price(self, value: float) -> None:
        ...

    @property
    def volume(self) -> int:
        """Gets the last volume this contract traded at"""
        ...

    @property.setter
    def volume(self, value: int) -> None:
        ...

    @property
    def bid_price(self) -> float:
        """Gets the current bid price"""
        ...

    @property.setter
    def bid_price(self, value: float) -> None:
        ...

    @property
    def bid_size(self) -> int:
        """Get the current bid size"""
        ...

    @property.setter
    def bid_size(self, value: int) -> None:
        ...

    @property
    def ask_price(self) -> float:
        """Gets the ask price"""
        ...

    @property.setter
    def ask_price(self, value: float) -> None:
        ...

    @property
    def ask_size(self) -> int:
        """Gets the current ask size"""
        ...

    @property.setter
    def ask_size(self, value: int) -> None:
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], underlyingSymbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Initializes a new instance of the FuturesContract class
        
        :param symbol: The futures contract symbol
        :param underlyingSymbol: The symbol of the underlying security
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class FuturesContracts(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.FuturesContract]):
    """Collection of FuturesContract keyed by futures symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.FuturesContract:
        """
        Gets or sets the FuturesContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesContract with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.FuturesContract:
        """
        Gets or sets the FuturesContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesContract with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the FuturesContracts dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the FuturesContracts dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.FuturesContract) -> None:
        """
        Gets or sets the FuturesContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesContract with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.FuturesContract) -> None:
        """
        Gets or sets the FuturesContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesContract with the specified Symbol.
        """
        ...


class FuturesChain(QuantConnect.Data.BaseData, typing.Iterable[QuantConnect.Data.Market.FuturesContract]):
    """
    Represents an entire chain of futures contracts for a single underlying
    This type is IEnumerable{FuturesContract}
    """

    @property
    def underlying(self) -> QuantConnect.Data.BaseData:
        """
        Gets the most recent trade information for the underlying. This may
        be a Tick or a TradeBar
        """
        ...

    @property
    def ticks(self) -> QuantConnect.Data.Market.Ticks:
        """Gets all ticks for every futures contract in this chain, keyed by symbol"""
        ...

    @property
    def trade_bars(self) -> QuantConnect.Data.Market.TradeBars:
        """Gets all trade bars for every futures contract in this chain, keyed by symbol"""
        ...

    @property
    def quote_bars(self) -> QuantConnect.Data.Market.QuoteBars:
        """Gets all quote bars for every futures contract in this chain, keyed by symbol"""
        ...

    @property
    def contracts(self) -> QuantConnect.Data.Market.FuturesContracts:
        """Gets all contracts in the chain, keyed by symbol"""
        ...

    @property
    def filtered_contracts(self) -> System.Collections.Generic.HashSet[QuantConnect.Symbol]:
        """Gets the set of symbols that passed the Future.ContractFilter"""
        ...

    @overload
    def __init__(self, canonicalFutureSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the FuturesChain class
        
        :param canonicalFutureSymbol: The symbol for this chain.
        :param time: The time of this chain
        """
        ...

    @overload
    def __init__(self, canonicalFutureSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], trades: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], quotes: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], contracts: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.FuturesContract], filteredContracts: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the FuturesChain class
        
        :param canonicalFutureSymbol: The symbol for this chain.
        :param time: The time of this chain
        :param trades: All trade data for the entire futures chain
        :param quotes: All quote data for the entire futures chain
        :param contracts: All contracts for this futures chain
        :param filteredContracts: The filtered list of contracts for this futures chain
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    @overload
    def get_aux(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_FuturesChain_GetAux_T:
        """
        Gets the auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The last auxiliary data with the specified type and symbol.
        """
        ...

    @overload
    def get_aux(self) -> QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Market_FuturesChain_GetAux_T]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def get_aux_list(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, System.Collections.Generic.List[QuantConnect.Data.BaseData]]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def get_aux_list(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect_Data_Market_FuturesChain_GetAuxList_T]:
        """
        Gets a list of auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The list of auxiliary data with the specified type and symbol.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Market.FuturesContract]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...


class FuturesChains(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.FuturesChain]):
    """Collection of FuturesChain keyed by canonical futures symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.FuturesChain:
        """
        Gets or sets the FuturesChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesChain with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.FuturesChain:
        """
        Gets or sets the FuturesChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesChain with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the FuturesChains dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the FuturesChains dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.FuturesChain) -> None:
        """
        Gets or sets the FuturesChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesChain with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.FuturesChain) -> None:
        """
        Gets or sets the FuturesChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesChain with the specified Symbol.
        """
        ...


class Greeks(System.Object, metaclass=abc.ABCMeta):
    """Defines the greeks"""

    @property
    @abc.abstractmethod
    def delta(self) -> float:
        """
        Gets the delta.
        
        Delta measures the rate of change of the option value with respect to changes in
        the underlying asset'sprice. (∂V/∂S)
        """
        ...

    @property
    @abc.abstractmethod
    def gamma(self) -> float:
        """
        Gets the gamma.
        
        Gamma measures the rate of change of Delta with respect to changes in
        the underlying asset'sprice. (∂²V/∂S²)
        """
        ...

    @property
    @abc.abstractmethod
    def vega(self) -> float:
        """
        Gets the vega.
        
        Vega measures the rate of change of the option value with respect to changes in
        the underlying's volatility. (∂V/∂σ)
        """
        ...

    @property
    @abc.abstractmethod
    def theta(self) -> float:
        """
        Gets the theta.
        
        Theta measures the rate of change of the option value with respect to changes in
        time. This is commonly known as the 'time decay.' (∂V/∂τ)
        """
        ...

    @property
    @abc.abstractmethod
    def rho(self) -> float:
        """
        Gets the rho.
        
        Rho measures the rate of change of the option value with respect to changes in
        the risk free interest rate. (∂V/∂r)
        """
        ...

    @property
    @abc.abstractmethod
    def Lambda(self) -> float:
        """
        Gets the lambda.
        
        Lambda is the percentage change in option value per percentage change in the
        underlying's price, a measure of leverage. Sometimes referred to as gearing.
        (∂V/∂S ✕ S/V)
        """
        ...

    @property
    def lambda_(self) -> float:
        """
        Gets the lambda.
        
        Lambda is the percentage change in option value per percentage change in the
        underlying's price, a measure of leverage. Sometimes referred to as gearing.
        (∂V/∂S ✕ S/V)
        """
        ...

    @property
    def theta_per_day(self) -> float:
        """
        Gets the theta per day.
        
        Theta measures the rate of change of the option value with respect to changes in
        time. This is commonly known as the 'time decay.' (∂V/∂τ)
        """
        ...


class OptionContract(System.Object, QuantConnect.Data.ISymbolProvider, QuantConnect.Securities.ISymbol):
    """Defines a single option contract at a specific expiration and strike price"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the option contract's symbol"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def id(self) -> QuantConnect.SecurityIdentifier:
        """The security identifier of the option symbol"""
        ...

    @property
    def underlying_symbol(self) -> QuantConnect.Symbol:
        """Gets the underlying security's symbol"""
        ...

    @property
    def strike(self) -> float:
        """Gets the strike price"""
        ...

    @property
    def scaled_strike(self) -> float:
        """Gets the strike price multiplied by the strike multiplier"""
        ...

    @property
    def expiry(self) -> datetime.datetime:
        """Gets the expiration date"""
        ...

    @property
    def right(self) -> QuantConnect.OptionRight:
        """Gets the right being purchased (call [right to buy] or put [right to sell])"""
        ...

    @property
    def style(self) -> QuantConnect.OptionStyle:
        """Gets the option style"""
        ...

    @property
    def theoretical_price(self) -> float:
        """Gets the theoretical price of this option contract as computed by the IOptionPriceModel"""
        ...

    @property
    def implied_volatility(self) -> float:
        """Gets the implied volatility of the option contract as computed by the IOptionPriceModel"""
        ...

    @property
    def greeks(self) -> QuantConnect.Data.Market.Greeks:
        """Gets the greeks for this contract"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Gets the local date time this contract's data was last updated"""
        ...

    @property.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def open_interest(self) -> float:
        """Gets the open interest"""
        ...

    @property
    def last_price(self) -> float:
        """Gets the last price this contract traded at"""
        ...

    @property
    def volume(self) -> int:
        """Gets the last volume this contract traded at"""
        ...

    @property
    def bid_price(self) -> float:
        """Gets the current bid price"""
        ...

    @property
    def bid_size(self) -> int:
        """Get the current bid size"""
        ...

    @property
    def ask_price(self) -> float:
        """Gets the ask price"""
        ...

    @property
    def ask_size(self) -> int:
        """Gets the current ask size"""
        ...

    @property
    def underlying_last_price(self) -> float:
        """Gets the last price the underlying security traded at"""
        ...

    @overload
    def __init__(self, security: QuantConnect.Interfaces.ISecurityPrice) -> None:
        """
        Initializes a new instance of the OptionContract class
        
        :param security: The option contract security
        """
        ...

    @overload
    def __init__(self, contractData: QuantConnect.Data.UniverseSelection.OptionUniverse, symbolProperties: QuantConnect.Securities.SymbolProperties) -> None:
        """
        Initializes a new option contract from a given OptionUniverse instance
        
        :param contractData: The option universe contract data to use as source for this contract
        :param symbolProperties: The contract symbol properties
        """
        ...

    @staticmethod
    @overload
    def create(base_data: QuantConnect.Data.BaseData, security: QuantConnect.Interfaces.ISecurityPrice, underlying: QuantConnect.Data.BaseData) -> QuantConnect.Data.Market.OptionContract:
        """
        Creates a OptionContract
        
        :param security: Provides price properties for a Security
        :param underlying: Last underlying security trade data
        :returns: Option contract.
        """
        ...

    @staticmethod
    @overload
    def create(end_time: typing.Union[datetime.datetime, datetime.date], security: QuantConnect.Interfaces.ISecurityPrice, underlying: QuantConnect.Data.BaseData) -> QuantConnect.Data.Market.OptionContract:
        """
        Creates a OptionContract
        
        :param end_time: local date time this contract's data was last updated
        :param security: provides price properties for a Security
        :param underlying: last underlying security trade data
        :returns: Option contract.
        """
        ...

    @staticmethod
    @overload
    def create(contract_data: QuantConnect.Data.UniverseSelection.OptionUniverse, symbol_properties: QuantConnect.Securities.SymbolProperties) -> QuantConnect.Data.Market.OptionContract:
        """
        Creates a new option contract from a given OptionUniverse instance,
        using its data to form a quote bar to source pricing data
        
        :param contract_data: The option universe contract data to use as source for this contract
        :param symbol_properties: The contract symbol properties
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class OptionContracts(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.OptionContract]):
    """Collection of OptionContract keyed by option symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.OptionContract:
        """
        Gets or sets the OptionContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionContract with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.OptionContract:
        """
        Gets or sets the OptionContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionContract with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the OptionContracts dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the OptionContracts dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.OptionContract) -> None:
        """
        Gets or sets the OptionContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionContract with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.OptionContract) -> None:
        """
        Gets or sets the OptionContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionContract with the specified Symbol.
        """
        ...


class OptionChain(QuantConnect.Data.BaseData, typing.Iterable[QuantConnect.Data.Market.OptionContract]):
    """
    Represents an entire chain of option contracts for a single underying security.
    This type is IEnumerable{OptionContract}
    """

    @property
    def underlying(self) -> QuantConnect.Data.BaseData:
        """
        Gets the most recent trade information for the underlying. This may
        be a Tick or a TradeBar
        """
        ...

    @property
    def ticks(self) -> QuantConnect.Data.Market.Ticks:
        """Gets all ticks for every option contract in this chain, keyed by option symbol"""
        ...

    @property
    def trade_bars(self) -> QuantConnect.Data.Market.TradeBars:
        """Gets all trade bars for every option contract in this chain, keyed by option symbol"""
        ...

    @property
    def quote_bars(self) -> QuantConnect.Data.Market.QuoteBars:
        """Gets all quote bars for every option contract in this chain, keyed by option symbol"""
        ...

    @property
    def contracts(self) -> QuantConnect.Data.Market.OptionContracts:
        """Gets all contracts in the chain, keyed by option symbol"""
        ...

    @property
    def filtered_contracts(self) -> System.Collections.Generic.HashSet[QuantConnect.Symbol]:
        """Gets the set of symbols that passed the Option.ContractFilter"""
        ...

    @property
    def data_frame(self) -> typing.Any:
        """The data frame representation of the option chain"""
        ...

    @overload
    def __init__(self, canonicalOptionSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], flatten: bool = True) -> None:
        """
        Initializes a new instance of the OptionChain class
        
        :param canonicalOptionSymbol: The symbol for this chain.
        :param time: The time of this chain
        :param flatten: Whether to flatten the data frame
        """
        ...

    @overload
    def __init__(self, canonicalOptionSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], underlying: QuantConnect.Data.BaseData, trades: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], quotes: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], contracts: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.OptionContract], filteredContracts: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], flatten: bool = True) -> None:
        """
        Initializes a new instance of the OptionChain class
        
        :param canonicalOptionSymbol: The symbol for this chain.
        :param time: The time of this chain
        :param underlying: The most recent underlying trade data
        :param trades: All trade data for the entire option chain
        :param quotes: All quote data for the entire option chain
        :param contracts: All contracts for this option chain
        :param filteredContracts: The filtered list of contracts for this option chain
        :param flatten: Whether to flatten the data frame
        """
        ...

    @overload
    def __init__(self, canonicalOptionSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], contracts: System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.OptionUniverse], symbolProperties: QuantConnect.Securities.SymbolProperties, flatten: bool = True) -> None:
        """
        Initializes a new option chain for a list of contracts as OptionUniverse instances
        
        :param canonicalOptionSymbol: The canonical option symbol
        :param time: The time of this chain
        :param contracts: The list of contracts data
        :param symbolProperties: The option symbol properties
        :param flatten: Whether to flatten the data frame
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    @overload
    def get_aux(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_OptionChain_GetAux_T:
        """
        Gets the auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The last auxiliary data with the specified type and symbol.
        """
        ...

    @overload
    def get_aux(self) -> QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Market_OptionChain_GetAux_T]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def get_aux_list(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, System.Collections.Generic.List[QuantConnect.Data.BaseData]]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def get_aux_list(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect_Data_Market_OptionChain_GetAuxList_T]:
        """
        Gets a list of auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The list of auxiliary data with the specified type and symbol.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Market.OptionContract]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...


class OptionChains(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.OptionChain]):
    """Collection of OptionChain keyed by canonical option symbol"""

    @property
    def data_frame(self) -> typing.Any:
        """The data frame representation of the option chains"""
        ...

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.OptionChain:
        """
        Gets or sets the OptionChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionChain with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.OptionChain:
        """
        Gets or sets the OptionChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionChain with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the OptionChains dictionary"""
        ...

    @overload
    def __init__(self, flatten: bool) -> None:
        """Creates a new instance of the OptionChains dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], flatten: bool = True) -> None:
        """Creates a new instance of the OptionChains dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.OptionChain) -> None:
        """
        Gets or sets the OptionChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionChain with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.OptionChain) -> None:
        """
        Gets or sets the OptionChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionChain with the specified Symbol.
        """
        ...


class Delistings(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.Delisting]):
    """Collections of Delisting keyed by Symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.Delisting:
        """
        Gets or sets the Delisting with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Delisting with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.Delisting:
        """
        Gets or sets the Delisting with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Delisting with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Delistings dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Delistings dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.Delisting) -> None:
        """
        Gets or sets the Delisting with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Delisting with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.Delisting) -> None:
        """
        Gets or sets the Delisting with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Delisting with the specified Symbol.
        """
        ...


class Dividend(QuantConnect.Data.BaseData):
    """Dividend event from a security"""

    @property
    def distribution(self) -> float:
        """Gets the dividend payment"""
        ...

    @property.setter
    def distribution(self, value: float) -> None:
        ...

    @property
    def reference_price(self) -> float:
        """
        Gets the price at which the dividend occurred.
        This is typically the previous day's closing price
        """
        ...

    @property.setter
    def reference_price(self, value: float) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Dividend class"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], distribution: float, referencePrice: float) -> None:
        """
        Initializes a new instance of the Dividend class
        
        :param symbol: The symbol
        :param date: The date
        :param distribution: The dividend amount
        :param referencePrice: The previous day's closing price
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    @staticmethod
    def compute_distribution(close: float, price_factor_ratio: float, decimal_places: int) -> float:
        """
        Computes the price factor ratio given the previous day's closing price and the p
        
        :param close: Previous day's closing price
        :param price_factor_ratio: Price factor ratio pf_i/pf_i+1
        :param decimal_places: The number of decimal places to round the result to, defaulting to 2
        :returns: The distribution rounded to the specified number of decimal places, defaulting to 2.
        """
        ...

    @staticmethod
    def create(symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], reference_price: float, price_factor_ratio: float, decimal_places: int = 2) -> QuantConnect.Data.Market.Dividend:
        """
        Initializes a new instance of the Dividend class
        
        :param symbol: The symbol
        :param date: The date
        :param reference_price: The previous day's closing price
        :param price_factor_ratio: The ratio of the price factors, pf_i/pf_i+1
        :param decimal_places: The number of decimal places to round the dividend's distribution to, defaulting to 2
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def to_string(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...


class BaseRenkoBar(QuantConnect.Data.Market.TradeBar, QuantConnect.Data.Market.IBaseDataBar, metaclass=abc.ABCMeta):
    """
    Represents a bar sectioned not by time, but by some amount of movement in a set field,
    where:
    - Open : Gets the opening value that started this bar
    - Close : Gets the closing value or the current value if the bar has not yet closed.
    - High : Gets the highest value encountered during this bar
    - Low : Gets the lowest value encountered during this bar
    """

    @property
    def type(self) -> QuantConnect.Data.Market.RenkoType:
        """Gets the kind of the bar"""
        ...

    @property
    def brick_size(self) -> float:
        """The preset size of the consolidated bar"""
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Gets the end time of this renko bar or the most recent update time if it IsClosed"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def start(self) -> datetime.datetime:
        """Gets the time this bar started"""
        ...

    @property
    def is_closed(self) -> bool:
        """Gets whether or not this bar is considered closed."""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader Method :: using set of arguements we specify read out type. Enumerate
        until the end of the data stream or file. E.g. Read CSV file line by line and convert
        into data types.
        
        :param config: Config.
        :param line: Line.
        :param date: Date.
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: BaseData type set by Subscription Method.
        """
        ...


class BarDirection(Enum):
    """Enum for Bar Direction"""

    RISING = 0
    """Rising bar (0)"""

    NO_DELTA = 1
    """No change (1)"""

    FALLING = 2
    """Falling bar (2)"""


class RenkoBar(QuantConnect.Data.Market.BaseRenkoBar):
    """Represents a bar sectioned not by time, but by some amount of movement in a value (for example, Closing price moving in $10 bar sizes)"""

    @property
    def end(self) -> datetime.datetime:
        """
        Gets the end time of this renko bar or the most recent update time if it BaseRenkoBar.IsClosed
        
        RenkoBar.End is obsolete. Please use RenkoBar.EndTime property instead.
        """
        warnings.warn("RenkoBar.End is obsolete. Please use RenkoBar.EndTime property instead.", DeprecationWarning)

    @property.setter
    def end(self, value: datetime.datetime) -> None:
        warnings.warn("RenkoBar.End is obsolete. Please use RenkoBar.EndTime property instead.", DeprecationWarning)

    @property
    def direction(self) -> QuantConnect.Data.Market.BarDirection:
        """The trend of the bar (i.e. Rising, Falling or NoDelta)"""
        ...

    @property
    def spread(self) -> float:
        """The "spread" of the bar"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the RenkoBar class."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], brickSize: float, open: float, volume: float) -> None:
        """
        Initializes a new instance of the RenkoBar class with the specified values
        
        :param symbol: The symbol of this data
        :param time: The start time of the bar
        :param brickSize: The size of each renko brick
        :param open: The opening price for the new bar
        :param volume: Any initial volume associated with the data
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], endTime: typing.Union[datetime.datetime, datetime.date], brickSize: float, open: float, high: float, low: float, close: float) -> None:
        """
        Initializes a new instance of the RenkoBar class with the specified values
        
        :param symbol: The symbol of this data
        :param start: The start time of the bar
        :param endTime: The end time of the bar
        :param brickSize: The size of each wicko brick
        :param open: The opening price for the new bar
        :param high: The high price for the new bar
        :param low: The low price for the new bar
        :param close: The closing price for the new bar
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def update(self, time: typing.Union[datetime.datetime, datetime.date], current_value: float, volume_since_last_update: float) -> bool:
        """
        Updates this RenkoBar with the specified values and returns whether or not this bar is closed
        
        :param time: The current time
        :param current_value: The current value
        :param volume_since_last_update: The volume since the last update called on this instance
        :returns: True if this bar BaseRenkoBar.IsClosed.
        """
        ...


class Split(QuantConnect.Data.BaseData):
    """Split event from a security"""

    @property
    def type(self) -> QuantConnect.SplitType:
        """Gets the type of split event, warning or split."""
        ...

    @property
    def split_factor(self) -> float:
        """Gets the split factor"""
        ...

    @property.setter
    def split_factor(self, value: float) -> None:
        ...

    @property
    def reference_price(self) -> float:
        """
        Gets the price at which the split occurred
        This is typically the previous day's closing price
        """
        ...

    @property.setter
    def reference_price(self, value: float) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Split class"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], price: float, splitFactor: float, type: QuantConnect.SplitType) -> None:
        """
        Initializes a new instance of the Split class
        
        :param symbol: The symbol
        :param date: The date
        :param price: The price at the time of the split
        :param splitFactor: The split factor to be applied to current holdings
        :param type: The type of split event, warning or split occurred
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def to_string(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...


class VolumeRenkoBar(QuantConnect.Data.Market.BaseRenkoBar):
    """Represents a bar sectioned not by time, but by some amount of movement in volume"""

    @property
    def is_closed(self) -> bool:
        """Gets whether or not this bar is considered closed."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the RenkoBar class."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], endTime: typing.Union[datetime.datetime, datetime.date], brickSize: float, open: float, high: float, low: float, close: float, volume: float) -> None:
        """
        Initializes a new instance of the VolumeRenkoBar class with the specified values
        
        :param symbol: symbol of the data
        :param start: The current data start time
        :param endTime: The current data end time
        :param brickSize: The preset volume capacity of this bar
        :param open: The current data open value
        :param high: The current data high value
        :param low: The current data low value
        :param close: The current data close value
        :param volume: The current data volume
        """
        ...

    def rollover(self) -> QuantConnect.Data.Market.VolumeRenkoBar:
        """Create a new VolumeRenkoBar with previous information rollover"""
        ...

    def update(self, time: typing.Union[datetime.datetime, datetime.date], high: float, low: float, close: float, volume: float) -> float:
        """
        Updates this VolumeRenkoBar with the specified values and returns whether or not this bar is closed
        
        :param time: The current data end time
        :param high: The current data high value
        :param low: The current data low value
        :param close: The current data close value
        :param volume: The current data volume
        :returns: The excess volume that the current bar cannot absorb.
        """
        ...


class Dividends(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.Dividend]):
    """Collection of dividends keyed by Symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.Dividend:
        """
        Gets or sets the Dividend with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Dividend with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.Dividend:
        """
        Gets or sets the Dividend with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Dividend with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Dividends dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Dividends dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.Dividend) -> None:
        """
        Gets or sets the Dividend with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Dividend with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.Dividend) -> None:
        """
        Gets or sets the Dividend with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Dividend with the specified Symbol.
        """
        ...


class Splits(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.Split]):
    """Collection of splits keyed by Symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.Split:
        """
        Gets or sets the Split with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Split with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.Split:
        """
        Gets or sets the Split with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Split with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Splits dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Splits dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.Split) -> None:
        """
        Gets or sets the Split with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Split with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.Split) -> None:
        """
        Gets or sets the Split with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Split with the specified Symbol.
        """
        ...


