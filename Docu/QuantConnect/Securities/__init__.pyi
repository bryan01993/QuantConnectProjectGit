from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.Fundamental
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Indicators
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Slippage
import QuantConnect.Python
import QuantConnect.Securities
import QuantConnect.Securities.CurrencyConversion
import QuantConnect.Securities.Interfaces
import QuantConnect.Securities.Option
import QuantConnect.Securities.Positions
import QuantConnect.Securities.Volatility
import System
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Collections.Specialized

QuantConnect_Securities_MarketHoursDatabase = typing.Any
QuantConnect_Securities_MarketHoursDatabase_Entry = typing.Any
QuantConnect_Securities_SecurityDatabaseKey = typing.Any
DynamicObject = typing.Any
IDynamicMetaObjectProvider = typing.Any
PyObject = typing.Any
QuantConnect_Securities_SymbolPropertiesDatabase = typing.Any
QuantConnect_Securities_OptionFilterUniverse = typing.Any
QuantConnect_Securities_FutureFilterUniverse = typing.Any

QuantConnect_Securities_IDerivativeSecurityFilterUniverse_T = typing.TypeVar("QuantConnect_Securities_IDerivativeSecurityFilterUniverse_T")
QuantConnect_Securities_SecurityCache_GetData_T = typing.TypeVar("QuantConnect_Securities_SecurityCache_GetData_T")
QuantConnect_Securities_SecurityCache_GetAll_T = typing.TypeVar("QuantConnect_Securities_SecurityCache_GetAll_T")
QuantConnect_Securities_BaseSecurityDatabase_T = typing.TypeVar("QuantConnect_Securities_BaseSecurityDatabase_T")
QuantConnect_Securities_BaseSecurityDatabase_TEntry = typing.TypeVar("QuantConnect_Securities_BaseSecurityDatabase_TEntry")
QuantConnect_Securities_FuncSecurityDerivativeFilter_T = typing.TypeVar("QuantConnect_Securities_FuncSecurityDerivativeFilter_T")
QuantConnect_Securities_ContractSecurityFilterUniverse_TData = typing.TypeVar("QuantConnect_Securities_ContractSecurityFilterUniverse_TData")
QuantConnect_Securities_ContractSecurityFilterUniverse_T = typing.TypeVar("QuantConnect_Securities_ContractSecurityFilterUniverse_T")
QuantConnect_Securities_Security_Get_T = typing.TypeVar("QuantConnect_Securities_Security_Get_T")
QuantConnect_Securities_Security_TryGet_T = typing.TypeVar("QuantConnect_Securities_Security_TryGet_T")
QuantConnect_Securities_Security_Remove_T = typing.TypeVar("QuantConnect_Securities_Security_Remove_T")
QuantConnect_Securities_IDerivativeSecurityFilter_T = typing.TypeVar("QuantConnect_Securities_IDerivativeSecurityFilter_T")
QuantConnect_Securities_DynamicSecurityData_Get_T = typing.TypeVar("QuantConnect_Securities_DynamicSecurityData_Get_T")
QuantConnect_Securities_DynamicSecurityData_GetAll_T = typing.TypeVar("QuantConnect_Securities_DynamicSecurityData_GetAll_T")
QuantConnect_Securities__EventContainer_Callable = typing.TypeVar("QuantConnect_Securities__EventContainer_Callable")
QuantConnect_Securities__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Securities__EventContainer_ReturnType")


class Cash(System.Object):
    """Represents a holding of a currency in cash."""

    @property
    def updated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """
        Event fired when this instance is updated
        AddAmount, SetAmount, Update
        """
        ...

    @property
    def currency_conversion_updated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event fired when this instance's CurrencyConversion is set/updated"""
        ...

    @property
    def security_symbols(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the symbols of the securities required to provide conversion rates.
        If this cash represents the account currency, then an empty enumerable is returned.
        """
        ...

    @property
    def currency_conversion(self) -> QuantConnect.Securities.CurrencyConversion.ICurrencyConversion:
        """Gets the object that calculates the conversion rate to account currency"""
        ...

    @property
    def symbol(self) -> str:
        """Gets the symbol used to represent this cash"""
        ...

    @property
    def amount(self) -> float:
        """Gets or sets the amount of cash held"""
        ...

    @property
    def conversion_rate(self) -> float:
        """Gets the conversion rate into account currency"""
        ...

    @property
    def currency_symbol(self) -> str:
        """The symbol of the currency, such as $"""
        ...

    @property
    def value_in_account_currency(self) -> float:
        """Gets the value of this cash in the account currency"""
        ...

    def __init__(self, symbol: str, amount: float, conversionRate: float) -> None:
        """
        Initializes a new instance of the Cash class
        
        :param symbol: The symbol used to represent this cash
        :param amount: The amount of this currency held
        :param conversionRate: The initial conversion rate of this currency into the CashBook.AccountCurrency
        """
        ...

    def add_amount(self, amount: float) -> float:
        """
        Adds the specified amount of currency to this Cash instance and returns the new total.
        This operation is thread-safe
        
        :param amount: The amount of currency to be added
        :returns: The amount of currency directly after the addition.
        """
        ...

    def ensure_currency_data_feed(self, securities: QuantConnect.Securities.SecurityManager, subscriptions: QuantConnect.Data.SubscriptionManager, market_map: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, security_service: QuantConnect.Interfaces.ISecurityService, account_currency: str, default_resolution: QuantConnect.Resolution = ...) -> System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Ensures that we have a data feed to convert this currency into the base currency.
        This will add a SubscriptionDataConfig and create a Security at the lowest resolution if one is not found.
        
        :param securities: The security manager
        :param subscriptions: The subscription manager used for searching and adding subscriptions
        :param market_map: The market map that decides which market the new security should be in
        :param changes: Will be used to consume SecurityChanges.AddedSecurities
        :param security_service: Will be used to create required new Security
        :param account_currency: The account currency
        :param default_resolution: The default resolution to use for the internal subscriptions
        :returns: Returns the added SubscriptionDataConfig, otherwise null.
        """
        ...

    def set_amount(self, amount: float) -> None:
        """
        Sets the Quantity to the specified amount
        
        :param amount: The amount to set the quantity to
        """
        ...

    @overload
    def to_string(self) -> str:
        """
        Returns a string that represents the current Cash.
        
        :returns: A string that represents the current Cash.
        """
        ...

    @overload
    def to_string(self, account_currency: str) -> str:
        """
        Returns a string that represents the current Cash.
        
        :returns: A string that represents the current Cash.
        """
        ...

    def update(self) -> None:
        """Marks this cash object's conversion rate as being potentially outdated"""
        ...


class SymbolProperties(System.Object):
    """Represents common properties for a specific security, uniquely identified by market, symbol and security type"""

    @property
    def description(self) -> str:
        """The description of the security"""
        ...

    @property
    def quote_currency(self) -> str:
        """The quote currency of the security"""
        ...

    @property
    def contract_multiplier(self) -> float:
        """The contract multiplier for the security"""
        ...

    @property
    def minimum_price_variation(self) -> float:
        """The minimum price variation (tick size) for the security"""
        ...

    @property
    def lot_size(self) -> float:
        """The lot size (lot size of the order) for the security"""
        ...

    @property
    def market_ticker(self) -> str:
        """The market ticker"""
        ...

    @property
    def minimum_order_size(self) -> typing.Optional[float]:
        """
        The minimum order size allowed
        For crypto/forex pairs it's expected to be expressed in base or quote currency
        i.e For BTC/USD the minimum order size allowed with Coinbase is 0.0001 BTC
        while on Binance the minimum order size allowed is 10 USD
        """
        ...

    @property
    def price_magnifier(self) -> float:
        """
        Allows normalizing live asset prices to US Dollars for Lean consumption. In some exchanges,
        for some securities, data is expressed in cents like for example for corn futures ('ZC').
        """
        ...

    @property
    def strike_multiplier(self) -> float:
        """
        Scale factor for option's strike price. For some options, such as NQX, the strike price
        is based on a fraction of the underlying, thus this paramater scales the strike price so
        that it can be used in comparation with the underlying such as
        in OptionFilterUniverse.Strikes(int, int)
        """
        ...

    @overload
    def __init__(self, properties: QuantConnect.Securities.SymbolProperties) -> None:
        """
        Creates an instance of the SymbolProperties class
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, description: str, quoteCurrency: str, contractMultiplier: float, minimumPriceVariation: float, lotSize: float, marketTicker: str, minimumOrderSize: typing.Optional[float] = None, priceMagnifier: float = 1, strikeMultiplier: float = 1) -> None:
        """Creates an instance of the SymbolProperties class"""
        ...

    @staticmethod
    def get_default(quote_currency: str) -> QuantConnect.Securities.SymbolProperties:
        """
        Gets a default instance of the SymbolProperties class for the specified
        
        :param quote_currency: The quote currency of the symbol
        :returns: A default instance of theSymbolProperties class.
        """
        ...

    def to_string(self) -> str:
        """The string representation of these symbol properties"""
        ...


class SecurityCache(System.Object):
    """Base class caching spot for security data and any other temporary properties."""

    @property
    def price(self) -> float:
        """Gets the most recent price submitted to this cache"""
        ...

    @property
    def open(self) -> float:
        """Gets the most recent open submitted to this cache"""
        ...

    @property
    def high(self) -> float:
        """Gets the most recent high submitted to this cache"""
        ...

    @property
    def low(self) -> float:
        """Gets the most recent low submitted to this cache"""
        ...

    @property
    def close(self) -> float:
        """Gets the most recent close submitted to this cache"""
        ...

    @property
    def bid_price(self) -> float:
        """Gets the most recent bid submitted to this cache"""
        ...

    @property
    def ask_price(self) -> float:
        """Gets the most recent ask submitted to this cache"""
        ...

    @property
    def bid_size(self) -> float:
        """Gets the most recent bid size submitted to this cache"""
        ...

    @property
    def ask_size(self) -> float:
        """Gets the most recent ask size submitted to this cache"""
        ...

    @property
    def volume(self) -> float:
        """Gets the most recent volume submitted to this cache"""
        ...

    @property
    def open_interest(self) -> int:
        """Gets the most recent open interest submitted to this cache"""
        ...

    @property
    def properties(self) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Collection of keyed custom properties"""
        ...

    def add_data(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Add a new market data point to the local security cache for the current market price.
        Rules:
            Don't cache fill forward data.
            Always return the last observation.
            If two consecutive data has the same time stamp and one is Quotebars and the other Tradebar, prioritize the Quotebar.
        """
        ...

    def add_data_list(self, data: System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData], data_type: typing.Type, contains_fill_forward_data: typing.Optional[bool] = None) -> None:
        """Add a list of market data points to the local security cache for the current market price."""
        ...

    def get_all(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Securities_SecurityCache_GetAll_T]:
        """
        Gets all data points of the specified type from the most recent time step
        that produced data for that type
        """
        ...

    @overload
    def get_data(self) -> QuantConnect.Data.BaseData:
        """
        Get last data packet received for this security if any else null
        
        :returns: BaseData type of the security.
        """
        ...

    @overload
    def get_data(self) -> QuantConnect_Securities_SecurityCache_GetData_T:
        """
        Get last data packet received for this security of the specified type
        
        :returns: The last data packet, null if none received of type.
        """
        ...

    def has_data(self, type: typing.Type) -> bool:
        """Gets whether or not this dynamic data instance has data stored for the specified type"""
        ...

    def process_data_point(self, data: QuantConnect.Data.BaseData, cache_by_type: bool) -> None:
        """
        Will consume the given data point updating the cache state and it's properties
        
        This method is protected.
        
        :param data: The data point to process
        :param cache_by_type: True if this data point should be cached by type
        """
        ...

    def reset(self) -> None:
        """Reset cache storage and free memory"""
        ...

    @staticmethod
    def share_type_cache_instance(source_to_share: QuantConnect.Securities.SecurityCache, target_to_modify: QuantConnect.Securities.SecurityCache) -> None:
        """
        Helper method that modifies the target security cache instance to use the
        type cache of the source
        
        :param source_to_share: The source cache to use
        :param target_to_modify: The target security cache that will be modified
        """
        ...

    def store_data(self, data: System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData], data_type: typing.Type) -> None:
        """
        Stores the specified data list in the cache WITHOUT updating any of the cache properties, such as Price
        
        :param data: The collection of data to store in this cache
        :param data_type: The data type
        """
        ...

    def try_get_value(self, type: typing.Type, data: typing.Optional[System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]]) -> typing.Union[bool, System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]]:
        """Gets whether or not this dynamic data instance has data stored for the specified type"""
        ...


class MarketHoursState(Enum):
    """Specifies the open/close state for a MarketHoursSegment"""

    CLOSED = 0
    """The market is not open (0)"""

    PRE_MARKET = 1
    """The market is open, but before normal trading hours (1)"""

    MARKET = 2
    """The market is open and within normal trading hours (2)"""

    POST_MARKET = 3
    """The market is open, but after normal trading hours (3)"""


class MarketHoursSegment(System.Object):
    """Represents the state of an exchange during a specified time range"""

    @property
    def start(self) -> datetime.timedelta:
        """Gets the start time for this segment"""
        ...

    @property
    def end(self) -> datetime.timedelta:
        """Gets the end time for this segment"""
        ...

    @property
    def state(self) -> QuantConnect.Securities.MarketHoursState:
        """Gets the market hours state for this segment"""
        ...

    def __init__(self, state: QuantConnect.Securities.MarketHoursState, start: datetime.timedelta, end: datetime.timedelta) -> None:
        """
        Initializes a new instance of the MarketHoursSegment class
        
        :param state: The state of the market during the specified times
        :param start: The start time of the segment
        :param end: The end time of the segment
        """
        ...

    @staticmethod
    def closed_all_day() -> QuantConnect.Securities.MarketHoursSegment:
        """Gets a new market hours segment representing being open all day"""
        ...

    def contains(self, time: datetime.timedelta) -> bool:
        """
        Determines whether or not the specified time is contained within this segment
        
        :param time: The time to check
        :returns: True if this segment contains the specified time, false otherwise.
        """
        ...

    @staticmethod
    def get_market_hours_segments(extended_market_open: datetime.timedelta, market_open: datetime.timedelta, market_close: datetime.timedelta, extended_market_close: datetime.timedelta) -> typing.List[QuantConnect.Securities.MarketHoursSegment]:
        """
        Creates the market hours segments for the specified market open/close times
        
        :param extended_market_open: The extended market open time. If no pre market, set to market open
        :param market_open: The regular market open time
        :param market_close: The regular market close time
        :param extended_market_close: The extended market close time. If no post market, set to market close
        :returns: An array of MarketHoursSegment representing the specified market open/close times.
        """
        ...

    @staticmethod
    def open_all_day() -> QuantConnect.Securities.MarketHoursSegment:
        """Gets a new market hours segment representing being open all day"""
        ...

    def overlaps(self, start: datetime.timedelta, end: datetime.timedelta) -> bool:
        """
        Determines whether or not the specified time range overlaps with this segment
        
        :param start: The start of the range
        :param end: The end of the range
        :returns: True if the specified range overlaps this time segment, false otherwise.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class LocalMarketHours(System.Object):
    """Represents the market hours under normal conditions for an exchange and a specific day of the week in terms of local time"""

    @property
    def is_closed_all_day(self) -> bool:
        """Gets whether or not this exchange is closed all day"""
        ...

    @property
    def is_open_all_day(self) -> bool:
        """Gets whether or not this exchange is closed all day"""
        ...

    @property
    def day_of_week(self) -> System.DayOfWeek:
        """Gets the day of week these hours apply to"""
        ...

    @property
    def market_duration(self) -> datetime.timedelta:
        """
        Gets the tradable time during the market day.
        For a normal US equity trading day this is 6.5 hours.
        This does NOT account for extended market hours and only
        considers MarketHoursState.Market
        """
        ...

    @property
    def segments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[QuantConnect.Securities.MarketHoursSegment]:
        """Gets the individual market hours segments that define the hours of operation for this day"""
        ...

    @overload
    def __init__(self, day: System.DayOfWeek, *segments: QuantConnect.Securities.MarketHoursSegment) -> None:
        """
        Initializes a new instance of the LocalMarketHours class
        
        :param day: The day of the week these hours are applicable
        :param segments: The open/close segments defining the market hours for one day
        """
        ...

    @overload
    def __init__(self, day: System.DayOfWeek, segments: System.Collections.Generic.IEnumerable[QuantConnect.Securities.MarketHoursSegment]) -> None:
        """
        Initializes a new instance of the LocalMarketHours class
        
        :param day: The day of the week these hours are applicable
        :param segments: The open/close segments defining the market hours for one day
        """
        ...

    @overload
    def __init__(self, day: System.DayOfWeek, extendedMarketOpen: datetime.timedelta, marketOpen: datetime.timedelta, marketClose: datetime.timedelta, extendedMarketClose: datetime.timedelta) -> None:
        """
        Initializes a new instance of the LocalMarketHours class from the specified open/close times
        
        :param day: The day of week these hours apply to
        :param extendedMarketOpen: The extended market open time
        :param marketOpen: The regular market open time, must be greater than or equal to the extended market open time
        :param marketClose: The regular market close time, must be greater than the regular market open time
        :param extendedMarketClose: The extended market close time, must be greater than or equal to the regular market close time
        """
        ...

    @overload
    def __init__(self, day: System.DayOfWeek, marketOpen: datetime.timedelta, marketClose: datetime.timedelta) -> None:
        """
        Initializes a new instance of the LocalMarketHours class from the specified open/close times
        using the market open as the extended market open and the market close as the extended market close, effectively
        removing any 'extended' session from these exchange hours
        
        :param day: The day of week these hours apply to
        :param marketOpen: The regular market open time
        :param marketClose: The regular market close time, must be greater than the regular market open time
        """
        ...

    @staticmethod
    def closed_all_day(day_of_week: System.DayOfWeek) -> QuantConnect.Securities.LocalMarketHours:
        """
        Gets a LocalMarketHours instance that is always closed
        
        :param day_of_week: The day of week
        :returns: A LocalMarketHours instance that is always closed.
        """
        ...

    @overload
    def get_market_close(self, time: datetime.timedelta, extended_market_hours: bool, next_day_segment_start: typing.Optional[datetime.timedelta] = None) -> typing.Optional[datetime.timedelta]:
        """
        Gets the market closing time of day
        
        :param time: The reference time, the close returned will be the first close after the specified time if there are multiple market open segments
        :param extended_market_hours: True to include extended market hours, false for regular market hours
        :param next_day_segment_start: Next day first segment start. This is used when the potential next market close is the last segment of the day so we need to check that segment is not continued on next day first segment. If null, it means there are no segments on the next day
        :returns: The market's closing time of day.
        """
        ...

    @overload
    def get_market_close(self, time: datetime.timedelta, extended_market_hours: bool, last_close: bool, next_day_segment_start: typing.Optional[datetime.timedelta] = None) -> typing.Optional[datetime.timedelta]:
        """
        Gets the market closing time of day
        
        :param time: The reference time, the close returned will be the first close after the specified time if there are multiple market open segments
        :param extended_market_hours: True to include extended market hours, false for regular market hours
        :param last_close: True if the last available close of the date should be returned, else the first will be used
        :param next_day_segment_start: Next day first segment start. This is used when the potential next market close is the last segment of the day so we need to check that segment is not continued on next day first segment. If null, it means there are no segments on the next day
        :returns: The market's closing time of day.
        """
        ...

    def get_market_open(self, time: datetime.timedelta, extended_market_hours: bool, previous_day_last_segment: typing.Optional[datetime.timedelta] = None) -> typing.Optional[datetime.timedelta]:
        """
        Gets the market opening time of day
        
        :param time: The reference time, the open returned will be the first open after the specified time if there are multiple market open segments
        :param extended_market_hours: True to include extended market hours, false for regular market hours
        :param previous_day_last_segment: The previous days last segment. This is used when the potential next market open is the first segment of the day so we need to check that segment is not part of previous day last segment. If null, it means there were no segments on the last day
        :returns: The market's opening time of day.
        """
        ...

    @staticmethod
    def is_continuous_market_open(previous_segment_end: typing.Optional[datetime.timedelta], next_segment_start: typing.Optional[datetime.timedelta], prev_segment_is_from_prev_day: bool = True) -> bool:
        """
        Check the given segment is not part of the current previous segment
        
        :param previous_segment_end: Previous segment end time before the current segment
        :param next_segment_start: The next segment start time
        :param prev_segment_is_from_prev_day: Indicated whether the previous segment is from the previous day or not (then it is from the same day as the next segment). Defaults to true
        :returns: True if indeed the given segment is part of the last segment. False otherwise.
        """
        ...

    @overload
    def is_open(self, time: datetime.timedelta, extended_market_hours: bool) -> bool:
        """
        Determines if the exchange is open at the specified time
        
        :param time: The time of day to check
        :param extended_market_hours: True to check exended market hours, false to check regular market hours
        :returns: True if the exchange is considered open, false otherwise.
        """
        ...

    @overload
    def is_open(self, start: datetime.timedelta, end: datetime.timedelta, extended_market_hours: bool) -> bool:
        """
        Determines if the exchange is open during the specified interval
        
        :param start: The start time of the interval
        :param end: The end time of the interval
        :param extended_market_hours: True to check exended market hours, false to check regular market hours
        :returns: True if the exchange is considered open, false otherwise.
        """
        ...

    @staticmethod
    def open_all_day(day_of_week: System.DayOfWeek) -> QuantConnect.Securities.LocalMarketHours:
        """
        Gets a LocalMarketHours instance that is always open
        
        :param day_of_week: The day of week
        :returns: A LocalMarketHours instance that is always open.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class SecurityExchangeHours(System.Object):
    """
    Represents the schedule of a security exchange. This includes daily regular and extended market hours
    as well as holidays, early closes and late opens.
    """

    @property
    def time_zone(self) -> typing.Any:
        """Gets the time zone this exchange resides in"""
        ...

    @property
    def holidays(self) -> System.Collections.Generic.HashSet[datetime.datetime]:
        """Gets the holidays for the exchange"""
        ...

    @property
    def bank_holidays(self) -> System.Collections.Generic.HashSet[datetime.datetime]:
        """Gets the bank holidays for the exchange"""
        ...

    @property
    def market_hours(self) -> System.Collections.Generic.IReadOnlyDictionary[System.DayOfWeek, QuantConnect.Securities.LocalMarketHours]:
        """Gets the market hours for this exchange"""
        ...

    @property
    def early_closes(self) -> System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta]:
        """Gets the early closes for this exchange"""
        ...

    @property
    def late_opens(self) -> System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta]:
        """Gets the late opens for this exchange"""
        ...

    @property
    def regular_market_duration(self) -> datetime.timedelta:
        """
        Gets the most common tradable time during the market week.
        For a normal US equity trading day this is 6.5 hours.
        This does NOT account for extended market hours and only
        considers MarketHoursState.Market
        """
        ...

    @property
    def is_market_always_open(self) -> bool:
        """Checks whether the market is always open or not"""
        ...

    def __init__(self, timeZone: typing.Any, holidayDates: System.Collections.Generic.IEnumerable[datetime.datetime], marketHoursForEachDayOfWeek: System.Collections.Generic.Dictionary[System.DayOfWeek, QuantConnect.Securities.LocalMarketHours], earlyCloses: System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta], lateOpens: System.Collections.Generic.IReadOnlyDictionary[datetime.datetime, datetime.timedelta], bankHolidayDates: System.Collections.Generic.IEnumerable[datetime.datetime] = None) -> None:
        """
        Initializes a new instance of the SecurityExchangeHours class
        
        :param timeZone: The time zone the dates and hours are represented in
        :param holidayDates: The dates this exchange is closed for holiday
        :param marketHoursForEachDayOfWeek: The exchange's schedule for each day of the week
        :param earlyCloses: The dates this exchange has an early close
        :param lateOpens: The dates this exchange has a late open
        """
        ...

    @staticmethod
    def always_open(time_zone: typing.Any) -> QuantConnect.Securities.SecurityExchangeHours:
        """Gets a SecurityExchangeHours instance that is always open"""
        ...

    def get_first_daily_market_open(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> datetime.datetime:
        """
        Gets the local date time corresponding to the first market open to the specified previous date
        
        :param local_date_time: The time to begin searching for the last market open (non-inclusive)
        :param extended_market_hours: True to include extended market hours in the search
        :returns: The previous market opening date time to the specified local date time.
        """
        ...

    def get_last_daily_market_close(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> datetime.datetime:
        """
        Gets the local date time corresponding to the last market close following the specified date
        
        :param local_date_time: The time to begin searching for market close (non-inclusive)
        :param extended_market_hours: True to include extended market hours in the search
        :returns: The next market closing date time following the specified local date time.
        """
        ...

    def get_market_hours(self, local_date_time: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.LocalMarketHours:
        """
        Helper to access the market hours field based on the day of week
        
        :param local_date_time: The local date time to retrieve market hours for
        """
        ...

    @overload
    def get_next_market_close(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> datetime.datetime:
        """
        Gets the local date time corresponding to the next market close following the specified time
        
        :param local_date_time: The time to begin searching for market close (non-inclusive)
        :param extended_market_hours: True to include extended market hours in the search
        :returns: The next market closing date time following the specified local date time.
        """
        ...

    @overload
    def get_next_market_close(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool, last_close: bool) -> datetime.datetime:
        """
        Gets the local date time corresponding to the next market close following the specified time
        
        :param local_date_time: The time to begin searching for market close (non-inclusive)
        :param extended_market_hours: True to include extended market hours in the search
        :param last_close: True if the last available close of the date should be returned, else the first will be used
        :returns: The next market closing date time following the specified local date time.
        """
        ...

    def get_next_market_open(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> datetime.datetime:
        """
        Gets the local date time corresponding to the next market open following the specified time
        
        :param local_date_time: The time to begin searching for market open (non-inclusive)
        :param extended_market_hours: True to include extended market hours in the search
        :returns: The next market opening date time following the specified local date time.
        """
        ...

    def get_next_trading_day(self, date: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Gets the next trading day
        
        :param date: The date to start searching at
        :returns: The next trading day.
        """
        ...

    @overload
    def get_previous_market_open(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> datetime.datetime:
        """
        Gets the local date time corresponding to the previous market open to the specified time
        
        :param local_date_time: The time to begin searching for the last market open (non-inclusive)
        :param extended_market_hours: True to include extended market hours in the search
        :returns: The previous market opening date time to the specified local date time.
        """
        ...

    @overload
    def get_previous_market_open(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool, first_open: bool) -> datetime.datetime:
        """
        Gets the local date time corresponding to the previous market open to the specified time
        
        :param local_date_time: The time to begin searching for the last market open (non-inclusive)
        :param extended_market_hours: True to include extended market hours in the search
        :returns: The previous market opening date time to the specified local date time.
        """
        ...

    def get_previous_trading_day(self, local_date: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Gets the previous trading day
        
        :param local_date: The date to start searching at in this exchange's time zones
        :returns: The previous trading day.
        """
        ...

    def is_date_open(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool = False) -> bool:
        """
        Determines if the exchange will be open on the date specified by the local date time
        
        :param local_date_time: The date time to check if the day is open
        :param extended_market_hours: True to consider days with extended market hours only as open
        :returns: True if the exchange will be open on the specified date, false otherwise.
        """
        ...

    @overload
    def is_open(self, local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> bool:
        """
        Determines if the exchange is open at the specified local date time.
        
        :param local_date_time: The time to check represented as a local time
        :param extended_market_hours: True to use the extended market hours, false for just regular market hours
        :returns: True if the exchange is considered open at the specified time, false otherwise.
        """
        ...

    @overload
    def is_open(self, start_local_date_time: typing.Union[datetime.datetime, datetime.date], end_local_date_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> bool:
        """
        Determines if the exchange is open at any point in time over the specified interval.
        
        :param start_local_date_time: The start of the interval in local time
        :param end_local_date_time: The end of the interval in local time
        :param extended_market_hours: True to use the extended market hours, false for just regular market hours
        :returns: True if the exchange is considered open at the specified time, false otherwise.
        """
        ...


class SecurityExchange(System.Object):
    """Base exchange class providing information and helper tools for reading the current exchange situation"""

    @property
    def hours(self) -> QuantConnect.Securities.SecurityExchangeHours:
        """Gets the SecurityExchangeHours for this exchange"""
        ...

    @property
    def time_zone(self) -> typing.Any:
        """Gets the time zone for this exchange"""
        ...

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days per year for this security. By default the market is open 365 days per year."""
        ...

    @property
    def local_time(self) -> datetime.datetime:
        """Time from the most recent data"""
        ...

    @property
    def exchange_open(self) -> bool:
        """Boolean property for quickly testing if the exchange is open."""
        ...

    @property
    def closing_soon(self) -> bool:
        """Boolean property for quickly testing if the exchange is 10 minutes away from closing."""
        ...

    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the SecurityExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...

    def date_is_open(self, date_to_check: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool = False) -> bool:
        """
        Check if the *date* is open.
        
        :param date_to_check: Date to check
        :param extended_market_hours: True to consider days with extended market hours only as open
        :returns: Return true if the exchange is open for this date.
        """
        ...

    def date_time_is_open(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Check if this DateTime is open.
        
        :param date_time: DateTime to check
        :returns: Boolean true if the market is open.
        """
        ...

    def is_closing_soon(self, minutes_to_close: int) -> bool:
        """
        Determines if the exchange is going to close in the next provided minutes
        
        :param minutes_to_close: Minutes to close to check
        :returns: Returns true if the exchange is going to close in the next provided minutes.
        """
        ...

    def is_open_during_bar(self, bar_start_time: typing.Union[datetime.datetime, datetime.date], bar_end_time: typing.Union[datetime.datetime, datetime.date], is_extended_market_hours: bool) -> bool:
        """Determines if the exchange was open at any time between start and stop"""
        ...

    def set_local_date_time_frontier_provider(self, time_provider: QuantConnect.LocalTimeKeeper) -> None:
        """
        Set the current datetime in terms of the exchange's local time zone
        
        :param time_provider: Most recent data tick
        """
        ...

    def set_market_hours(self, market_hours_segments: System.Collections.Generic.IEnumerable[QuantConnect.Securities.MarketHoursSegment], *days: System.DayOfWeek) -> None:
        """
        Sets the regular market hours for the specified days If no days are specified then
        all days will be updated.
        
        :param market_hours_segments: Specifies each segment of the market hours, such as premarket/market/postmark
        :param days: The days of the week to set these times for
        """
        ...


class IVolatilityModel(metaclass=abc.ABCMeta):
    """Represents a model that computes the volatility of a security"""

    @property
    @abc.abstractmethod
    def volatility(self) -> float:
        """Gets the volatility of the security as a percentage"""
        ...

    def get_history_requirements(self, security: QuantConnect.Securities.Security, utc_time: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Returns history requirements for the volatility model expressed in the form of history request
        
        :param security: The security of the request
        :param utc_time: The date/time of the request
        :returns: History request object list, or empty if no requirements.
        """
        ...

    def update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        """
        Updates this model using the new price information in
        the specified security instance
        
        :param security: The security to calculate volatility for
        :param data: The new data used to update the model
        """
        ...


class GetMinimumPriceVariationParameters(System.Object):
    """Defines the parameters for IPriceVariationModel.GetMinimumPriceVariation"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def reference_price(self) -> float:
        """Gets the reference price to be used for the calculation"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, referencePrice: float) -> None:
        """
        Initializes a new instance of the GetMinimumPriceVariationParameters class
        
        :param security: The security
        :param referencePrice: The reference price to be used for the calculation
        """
        ...


class IPriceVariationModel(metaclass=abc.ABCMeta):
    """Gets the minimum price variation of a given security"""

    def get_minimum_price_variation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        """
        Get the minimum price variation from a security
        
        :param parameters: An object containing the method parameters
        :returns: Decimal minimum price variation of a given security.
        """
        ...


class IRegisteredSecurityDataTypesProvider(metaclass=abc.ABCMeta):
    """Provides the set of base data types registered in the algorithm"""

    def register_type(self, type: typing.Type) -> bool:
        """
        Registers the specified type w/ the provider
        
        :returns: True if the type was previously not registered.
        """
        ...

    def try_get_type(self, name: str, type: typing.Optional[typing.Type]) -> typing.Union[bool, typing.Type]:
        """
        Determines if the specified type is registered or not and returns it
        
        :returns: True if the type was previously registered.
        """
        ...

    def unregister_type(self, type: typing.Type) -> bool:
        """
        Removes the registration for the specified type
        
        :returns: True if the type was previously registered.
        """
        ...


class DynamicSecurityData(IDynamicMetaObjectProvider):
    """
    Provides access to a security's data via it's type. This implementation supports dynamic access
    by type name.
    """

    def __init__(self, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cache: QuantConnect.Securities.SecurityCache) -> None:
        """
        Initializes a new instance of the DynamicSecurityData class
        
        :param registeredTypes: Provides all the registered data types for the algorithm
        :param cache: The security cache
        """
        ...

    def get(self, type: QuantConnect_Securities_DynamicSecurityData_Get_T) -> QuantConnect_Securities_DynamicSecurityData_Get_T:
        """
        Get the matching cached object in a python friendly accessor
        
        :param type: Type to search for
        :returns: Matching object.
        """
        ...

    def get_all(self, type: QuantConnect_Securities_DynamicSecurityData_GetAll_T) -> System.Collections.Generic.IReadOnlyList[QuantConnect_Securities_DynamicSecurityData_GetAll_T]:
        """
        Get all the matching types with a python friendly overload.
        
        :param type: Search type
        :returns: List of matching objects cached.
        """
        ...

    def get_meta_object(self, parameter: typing.Any) -> typing.Any:
        """
        Returns the System.Dynamic.DynamicMetaObject responsible for binding operations performed on this object.
        
        :param parameter: The expression tree representation of the runtime value.
        :returns: The System.Dynamic.DynamicMetaObject to bind this object.
        """
        ...

    def get_property(self, name: str) -> System.Object:
        """
        Gets the property's value with the specified name. This is a case-insensitve search.
        
        :param name: The property name to access
        :returns: object value of BaseData.
        """
        ...

    def has_data(self) -> bool:
        """Gets whether or not this dynamic data instance has data stored for the specified type"""
        ...

    def has_property(self, name: str) -> bool:
        """
        Gets whether or not this dynamic data instance has a property with the specified name.
        This is a case-insensitive search.
        
        :param name: The property name to check for
        :returns: True if the property exists, false otherwise.
        """
        ...

    def set_property(self, name: str, value: typing.Any) -> System.Object:
        """
        Sets the property with the specified name to the value. This is a case-insensitve search.
        
        DynamicSecurityData is a view of the SecurityCache. It is readonly, properties can not be set
        
        :param name: The property name to set
        :param value: The new property value
        :returns: Returns the input value back to the caller.
        """
        warnings.warn("DynamicSecurityData is a view of the SecurityCache. It is readonly, properties can not be set", DeprecationWarning)


class CashAmount:
    """Represents a cash amount which can be converted to account currency using a currency converter"""

    @property
    def amount(self) -> float:
        """The amount of cash"""
        ...

    @property
    def currency(self) -> str:
        """The currency in which the cash amount is denominated"""
        ...

    def __init__(self, amount: float, currency: str) -> None:
        """
        Initializes a new instance of the CashAmount class
        
        :param amount: The amount
        :param currency: The currency
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Used to compare two CashAmount instances.
        Useful to compare against the default instance
        
        :param obj: The other object to compare with
        :returns: True if Currency and Amount are equal.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Get Hash Code for this Object
        
        :returns: Integer Hash Code.
        """
        ...


class ICurrencyConverter(metaclass=abc.ABCMeta):
    """Provides the ability to convert cash amounts to the account currency"""

    @property
    @abc.abstractmethod
    def account_currency(self) -> str:
        """Gets account currency"""
        ...

    def convert_to_account_currency(self, cash_amount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        """
        Converts a cash amount to the account currency
        
        :param cash_amount: The CashAmount instance to convert
        :returns: A new CashAmount instance denominated in the account currency.
        """
        ...


class Security(DynamicObject, QuantConnect.Interfaces.ISecurityPrice):
    """A base vehicle properties class for providing a common interface to all assets in QuantConnect."""

    @property
    def shortable_provider(self) -> QuantConnect.Interfaces.IShortableProvider:
        """This securities IShortableProvider"""
        ...

    NULL_LEVERAGE: float = 0
    """A null security leverage value"""

    @property
    def subscriptions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]:
        """Gets all the subscriptions for this security"""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol for the asset."""
        ...

    @property
    def quote_currency(self) -> QuantConnect.Securities.Cash:
        """Gets the Cash object used for converting the quote currency to the account currency"""
        ...

    @property
    def symbol_properties(self) -> QuantConnect.Securities.SymbolProperties:
        """Gets the symbol properties for this security"""
        ...

    @property
    def type(self) -> QuantConnect.SecurityType:
        """Type of the security."""
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """
        Resolution of data requested for this security.
        
        This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'
        """
        warnings.warn("This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'", DeprecationWarning)

    @property
    def is_fill_data_forward(self) -> bool:
        """
        Indicates the data will use previous bars when there was no trading in this time period. This was a configurable datastream setting set in initialization.
        
        This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'
        """
        warnings.warn("This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'", DeprecationWarning)

    @property
    def is_extended_market_hours(self) -> bool:
        """
        Indicates the security will continue feeding data after the primary market hours have closed. This was a configurable setting set in initialization.
        
        This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'
        """
        warnings.warn("This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'", DeprecationWarning)

    @property
    def data_normalization_mode(self) -> QuantConnect.DataNormalizationMode:
        """
        Gets the data normalization mode used for this security
        
        This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'
        """
        warnings.warn("This property is obsolete. Use the 'SubscriptionDataConfig' exposed by 'SubscriptionManager'", DeprecationWarning)

    @property
    def subscription_data_config(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Gets the subscription configuration for this security
        
        This property returns only the first subscription. Use the 'Subscriptions' property for all of this security's subscriptions.
        """
        warnings.warn("This property returns only the first subscription. Use the 'Subscriptions' property for all of this security's subscriptions.", DeprecationWarning)

    @property
    def has_data(self) -> bool:
        """There has been at least one datapoint since our algorithm started running for us to determine price."""
        ...

    @property
    def is_tradable(self) -> bool:
        """Gets or sets whether or not this security should be considered tradable"""
        ...

    @property.setter
    def is_tradable(self, value: bool) -> None:
        ...

    @property
    def is_delisted(self) -> bool:
        """True if the security has been delisted from exchanges and is no longer tradable"""
        ...

    @property.setter
    def is_delisted(self, value: bool) -> None:
        ...

    @property
    def cache(self) -> QuantConnect.Securities.SecurityCache:
        """Data cache for the security to store previous price information."""
        ...

    @property.setter
    def cache(self, value: QuantConnect.Securities.SecurityCache) -> None:
        ...

    @property
    def holdings(self) -> QuantConnect.Securities.SecurityHolding:
        """Holdings class contains the portfolio, cash and processes order fills."""
        ...

    @property.setter
    def holdings(self, value: QuantConnect.Securities.SecurityHolding) -> None:
        ...

    @property
    def exchange(self) -> QuantConnect.Securities.SecurityExchange:
        """Exchange class contains the market opening hours, along with pre-post market hours."""
        ...

    @property.setter
    def exchange(self, value: QuantConnect.Securities.SecurityExchange) -> None:
        ...

    @property
    def fee_model(self) -> QuantConnect.Orders.Fees.IFeeModel:
        """Fee model used to compute order fees for this security"""
        ...

    @property.setter
    def fee_model(self, value: QuantConnect.Orders.Fees.IFeeModel) -> None:
        ...

    @property
    def fill_model(self) -> QuantConnect.Orders.Fills.IFillModel:
        """Fill model used to produce fill events for this security"""
        ...

    @property.setter
    def fill_model(self, value: QuantConnect.Orders.Fills.IFillModel) -> None:
        ...

    @property
    def slippage_model(self) -> QuantConnect.Orders.Slippage.ISlippageModel:
        """Slippage model use to compute slippage of market orders"""
        ...

    @property.setter
    def slippage_model(self, value: QuantConnect.Orders.Slippage.ISlippageModel) -> None:
        ...

    @property
    def portfolio_model(self) -> QuantConnect.Securities.ISecurityPortfolioModel:
        """Gets the portfolio model used by this security"""
        ...

    @property.setter
    def portfolio_model(self, value: QuantConnect.Securities.ISecurityPortfolioModel) -> None:
        ...

    @property
    def buying_power_model(self) -> QuantConnect.Securities.IBuyingPowerModel:
        """Gets the buying power model used for this security"""
        ...

    @property.setter
    def buying_power_model(self, value: QuantConnect.Securities.IBuyingPowerModel) -> None:
        ...

    @property
    def margin_model(self) -> QuantConnect.Securities.IBuyingPowerModel:
        """Gets the buying power model used for this security, an alias for BuyingPowerModel"""
        ...

    @property.setter
    def margin_model(self, value: QuantConnect.Securities.IBuyingPowerModel) -> None:
        ...

    @property
    def margin_interest_rate_model(self) -> QuantConnect.Securities.IMarginInterestRateModel:
        """Gets or sets the margin interest rate model"""
        ...

    @property.setter
    def margin_interest_rate_model(self, value: QuantConnect.Securities.IMarginInterestRateModel) -> None:
        ...

    @property
    def settlement_model(self) -> QuantConnect.Securities.ISettlementModel:
        """Gets the settlement model used for this security"""
        ...

    @property.setter
    def settlement_model(self, value: QuantConnect.Securities.ISettlementModel) -> None:
        ...

    @property
    def volatility_model(self) -> QuantConnect.Securities.IVolatilityModel:
        """Gets the volatility model used for this security"""
        ...

    @property.setter
    def volatility_model(self, value: QuantConnect.Securities.IVolatilityModel) -> None:
        ...

    @property
    def data_filter(self) -> QuantConnect.Securities.Interfaces.ISecurityDataFilter:
        """
        Customizable data filter to filter outlier ticks before they are passed into user event handlers.
        By default all ticks are passed into the user algorithms.
        """
        ...

    @property.setter
    def data_filter(self, value: QuantConnect.Securities.Interfaces.ISecurityDataFilter) -> None:
        ...

    @property
    def price_variation_model(self) -> QuantConnect.Securities.IPriceVariationModel:
        """
        Customizable price variation model used to define the minimum price variation of this security.
        By default minimum price variation is a constant find in the symbol-properties-database.
        """
        ...

    @property.setter
    def price_variation_model(self, value: QuantConnect.Securities.IPriceVariationModel) -> None:
        ...

    @property
    def data(self) -> QuantConnect.Securities.DynamicSecurityData:
        """Provides dynamic access to data in the cache"""
        ...

    @property
    def hold_stock(self) -> bool:
        """Read only property that checks if we currently own stock in the company."""
        ...

    @property
    def invested(self) -> bool:
        """Alias for HoldStock - Do we have any of this security"""
        ...

    @property
    def local_time(self) -> datetime.datetime:
        """Local time for this market"""
        ...

    @property
    def price(self) -> float:
        """Get the current value of the security."""
        ...

    @property
    def leverage(self) -> float:
        """Leverage for this Security."""
        ...

    @property
    def high(self) -> float:
        """If this uses tradebar data, return the most recent high."""
        ...

    @property
    def low(self) -> float:
        """If this uses tradebar data, return the most recent low."""
        ...

    @property
    def close(self) -> float:
        """If this uses tradebar data, return the most recent close."""
        ...

    @property
    def open(self) -> float:
        """If this uses tradebar data, return the most recent open."""
        ...

    @property
    def volume(self) -> float:
        """Access to the volume of the equity today"""
        ...

    @property
    def bid_price(self) -> float:
        """Gets the most recent bid price if available"""
        ...

    @property
    def bid_size(self) -> float:
        """Gets the most recent bid size if available"""
        ...

    @property
    def ask_price(self) -> float:
        """Gets the most recent ask price if available"""
        ...

    @property
    def ask_size(self) -> float:
        """Gets the most recent ask size if available"""
        ...

    @property
    def open_interest(self) -> int:
        """Access to the open interest of the security today"""
        ...

    @property
    def fundamentals(self) -> QuantConnect.Data.Fundamental.Fundamental:
        """Gets the fundamental data associated with the security if there is any, otherwise null."""
        ...

    def __getitem__(self, key: str) -> typing.Any:
        """
        Gets or sets the specified custom property through the indexer.
        This is a wrapper around the Get{T}(string) and Add(string,object) methods.
        
        :param key: The property key
        """
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cache: QuantConnect.Securities.SecurityCache) -> None:
        """Construct a new security vehicle based on the user options."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cache: QuantConnect.Securities.SecurityCache) -> None:
        """Construct a new security vehicle based on the user options."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, exchange: QuantConnect.Securities.SecurityExchange, cache: QuantConnect.Securities.SecurityCache, portfolioModel: QuantConnect.Securities.ISecurityPortfolioModel, fillModel: QuantConnect.Orders.Fills.IFillModel, feeModel: QuantConnect.Orders.Fees.IFeeModel, slippageModel: QuantConnect.Orders.Slippage.ISlippageModel, settlementModel: QuantConnect.Securities.ISettlementModel, volatilityModel: QuantConnect.Securities.IVolatilityModel, buyingPowerModel: QuantConnect.Securities.IBuyingPowerModel, dataFilter: QuantConnect.Securities.Interfaces.ISecurityDataFilter, priceVariationModel: QuantConnect.Securities.IPriceVariationModel, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, marginInterestRateModel: QuantConnect.Securities.IMarginInterestRateModel) -> None:
        """
        Construct a new security vehicle based on the user options.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, exchange: QuantConnect.Securities.SecurityExchange, cache: QuantConnect.Securities.SecurityCache, portfolioModel: QuantConnect.Securities.ISecurityPortfolioModel, fillModel: QuantConnect.Orders.Fills.IFillModel, feeModel: QuantConnect.Orders.Fees.IFeeModel, slippageModel: QuantConnect.Orders.Slippage.ISlippageModel, settlementModel: QuantConnect.Securities.ISettlementModel, volatilityModel: QuantConnect.Securities.IVolatilityModel, buyingPowerModel: QuantConnect.Securities.IBuyingPowerModel, dataFilter: QuantConnect.Securities.Interfaces.ISecurityDataFilter, priceVariationModel: QuantConnect.Securities.IPriceVariationModel, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, marginInterestRateModel: QuantConnect.Securities.IMarginInterestRateModel) -> None:
        """
        Temporary convenience constructor
        
        This method is protected.
        """
        ...

    def __setitem__(self, key: str, value: typing.Any) -> None:
        """
        Gets or sets the specified custom property through the indexer.
        This is a wrapper around the Get{T}(string) and Add(string,object) methods.
        
        :param key: The property key
        """
        ...

    def add(self, key: str, value: typing.Any) -> None:
        """
        Adds the specified custom property.
        This allows us to use the security object as a dynamic object for quick storage.
        
        :param key: The property key
        :param value: The property value
        """
        ...

    def clear(self) -> None:
        """Removes every custom property that had been set."""
        ...

    def get(self, key: str) -> QuantConnect_Securities_Security_Get_T:
        """
        Gets the specified custom property
        
        :param key: The property key
        :returns: The property value is found.
        """
        ...

    def get_last_data(self) -> QuantConnect.Data.BaseData:
        """
        Get the last price update set to the security if any else null
        
        :returns: BaseData object for this security.
        """
        ...

    def is_custom_data(self) -> bool:
        """
        Returns true if the security contains at least one subscription that represents custom data
        
        This method is obsolete. Use the 'SubscriptionDataConfig' exposed by" +
                    " 'SubscriptionManager' and the 'IsCustomData()' extension method
        """
        warnings.warn("This method is obsolete. Use the 'SubscriptionDataConfig' exposed by" +
                    " 'SubscriptionManager' and the 'IsCustomData()' extension method", DeprecationWarning)

    def refresh_data_normalization_mode_property(self) -> None:
        """
        This method will refresh the value of the DataNormalizationMode property.
        This is required for backward-compatibility.
        TODO: to be deleted with the DataNormalizationMode property
        """
        ...

    @overload
    def remove(self, key: str) -> bool:
        """
        Removes a custom property.
        
        :param key: The property key
        :returns: True if the property is successfully removed.
        """
        ...

    @overload
    def remove(self, key: str, value: typing.Optional[QuantConnect_Securities_Security_Remove_T]) -> typing.Union[bool, QuantConnect_Securities_Security_Remove_T]:
        """
        Removes a custom property.
        
        :param key: The property key
        :param value: The removed property value
        :returns: True if the property is successfully removed.
        """
        ...

    def set(self, key: str, value: typing.Any) -> None:
        """
        Sets the specified custom property.
        This allows us to use the security object as a dynamic object for quick storage.
        
        :param key: The property key
        :param value: The property value
        """
        ...

    @overload
    def set_buying_power_model(self, buying_power_model: QuantConnect.Securities.IBuyingPowerModel) -> None:
        """
        Sets the buying power model
        
        :param buying_power_model: Model that represents a security's model of buying power
        """
        ...

    @overload
    def set_buying_power_model(self, py_object: typing.Any) -> None:
        """
        Sets the buying power model
        
        :param py_object: Model that represents a security's model of buying power
        """
        ...

    @overload
    def set_data_filter(self, py_object: typing.Any) -> None:
        """
        Set Security Data Filter
        
        :param py_object: Python class that represents a custom Security Data Filter
        """
        ...

    @overload
    def set_data_filter(self, data_filter: QuantConnect.Securities.Interfaces.ISecurityDataFilter) -> None:
        """
        Set Security Data Filter
        
        :param data_filter: Security Data Filter
        """
        ...

    def set_data_normalization_mode(self, mode: QuantConnect.DataNormalizationMode) -> None:
        """
        Sets the data normalization mode to be used by this security
        
        This method is obsolete. Use the 'SubscriptionDataConfig' exposed by" +
                    " 'SubscriptionManager' and the 'SetDataNormalizationMode()' extension method
        """
        warnings.warn("This method is obsolete. Use the 'SubscriptionDataConfig' exposed by" +
                    " 'SubscriptionManager' and the 'SetDataNormalizationMode()' extension method", DeprecationWarning)

    @overload
    def set_fee_model(self, feel_model: QuantConnect.Orders.Fees.IFeeModel) -> None:
        """
        Sets the fee model
        
        :param feel_model: Model that represents a fee model
        """
        ...

    @overload
    def set_fee_model(self, feel_model: typing.Any) -> None:
        """
        Sets the fee model
        
        :param feel_model: Model that represents a fee model
        """
        ...

    @overload
    def set_fill_model(self, fill_model: QuantConnect.Orders.Fills.IFillModel) -> None:
        """
        Sets the fill model
        
        :param fill_model: Model that represents a fill model
        """
        ...

    @overload
    def set_fill_model(self, fill_model: typing.Any) -> None:
        """
        Sets the fill model
        
        :param fill_model: Model that represents a fill model
        """
        ...

    def set_leverage(self, leverage: float) -> None:
        """
        Set the leverage parameter for this security
        
        :param leverage: Leverage for this asset
        """
        ...

    def set_local_time_keeper(self, local_time_keeper: QuantConnect.LocalTimeKeeper) -> None:
        """
        Sets the LocalTimeKeeper to be used for this Security.
        This is the source of this instance's time.
        
        :param local_time_keeper: The source of this Security's time.
        """
        ...

    @overload
    def set_margin_interest_rate_model(self, margin_interest_rate_model: QuantConnect.Securities.IMarginInterestRateModel) -> None:
        """
        Sets the margin interests rate model
        
        :param margin_interest_rate_model: Model that represents a security's model of margin interest rate
        """
        ...

    @overload
    def set_margin_interest_rate_model(self, py_object: typing.Any) -> None:
        """
        Sets the margin interests rate model
        
        :param py_object: Model that represents a security's model of margin interest rate
        """
        ...

    @overload
    def set_margin_model(self, margin_model: QuantConnect.Securities.IBuyingPowerModel) -> None:
        """
        Sets the margin model
        
        :param margin_model: Model that represents a security's model of buying power
        """
        ...

    @overload
    def set_margin_model(self, py_object: typing.Any) -> None:
        """
        Sets the margin model
        
        :param py_object: Model that represents a security's model of buying power
        """
        ...

    def set_market_price(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Update any security properties based on the latest market data and time
        
        :param data: New data packet from LEAN
        """
        ...

    @overload
    def set_settlement_model(self, settlement_model: QuantConnect.Securities.ISettlementModel) -> None:
        """
        Sets the settlement model
        
        :param settlement_model: Model that represents a settlement model
        """
        ...

    @overload
    def set_settlement_model(self, settlement_model: typing.Any) -> None:
        """
        Sets the settlement model
        
        :param settlement_model: Model that represents a settlement model
        """
        ...

    @overload
    def set_shortable_provider(self, py_object: typing.Any) -> None:
        """
        Set Python Shortable Provider for this Security
        
        :param py_object: Python class that represents a custom shortable provider
        """
        ...

    @overload
    def set_shortable_provider(self, shortable_provider: QuantConnect.Interfaces.IShortableProvider) -> None:
        """
        Set Shortable Provider for this Security
        
        :param shortable_provider: Provider to use
        """
        ...

    @overload
    def set_slippage_model(self, slippage_model: QuantConnect.Orders.Slippage.ISlippageModel) -> None:
        """
        Sets the slippage model
        
        :param slippage_model: Model that represents a slippage model
        """
        ...

    @overload
    def set_slippage_model(self, slippage_model: typing.Any) -> None:
        """
        Sets the slippage model
        
        :param slippage_model: Model that represents a slippage model
        """
        ...

    @overload
    def set_volatility_model(self, volatility_model: QuantConnect.Securities.IVolatilityModel) -> None:
        """
        Sets the volatility model
        
        :param volatility_model: Model that represents a volatility model
        """
        ...

    @overload
    def set_volatility_model(self, volatility_model: typing.Any) -> None:
        """
        Sets the volatility model
        
        :param volatility_model: Model that represents a volatility model
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def try_get(self, key: str, value: typing.Optional[QuantConnect_Securities_Security_TryGet_T]) -> typing.Union[bool, QuantConnect_Securities_Security_TryGet_T]:
        """
        Gets the specified custom property
        
        :param key: The property key
        :param value: The property value
        :returns: True if the property is found.
        """
        ...

    def try_get_member(self, binder: typing.Any, result: typing.Optional[typing.Any]) -> typing.Union[bool, typing.Any]:
        """This is a DynamicObject override. Not meant for external use."""
        ...

    def try_invoke_member(self, binder: typing.Any, args: typing.List[System.Object], result: typing.Optional[typing.Any]) -> typing.Union[bool, typing.Any]:
        """This is a DynamicObject override. Not meant for external use."""
        ...

    def try_set_member(self, binder: typing.Any, value: typing.Any) -> bool:
        """This is a DynamicObject override. Not meant for external use."""
        ...

    def update(self, data: System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData], data_type: typing.Type, contains_fill_forward_data: typing.Optional[bool] = None) -> None:
        """
        Updates all of the security properties, such as price/OHLCV/bid/ask based
        on the data provided. Data is also stored into the security's data cache
        
        :param data: The security update data
        :param data_type: The data type
        :param contains_fill_forward_data: Flag indicating whether  contains any fill forward bar or not
        """
        ...

    def update_consumers_market_price(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Update market price of this Security
        
        This method is protected.
        
        :param data: Data to pull price from
        """
        ...


class ISecuritySeeder(metaclass=abc.ABCMeta):
    """Used to seed the security with the correct price"""

    def seed_security(self, security: QuantConnect.Securities.Security) -> bool:
        """
        Seed the security
        
        :param security: Security being seeded
        :returns: true if the security was seeded, false otherwise.
        """
        ...


class SecuritySeeder(System.Object):
    """Provides access to a null implementation for ISecuritySeeder"""

    NULL: QuantConnect.Securities.ISecuritySeeder = ...
    """Gets an instance of ISecuritySeeder that is a no-op"""


class ReservedBuyingPowerForPosition(System.Object):
    """Defines the result for IBuyingPowerModel.GetReservedBuyingPowerForPosition"""

    @property
    def absolute_used_buying_power(self) -> float:
        """Gets the reserved buying power"""
        ...

    def __init__(self, reservedBuyingPowerForPosition: float) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerForPosition class
        
        :param reservedBuyingPowerForPosition: The reserved buying power for the security's holdings
        """
        ...


class ReservedBuyingPowerForPositionParameters(System.Object):
    """Defines the parameters for IBuyingPowerModel.GetReservedBuyingPowerForPosition"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerForPositionParameters class
        
        :param security: The security
        """
        ...

    def result_in_account_currency(self, reserved_buying_power: float) -> QuantConnect.Securities.ReservedBuyingPowerForPosition:
        """
        Creates the result using the specified reserved buying power in units of the account currency
        
        :param reserved_buying_power: The reserved buying power in units of the account currency
        :returns: The reserved buying power.
        """
        ...


class MaintenanceMarginParameters(System.Object):
    """Parameters for IBuyingPowerModel.GetMaintenanceMargin"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def quantity(self) -> float:
        """Gets the quantity of the security"""
        ...

    @property
    def absolute_quantity(self) -> float:
        """Gets the absolute quantity of the security"""
        ...

    @property
    def holdings_cost(self) -> float:
        """Gets the holdings cost of the security"""
        ...

    @property
    def absolute_holdings_cost(self) -> float:
        """Gets the absolute holdings cost of the security"""
        ...

    @property
    def holdings_value(self) -> float:
        """Gets the holdings value of the security"""
        ...

    @property
    def absolute_holdings_value(self) -> float:
        """Gets the absolute holdings value of the security"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, quantity: float, holdingsCost: float, holdingsValue: float) -> None:
        """
        Initializes a new instance of the MaintenanceMarginParameters class
        
        :param security: The security
        :param quantity: The quantity
        :param holdingsCost: The holdings cost
        :param holdingsValue: The holdings value
        """
        ...

    @staticmethod
    def for_current_holdings(security: QuantConnect.Securities.Security) -> QuantConnect.Securities.MaintenanceMarginParameters:
        """
        Creates a new instance of the MaintenanceMarginParameters class to compute the maintenance margin
        required to support the algorithm's current holdings
        """
        ...

    @staticmethod
    def for_quantity_at_current_price(security: QuantConnect.Securities.Security, quantity: float) -> QuantConnect.Securities.MaintenanceMarginParameters:
        """
        Creates a new instance of the MaintenanceMarginParameters class to compute the maintenance margin
        required to support the specified quantity of holdings at current market prices
        """
        ...

    def for_underlying(self, quantity: float) -> QuantConnect.Securities.MaintenanceMarginParameters:
        """Creates a new instance of MaintenanceMarginParameters for the security's underlying"""
        ...


class ISecurityProvider(metaclass=abc.ABCMeta):
    """Represents a type capable of fetching the holdings for the specified symbol"""

    def get_security(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Security:
        """
        Retrieves a summary of the holdings for the specified symbol
        
        :param symbol: The symbol to get holdings for
        :returns: The holdings for the symbol or null if the symbol is invalid and/or not in the portfolio.
        """
        ...


class CashBookUpdatedEventArgs(System.EventArgs):
    """Event fired when the cash book is updated"""

    @property
    def update_type(self) -> QuantConnect.CashBookUpdateType:
        """The update type"""
        ...

    @property
    def cash(self) -> QuantConnect.Securities.Cash:
        """The updated cash instance."""
        ...

    def __init__(self, type: QuantConnect.CashBookUpdateType, cash: QuantConnect.Securities.Cash) -> None:
        """Creates a new instance"""
        ...


class CashBook(System.Object, System.Collections.Generic.IDictionary[str, QuantConnect.Securities.Cash], QuantConnect.Securities.ICurrencyConverter, typing.Iterable[System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]]):
    """Provides a means of keeping track of the different cash holdings of an algorithm"""

    @property
    def updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Securities.CashBookUpdatedEventArgs], None], None]:
        """
        Event fired when a Cash instance is added or removed, and when
        the Cash.Updated is triggered for the currently hold instances
        """
        ...

    @property
    def account_currency(self) -> str:
        """Gets the base currency used"""
        ...

    @property.setter
    def account_currency(self, value: str) -> None:
        ...

    @property
    def total_value_in_account_currency(self) -> float:
        """Gets the total value of the cash book in units of the base currency"""
        ...

    @property
    def count(self) -> int:
        """Gets the count of Cash items in this CashBook."""
        ...

    @property
    def is_read_only(self) -> bool:
        """Gets a value indicating whether this instance is read only."""
        ...

    @property
    def keys(self) -> System.Collections.Generic.ICollection[str]:
        """Gets the keys."""
        ...

    @property
    def values(self) -> System.Collections.Generic.ICollection[QuantConnect.Securities.Cash]:
        """Gets the values."""
        ...

    def __getitem__(self, symbol: str) -> QuantConnect.Securities.Cash:
        """
        Gets or sets the QuantConnect.Securities.Cash with the specified symbol.
        
        :param symbol: Symbol.
        """
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the CashBook class."""
        ...

    def __setitem__(self, symbol: str, value: QuantConnect.Securities.Cash) -> None:
        """
        Gets or sets the QuantConnect.Securities.Cash with the specified symbol.
        
        :param symbol: Symbol.
        """
        ...

    @overload
    def add(self, symbol: str, quantity: float, conversion_rate: float) -> QuantConnect.Securities.Cash:
        """
        Adds a new cash of the specified symbol and quantity
        
        :param symbol: The symbol used to reference the new cash
        :param quantity: The amount of new cash to start
        :param conversion_rate: The conversion rate used to determine the initial portfolio value/starting capital impact caused by this currency position.
        :returns: The added cash instance.
        """
        ...

    @overload
    def add(self, item: System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]) -> None:
        """
        Add the specified item to this CashBook.
        
        :param item: KeyValuePair of symbol -> Cash item
        """
        ...

    @overload
    def add(self, symbol: str, value: QuantConnect.Securities.Cash) -> None:
        """
        Add the specified key and value.
        
        :param symbol: The symbol of the Cash value.
        :param value: Value.
        """
        ...

    def clear(self) -> None:
        """Clear this instance of all Cash entries."""
        ...

    def contains(self, item: System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]) -> bool:
        """
        Determines whether the current collection contains the specified value.
        
        :param item: Item.
        """
        ...

    def contains_key(self, symbol: str) -> bool:
        """
        Determines whether the current instance contains an entry with the specified symbol.
        
        :param symbol: Key.
        :returns: true, if key was contained, false otherwise.
        """
        ...

    def convert(self, source_quantity: float, source_currency: str, destination_currency: str) -> float:
        """
        Converts a quantity of source currency units into the specified destination currency
        
        :param source_quantity: The quantity of source currency to be converted
        :param source_currency: The source currency symbol
        :param destination_currency: The destination currency symbol
        :returns: The converted value.
        """
        ...

    @overload
    def convert_to_account_currency(self, source_quantity: float, source_currency: str) -> float:
        """
        Converts a quantity of source currency units into the account currency
        
        :param source_quantity: The quantity of source currency to be converted
        :param source_currency: The source currency symbol
        :returns: The converted value.
        """
        ...

    @overload
    def convert_to_account_currency(self, cash_amount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        """
        Converts a cash amount to the account currency
        
        :param cash_amount: The CashAmount instance to convert
        :returns: A new CashAmount instance denominated in the account currency.
        """
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]], array_index: int) -> None:
        """
        Copies to the specified array.
        
        :param array: Array.
        :param array_index: Array index.
        """
        ...

    def ensure_currency_data_feeds(self, securities: QuantConnect.Securities.SecurityManager, subscriptions: QuantConnect.Data.SubscriptionManager, market_map: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, security_service: QuantConnect.Interfaces.ISecurityService, default_resolution: QuantConnect.Resolution = ...) -> System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Checks the current subscriptions and adds necessary currency pair feeds to provide real time conversion data
        
        :param securities: The SecurityManager for the algorithm
        :param subscriptions: The SubscriptionManager for the algorithm
        :param market_map: The market map that decides which market the new security should be in
        :param changes: Will be used to consume SecurityChanges.AddedSecurities
        :param security_service: Will be used to create required new Security
        :param default_resolution: The default resolution to use for the internal subscriptions
        :returns: Returns a list of added currency SubscriptionDataConfig.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]]:
        """
        Gets the enumerator.
        
        :returns: The enumerator.
        """
        ...

    @overload
    def remove(self, symbol: str) -> bool:
        """
        Remove the Cash item corresponding to the specified symbol
        
        :param symbol: The symbolto be removed
        """
        ...

    @overload
    def remove(self, item: System.Collections.Generic.KeyValuePair[str, QuantConnect.Securities.Cash]) -> bool:
        """
        Remove the specified item.
        
        :param item: Item.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def try_get_value(self, symbol: str, value: typing.Optional[QuantConnect.Securities.Cash]) -> typing.Union[bool, QuantConnect.Securities.Cash]:
        """
        Try to get the value.
        
        :param symbol: The symbol.
        :param value: Value.
        :returns: true, if get value was tryed, false otherwise.
        """
        ...


class SecurityDatabaseKey(System.Object, System.IEquatable[QuantConnect_Securities_SecurityDatabaseKey]):
    """Represents the key to a single entry in the MarketHoursDatabase or the SymbolPropertiesDatabase"""

    WILDCARD: str = "[*]"
    """Represents that the specified symbol or market field will match all"""

    @property
    def market(self) -> str:
        """The market. If null, ignore market filtering"""
        ...

    @property
    def symbol(self) -> str:
        """The symbol. If null, ignore symbol filtering"""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """The security type"""
        ...

    def __init__(self, market: str, symbol: str, securityType: QuantConnect.SecurityType) -> None:
        """
        Initializes a new instance of the SecurityDatabaseKey class
        
        :param market: The market
        :param symbol: The symbol. specify null to apply to all symbols in market/security type
        :param securityType: The security type
        """
        ...

    def create_common_key(self) -> QuantConnect.Securities.SecurityDatabaseKey:
        """Based on this entry will initializes the generic market and security type instance of the SecurityDatabaseKey class"""
        ...

    @overload
    def equals(self, other: QuantConnect.Securities.SecurityDatabaseKey) -> bool:
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

    @staticmethod
    def parse(key: str) -> QuantConnect.Securities.SecurityDatabaseKey:
        """
        Parses the specified string as a SecurityDatabaseKey
        
        :param key: The string representation of the key
        :returns: A new SecurityDatabaseKey instance.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class BaseSecurityDatabase(typing.Generic[QuantConnect_Securities_BaseSecurityDatabase_T, QuantConnect_Securities_BaseSecurityDatabase_TEntry], System.Object, metaclass=abc.ABCMeta):
    """Base class for security databases, including market hours and symbol properties."""

    data_folder_database: QuantConnect_Securities_BaseSecurityDatabase_T
    """
    The database instance loaded from the data folder
    
    This property is protected.
    """

    DATA_FOLDER_DATABASE_LOCK: System.Object = ...
    """
    Lock object for the data folder database
    
    This field is protected.
    """

    @property
    def entries(self) -> System.Collections.Generic.Dictionary[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect_Securities_BaseSecurityDatabase_TEntry]:
        """
        The database entries
        
        This property is protected.
        """
        ...

    @property.setter
    def entries(self, value: System.Collections.Generic.Dictionary[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect_Securities_BaseSecurityDatabase_TEntry]) -> None:
        ...

    @property
    def custom_entries(self) -> System.Collections.Generic.HashSet[QuantConnect.Securities.SecurityDatabaseKey]:
        """
        Custom entries set by the user.
        
        This property is protected.
        """
        ...

    def __init__(self, entries: System.Collections.Generic.Dictionary[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect_Securities_BaseSecurityDatabase_TEntry], fromDataFolder: typing.Callable[[], QuantConnect_Securities_BaseSecurityDatabase_T], updateEntry: typing.Callable[[QuantConnect_Securities_BaseSecurityDatabase_TEntry, QuantConnect_Securities_BaseSecurityDatabase_TEntry], None]) -> None:
        """
        Initializes a new instance of the BaseSecurityDatabase{T, TEntry} class
        
        This method is protected.
        
        :param entries: The full listing of exchange hours by key
        :param fromDataFolder: Method to load the database form the data folder
        :param updateEntry: Method to update a database entry
        """
        ...

    @overload
    def contains_key(self, key: QuantConnect.Securities.SecurityDatabaseKey) -> bool:
        """
        Determines if the database contains the specified key
        
        This method is protected.
        
        :param key: The key to search for
        :returns: True if an entry is found, otherwise false.
        """
        ...

    @overload
    def contains_key(self, market: str, symbol: str, security_type: QuantConnect.SecurityType) -> bool:
        """
        Check whether an entry exists for the specified market/symbol/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        """
        ...

    @overload
    def contains_key(self, market: str, symbol: typing.Union[QuantConnect.Symbol, str], security_type: QuantConnect.SecurityType) -> bool:
        """
        Check whether an entry exists for the specified market/symbol/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded (Symbol class)
        :param security_type: The security type of the symbol
        """
        ...

    @staticmethod
    def get_database_symbol_key(symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Gets the correct string symbol to use as a database key
        
        :param symbol: The symbol
        :returns: The symbol string used in the database ke.
        """
        ...

    @staticmethod
    def reset() -> None:
        """
        Resets the database, forcing a reload when reused.
        Called in tests where multiple algorithms are run sequentially,
        and we need to guarantee that every test starts with the same environment.
        """
        ...


class MarketHoursDatabase(QuantConnect.Securities.BaseSecurityDatabase[QuantConnect_Securities_MarketHoursDatabase, QuantConnect_Securities_MarketHoursDatabase_Entry]):
    """Provides access to exchange hours and raw data times zones in various markets"""

    class Entry(System.Object):
        """Represents a single entry in the MarketHoursDatabase"""

        @property
        def data_time_zone(self) -> typing.Any:
            """Gets the raw data time zone for this entry"""
            ...

        @property
        def exchange_hours(self) -> QuantConnect.Securities.SecurityExchangeHours:
            """Gets the exchange hours for this entry"""
            ...

        def __init__(self, dataTimeZone: typing.Any, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
            """
            Initializes a new instance of the Entry class
            
            :param dataTimeZone: The raw data time zone
            :param exchangeHours: The security exchange hours for this entry
            """
            ...

    @property
    def exchange_hours_listing(self) -> System.Collections.Generic.List[System.Collections.Generic.KeyValuePair[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect.Securities.MarketHoursDatabase.Entry]]:
        """Gets all the exchange hours held by this provider"""
        ...

    ALWAYS_OPEN: QuantConnect.Securities.MarketHoursDatabase
    """Gets a MarketHoursDatabase that always returns SecurityExchangeHours.AlwaysOpen"""

    def __init__(self, exchangeHours: System.Collections.Generic.Dictionary[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect.Securities.MarketHoursDatabase.Entry]) -> None:
        """
        Initializes a new instance of the MarketHoursDatabase class
        
        :param exchangeHours: The full listing of exchange hours by key
        """
        ...

    @staticmethod
    def from_data_folder() -> QuantConnect.Securities.MarketHoursDatabase:
        """
        Gets the instance of the MarketHoursDatabase class produced by reading in the market hours
        data found in /Data/market-hours/
        
        :returns: A MarketHoursDatabase class that represents the data in the market-hours folder.
        """
        ...

    @staticmethod
    def from_file(path: str) -> QuantConnect.Securities.MarketHoursDatabase:
        """
        Reads the specified file as a market hours database instance
        
        :param path: The market hours database file path
        :returns: A new instance of the MarketHoursDatabase class.
        """
        ...

    def get_data_time_zone(self, market: str, symbol: typing.Union[QuantConnect.Symbol, str], security_type: QuantConnect.SecurityType) -> typing.Any:
        """
        Performs a lookup using the specified information and returns the data's time zone if found,
        if an entry is not found, an exception is thrown
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :returns: The raw data time zone for the specified security.
        """
        ...

    @overload
    def get_entry(self, market: str, symbol: str, security_type: QuantConnect.SecurityType) -> QuantConnect.Securities.MarketHoursDatabase.Entry:
        """
        Gets the entry for the specified market/symbol/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :returns: The entry matching the specified market/symbol/security-type.
        """
        ...

    @overload
    def get_entry(self, market: str, symbol: typing.Union[QuantConnect.Symbol, str], security_type: QuantConnect.SecurityType) -> QuantConnect.Securities.MarketHoursDatabase.Entry:
        """
        Gets the entry for the specified market/symbol/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded (Symbol class)
        :param security_type: The security type of the symbol
        :returns: The entry matching the specified market/symbol/security-type.
        """
        ...

    @overload
    def get_exchange_hours(self, configuration: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Securities.SecurityExchangeHours:
        """
        Convenience method for retrieving exchange hours from market hours database using a subscription config
        
        :param configuration: The subscription data config to get exchange hours for
        :returns: The configure exchange hours for the specified configuration.
        """
        ...

    @overload
    def get_exchange_hours(self, market: str, symbol: typing.Union[QuantConnect.Symbol, str], security_type: QuantConnect.SecurityType) -> QuantConnect.Securities.SecurityExchangeHours:
        """
        Convenience method for retrieving exchange hours from market hours database using a subscription config
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :returns: The exchange hours for the specified security.
        """
        ...

    def set_entry(self, market: str, symbol: str, security_type: QuantConnect.SecurityType, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, data_time_zone: typing.Any = None) -> QuantConnect.Securities.MarketHoursDatabase.Entry:
        """
        Sets the entry for the specified market/symbol/security-type.
        This is intended to be used by custom data and other data sources that don't have explicit
        entries in market-hours-database.csv. At run time, the algorithm can update the market hours
        database via calls to AddData.
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :param exchange_hours: The exchange hours for the specified symbol
        :param data_time_zone: The time zone of the symbol's raw data. Optional, defaults to the exchange time zone
        :returns: The entry matching the specified market/symbol/security-type.
        """
        ...

    def set_entry_always_open(self, market: str, symbol: str, security_type: QuantConnect.SecurityType, time_zone: typing.Any) -> QuantConnect.Securities.MarketHoursDatabase.Entry:
        """
        Convenience method for the common custom data case.
        Sets the entry for the specified symbol using SecurityExchangeHours.AlwaysOpen(time_zone)
        This sets the data time zone equal to the exchange time zone as well.
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :param time_zone: The time zone of the symbol's exchange and raw data
        :returns: The entry matching the specified market/symbol/security-type.
        """
        ...

    @overload
    def try_get_entry(self, market: str, symbol: typing.Union[QuantConnect.Symbol, str], security_type: QuantConnect.SecurityType, entry: typing.Optional[QuantConnect.Securities.MarketHoursDatabase.Entry]) -> typing.Union[bool, QuantConnect.Securities.MarketHoursDatabase.Entry]:
        """
        Tries to get the entry for the specified market/symbol/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :param entry: The entry found if any
        :returns: True if the entry was present, else false.
        """
        ...

    @overload
    def try_get_entry(self, market: str, symbol: str, security_type: QuantConnect.SecurityType, entry: typing.Optional[QuantConnect.Securities.MarketHoursDatabase.Entry]) -> typing.Union[bool, QuantConnect.Securities.MarketHoursDatabase.Entry]:
        """
        Tries to get the entry for the specified market/symbol/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :param entry: The entry found if any
        :returns: True if the entry was present, else false.
        """
        ...


class SymbolPropertiesDatabase(QuantConnect.Securities.BaseSecurityDatabase[QuantConnect_Securities_SymbolPropertiesDatabase, QuantConnect.Securities.SymbolProperties]):
    """Provides access to specific properties for various symbols"""

    def __init__(self, file: str) -> None:
        """
        Initialize a new instance of SymbolPropertiesDatabase using the given file
        
        This method is protected.
        
        :param file: File to read from
        """
        ...

    @staticmethod
    def from_csv_line(line: str, key: typing.Optional[QuantConnect.Securities.SecurityDatabaseKey]) -> typing.Union[QuantConnect.Securities.SymbolProperties, QuantConnect.Securities.SecurityDatabaseKey]:
        """
        Creates a new instance of SymbolProperties from the specified csv line
        
        This method is protected.
        
        :param line: The csv line to be parsed
        :param key: The key used to uniquely identify this security
        :returns: A new SymbolProperties for the specified csv line.
        """
        ...

    @staticmethod
    def from_data_folder() -> QuantConnect.Securities.SymbolPropertiesDatabase:
        """
        Gets the instance of the SymbolPropertiesDatabase class produced by reading in the symbol properties
        data found in /Data/symbol-properties/
        
        :returns: A SymbolPropertiesDatabase class that represents the data in the symbol-properties folder.
        """
        ...

    def get_symbol_properties(self, market: str, symbol: typing.Union[QuantConnect.Symbol, str], security_type: QuantConnect.SecurityType, default_quote_currency: str) -> QuantConnect.Securities.SymbolProperties:
        """
        Gets the symbol properties for the specified market/symbol/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param symbol: The particular symbol being traded (Symbol class)
        :param security_type: The security type of the symbol
        :param default_quote_currency: Specifies the quote currency to be used when returning a default instance of an entry is not found in the database
        :returns: The symbol properties matching the specified market/symbol/security-type or null if not found.
        """
        ...

    @overload
    def get_symbol_properties_list(self, market: str, security_type: QuantConnect.SecurityType) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect.Securities.SymbolProperties]]:
        """
        Gets a list of symbol properties for the specified market/security-type
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :param security_type: The security type of the symbol
        :returns: An IEnumerable of symbol properties matching the specified market/security-type.
        """
        ...

    @overload
    def get_symbol_properties_list(self, market: str) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[QuantConnect.Securities.SecurityDatabaseKey, QuantConnect.Securities.SymbolProperties]]:
        """
        Gets a list of symbol properties for the specified market
        
        :param market: The market the exchange resides in, i.e, 'usa', 'fxcm', ect...
        :returns: An IEnumerable of symbol properties matching the specified market.
        """
        ...

    def set_entry(self, market: str, symbol: str, security_type: QuantConnect.SecurityType, properties: QuantConnect.Securities.SymbolProperties) -> bool:
        """
        Set SymbolProperties entry for a particular market, symbol and security type.
        
        :param market: Market of the entry
        :param symbol: Symbol of the entry
        :param security_type: Type of security for the entry
        :param properties: The new symbol properties to store
        :returns: True if successful.
        """
        ...

    def try_get_market(self, symbol: str, security_type: QuantConnect.SecurityType, market: typing.Optional[str]) -> typing.Union[bool, str]:
        """
        Tries to get the market for the provided symbol/security type
        
        :param symbol: The particular symbol being traded
        :param security_type: The security type of the symbol
        :param market: The market the exchange resides in Market
        :returns: True if market was retrieved, false otherwise.
        """
        ...


class SecurityCacheProvider(System.Object):
    """A helper class that will provide SecurityCache instances"""

    def __init__(self, securityProvider: QuantConnect.Securities.ISecurityProvider) -> None:
        """
        Creates a new instance
        
        :param securityProvider: The security provider to use
        """
        ...

    def get_security_cache(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.SecurityCache:
        """
        Will return the SecurityCache instance to use for a give Symbol.
        If the provided Symbol is a custom type which has an underlying we will try to use the
        underlying SecurityCache type cache, if the underlying is not present we will keep track
        of the custom Symbol in case it is added later.
        
        :returns: The cache instance to use.
        """
        ...


class SecurityService(System.Object, QuantConnect.Interfaces.ISecurityService):
    """This class implements interface ISecurityService providing methods for creating new Security"""

    def __init__(self, cashBook: QuantConnect.Securities.CashBook, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase, symbolPropertiesDatabase: QuantConnect.Securities.SymbolPropertiesDatabase, securityInitializerProvider: QuantConnect.Interfaces.ISecurityInitializerProvider, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cacheProvider: QuantConnect.Securities.SecurityCacheProvider, primaryExchangeProvider: QuantConnect.Interfaces.IPrimaryExchangeProvider = None, algorithm: QuantConnect.Interfaces.IAlgorithm = None) -> None:
        """Creates a new instance of the SecurityService class"""
        ...

    def create_benchmark_security(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Security:
        """Creates a new security"""
        ...

    @overload
    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str], subscription_data_config_list: System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig], leverage: float = 0, add_to_symbol_cache: bool = True, underlying: QuantConnect.Securities.Security = None) -> QuantConnect.Securities.Security:
        """Creates a new security"""
        ...

    @overload
    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str], subscription_data_config: QuantConnect.Data.SubscriptionDataConfig, leverage: float = 0, add_to_symbol_cache: bool = True, underlying: QuantConnect.Securities.Security = None) -> QuantConnect.Securities.Security:
        """Creates a new security"""
        ...

    def set_live_mode(self, is_live_mode: bool) -> None:
        """
        Set live mode state of the algorithm
        
        :param is_live_mode: True, live mode is enabled
        """
        ...


class SecurityManager(QuantConnect.ExtendedDictionary[QuantConnect.Securities.Security], System.Collections.Generic.IDictionary[QuantConnect.Symbol, QuantConnect.Securities.Security], System.Collections.Specialized.INotifyCollectionChanged, typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]]):
    """Enumerable security management class for grouping security objects into an array and providing any common properties."""

    @property
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]:
        """Event fired when a security is added or removed from this collection"""
        ...

    @property
    def utc_time(self) -> datetime.datetime:
        """Gets the most recent time this manager was updated"""
        ...

    @property
    def count(self) -> int:
        """Count of the number of securities in the collection."""
        ...

    @property
    def is_read_only(self) -> bool:
        """Flag indicating if the internal array is read only."""
        ...

    @property
    def keys(self) -> System.Collections.Generic.ICollection[QuantConnect.Symbol]:
        """List of the symbol-keys in the collection of securities."""
        ...

    @property
    def get_keys(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets an System.Collections.Generic.ICollection{T} containing the Symbol objects of the System.Collections.Generic.IDictionary{TKey, TValue}.
        
        This property is protected.
        """
        ...

    @property
    def get_values(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security]:
        """
        Gets an System.Collections.Generic.ICollection{T} containing the values in the System.Collections.Generic.IDictionary{TKey, TValue}.
        
        This property is protected.
        """
        ...

    @property
    def values(self) -> System.Collections.Generic.ICollection[QuantConnect.Securities.Security]:
        """Get a list of the security objects for this collection."""
        ...

    @property
    def total(self) -> System.Collections.Generic.ICollection[QuantConnect.Securities.Security]:
        """Get a list of the complete security objects for this collection, including non active or delisted securities"""
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Security:
        """
        Indexer method for the security manager to access the securities objects by their symbol.
        
        :param symbol: Symbol object indexer
        :returns: Security.
        """
        ...

    def __init__(self, timeKeeper: QuantConnect.Interfaces.ITimeKeeper) -> None:
        """Initialise the algorithm security manager with two empty dictionaries"""
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Securities.Security) -> None:
        """
        Indexer method for the security manager to access the securities objects by their symbol.
        
        :param symbol: Symbol object indexer
        :returns: Security.
        """
        ...

    @overload
    def add(self, symbol: typing.Union[QuantConnect.Symbol, str], security: QuantConnect.Securities.Security) -> None:
        """
        Add a new security with this symbol to the collection.
        
        :param symbol: symbol for security we're trading
        :param security: security object
        """
        ...

    @overload
    def add(self, security: QuantConnect.Securities.Security) -> None:
        """
        Add a new security with this symbol to the collection.
        
        :param security: security object
        """
        ...

    @overload
    def add(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]) -> None:
        """Add a symbol-security by its key value pair."""
        ...

    def clear(self) -> None:
        """Clear the securities array to delete all the portfolio and asset information."""
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]) -> bool:
        """
        Check if this collection contains this key value pair.
        
        :param pair: Search key-value pair
        :returns: Bool true if contains this key-value pair.
        """
        ...

    def contains_key(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Check if this collection contains this symbol.
        
        :param symbol: Symbol we're checking for.
        :returns: Bool true if contains this symbol pair.
        """
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]], number: int) -> None:
        """
        Copy from the internal array to an external array.
        
        :param array: Array we're outputting to
        :param number: Starting index of array
        """
        ...

    def create_benchmark_security(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Security:
        """Creates a new benchmark security"""
        ...

    @overload
    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str], subscription_data_config_list: System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig], leverage: float = 0, add_to_symbol_cache: bool = True, underlying: QuantConnect.Securities.Security = None) -> QuantConnect.Securities.Security:
        """Creates a new security"""
        ...

    @overload
    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str], subscription_data_config: QuantConnect.Data.SubscriptionDataConfig, leverage: float = 0, add_to_symbol_cache: bool = True, underlying: QuantConnect.Securities.Security = None) -> QuantConnect.Securities.Security:
        """Creates a new security"""
        ...

    def on_collection_changed(self, changed_event_args: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        """
        Event invocator for the CollectionChanged event
        
        This method is protected.
        
        :param changed_event_args: Event arguments for the CollectionChanged event
        """
        ...

    @overload
    def remove(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.Security]) -> bool:
        """
        Remove a key value of of symbol-securities from the collections.
        
        :param pair: Key Value pair of symbol-security to remove
        :returns: Boolean true on success.
        """
        ...

    @overload
    def remove(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Remove this symbol security: Dictionary interface implementation.
        
        :param symbol: Symbol we're searching for
        :returns: true success.
        """
        ...

    def set_live_mode(self, is_live_mode: bool) -> None:
        """
        Set live mode state of the algorithm
        
        :param is_live_mode: True, live mode is enabled
        """
        ...

    def set_security_service(self, security_service: QuantConnect.Securities.SecurityService) -> None:
        """Sets the Security Service to be used"""
        ...

    def try_get_value(self, symbol: typing.Union[QuantConnect.Symbol, str], security: typing.Optional[QuantConnect.Securities.Security]) -> typing.Union[bool, QuantConnect.Securities.Security]:
        """
        Try and get this security object with matching symbol and return true on success.
        
        :param symbol: String search symbol
        :param security: Output Security object
        :returns: True on successfully locating the security object.
        """
        ...


class IOrderProvider(metaclass=abc.ABCMeta):
    """Represents a type capable of fetching Order instances by its QC order id or by a brokerage id"""

    @property
    @abc.abstractmethod
    def orders_count(self) -> int:
        """Gets the current number of orders that have been processed"""
        ...

    def get_open_orders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool] = None) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets open orders matching the specified filter. Specifying null will return an enumerable
        of all open orders.
        
        :param filter: Delegate used to filter the orders
        :returns: All filtered open orders this order provider currently holds.
        """
        ...

    def get_open_order_tickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets and enumerable of opened OrderTicket matching the specified
        
        :param filter: The filter predicate used to find the required order tickets. If null is specified then all tickets are returned
        :returns: An enumerable of opened OrderTicket matching the specified.
        """
        ...

    def get_order_by_id(self, order_id: int) -> QuantConnect.Orders.Order:
        """
        Get the order by its id
        
        :param order_id: Order id to fetch
        :returns: A clone of the order with the specified id, or null if no match is found.
        """
        ...

    def get_orders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.Order]:
        """
        Gets all orders matching the specified filter. Specifying null will return an enumerable
        of all orders.
        
        :param filter: Delegate used to filter the orders
        :returns: All orders this order provider currently holds by the specified filter.
        """
        ...

    def get_orders_by_brokerage_id(self, brokerage_id: str) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets the Lean orders by its brokerage id
        
        :param brokerage_id: The brokerage id to fetch
        :returns: The orders matching the brokerage id, or null if no match is found.
        """
        ...

    def get_order_ticket(self, order_id: int) -> QuantConnect.Orders.OrderTicket:
        """
        Gets the order ticket for the specified order id. Returns null if not found
        
        :param order_id: The order's id
        :returns: The order ticket with the specified id, or null if not found.
        """
        ...

    def get_order_tickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets and enumerable of OrderTicket matching the specified
        
        :param filter: The filter predicate used to find the required order tickets. If null is specified then all tickets are returned
        :returns: An enumerable of OrderTicket matching the specified.
        """
        ...


class IOrderProcessor(QuantConnect.Securities.IOrderProvider, metaclass=abc.ABCMeta):
    """Represents a type capable of processing orders"""

    def process(self, request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Adds the specified order to be processed
        
        :param request: The OrderRequest to be processed
        :returns: The OrderTicket for the corresponding OrderRequest.OrderId.
        """
        ...


class SecurityTransactionManager(System.Object, QuantConnect.Securities.IOrderProvider):
    """Algorithm Transactions Manager - Recording Transactions"""

    @property
    def utc_time(self) -> datetime.datetime:
        """Gets the time the security information was last updated"""
        ...

    @property
    def transaction_record(self) -> System.Collections.Generic.Dictionary[datetime.datetime, float]:
        """Trade record of profits and losses for each trade statistics calculations"""
        ...

    @property
    def win_count(self) -> int:
        """Gets the number or winning transactions"""
        ...

    @property
    def loss_count(self) -> int:
        """Gets the number of losing transactions"""
        ...

    @property
    def winning_transactions(self) -> System.Collections.Generic.Dictionary[datetime.datetime, float]:
        """Trade record of profits and losses for each trade statistics calculations that are considered winning trades"""
        ...

    @property
    def losing_transactions(self) -> System.Collections.Generic.Dictionary[datetime.datetime, float]:
        """Trade record of profits and losses for each trade statistics calculations that are considered losing trades"""
        ...

    @property
    def minimum_order_size(self) -> float:
        """
        Configurable minimum order value to ignore bad orders, or orders with unrealistic sizes
        
        MinimumOrderSize is obsolete and will not be used, please use Settings.MinimumOrderMarginPortfolioPercentage instead
        """
        warnings.warn("MinimumOrderSize is obsolete and will not be used, please use Settings.MinimumOrderMarginPortfolioPercentage instead", DeprecationWarning)

    @property
    def minimum_order_quantity(self) -> int:
        """
        Configurable minimum order size to ignore bad orders, or orders with unrealistic sizes
        
        MinimumOrderQuantity is obsolete and will not be used, please use Settings.MinimumOrderMarginPortfolioPercentage instead
        """
        warnings.warn("MinimumOrderQuantity is obsolete and will not be used, please use Settings.MinimumOrderMarginPortfolioPercentage instead", DeprecationWarning)

    @property
    def last_order_id(self) -> int:
        """Get the last order id."""
        ...

    @property
    def market_order_fill_timeout(self) -> datetime.timedelta:
        """Configurable timeout for market order fills"""
        ...

    @property.setter
    def market_order_fill_timeout(self, value: datetime.timedelta) -> None:
        ...

    @property
    def orders_count(self) -> int:
        """Gets the current number of orders that have been processed"""
        ...

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, security: QuantConnect.Securities.SecurityManager) -> None:
        """Initialise the transaction manager for holding and processing orders."""
        ...

    def add_order(self, request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Add an order to collection and return the unique order id or negative if an error.
        
        :param request: A request detailing the order to be submitted
        :returns: New unique, increasing orderid.
        """
        ...

    def add_transaction_record(self, time: typing.Union[datetime.datetime, datetime.date], transaction_profit_loss: float, is_win: bool) -> None:
        """
        Record the transaction value and time in a list to later be processed for statistics creation.
        
        :param time: Time of order processed
        :param transaction_profit_loss: Profit Loss.
        :param is_win: Whether the transaction is a win. For options exercise, this might not depend only on the profit/loss value
        """
        ...

    @overload
    def cancel_open_orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Cancels all open orders for all symbols
        
        :returns: List containing the cancelled order tickets.
        """
        ...

    @overload
    def cancel_open_orders(self, symbol: typing.Union[QuantConnect.Symbol, str], tag: str = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Cancels all open orders for the specified symbol
        
        :param symbol: The symbol whose orders are to be cancelled
        :param tag: Custom order tag
        :returns: List containing the cancelled order tickets.
        """
        ...

    def cancel_order(self, order_id: int, order_tag: str = None) -> QuantConnect.Orders.OrderTicket:
        """
        Added alias for RemoveOrder -
        
        :param order_id: Order id we wish to cancel
        :param order_tag: Tag to indicate from where this method was called
        """
        ...

    def get_increment_group_order_manager_id(self) -> int:
        """
        Get a new group order manager id, and increment the internal counter.
        
        :returns: New unique int group order manager id.
        """
        ...

    def get_increment_order_id(self) -> int:
        """
        Get a new order id, and increment the internal counter.
        
        :returns: New unique int order id.
        """
        ...

    @overload
    def get_open_orders(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Get a list of all open orders for a symbol.
        
        :param symbol: The symbol for which to return the orders
        :returns: List of open orders.
        """
        ...

    @overload
    def get_open_orders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool] = None) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets open orders matching the specified filter. Specifying null will return an enumerable
        of all open orders.
        
        :param filter: Delegate used to filter the orders
        :returns: All filtered open orders this order provider currently holds.
        """
        ...

    @overload
    def get_open_orders(self, filter: typing.Any) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets open orders matching the specified filter. However, this method can be confused with the
        override that takes a Symbol as parameter. For this reason it first checks if it can convert
        the parameter into a symbol. If that conversion cannot be aplied it assumes the parameter is
        a Python function object and not a Python representation of a Symbol.
        
        :param filter: Python function object used to filter the orders
        :returns: All filtered open orders this order provider currently holds.
        """
        ...

    @overload
    def get_open_orders_remaining_quantity(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool] = None) -> float:
        """
        Gets the remaining quantity to be filled from open orders, i.e. order size minus quantity filled
        
        :param filter: Filters the order tickets to be included in the aggregate quantity remaining to be filled
        :returns: Total quantity that hasn't been filled yet for all orders that were not filtered.
        """
        ...

    @overload
    def get_open_orders_remaining_quantity(self, filter: typing.Any) -> float:
        """
        Gets the remaining quantity to be filled from open orders, i.e. order size minus quantity filled
        However, this method can be confused with the override that takes a Symbol as parameter. For this reason
        it first checks if it can convert the parameter into a symbol. If that conversion cannot be aplied it
        assumes the parameter is a Python function object and not a Python representation of a Symbol.
        
        :param filter: Filters the order tickets to be included in the aggregate quantity remaining to be filled
        :returns: Total quantity that hasn't been filled yet for all orders that were not filtered.
        """
        ...

    @overload
    def get_open_orders_remaining_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> float:
        """
        Gets the remaining quantity to be filled from open orders for a Symbol, i.e. order size minus quantity filled
        
        :param symbol: Symbol to get the remaining quantity of currently open orders
        :returns: Total quantity that hasn't been filled yet for orders matching the Symbol.
        """
        ...

    @overload
    def get_open_order_tickets(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Get an enumerable of open OrderTicket for the specified symbol
        
        :param symbol: The symbol for which to return the order tickets
        :returns: An enumerable of open OrderTicket.
        """
        ...

    @overload
    def get_open_order_tickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets an enumerable of opened OrderTicket matching the specified
        
        :param filter: The filter predicate used to find the required order tickets
        :returns: An enumerable of opened OrderTicket matching the specified.
        """
        ...

    @overload
    def get_open_order_tickets(self, filter: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets an enumerable of opened OrderTicket matching the specified 
        However, this method can be confused with the override that takes a Symbol as parameter. For this reason
        it first checks if it can convert the parameter into a symbol. If that conversion cannot be aplied it
        assumes the parameter is a Python function object and not a Python representation of a Symbol.
        
        :param filter: The Python function filter used to find the required order tickets
        :returns: An enumerable of opened OrderTicket matching the specified.
        """
        ...

    def get_order_by_id(self, order_id: int) -> QuantConnect.Orders.Order:
        """
        Get the order by its id
        
        :param order_id: Order id to fetch
        :returns: A clone of the order with the specified id, or null if no match is found.
        """
        ...

    @overload
    def get_orders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.Order]:
        """
        Gets all orders matching the specified filter. Specifying null will return an enumerable
        of all orders.
        
        :param filter: Delegate used to filter the orders
        :returns: All orders this order provider currently holds by the specified filter.
        """
        ...

    @overload
    def get_orders(self, filter: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.Order]:
        """
        Gets all orders matching the specified filter.
        
        :param filter: Python function object used to filter the orders
        :returns: All orders this order provider currently holds by the specified filter.
        """
        ...

    def get_orders_by_brokerage_id(self, brokerage_id: str) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets the order by its brokerage id
        
        :param brokerage_id: The brokerage id to fetch
        :returns: The first order matching the brokerage id, or null if no match is found.
        """
        ...

    def get_order_ticket(self, order_id: int) -> QuantConnect.Orders.OrderTicket:
        """
        Gets the order ticket for the specified order id. Returns null if not found
        
        :param order_id: The order's id
        :returns: The order ticket with the specified id, or null if not found.
        """
        ...

    @overload
    def get_order_tickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets an enumerable of OrderTicket matching the specified
        
        :param filter: The filter predicate used to find the required order tickets
        :returns: An enumerable of OrderTicket matching the specified.
        """
        ...

    @overload
    def get_order_tickets(self, filter: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets an enumerable of OrderTicket matching the specified
        
        :param filter: The Python function filter used to find the required order tickets
        :returns: An enumerable of OrderTicket matching the specified.
        """
        ...

    def process_request(self, request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Processes the order request
        
        :param request: The request to be processed
        :returns: The order ticket for the request.
        """
        ...

    def remove_order(self, order_id: int, tag: str = None) -> QuantConnect.Orders.OrderTicket:
        """
        Remove this order from outstanding queue: user is requesting a cancel.
        
        :param order_id: Specific order id to remove
        :param tag: Tag request
        """
        ...

    def set_live_mode(self, is_live_mode: bool) -> None:
        """
        Set live mode state of the algorithm
        
        :param is_live_mode: True, live mode is enabled
        """
        ...

    def set_order_id(self, request: QuantConnect.Orders.SubmitOrderRequest) -> None:
        """
        Sets the order id for the specified submit request
        
        :param request: Request to set the order id for
        """
        ...

    def set_order_processor(self, order_provider: QuantConnect.Securities.IOrderProcessor) -> None:
        """
        Sets the IOrderProvider used for fetching orders for the algorithm
        
        :param order_provider: The IOrderProvider to be used to manage fetching orders
        """
        ...

    def update_order(self, request: QuantConnect.Orders.UpdateOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Update an order yet to be filled such as stop or limit orders.
        
        :param request: Request detailing how the order should be updated
        """
        ...

    def wait_for_order(self, order_id: int) -> bool:
        """
        Wait for a specific order to be either Filled, Invalid or Canceled
        
        :param order_id: The id of the order to wait for
        :returns: True if we successfully wait for the fill, false if we were unable to wait. This may be because it is not a market order or because the timeout was reached.
        """
        ...


class IMarginCallModel(metaclass=abc.ABCMeta):
    """Represents the model responsible for picking which orders should be executed during a margin call"""

    def execute_margin_call(self, generated_margin_call_orders: System.Collections.Generic.IEnumerable[QuantConnect.Orders.SubmitOrderRequest]) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Executes synchronous orders to bring the account within margin requirements.
        
        :param generated_margin_call_orders: These are the margin call orders that were generated by individual security margin models.
        :returns: The list of orders that were actually executed.
        """
        ...

    def get_margin_call_orders(self, issue_margin_call_warning: typing.Optional[bool]) -> typing.Union[System.Collections.Generic.List[QuantConnect.Orders.SubmitOrderRequest], bool]:
        """
        Scan the portfolio and the updated data for a potential margin call situation which may get the holdings below zero!
        If there is a margin call, liquidate the portfolio immediately before the portfolio gets sub zero.
        
        :param issue_margin_call_warning: Set to true if a warning should be issued to the algorithm
        :returns: True for a margin call on the holdings.
        """
        ...


class ConvertibleCashAmount(System.Object):
    """A cash amount that can easily be converted into account currency"""

    @property
    def amount(self) -> float:
        """The amount"""
        ...

    @property
    def cash(self) -> QuantConnect.Securities.Cash:
        """The cash associated with the amount"""
        ...

    @property
    def in_account_currency(self) -> float:
        """The amount in account currency"""
        ...

    def __init__(self, amount: float, cash: QuantConnect.Securities.Cash) -> None:
        """Creates a new instance"""
        ...


class SecurityEventArgs(System.Object, metaclass=abc.ABCMeta):
    """Defines a base class for Security related events"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security related to this event"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes a new instance of the SecurityEventArgs class
        
        This method is protected.
        
        :param security: The security
        """
        ...


class SecurityHoldingQuantityChangedEventArgs(QuantConnect.Securities.SecurityEventArgs):
    """
    Event arguments for the SecurityHolding.QuantityChanged event.
    The event data contains the previous quantity/price. The current quantity/price
    can be accessed via the SecurityEventArgs.Security property
    """

    @property
    def previous_quantity(self) -> float:
        """Gets the holdings quantity before this change"""
        ...

    @property
    def previous_average_price(self) -> float:
        """Gets the average holdings price before this change"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, previousAveragePrice: float, previousQuantity: float) -> None:
        """
        Initializes a new instance of the SecurityHoldingQuantityChangedEventArgs class
        
        :param security: The security
        :param previousAveragePrice: The security's previous average holdings price
        :param previousQuantity: The security's previous holdings quantity
        """
        ...


class SecurityHolding(System.Object):
    """SecurityHolding is a base class for purchasing and holding a market item which manages the asset portfolio"""

    @property
    def quantity_changed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Securities.SecurityHoldingQuantityChangedEventArgs], None], None]:
        """Event raised each time the holdings quantity is changed."""
        ...

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """
        The security being held
        
        This property is protected.
        """
        ...

    @property
    def target(self) -> QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget:
        """Gets the current target holdings for this security"""
        ...

    @property.setter
    def target(self, value: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> None:
        ...

    @property
    def average_price(self) -> float:
        """Average price of the security holdings."""
        ...

    @property
    def quantity(self) -> float:
        """Quantity of the security held."""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol identifier of the underlying security."""
        ...

    @property
    def type(self) -> QuantConnect.SecurityType:
        """The security type of the symbol"""
        ...

    @property
    def leverage(self) -> float:
        """Leverage of the underlying security."""
        ...

    @property
    def holdings_cost(self) -> float:
        """Acquisition cost of the security total holdings in units of the account's currency."""
        ...

    @property
    def unlevered_holdings_cost(self) -> float:
        """Unlevered Acquisition cost of the security total holdings in units of the account's currency."""
        ...

    @property
    def price(self) -> float:
        """Current market price of the security."""
        ...

    @property
    def absolute_holdings_cost(self) -> float:
        """Absolute holdings cost for current holdings in units of the account's currency."""
        ...

    @property
    def unlevered_absolute_holdings_cost(self) -> float:
        """Unlevered absolute acquisition cost of the security total holdings in units of the account's currency."""
        ...

    @property
    def holdings_value(self) -> float:
        """Market value of our holdings in units of the account's currency."""
        ...

    @property
    def absolute_holdings_value(self) -> float:
        """Absolute of the market value of our holdings in units of the account's currency."""
        ...

    @property
    def hold_stock(self) -> bool:
        """Boolean flag indicating if we hold any of the security"""
        ...

    @property
    def invested(self) -> bool:
        """Boolean flag indicating if we hold any of the security"""
        ...

    @property
    def total_sale_volume(self) -> float:
        """The total transaction volume for this security since the algorithm started in units of the account's currency."""
        ...

    @property
    def total_fees(self) -> float:
        """Total fees for this company since the algorithm started in units of the account's currency."""
        ...

    @property
    def total_dividends(self) -> float:
        """Total dividends for this company since the algorithm started in units of the account's currency."""
        ...

    @property
    def is_long(self) -> bool:
        """Boolean flag indicating we have a net positive holding of the security."""
        ...

    @property
    def is_short(self) -> bool:
        """BBoolean flag indicating we have a net negative holding of the security."""
        ...

    @property
    def absolute_quantity(self) -> float:
        """Absolute quantity of holdings of this security"""
        ...

    @property
    def last_trade_profit(self) -> float:
        """Record of the closing profit from the last trade conducted in units of the account's currency."""
        ...

    @property
    def profit(self) -> float:
        """Calculate the total profit for this security in units of the account's currency."""
        ...

    @property
    def net_profit(self) -> float:
        """Return the net for this company measured by the profit less fees in units of the account's currency."""
        ...

    @property
    def unrealized_profit_percent(self) -> float:
        """Gets the unrealized profit as a percentage of holdings cost"""
        ...

    @property
    def unrealized_profit(self) -> float:
        """Unrealized profit of this security when absolute quantity held is more than zero in units of the account's currency."""
        ...

    @overload
    def __init__(self, security: QuantConnect.Securities.Security, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Create a new holding class instance setting the initial properties to $0.
        
        :param security: The security being held
        :param currencyConverter: A currency converter instance
        """
        ...

    @overload
    def __init__(self, holding: QuantConnect.Securities.SecurityHolding) -> None:
        """
        Create a new holding class instance copying the initial properties
        
        This method is protected.
        
        :param holding: The security being held
        """
        ...

    def add_new_dividend(self, dividend: float) -> None:
        """Adds a new dividend payment to the running total dividend in units of the account's currency."""
        ...

    def add_new_fee(self, new_fee: float) -> None:
        """Adds a fee to the running total of total fees in units of the account's currency."""
        ...

    def add_new_profit(self, profit_loss: float) -> None:
        """
        Adds a profit record to the running total of profit in units of the account's currency.
        
        :param profit_loss: The cash change in portfolio from closing a position
        """
        ...

    def add_new_sale(self, sale_value: float) -> None:
        """Adds a new sale value to the running total trading volume in units of the account's currency."""
        ...

    @overload
    def get_quantity_value(self, quantity: float) -> QuantConnect.Securities.ConvertibleCashAmount:
        """
        Gets the total value of the specified  of shares of this security
        in the account currency
        
        :param quantity: The quantity of shares
        :returns: The value of the quantity of shares in the account currency.
        """
        ...

    @overload
    def get_quantity_value(self, quantity: float, price: float) -> QuantConnect.Securities.ConvertibleCashAmount:
        """
        Gets the total value of the specified  of shares of this security
        in the account currency
        
        :param quantity: The quantity of shares
        :param price: The current price
        :returns: The value of the quantity of shares in the account currency.
        """
        ...

    def on_quantity_changed(self, previous_average_price: float, previous_quantity: float) -> None:
        """
        Event invocator for the QuantityChanged event
        
        This method is protected.
        """
        ...

    @overload
    def set_holdings(self, average_price: float, quantity: int) -> None:
        """Set the quantity of holdings and their average price after processing a portfolio fill."""
        ...

    @overload
    def set_holdings(self, average_price: float, quantity: float) -> None:
        """Set the quantity of holdings and their average price after processing a portfolio fill."""
        ...

    def set_last_trade_profit(self, last_trade_profit: float) -> None:
        """
        Set the last trade profit for this security from a Portfolio.ProcessFill call in units of the account's currency.
        
        :param last_trade_profit: Value of the last trade profit
        """
        ...

    def to_string(self) -> str:
        """Writes out the properties of this instance to string"""
        ...

    def total_close_profit(self, include_fees: bool = True, exit_price: typing.Optional[float] = None, entry_price: typing.Optional[float] = None, quantity: typing.Optional[float] = None) -> float:
        """Profit if we closed the holdings right now including the approximate fees in units of the account's currency."""
        ...

    def update_market_price(self, closing_price: float) -> None:
        """
        Update local copy of closing price value.
        
        :param closing_price: Price of the underlying asset to be used for calculating market price / portfolio value
        """
        ...


class HasSufficientBuyingPowerForOrderResult(System.Object):
    """Contains the information returned by IBuyingPowerModel.HasSufficientBuyingPowerForOrder"""

    @property
    def is_sufficient(self) -> bool:
        """Gets true if there is sufficient buying power to execute an order"""
        ...

    @property
    def reason(self) -> str:
        """Gets the reason for insufficient buying power to execute an order"""
        ...

    def __init__(self, isSufficient: bool, reason: str = None) -> None:
        """
        Initializes a new instance of the HasSufficientBuyingPowerForOrderResult class
        
        :param isSufficient: True if the order can be executed
        :param reason: The reason for insufficient buying power
        """
        ...


class SecurityPortfolioManager(QuantConnect.ExtendedDictionary[QuantConnect.Securities.SecurityHolding], System.Collections.Generic.IDictionary[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding], QuantConnect.Securities.ISecurityProvider, typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]]):
    """
    Portfolio manager class groups popular properties and makes them accessible through one interface.
    It also provide indexing by the vehicle symbol to get the Security.Holding objects.
    """

    @property
    def securities(self) -> QuantConnect.Securities.SecurityManager:
        """Local access to the securities collection for the portfolio summation."""
        ...

    @property
    def transactions(self) -> QuantConnect.Securities.SecurityTransactionManager:
        """Local access to the transactions collection for the portfolio summation and updates."""
        ...

    @property
    def positions(self) -> QuantConnect.Securities.Positions.SecurityPositionGroupModel:
        """Local access to the position manager"""
        ...

    @property.setter
    def positions(self, value: QuantConnect.Securities.Positions.SecurityPositionGroupModel) -> None:
        ...

    @property
    def cash_book(self) -> QuantConnect.Securities.CashBook:
        """Gets the cash book that keeps track of all currency holdings (only settled cash)"""
        ...

    @property
    def unsettled_cash_book(self) -> QuantConnect.Securities.CashBook:
        """Gets the cash book that keeps track of all currency holdings (only unsettled cash)"""
        ...

    @property
    def count(self) -> int:
        """Count the securities objects in the portfolio."""
        ...

    @property
    def is_read_only(self) -> bool:
        """Check if the underlying securities array is read only."""
        ...

    @property
    def get_keys(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets an System.Collections.Generic.ICollection{T} containing the Symbol objects of the System.Collections.Generic.IDictionary{TKey, TValue}.
        
        This property is protected.
        """
        ...

    @property
    def get_values(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.SecurityHolding]:
        """
        Gets an System.Collections.Generic.ICollection{T} containing the values in the System.Collections.Generic.IDictionary{TKey, TValue}.
        
        This property is protected.
        """
        ...

    @property
    def keys(self) -> System.Collections.Generic.ICollection[QuantConnect.Symbol]:
        """Symbol keys collection of the underlying assets in the portfolio."""
        ...

    @property
    def values(self) -> System.Collections.Generic.ICollection[QuantConnect.Securities.SecurityHolding]:
        """Collection of securities objects in the portfolio."""
        ...

    @property
    def cash(self) -> float:
        """Sum of all currencies in account in US dollars (only settled cash)"""
        ...

    @property
    def unsettled_cash(self) -> float:
        """Sum of all currencies in account in US dollars (only unsettled cash)"""
        ...

    @property
    def total_unlevered_absolute_holdings_cost(self) -> float:
        """Absolute value of cash discounted from our total cash by the holdings we own."""
        ...

    @property
    def total_absolute_holdings_cost(self) -> float:
        """
        Gets the total absolute holdings cost of the portfolio. This sums up the individual
        absolute cost of each holding
        """
        ...

    @property
    def total_holdings_value(self) -> float:
        """Absolute sum the individual items in portfolio."""
        ...

    @property
    def hold_stock(self) -> bool:
        """Boolean flag indicating we have any holdings in the portfolio."""
        ...

    @property
    def invested(self) -> bool:
        """Alias for HoldStock. Check if we have any holdings."""
        ...

    @property
    def total_unrealised_profit(self) -> float:
        """Get the total unrealised profit in our portfolio from the individual security unrealized profits."""
        ...

    @property
    def total_unrealized_profit(self) -> float:
        """Get the total unrealised profit in our portfolio from the individual security unrealized profits."""
        ...

    @property
    def total_portfolio_value(self) -> float:
        """Total portfolio value if we sold all holdings at current market rates."""
        ...

    @property
    def total_portfolio_value_less_free_buffer(self) -> float:
        """
        Returns the adjusted total portfolio value removing the free amount
        If the IAlgorithmSettings.FreePortfolioValue has not been set, the free amount will have a trailing behavior and be updated when requested
        """
        ...

    @property
    def total_fees(self) -> float:
        """Total fees paid during the algorithm operation across all securities in portfolio."""
        ...

    @property
    def total_profit(self) -> float:
        """Sum of all gross profit across all securities in portfolio and dividend payments."""
        ...

    @property
    def total_net_profit(self) -> float:
        """Sum of all net profit across all securities in portfolio and dividend payments."""
        ...

    @property
    def total_sale_volume(self) -> float:
        """Total sale volume since the start of algorithm operations."""
        ...

    @property
    def total_margin_used(self) -> float:
        """Gets the total margin used across all securities in the account's currency"""
        ...

    @property
    def margin_remaining(self) -> float:
        """Gets the remaining margin on the account in the account's currency"""
        ...

    @property
    def margin_call_model(self) -> QuantConnect.Securities.IMarginCallModel:
        """
        Gets or sets the MarginCallModel for the portfolio. This
        is used to executed margin call orders.
        """
        ...

    @property.setter
    def margin_call_model(self, value: QuantConnect.Securities.IMarginCallModel) -> None:
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.SecurityHolding:
        """
        Indexer for the PortfolioManager class to access the underlying security holdings objects.
        
        :param symbol: Symbol object indexer
        :returns: SecurityHolding class from the algorithm securities.
        """
        ...

    def __init__(self, securityManager: QuantConnect.Securities.SecurityManager, transactions: QuantConnect.Securities.SecurityTransactionManager, algorithmSettings: QuantConnect.Interfaces.IAlgorithmSettings, defaultOrderProperties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """Initialise security portfolio manager."""
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Securities.SecurityHolding) -> None:
        """
        Indexer for the PortfolioManager class to access the underlying security holdings objects.
        
        :param symbol: Symbol object indexer
        :returns: SecurityHolding class from the algorithm securities.
        """
        ...

    @overload
    def add(self, symbol: typing.Union[QuantConnect.Symbol, str], holding: QuantConnect.Securities.SecurityHolding) -> None:
        """
        Add a new securities string-security to the portfolio.
        
        :param symbol: Symbol of dictionary
        :param holding: SecurityHoldings object
        """
        ...

    @overload
    def add(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]) -> None:
        """
        Add a new securities key value pair to the portfolio.
        
        :param pair: Key value pair of dictionary
        """
        ...

    def add_transaction_record(self, time: typing.Union[datetime.datetime, datetime.date], transaction_profit_loss: float, is_win: bool) -> None:
        """
        Record the transaction value and time in a list to later be processed for statistics creation.
        
        :param time: Time of order processed
        :param transaction_profit_loss: Profit Loss.
        :param is_win: Whether the transaction is a win. For options exercise, this might not depend only on the profit/loss value
        """
        ...

    def apply_dividend(self, dividend: QuantConnect.Data.Market.Dividend, live_mode: bool, mode: QuantConnect.DataNormalizationMode) -> None:
        """
        Applies a dividend to the portfolio
        
        :param dividend: The dividend to be applied
        :param live_mode: True if live mode, false for backtest
        :param mode: The DataNormalizationMode for this security
        """
        ...

    def apply_split(self, split: QuantConnect.Data.Market.Split, security: QuantConnect.Securities.Security, live_mode: bool, mode: QuantConnect.DataNormalizationMode) -> None:
        """
        Applies a split to the portfolio
        
        :param split: The split to be applied
        :param security: The security the split will be applied to
        :param live_mode: True if live mode, false for backtest
        :param mode: The DataNormalizationMode for this security
        """
        ...

    def clear(self) -> None:
        """Clear the portfolio of securities objects."""
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]) -> bool:
        """
        Check if the key-value pair is in the portfolio.
        
        :param pair: Pair we're searching for
        :returns: True if we have this object.
        """
        ...

    def contains_key(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Check if the portfolio contains this symbol string.
        
        :param symbol: String search symbol for the security
        :returns: Boolean true if portfolio contains this symbol.
        """
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]], index: int) -> None:
        """
        Copy contents of the portfolio collection to a new destination.
        
        :param array: Destination array
        :param index: Position in array to start copying
        """
        ...

    def get_buying_power(self, symbol: typing.Union[QuantConnect.Symbol, str], direction: QuantConnect.Orders.OrderDirection = ...) -> float:
        """
        Gets the margin available for trading a specific symbol in a specific direction.
        Alias for GetMarginRemaining(Symbol, OrderDirection)
        
        :param symbol: The symbol to compute margin remaining for
        :param direction: The order/trading direction
        :returns: The maximum order size that is currently executable in the specified direction.
        """
        ...

    @overload
    def get_margin_remaining(self, total_portfolio_value: float) -> float:
        """
        Gets the remaining margin on the account in the account's currency
        for the given total portfolio value
        
        :param total_portfolio_value: The total portfolio value TotalPortfolioValue
        """
        ...

    @overload
    def get_margin_remaining(self, symbol: typing.Union[QuantConnect.Symbol, str], direction: QuantConnect.Orders.OrderDirection = ...) -> float:
        ...

    def has_sufficient_buying_power_for_order(self, orders: System.Collections.Generic.List[QuantConnect.Orders.Order]) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Will determine if the algorithms portfolio has enough buying power to fill the given orders
        
        :param orders: The orders to check
        :returns: True if the algorithm has enough buying power available.
        """
        ...

    def invalidate_total_portfolio_value(self) -> None:
        """
        Will flag the current TotalPortfolioValue as invalid
        so it is recalculated when gotten
        """
        ...

    def log_margin_information(self, order_request: QuantConnect.Orders.OrderRequest = None) -> None:
        """Logs margin information for debugging"""
        ...

    def process_fills(self, fills: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]) -> None:
        """Calculate the new average price after processing a list of partial/complete order fill events."""
        ...

    @overload
    def remove(self, pair: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Securities.SecurityHolding]) -> bool:
        """
        Remove this keyvalue pair from the portfolio.
        
        :param pair: Key value pair of dictionary
        """
        ...

    @overload
    def remove(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Remove this symbol from the portfolio.
        
        :param symbol: Symbol of dictionary
        """
        ...

    def set_account_currency(self, account_currency: str, starting_cash: typing.Optional[float] = None) -> None:
        """
        Sets the account currency cash symbol this algorithm is to manage, as well
        as the starting cash in this currency if given
        
        :param account_currency: The account currency cash symbol to set
        :param starting_cash: The account currency starting cash to set
        """
        ...

    @overload
    def set_cash(self, cash: float) -> None:
        """
        Set the account currency cash this algorithm is to manage.
        
        :param cash: Decimal cash value of portfolio
        """
        ...

    @overload
    def set_cash(self, symbol: str, cash: float, conversion_rate: float) -> None:
        """
        Set the cash for the specified symbol
        
        :param symbol: The cash symbol to set
        :param cash: Decimal cash value of portfolio
        :param conversion_rate: The current conversion rate for the
        """
        ...

    @overload
    def set_margin_call_model(self, margin_call_model: QuantConnect.Securities.IMarginCallModel) -> None:
        """
        Sets the margin call model
        
        :param margin_call_model: Model that represents a portfolio's model to executed margin call orders.
        """
        ...

    @overload
    def set_margin_call_model(self, py_object: typing.Any) -> None:
        """
        Sets the margin call model
        
        :param py_object: Model that represents a portfolio's model to executed margin call orders.
        """
        ...

    def set_positions(self, position_group_model: QuantConnect.Securities.Positions.SecurityPositionGroupModel) -> None:
        """
        Will set the security position group model to use
        
        :param position_group_model: The position group model instance
        """
        ...

    def try_get_value(self, symbol: typing.Union[QuantConnect.Symbol, str], holding: typing.Optional[QuantConnect.Securities.SecurityHolding]) -> typing.Union[bool, QuantConnect.Securities.SecurityHolding]:
        """
        Attempt to get the value of the securities holding class if this symbol exists.
        
        :param symbol: String search symbol
        :param holding: Holdings object of this security
        :returns: Boolean true if successful locating and setting the holdings object.
        """
        ...


class GetMaximumOrderQuantityForTargetBuyingPowerParameters(System.Object):
    """Defines the parameters for IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio"""
        ...

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def target_buying_power(self) -> float:
        """Gets the target signed percentage buying power"""
        ...

    @property
    def silence_non_error_reasons(self) -> bool:
        """
        True enables the IBuyingPowerModel to skip setting GetMaximumOrderQuantityResult.Reason
        for non error situations, for performance
        """
        ...

    @property
    def minimum_order_margin_portfolio_percentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, targetBuyingPower: float, minimumOrderMarginPortfolioPercentage: float, silenceNonErrorReasons: bool = False) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityForTargetBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio
        :param security: The security
        :param targetBuyingPower: The target percentage buying power
        :param minimumOrderMarginPortfolioPercentage: Configurable minimum order margin portfolio percentage to ignore orders with unrealistic small sizes
        :param silenceNonErrorReasons: True will not return GetMaximumOrderQuantityResult.Reason set for non error situation, this is for performance
        """
        ...


class IDerivativeSecurity(metaclass=abc.ABCMeta):
    """Defines a security as a derivative of another security"""

    @property
    @abc.abstractmethod
    def underlying(self) -> QuantConnect.Securities.Security:
        """Gets or sets the underlying security for the derivative"""
        ...

    @property.setter
    def underlying(self, value: QuantConnect.Securities.Security) -> None:
        ...


class ApplyFundsSettlementModelParameters(System.Object):
    """Helper parameters class for ISettlementModel.ApplyFunds(ApplyFundsSettlementModelParameters)"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """The algorithm portfolio instance"""
        ...

    @property.setter
    def portfolio(self, value: QuantConnect.Securities.SecurityPortfolioManager) -> None:
        ...

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """The associated security type"""
        ...

    @property.setter
    def security(self, value: QuantConnect.Securities.Security) -> None:
        ...

    @property
    def utc_time(self) -> datetime.datetime:
        """The current Utc time"""
        ...

    @property.setter
    def utc_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def cash_amount(self) -> QuantConnect.Securities.CashAmount:
        """The funds to apply"""
        ...

    @property.setter
    def cash_amount(self, value: QuantConnect.Securities.CashAmount) -> None:
        ...

    @property
    def fill(self) -> QuantConnect.Orders.OrderEvent:
        """The associated fill event"""
        ...

    @property.setter
    def fill(self, value: QuantConnect.Orders.OrderEvent) -> None:
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, applicationTimeUtc: typing.Union[datetime.datetime, datetime.date], cashAmount: QuantConnect.Securities.CashAmount, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Creates a new instance
        
        :param portfolio: The algorithm's portfolio
        :param security: The fill's security
        :param applicationTimeUtc: The fill time (in UTC)
        :param cashAmount: The amount to settle
        :param fill: The associated fill
        """
        ...


class FuncSecuritySeeder(System.Object, QuantConnect.Securities.ISecuritySeeder):
    """Seed a security price from a history function"""

    @overload
    def __init__(self, seedFunction: typing.Any) -> None:
        """
        Constructor that takes as a parameter the security used to seed the price
        
        :param seedFunction: The seed function to use
        """
        ...

    @overload
    def __init__(self, seedFunction: typing.Callable[[QuantConnect.Securities.Security], QuantConnect.Data.BaseData]) -> None:
        """
        Constructor that takes as a parameter the security used to seed the price
        
        :param seedFunction: The seed function to use
        """
        ...

    @overload
    def __init__(self, seedFunction: typing.Callable[[QuantConnect.Securities.Security], System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]]) -> None:
        """
        Constructor that takes as a parameter the security used to seed the price
        
        :param seedFunction: The seed function to use
        """
        ...

    def seed_security(self, security: QuantConnect.Securities.Security) -> bool:
        """
        Seed the security
        
        :param security: Security being seeded
        :returns: true if the security was seeded, false otherwise.
        """
        ...


class GetMaximumOrderQuantityForDeltaBuyingPowerParameters(System.Object):
    """Defines the parameters for IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio"""
        ...

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def delta_buying_power(self) -> float:
        """The delta buying power."""
        ...

    @property
    def silence_non_error_reasons(self) -> bool:
        """
        True enables the IBuyingPowerModel to skip setting GetMaximumOrderQuantityResult.Reason
        for non error situations, for performance
        """
        ...

    @property
    def minimum_order_margin_portfolio_percentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, deltaBuyingPower: float, minimumOrderMarginPortfolioPercentage: float, silenceNonErrorReasons: bool = False) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityForDeltaBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio
        :param security: The security
        :param deltaBuyingPower: The delta buying power to apply. Sign defines the position side to apply the delta
        :param minimumOrderMarginPortfolioPercentage: Configurable minimum order margin portfolio percentage to ignore orders with unrealistic small sizes
        :param silenceNonErrorReasons: True will not return GetMaximumOrderQuantityResult.Reason set for non error situation, this is for performance
        """
        ...


class ScanSettlementModelParameters(System.Object):
    """The settlement model ISettlementModel.Scan(ScanSettlementModelParameters) parameters"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """The algorithm portfolio instance"""
        ...

    @property.setter
    def portfolio(self, value: QuantConnect.Securities.SecurityPortfolioManager) -> None:
        ...

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """The associated security type"""
        ...

    @property.setter
    def security(self, value: QuantConnect.Securities.Security) -> None:
        ...

    @property
    def utc_time(self) -> datetime.datetime:
        """The current Utc time"""
        ...

    @property.setter
    def utc_time(self, value: datetime.datetime) -> None:
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, timeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Creates a new instance
        
        :param portfolio: The algorithm portfolio
        :param security: The associated security type
        :param timeUtc: The current utc time
        """
        ...


class ISettlementModel(metaclass=abc.ABCMeta):
    """Represents the model responsible for applying cash settlement rules"""

    def apply_funds(self, apply_funds_parameters: QuantConnect.Securities.ApplyFundsSettlementModelParameters) -> None:
        """
        Applies cash settlement rules
        
        :param apply_funds_parameters: The funds application parameters
        """
        ...

    def get_unsettled_cash(self) -> QuantConnect.Securities.CashAmount:
        """Gets the unsettled cash amount for the security"""
        ...

    def scan(self, settlement_parameters: QuantConnect.Securities.ScanSettlementModelParameters) -> None:
        """
        Scan for pending settlements
        
        :param settlement_parameters: The settlement parameters
        """
        ...


class ImmediateSettlementModel(System.Object, QuantConnect.Securities.ISettlementModel):
    """Represents the model responsible for applying cash settlement rules"""

    def apply_funds(self, apply_funds_parameters: QuantConnect.Securities.ApplyFundsSettlementModelParameters) -> None:
        """
        Applies cash settlement rules
        
        :param apply_funds_parameters: The funds application parameters
        """
        ...

    def get_unsettled_cash(self) -> QuantConnect.Securities.CashAmount:
        """Gets the unsettled cash amount for the security"""
        ...

    def scan(self, settlement_parameters: QuantConnect.Securities.ScanSettlementModelParameters) -> None:
        """
        Scan for pending settlements
        
        :param settlement_parameters: The settlement parameters
        """
        ...


class MarginInterestRateParameters(System.Object):
    """Defines the parameters for IMarginInterestRateModel.ApplyMarginInterestRate"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """The target security"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """The current UTC time"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance"""
        ...


class IMarginInterestRateModel(metaclass=abc.ABCMeta):
    """The responsability of this model is to apply margin interest rate cash flows to the portfolio"""

    def apply_margin_interest_rate(self, margin_interest_rate_parameters: QuantConnect.Securities.MarginInterestRateParameters) -> None:
        """
        Apply margin interest rates to the portfolio
        
        :param margin_interest_rate_parameters: The parameters to use
        """
        ...


class MarginInterestRateModel(System.Object):
    """Provides access to a null implementation for IMarginInterestRateModel"""

    NULL: QuantConnect.Securities.IMarginInterestRateModel = ...
    """The null margin interest rate model"""


class MaintenanceMargin(System.Object):
    """Result type for IBuyingPowerModel.GetMaintenanceMargin"""

    ZERO: QuantConnect.Securities.MaintenanceMargin
    """Gets an instance of MaintenanceMargin with zero values."""

    @property
    def value(self) -> float:
        """The maintenance margin value in account currency"""
        ...

    def __init__(self, value: float) -> None:
        """
        Initializes a new instance of the MaintenanceMargin class
        
        :param value: The maintenance margin
        """
        ...


class InitialMargin(System.Object):
    """
    Result type for IBuyingPowerModel.GetInitialMarginRequirement
    and IBuyingPowerModel.GetInitialMarginRequiredForOrder
    """

    ZERO: QuantConnect.Securities.InitialMargin
    """Gets an instance of InitialMargin with zero values"""

    @property
    def value(self) -> float:
        """The initial margin value in account currency"""
        ...

    def __init__(self, value: float) -> None:
        """
        Initializes a new instance of the InitialMargin class
        
        :param value: The initial margin
        """
        ...


class InitialMarginParameters(System.Object):
    """Parameters for IBuyingPowerModel.GetInitialMarginRequirement"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def quantity(self) -> float:
        """Gets the quantity"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, quantity: float) -> None:
        """
        Initializes a new instance of the InitialMarginParameters class
        
        :param security: The security
        :param quantity: The quantity
        """
        ...

    def for_underlying(self) -> QuantConnect.Securities.InitialMarginParameters:
        """Creates a new instance of InitialMarginParameters for the security's underlying"""
        ...


class InitialMarginRequiredForOrderParameters(System.Object):
    """Defines the parameters for BuyingPowerModel.GetInitialMarginRequiredForOrder"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    @property
    def currency_converter(self) -> QuantConnect.Securities.ICurrencyConverter:
        """Gets the currency converter"""
        ...

    def __init__(self, currencyConverter: QuantConnect.Securities.ICurrencyConverter, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the InitialMarginRequiredForOrderParameters class
        
        :param currencyConverter: The currency converter
        :param security: The security
        :param order: The order
        """
        ...


class HasSufficientBuyingPowerForOrderParameters(System.Object):
    """Defines the parameters for IBuyingPowerModel.HasSufficientBuyingPowerForOrder"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio"""
        ...

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the HasSufficientBuyingPowerForOrderParameters class
        
        :param portfolio: The algorithm's portfolio
        :param security: The security
        :param order: The order
        """
        ...

    def for_underlying(self, order: QuantConnect.Orders.Order) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters:
        """
        Creates a new HasSufficientBuyingPowerForOrderParameters targeting the security's underlying.
        If the security does not implement IDerivativeSecurity then an InvalidCastException
        will be thrown. If the order's symbol does not match the underlying then an ArgumentException will
        be thrown.
        
        :param order: The new order targeting the underlying
        :returns: New parameters instance suitable for invoking the sufficient capital method for the underlying security.
        """
        ...

    @overload
    def insufficient(self, reason: str) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there is insufficient buying power for the contemplated order"""
        ...

    @overload
    def insufficient(self, reason: System.FormattableString) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there is insufficient buying power for the contemplated order"""
        ...

    def sufficient(self) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there is sufficient buying power for the contemplated order"""
        ...


class GetMaximumOrderQuantityResult(System.Object):
    """
    Contains the information returned by IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower
    and  IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower
    """

    @property
    def quantity(self) -> float:
        """Returns the maximum quantity for the order"""
        ...

    @property
    def reason(self) -> str:
        """Returns the reason for which the maximum order quantity is zero"""
        ...

    @property
    def is_error(self) -> bool:
        """Returns true if the zero order quantity is an error condition and will be shown to the user."""
        ...

    @overload
    def __init__(self, quantity: float, reason: str = None) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityResult class
        
        :param quantity: Returns the maximum quantity for the order
        :param reason: The reason for which the maximum order quantity is zero
        """
        ...

    @overload
    def __init__(self, quantity: float, reason: str, isError: bool = True) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityResult class
        
        :param quantity: Returns the maximum quantity for the order
        :param reason: The reason for which the maximum order quantity is zero
        :param isError: True if the zero order quantity is an error condition
        """
        ...


class BuyingPower(System.Object):
    """Defines the result for IBuyingPowerModel.GetBuyingPower"""

    @property
    def value(self) -> float:
        """Gets the buying power"""
        ...

    def __init__(self, buyingPower: float) -> None:
        """
        Initializes a new instance of the BuyingPower class
        
        :param buyingPower: The buying power
        """
        ...


class BuyingPowerParameters(System.Object):
    """Defines the parameters for IBuyingPowerModel.GetBuyingPower"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio"""
        ...

    @property
    def direction(self) -> QuantConnect.Orders.OrderDirection:
        """Gets the direction in which buying power is to be computed"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> None:
        """
        Initializes a new instance of the BuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio
        :param security: The security
        :param direction: The direction to compute buying power in
        """
        ...

    def result(self, buying_power: float, currency: str) -> QuantConnect.Securities.BuyingPower:
        """
        Creates the result using the specified buying power
        
        :param buying_power: The buying power
        :param currency: The units the buying power is denominated in
        :returns: The buying power.
        """
        ...

    def result_in_account_currency(self, buying_power: float) -> QuantConnect.Securities.BuyingPower:
        """
        Creates the result using the specified buying power in units of the account currency
        
        :param buying_power: The buying power
        :returns: The buying power.
        """
        ...


class IBuyingPowerModel(metaclass=abc.ABCMeta):
    """Represents a security's model of buying power"""

    def get_buying_power(self, parameters: QuantConnect.Securities.BuyingPowerParameters) -> QuantConnect.Securities.BuyingPower:
        """
        Gets the buying power available for a trade
        
        :param parameters: A parameters object containing the algorithm's portfolio, security, and order direction
        :returns: The buying power available for the trade.
        """
        ...

    def get_initial_margin_required_for_order(self, parameters: QuantConnect.Securities.InitialMarginRequiredForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity
        :returns: The initial margin required for the provided security and quantity.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the current leverage of the security
        
        :param security: The security to get leverage for
        :returns: The current leverage in the security.
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security and holdings quantity/cost/value
        :returns: The maintenance margin required for the provided holdings quantity/cost/value.
        """
        ...

    def get_maximum_order_quantity_for_delta_buying_power(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a delta in the buying power used by a security.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the security and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_maximum_order_quantity_for_target_buying_power(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a position with a given buying power percentage.
        Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the security and the target signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_reserved_buying_power_for_position(self, parameters: QuantConnect.Securities.ReservedBuyingPowerForPositionParameters) -> QuantConnect.Securities.ReservedBuyingPowerForPosition:
        """
        Gets the amount of buying power reserved to maintain the specified position
        
        :param parameters: A parameters object containing the security
        :returns: The reserved buying power in account currency.
        """
        ...

    def has_sufficient_buying_power_for_order(self, parameters: QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power to execute this order.
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: Returns buying power information for an order.
        """
        ...

    def set_leverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, equities
        
        :param security: The security to set leverage for
        :param leverage: The new leverage
        """
        ...


class BuyingPowerModel(System.Object, QuantConnect.Securities.IBuyingPowerModel):
    """Provides a base class for all buying power models"""

    NULL: QuantConnect.Securities.IBuyingPowerModel = ...
    """
    Gets an implementation of IBuyingPowerModel that
    does not check for sufficient buying power
    """

    @property
    def required_free_buying_power_percent(self) -> float:
        """
        The percentage used to determine the required unused buying power for the account.
        
        This property is protected.
        """
        ...

    @property.setter
    def required_free_buying_power_percent(self, value: float) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the BuyingPowerModel with no leverage (1x)"""
        ...

    @overload
    def __init__(self, initialMarginRequirement: float, maintenanceMarginRequirement: float, requiredFreeBuyingPowerPercent: float) -> None:
        """
        Initializes a new instance of the BuyingPowerModel
        
        :param initialMarginRequirement: The percentage of an order's absolute cost that must be held in free cash in order to place the order
        :param maintenanceMarginRequirement: The percentage of the holding's absolute cost that must be held in free cash in order to avoid a margin call
        :param requiredFreeBuyingPowerPercent: The percentage used to determine the required unused buying power for the account.
        """
        ...

    @overload
    def __init__(self, leverage: float, requiredFreeBuyingPowerPercent: float = 0) -> None:
        """
        Initializes a new instance of the BuyingPowerModel
        
        :param leverage: The leverage
        :param requiredFreeBuyingPowerPercent: The percentage used to determine the required unused buying power for the account.
        """
        ...

    def get_amount_to_order(self, security: QuantConnect.Securities.Security, target_margin: float, margin_for_one_unit: float, final_margin: typing.Optional[float]) -> typing.Union[float, float]:
        """
        Helper function that determines the amount to order to get to a given target safely.
        Meaning it will either be at or just below target always.
        
        :param security: Security we are to determine order size for
        :param target_margin: Target margin allocated
        :param margin_for_one_unit: Margin requirement for one unit; used in our initial order guess
        :param final_margin: Output the final margin allocated to this security
        :returns: The size of the order to get safely to our target.
        """
        ...

    def get_buying_power(self, parameters: QuantConnect.Securities.BuyingPowerParameters) -> QuantConnect.Securities.BuyingPower:
        """
        Gets the buying power available for a trade
        
        :param parameters: A parameters object containing the algorithm's portfolio, security, and order direction
        :returns: The buying power available for the trade.
        """
        ...

    def get_initial_margin_required_for_order(self, parameters: QuantConnect.Securities.InitialMarginRequiredForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity of shares
        :returns: The initial margin required for the provided security and quantity.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the current leverage of the security
        
        :param security: The security to get leverage for
        :returns: The current leverage in the security.
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security and holdings quantity/cost/value
        :returns: The maintenance margin required for the provided holdings quantity/cost/value.
        """
        ...

    def get_margin_remaining(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> float:
        """
        Gets the margin cash available for a trade
        
        This method is protected.
        
        :param portfolio: The algorithm's portfolio
        :param security: The security to be traded
        :param direction: The direction of the trade
        :returns: The margin available for the trade.
        """
        ...

    def get_maximum_order_quantity_for_delta_buying_power(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a delta in the buying power used by a security.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the security and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_maximum_order_quantity_for_target_buying_power(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a position with a given buying power percentage.
        Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the security and the target signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_reserved_buying_power_for_position(self, parameters: QuantConnect.Securities.ReservedBuyingPowerForPositionParameters) -> QuantConnect.Securities.ReservedBuyingPowerForPosition:
        """
        Gets the amount of buying power reserved to maintain the specified position
        
        :param parameters: A parameters object containing the security
        :returns: The reserved buying power in account currency.
        """
        ...

    def has_sufficient_buying_power_for_order(self, parameters: QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power to execute this order.
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: Returns buying power information for an order.
        """
        ...

    def set_leverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, equities
        
        :param leverage: The new leverage
        """
        ...


class ConstantBuyingPowerModel(QuantConnect.Securities.BuyingPowerModel):
    """
    Provides an implementation of IBuyingPowerModel that uses an absurdly low margin
    requirement to ensure all orders have sufficient margin provided the portfolio is not underwater.
    """

    def __init__(self, marginRequiredPerUnitInAccountCurrency: float) -> None:
        """
        Initializes a new instance of the ConstantBuyingPowerModel class
        
        :param marginRequiredPerUnitInAccountCurrency: The constant amount of margin required per single unit of an asset. Each unit is defined as a quantity of 1 and NOT based on the lot size.
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity of shares
        :returns: The initial margin required for the provided security and quantity.
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the provided holdings quantity/cost/value.
        """
        ...

    def set_leverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, equities
        
        :param leverage: The new leverage
        """
        ...


class IBaseCurrencySymbol(metaclass=abc.ABCMeta):
    """Interface for various currency symbols"""

    @property
    @abc.abstractmethod
    def base_currency(self) -> QuantConnect.Securities.Cash:
        """Gets the currency acquired by going long this currency pair"""
        ...


class ISecurityPortfolioModel(metaclass=abc.ABCMeta):
    """Performs order fill application to portfolio"""

    def process_fill(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Performs application of an OrderEvent to the portfolio
        
        :param portfolio: The algorithm's portfolio
        :param security: The fill's security
        :param fill: The order event fill object to be applied
        """
        ...


class SecurityPortfolioModel(System.Object, QuantConnect.Securities.ISecurityPortfolioModel):
    """
    Provides a default implementation of ISecurityPortfolioModel that simply
    applies the fills to the algorithm's portfolio. This implementation is intended to
    handle all security types.
    """

    def process_close_trade_profit(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> QuantConnect.Securities.ConvertibleCashAmount:
        """
        Helper method to determine the close trade profit
        
        This method is protected.
        """
        ...

    def process_fill(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Performs application of an OrderEvent to the portfolio
        
        :param portfolio: The algorithm's portfolio
        :param security: The fill's security
        :param fill: The order event fill object to be applied
        """
        ...


class IDerivativeSecurityFilterUniverse(typing.Generic[QuantConnect_Securities_IDerivativeSecurityFilterUniverse_T], metaclass=abc.ABCMeta):
    """Represents derivative symbols universe used in filtering."""


class SecurityDefinitionSymbolResolver(System.Object):
    """
    Resolves standardized security definitions such as FIGI, CUSIP, ISIN, SEDOL into
    a properly mapped Lean Symbol, and vice-versa.
    """

    @overload
    def cik(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> typing.Optional[int]:
        """
        Get's the CIK value associated with the given Symbol
        
        :param symbol: The Lean Symbol
        :returns: The Central Index Key number (CIK) corresponding to the given Lean Symbol if any, else null.
        """
        ...

    @overload
    def cik(self, cik: int, trading_date: typing.Union[datetime.datetime, datetime.date]) -> typing.List[QuantConnect.Symbol]:
        """
        Converts CIK into a Lean Symbol array
        
        :param cik: The Central Index Key (CIK) of a company
        :param trading_date: The date that the stock was trading at with the CIK provided. This is used to get the ticker of the symbol on this date.
        :returns: The Lean Symbols corresponding to the CIK on the trading date provided.
        """
        ...

    @overload
    def composite_figi(self, composite_figi: str, trading_date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Symbol:
        """
        Converts an asset's composite FIGI into a Lean Symbol
        
        :param composite_figi: The composite Financial Instrument Global Identifier (FIGI) of a security
        :param trading_date: The date that the stock was trading at with the composite FIGI provided. This is used to get the ticker of the symbol on this date.
        :returns: The Lean Symbol corresponding to the composite FIGI on the trading date provided.
        """
        ...

    @overload
    def composite_figi(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Lean Symbol to its composite FIGI representation
        
        :param symbol: The Lean Symbol
        :returns: The composite Financial Instrument Global Identifier (FIGI) corresponding to the given Lean Symbol.
        """
        ...

    @overload
    def cusip(self, cusip: str, trading_date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Symbol:
        """
        Converts CUSIP into a Lean Symbol
        
        :param cusip: The Committee on Uniform Securities Identification Procedures (CUSIP) number of a security
        :param trading_date: The date that the stock was trading at with the CUSIP provided. This is used to get the ticker of the symbol on this date.
        :returns: The Lean Symbol corresponding to the CUSIP number on the trading date provided.
        """
        ...

    @overload
    def cusip(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Lean Symbol to its CUSIP number
        
        :param symbol: The Lean Symbol
        :returns: The Committee on Uniform Securities Identification Procedures (CUSIP) number corresponding to the given Lean Symbol.
        """
        ...

    @staticmethod
    def get_instance(data_provider: QuantConnect.Interfaces.IDataProvider = None, securities_definition_key: str = None) -> QuantConnect.Securities.SecurityDefinitionSymbolResolver:
        """
        Gets the single instance of the symbol resolver
        
        :param data_provider: Data provider used to obtain symbol mappings data
        :param securities_definition_key: Location to read the securities definition data from
        :returns: The single instance of the symbol resolver.
        """
        ...

    @overload
    def isin(self, isin: str, trading_date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Symbol:
        """
        Converts ISIN into a Lean Symbol
        
        :param isin: The International Securities Identification Number (ISIN) of a security
        :param trading_date: The date that the stock was trading at with the ISIN provided. This is used to get the ticker of the symbol on this date.
        :returns: The Lean Symbol corresponding to the ISIN on the trading date provided.
        """
        ...

    @overload
    def isin(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Lean Symbol to its ISIN representation
        
        :param symbol: The Lean Symbol
        :returns: The International Securities Identification Number (ISIN) corresponding to the given Lean Symbol.
        """
        ...

    @staticmethod
    def reset() -> None:
        """
        Resets the security definition symbol resolver, forcing a reload when reused.
        Called in tests where multiple algorithms are run sequentially,
        and we need to guarantee that every test starts with the same environment.
        """
        ...

    @overload
    def sedol(self, sedol: str, trading_date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Symbol:
        """
        Converts SEDOL into a Lean Symbol
        
        :param sedol: The Stock Exchange Daily Official List (SEDOL) security identifier of a security
        :param trading_date: The date that the stock was trading at with the SEDOL provided. This is used to get the ticker of the symbol on this date.
        :returns: The Lean Symbol corresponding to the SEDOL on the trading date provided.
        """
        ...

    @overload
    def sedol(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Lean Symbol to its SEDOL representation
        
        :param symbol: The Lean Symbol
        :returns: The Stock Exchange Daily Official List (SEDOL) security identifier corresponding to the given Lean Symbol.
        """
        ...


class ISecurityInitializer(metaclass=abc.ABCMeta):
    """Represents a type capable of initializing a new security"""

    def initialize(self, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes the specified security
        
        :param security: The security to be initialized
        """
        ...


class SecurityInitializer(System.Object):
    """Provides static access to the Null security initializer"""

    NULL: QuantConnect.Securities.ISecurityInitializer = ...
    """Gets an implementation of ISecurityInitializer that is a no-op"""


class AccountCurrencyImmediateSettlementModel(QuantConnect.Securities.ImmediateSettlementModel):
    """Represents the model responsible for applying cash settlement rules"""

    def apply_funds(self, apply_funds_parameters: QuantConnect.Securities.ApplyFundsSettlementModelParameters) -> None:
        """
        Applies cash settlement rules
        
        :param apply_funds_parameters: The funds application parameters
        """
        ...


class IContinuousSecurity(metaclass=abc.ABCMeta):
    """A continuous security that get's mapped during his life"""

    @property
    @abc.abstractmethod
    def mapped(self) -> QuantConnect.Symbol:
        """Gets or sets the currently mapped symbol for the security"""
        ...

    @property.setter
    def mapped(self, value: QuantConnect.Symbol) -> None:
        ...


class BrokerageModelSecurityInitializer(System.Object, QuantConnect.Securities.ISecurityInitializer):
    """
    Provides an implementation of ISecurityInitializer that initializes a security
    by settings the Security.FillModel, Security.FeeModel,
    Security.SlippageModel, and the Security.SettlementModel properties
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the BrokerageModelSecurityInitializer class
        for the specified algorithm
        """
        ...

    @overload
    def __init__(self, brokerageModel: QuantConnect.Brokerages.IBrokerageModel, securitySeeder: QuantConnect.Securities.ISecuritySeeder) -> None:
        """
        Initializes a new instance of the BrokerageModelSecurityInitializer class
        for the specified algorithm
        
        :param brokerageModel: The brokerage model used to initialize the security models
        :param securitySeeder: An ISecuritySeeder used to seed the initial price of the security
        """
        ...

    def initialize(self, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes the specified security by setting up the models
        
        :param security: The security to be initialized
        """
        ...


class SecurityDefinition(System.Object):
    """
    Helper class containing various unique identifiers for a given
    SecurityIdentifier, such as FIGI, ISIN, CUSIP, SEDOL.
    """

    @property
    def security_identifier(self) -> QuantConnect.SecurityIdentifier:
        """
        The unique SecurityIdentifier identified by
        the industry-standard security identifiers contained within this class.
        """
        ...

    @property.setter
    def security_identifier(self, value: QuantConnect.SecurityIdentifier) -> None:
        ...

    @property
    def cusip(self) -> str:
        """The Committee on Uniform Securities Identification Procedures (CUSIP) number of a security"""
        ...

    @property.setter
    def cusip(self, value: str) -> None:
        ...

    @property
    def composite_figi(self) -> str:
        """The composite Financial Instrument Global Identifier (FIGI) of a security"""
        ...

    @property.setter
    def composite_figi(self, value: str) -> None:
        ...

    @property
    def sedol(self) -> str:
        """The Stock Exchange Daily Official List (SEDOL) security identifier of a security"""
        ...

    @property.setter
    def sedol(self, value: str) -> None:
        ...

    @property
    def isin(self) -> str:
        """The International Securities Identification Number (ISIN) of a security"""
        ...

    @property.setter
    def isin(self, value: str) -> None:
        ...

    @property
    def cik(self) -> typing.Optional[int]:
        """
        A Central Index Key or CIK number is a unique number assigned to an individual, company, filing agent or foreign government by the United States
        Securities and Exchange Commission (SEC). The number is used to identify its filings in several online databases, including EDGAR.
        """
        ...

    @property.setter
    def cik(self, value: typing.Optional[int]) -> None:
        ...

    @staticmethod
    def from_csv_line(line: str) -> QuantConnect.Securities.SecurityDefinition:
        """
        Parses a single line of CSV and converts it into an instance
        
        :param line: Line of CSV
        :returns: SecurityDefinition instance.
        """
        ...

    @staticmethod
    def read(data_provider: QuantConnect.Interfaces.IDataProvider, securities_definition_key: str) -> System.Collections.Generic.List[QuantConnect.Securities.SecurityDefinition]:
        """
        Reads data from the specified file and converts it to a list of SecurityDefinition
        
        :param data_provider: Data provider used to obtain symbol mappings data
        :param securities_definition_key: Location to read the securities definition data from
        :returns: List of security definitions.
        """
        ...

    @staticmethod
    def try_read(data_provider: QuantConnect.Interfaces.IDataProvider, securities_database_key: str, security_definitions: typing.Optional[System.Collections.Generic.List[QuantConnect.Securities.SecurityDefinition]]) -> typing.Union[bool, System.Collections.Generic.List[QuantConnect.Securities.SecurityDefinition]]:
        """
        Attempts to read data from the specified file and convert it into a list of SecurityDefinition
        
        :param data_provider: Data provider used to obtain symbol mappings data
        :param securities_database_key: Location of the file to read from
        :param security_definitions: Security definitions read
        :returns: true if data was read successfully, false otherwise.
        """
        ...


class ISymbol(metaclass=abc.ABCMeta):
    """Base interface intended for universe data to have some of their symbol properties accessible directly."""

    @property
    @abc.abstractmethod
    def id(self) -> QuantConnect.SecurityIdentifier:
        """Gets the security identifier."""
        ...


class SecurityPriceVariationModel(System.Object, QuantConnect.Securities.IPriceVariationModel):
    """
    Provides default implementation of IPriceVariationModel
    for use in defining the minimum price variation.
    """

    def get_minimum_price_variation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        """
        Get the minimum price variation from a security
        
        :param parameters: An object containing the method parameters
        :returns: Decimal minimum price variation of a given security.
        """
        ...


class EquityPriceVariationModel(QuantConnect.Securities.SecurityPriceVariationModel):
    """
    Provides an implementation of IPriceVariationModel
    for use in defining the minimum price variation for a given equity
    under Regulation NMS – Rule 612 (a.k.a – the “sub-penny rule”)
    """

    def get_minimum_price_variation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        """
        Get the minimum price variation from a security
        
        :param parameters: An object containing the method parameters
        :returns: Decimal minimum price variation of a given security.
        """
        ...


class MarginCallOrdersParameters(System.Object):
    """Defines the parameters for DefaultMarginCallModel.GenerateMarginCallOrders"""

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def total_portfolio_value(self) -> float:
        """Gets the algorithm's total portfolio value"""
        ...

    @property
    def total_used_margin(self) -> float:
        """Gets the total used margin"""
        ...

    def __init__(self, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, totalPortfolioValue: float, totalUsedMargin: float) -> None:
        """
        Initializes a new instance of the MarginCallOrdersParameters class
        
        :param positionGroup: The position group
        :param totalPortfolioValue: The algorithm's total portfolio value
        :param totalUsedMargin: The total used margin
        """
        ...


class SecurityDataFilterPythonWrapper(QuantConnect.Python.BasePythonWrapper[QuantConnect.Securities.Interfaces.ISecurityDataFilter], QuantConnect.Securities.Interfaces.ISecurityDataFilter):
    """Python Wrapper for custom security data filters from Python"""

    def __init__(self, dataFilter: typing.Any) -> None:
        """
        Creates a new instance
        
        :param dataFilter: The Python class to wrapp
        """
        ...

    def filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Performs Filter method from Python instance returning true to accept, or false to fail/reject the data point.
        
        :param vehicle: Security vehicle for filter
        :param data: BasData data object we're filtering
        """
        ...


class NullBuyingPowerModel(QuantConnect.Securities.BuyingPowerModel):
    """Provides a buying power model considers that there is sufficient buying power for all orders"""

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the provided holdings quantity/cost/value.
        """
        ...

    def has_sufficient_buying_power_for_order(self, parameters: QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power to execute this order.
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: Returns buying power information for an order.
        """
        ...


class DefaultMarginCallModel(System.Object, QuantConnect.Securities.IMarginCallModel):
    """Represents the model responsible for picking which orders should be executed during a margin call"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """
        Gets the portfolio that margin calls will be transacted against
        
        This property is protected.
        """
        ...

    @property
    def default_order_properties(self) -> QuantConnect.Interfaces.IOrderProperties:
        """
        Gets the default order properties to be used in margin call orders
        
        This property is protected.
        """
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, defaultOrderProperties: QuantConnect.Interfaces.IOrderProperties, marginBuffer: float = 0.10) -> None:
        """
        Initializes a new instance of the DefaultMarginCallModel class
        
        :param portfolio: The portfolio object to receive margin calls
        :param defaultOrderProperties: The default order properties to be used in margin call orders
        :param marginBuffer: The percent margin buffer to use when checking whether the total margin used is above the total portfolio value to generate margin call orders
        """
        ...

    def execute_margin_call(self, generated_margin_call_orders: System.Collections.Generic.IEnumerable[QuantConnect.Orders.SubmitOrderRequest]) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Executes synchronous orders to bring the account within margin requirements.
        
        :param generated_margin_call_orders: These are the margin call orders that were generated by individual security margin models.
        :returns: The list of orders that were actually executed.
        """
        ...

    def generate_margin_call_orders(self, parameters: QuantConnect.Securities.MarginCallOrdersParameters) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.SubmitOrderRequest]:
        """
        Generates a new order for the specified security taking into account the total margin
        used by the account. Returns null when no margin call is to be issued.
        
        This method is protected.
        
        :param parameters: The set of parameters required to generate the margin call orders
        :returns: An order object representing a liquidation order to be executed to bring the account within margin requirements.
        """
        ...

    def get_margin_call_orders(self, issue_margin_call_warning: typing.Optional[bool]) -> typing.Union[System.Collections.Generic.List[QuantConnect.Orders.SubmitOrderRequest], bool]:
        """
        Scan the portfolio and the updated data for a potential margin call situation which may get the holdings below zero!
        If there is a margin call, liquidate the portfolio immediately before the portfolio gets sub zero.
        
        :param issue_margin_call_warning: Set to true if a warning should be issued to the algorithm
        :returns: True for a margin call on the holdings.
        """
        ...


class SecurityProviderExtensions(System.Object):
    """Provides extension methods for the ISecurityProvider interface."""

    @staticmethod
    def get_holdings_quantity(provider: QuantConnect.Securities.ISecurityProvider, symbol: typing.Union[QuantConnect.Symbol, str]) -> float:
        """
        Extension method to return the quantity of holdings, if no holdings are present, then zero is returned.
        
        :param provider: The ISecurityProvider
        :param symbol: The symbol we want holdings quantity for
        :returns: The quantity of holdings for the specified symbol.
        """
        ...


class BuyingPowerModelExtensions(System.Object):
    """Provides extension methods as backwards compatibility shims"""

    @staticmethod
    @overload
    def above_minimum_order_margin_portfolio_percentage(model: QuantConnect.Securities.IBuyingPowerModel, security: QuantConnect.Securities.Security, quantity: float, portfolio_manager: QuantConnect.Securities.SecurityPortfolioManager, minimum_order_margin_portfolio_percentage: float) -> bool:
        """
        Helper method to determine if the requested quantity is above the algorithm minimum order margin portfolio percentage
        
        :param model: The buying power model
        :param security: The security
        :param quantity: The quantity of shares
        :param portfolio_manager: The algorithm's portfolio
        :param minimum_order_margin_portfolio_percentage: Minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes
        :returns: True if this order quantity is above the minimum requested.
        """
        ...

    @staticmethod
    @overload
    def above_minimum_order_margin_portfolio_percentage(portfolio_manager: QuantConnect.Securities.SecurityPortfolioManager, minimum_order_margin_portfolio_percentage: float, abs_final_order_margin: float) -> bool:
        """
        Helper method to determine if the requested quantity is above the algorithm minimum order margin portfolio percentage
        
        :param portfolio_manager: The algorithm's portfolio
        :param minimum_order_margin_portfolio_percentage: Minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes
        :param abs_final_order_margin: The calculated order margin value
        :returns: True if this order quantity is above the minimum requested.
        """
        ...

    @staticmethod
    def get_buying_power(model: QuantConnect.Securities.IBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> float:
        """
        Gets the buying power available for a trade
        
        :param model: The IBuyingPowerModel
        :param portfolio: The algorithm's portfolio
        :param security: The security to be traded
        :param direction: The direction of the trade
        :returns: The buying power available for the trade.
        """
        ...

    @staticmethod
    def get_initial_margin_requirement(model: QuantConnect.Securities.IBuyingPowerModel, security: QuantConnect.Securities.Security, quantity: float) -> float:
        """
        Gets the margin currently allocated to the specified holding
        
        :param model: The buying power model
        :param security: The security
        :param quantity: The quantity of shares
        :returns: The initial margin required for the provided security and quantity.
        """
        ...

    @staticmethod
    def get_maintenance_margin(model: QuantConnect.Securities.IBuyingPowerModel, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the margin currently allocated to the specified holding
        
        :param model: The buying power model
        :param security: The security
        :returns: The maintenance margin required for the provided holdings quantity/cost/value.
        """
        ...

    @staticmethod
    def get_maximum_order_quantity_for_target_buying_power(model: QuantConnect.Securities.IBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, target: float, minimum_order_margin_portfolio_percentage: float) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a position with a given value in account currency
        
        :param model: The IBuyingPowerModel
        :param portfolio: The algorithm's portfolio
        :param security: The security to be traded
        :param target: The target percent holdings
        :param minimum_order_margin_portfolio_percentage: Configurable minimum order margin portfolio percentage to ignore orders with unrealistic small sizes
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    @staticmethod
    def get_reserved_buying_power_for_position(model: QuantConnect.Securities.IBuyingPowerModel, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the amount of buying power reserved to maintain the specified position
        
        :param model: The IBuyingPowerModel
        :param security: The security
        :returns: The reserved buying power in account currency.
        """
        ...

    @staticmethod
    def has_sufficient_buying_power_for_order(model: QuantConnect.Securities.IBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power to execute this order.
        
        :param model: The IBuyingPowerModel
        :param portfolio: The algorithm's portfolio
        :param security: The security to be traded
        :param order: The order
        :returns: Returns buying power information for an order.
        """
        ...


class AdjustedPriceVariationModel(System.Object, QuantConnect.Securities.IPriceVariationModel):
    """
    Provides an implementation of IPriceVariationModel
    for use when data is DataNormalizationMode.Adjusted.
    """

    def get_minimum_price_variation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        """
        Get the minimum price variation from a security
        
        :param parameters: An object containing the method parameters
        :returns: Zero.
        """
        ...


class SecurityDataFilter(System.Object, QuantConnect.Securities.Interfaces.ISecurityDataFilter):
    """Base class implementation for packet by packet data filtering mechanism to dynamically detect bad ticks."""

    def __init__(self) -> None:
        """Initialize data filter class"""
        ...

    def filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Filter the data packet passing through this method by returning true to accept, or false to fail/reject the data point.
        
        :param vehicle: Security vehicle for filter
        :param data: BasData data object we're filtering
        """
        ...


class SecurityMarginModel(QuantConnect.Securities.BuyingPowerModel):
    """Represents a simple, constant margin model by specifying the percentages of required margin."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the SecurityMarginModel with no leverage (1x)"""
        ...

    @overload
    def __init__(self, initialMarginRequirement: float, maintenanceMarginRequirement: float, requiredFreeBuyingPowerPercent: float) -> None:
        """
        Initializes a new instance of the SecurityMarginModel
        
        :param initialMarginRequirement: The percentage of an order's absolute cost that must be held in free cash in order to place the order
        :param maintenanceMarginRequirement: The percentage of the holding's absolute cost that must be held in free cash in order to avoid a margin call
        :param requiredFreeBuyingPowerPercent: The percentage used to determine the required unused buying power for the account.
        """
        ...

    @overload
    def __init__(self, leverage: float, requiredFreeBuyingPowerPercent: float = 0) -> None:
        """
        Initializes a new instance of the SecurityMarginModel
        
        :param leverage: The leverage
        :param requiredFreeBuyingPowerPercent: The percentage used to determine the required unused buying power for the account.
        """
        ...


class ErrorCurrencyConverter(System.Object, QuantConnect.Securities.ICurrencyConverter):
    """
    Provides an implementation of ICurrencyConverter for use in
    tests that don't depend on this behavior.
    """

    @property
    def account_currency(self) -> str:
        """Gets account currency"""
        ...

    instance: QuantConnect.Securities.ICurrencyConverter = ...
    """
    Provides access to the single instance of ErrorCurrencyConverter.
    This is done this way to ensure usage is explicit.
    """

    def convert_to_account_currency(self, cash_amount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        """
        Converts a cash amount to the account currency
        
        :param cash_amount: The CashAmount instance to convert
        :returns: A new CashAmount instance denominated in the account currency.
        """
        ...


class AccountEvent(System.Object):
    """Messaging class signifying a change in a user's account"""

    @property
    def cash_balance(self) -> float:
        """Gets the total cash balance of the account in units of CurrencySymbol"""
        ...

    @property
    def currency_symbol(self) -> str:
        """Gets the currency symbol"""
        ...

    def __init__(self, currencySymbol: str, cashBalance: float) -> None:
        """
        Creates an AccountEvent
        
        :param currencySymbol: The currency's symbol
        :param cashBalance: The total cash balance of the account
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class UniverseManager(System.Object, System.Collections.Generic.IDictionary[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe], System.Collections.Specialized.INotifyCollectionChanged, typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]]):
    """Manages the algorithm's collection of universes"""

    @property
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]:
        """Event fired when a universe is added or removed"""
        ...

    @property
    def active_securities(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Symbol, QuantConnect.Securities.Security]:
        """
        Read-only dictionary containing all active securities. An active security is
        a security that is currently selected by the universe or has holdings or open orders.
        """
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
    def values(self) -> System.Collections.Generic.ICollection[QuantConnect.Data.UniverseSelection.Universe]:
        """Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2."""
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Gets or sets the element with the specified key.
        
        :param symbol: The key of the element to get or set.
        :returns: The element with the specified key.
        """
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the UniverseManager class"""
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.UniverseSelection.Universe) -> None:
        """
        Gets or sets the element with the specified key.
        
        :param symbol: The key of the element to get or set.
        :returns: The element with the specified key.
        """
        ...

    @overload
    def add(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]) -> None:
        """
        Adds an item to the System.Collections.Generic.ICollection`1.
        
        :param item: The object to add to the System.Collections.Generic.ICollection`1.
        """
        ...

    @overload
    def add(self, key: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.UniverseSelection.Universe) -> None:
        """
        Adds an element with the provided key and value to the System.Collections.Generic.IDictionary{TKey, TValue}.
        
        :param key: The object to use as the key of the element to add.
        :param value: The object to use as the value of the element to add.
        """
        ...

    def clear(self) -> None:
        """Removes all items from the System.Collections.Generic.ICollection`1."""
        ...

    def contains(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]) -> bool:
        """
        Determines whether the System.Collections.Generic.ICollection`1 contains a specific value.
        
        :param item: The object to locate in the System.Collections.Generic.ICollection`1.
        :returns: true if  is found in the System.Collections.Generic.ICollection`1; otherwise, false.
        """
        ...

    def contains_key(self, key: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines whether the System.Collections.Generic.IDictionary`2 contains an element with the specified key.
        
        :param key: The key to locate in the System.Collections.Generic.IDictionary`2.
        :returns: true if the System.Collections.Generic.IDictionary`2 contains an element with the key; otherwise, false.
        """
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]], array_index: int) -> None:
        """
        Copies the elements of the System.Collections.Generic.ICollection`1 to an System.Array, starting at a particular System.Array index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection`1. The System.Array must have zero-based indexing.
        :param array_index: The zero-based index in  at which copying begins.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        """
        Event invocator for the CollectionChanged event
        
        This method is protected.
        """
        ...

    def process_changes(self) -> None:
        """Will trigger collection changed event if required"""
        ...

    @overload
    def remove(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe]) -> bool:
        """
        Removes the first occurrence of a specific object from the System.Collections.Generic.ICollection`1.
        
        :param item: The object to remove from the System.Collections.Generic.ICollection`1.
        :returns: true if  was successfully removed from the System.Collections.Generic.ICollection`1; otherwise, false. This method also returns false if  is not found in the original System.Collections.Generic.ICollection`1.
        """
        ...

    @overload
    def remove(self, key: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Removes the element with the specified key from the System.Collections.Generic.IDictionary`2.
        
        :param key: The key of the element to remove.
        :returns: true if the element is successfully removed; otherwise, false.  This method also returns false if  was not found in the original System.Collections.Generic.IDictionary`2.
        """
        ...

    def try_get_value(self, key: typing.Union[QuantConnect.Symbol, str], value: typing.Optional[QuantConnect.Data.UniverseSelection.Universe]) -> typing.Union[bool, QuantConnect.Data.UniverseSelection.Universe]:
        """
        Gets the value associated with the specified key.
        
        :param key: The key whose value to get.
        :param value: When this method returns, the value associated with the specified key, if the key is found; otherwise, the default value for the type of the  parameter. This parameter is passed uninitialized.
        :returns: true if the object that implements System.Collections.Generic.IDictionary`2 contains an element with the specified key; otherwise, false.
        """
        ...


class IDerivativeSecurityFilter(typing.Generic[QuantConnect_Securities_IDerivativeSecurityFilter_T], metaclass=abc.ABCMeta):
    """Filters a set of derivative symbols using the underlying price data."""

    @property
    @abc.abstractmethod
    def asynchronous(self) -> bool:
        """True if this universe filter can run async in the data stack"""
        ...

    @property.setter
    def asynchronous(self, value: bool) -> None:
        ...

    def filter(self, universe: QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect_Securities_IDerivativeSecurityFilter_T]) -> QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect_Securities_IDerivativeSecurityFilter_T]:
        """
        Filters the input set of symbols represented by the universe
        
        :param universe: derivative symbols universe used in filtering
        :returns: The filtered set of symbols.
        """
        ...


class FuncSecurityDerivativeFilter(typing.Generic[QuantConnect_Securities_FuncSecurityDerivativeFilter_T], System.Object, QuantConnect.Securities.IDerivativeSecurityFilter[QuantConnect_Securities_FuncSecurityDerivativeFilter_T]):
    """Provides a functional implementation of IDerivativeSecurityFilter{T}"""

    @property
    def asynchronous(self) -> bool:
        """True if this universe filter can run async in the data stack"""
        ...

    @property.setter
    def asynchronous(self, value: bool) -> None:
        ...

    def __init__(self, filter: typing.Callable[[QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect_Securities_FuncSecurityDerivativeFilter_T]], QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect_Securities_FuncSecurityDerivativeFilter_T]]) -> None:
        """
        Initializes a new instance of the FuncSecurityDerivativeFilter{T} class
        
        :param filter: The functional implementation of the Filter method
        """
        ...

    def filter(self, universe: QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect_Securities_FuncSecurityDerivativeFilter_T]) -> QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect_Securities_FuncSecurityDerivativeFilter_T]:
        """
        Filters the input set of symbols represented by the universe
        
        :param universe: Derivative symbols universe used in filtering
        :returns: The filtered set of symbols.
        """
        ...


class ContractSecurityFilterUniverse(typing.Generic[QuantConnect_Securities_ContractSecurityFilterUniverse_T, QuantConnect_Securities_ContractSecurityFilterUniverse_TData], System.Object, QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect_Securities_ContractSecurityFilterUniverse_TData], typing.Iterable[QuantConnect_Securities_ContractSecurityFilterUniverse_TData], metaclass=abc.ABCMeta):
    """
    Base class for contract symbols filtering universes.
    Used by OptionFilterUniverse and FutureFilterUniverse
    """

    class ContractExpirationType(Enum):
        """
        Defines listed contract types with Flags attribute
        
        This class is protected.
        """

        STANDARD = 1
        """Standard contracts"""

        WEEKLY = 2
        """Non standard weekly contracts"""

    @property
    def type(self) -> QuantConnect.Securities.ContractSecurityFilterUniverse.ContractExpirationType:
        """
        Expiration Types allowed through the filter
        Standards only by default
        
        This property is protected.
        """
        ...

    @property.setter
    def type(self, value: QuantConnect.Securities.ContractSecurityFilterUniverse.ContractExpirationType) -> None:
        ...

    @property
    def local_time(self) -> datetime.datetime:
        """The local exchange current time"""
        ...

    @overload
    def __init__(self) -> None:
        """
        Constructs ContractSecurityFilterUniverse
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, allData: System.Collections.Generic.IEnumerable[QuantConnect_Securities_ContractSecurityFilterUniverse_TData], localTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Constructs ContractSecurityFilterUniverse
        
        This method is protected.
        """
        ...

    def adjust_expiration_reference_date(self, reference_date: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Adjust the reference date used for expiration filtering. By default it just returns the same date.
        
        This method is protected.
        
        :param reference_date: The reference date to be adjusted
        :returns: The adjusted date.
        """
        ...

    def back_month(self) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Returns first of back month contracts
        
        :returns: Universe with filter applied.
        """
        ...

    def back_months(self) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Returns a list of back month contracts
        
        :returns: Universe with filter applied.
        """
        ...

    @overload
    def contracts(self, contracts: typing.Any) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Explicitly sets the selected contract symbols for this universe.
        This overrides and and all other methods of selecting symbols assuming it is called last.
        
        :param contracts: The option contract symbol objects to select
        :returns: Universe with filter applied.
        """
        ...

    @overload
    def contracts(self, contracts: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Explicitly sets the selected contract symbols for this universe.
        This overrides and and all other methods of selecting symbols assuming it is called last.
        
        :param contracts: The option contract symbol objects to select
        :returns: Universe with filter applied.
        """
        ...

    @overload
    def contracts(self, contracts: System.Collections.Generic.IEnumerable[QuantConnect_Securities_ContractSecurityFilterUniverse_TData]) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Explicitly sets the selected contract symbols for this universe.
        This overrides and and all other methods of selecting symbols assuming it is called last.
        
        :param contracts: The option contract symbol objects to select
        :returns: Universe with filter applied.
        """
        ...

    @overload
    def contracts(self, contract_selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect_Securities_ContractSecurityFilterUniverse_TData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Sets a function used to filter the set of available contract filters. The input to the 'contract_selector'
        function will be the already filtered list if any other filters have already been applied.
        
        :param contract_selector: The option contract symbol objects to select
        :returns: Universe with filter applied.
        """
        ...

    @overload
    def contracts(self, contract_selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect_Securities_ContractSecurityFilterUniverse_TData]], System.Collections.Generic.IEnumerable[QuantConnect_Securities_ContractSecurityFilterUniverse_TData]]) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Sets a function used to filter the set of available contract filters. The input to the 'contract_selector'
        function will be the already filtered list if any other filters have already been applied.
        
        :param contract_selector: The option contract symbol objects to select
        :returns: Universe with filter applied.
        """
        ...

    def create_data_instance(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Securities_ContractSecurityFilterUniverse_TData:
        """
        Creates a new instance of the data type for the given symbol
        
        This method is protected.
        
        :returns: A data instance for the given symbol.
        """
        ...

    @overload
    def expiration(self, min_expiry: datetime.timedelta, max_expiry: datetime.timedelta) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Applies filter selecting options contracts based on a range of expiration dates relative to the current day
        
        :param min_expiry: The minimum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in less than 10 days
        :param max_expiry: The maximum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in more than 10 days
        :returns: Universe with filter applied.
        """
        ...

    @overload
    def expiration(self, min_expiry_days: int, max_expiry_days: int) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Applies filter selecting contracts based on a range of expiration dates relative to the current day
        
        :param min_expiry_days: The minimum time, expressed in days, until expiry to include, for example, 10 would exclude contracts expiring in less than 10 days
        :param max_expiry_days: The maximum time, expressed in days, until expiry to include, for example, 10 would exclude contracts expiring in more than 10 days
        :returns: Universe with filter applied.
        """
        ...

    def front_month(self) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Returns front month contract
        
        :returns: Universe with filter applied.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect_Securities_ContractSecurityFilterUniverse_TData]:
        """
        IEnumerable interface method implementation
        
        :returns: IEnumerator of Symbols in Universe.
        """
        ...

    def get_symbol(self, data: QuantConnect_Securities_ContractSecurityFilterUniverse_TData) -> QuantConnect.Symbol:
        """
        Gets the symbol from the data
        
        This method is protected.
        
        :returns: The symbol that represents the datum.
        """
        ...

    def include_weeklys(self) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Includes universe of non-standard weeklys contracts (if any) into selection
        
        :returns: Universe with filter applied.
        """
        ...

    def is_standard(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Function to determine if the given symbol is a standard contract
        
        This method is protected.
        
        :returns: True if standard type.
        """
        ...

    def only_apply_filter_at_market_open(self) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Instructs the engine to only filter contracts on the first time step of each market day.
        
        Deprecated as of 2023-12-13. Filters are always non-dynamic as of now, which means they will only bee applied daily.
        
        :returns: Universe with filter applied.
        """
        warnings.warn("Deprecated as of 2023-12-13. Filters are always non-dynamic as of now, which means they will only bee applied daily.", DeprecationWarning)

    def refresh(self, all_data: System.Collections.Generic.IEnumerable[QuantConnect_Securities_ContractSecurityFilterUniverse_TData], local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Refreshes this filter universe
        
        :param all_data: All data for contracts in the Universe
        :param local_time: The local exchange current time
        """
        ...

    def standards_only(self) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Sets universe of standard contracts (if any) as selection
        Contracts by default are standards; only needed to switch back if changed
        
        :returns: Universe with filter applied.
        """
        ...

    def weeklys_only(self) -> QuantConnect_Securities_ContractSecurityFilterUniverse_T:
        """
        Sets universe of weeklys contracts (if any) as selection
        
        :returns: Universe with filter applied.
        """
        ...


class FuncSecurityInitializer(System.Object, QuantConnect.Securities.ISecurityInitializer):
    """Provides a functional implementation of ISecurityInitializer"""

    @overload
    def __init__(self, initializer: typing.Any) -> None:
        """
        Initializes a new instance of the FuncSecurityInitializer class
        
        :param initializer: The functional implementation of ISecurityInitializer.Initialize
        """
        ...

    @overload
    def __init__(self, initializer: typing.Callable[[QuantConnect.Securities.Security], None]) -> None:
        """
        Initializes a new instance of the FuncSecurityInitializer class
        
        :param initializer: The functional implementation of ISecurityInitializer.Initialize
        """
        ...

    def initialize(self, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes the specified security
        
        :param security: The security to be initialized
        """
        ...


class IOrderEventProvider(metaclass=abc.ABCMeta):
    """Represents a type with a new OrderEvent event EventHandler."""

    @property
    @abc.abstractmethod
    def new_order_event(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.OrderEvent], None], None]:
        """Event fired when there is a new OrderEvent"""
        ...


class SecurityCacheDataStoredEventArgs(System.EventArgs):
    """Event args for SecurityCache's DataStored event"""

    @property
    def data_type(self) -> typing.Type:
        """The type of data that was stored, such as TradeBar"""
        ...

    @property
    def data(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]:
        """The list of data points stored"""
        ...

    def __init__(self, dataType: typing.Type, data: System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]) -> None:
        """
        Initializes a new instance of the SecurityCacheDataStoredEventArgs class
        
        :param dataType: The type of data
        :param data: The list of data points
        """
        ...


class CashBuyingPowerModel(QuantConnect.Securities.BuyingPowerModel):
    """Represents a buying power model for cash accounts"""

    def __init__(self) -> None:
        """Initializes a new instance of the CashBuyingPowerModel class"""
        ...

    def get_buying_power(self, parameters: QuantConnect.Securities.BuyingPowerParameters) -> QuantConnect.Securities.BuyingPower:
        """
        Gets the buying power available for a trade
        
        :param parameters: A parameters object containing the algorithm's portfolio, security, and order direction
        :returns: The buying power available for the trade.
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity of shares
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the current leverage of the security
        
        :param security: The security to get leverage for
        :returns: The current leverage in the security.
        """
        ...

    def get_maximum_order_quantity_for_delta_buying_power(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a delta in the buying power used by a security.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the security and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_maximum_order_quantity_for_target_buying_power(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a position with a given buying power percentage.
        Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the security and the target signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_reserved_buying_power_for_position(self, parameters: QuantConnect.Securities.ReservedBuyingPowerForPositionParameters) -> QuantConnect.Securities.ReservedBuyingPowerForPosition:
        """
        Gets the amount of buying power reserved to maintain the specified position
        
        :param parameters: A parameters object containing the security
        :returns: The reserved buying power in account currency.
        """
        ...

    def has_sufficient_buying_power_for_order(self, parameters: QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power to execute this order.
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: Returns buying power information for an order.
        """
        ...

    def set_leverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, equities
        
        :param security: The security to set leverage for
        :param leverage: The new leverage
        """
        ...


class MarginCallModel(System.Object):
    """Provides access to a null implementation for IMarginCallModel"""

    NULL: QuantConnect.Securities.IMarginCallModel = ...
    """
    Gets an instance of IMarginCallModel that will always
    return an empty list of executed orders.
    """


class PatternDayTradingMarginModel(QuantConnect.Securities.SecurityMarginModel):
    """
    Represents a simple margining model where margin/leverage depends on market state (open or close).
    During regular market hours, leverage is 4x, otherwise 2x
    """

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the PatternDayTradingMarginModel"""
        ...

    @overload
    def __init__(self, closedMarketLeverage: float, openMarketLeverage: float) -> None:
        """
        Initializes a new instance of the PatternDayTradingMarginModel
        
        :param closedMarketLeverage: Leverage used outside regular market hours
        :param openMarketLeverage: Leverage used during regular market hours
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """The percentage of an order's absolute cost that must be held in free cash in order to place the order"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the current leverage of the security
        
        :param security: The security to get leverage for
        :returns: The current leverage in the security.
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """The percentage of the holding's absolute cost that must be held in free cash in order to avoid a margin call"""
        ...

    def set_leverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, equities
        
        :param security: The security to set leverage to
        :param leverage: The new leverage
        """
        ...


class UnsettledCashAmount(System.Object):
    """Represents a pending cash amount waiting for settlement time"""

    @property
    def settlement_time_utc(self) -> datetime.datetime:
        """The settlement time (in UTC)"""
        ...

    @property
    def currency(self) -> str:
        """The currency symbol"""
        ...

    @property
    def amount(self) -> float:
        """The amount of cash"""
        ...

    def __init__(self, settlementTimeUtc: typing.Union[datetime.datetime, datetime.date], currency: str, amount: float) -> None:
        """Creates a new instance of the UnsettledCashAmount class"""
        ...


class OptionInitialMargin(QuantConnect.Securities.InitialMargin):
    """Result type for Option.OptionStrategyPositionGroupBuyingPowerModel.GetInitialMarginRequirement"""

    ZERO: QuantConnect.Securities.OptionInitialMargin
    """Gets an instance of OptionInitialMargin with zero values"""

    @property
    def premium(self) -> float:
        """The option/strategy premium value in account currency"""
        ...

    @property
    def value_without_premium(self) -> float:
        """The initial margin value in account currency, not including the premium in cases that apply (premium debited)"""
        ...

    def __init__(self, value: float, premium: float) -> None:
        """
        Initializes a new instance of the OptionInitialMargin class
        
        :param value: The initial margin
        :param premium: The premium of the option/option strategy
        """
        ...


class OrderProviderExtensions(System.Object):
    """Provides extension methods for the IOrderProvider interface"""

    @staticmethod
    @overload
    def get_orders_by_brokerage_id(order_provider: QuantConnect.Securities.IOrderProvider, brokerage_id: int) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets the order by its brokerage id
        
        :param order_provider: The order provider to search
        :param brokerage_id: The brokerage id to fetch
        :returns: The first order matching the brokerage id, or null if no match is found.
        """
        ...

    @staticmethod
    @overload
    def get_orders_by_brokerage_id(order_provider: QuantConnect.Securities.IOrderProvider, brokerage_id: int) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets the order by its brokerage id
        
        :param order_provider: The order provider to search
        :param brokerage_id: The brokerage id to fetch
        :returns: The first order matching the brokerage id, or null if no match is found.
        """
        ...


class CompositeSecurityInitializer(System.Object, QuantConnect.Securities.ISecurityInitializer):
    """
    Provides an implementation of ISecurityInitializer that executes
    each initializer in order
    """

    @overload
    def __init__(self, *initializers: PyObject) -> None:
        """
        Initializes a new instance of the CompositeSecurityInitializer class
        
        :param initializers: The initializers to execute in order
        """
        ...

    @overload
    def __init__(self, *initializers: QuantConnect.Securities.ISecurityInitializer) -> None:
        """
        Initializes a new instance of the CompositeSecurityInitializer class
        
        :param initializers: The initializers to execute in order
        """
        ...

    def initialize(self, security: QuantConnect.Securities.Security) -> None:
        """
        Execute each of the internally held initializers in sequence
        
        :param security: The security to be initialized
        """
        ...


class RegisteredSecurityDataTypesProvider(System.Object, QuantConnect.Securities.IRegisteredSecurityDataTypesProvider):
    """
    Provides an implementation of IRegisteredSecurityDataTypesProvider that permits the
    consumer to modify the expected types
    """

    NULL: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider = ...
    """Provides a reference to an instance of IRegisteredSecurityDataTypesProvider that contains no registered types"""

    def register_type(self, type: typing.Type) -> bool:
        """
        Registers the specified type w/ the provider
        
        :returns: True if the type was previously not registered.
        """
        ...

    def try_get_type(self, name: str, type: typing.Optional[typing.Type]) -> typing.Union[bool, typing.Type]:
        """Gets an enumerable of data types expected to be contained in a DynamicSecurityData instance"""
        ...

    def unregister_type(self, type: typing.Type) -> bool:
        """
        Removes the registration for the specified type
        
        :returns: True if the type was previously registered.
        """
        ...


class EmptyContractFilter(System.Object, QuantConnect.Securities.IDerivativeSecurityFilter[QuantConnect.Symbol]):
    """Derivate security universe selection filter which will always return empty"""

    @property
    def asynchronous(self) -> bool:
        """True if this universe filter can run async in the data stack"""
        ...

    @property.setter
    def asynchronous(self, value: bool) -> None:
        ...

    def filter(self, universe: QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect.Symbol]) -> QuantConnect.Securities.IDerivativeSecurityFilterUniverse[QuantConnect.Symbol]:
        """
        Filters the input set of symbols represented by the universe
        
        :param universe: derivative symbols universe used in filtering
        :returns: The filtered set of symbols.
        """
        ...


class IdentityCurrencyConverter(System.Object, QuantConnect.Securities.ICurrencyConverter):
    """
    Provides an implementation of ICurrencyConverter that does NOT perform conversions.
    This implementation will throw if the specified cashAmount is not in units of account currency.
    """

    @property
    def account_currency(self) -> str:
        """Gets account currency"""
        ...

    def __init__(self, accountCurrency: str) -> None:
        """
        Initializes a new instance of the ICurrencyConverter class
        
        :param accountCurrency: The algorithm's account currency
        """
        ...

    def convert_to_account_currency(self, cash_amount: QuantConnect.Securities.CashAmount) -> QuantConnect.Securities.CashAmount:
        """
        Converts a cash amount to the account currency.
        This implementation can only handle cash amounts in units of the account currency.
        
        :param cash_amount: The CashAmount instance to convert
        :returns: A new CashAmount instance denominated in the account currency.
        """
        ...


class DelayedSettlementModel(System.Object, QuantConnect.Securities.ISettlementModel):
    """Represents the model responsible for applying cash settlement rules"""

    def __init__(self, numberOfDays: int, timeOfDay: datetime.timedelta) -> None:
        """
        Creates an instance of the DelayedSettlementModel class
        
        :param numberOfDays: The number of days required for settlement
        :param timeOfDay: The time of day used for settlement
        """
        ...

    def apply_funds(self, apply_funds_parameters: QuantConnect.Securities.ApplyFundsSettlementModelParameters) -> None:
        """
        Applies cash settlement rules
        
        :param apply_funds_parameters: The funds application parameters
        """
        ...

    def get_unsettled_cash(self) -> QuantConnect.Securities.CashAmount:
        """Gets the unsettled cash amount for the security"""
        ...

    def scan(self, settlement_parameters: QuantConnect.Securities.ScanSettlementModelParameters) -> None:
        """
        Scan for pending settlements
        
        :param settlement_parameters: The settlement parameters
        """
        ...


class IndicatorVolatilityModel(QuantConnect.Securities.Volatility.BaseVolatilityModel):
    """
    Provides an implementation of IVolatilityModel that uses an indicator
    to compute its value
    """

    @property
    def volatility(self) -> float:
        """Gets the volatility of the security as a percentage"""
        ...

    @overload
    def __init__(self, indicator: QuantConnect.Indicators.IIndicator) -> None:
        """
        Initializes a new instance of the IVolatilityModel using
        the specified . The 
        is assumed to but updated externally from this model, such as being registered
        into the consolidator system.
        
        :param indicator: The auto-updating indicator
        """
        ...

    @overload
    def __init__(self, indicator: QuantConnect.Indicators.IIndicator, indicatorUpdate: typing.Callable[[QuantConnect.Securities.Security, QuantConnect.Data.BaseData, QuantConnect.Indicators.IIndicator], None]) -> None:
        """
        Initializes a new instance of the IVolatilityModel using
        the specified . The 
        is assumed to but updated externally from this model, such as being registered
        into the consolidator system.
        
        :param indicator: The auto-updating indicator
        :param indicatorUpdate: Function delegate used to update the indicator on each call to Update
        """
        ...

    def update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        """
        Updates this model using the new price information in
        the specified security instance
        
        :param security: The security to calculate volatility for
        :param data: The new piece of data for the security
        """
        ...


class RelativeStandardDeviationVolatilityModel(QuantConnect.Securities.Volatility.BaseVolatilityModel):
    """
    Provides an implementation of IVolatilityModel that computes the
    relative standard deviation as the volatility of the security
    """

    @property
    def volatility(self) -> float:
        """Gets the volatility of the security as a percentage"""
        ...

    def __init__(self, periodSpan: datetime.timedelta, periods: int) -> None:
        """
        Initializes a new instance of the RelativeStandardDeviationVolatilityModel class
        
        :param periodSpan: The time span representing one 'period' length
        :param periods: The number of 'period' lengths to wait until updating the value
        """
        ...

    def get_history_requirements(self, security: QuantConnect.Securities.Security, utc_time: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Returns history requirements for the volatility model expressed in the form of history request
        
        :param security: The security of the request
        :param utc_time: The date/time of the request
        :returns: History request object list, or empty if no requirements.
        """
        ...

    def update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        """
        Updates this model using the new price information in
        the specified security instance
        
        :param security: The security to calculate volatility for
        """
        ...


class VolatilityModel(System.Object):
    """Provides access to a null implementation for IVolatilityModel"""

    NULL: QuantConnect.Securities.IVolatilityModel = ...
    """
    Gets an instance of IVolatilityModel that will always
    return 0 for its volatility and does nothing during Update.
    """


class StandardDeviationOfReturnsVolatilityModel(QuantConnect.Securities.Volatility.BaseVolatilityModel):
    """
    Provides an implementation of IVolatilityModel that computes the
    annualized sample standard deviation of daily returns as the volatility of the security
    """

    @property
    def volatility(self) -> float:
        """Gets the volatility of the security as a percentage"""
        ...

    @overload
    def __init__(self, periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, updateFrequency: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the StandardDeviationOfReturnsVolatilityModel class
        
        :param periods: The max number of samples in the rolling window to be considered for calculating the standard deviation of returns
        :param resolution: Resolution of the price data inserted into the rolling window series to calculate standard deviation. Will be used as the default value for update frequency if a value is not provided for . This only has a material effect in live mode. For backtesting, this value does not cause any behavioral changes.
        :param updateFrequency: Frequency at which we insert new values into the rolling window for the standard deviation calculation
        """
        ...

    @overload
    def __init__(self, resolution: QuantConnect.Resolution, updateFrequency: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the StandardDeviationOfReturnsVolatilityModel class
        
        :param resolution: Resolution of the price data inserted into the rolling window series to calculate standard deviation. Will be used as the default value for update frequency if a value is not provided for . This only has a material effect in live mode. For backtesting, this value does not cause any behavioral changes.
        :param updateFrequency: Frequency at which we insert new values into the rolling window for the standard deviation calculation
        """
        ...

    def get_history_requirements(self, security: QuantConnect.Securities.Security, utc_time: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Returns history requirements for the volatility model expressed in the form of history request
        
        :param security: The security of the request
        :param utc_time: The date of the request
        :returns: History request object list, or empty if no requirements.
        """
        ...

    def update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        """
        Updates this model using the new price information in
        the specified security instance
        
        :param security: The security to calculate volatility for
        :param data: Data to update the volatility model with
        """
        ...


class OptionFilterUniverse(QuantConnect.Securities.ContractSecurityFilterUniverse[QuantConnect_Securities_OptionFilterUniverse, QuantConnect.Data.UniverseSelection.OptionUniverse]):
    """Represents options symbols universe used in filtering."""

    @property
    def underlying_internal(self) -> QuantConnect.Data.BaseData:
        """
        The underlying price data
        
        This property is protected.
        """
        ...

    @property.setter
    def underlying_internal(self, value: QuantConnect.Data.BaseData) -> None:
        ...

    @property
    def underlying(self) -> QuantConnect.Data.BaseData:
        """The underlying price data"""
        ...

    @overload
    def __init__(self, option: QuantConnect.Securities.Option.Option) -> None:
        """
        Constructs OptionFilterUniverse
        
        :param option: The canonical option chain security
        """
        ...

    @overload
    def __init__(self, option: QuantConnect.Securities.Option.Option, allData: System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.OptionUniverse], underlying: QuantConnect.Data.BaseData, underlyingScaleFactor: float = 1) -> None:
        """Constructs OptionFilterUniverse"""
        ...

    def adjust_expiration_reference_date(self, reference_date: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Adjusts the date to the next trading day if the current date is not a trading day, so that expiration filter is properly applied.
        e.g. Selection for Mondays happen on Friday midnight (Saturday start), so if the minimum time to expiration is, say 0,
        contracts expiring on Monday would be filtered out if the date is not properly adjusted to the next trading day (Monday).
        
        This method is protected.
        
        :param reference_date: The date to be adjusted
        :returns: The adjusted date.
        """
        ...

    def box_spread(self, min_days_till_expiry: int = 30, strike_spread: float = 5) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of an OTM call, an ITM call, an OTM put, and an ITM put with the same expiry with closest match to the criteria given.
        The OTM call has the same strike as the ITM put, while the same holds for the ITM call and the OTM put
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param strike_spread: The desire strike price distance of the OTM call and the OTM put from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def call_butterfly(self, min_days_till_expiry: int = 30, strike_spread: float = 5) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of an ITM call, an ATM call, and an OTM call with the same expiry and equal strike price distance, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param strike_spread: The desire strike price distance of the ITM call and the OTM call from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def call_calendar_spread(self, strike_from_atm: float = 0, min_near_days_till_expiry: int = 30, min_far_days_till_expiry: int = 60) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of 2 call contracts with the same strike price and different expiration dates, with closest match to the criteria given
        
        :param strike_from_atm: The desire strike price distance from the current underlying price
        :param min_near_days_till_expiry: The mininum days till expiry of the closer contract from the current time, closest expiry will be selected
        :param min_far_days_till_expiry: The mininum days till expiry of the further conrtact from the current time, closest expiry will be selected
        :returns: Universe with filter applied.
        """
        ...

    def call_ladder(self, min_days_till_expiry: int, higher_strike_from_atm: float, middle_strike_from_atm: float, lower_strike_from_atm: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of 3 call contracts with the same expiry and different strike prices, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param higher_strike_from_atm: The desire strike price distance from the current underlying price of the higher strike price
        :param middle_strike_from_atm: The desire strike price distance from the current underlying price of the middle strike price
        :param lower_strike_from_atm: The desire strike price distance from the current underlying price of the lower strike price
        :returns: Universe with filter applied.
        """
        ...

    def calls_only(self) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of call options (if any) as a selection
        
        :returns: Universe with filter applied.
        """
        ...

    def call_spread(self, min_days_till_expiry: int = 30, higher_strike_from_atm: float = 5, lower_strike_from_atm: typing.Optional[float] = None) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of 2 call contracts with the same expiry and different strike prices, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param higher_strike_from_atm: The desire strike price distance from the current underlying price of the higher strike price
        :param lower_strike_from_atm: The desire strike price distance from the current underlying price of the lower strike price
        :returns: Universe with filter applied.
        """
        ...

    def conversion(self, min_days_till_expiry: int = 30, strike_from_atm: float = 5) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of a call contract and a put contract with the same expiry and strike price, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param strike_from_atm: The desire strike price distance from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def create_data_instance(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.UniverseSelection.OptionUniverse:
        """
        Creates a new instance of the data type for the given symbol
        
        This method is protected.
        
        :returns: A data instance for the given symbol.
        """
        ...

    def d(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Delta between the given range.
        Alias for Delta(decimal, decimal)
        
        :param min: The minimum Delta value
        :param max: The maximum Delta value
        :returns: Universe with filter applied.
        """
        ...

    def delta(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Delta between the given range
        
        :param min: The minimum Delta value
        :param max: The maximum Delta value
        :returns: Universe with filter applied.
        """
        ...

    def g(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Gamma between the given range.
        Alias for Gamma(decimal, decimal)
        
        :param min: The minimum Gamma value
        :param max: The maximum Gamma value
        :returns: Universe with filter applied.
        """
        ...

    def gamma(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Gamma between the given range
        
        :param min: The minimum Gamma value
        :param max: The maximum Gamma value
        :returns: Universe with filter applied.
        """
        ...

    def get_symbol(self, data: QuantConnect.Data.UniverseSelection.OptionUniverse) -> QuantConnect.Symbol:
        """
        Gets the symbol from the data
        
        This method is protected.
        
        :returns: The symbol that represents the datum.
        """
        ...

    def implied_volatility(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with implied volatility between the given range
        
        :param min: The minimum implied volatility value
        :param max: The maximum implied volatility value
        :returns: Universe with filter applied.
        """
        ...

    def iron_butterfly(self, min_days_till_expiry: int = 30, strike_spread: float = 5) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of an OTM call, an ATM call, an ATM put, and an OTM put with the same expiry and equal strike price distance, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param strike_spread: The desire strike price distance of the OTM call and the OTM put from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def iron_condor(self, min_days_till_expiry: int = 30, near_strike_spread: float = 5, far_strike_spread: float = 10) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of a far-OTM call, a near-OTM call, a near-OTM put, and a far-OTM put with the same expiry
        and equal strike price distance between both calls and both puts, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param near_strike_spread: The desire strike price distance of the near-to-expiry call and the near-to-expiry put from the current underlying price
        :param far_strike_spread: The desire strike price distance of the further-to-expiry call and the further-to-expiry put from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def is_standard(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determine if the given Option contract symbol is standard
        
        This method is protected.
        
        :returns: True if standard.
        """
        ...

    def iv(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with implied volatility between the given range.
        Alias for ImpliedVolatility(decimal, decimal)
        
        :param min: The minimum implied volatility value
        :param max: The maximum implied volatility value
        :returns: Universe with filter applied.
        """
        ...

    def jelly_roll(self, strike_from_atm: float = 0, min_near_days_till_expiry: int = 30, min_far_days_till_expiry: int = 60) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of 2 call and 2 put contracts with the same strike price and 2 expiration dates, with closest match to the criteria given
        
        :param strike_from_atm: The desire strike price distance from the current underlying price
        :param min_near_days_till_expiry: The mininum days till expiry of the closer contract from the current time, closest expiry will be selected
        :param min_far_days_till_expiry: The mininum days till expiry of the further conrtact from the current time, closest expiry will be selected
        :returns: Universe with filter applied.
        """
        ...

    def naked_call(self, min_days_till_expiry: int = 30, strike_from_atm: float = 0) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of a single call contract with the closest match to criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param strike_from_atm: The desire strike price distance from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def naked_put(self, min_days_till_expiry: int = 30, strike_from_atm: float = 0) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of a single put contract with the closest match to criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param strike_from_atm: The desire strike price distance from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def oi(self, min: int, max: int) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with open interest between the given range.
        Alias for OpenInterest(long, long)
        
        :param min: The minimum open interest value
        :param max: The maximum open interest value
        :returns: Universe with filter applied.
        """
        ...

    def open_interest(self, min: int, max: int) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with open interest between the given range
        
        :param min: The minimum open interest value
        :param max: The maximum open interest value
        :returns: Universe with filter applied.
        """
        ...

    def protective_collar(self, min_days_till_expiry: int = 30, call_strike_from_atm: float = 5, put_strike_from_atm: float = -5) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of a call contract and a put contract with the same expiry but lower strike price, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param call_strike_from_atm: The desire strike price distance from the current underlying price of the call.
        :param put_strike_from_atm: The desire strike price distance from the current underlying price of the put.
        :returns: Universe with filter applied.
        """
        ...

    def put_butterfly(self, min_days_till_expiry: int = 30, strike_spread: float = 5) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of an ITM put, an ATM put, and an OTM put with the same expiry and equal strike price distance, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param strike_spread: The desire strike price distance of the ITM put and the OTM put from the current underlying price
        :returns: Universe with filter applied.
        """
        ...

    def put_calendar_spread(self, strike_from_atm: float = 0, min_near_days_till_expiry: int = 30, min_far_days_till_expiry: int = 60) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of 2 put contracts with the same strike price and different expiration dates, with closest match to the criteria given
        
        :param strike_from_atm: The desire strike price distance from the current underlying price
        :param min_near_days_till_expiry: The mininum days till expiry of the closer contract from the current time, closest expiry will be selected
        :param min_far_days_till_expiry: The mininum days till expiry of the further conrtact from the current time, closest expiry will be selected
        :returns: Universe with filter applied.
        """
        ...

    def put_ladder(self, min_days_till_expiry: int, higher_strike_from_atm: float, middle_strike_from_atm: float, lower_strike_from_atm: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of 3 put contracts with the same expiry and different strike prices, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param higher_strike_from_atm: The desire strike price distance from the current underlying price of the higher strike price
        :param middle_strike_from_atm: The desire strike price distance from the current underlying price of the middle strike price
        :param lower_strike_from_atm: The desire strike price distance from the current underlying price of the lower strike price
        :returns: Universe with filter applied.
        """
        ...

    def puts_only(self) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of put options (if any) as a selection
        
        :returns: Universe with filter applied.
        """
        ...

    def put_spread(self, min_days_till_expiry: int = 30, higher_strike_from_atm: float = 5, lower_strike_from_atm: typing.Optional[float] = None) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of 2 put contracts with the same expiry and different strike prices, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param higher_strike_from_atm: The desire strike price distance from the current underlying price of the higher strike price
        :param lower_strike_from_atm: The desire strike price distance from the current underlying price of the lower strike price
        :returns: Universe with filter applied.
        """
        ...

    def r(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Rho between the given range.
        Alias for Rho(decimal, decimal)
        
        :param min: The minimum Rho value
        :param max: The maximum Rho value
        :returns: Universe with filter applied.
        """
        ...

    def refresh(self, all_contracts_data: System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.OptionUniverse], underlying: QuantConnect.Data.BaseData, local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Refreshes this option filter universe and allows specifying if the exchange date changed from last call
        
        :param all_contracts_data: All data for the option contracts
        :param underlying: The current underlying last data point
        :param local_time: The current local time
        """
        ...

    def rho(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Rho between the given range
        
        :param min: The minimum Rho value
        :param max: The maximum Rho value
        :returns: Universe with filter applied.
        """
        ...

    def straddle(self, min_days_till_expiry: int = 30) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of an ATM call contract and an ATM put contract with the same expiry, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :returns: Universe with filter applied.
        """
        ...

    def strangle(self, min_days_till_expiry: int = 30, call_strike_from_atm: float = 5, put_strike_from_atm: float = -5) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Sets universe of an OTM call contract and an OTM put contract with the same expiry, with closest match to the criteria given
        
        :param min_days_till_expiry: The minimum days till expiry from the current time, closest expiry will be selected
        :param call_strike_from_atm: The desire strike price distance from the current underlying price of the OTM call. It must be positive.
        :param put_strike_from_atm: The desire strike price distance from the current underlying price of the OTM put. It must be negative.
        :returns: Universe with filter applied.
        """
        ...

    def strikes(self, min_strike: int, max_strike: int) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies filter selecting options contracts based on a range of strikes in relative terms
        
        :param min_strike: The minimum strike relative to the underlying price, for example, -1 would filter out contracts further than 1 strike below market price
        :param max_strike: The maximum strike relative to the underlying price, for example, +1 would filter out contracts further than 1 strike above market price
        :returns: Universe with filter applied.
        """
        ...

    def t(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Theta between the given range.
        Alias for Theta(decimal, decimal)
        
        :param min: The minimum Theta value
        :param max: The maximum Theta value
        :returns: Universe with filter applied.
        """
        ...

    def theta(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Theta between the given range
        
        :param min: The minimum Theta value
        :param max: The maximum Theta value
        :returns: Universe with filter applied.
        """
        ...

    def v(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Vega between the given range.
        Alias for Vega(decimal, decimal)
        
        :param min: The minimum Vega value
        :param max: The maximum Vega value
        :returns: Universe with filter applied.
        """
        ...

    def vega(self, min: float, max: float) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Applies the filter to the universe selecting the contracts with Vega between the given range
        
        :param min: The minimum Vega value
        :param max: The maximum Vega value
        :returns: Universe with filter applied.
        """
        ...


class OptionFilterUniverseEx(System.Object):
    """Extensions for Linq support"""

    @staticmethod
    @overload
    def select(universe: QuantConnect.Securities.OptionFilterUniverse, map_func: typing.Callable[[QuantConnect.Data.UniverseSelection.OptionUniverse], QuantConnect.Symbol]) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Maps universe
        
        :param universe: Universe to apply the filter too
        :param map_func: Symbol function to determine which Symbols are filtered
        :returns: Universe with filter applied.
        """
        ...

    @staticmethod
    @overload
    def select(universe: QuantConnect.Securities.OptionFilterUniverse, map_func: typing.Any) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Maps universe
        
        :param universe: Universe to apply the filter too
        :param map_func: Symbol function to determine which Symbols are filtered
        :returns: Universe with filter applied.
        """
        ...

    @staticmethod
    @overload
    def select_many(universe: QuantConnect.Securities.OptionFilterUniverse, map_func: typing.Callable[[QuantConnect.Data.UniverseSelection.OptionUniverse], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Binds universe
        
        :param universe: Universe to apply the filter too
        :param map_func: Symbol function to determine which Symbols are filtered
        :returns: Universe with filter applied.
        """
        ...

    @staticmethod
    @overload
    def select_many(universe: QuantConnect.Securities.OptionFilterUniverse, map_func: typing.Any) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Binds universe
        
        :param universe: Universe to apply the filter too
        :param map_func: Symbol function to determine which Symbols are filtered
        :returns: Universe with filter applied.
        """
        ...

    @staticmethod
    @overload
    def where(universe: QuantConnect.Securities.OptionFilterUniverse, predicate: typing.Callable[[QuantConnect.Data.UniverseSelection.OptionUniverse], bool]) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Filters universe
        
        :param universe: Universe to apply the filter too
        :param predicate: Bool function to determine which Symbol are filtered
        :returns: Universe with filter applied.
        """
        ...

    @staticmethod
    @overload
    def where(universe: QuantConnect.Securities.OptionFilterUniverse, predicate: typing.Any) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Filters universe
        
        :param universe: Universe to apply the filter too
        :param predicate: Bool function to determine which Symbol are filtered
        :returns: Universe with filter applied.
        """
        ...

    @staticmethod
    @overload
    def where_contains(universe: QuantConnect.Securities.OptionFilterUniverse, filter_list: System.Collections.Generic.List[QuantConnect.Symbol]) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Updates universe to only contain the symbols in the list
        
        :param universe: Universe to apply the filter too
        :param filter_list: List of Symbols to keep in the Universe
        :returns: Universe with filter applied.
        """
        ...

    @staticmethod
    @overload
    def where_contains(universe: QuantConnect.Securities.OptionFilterUniverse, filter_list: typing.Any) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Updates universe to only contain the symbols in the list
        
        :param universe: Universe to apply the filter too
        :param filter_list: List of Symbols to keep in the Universe
        :returns: Universe with filter applied.
        """
        ...


class FutureExpirationCycles(System.Object):
    """Static class contains definitions of popular futures expiration cycles"""

    JANUARY: typing.List[int] = ...
    """January Cycle: Expirations in January, April, July, October (the first month of each quarter)"""

    FEBRUARY: typing.List[int] = ...
    """February Cycle: Expirations in February, May, August, November (second month)"""

    MARCH: typing.List[int] = ...
    """March Cycle: Expirations in March, June, September, December (third month)"""

    DECEMBER: typing.List[int] = ...
    """December Cycle: Expirations in December"""

    ALL_YEAR: typing.List[int] = ...
    """All Year Cycle: Expirations in every month of the year"""

    GJMQVZ: typing.List[int] = ...
    """GJMQVZ Cycle"""

    GJKMNQVZ: typing.List[int] = ...
    """GJKMNQVZ Cycle"""

    HMUZ: typing.List[int] = ...
    """HMUZ Cycle"""

    HKNUZ: typing.List[int] = ...
    """HKNUZ Cycle"""

    HKNV: typing.List[int] = ...
    """HKNV Cycle"""

    HKNVZ: typing.List[int] = ...
    """HKNVZ Cycle"""

    FHKNUX: typing.List[int] = ...
    """FHKNUX Cycle"""

    FHJKQUVX: typing.List[int] = ...
    """FHJKQUVX Cycle"""

    HKNUVZ: typing.List[int] = ...
    """HKNUVZ Cycle"""

    FHKNUVZ: typing.List[int] = ...
    """FHKNQUVZ Cycle"""

    FHKNQUVZ: typing.List[int] = ...
    """FHKMQUVZ Cycle"""

    FHKNQUX: typing.List[int] = ...
    """FHKNQUX Cycle"""

    FGHJKMNQUVXZ: typing.List[int] = ...
    """FGHJKMNQUVXZ Cycle"""


class Futures(System.Object):
    """Futures static class contains shortcut definitions of major futures contracts available for trading"""

    class Grains(System.Object):
        """Grains and Oilseeds group"""

        BLACK_SEA_CORN_FINANCIALLY_SETTLED_PLATTS: str = "BCF"
        """Black Sea Corn Financially Settled (Platts) Futures"""

        BLACK_SEA_WHEAT_FINANCIALLY_SETTLED_PLATTS: str = "BWF"
        """Black Sea Wheat Financially Settled (Platts) Futures"""

        SRW_WHEAT: str = "ZW"
        """Chicago SRW Wheat Futures"""

        WHEAT: str = ...
        """Default wheat contract is SRWWheat"""

        HRW_WHEAT: str = "KE"
        """KC HRW Wheat Futures"""

        CORN: str = "ZC"
        """Corn Futures"""

        SOYBEANS: str = "ZS"
        """Soybeans Futures"""

        SOYBEAN_MEAL: str = "ZM"
        """Soybean Meal Futures"""

        SOYBEAN_OIL: str = "ZL"
        """Soybean Oil Futures"""

        OATS: str = "ZO"
        """Oats Futures"""

    class Currencies(System.Object):
        """Currencies group"""

        USD: str = "DX"
        """U.S. Dollar Index Futures"""

        GBP: str = "6B"
        """British Pound Futures"""

        CAD: str = "6C"
        """Canadian Dollar Futures"""

        JPY: str = "6J"
        """Japanese Yen Futures"""

        CHF: str = "6S"
        """Swiss Franc Futures"""

        EUR: str = "6E"
        """Euro FX Futures"""

        AUD: str = "6A"
        """Australian Dollar Futures"""

        NZD: str = "6N"
        """New Zealand Dollar Futures"""

        RUB: str = "6R"
        """Russian Ruble Futures"""

        BRL: str = "6L"
        """Brazillian Real Futures"""

        MXN: str = "6M"
        """Mexican Peso Futures"""

        ZAR: str = "6Z"
        """South African Rand Futures"""

        AUDCAD: str = "ACD"
        """Australian Dollar/Canadian Dollar Futures"""

        AUDJPY: str = "AJY"
        """Australian Dollar/Japanese Yen Futures"""

        AUDNZD: str = "ANE"
        """Australian Dollar/New Zealand Dollar Futures"""

        BTC: str = "BTC"
        """Bitcoin Futures"""

        ETH: str = "ETH"
        """Ether Futures"""

        CADJPY: str = "CJY"
        """Canadian Dollar/Japanese Yen Futures"""

        STANDARD_SIZE_USD_OFFSHORE_RMBCNH: str = "CNH"
        """Standard-Size USD/Offshore RMB (CNH) Futures"""

        EURO_FX_EMINI: str = "E7"
        """E-mini Euro FX Futures"""

        EURAUD: str = "EAD"
        """Euro/Australian Dollar Futures"""

        EURCAD: str = "ECD"
        """Euro/Canadian Dollar Futures"""

        EURSEK: str = "ESK"
        """Euro/Swedish Krona Futures"""

        JAPANESE_YEN_EMINI: str = "J7"
        """E-mini Japanese Yen Futures"""

        MICRO_EUR: str = "M6E"
        """Micro EUR/USD Futures"""

        MICRO_AUD: str = "M6A"
        """Micro AUD/USD Futures"""

        MICRO_GBP: str = "M6B"
        """Micro GBP/USD Futures"""

        MICRO_CADUSD: str = "MCD"
        """Micro CAD/USD Futures"""

        MICRO_JPY: str = "MJY"
        """Micro JPY/USD Futures"""

        MICRO_CHF: str = "MSF"
        """Micro CHF/USD Futures"""

        MICRO_USDJPY: str = "M6J"
        """Micro USD/JPY Futures"""

        MICRO_INRUSD: str = "MIR"
        """Micro INR/USD Futures"""

        MICRO_CAD: str = "M6C"
        """Micro USD/CAD Futures"""

        MICRO_USDCHF: str = "M6S"
        """Micro USD/CHF Futures"""

        MICRO_USDCNH: str = "MNH"
        """Micro USD/CNH Futures"""

        MICRO_ETHER: str = "MET"
        """Micro Ether Futures"""

        MICRO_BTC: str = "MBT"
        """Micro Bitcoin Futures"""

        BTIC_MICRO_ETHER: str = "MRB"
        """BTIC on Micro Ether Futures"""

        BTIC_MICRO_BTC: str = "MIB"
        """BTIC on Micro Bitcoin Futures"""

    class Energies(System.Object):
        """
        Energy group
        
        Futures.Energies is obsolete, please use Futures.Energy instead.
        """

        PROPANE_NON_LDH_MONT_BELVIEU: str = "1S"
        """Propane Non LDH Mont Belvieu (OPIS) BALMO Futures"""

        ARGUS_PROPANE_FAR_EAST_INDEX_BALMO: str = "22"
        """Argus Propane Far East Index BALMO Futures"""

        MINI_EUROPEAN_THREE_POINT_PERCENT_FIVE_FUEL_OIL_BARGES_PLATTS: str = "A0D"
        """Mini European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        MINI_SINGAPORE_FUEL_OIL_180_CST_PLATTS: str = "A0F"
        """Mini Singapore Fuel Oil 180 cst (Platts) Futures"""

        GULF_COAST_ULSD_PLATTS_UP_DOWN_BALMO: str = "A1L"
        """Gulf Coast ULSD (Platts) Up-Down BALMO Futures"""

        GULF_COAST_JET_PLATTS_UP_DOWN_BALMO: str = "A1M"
        """Gulf Coast Jet (Platts) Up-Down BALMO Futures"""

        PROPANE_NON_LDH_MONT_BELVIEU_OPIS: str = "A1R"
        """Propane Non-LDH Mont Belvieu (OPIS) Futures"""

        EUROPEAN_PROPANE_CIFARA_ARGUS_BALMO: str = "A32"
        """European Propane CIF ARA (Argus) BALMO Futures"""

        PREMIUM_UNLEADED_GASOLINE_10_PPM_FOBMED_PLATTS: str = "A3G"
        """Premium Unleaded Gasoline 10 ppm FOB MED (Platts) Futures"""

        ARGUS_PROPANE_FAR_EAST_INDEX: str = "A7E"
        """Argus Propane Far East Index Futures"""

        GASOLINE_EUROBOB_OXY_NWE_BARGES_ARGUS_CRACK_SPREAD_BALMO: str = "A7I"
        """Gasoline Euro-bob Oxy NWE Barges (Argus) Crack Spread BALMO Futures"""

        MONT_BELVIEU_NATURAL_GASOLINE_OPIS: str = "A7Q"
        """Mont Belvieu Natural Gasoline (OPIS) Futures"""

        MONT_BELVIEU_NORMAL_BUTANE_OPISBALMO: str = "A8J"
        """Mont Belvieu Normal Butane (OPIS) BALMO Futures"""

        CONWAY_PROPANE_OPIS: str = "A8K"
        """Conway Propane (OPIS) Futures"""

        MONT_BELVIEU_LDH_PROPANE_OPISBALMO: str = "A8O"
        """Mont Belvieu LDH Propane (OPIS) BALMO Futures"""

        ARGUS_PROPANE_FAR_EAST_INDEX_VS_EUROPEAN_PROPANE_CIFARA_ARGUS: str = "A91"
        """Argus Propane Far East Index vs. European Propane CIF ARA (Argus) Futures"""

        ARGUS_PROPANE_SAUDI_ARAMCO: str = "A9N"
        """Argus Propane (Saudi Aramco) Futures"""

        GROUP_THREE_ULSD_PLATTS_VS_NY_HARBOR_ULSD: str = "AA6"
        """Group Three ULSD (Platts) vs. NY Harbor ULSD Futures"""

        GROUP_THREE_SUBOCTANE_GASOLINE_PLATTS_VS_RBOB: str = "AA8"
        """Group Three Sub-octane Gasoliine (Platts) vs. RBOB Futures"""

        SINGAPORE_FUEL_OIL_180_CST_PLATTS_BALMO: str = "ABS"
        """Singapore Fuel Oil 180 cst (Platts) BALMO Futures"""

        SINGAPORE_FUEL_OIL_380_CST_PLATTS_BALMO: str = "ABT"
        """Singapore Fuel Oil 380 cst (Platts) BALMO Futures"""

        MONT_BELVIEU_ETHANE_OPIS: str = "AC0"
        """Mont Belvieu Ethane (OPIS) Futures"""

        MONT_BELVIEU_NORMAL_BUTANE_OPIS: str = "AD0"
        """Mont Belvieu Normal Butane (OPIS) Futures"""

        BRENT_CRUDE_OIL_VS_DUBAI_CRUDE_OIL_PLATTS: str = "ADB"
        """Brent Crude Oil vs. Dubai Crude Oil (Platts) Futures"""

        ARGUS_LL_SVS_WTI_ARGUS_TRADE_MONTH: str = "AE5"
        """Argus LLS vs. WTI (Argus) Trade Month Futures"""

        SINGAPORE_GASOIL_PLATTS_VS_LOW_SULPHUR_GASOIL_FUTURES: str = "AGA"
        """Singapore Gasoil (Platts) vs. Low Sulphur Gasoil Futures"""

        LOS_ANGELES_CARBOB_GASOLINE_OPI_SVS_RBOB_GASOLINE: str = "AJL"
        """Los Angeles CARBOB Gasoline (OPIS) vs. RBOB Gasoline Futures"""

        LOS_ANGELES_JET_OPI_SVS_NY_HARBOR_ULSD: str = "AJS"
        """Los Angeles Jet (OPIS) vs. NY Harbor ULSD Futures"""

        LOS_ANGELES_CARB_DIESEL_OPI_SVS_NY_HARBOR_ULSD: str = "AKL"
        """Los Angeles CARB Diesel (OPIS) vs. NY Harbor ULSD Futures"""

        EUROPEAN_NAPHTHA_PLATTS_BALMO: str = "AKZ"
        """European Naphtha (Platts) BALMO Futures"""

        EUROPEAN_PROPANE_CIFARA_ARGUS: str = "APS"
        """European Propane CIF ARA (Argus) Futures"""

        MONT_BELVIEU_NATURAL_GASOLINE_OPISBALMO: str = "AR0"
        """Mont Belvieu Natural Gasoline (OPIS) BALMO Futures"""

        RBOB_GASOLINE_CRACK_SPREAD: str = "ARE"
        """RBOB Gasoline Crack Spread Futures"""

        GULF_COAST_HSFO_PLATTS_BALMO: str = "AVZ"
        """Gulf Coast HSFO (Platts) BALMO Futures"""

        MARS_ARGUS_VS_WTI_TRADE_MONTH: str = "AYV"
        """Mars (Argus) vs. WTI Trade Month Futures"""

        MARS_ARGUS_VS_WTI_FINANCIAL: str = "AYX"
        """Mars (Argus) vs. WTI Financial Futures"""

        ETHANOL_T_2_FOB_RDAM_INCLUDING_DUTY_PLATTS: str = "AZ1"
        """Ethanol T2 FOB Rdam Including Duty (Platts) Futures"""

        MONT_BELVIEU_LDH_PROPANE_OPIS: str = "B0"
        """Mont Belvieu LDH Propane (OPIS) Futures"""

        GASOLINE_EUROBOB_OXY_NWE_BARGES_ARGUS: str = "B7H"
        """Gasoline Euro-bob Oxy NWE Barges (Argus) Futures"""

        WTI_BRENT_FINANCIAL: str = "BK"
        """WTI-Brent Financial Futures"""

        THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS_CRACK_SPREAD_1000_MT: str = "BOO"
        """3.5% Fuel Oil Barges FOB Rdam (Platts) Crack Spread (1000mt) Futures"""

        GASOLINE_EUROBOB_OXY_NWE_BARGES_ARGUS_BALMO: str = "BR7"
        """Gasoline Euro-bob Oxy NWE Barges (Argus) BALMO Futures"""

        BRENT_LAST_DAY_FINANCIAL: str = "BZ"
        """Brent Last Day Financial Futures"""

        CRUDE_OIL_WTI: str = "CL"
        """Crude Oil WTI Futures"""

        GULF_COAST_CBOB_GASOLINE_A_2_PLATTS_VS_RBOB_GASOLINE: str = "CRB"
        """Gulf Coast CBOB Gasoline A2 (Platts) vs. RBOB Gasoline Futures"""

        CLEARBROOK_BAKKEN_SWEET_CRUDE_OIL_MONTHLY_INDEX_NET_ENERGY: str = "CSW"
        """Clearbrook Bakken Sweet Crude Oil Monthly Index (Net Energy) Futures"""

        WTI_FINANCIAL: str = "CSX"
        """WTI Financial Futures"""

        CHICAGO_ETHANOL_PLATTS: str = "CU"
        """Chicago Ethaanol (Platts) Futures"""

        SINGAPORE_MOGAS_92_UNLEADED_PLATTS_BRENT_CRACK_SPREAD: str = "D1N"
        """Singapore Mogas 92 Unleaded (Platts) Brent Crack Spread Futures"""

        DUBAI_CRUDE_OIL_PLATTS_FINANCIAL: str = "DCB"
        """Dubai Crude Oil (Platts) Financial Futures"""

        JAPAN_CN_F_NAPHTHA_PLATTS_BALMO: str = "E6"
        """Japan C&F Naphtha (Platts) BALMO Futures"""

        ETHANOL: str = "EH"
        """Ethanol Futures"""

        EUROPEAN_NAPHTHA_PLATTS_CRACK_SPREAD: str = "EN"
        """European Naphtha (Platts) Crack Spread Futures"""

        EUROPEAN_PROPANE_CIFARA_ARGUS_VS_NAPHTHA_CARGOES_CIFNWE_PLATTS: str = "EPN"
        """European Propane CIF ARA (Argus) vs. Naphtha Cargoes CIF NWE (Platts) Futures"""

        SINGAPORE_FUEL_OIL_380_CST_PLATTS_VS_EUROPEAN_THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS: str = "EVC"
        """Singapore Fuel Oil 380 cst (Platts) vs. European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        EAST_WEST_GASOLINE_SPREAD_PLATTS_ARGUS: str = "EWG"
        """East-West Gasoline Spread (Platts-Argus) Futures"""

        EAST_WEST_NAPHTHA_JAPAN_C_FVS_CARGOES_CIFNWE_SPREAD_PLATTS: str = "EWN"
        """East-West Naphtha: Japan C&F vs. Cargoes CIF NWE Spread (Platts) Futures"""

        RBOB_GASOLINE_VS_EUROBOB_OXY_NWE_BARGES_ARGUS_THREE_HUNDRED_FIFTY_THOUSAND_GALLONS: str = "EXR"
        """RBOB Gasoline vs. Euro-bob Oxy NWE Barges (Argus) (350,000 gallons) Futures"""

        THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS_CRACK_SPREAD: str = "FO"
        """3.5% Fuel Oil Barges FOB Rdam (Platts) Crack Spread Futures"""

        FREIGHT_ROUTE_TC_14_BALTIC: str = "FRC"
        """Freight Route TC14 (Baltic) Futures"""

        ONE_PERCENT_FUEL_OIL_CARGOES_FOBNWE_PLATTS_VS_THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS: str = "FSS"
        """1% Fuel Oil Cargoes FOB NWE (Platts) vs. 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        GULF_COAST_HSFO_PLATTS_VS_EUROPEAN_THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS: str = "GCU"
        """Gulf Coast HSFO (Platts) vs. European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        WTI_HOUSTON_CRUDE_OIL: str = "HCL"
        """WTI Houston Crude Oil Futures"""

        NATURAL_GAS_HENRY_HUB_LAST_DAY_FINANCIAL: str = "HH"
        """Natural Gas (Henry Hub) Last-day Financial Futures"""

        HEATING_OIL: str = "HO"
        """Heating Oil Futures"""

        NATURAL_GAS_HENRY_HUB_PENULTIMATE_FINANCIAL: str = "HP"
        """Natural Gas (Henry Hub) Penultimate Financial Futures"""

        WTI_HOUSTON_ARGUS_VS_WTI_TRADE_MONTH: str = "HTT"
        """WTI Houston (Argus) vs. WTI Trade Month Futures"""

        GASOLINE: str = "RB"
        """Gasoline RBOB Futures"""

        NATURAL_GAS: str = "NG"
        """Natural Gas Futures"""

        BRENT_CRUDE: str = "B"
        """Brent Crude Futures"""

        LOW_SULFUR_GASOIL: str = "G"
        """Low Sulfur Gasoil"""

        MICRO_CRUDE_OIL_WTI: str = "MCL"
        """Micro WTI Crude Oil Futures"""

        MICRO_SINGAPORE_FOB_MARINE_FUEL_ZERO_POINT_FIVE_PERCET_PLATTS: str = "S5O"
        """Micro Singapore FOB Marine Fuel 0.5% (Platts) Futures"""

        MICRO_GASOIL_ZERO_POINT_ONE_PERCENT_BARGES_FOBARA_PLATTS: str = "M1B"
        """Micro Gasoil 0.1% Barges FOB ARA (Platts) Futures"""

        MICRO_EUROPEAN_FOB_RDAM_MARINE_FUEL_ZERO_POINT_FIVE_PERCENT_BARGES_PLATTS: str = "R5O"
        """Micro European FOB Rdam Marine Fuel 0.5% Barges (Platts) Futures"""

        MICRO_EUROPEAN_THREE_POINT_FIVE_PERCENT_OIL_BARGES_FOB_RDAM_PLATTS: str = "MEF"
        """Micro European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        MICRO_SINGAPORE_FUEL_OIL_380_CST_PLATTS: str = "MAF"
        """Micro Singapore Fuel Oil 380CST (Platts) Futures"""

        MICRO_COAL_API_FIVEFOB_NEWCASTLE_ARGUS_MC_CLOSKEY: str = "M5F"
        """Micro Coal (API 5) fob Newcastle (Argus/McCloskey) Futures"""

        MICRO_EUROPEAN_THREE_POINT_FIVE_PERCENT_FUEL_OIL_CARGOES_FOB_MED_PLATTS: str = "M35"
        """Micro European 3.5% Fuel Oil Cargoes FOB Med (Platts) Futures"""

    class Energy(System.Object):
        """Energy group"""

        PROPANE_NON_LDH_MONT_BELVIEU: str = "1S"
        """Propane Non LDH Mont Belvieu (OPIS) BALMO Futures"""

        ARGUS_PROPANE_FAR_EAST_INDEX_BALMO: str = "22"
        """Argus Propane Far East Index BALMO Futures"""

        MINI_EUROPEAN_THREE_POINT_PERCENT_FIVE_FUEL_OIL_BARGES_PLATTS: str = "A0D"
        """Mini European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        MINI_SINGAPORE_FUEL_OIL_180_CST_PLATTS: str = "A0F"
        """Mini Singapore Fuel Oil 180 cst (Platts) Futures"""

        GULF_COAST_ULSD_PLATTS_UP_DOWN_BALMO: str = "A1L"
        """Gulf Coast ULSD (Platts) Up-Down BALMO Futures"""

        GULF_COAST_JET_PLATTS_UP_DOWN_BALMO: str = "A1M"
        """Gulf Coast Jet (Platts) Up-Down BALMO Futures"""

        PROPANE_NON_LDH_MONT_BELVIEU_OPIS: str = "A1R"
        """Propane Non-LDH Mont Belvieu (OPIS) Futures"""

        EUROPEAN_PROPANE_CIFARA_ARGUS_BALMO: str = "A32"
        """European Propane CIF ARA (Argus) BALMO Futures"""

        PREMIUM_UNLEADED_GASOLINE_10_PPM_FOBMED_PLATTS: str = "A3G"
        """Premium Unleaded Gasoline 10 ppm FOB MED (Platts) Futures"""

        ARGUS_PROPANE_FAR_EAST_INDEX: str = "A7E"
        """Argus Propane Far East Index Futures"""

        GASOLINE_EUROBOB_OXY_NWE_BARGES_ARGUS_CRACK_SPREAD_BALMO: str = "A7I"
        """Gasoline Euro-bob Oxy NWE Barges (Argus) Crack Spread BALMO Futures"""

        MONT_BELVIEU_NATURAL_GASOLINE_OPIS: str = "A7Q"
        """Mont Belvieu Natural Gasoline (OPIS) Futures"""

        MONT_BELVIEU_NORMAL_BUTANE_OPISBALMO: str = "A8J"
        """Mont Belvieu Normal Butane (OPIS) BALMO Futures"""

        CONWAY_PROPANE_OPIS: str = "A8K"
        """Conway Propane (OPIS) Futures"""

        MONT_BELVIEU_LDH_PROPANE_OPISBALMO: str = "A8O"
        """Mont Belvieu LDH Propane (OPIS) BALMO Futures"""

        ARGUS_PROPANE_FAR_EAST_INDEX_VS_EUROPEAN_PROPANE_CIFARA_ARGUS: str = "A91"
        """Argus Propane Far East Index vs. European Propane CIF ARA (Argus) Futures"""

        ARGUS_PROPANE_SAUDI_ARAMCO: str = "A9N"
        """Argus Propane (Saudi Aramco) Futures"""

        GROUP_THREE_ULSD_PLATTS_VS_NY_HARBOR_ULSD: str = "AA6"
        """Group Three ULSD (Platts) vs. NY Harbor ULSD Futures"""

        GROUP_THREE_SUBOCTANE_GASOLINE_PLATTS_VS_RBOB: str = "AA8"
        """Group Three Sub-octane Gasoliine (Platts) vs. RBOB Futures"""

        SINGAPORE_FUEL_OIL_180_CST_PLATTS_BALMO: str = "ABS"
        """Singapore Fuel Oil 180 cst (Platts) BALMO Futures"""

        SINGAPORE_FUEL_OIL_380_CST_PLATTS_BALMO: str = "ABT"
        """Singapore Fuel Oil 380 cst (Platts) BALMO Futures"""

        MONT_BELVIEU_ETHANE_OPIS: str = "AC0"
        """Mont Belvieu Ethane (OPIS) Futures"""

        MONT_BELVIEU_NORMAL_BUTANE_OPIS: str = "AD0"
        """Mont Belvieu Normal Butane (OPIS) Futures"""

        BRENT_CRUDE_OIL_VS_DUBAI_CRUDE_OIL_PLATTS: str = "ADB"
        """Brent Crude Oil vs. Dubai Crude Oil (Platts) Futures"""

        ARGUS_LL_SVS_WTI_ARGUS_TRADE_MONTH: str = "AE5"
        """Argus LLS vs. WTI (Argus) Trade Month Futures"""

        SINGAPORE_GASOIL_PLATTS_VS_LOW_SULPHUR_GASOIL_FUTURES: str = "AGA"
        """Singapore Gasoil (Platts) vs. Low Sulphur Gasoil Futures"""

        LOS_ANGELES_CARBOB_GASOLINE_OPI_SVS_RBOB_GASOLINE: str = "AJL"
        """Los Angeles CARBOB Gasoline (OPIS) vs. RBOB Gasoline Futures"""

        LOS_ANGELES_JET_OPI_SVS_NY_HARBOR_ULSD: str = "AJS"
        """Los Angeles Jet (OPIS) vs. NY Harbor ULSD Futures"""

        LOS_ANGELES_CARB_DIESEL_OPI_SVS_NY_HARBOR_ULSD: str = "AKL"
        """Los Angeles CARB Diesel (OPIS) vs. NY Harbor ULSD Futures"""

        EUROPEAN_NAPHTHA_PLATTS_BALMO: str = "AKZ"
        """European Naphtha (Platts) BALMO Futures"""

        EUROPEAN_PROPANE_CIFARA_ARGUS: str = "APS"
        """European Propane CIF ARA (Argus) Futures"""

        MONT_BELVIEU_NATURAL_GASOLINE_OPISBALMO: str = "AR0"
        """Mont Belvieu Natural Gasoline (OPIS) BALMO Futures"""

        RBOB_GASOLINE_CRACK_SPREAD: str = "ARE"
        """RBOB Gasoline Crack Spread Futures"""

        GULF_COAST_HSFO_PLATTS_BALMO: str = "AVZ"
        """Gulf Coast HSFO (Platts) BALMO Futures"""

        MARS_ARGUS_VS_WTI_TRADE_MONTH: str = "AYV"
        """Mars (Argus) vs. WTI Trade Month Futures"""

        MARS_ARGUS_VS_WTI_FINANCIAL: str = "AYX"
        """Mars (Argus) vs. WTI Financial Futures"""

        ETHANOL_T_2_FOB_RDAM_INCLUDING_DUTY_PLATTS: str = "AZ1"
        """Ethanol T2 FOB Rdam Including Duty (Platts) Futures"""

        MONT_BELVIEU_LDH_PROPANE_OPIS: str = "B0"
        """Mont Belvieu LDH Propane (OPIS) Futures"""

        GASOLINE_EUROBOB_OXY_NWE_BARGES_ARGUS: str = "B7H"
        """Gasoline Euro-bob Oxy NWE Barges (Argus) Futures"""

        WTI_BRENT_FINANCIAL: str = "BK"
        """WTI-Brent Financial Futures"""

        THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS_CRACK_SPREAD_1000_MT: str = "BOO"
        """3.5% Fuel Oil Barges FOB Rdam (Platts) Crack Spread (1000mt) Futures"""

        GASOLINE_EUROBOB_OXY_NWE_BARGES_ARGUS_BALMO: str = "BR7"
        """Gasoline Euro-bob Oxy NWE Barges (Argus) BALMO Futures"""

        BRENT_LAST_DAY_FINANCIAL: str = "BZ"
        """Brent Last Day Financial Futures"""

        CRUDE_OIL_WTI: str = "CL"
        """Crude Oil WTI Futures"""

        GULF_COAST_CBOB_GASOLINE_A_2_PLATTS_VS_RBOB_GASOLINE: str = "CRB"
        """Gulf Coast CBOB Gasoline A2 (Platts) vs. RBOB Gasoline Futures"""

        CLEARBROOK_BAKKEN_SWEET_CRUDE_OIL_MONTHLY_INDEX_NET_ENERGY: str = "CSW"
        """Clearbrook Bakken Sweet Crude Oil Monthly Index (Net Energy) Futures"""

        WTI_FINANCIAL: str = "CSX"
        """WTI Financial Futures"""

        CHICAGO_ETHANOL_PLATTS: str = "CU"
        """Chicago Ethaanol (Platts) Futures"""

        SINGAPORE_MOGAS_92_UNLEADED_PLATTS_BRENT_CRACK_SPREAD: str = "D1N"
        """Singapore Mogas 92 Unleaded (Platts) Brent Crack Spread Futures"""

        DUBAI_CRUDE_OIL_PLATTS_FINANCIAL: str = "DCB"
        """Dubai Crude Oil (Platts) Financial Futures"""

        JAPAN_CN_F_NAPHTHA_PLATTS_BALMO: str = "E6"
        """Japan C&F Naphtha (Platts) BALMO Futures"""

        ETHANOL: str = "EH"
        """Ethanol Futures"""

        EUROPEAN_NAPHTHA_PLATTS_CRACK_SPREAD: str = "EN"
        """European Naphtha (Platts) Crack Spread Futures"""

        EUROPEAN_PROPANE_CIFARA_ARGUS_VS_NAPHTHA_CARGOES_CIFNWE_PLATTS: str = "EPN"
        """European Propane CIF ARA (Argus) vs. Naphtha Cargoes CIF NWE (Platts) Futures"""

        SINGAPORE_FUEL_OIL_380_CST_PLATTS_VS_EUROPEAN_THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS: str = "EVC"
        """Singapore Fuel Oil 380 cst (Platts) vs. European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        EAST_WEST_GASOLINE_SPREAD_PLATTS_ARGUS: str = "EWG"
        """East-West Gasoline Spread (Platts-Argus) Futures"""

        EAST_WEST_NAPHTHA_JAPAN_C_FVS_CARGOES_CIFNWE_SPREAD_PLATTS: str = "EWN"
        """East-West Naphtha: Japan C&F vs. Cargoes CIF NWE Spread (Platts) Futures"""

        RBOB_GASOLINE_VS_EUROBOB_OXY_NWE_BARGES_ARGUS_THREE_HUNDRED_FIFTY_THOUSAND_GALLONS: str = "EXR"
        """RBOB Gasoline vs. Euro-bob Oxy NWE Barges (Argus) (350,000 gallons) Futures"""

        THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS_CRACK_SPREAD: str = "FO"
        """3.5% Fuel Oil Barges FOB Rdam (Platts) Crack Spread Futures"""

        FREIGHT_ROUTE_TC_14_BALTIC: str = "FRC"
        """Freight Route TC14 (Baltic) Futures"""

        ONE_PERCENT_FUEL_OIL_CARGOES_FOBNWE_PLATTS_VS_THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS: str = "FSS"
        """1% Fuel Oil Cargoes FOB NWE (Platts) vs. 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        GULF_COAST_HSFO_PLATTS_VS_EUROPEAN_THREE_POINT_FIVE_PERCENT_FUEL_OIL_BARGES_FOB_RDAM_PLATTS: str = "GCU"
        """Gulf Coast HSFO (Platts) vs. European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        WTI_HOUSTON_CRUDE_OIL: str = "HCL"
        """WTI Houston Crude Oil Futures"""

        NATURAL_GAS_HENRY_HUB_LAST_DAY_FINANCIAL: str = "HH"
        """Natural Gas (Henry Hub) Last-day Financial Futures"""

        HEATING_OIL: str = "HO"
        """Heating Oil Futures"""

        NATURAL_GAS_HENRY_HUB_PENULTIMATE_FINANCIAL: str = "HP"
        """Natural Gas (Henry Hub) Penultimate Financial Futures"""

        WTI_HOUSTON_ARGUS_VS_WTI_TRADE_MONTH: str = "HTT"
        """WTI Houston (Argus) vs. WTI Trade Month Futures"""

        GASOLINE: str = "RB"
        """Gasoline RBOB Futures"""

        NATURAL_GAS: str = "NG"
        """Natural Gas Futures"""

        BRENT_CRUDE: str = "B"
        """Brent Crude Futures"""

        LOW_SULFUR_GASOIL: str = "G"
        """Low Sulfur Gasoil"""

        MICRO_CRUDE_OIL_WTI: str = "MCL"
        """Micro WTI Crude Oil Futures"""

        MICRO_SINGAPORE_FOB_MARINE_FUEL_ZERO_POINT_FIVE_PERCET_PLATTS: str = "S5O"
        """Micro Singapore FOB Marine Fuel 0.5% (Platts) Futures"""

        MICRO_GASOIL_ZERO_POINT_ONE_PERCENT_BARGES_FOBARA_PLATTS: str = "M1B"
        """Micro Gasoil 0.1% Barges FOB ARA (Platts) Futures"""

        MICRO_EUROPEAN_FOB_RDAM_MARINE_FUEL_ZERO_POINT_FIVE_PERCENT_BARGES_PLATTS: str = "R5O"
        """Micro European FOB Rdam Marine Fuel 0.5% Barges (Platts) Futures"""

        MICRO_EUROPEAN_THREE_POINT_FIVE_PERCENT_OIL_BARGES_FOB_RDAM_PLATTS: str = "MEF"
        """Micro European 3.5% Fuel Oil Barges FOB Rdam (Platts) Futures"""

        MICRO_SINGAPORE_FUEL_OIL_380_CST_PLATTS: str = "MAF"
        """Micro Singapore Fuel Oil 380CST (Platts) Futures"""

        MICRO_COAL_API_FIVEFOB_NEWCASTLE_ARGUS_MC_CLOSKEY: str = "M5F"
        """Micro Coal (API 5) fob Newcastle (Argus/McCloskey) Futures"""

        MICRO_EUROPEAN_THREE_POINT_FIVE_PERCENT_FUEL_OIL_CARGOES_FOB_MED_PLATTS: str = "M35"
        """Micro European 3.5% Fuel Oil Cargoes FOB Med (Platts) Futures"""

    class Financials(System.Object):
        """Financials group"""

        Y_30_TREASURY_BOND: str = "ZB"
        """30Y U.S. Treasury Bond Futures"""

        Y_10_TREASURY_NOTE: str = "ZN"
        """10Y U.S. Treasury Note Futures"""

        Y_5_TREASURY_NOTE: str = "ZF"
        """5Y U.S. Treasury Note Futures"""

        Y_2_TREASURY_NOTE: str = "ZT"
        """2Y U.S. Treasury Note Futures"""

        EURO_DOLLAR: str = "GE"
        """EuroDollar Futures"""

        FIVE_YEAR_USDMAC_SWAP: str = "F1U"
        """5-Year USD MAC Swap Futures"""

        ULTRA_US_TREASURY_BOND: str = "UB"
        """Ultra U.S. Treasury Bond Futures"""

        ULTRA_TEN_YEAR_US_TREASURY_NOTE: str = "TN"
        """Ultra 10-Year U.S. Treasury Note Futures"""

        MICRO_Y_10_TREASURY_NOTE: str = "10Y"
        """Micro 10-Year Yield Futures"""

        MICRO_Y_30_TREASURY_BOND: str = "30Y"
        """Micro 30-Year Yield Futures"""

        MICRO_Y_2_TREASURY_BOND: str = "2YY"
        """Micro 2-Year Yield Futures"""

        MICRO_Y_5_TREASURY_BOND: str = "5YY"
        """Micro 5-Year Yield Futures"""

    class Indices(System.Object):
        """Indices group"""

        SP_500_E_MINI: str = "ES"
        """E-mini S&P 500 Futures"""

        NASDAQ_100_E_MINI: str = "NQ"
        """E-mini NASDAQ 100 Futures"""

        DOW_30_E_MINI: str = "YM"
        """E-mini Dow Indu 30 Futures"""

        VIX: str = "VX"
        """CBOE Volatility Index Futures"""

        RUSSELL_2000_E_MINI: str = "RTY"
        """E-mini Russell 2000 Futures"""

        NIKKEI_225_DOLLAR: str = "NKD"
        """Nikkei-225 Dollar Futures"""

        NIKKEI_225_YEN_CME: str = "NIY"
        """Nikkei-225 Yen denominated Futures on CME"""

        NIKKEI_225_YEN_E_MINI: str = "ENY"
        """E-mini Nikkei 225 Yen denominated Futures on CME"""

        FTSE_CHINA_50_E_MINI: str = "FT5"
        """E-MINI FTSE China 50 Index Futures on CME"""

        FTSE_100_E_MINI: str = "FT1"
        """E-mini FTSE 100 Index (GBP) Futures on CME"""

        SP_EUROP_350_ESGE_MINI: str = "E3G"

        FTSE_100_USDE_MINI: str = "FTU"
        """E-MINI USD Denominated FTSE 100 Index Futures on CME"""

        TOPIXUSD: str = "TPD"
        """USD Denominated Topix Index Futures on CME"""

        TOPIXYEN: str = "TPY"
        """YEN Denominated Topix Index Futures on CME"""

        DOW_JONES_REAL_ESTATE: str = "RX"
        """Dow Jones Real Estate futures on CME"""

        SP_500_E_MINI_ESG: str = "ESG"
        """E-mini SP500 ESG futures on CME"""

        RUSSELL_1000_E_MINI: str = "RS1"
        """E-mini Russell 1000 futures on CME"""

        SP_500_ANNUAL_DIVIDEND_INDEX: str = "SDA"

        BLOOMBERG_COMMODITY_INDEX: str = "AW"
        """Bloomberg Commodity Index Futures"""

        NASDAQ_100_BIOTECHNOLOGY_E_MINI: str = "BIO"
        """E-mini Nasdaq-100 Biotechnology Index Futures"""

        FTSE_EMERGING_EMINI: str = "EI"
        """E-mini FTSE Emerging Index Futures"""

        SP_400_MID_CAP_EMINI: str = "EMD"
        """E-mini S&P MidCap 400 Futures"""

        SPGSCI_COMMODITY: str = "GD"
        """S&P-GSCI Commodity Index Futures"""

        USD_DENOMINATED_IBOVESPA: str = "IBV"
        """USD-Denominated Ibovespa Index Futures"""

        MSCI_TAIWAN_INDEX: str = "TW"
        """USD-Denominated MSCI Taiwan Index Futures"""

        NIKKEI_225_YEN: str = "NK"
        """Nikkei-225 Yen denominated Index Futures"""

        NIFTY_50: str = "NIFTY"
        """NSE Nifty50 Index Futures"""

        BANK_NIFTY: str = "BANKNIFTY"
        """NSE BankNifty Futures"""

        BSE_SENSEX: str = "SENSEX"
        """S&P BSE Sensex Index Futures"""

        HANG_SENG: str = "HSI"
        """Hang Seng Index"""

        MICRO_SP_500_E_MINI: str = "MES"
        """Micro E-mini S&P 500 Index Futures"""

        MICRO_NASDAQ_100_E_MINI: str = "MNQ"
        """Micro E-mini Nasdaq-100 Index Futures"""

        MICRO_RUSSELL_2000_E_MINI: str = "M2K"
        """Micro E-mini Russell 2000 Index Futures"""

        MICRO_DOW_30_E_MINI: str = "MYM"
        """Micro E-mini Dow Jones Industrial Average Index Futures"""

        MSCI_EUROPE_NTR: str = "M1EU"
        """MSCI Europe Net Total Return (USD) Futures"""

        MSCI_JAPAN_NTR: str = "M1JP"
        """MSCI Japan Net Total Return Futures"""

        MSCI_EMERGING_MARKETS_ASIA_NTR: str = "M1MSA"
        """MSCI Emerging Markets Asia Net Total Return Futures"""

        MSCI_EAFE_INDEX: str = "MXEA"
        """MSCI EAFE Index Futures"""

        MSCI_EMERGING_MARKETS_INDEX: str = "MXEF"
        """MSCI Emerging Markets Index Futures"""

        MSCI_USA_INDEX: str = "MXUS"
        """MSCI USA Index Futures"""

        EURO_STOXX_50: str = "FESX"
        """Euro Stoxx 50 Index Futures"""

    class Forestry(System.Object):
        """Forestry group"""

        RANDOM_LENGTH_LUMBER: str = "LBS"
        """Random Length Lumber Futures"""

        LUMBER: str = "LBR"
        """Lumber Futures"""

    class Meats(System.Object):
        """Meats group"""

        LIVE_CATTLE: str = "LE"
        """Live Cattle Futures"""

        FEEDER_CATTLE: str = "GF"
        """Feeder Cattle Futures"""

        LEAN_HOGS: str = "HE"
        """Lean Hogs Futures"""

    class Metals(System.Object):
        """Metals group"""

        GOLD: str = "GC"
        """Gold Futures"""

        SILVER: str = "SI"
        """Silver Futures"""

        PLATINUM: str = "PL"
        """Platinum Futures"""

        PALLADIUM: str = "PA"
        """Palladium Futures"""

        ALUMINUM_MWUS_TRANSACTION_PREMIUM_PLATTS_25_MT: str = "AUP"
        """Aluminum MW U.S. Transaction Premium Platts (25MT) Futures"""

        ALUMINIUM_EUROPEAN_PREMIUM_DUTY_PAID_METAL_BULLETIN: str = "EDP"
        """Aluminium European Premium Duty-Paid (Metal Bulletin) Futures"""

        COPPER: str = "HG"
        """Copper Futures"""

        US_MIDWEST_DOMESTIC_HOT_ROLLED_COIL_STEEL_CRU_INDEX: str = "HRC"
        """U.S. Midwest Domestic Hot-Rolled Coil Steel (CRU) Index Futures"""

        MICRO_GOLD: str = "MGC"
        """Micro Gold Futures"""

        MICRO_SILVER: str = "SIL"
        """Micro Silver Futures"""

        MICRO_GOLD_TAS: str = "MGT"
        """Micro Gold TAS Futures"""

        MICRO_PALLADIUM: str = "PAM"
        """Micro Palladium Futures"""

        MINI_NY_GOLD: str = "YG"
        """Mini Sized NY Gold Futures"""

        MINI_NY_SILVER: str = "YI"
        """Mini Sized NY Silver Futures"""

        GOLD_100_OZ: str = "ZG"
        """Gold 100 Oz Futures"""

        SILVER_5000_OZ: str = "ZI"
        """Silver 5000 Oz Futures"""

    class Softs(System.Object):
        """Softs group"""

        COTTON_2: str = "CT"
        """Cotton #2 Futures"""

        ORANGE_JUICE: str = "OJ"
        """Orange Juice Futures"""

        COFFEE: str = "KC"
        """Coffee C Arabica Futures"""

        SUGAR_11: str = "SB"
        """Sugar #11 Futures ICE"""

        SUGAR_11_CME: str = "YO"
        """Sugar #11 Futures CME"""

        COCOA: str = "CC"
        """Cocoa Futures"""

    class Dairy(System.Object):
        """Dairy group"""

        CASH_SETTLED_BUTTER: str = "CB"
        """Cash-settled Butter Futures"""

        CASH_SETTLED_CHEESE: str = "CSC"
        """Cash-settled Cheese Futures"""

        CLASS_III_MILK: str = "DC"
        """Class III Milk Futures"""

        DRY_WHEY: str = "DY"
        """Dry Whey Futures"""

        CLASS_IV_MILK: str = "GDK"
        """Class IV Milk Futures"""

        NONFAT_DRY_MILK: str = "GNF"
        """Non-fat Dry Milk Futures"""

    MAXIMUM_CONTRACT_DEPTH_OFFSET: int = 2
    """The maximum supported contract offset depth"""


class FutureFilterUniverse(QuantConnect.Securities.ContractSecurityFilterUniverse[QuantConnect_Securities_FutureFilterUniverse, QuantConnect.Symbol]):
    """Represents futures symbols universe used in filtering."""

    def __init__(self, allSymbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], localTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Constructs FutureFilterUniverse"""
        ...

    def create_data_instance(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Symbol:
        """
        Creates a new instance of the data type for the given symbol
        
        This method is protected.
        
        :returns: A data instance for the given symbol, which is just the symbol itself.
        """
        ...

    def expiration_cycle(self, months: typing.List[int]) -> QuantConnect.Securities.FutureFilterUniverse:
        """
        Applies filter selecting futures contracts based on expiration cycles. See FutureExpirationCycles for details
        
        :param months: Months to select contracts from
        :returns: Universe with filter applied.
        """
        ...

    def get_symbol(self, data: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Symbol:
        """
        Gets the symbol from the data
        
        This method is protected.
        
        :returns: The symbol that represents the datum.
        """
        ...

    def is_standard(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determine if the given Future contract symbol is standard
        
        This method is protected.
        
        :returns: True if contract is standard.
        """
        ...


class FutureFilterUniverseEx(System.Object):
    """Extensions for Linq support"""

    @staticmethod
    def select(universe: QuantConnect.Securities.FutureFilterUniverse, map_func: typing.Callable[[QuantConnect.Symbol], QuantConnect.Symbol]) -> QuantConnect.Securities.FutureFilterUniverse:
        """
        Maps universe
        
        :param universe: Universe to apply the filter too
        :param map_func: Symbol function to determine which Symbols are filtered
        :returns: FutureFilterUniverse with filter applied.
        """
        ...

    @staticmethod
    def select_many(universe: QuantConnect.Securities.FutureFilterUniverse, map_func: typing.Callable[[QuantConnect.Symbol], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Securities.FutureFilterUniverse:
        """
        Binds universe
        
        :param universe: Universe to apply the filter too
        :param map_func: Symbols function to determine which Symbols are filtered
        :returns: FutureFilterUniverse with filter applied.
        """
        ...

    @staticmethod
    def where(universe: QuantConnect.Securities.FutureFilterUniverse, predicate: typing.Callable[[QuantConnect.Symbol], bool]) -> QuantConnect.Securities.FutureFilterUniverse:
        """
        Filters universe
        
        :param universe: Universe to apply the filter too
        :param predicate: Bool function to determine which Symbol are filtered
        :returns: FutureFilterUniverse with filter applied.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Securities__EventContainer_Callable, QuantConnect_Securities__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Securities__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Securities__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Securities__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


