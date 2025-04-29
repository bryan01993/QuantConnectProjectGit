from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Indicators
import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Python
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections.Concurrent
import System.Collections.Generic
import System.IO
import System.Reflection
import System.Threading.Tasks

IDynamicMetaObjectProvider = typing.Any
QuantConnect_Data_SubscriptionDataConfig = typing.Any
PyObject = typing.Any
QuantConnect_Data_SubscriptionDataSource = typing.Any
DynamicMetaObject = typing.Any

QuantConnect_Data_DataHistory_T = typing.TypeVar("QuantConnect_Data_DataHistory_T")
QuantConnect_Data_Slice_Get_T = typing.TypeVar("QuantConnect_Data_Slice_Get_T")
QuantConnect_Data_SliceExtensions_Get_T = typing.TypeVar("QuantConnect_Data_SliceExtensions_Get_T")
QuantConnect_Data_SliceExtensions_TryGet_T = typing.TypeVar("QuantConnect_Data_SliceExtensions_TryGet_T")
QuantConnect_Data__EventContainer_Callable = typing.TypeVar("QuantConnect_Data__EventContainer_Callable")
QuantConnect_Data__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Data__EventContainer_ReturnType")


class SubscriptionDataConfig(System.Object, System.IEquatable[QuantConnect_Data_SubscriptionDataConfig]):
    """Subscription data required including the type of data."""

    class NewSymbolEventArgs(System.EventArgs):
        """New base class for all event classes."""

        @property
        def old(self) -> QuantConnect.Symbol:
            """The old symbol instance"""
            ...

        @property
        def new(self) -> QuantConnect.Symbol:
            """The new symbol instance"""
            ...

        def __init__(self, new: typing.Union[QuantConnect.Symbol, str], old: typing.Union[QuantConnect.Symbol, str]) -> None:
            """Create an instance of NewSymbolEventArgs"""
            ...

    @property
    def new_symbol(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.SubscriptionDataConfig.NewSymbolEventArgs], None], None]:
        """Event fired when there is a new symbol due to mapping"""
        ...

    @property
    def type(self) -> typing.Type:
        """Type of data"""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Security type of this data subscription"""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol of the asset we're requesting: this is really a perm tick!!"""
        ...

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """Trade, quote or open interest data"""
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """Resolution of the asset we're requesting, second minute or tick"""
        ...

    @property
    def increment(self) -> datetime.timedelta:
        """Timespan increment between triggers of this data:"""
        ...

    @property
    def fill_data_forward(self) -> bool:
        """True if wish to send old data when time gaps in data feed."""
        ...

    @property
    def extended_market_hours(self) -> bool:
        """Boolean Send Data from between 4am - 8am (Equities Setting Only)"""
        ...

    @property
    def is_internal_feed(self) -> bool:
        """True if this subscription was added for the sole purpose of providing currency conversion rates via CashBook.EnsureCurrencyDataFeeds"""
        ...

    @property
    def is_custom_data(self) -> bool:
        """True if this subscription is for custom user data, false for QC data"""
        ...

    @property
    def sum_of_dividends(self) -> float:
        """The sum of dividends accrued in this subscription, used for scaling total return prices"""
        ...

    @property.setter
    def sum_of_dividends(self, value: float) -> None:
        ...

    @property
    def data_normalization_mode(self) -> QuantConnect.DataNormalizationMode:
        """Gets the normalization mode used for this subscription"""
        ...

    @property.setter
    def data_normalization_mode(self, value: QuantConnect.DataNormalizationMode) -> None:
        ...

    @property
    def data_mapping_mode(self) -> QuantConnect.DataMappingMode:
        """Gets the securities mapping mode used for this subscription"""
        ...

    @property
    def contract_depth_offset(self) -> int:
        """
        The continuous contract desired offset from the current front month.
        For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @property
    def price_scale_factor(self) -> float:
        """Price Scaling Factor:"""
        ...

    @property.setter
    def price_scale_factor(self, value: float) -> None:
        ...

    @property
    def mapped_symbol(self) -> str:
        """Symbol Mapping: When symbols change over time (e.g. CHASE-> JPM) need to update the symbol requested."""
        ...

    @property.setter
    def mapped_symbol(self, value: str) -> None:
        ...

    @property
    def market(self) -> str:
        """Gets the market / scope of the symbol"""
        ...

    @property
    def data_time_zone(self) -> typing.Any:
        """Gets the data time zone for this subscription"""
        ...

    @property
    def exchange_time_zone(self) -> typing.Any:
        """Gets the exchange time zone for this subscription"""
        ...

    @property
    def consolidators(self) -> System.Collections.Generic.ISet[QuantConnect.Data.Consolidators.IDataConsolidator]:
        """Consolidators that are registred with this subscription"""
        ...

    @property
    def is_filtered_subscription(self) -> bool:
        """Gets whether or not this subscription should have filters applied to it (market hours/user filters from security)"""
        ...

    @overload
    def __init__(self, objectType: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, dataTimeZone: typing.Any, exchangeTimeZone: typing.Any, fillForward: bool, extendedHours: bool, isInternalFeed: bool, isCustom: bool = False, tickType: typing.Optional[QuantConnect.TickType] = None, isFilteredSubscription: bool = True, dataNormalizationMode: QuantConnect.DataNormalizationMode = ..., dataMappingMode: QuantConnect.DataMappingMode = ..., contractDepthOffset: int = 0, mappedConfig: bool = False) -> None:
        """
        Constructor for Data Subscriptions
        
        :param objectType: Type of the data objects.
        :param symbol: Symbol of the asset we're requesting
        :param resolution: Resolution of the asset we're requesting
        :param dataTimeZone: The time zone the raw data is time stamped in
        :param exchangeTimeZone: Specifies the time zone of the exchange for the security this subscription is for. This is this output time zone, that is, the time zone that will be used on BaseData instances
        :param fillForward: Fill in gaps with historical data
        :param extendedHours: Equities only - send in data from 4am - 8pm
        :param isInternalFeed: Set to true if this subscription is added for the sole purpose of providing currency conversion rates, setting this flag to true will prevent the data from being sent into the algorithm's OnData methods
        :param isCustom: True if this is user supplied custom data, false for normal QC data
        :param tickType: Specifies if trade or quote data is subscribed
        :param isFilteredSubscription: True if this subscription should have filters applied to it (market hours/user filters from security), false otherwise
        :param dataNormalizationMode: Specifies normalization mode used for this subscription
        :param dataMappingMode: The contract mapping mode to use for the security
        :param contractDepthOffset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, objectType: typing.Type = None, symbol: typing.Union[QuantConnect.Symbol, str] = None, resolution: typing.Optional[QuantConnect.Resolution] = None, dataTimeZone: typing.Any = None, exchangeTimeZone: typing.Any = None, fillForward: typing.Optional[bool] = None, extendedHours: typing.Optional[bool] = None, isInternalFeed: typing.Optional[bool] = None, isCustom: typing.Optional[bool] = None, tickType: typing.Optional[QuantConnect.TickType] = None, isFilteredSubscription: typing.Optional[bool] = None, dataNormalizationMode: typing.Optional[QuantConnect.DataNormalizationMode] = None, dataMappingMode: typing.Optional[QuantConnect.DataMappingMode] = None, contractDepthOffset: typing.Optional[int] = None, mappedConfig: typing.Optional[bool] = None) -> None:
        """
        Copy constructor with overrides
        
        :param config: The config to copy, then overrides are applied and all option
        :param objectType: Type of the data objects.
        :param symbol: Symbol of the asset we're requesting
        :param resolution: Resolution of the asset we're requesting
        :param dataTimeZone: The time zone the raw data is time stamped in
        :param exchangeTimeZone: Specifies the time zone of the exchange for the security this subscription is for. This is this output time zone, that is, the time zone that will be used on BaseData instances
        :param fillForward: Fill in gaps with historical data
        :param extendedHours: Equities only - send in data from 4am - 8pm
        :param isInternalFeed: Set to true if this subscription is added for the sole purpose of providing currency conversion rates, setting this flag to true will prevent the data from being sent into the algorithm's OnData methods
        :param isCustom: True if this is user supplied custom data, false for normal QC data
        :param tickType: Specifies if trade or quote data is subscribed
        :param isFilteredSubscription: True if this subscription should have filters applied to it (market hours/user filters from security), false otherwise
        :param dataNormalizationMode: Specifies normalization mode used for this subscription
        :param dataMappingMode: The contract mapping mode to use for the security
        :param contractDepthOffset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        :param mappedConfig: True if this is created as a mapped config. This is useful for continuous contract at live trading where we subscribe to the mapped symbol but want to preserve uniqueness
        """
        ...

    @overload
    def equals(self, other: QuantConnect.Data.SubscriptionDataConfig) -> bool:
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

    @overload
    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    @overload
    def to_string(self, symbol: str) -> str:
        """
        Returns a string that represents the current object.
        
        :param symbol: Symbol to use in the string representation of the object
        :returns: /// A string that represents the current object.
        """
        ...


class SubscriptionDataConfigList(System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]):
    """Provides convenient methods for holding several SubscriptionDataConfig"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol for which this class holds SubscriptionDataConfig"""
        ...

    @property
    def is_internal_feed(self) -> bool:
        """Assume that the InternalDataFeed is the same for both SubscriptionDataConfig"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """Default constructor that specifies the Symbol that the SubscriptionDataConfig represent"""
        ...

    def set_data_normalization_mode(self, normalization_mode: QuantConnect.DataNormalizationMode) -> None:
        """Sets the DataNormalizationMode for all SubscriptionDataConfig contained in the list"""
        ...


class FileFormat(Enum):
    """Specifies the format of data in a subscription"""

    CSV = 0
    """Comma separated values (0)"""

    BINARY = 1
    """Binary file data (1)"""

    ZIP_ENTRY_NAME = 2
    """Only the zip entry names are read in as symbols (2)"""

    UNFOLDING_COLLECTION = 3
    """Reader returns a BaseDataCollection object (3)"""

    INDEX = 4
    """Data stored using an intermediate index source (4)"""

    FOLDING_COLLECTION = 5
    """
    Data type inherits from BaseDataCollection.
    Reader method can return a non BaseDataCollection type which will be folded, based on unique time,
    into an instance of the data type (5)
    """


class SubscriptionDataSource(System.Object, System.IEquatable[QuantConnect_Data_SubscriptionDataSource]):
    """Represents the source location and transport medium for a subscription"""

    @property
    def sort(self) -> bool:
        """
        Specifies whether the data source should be sorted.
        If False, data will be returned in the original order, else it will be ordered by time.
        """
        ...

    @property.setter
    def sort(self, value: bool) -> None:
        ...

    @property
    def source(self) -> str:
        """Identifies where to get the subscription's data from"""
        ...

    @property
    def format(self) -> QuantConnect.Data.FileFormat:
        """Identifies the format of the data within the source"""
        ...

    @property
    def transport_medium(self) -> QuantConnect.SubscriptionTransportMedium:
        """Identifies the transport medium used to access the data, such as a local or remote file, or a polling rest API"""
        ...

    @property
    def headers(self) -> System.Collections.Generic.IReadOnlyList[System.Collections.Generic.KeyValuePair[str, str]]:
        """Gets the header values to be used in the web request."""
        ...

    @overload
    def __init__(self, source: str) -> None:
        """
        Initializes a new instance of the SubscriptionDataSource class.
        
        :param source: The subscription's data source location
        """
        ...

    @overload
    def __init__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium) -> None:
        """
        Initializes a new instance of the SubscriptionDataSource class.
        
        :param source: The subscription's data source location
        :param transportMedium: The transport medium to be used to retrieve the subscription's data from the source
        """
        ...

    @overload
    def __init__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium, format: QuantConnect.Data.FileFormat) -> None:
        """
        Initializes a new instance of the SubscriptionDataSource class.
        
        :param source: The subscription's data source location
        :param transportMedium: The transport medium to be used to retrieve the subscription's data from the source
        :param format: The format of the data within the source
        """
        ...

    @overload
    def __init__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium, format: QuantConnect.Data.FileFormat, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]]) -> None:
        """
        Initializes a new instance of the SubscriptionDataSource class with SubscriptionTransportMedium.Rest
        including the specified header values
        
        :param source: The subscription's data source location
        :param transportMedium: The transport medium to be used to retrieve the subscription's data from the source
        :param format: The format of the data within the source
        :param headers: The headers to be used for this source
        """
        ...

    @overload
    def equals(self, other: QuantConnect.Data.SubscriptionDataSource) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified instance is equal to the current instance.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as a hash function for a particular type.
        
        :returns: A hash code for the current System.Object.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class BaseData(System.Object, QuantConnect.Data.IBaseData, metaclass=abc.ABCMeta):
    """
    Abstract base data class of QuantConnect. It is intended to be extended to define
    generic user customizable data types while at the same time implementing the basics of data where possible
    """

    ALL_RESOLUTIONS: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of all Resolution
    
    This field is protected.
    """

    DAILY_RESOLUTION: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of Resolution.Daily
    
    This field is protected.
    """

    MINUTE_RESOLUTION: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of Resolution.Minute
    
    This field is protected.
    """

    HIGH_RESOLUTION: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of high Resolution, including minute, second, and tick.
    
    This field is protected.
    """

    OPTION_RESOLUTIONS: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of resolutions support by Options
    
    This field is protected.
    """

    @property
    def data_type(self) -> QuantConnect.MarketDataType:
        """Market Data Type of this data - does it come in individual price packets or is it grouped into OHLC."""
        ...

    @property.setter
    def data_type(self, value: QuantConnect.MarketDataType) -> None:
        ...

    @property
    def is_fill_forward(self) -> bool:
        """True if this is a fill forward piece of data"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Current time marker of this data packet."""
        ...

    @property.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """
        The end time of this data. Some data covers spans (trade bars) and as such we want
        to know the entire time span covered
        """
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol representation for underlying Security"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def value(self) -> float:
        """
        Value representation of this data packet. All data requires a representative value for this moment in time.
        For streams of data this is the price now, for OHLC packets this is the closing price.
        """
        ...

    @property.setter
    def value(self, value: float) -> None:
        ...

    @property
    def price(self) -> float:
        """As this is a backtesting platform we'll provide an alias of value as price."""
        ...

    def __init__(self) -> None:
        """Constructor for initialising the dase data class"""
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
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    @staticmethod
    def deserialize_message(serialized: str) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Deserialize the message from the data server
        
        :param serialized: The data server's message
        :returns: An enumerable of base data, if unsuccessful, returns an empty enumerable.
        """
        ...

    @overload
    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    @overload
    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], datafeed: QuantConnect.DataFeedEndpoint) -> str:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        GetSource(SubscriptionDataConfig, DateTime, DataFeedEndpoint) method has been made obsolete, use GetSource(SubscriptionDataConfig, DateTime, bool) instead.
        
        :param config: Configuration object
        :param date: Date of this source file
        :param datafeed: Type of datafeed we're reqesting - backtest or live
        :returns: String URL of source file.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
        """
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    @overload
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

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], data_feed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        Reader(SubscriptionDataConfig, string, DateTime, DataFeedEndpoint) method has been made obsolete, use Reader(SubscriptionDataConfig, string, DateTime, bool) instead.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param data_feed: Type of datafeed we're requesting - a live or backtest feed.
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def should_cache_to_security(self) -> bool:
        """
        Indicates whether this contains data that should be stored in the security cache
        
        :returns: Whether this contains data that should be stored in the security cache.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...

    def update(self, last_trade: float, bid_price: float, ask_price: float, volume: float, bid_size: float, ask_size: float) -> None:
        """
        Update routine to build a bar/tick from a data update.
        
        :param last_trade: The last trade price
        :param bid_price: Current bid price
        :param ask_price: Current asking price
        :param volume: Volume of this trade
        :param bid_size: The size of the current bid, if available
        :param ask_size: The size of the current ask, if available
        """
        ...

    def update_ask(self, ask_price: float, ask_size: float) -> None:
        """
        Updates this base data with the new quote ask information
        
        :param ask_price: The current ask price
        :param ask_size: The current ask size
        """
        ...

    def update_bid(self, bid_price: float, bid_size: float) -> None:
        """
        Updates this base data with the new quote bid information
        
        :param bid_price: The current bid price
        :param bid_size: The current bid size
        """
        ...

    def update_quote(self, bid_price: float, bid_size: float, ask_price: float, ask_size: float) -> None:
        """
        Updates this base data with new quote information
        
        :param bid_price: The current bid price
        :param bid_size: The current bid size
        :param ask_price: The current ask price
        :param ask_size: The current ask size
        """
        ...

    def update_trade(self, last_trade: float, trade_size: float) -> None:
        """
        Updates this base data with a new trade
        
        :param last_trade: The price of the last trade
        :param trade_size: The quantity traded
        """
        ...


class DynamicData(QuantConnect.Data.BaseData, IDynamicMetaObjectProvider, metaclass=abc.ABCMeta):
    """Dynamic Data Class: Accept flexible data, adapting to the columns provided by source."""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def get_meta_object(self, parameter: typing.Any) -> typing.Any:
        """Get the metaObject required for Dynamism."""
        ...

    def get_property(self, name: str) -> System.Object:
        """
        Gets the property's value with the specified name. This is a case-insensitve search.
        
        :param name: The property name to access
        :returns: object value of BaseData.
        """
        ...

    def get_storage_dictionary(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        """
        Gets the storage dictionary
        Python algorithms need this information since DynamicMetaObject does not work
        
        :returns: Dictionary that stores the paramenters names and values.
        """
        ...

    def has_property(self, name: str) -> bool:
        """
        Gets whether or not this dynamic data instance has a property with the specified name.
        This is a case-insensitve search.
        
        :param name: The property name to check for
        :returns: True if the property exists, false otherwise.
        """
        ...

    def set_property(self, name: str, value: typing.Any) -> System.Object:
        """
        Sets the property with the specified name to the value. This is a case-insensitve search.
        
        :param name: The property name to set
        :param value: The new property value
        :returns: Returns the input value back to the caller.
        """
        ...


class DiskDataCacheProvider(System.Object, QuantConnect.Interfaces.IDataCacheProvider):
    """
    Simple data cache provider, writes and reads directly from disk
    Used as default for LeanDataWriter
    """

    @property
    def is_data_ephemeral(self) -> bool:
        """Property indicating the data is temporary in nature and should not be cached."""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    @overload
    def __init__(self, locker: QuantConnect.Util.KeyStringSynchronizer) -> None:
        """
        Creates a new instance using the given synchronizer
        
        :param locker: The synchronizer instance to use
        """
        ...

    def dispose(self) -> None:
        """Dispose for this class"""
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Fetch data from the cache
        
        :param key: A string representing the key of the cached data
        :returns: An Stream of the cached data.
        """
        ...

    def get_zip_entries(self, zip_file: str) -> System.Collections.Generic.List[str]:
        """Returns a list of zip entries in a provided zip file"""
        ...

    def store(self, key: str, data: typing.List[int]) -> None:
        """
        Store the data in the cache. Not implemented in this instance of the IDataCacheProvider
        
        :param key: The source of the data, used as a key to retrieve data in the cache
        :param data: The data as a byte array
        """
        ...


class DataMonitor(System.Object, QuantConnect.Interfaces.IDataMonitor):
    """Monitors data requests and reports on missing data"""

    def __init__(self) -> None:
        """Initializes a new instance of the DataMonitor class"""
        ...

    def dispose(self) -> None:
        """Disposes this object"""
        ...

    def exit(self) -> None:
        """Terminates the data monitor generating a final report"""
        ...

    def on_new_data_request(self, sender: typing.Any, e: QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs) -> None:
        """Event handler for the IDataProvider.NewDataRequest event"""
        ...

    def strip_data_folder(self, path: str) -> str:
        """
        Strips the given data folder path
        
        This method is protected.
        """
        ...


class IndexedBaseData(QuantConnect.Data.BaseData, metaclass=abc.ABCMeta):
    """
    Abstract indexed base data class of QuantConnect.
    It is intended to be extended to define customizable data types which are stored
    using an intermediate index source
    """

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Returns the index source for a date
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: The SubscriptionDataSource instance to use.
        """
        ...

    def get_source_for_an_index(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], index: str, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Returns the source for a given index value
        
        :param config: Configuration object
        :param date: Date of this source file
        :param index: The index value for which we want to fetch the source
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: The SubscriptionDataSource instance to use.
        """
        ...


class BaseDataRequest(System.Object, metaclass=abc.ABCMeta):
    """Abstract sharing logic for data requests"""

    @property
    def start_time_utc(self) -> datetime.datetime:
        """Gets the beginning of the requested time interval in UTC"""
        ...

    @property
    def end_time_utc(self) -> datetime.datetime:
        """Gets the end of the requested time interval in UTC"""
        ...

    @property
    def start_time_local(self) -> datetime.datetime:
        """Gets the StartTimeUtc in the security's exchange time zone"""
        ...

    @property
    def end_time_local(self) -> datetime.datetime:
        """Gets the EndTimeUtc in the security's exchange time zone"""
        ...

    @property
    def exchange_hours(self) -> QuantConnect.Securities.SecurityExchangeHours:
        """Gets the exchange hours used for processing fill forward requests"""
        ...

    @property
    @abc.abstractmethod
    def tradable_days_in_data_time_zone(self) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """Gets the tradable days specified by this request, in the security's data time zone"""
        ...

    @property
    def is_custom_data(self) -> bool:
        """Gets true if this is a custom data request, false for normal QC data"""
        ...

    @property
    def data_type(self) -> typing.Type:
        """The data type of this request"""
        ...

    @property.setter
    def data_type(self, value: typing.Type) -> None:
        ...

    def __init__(self, startTimeUtc: typing.Union[datetime.datetime, datetime.date], endTimeUtc: typing.Union[datetime.datetime, datetime.date], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, tickType: QuantConnect.TickType, isCustomData: bool, dataType: typing.Type) -> None:
        """
        Initializes the base data request
        
        This method is protected.
        
        :param startTimeUtc: The start time for this request,
        :param endTimeUtc: The start time for this request
        :param exchangeHours: The exchange hours for this request
        :param tickType: The tick type of this request
        :param isCustomData: True if this subscription is for custom data
        :param dataType: The data type of the output data
        """
        ...


class Channel(System.Object):
    """Represents a subscription channel"""

    single: str = "common"
    """Represents an internal channel name for all brokerage channels in case we don't differentiate them"""

    @property
    def name(self) -> str:
        """The name of the channel"""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """The ticker symbol of the channel"""
        ...

    def __init__(self, channelName: str, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Creates an instance of subscription channel
        
        :param channelName: Socket channel name
        :param symbol: Associated symbol
        """
        ...

    @overload
    def equals(self, other: QuantConnect.Data.Channel) -> bool:
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


class DownloaderExtensions(System.Object):
    """Contains extension methods for the Downloader functionality."""

    @staticmethod
    def get_data_downloader_parameter_for_all_mapped_symbols(data_downloader_parameter: QuantConnect.DataDownloaderGetParameters, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, exchange_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.DataDownloaderGetParameters]:
        """
        Get DataDownloaderGetParameters for all mapped  with appropriate ticker name in specific date time range.
        
        :param data_downloader_parameter: Generated class in "Lean.Engine.DataFeeds.DownloaderDataProvider"
        :param map_file_provider: Provides instances of MapFileResolver at run time
        :param exchange_time_zone: Provides the time zone this exchange
        :returns: Return DataDownloaderGetParameters with different DataDownloaderGetParameters.StartUtc -  range and.
        """
        ...


class DataAggregatorInitializeParameters(System.Object):
    """The IDataAggregator parameters initialize dto"""

    @property
    def algorithm_settings(self) -> QuantConnect.Interfaces.IAlgorithmSettings:
        """The algorithm settings instance to use"""
        ...

    @property.setter
    def algorithm_settings(self, value: QuantConnect.Interfaces.IAlgorithmSettings) -> None:
        ...


class SubscriptionDataConfigExtensions(System.Object):
    """
    Helper methods used to determine different configurations properties
    for a given set of SubscriptionDataConfig
    """

    @staticmethod
    def data_normalization_mode(subscription_data_configs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> QuantConnect.DataNormalizationMode:
        """
        Extension method used to determine what QuantConnect.DataNormalizationMode
        to use for a given set of SubscriptionDataConfig
        
        :returns: The first DataNormalizationMode, DataNormalizationMode.Adjusted if there  are no subscriptions.
        """
        ...

    @staticmethod
    def emit_splits_and_dividends(config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Will determine if splits and dividends should be used for this subscription configuration
        
        :param config: The subscription data configuration we are processing
        :returns: True if this configuration requires split and divided handling.
        """
        ...

    @staticmethod
    def get_base_data_instance(config: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.BaseData:
        """Initializes a new instance of the BaseData type defined in  with the symbol properly set"""
        ...

    @staticmethod
    def get_highest_resolution(subscription_data_configs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> QuantConnect.Resolution:
        """
        Extension method used to obtain the highest Resolution
        for a given set of SubscriptionDataConfig
        
        :returns: The highest resolution, Resolution.Daily if there are no subscriptions.
        """
        ...

    @staticmethod
    def is_custom_data(subscription_data_configs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        """
        Extension method used to determine if it is custom data
        for a given set of SubscriptionDataConfig
        
        :returns: True, at least one subscription is custom data.
        """
        ...

    @staticmethod
    def is_extended_market_hours(subscription_data_configs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        """
        Extension method used to determine if ExtendedMarketHours is enabled
        for a given set of SubscriptionDataConfig
        
        :returns: True, at least one subscription has it enabled.
        """
        ...

    @staticmethod
    def is_fill_forward(subscription_data_configs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        """
        Extension method used to determine if FillForward is enabled
        for a given set of SubscriptionDataConfig
        
        :returns: True, at least one subscription has it enabled.
        """
        ...

    @staticmethod
    def prices_should_be_scaled(config: QuantConnect.Data.SubscriptionDataConfig, live_mode: bool = False) -> bool:
        """
        Will determine if price scaling should be used for this subscription configuration
        
        :param config: The subscription data configuration we are processing
        :param live_mode: True, is this is a live mode data stream
        :returns: True if ticker prices should be scaled.
        """
        ...

    @staticmethod
    def set_data_normalization_mode(subscription_data_configs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig], mode: QuantConnect.DataNormalizationMode) -> None:
        """
        Sets the data normalization mode to be used by
        this set of SubscriptionDataConfig
        """
        ...

    @staticmethod
    def ticker_should_be_mapped(config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Will determine if mapping should be used for this subscription configuration
        
        :param config: The subscription data configuration we are processing
        :returns: True if ticker should be mapped.
        """
        ...


class LeanDataWriter(System.Object):
    """Data writer for saving an IEnumerable of BaseData into the LEAN data directory."""

    map_file_provider: System.Lazy[QuantConnect.Interfaces.IMapFileProvider]
    """The map file provider instance to use"""

    @overload
    def __init__(self, resolution: QuantConnect.Resolution, symbol: typing.Union[QuantConnect.Symbol, str], dataDirectory: str, tickType: QuantConnect.TickType = ..., dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider = None, writePolicy: typing.Optional[QuantConnect.WritePolicy] = None, mapSymbol: bool = False) -> None:
        """
        Create a new lean data writer to this base data directory.
        
        :param resolution: Resolution of the desired output data
        :param symbol: Symbol string
        :param dataDirectory: Base data directory
        :param tickType: The tick type
        :param dataCacheProvider: The data cache provider to use
        :param writePolicy: The file write policy to use
        :param mapSymbol: True if the symbol should be mapped while writting the data
        """
        ...

    @overload
    def __init__(self, dataDirectory: str, resolution: QuantConnect.Resolution, securityType: QuantConnect.SecurityType, tickType: QuantConnect.TickType, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider = None, writePolicy: typing.Optional[QuantConnect.WritePolicy] = None) -> None:
        """
        Create a new lean data writer to this base data directory.
        
        :param dataDirectory: Base data directory
        :param resolution: Resolution of the desired output data
        :param securityType: The security type
        :param tickType: The tick type
        :param dataCacheProvider: The data cache provider to use
        :param writePolicy: The file write policy to use
        """
        ...

    def download_and_save(self, brokerage: QuantConnect.Interfaces.IBrokerage, symbols: System.Collections.Generic.List[QuantConnect.Symbol], start_time_utc: typing.Union[datetime.datetime, datetime.date], end_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Downloads historical data from the brokerage and saves it in LEAN format.
        
        :param brokerage: The brokerage from where to fetch the data
        :param symbols: The list of symbols
        :param start_time_utc: The starting date/time (UTC)
        :param end_time_utc: The ending date/time (UTC)
        """
        ...

    def write(self, source: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]) -> None:
        """
        Given the constructor parameters, write out the data in LEAN format.
        
        :param source: IEnumerable source of the data: sorted from oldest to newest.
        """
        ...


class IDataAggregator(System.IDisposable, metaclass=abc.ABCMeta):
    """Aggregates ticks and bars based on given subscriptions."""

    def add(self, data_config: QuantConnect.Data.SubscriptionDataConfig, new_data_available_handler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Add new subscription to current IDataAggregator instance
        
        :param data_config: defines the parameters to subscribe to a data feed
        :param new_data_available_handler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.DataAggregatorInitializeParameters) -> None:
        """
        Initialize this instance
        
        :param parameters: The parameters dto instance
        """
        ...

    def remove(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Remove the given subscription
        
        :param data_config: defines the subscription configuration data.
        :returns: Returns true if given SubscriptionDataConfig was found and succesfully removed; otherwise false.
        """
        ...

    def update(self, input: QuantConnect.Data.BaseData) -> None:
        """
        Adds new BaseData input into aggregator.
        
        :param input: The new data
        """
        ...


class IRiskFreeInterestRateModel(metaclass=abc.ABCMeta):
    """Represents a model that provides risk free interest rate data"""

    def get_interest_rate(self, date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get interest rate by a given date
        
        :param date: The date
        :returns: Interest rate on the given date.
        """
        ...


class InterestRateProvider(System.Object, QuantConnect.Data.IRiskFreeInterestRateModel):
    """Fed US Primary Credit Rate at given date"""

    DEFAULT_RISK_FREE_RATE: float = 0.01
    """Default Risk Free Rate of 1%"""

    @staticmethod
    def from_csv_file(file: str, first_interest_rate: typing.Optional[float]) -> typing.Union[System.Collections.Generic.Dictionary[datetime.datetime, float], float]:
        """
        Reads Fed primary credit rate file and returns a dictionary of historical rate changes
        
        :param file: The csv file to be read
        :param first_interest_rate: The first interest rate on file
        :returns: Dictionary of historical credit rate change events.
        """
        ...

    def get_interest_rate(self, date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get interest rate by a given date
        
        :param date: The date
        :returns: Interest rate on the given date.
        """
        ...

    @staticmethod
    def get_interest_rate_provider() -> System.Collections.Generic.Dictionary[datetime.datetime, float]:
        """
        Generate the daily historical US primary credit rate
        
        This method is protected.
        """
        ...

    @staticmethod
    def try_parse(csv_line: str, date: typing.Optional[typing.Union[datetime.datetime, datetime.date]], interest_rate: typing.Optional[float]) -> typing.Union[bool, typing.Union[datetime.datetime, datetime.date], float]:
        """
        Parse the string into the interest rate date and value
        
        :param csv_line: The csv line to be parsed
        :param date: Parsed interest rate date
        :param interest_rate: Parsed interest rate value
        """
        ...


class IDividendYieldModel(metaclass=abc.ABCMeta):
    """Represents a model that provides dividend yield data"""

    @overload
    def get_dividend_yield(self, date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get dividend yield by a given date of a given symbol
        
        :param date: The date
        :returns: Dividend yield on the given date of the given symbol.
        """
        ...

    @overload
    def get_dividend_yield(self, date: typing.Union[datetime.datetime, datetime.date], security_price: float) -> float:
        """
        Get dividend yield at given date and security price
        
        :param date: The date
        :param security_price: The security price at the given date
        :returns: Dividend yield on the given date of the given symbol.
        """
        ...


class HistoryProviderInitializeParameters(System.Object):
    """Represents the set of parameters for the IHistoryProvider.Initialize method"""

    @property
    def job(self) -> QuantConnect.Packets.AlgorithmNodePacket:
        """The job"""
        ...

    @property
    def api(self) -> QuantConnect.Interfaces.IApi:
        """The API instance"""
        ...

    @property
    def data_provider(self) -> QuantConnect.Interfaces.IDataProvider:
        """The provider used to get data when it is not present on disk"""
        ...

    @property
    def data_cache_provider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """The provider used to cache history data files"""
        ...

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """The provider used to get a map file resolver to handle equity mapping"""
        ...

    @property
    def factor_file_provider(self) -> QuantConnect.Interfaces.IFactorFileProvider:
        """The provider used to get factor files to handle equity price scaling"""
        ...

    @property
    def status_update_action(self) -> typing.Callable[[int], None]:
        """A function used to send status updates"""
        ...

    @property
    def parallel_history_requests_enabled(self) -> bool:
        """True if parallel history requests are enabled"""
        ...

    @property
    def data_permission_manager(self) -> QuantConnect.Interfaces.IDataPermissionManager:
        """The data permission manager"""
        ...

    @property
    def object_store(self) -> QuantConnect.Interfaces.IObjectStore:
        """The object store"""
        ...

    @property
    def algorithm_settings(self) -> QuantConnect.Interfaces.IAlgorithmSettings:
        """The algorithm settings instance to use"""
        ...

    def __init__(self, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi, dataProvider: QuantConnect.Interfaces.IDataProvider, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, statusUpdateAction: typing.Callable[[int], None], parallelHistoryRequestsEnabled: bool, dataPermissionManager: QuantConnect.Interfaces.IDataPermissionManager, objectStore: QuantConnect.Interfaces.IObjectStore, algorithmSettings: QuantConnect.Interfaces.IAlgorithmSettings) -> None:
        """
        Initializes a new instance of the HistoryProviderInitializeParameters class from the specified parameters
        
        :param job: The job
        :param api: The API instance
        :param dataProvider: Provider used to get data when it is not present on disk
        :param dataCacheProvider: Provider used to cache history data files
        :param mapFileProvider: Provider used to get a map file resolver to handle equity mapping
        :param factorFileProvider: Provider used to get factor files to handle equity price scaling
        :param statusUpdateAction: Function used to send status updates
        :param parallelHistoryRequestsEnabled: True if parallel history requests are enabled
        :param dataPermissionManager: The data permission manager to use
        :param objectStore: The object store to use
        :param algorithmSettings: The algorithm settings instance to use
        """
        ...


class Slice(QuantConnect.ExtendedDictionary[typing.Any], typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.BaseData]]):
    """Provides a data structure for all of an algorithm's data at a single time step"""

    @property
    def all_data(self) -> System.Collections.Generic.List[QuantConnect.Data.BaseData]:
        """All the data hold in this slice"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Gets the timestamp for this slice of data"""
        ...

    @property
    def utc_time(self) -> datetime.datetime:
        """Gets the timestamp for this slice of data in UTC"""
        ...

    @property
    def has_data(self) -> bool:
        """Gets whether or not this slice has data"""
        ...

    @property
    def bars(self) -> QuantConnect.Data.Market.TradeBars:
        """Gets the TradeBars for this slice of data"""
        ...

    @property
    def quote_bars(self) -> QuantConnect.Data.Market.QuoteBars:
        """Gets the QuoteBars for this slice of data"""
        ...

    @property
    def ticks(self) -> QuantConnect.Data.Market.Ticks:
        """Gets the Ticks for this slice of data"""
        ...

    @property
    def option_chains(self) -> QuantConnect.Data.Market.OptionChains:
        """Gets the OptionChains for this slice of data"""
        ...

    @property
    def futures_chains(self) -> QuantConnect.Data.Market.FuturesChains:
        """Gets the FuturesChains for this slice of data"""
        ...

    @property
    def future_chains(self) -> QuantConnect.Data.Market.FuturesChains:
        """Gets the FuturesChains for this slice of data"""
        ...

    @property
    def splits(self) -> QuantConnect.Data.Market.Splits:
        """Gets the Splits for this slice of data"""
        ...

    @property
    def dividends(self) -> QuantConnect.Data.Market.Dividends:
        """Gets the Dividends for this slice of data"""
        ...

    @property
    def delistings(self) -> QuantConnect.Data.Market.Delistings:
        """Gets the Delistings for this slice of data"""
        ...

    @property
    def symbol_changed_events(self) -> QuantConnect.Data.Market.SymbolChangedEvents:
        """Gets the Market.SymbolChangedEvents for this slice of data"""
        ...

    @property
    def margin_interest_rates(self) -> QuantConnect.Data.Market.MarginInterestRates:
        """Gets the Market.MarginInterestRates for this slice of data"""
        ...

    @property
    def count(self) -> int:
        """Gets the number of symbols held in this slice"""
        ...

    @property
    def keys(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Symbol]:
        """Gets all the symbols in this slice"""
        ...

    @property
    def get_keys(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the Symbol objects of the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    @property
    def get_values(self) -> System.Collections.Generic.IEnumerable[typing.Any]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    @property
    def values(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]:
        """Gets a list of all the data in this slice"""
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> typing.Union[QuantConnect.Data.Market.TradeBar, QuantConnect.Data.Market.QuoteBar, System.Collections.Generic.List[QuantConnect.Data.Market.Tick], typing.Any]:
        """
        Gets the data corresponding to the specified symbol. If the requested data
        is of MarketDataType.Tick, then a List{Tick} will
        be returned, otherwise, it will be the subscribed type, for example, TradeBar
        or event UnlinkedData for custom data.
        
        :param symbol: The data's symbols
        :returns: The data for the specified symbol.
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], data: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], utcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Slice class, lazily
        instantiating the Slice.Bars and Slice.Ticks
        collections on demand
        
        :param time: The timestamp for this slice of data
        :param data: The raw data in this slice
        :param utcTime: The timestamp for this slice of data in UTC
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], data: System.Collections.Generic.List[QuantConnect.Data.BaseData], utcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Slice class, lazily
        instantiating the Slice.Bars and Slice.Ticks
        collections on demand
        
        :param time: The timestamp for this slice of data
        :param data: The raw data in this slice
        :param utcTime: The timestamp for this slice of data in UTC
        """
        ...

    @overload
    def __init__(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Initializes a new instance used by the PythonSlice
        
        This method is protected.
        
        :param slice: slice object to wrap
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], data: System.Collections.Generic.List[QuantConnect.Data.BaseData], tradeBars: QuantConnect.Data.Market.TradeBars, quoteBars: QuantConnect.Data.Market.QuoteBars, ticks: QuantConnect.Data.Market.Ticks, optionChains: QuantConnect.Data.Market.OptionChains, futuresChains: QuantConnect.Data.Market.FuturesChains, splits: QuantConnect.Data.Market.Splits, dividends: QuantConnect.Data.Market.Dividends, delistings: QuantConnect.Data.Market.Delistings, symbolChanges: QuantConnect.Data.Market.SymbolChangedEvents, marginInterestRates: QuantConnect.Data.Market.MarginInterestRates, utcTime: typing.Union[datetime.datetime, datetime.date], hasData: typing.Optional[bool] = None) -> None:
        """
        Initializes a new instance of the Slice class
        
        :param time: The timestamp for this slice of data
        :param data: The raw data in this slice
        :param tradeBars: The trade bars for this slice
        :param quoteBars: The quote bars for this slice
        :param ticks: This ticks for this slice
        :param optionChains: The option chains for this slice
        :param futuresChains: The futures chains for this slice
        :param splits: The splits for this slice
        :param dividends: The dividends for this slice
        :param delistings: The delistings for this slice
        :param symbolChanges: The symbol changed events for this slice
        :param marginInterestRates: The margin interest rates for this slice
        :param utcTime: The timestamp for this slice of data in UTC
        :param hasData: true if this slice contains data
        """
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: typing.Union[QuantConnect.Data.Market.TradeBar, QuantConnect.Data.Market.QuoteBar, System.Collections.Generic.List[QuantConnect.Data.Market.Tick], typing.Any]) -> None:
        """
        Gets the data corresponding to the specified symbol. If the requested data
        is of MarketDataType.Tick, then a List{Tick} will
        be returned, otherwise, it will be the subscribed type, for example, TradeBar
        or event UnlinkedData for custom data.
        
        :param symbol: The data's symbols
        :returns: The data for the specified symbol.
        """
        ...

    def contains_key(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines whether this instance contains data for the specified symbol
        
        :param symbol: The symbol we seek data for
        :returns: True if this instance contains data for the symbol, false otherwise.
        """
        ...

    @overload
    def get(self, type: QuantConnect_Data_Slice_Get_T) -> QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Slice_Get_T]:
        """
        Gets the data of the specified type.
        
        :param type: The type of data we seek
        :returns: The DataDictionary{T} instance for the requested type.
        """
        ...

    @overload
    def get(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Slice_Get_T:
        """
        Gets the data of the specified symbol and type.
        
        :param symbol: The specific symbol was seek
        :returns: The data for the requested symbol.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.BaseData]]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    def get_impl(self, type: typing.Type, instance: QuantConnect.Data.Slice) -> typing.Any:
        """
        Gets the data of the specified type.
        
        This method is protected.
        """
        ...

    def merge_slice(self, input_slice: QuantConnect.Data.Slice) -> None:
        """
        Merge two slice with same Time
        
        :param input_slice: slice instance
        """
        ...

    def try_get_value(self, symbol: typing.Union[QuantConnect.Symbol, str], data: typing.Optional[typing.Any]) -> typing.Union[bool, typing.Any]:
        """
        Gets the data associated with the specified symbol
        
        :param symbol: The symbol we want data for
        :param data: The data for the specifed symbol, or null if no data was found
        :returns: True if data was found, false otherwise.
        """
        ...


class HistoryRequest(QuantConnect.Data.BaseDataRequest):
    """Represents a request for historical data"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol to request data for"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """Gets the requested data resolution"""
        ...

    @property.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def fill_forward_resolution(self) -> typing.Optional[QuantConnect.Resolution]:
        """
        Gets the requested fill forward resolution, set to null for no fill forward behavior.
        Will always return null when Resolution is set to Tick.
        """
        ...

    @property.setter
    def fill_forward_resolution(self, value: typing.Optional[QuantConnect.Resolution]) -> None:
        ...

    @property
    def include_extended_market_hours(self) -> bool:
        """Gets whether or not to include extended market hours data, set to false for only normal market hours"""
        ...

    @property.setter
    def include_extended_market_hours(self, value: bool) -> None:
        ...

    @property
    def data_time_zone(self) -> typing.Any:
        """Gets the time zone of the time stamps on the raw input data"""
        ...

    @property.setter
    def data_time_zone(self, value: typing.Any) -> None:
        ...

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """TickType of the history request"""
        ...

    @property.setter
    def tick_type(self, value: QuantConnect.TickType) -> None:
        ...

    @property
    def data_normalization_mode(self) -> QuantConnect.DataNormalizationMode:
        """Gets the normalization mode used for this subscription"""
        ...

    @property.setter
    def data_normalization_mode(self, value: QuantConnect.DataNormalizationMode) -> None:
        ...

    @property
    def data_mapping_mode(self) -> QuantConnect.DataMappingMode:
        """Gets the data mapping mode used for this subscription"""
        ...

    @property.setter
    def data_mapping_mode(self, value: QuantConnect.DataMappingMode) -> None:
        ...

    @property
    def contract_depth_offset(self) -> int:
        """
        The continuous contract desired offset from the current front month.
        For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @property.setter
    def contract_depth_offset(self, value: int) -> None:
        ...

    @property
    def tradable_days_in_data_time_zone(self) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """Gets the tradable days specified by this request, in the security's data time zone"""
        ...

    @overload
    def __init__(self, startTimeUtc: typing.Union[datetime.datetime, datetime.date], endTimeUtc: typing.Union[datetime.datetime, datetime.date], dataType: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, dataTimeZone: typing.Any, fillForwardResolution: typing.Optional[QuantConnect.Resolution], includeExtendedMarketHours: bool, isCustomData: bool, dataNormalizationMode: QuantConnect.DataNormalizationMode, tickType: QuantConnect.TickType, dataMappingMode: QuantConnect.DataMappingMode = ..., contractDepthOffset: int = 0) -> None:
        """
        Initializes a new instance of the HistoryRequest class from the specified parameters
        
        :param startTimeUtc: The start time for this request,
        :param endTimeUtc: The end time for this request
        :param dataType: The data type of the output data
        :param symbol: The symbol to request data for
        :param resolution: The requested data resolution
        :param exchangeHours: The exchange hours used in fill forward processing
        :param dataTimeZone: The time zone of the data
        :param fillForwardResolution: The requested fill forward resolution for this request
        :param includeExtendedMarketHours: True to include data from pre/post market hours
        :param isCustomData: True for custom user data, false for normal QC data
        :param dataNormalizationMode: Specifies normalization mode used for this subscription
        :param tickType: The tick type used to created the SubscriptionDataConfig for the retrieval of history data
        :param dataMappingMode: The contract mapping mode to use for the security
        :param contractDepthOffset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, hours: QuantConnect.Securities.SecurityExchangeHours, startTimeUtc: typing.Union[datetime.datetime, datetime.date], endTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the HistoryRequest class from the specified config and exchange hours
        
        :param config: The subscription data config used to initialize this request
        :param hours: The exchange hours used for fill forward processing
        :param startTimeUtc: The start time for this request,
        :param endTimeUtc: The end time for this request
        """
        ...

    @overload
    def __init__(self, request: QuantConnect.Data.HistoryRequest, newSymbol: typing.Union[QuantConnect.Symbol, str], newStartTimeUtc: typing.Union[datetime.datetime, datetime.date], newEndTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the HistoryRequest class with new Symbol, StartTimeUtc, EndTimeUtc
        
        :param request: Represents a request for historical data
        :param newStartTimeUtc: The start time for this request
        :param newEndTimeUtc: The end time for this request
        """
        ...


class HistoryProviderBase(System.Object, QuantConnect.Interfaces.IHistoryProvider, metaclass=abc.ABCMeta):
    """Provides a base type for all history providers"""

    @property
    def invalid_configuration_detected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.InvalidConfigurationDetectedEventArgs], None], None]:
        """Event fired when an invalid configuration has been detected"""
        ...

    @property
    def numerical_precision_limited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.NumericalPrecisionLimitedEventArgs], None], None]:
        """Event fired when the numerical precision in the factor file has been limited"""
        ...

    @property
    def start_date_limited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.StartDateLimitedEventArgs], None], None]:
        """Event fired when the start date has been limited"""
        ...

    @property
    def download_failed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.DownloadFailedEventArgs], None], None]:
        """Event fired when there was an error downloading a remote file"""
        ...

    @property
    def reader_error_detected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.ReaderErrorDetectedEventArgs], None], None]:
        """Event fired when there was an error reading the data"""
        ...

    @property
    @abc.abstractmethod
    def data_point_count(self) -> int:
        """Gets the total number of data points emitted by this history provider"""
        ...

    def get_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param slice_time_zone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
        """
        ...

    def on_download_failed(self, e: QuantConnect.DownloadFailedEventArgs) -> None:
        """
        Event invocator for the DownloadFailed event
        
        This method is protected.
        
        :param e: Event arguments for the DownloadFailed event
        """
        ...

    def on_invalid_configuration_detected(self, e: QuantConnect.InvalidConfigurationDetectedEventArgs) -> None:
        """
        Event invocator for the InvalidConfigurationDetected event
        
        This method is protected.
        
        :param e: Event arguments for the InvalidConfigurationDetected event
        """
        ...

    def on_numerical_precision_limited(self, e: QuantConnect.NumericalPrecisionLimitedEventArgs) -> None:
        """
        Event invocator for the NumericalPrecisionLimited event
        
        This method is protected.
        
        :param e: Event arguments for the NumericalPrecisionLimited event
        """
        ...

    def on_reader_error_detected(self, e: QuantConnect.ReaderErrorDetectedEventArgs) -> None:
        """
        Event invocator for the ReaderErrorDetected event
        
        This method is protected.
        
        :param e: Event arguments for the ReaderErrorDetected event
        """
        ...

    def on_start_date_limited(self, e: QuantConnect.StartDateLimitedEventArgs) -> None:
        """
        Event invocator for the StartDateLimited event
        
        This method is protected.
        
        :param e: Event arguments for the StartDateLimited event
        """
        ...


class DataHistory(typing.Generic[QuantConnect_Data_DataHistory_T], System.Object, typing.Iterable[QuantConnect_Data_DataHistory_T]):
    """Historical data abstraction"""

    @property
    def data(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Data_DataHistory_T]:
        """
        The data we hold
        
        This property is protected.
        """
        ...

    @property
    def count(self) -> int:
        """The current data point count"""
        ...

    @property
    def data_frame(self) -> typing.Any:
        """This data pandas data frame"""
        ...

    def __init__(self, data: System.Collections.Generic.IEnumerable[QuantConnect_Data_DataHistory_T], dataframe: System.Lazy[PyObject]) -> None:
        """Creates a new instance"""
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect_Data_DataHistory_T]:
        """Returns an enumerator for the data"""
        ...

    def to_string(self) -> str:
        """Default to string implementation"""
        ...


class IndicatorHistory(QuantConnect.Data.DataHistory[QuantConnect.Indicators.IndicatorDataPoints]):
    """Provides historical values of an indicator"""

    @property
    def current(self) -> System.Collections.Generic.List[QuantConnect.Indicators.IndicatorDataPoint]:
        """The indicators historical values"""
        ...

    def __getitem__(self, name: str) -> System.Collections.Generic.List[QuantConnect.Indicators.IndicatorDataPoint]:
        """Access the historical indicator values per indicator property name"""
        ...

    def __init__(self, indicatorsDataPointsByTime: System.Collections.Generic.List[QuantConnect.Indicators.IndicatorDataPoints], indicatorsDataPointPerProperty: System.Collections.Generic.List[QuantConnect.Indicators.InternalIndicatorValues], dataframe: System.Lazy[PyObject]) -> None:
        """
        Creates a new instance
        
        :param indicatorsDataPointsByTime: Indicators data points by time
        :param indicatorsDataPointPerProperty: Indicators data points by property name
        :param dataframe: The lazy data frame constructor
        """
        ...


class RiskFreeInterestRateModelExtensions(System.Object):
    """Provide extension and static methods for IRiskFreeInterestRateModel"""

    @staticmethod
    def get_average_risk_free_rate(model: QuantConnect.Data.IRiskFreeInterestRateModel, dates: System.Collections.Generic.IEnumerable[datetime.datetime]) -> float:
        """
        Gets the average Risk Free Rate from the interest rate of the given dates
        
        :param model: The interest rate model
        :param dates: Collection of dates from which the interest rates will be computed and then the average of them
        """
        ...

    @staticmethod
    def get_risk_free_rate(model: QuantConnect.Data.IRiskFreeInterestRateModel, start_date: typing.Union[datetime.datetime, datetime.date], end_date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Gets the average risk free annual return rate
        
        :param model: The interest rate model
        :param start_date: Start date to calculate the average
        :param end_date: End date to calculate the average
        """
        ...


class DataQueueHandlerSubscriptionManager(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """Count number of subscribers for each channel (Symbol, Socket) pair"""

    @property
    def subscribers_by_channel(self) -> System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Data.Channel, int]:
        """
        Counter
        
        This property is protected.
        """
        ...

    def channel_name_from_tick_type(self, tick_type: QuantConnect.TickType) -> str:
        """
        Brokerage maps TickType to real socket/api channel
        
        This method is protected.
        
        :param tick_type: Type of tick data
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @overload
    def get_subscribed_symbols(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Returns subscribed symbols
        
        :returns: list of Symbol currently subscribed.
        """
        ...

    @overload
    def get_subscribed_symbols(self, tick_type: QuantConnect.TickType) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Retrieves the list of unique Symbol instances that are currently subscribed for a specific TickType.
        
        :param tick_type: The type of tick data to filter subscriptions by.
        :returns: A collection of unique Symbol objects that match the specified .
        """
        ...

    def is_subscribed(self, symbol: typing.Union[QuantConnect.Symbol, str], tick_type: QuantConnect.TickType) -> bool:
        """
        Checks if there is existing subscriber for current channel
        
        :param symbol: Symbol
        :param tick_type: Type of tick data
        :returns: return true if there is one subscriber at least; otherwise false.
        """
        ...

    @overload
    def subscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Increment number of subscribers for current TickType
        
        :param data_config: defines the subscription configuration data.
        """
        ...

    @overload
    def subscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tick_type: QuantConnect.TickType) -> bool:
        """
        Describes the way IDataQueueHandler implements subscription
        
        This method is protected.
        
        :param symbols: Symbols to subscribe
        :param tick_type: Type of tick data
        :returns: Returns true if subsribed; otherwise false.
        """
        ...

    @overload
    def unsubscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Decrement number of subscribers for current TickType
        
        :param data_config: defines the subscription configuration data.
        """
        ...

    @overload
    def unsubscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tick_type: QuantConnect.TickType) -> bool:
        """
        Describes the way IDataQueueHandler implements unsubscription
        
        This method is protected.
        
        :param symbols: Symbols to unsubscribe
        :param tick_type: Type of tick data
        :returns: Returns true if unsubsribed; otherwise false.
        """
        ...


class EventBasedDataQueueHandlerSubscriptionManager(QuantConnect.Data.DataQueueHandlerSubscriptionManager):
    """Overrides DataQueueHandlerSubscriptionManager methods using events"""

    @property
    def subscribe_impl(self) -> typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]:
        """Subscription method implementation"""
        ...

    @property.setter
    def subscribe_impl(self, value: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]) -> None:
        ...

    @property
    def unsubscribe_impl(self) -> typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]:
        """Unsubscription method implementation"""
        ...

    @property.setter
    def unsubscribe_impl(self, value: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Creates an instance of EventBasedDataQueueHandlerSubscriptionManager with a single channel name"""
        ...

    @overload
    def __init__(self, getChannelName: typing.Callable[[QuantConnect.TickType], str]) -> None:
        """
        Creates an instance of EventBasedDataQueueHandlerSubscriptionManager
        
        :param getChannelName: Convert TickType into string
        """
        ...

    def channel_name_from_tick_type(self, tick_type: QuantConnect.TickType) -> str:
        """
        Channel name
        
        This method is protected.
        
        :param tick_type: Type of tick data
        :returns: Returns Socket channel name corresponding.
        """
        ...

    def subscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tick_type: QuantConnect.TickType) -> bool:
        """
        The way Brokerage subscribes to symbol tickers
        
        This method is protected.
        
        :param symbols: Symbols to subscribe
        :param tick_type: Type of tick data
        """
        ...

    def unsubscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tick_type: QuantConnect.TickType) -> bool:
        """
        The way Brokerage unsubscribes from symbol tickers
        
        This method is protected.
        
        :param symbols: Symbols to unsubscribe
        :param tick_type: Type of tick data
        """
        ...


class ISymbolProvider(metaclass=abc.ABCMeta):
    """Base data with a symbol"""

    @property
    @abc.abstractmethod
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the Symbol"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...


class IBaseData(QuantConnect.Data.ISymbolProvider, metaclass=abc.ABCMeta):
    """Base Data Class: Type, Timestamp, Key -- Base Features."""

    @property
    @abc.abstractmethod
    def data_type(self) -> QuantConnect.MarketDataType:
        """Market Data Type of this data - does it come in individual price packets or is it grouped into OHLC."""
        ...

    @property.setter
    def data_type(self, value: QuantConnect.MarketDataType) -> None:
        ...

    @property
    @abc.abstractmethod
    def time(self) -> datetime.datetime:
        """Time keeper of data -- all data is timeseries based."""
        ...

    @property.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    @abc.abstractmethod
    def end_time(self) -> datetime.datetime:
        """End time of data"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    @abc.abstractmethod
    def value(self) -> float:
        """All timeseries data is a time-value pair:"""
        ...

    @property.setter
    def value(self, value: float) -> None:
        ...

    @property
    @abc.abstractmethod
    def price(self) -> float:
        """Alias of Value."""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Return a new instance clone of this object"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], datafeed: QuantConnect.DataFeedEndpoint) -> str:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param datafeed: Type of datafeed we're reqesting - backtest or live
        :returns: String URL of source file.
        """
        ...

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    @overload
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

    @overload
    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], data_feed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        """
        Reader Method :: using set of arguements we specify read out type. Enumerate
        until the end of the data stream or file. E.g. Read CSV file line by line and convert
        into data types.
        
        Reader(SubscriptionDataConfig, string, DateTime, DataFeedEndpoint) method has been made obsolete, use Reader(SubscriptionDataConfig, string, DateTime, bool) instead.
        
        :returns: BaseData type set by Subscription Method.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...


class HistoryRequestFactory(System.Object):
    """Helper class used to create new HistoryRequest"""

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Creates a new instance
        
        :param algorithm: The algorithm instance to use
        """
        ...

    def create_history_request(self, subscription: QuantConnect.Data.SubscriptionDataConfig, start_algo_tz: typing.Union[datetime.datetime, datetime.date], end_algo_tz: typing.Union[datetime.datetime, datetime.date], exchange_hours: QuantConnect.Securities.SecurityExchangeHours, resolution: typing.Optional[QuantConnect.Resolution], fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> QuantConnect.Data.HistoryRequest:
        """
        Creates a new history request
        
        :param subscription: The config
        :param start_algo_tz: History request start time in algorithm time zone
        :param end_algo_tz: History request end time in algorithm time zone
        :param exchange_hours: Security exchange hours
        :param resolution: The resolution to use. If null will use SubscriptionDataConfig.Resolution
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: The new HistoryRequest.
        """
        ...

    @overload
    def get_start_time_algo_tz(self, symbol: typing.Union[QuantConnect.Symbol, str], periods: int, resolution: QuantConnect.Resolution, exchange: QuantConnect.Securities.SecurityExchangeHours, data_time_zone: typing.Any, data_type: typing.Type, extended_market_hours: typing.Optional[bool] = None) -> datetime.datetime:
        """
        Gets the start time required for the specified bar count in terms of the algorithm's time zone
        
        :param symbol: The symbol to select proper SubscriptionDataConfig config
        :param periods: The number of bars requested
        :param resolution: The length of each bar
        :param exchange: The exchange hours used for market open hours
        :param data_time_zone: The time zone in which data are stored
        :param data_type: The data type to request
        :param extended_market_hours: True to include extended market hours data, false otherwise. If not passed, the config will be used to determined whether to include extended market hours.
        :returns: The start time that would provide the specified number of bars ending at the algorithm's current time.
        """
        ...

    @overload
    def get_start_time_algo_tz(self, reference_utc_time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], periods: int, resolution: QuantConnect.Resolution, exchange: QuantConnect.Securities.SecurityExchangeHours, data_time_zone: typing.Any, data_type: typing.Type, extended_market_hours: typing.Optional[bool] = None) -> datetime.datetime:
        """
        Gets the start time required for the specified bar count in terms of the algorithm's time zone
        
        :param reference_utc_time: The end time in utc
        :param symbol: The symbol to select proper SubscriptionDataConfig config
        :param periods: The number of bars requested
        :param resolution: The length of each bar
        :param exchange: The exchange hours used for market open hours
        :param data_time_zone: The time zone in which data are stored
        :param data_type: The data type to request
        :param extended_market_hours: True to include extended market hours data, false otherwise. If not passed, the config will be used to determined whether to include extended market hours.
        :returns: The start time that would provide the specified number of bars ending at the algorithm's current time.
        """
        ...


class GetSetPropertyDynamicMetaObject(DynamicMetaObject):
    """
    Provides an implementation of DynamicMetaObject that uses get/set methods to update
    values in the dynamic object.
    """

    def __init__(self, expression: typing.Any, value: typing.Any, setPropertyMethodInfo: System.Reflection.MethodInfo, getPropertyMethodInfo: System.Reflection.MethodInfo) -> None:
        """
        Initializes a new instance of the QuantConnect.Data.GetSetPropertyDynamicMetaObject class.
        
        :param expression: The expression representing this System.Dynamic.DynamicMetaObject
        :param value: The value represented by the System.Dynamic.DynamicMetaObject
        :param setPropertyMethodInfo: The set method to use for updating this dynamic object
        :param getPropertyMethodInfo: The get method to use for updating this dynamic object
        """
        ...

    def bind_get_member(self, binder: typing.Any) -> typing.Any:
        """
        Performs the binding of the dynamic get member operation.
        
        :param binder: An instance of the System.Dynamic.GetMemberBinder that represents the details of the dynamic operation.
        :returns: The new System.Dynamic.DynamicMetaObject representing the result of the binding.
        """
        ...

    def bind_set_member(self, binder: typing.Any, value: typing.Any) -> typing.Any:
        """
        Performs the binding of the dynamic set member operation.
        
        :param binder: An instance of the System.Dynamic.SetMemberBinder that represents the details of the dynamic operation.
        :param value: The System.Dynamic.DynamicMetaObject representing the value for the set member operation.
        :returns: The new System.Dynamic.DynamicMetaObject representing the result of the binding.
        """
        ...


class ConstantRiskFreeRateInterestRateModel(System.Object, QuantConnect.Data.IRiskFreeInterestRateModel):
    """Constant risk free rate interest rate model"""

    def __init__(self, riskFreeRate: float) -> None:
        """Instantiates a ConstantRiskFreeRateInterestRateModel with the specified risk free rate"""
        ...

    def get_interest_rate(self, date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get interest rate by a given date
        
        :param date: The date
        :returns: Interest rate on the given date.
        """
        ...


class HistoryExtensions(System.Object):
    """Helper extension methods for objects related with Histotical data"""

    @staticmethod
    def split_history_request_with_updated_mapped_symbol(request: QuantConnect.Data.HistoryRequest, map_file_provider: QuantConnect.Interfaces.IMapFileProvider) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Split HistoryRequest on several request with update mapped symbol.
        
        :param request: Represents historical data requests
        :param map_file_provider: Provides instances of MapFileResolver at run time
        :returns: Return HistoryRequests with different BaseDataRequest.StartTimeUtc -  range and.
        """
        ...

    @staticmethod
    def try_get_brokerage_name(history_provider_name: str, brokerage_name: typing.Optional[str]) -> typing.Union[bool, str]:
        """Helper method to get the brokerage name"""
        ...


class DividendYieldProvider(System.Object, QuantConnect.Data.IDividendYieldModel):
    """Estimated annualized continuous dividend yield at given date"""

    default_symbol: QuantConnect.Symbol
    """The default symbol to use as a dividend yield provider"""

    _corporate_events_cache: System.Collections.Generic.Dictionary[QuantConnect.Symbol, System.Collections.Generic.List[QuantConnect.Data.BaseData]]
    """
    The dividends by symbol
    
    This field is protected.
    """

    _cache_clear_task: System.Threading.Tasks.Task
    """
    Task to clear the cache
    
    This field is protected.
    """

    DEFAULT_DIVIDEND_YIELD_RATE: float = 0.0
    """Default no dividend payout"""

    @property
    def cache_refresh_period(self) -> datetime.timedelta:
        """
        The cached refresh period for the dividend yield rate
        
        This property is protected.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance using the default symbol"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """Instantiates a DividendYieldProvider with the specified Symbol"""
        ...

    @staticmethod
    def create_for_option(option_symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.IDividendYieldModel:
        """Creates a new instance for the given option symbol"""
        ...

    @overload
    def get_dividend_yield(self, date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get dividend yield by a given date of a given symbol.
        It will get the dividend yield at the time of the most recent dividend since no price is provided.
        In order to get more accurate dividend yield, provide the security price at the given date to
        the GetDividendYield(DateTime, decimal) or GetDividendYield(IBaseData) methods.
        
        :param date: The date
        :returns: Dividend yield on the given date of the given symbol.
        """
        ...

    @overload
    def get_dividend_yield(self, price_data: QuantConnect.Data.IBaseData) -> float:
        """
        Gets the dividend yield at the date of the specified data, using the data price as the security price
        
        :param price_data: Price data instance
        :returns: Dividend yield on the given date of the given symbol.
        """
        ...

    @overload
    def get_dividend_yield(self, date: typing.Union[datetime.datetime, datetime.date], security_price: float) -> float:
        """
        Get dividend yield at given date and security price
        
        :param date: The date
        :param security_price: The security price at the given date
        :returns: Dividend yield on the given date of the given symbol.
        """
        ...

    def load_corporate_events(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect.Data.BaseData]:
        """
        Generate the corporate events from the corporate factor file for the specified symbol
        
        This method is protected.
        """
        ...


class SubscriptionManager(System.Object):
    """Enumerable Subscription Management Class"""

    @property
    def subscription_data_config_service(self) -> QuantConnect.Interfaces.ISubscriptionDataConfigService:
        """Instance that implements ISubscriptionDataConfigService"""
        ...

    @property
    def subscriptions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]:
        """Returns an IEnumerable of Subscriptions"""
        ...

    @property
    def available_data_types(self) -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]:
        """The different TickType each SecurityType supports"""
        ...

    @property
    def count(self) -> int:
        """Get the count of assets:"""
        ...

    def __init__(self, timeKeeper: QuantConnect.Interfaces.ITimeKeeper) -> None:
        """Creates a new instance"""
        ...

    @overload
    def add(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, time_zone: typing.Any, exchange_time_zone: typing.Any, is_custom_data: bool = False, fill_forward: bool = True, extended_market_hours: bool = False) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Add Market Data Required (Overloaded method for backwards compatibility).
        
        :param symbol: Symbol of the asset we're like
        :param resolution: Resolution of Asset Required
        :param time_zone: The time zone the subscription's data is time stamped in
        :param exchange_time_zone: Specifies the time zone of the exchange for the security this subscription is for. This     is this output time zone, that is, the time zone that will be used on BaseData instances
        :param is_custom_data: True if this is custom user supplied data, false for normal QC data
        :param fill_forward: when there is no data pass the last tradebar forward
        :param extended_market_hours: Request premarket data as well when true
        :returns: The newly created SubscriptionDataConfig or existing instance if it already existed.
        """
        ...

    @overload
    def add(self, data_type: typing.Type, tick_type: QuantConnect.TickType, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, data_time_zone: typing.Any, exchange_time_zone: typing.Any, is_custom_data: bool, fill_forward: bool = True, extended_market_hours: bool = False, is_internal_feed: bool = False, is_filtered_subscription: bool = True, data_normalization_mode: QuantConnect.DataNormalizationMode = ...) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Add Market Data Required - generic data typing support as long as Type implements BaseData.
        
        :param data_type: Set the type of the data we're subscribing to.
        :param tick_type: Tick type for the subscription.
        :param symbol: Symbol of the asset we're like
        :param resolution: Resolution of Asset Required
        :param data_time_zone: The time zone the subscription's data is time stamped in
        :param exchange_time_zone: Specifies the time zone of the exchange for the security this subscription is for. This     is this output time zone, that is, the time zone that will be used on BaseData instances
        :param is_custom_data: True if this is custom user supplied data, false for normal QC data
        :param fill_forward: when there is no data pass the last tradebar forward
        :param extended_market_hours: Request premarket data as well when true
        :param is_internal_feed: Set to true to prevent data from this subscription from being sent into the algorithm's     OnData events
        :param is_filtered_subscription: True if this subscription should have filters applied to it (market hours/user     filters from security), false otherwise
        :param data_normalization_mode: Define how data is normalized
        :returns: The newly created SubscriptionDataConfig or existing instance if it already existed.
        """
        ...

    @overload
    def add_consolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta], tick_type: typing.Optional[QuantConnect.TickType] = None) -> None:
        """
        Add a consolidator for the symbol
        
        :param symbol: Symbol of the asset to consolidate
        :param consolidator: The consolidator
        :param tick_type: Desired tick type for the subscription
        """
        ...

    @overload
    def add_consolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], py_consolidator: typing.Any) -> None:
        """
        Add a custom python consolidator for the symbol
        
        :param symbol: Symbol of the asset to consolidate
        :param py_consolidator: The custom python consolidator
        """
        ...

    @staticmethod
    def default_data_types() -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]:
        """Hard code the set of default available data feeds"""
        ...

    def get_data_types_for_security(self, security_type: QuantConnect.SecurityType) -> System.Collections.Generic.IReadOnlyList[QuantConnect.TickType]:
        """Get the available data types for a security"""
        ...

    @staticmethod
    def is_subscription_valid_for_consolidator(subscription: QuantConnect.Data.SubscriptionDataConfig, consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta], desired_tick_type: typing.Optional[QuantConnect.TickType] = None) -> bool:
        """
        Checks if the subscription is valid for the consolidator
        
        :param subscription: The subscription configuration
        :param consolidator: The consolidator
        :param desired_tick_type: The desired tick type for the subscription. If not given is null.
        :returns: true if the subscription is valid for the consolidator.
        """
        ...

    def lookup_subscription_config_data_types(self, symbol_security_type: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, is_canonical: bool) -> System.Collections.Generic.List[System.Tuple[typing.Type, QuantConnect.TickType]]:
        """
        Get the data feed types for a given SecurityTypeResolution
        
        :param symbol_security_type: The SecurityType used to determine the types
        :param resolution: The resolution of the data requested
        :param is_canonical: Indicates whether the security is Canonical (future and options)
        :returns: Types that should be added to the SubscriptionDataConfig.
        """
        ...

    @overload
    def remove_consolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta]) -> None:
        """
        Removes the specified consolidator for the symbol
        
        :param symbol: The symbol the consolidator is receiving data from
        :param consolidator: The consolidator instance to be removed
        """
        ...

    @overload
    def remove_consolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], py_consolidator: typing.Any) -> None:
        """
        Removes the specified python consolidator for the symbol
        
        :param symbol: The symbol the consolidator is receiving data from
        :param py_consolidator: The python consolidator instance to be removed
        """
        ...

    def scan_past_consolidators(self, new_utc_time: typing.Union[datetime.datetime, datetime.date], algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Will trigger past consolidator scans
        
        :param new_utc_time: The new utc time
        :param algorithm: The algorithm instance
        """
        ...

    def set_data_manager(self, subscription_manager: QuantConnect.Interfaces.IAlgorithmSubscriptionManager) -> None:
        """Sets the Subscription Manager"""
        ...


class ISubscriptionEnumeratorFactory(metaclass=abc.ABCMeta):
    """Create an IEnumerator{BaseData}"""

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class FuncRiskFreeRateInterestRateModel(System.Object, QuantConnect.Data.IRiskFreeInterestRateModel):
    """Constant risk free rate interest rate model"""

    @overload
    def __init__(self, getInterestRateFunc: typing.Callable[[datetime.datetime], float]) -> None:
        """Create class instance of interest rate provider"""
        ...

    @overload
    def __init__(self, getInterestRateFunc: typing.Any) -> None:
        """Create class instance of interest rate provider with given PyObject"""
        ...

    def get_interest_rate(self, date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get interest rate by a given date
        
        :param date: The date
        :returns: Interest rate on the given date.
        """
        ...


class SliceExtensions(System.Object):
    """Provides extension methods to slices and slice enumerables"""

    @staticmethod
    @overload
    def get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], type: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str] = None) -> System.Collections.Generic.IEnumerable[typing.Any]:
        """
        Gets the data dictionaries or points of the requested type in each slice
        
        :param slices: The enumerable of slice
        :param type: Data type of the data that will be fetched
        :param symbol: The symbol to retrieve
        :returns: An enumerable of data dictionary or data point of the requested type.
        """
        ...

    @staticmethod
    @overload
    def get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.TradeBar]:
        """
        Gets an enumerable of TradeBar for the given symbol. This method does not verify
        that the specified symbol points to a TradeBar
        
        :param slices: The enumerable of slice
        :param symbol: The symbol to retrieve
        :returns: An enumerable of TradeBar for the matching symbol, of no TradeBar found for symbol, empty enumerable is returned.
        """
        ...

    @staticmethod
    @overload
    def get(data_dictionaries: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_SliceExtensions_Get_T]], symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect_Data_SliceExtensions_Get_T]:
        """
        Gets an enumerable of T for the given symbol. This method does not vify
        that the specified symbol points to a T
        
        :param data_dictionaries: The data dictionary enumerable to access
        :param symbol: The symbol to retrieve
        :returns: An enumerable of T for the matching symbol, if no T is found for symbol, empty enumerable is returned.
        """
        ...

    @staticmethod
    @overload
    def get(data_dictionaries: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_SliceExtensions_Get_T]], symbol: typing.Union[QuantConnect.Symbol, str], field: str) -> System.Collections.Generic.IEnumerable[float]:
        """
        Gets an enumerable of decimals by accessing the specified field on data for the symbol
        
        :param data_dictionaries: An enumerable of data dictionaries
        :param symbol: The symbol to retrieve
        :param field: The field to access
        :returns: An enumerable of decimals.
        """
        ...

    @staticmethod
    @overload
    def get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_SliceExtensions_Get_T]]:
        """
        Gets the data dictionaries of the requested type in each slice
        
        :param slices: The enumerable of slice
        :returns: An enumerable of data dictionary of the requested type.
        """
        ...

    @staticmethod
    @overload
    def get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect_Data_SliceExtensions_Get_T]:
        """
        Gets an enumerable of T by accessing the slices for the requested symbol
        
        :param slices: The enumerable of slice
        :param symbol: The symbol to retrieve
        :returns: An enumerable of T by accessing each slice for the requested symbol.
        """
        ...

    @staticmethod
    @overload
    def get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], symbol: typing.Union[QuantConnect.Symbol, str], field: typing.Callable[[QuantConnect.Data.BaseData], float]) -> System.Collections.Generic.IEnumerable[float]:
        """
        Gets an enumerable of decimal by accessing the slice for the symbol and then retrieving the specified
        field on each piece of data
        
        :param slices: The enumerable of slice
        :param symbol: The symbol to retrieve
        :param field: The field selector used to access the dats
        :returns: An enumerable of decimal.
        """
        ...

    @staticmethod
    def get_universe_data(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.UniverseSelection.BaseDataCollection]]:
        """
        Gets the data dictionaries or points of the requested type in each slice
        
        :param slices: The enumerable of slice
        :returns: An enumerable of data dictionary or data point of the requested type.
        """
        ...

    @staticmethod
    def push_through(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], handler: typing.Callable[[QuantConnect.Data.BaseData], None], data_type: typing.Type = None) -> None:
        """
        Loops through the specified slices and pushes the data into the consolidators. This can be used to
        easily warm up indicators from a history call that returns slice objects.
        
        :param slices: The data to send into the consolidators, likely result of a history request
        :param handler: Delegate handles each data piece from the slice
        :param data_type: Defines the type of the data that should be pushed
        """
        ...

    @staticmethod
    @overload
    def push_through_consolidators(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], consolidators_by_symbol: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Data.Consolidators.IDataConsolidator]) -> None:
        """
        Loops through the specified slices and pushes the data into the consolidators. This can be used to
        easily warm up indicators from a history call that returns slice objects.
        
        :param slices: The data to send into the consolidators, likely result of a history request
        :param consolidators_by_symbol: Dictionary of consolidators keyed by symbol
        """
        ...

    @staticmethod
    @overload
    def push_through_consolidators(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], consolidators_provider: typing.Callable[[QuantConnect.Symbol], QuantConnect.Data.Consolidators.IDataConsolidator]) -> None:
        """
        Loops through the specified slices and pushes the data into the consolidators. This can be used to
        easily warm up indicators from a history call that returns slice objects.
        
        :param slices: The data to send into the consolidators, likely result of a history request
        :param consolidators_provider: Delegate that fetches the consolidators by a symbol
        """
        ...

    @staticmethod
    def ticks(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.Ticks]:
        """
        Selects into the slice and returns the Ticks that have data in order
        
        :param slices: The enumerable of slice
        :returns: An enumerable of Ticks.
        """
        ...

    @staticmethod
    def to_double_array(decimals: System.Collections.Generic.IEnumerable[float]) -> typing.List[float]:
        """
        Converts the specified enumerable of decimals into a double array
        
        :param decimals: The enumerable of decimal
        :returns: Double array representing the enumerable of decimal.
        """
        ...

    @staticmethod
    def trade_bars(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.TradeBars]:
        """
        Selects into the slice and returns the TradeBars that have data in order
        
        :param slices: The enumerable of slice
        :returns: An enumerable of TradeBars.
        """
        ...

    @staticmethod
    @overload
    def try_get(slice: QuantConnect.Data.Slice, symbol: typing.Union[QuantConnect.Symbol, str], data: typing.Optional[QuantConnect_Data_SliceExtensions_TryGet_T]) -> typing.Union[bool, QuantConnect_Data_SliceExtensions_TryGet_T]:
        """
        Tries to get the data for the specified symbol and type
        
        :param slice: The slice
        :param symbol: The symbol data is sought for
        :param data: The found data
        :returns: True if data was found for the specified type and symbol.
        """
        ...

    @staticmethod
    @overload
    def try_get(slice: QuantConnect.Data.Slice, type: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], data: typing.Optional[typing.Any]) -> typing.Union[bool, typing.Any]:
        """
        Tries to get the data for the specified symbol and type
        
        :param slice: The slice
        :param type: The type of data we seek
        :param symbol: The symbol data is sought for
        :param data: The found data
        :returns: True if data was found for the specified type and symbol.
        """
        ...


class ConstantDividendYieldModel(System.Object, QuantConnect.Data.IDividendYieldModel):
    """Constant dividend yield model"""

    def __init__(self, dividendYield: float) -> None:
        """Instantiates a ConstantDividendYieldModel with the specified dividend yield"""
        ...

    @overload
    def get_dividend_yield(self, date: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get dividend yield by a given date of a given symbol
        
        :param date: The date
        :returns: Dividend yield on the given date of the given symbol.
        """
        ...

    @overload
    def get_dividend_yield(self, date: typing.Union[datetime.datetime, datetime.date], security_price: float) -> float:
        """
        Get dividend yield at given date and security price
        
        :param date: The date
        :param security_price: The security price at the given date
        :returns: Dividend yield on the given date of the given symbol.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Data__EventContainer_Callable, QuantConnect_Data__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Data__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Data__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Data__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


