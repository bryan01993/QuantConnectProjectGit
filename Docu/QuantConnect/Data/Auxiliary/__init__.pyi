from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Auxiliary
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Securities
import System
import System.Collections.Generic
import System.IO

QuantConnect_Data_Auxiliary_MapFileRow = typing.Any

QuantConnect_Data_Auxiliary_FactorFile_T = typing.TypeVar("QuantConnect_Data_Auxiliary_FactorFile_T")


class MapFileRow(System.Object, System.IEquatable[QuantConnect_Data_Auxiliary_MapFileRow]):
    """Represents a single row in a map_file. This is a csv file ordered as {date, mapped symbol}"""

    @property
    def date(self) -> datetime.datetime:
        """Gets the date associated with this data"""
        ...

    @property
    def mapped_symbol(self) -> str:
        """Gets the mapped symbol"""
        ...

    @property
    def primary_exchange(self) -> QuantConnect.Exchange:
        """Gets the mapped symbol"""
        ...

    @property
    def data_mapping_mode(self) -> typing.Optional[QuantConnect.DataMappingMode]:
        """Gets the securities mapping mode associated to this mapping row"""
        ...

    @overload
    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], mappedSymbol: str, primaryExchange: str, market: str = ..., securityType: QuantConnect.SecurityType = ..., dataMappingMode: typing.Optional[QuantConnect.DataMappingMode] = None) -> None:
        """Initializes a new instance of the MapFileRow class."""
        ...

    @overload
    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], mappedSymbol: str, primaryExchange: QuantConnect.Exchange = None, dataMappingMode: typing.Optional[QuantConnect.DataMappingMode] = None) -> None:
        """Initializes a new instance of the MapFileRow class."""
        ...

    @overload
    def equals(self, other: QuantConnect.Data.Auxiliary.MapFileRow) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified System.Object is equal to the current System.Object.
        
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

    @staticmethod
    def parse(line: str, market: str, security_type: QuantConnect.SecurityType) -> QuantConnect.Data.Auxiliary.MapFileRow:
        """Parses the specified line into a MapFileRow"""
        ...

    @staticmethod
    def read(file: str, market: str, security_type: QuantConnect.SecurityType, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.MapFileRow]:
        """Reads in the map_file for the specified equity symbol"""
        ...

    def to_csv(self) -> str:
        """Writes this row to csv format"""
        ...

    def to_string(self) -> str:
        """
        Convert this row into string form
        
        :returns: resulting string.
        """
        ...


class MapFile(System.Object, typing.Iterable[QuantConnect.Data.Auxiliary.MapFileRow]):
    """Represents an entire map file for a specified symbol"""

    @property
    def permtick(self) -> str:
        """Gets the entity's unique symbol, i.e OIH.1"""
        ...

    @property
    def delisting_date(self) -> datetime.datetime:
        """Gets the last date in the map file which is indicative of a delisting event"""
        ...

    @property
    def first_date(self) -> datetime.datetime:
        """Gets the first date in this map file"""
        ...

    @property
    def first_ticker(self) -> str:
        """Gets the first ticker for the security represented by this map file"""
        ...

    def __init__(self, permtick: str, data: System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.MapFileRow]) -> None:
        """Initializes a new instance of the MapFile class."""
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Auxiliary.MapFileRow]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    @staticmethod
    def get_map_files(map_file_directory: str, market: str, security_type: QuantConnect.SecurityType, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.MapFile]:
        """
        Reads all the map files in the specified directory
        
        :param map_file_directory: The map file directory path
        :param market: The map file market
        :param security_type: The map file security type
        :param data_provider: The data provider instance to use
        :returns: An enumerable of all map files.
        """
        ...

    def get_mapped_symbol(self, search_date: typing.Union[datetime.datetime, datetime.date], default_return_value: str = ..., data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None) -> str:
        """
        Memory overload search method for finding the mapped symbol for this date.
        
        :param search_date: date for symbol we need to find.
        :param default_return_value: Default return value if search was got no result.
        :param data_mapping_mode: The mapping mode to use if any.
        :returns: Symbol on this date.
        """
        ...

    @staticmethod
    def get_relative_map_file_path(market: str, security_type: QuantConnect.SecurityType) -> str:
        """
        Constructs the map file path for the specified market and symbol
        
        :param market: The market this symbol belongs to
        :param security_type: The map file security type
        :returns: The file path to the requested map file.
        """
        ...

    def has_data(self, date: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """Determines if there's data for the requested date"""
        ...

    def to_csv_lines(self) -> System.Collections.Generic.IEnumerable[str]:
        """
        Reads and writes each MapFileRow
        
        :returns: Enumerable of csv lines.
        """
        ...

    def write_to_csv(self, market: str, security_type: QuantConnect.SecurityType) -> None:
        """
        Writes the map file to a CSV file
        
        :param market: The market to save the MapFile to
        :param security_type: The map file security type
        """
        ...


class MapFileResolver(System.Object, typing.Iterable[QuantConnect.Data.Auxiliary.MapFile]):
    """
    Provides a means of mapping a symbol at a point in time to the map file
    containing that share class's mapping information
    """

    EMPTY: QuantConnect.Data.Auxiliary.MapFileResolver = ...
    """
    Gets an empty MapFileResolver, that is an instance that contains
    zero mappings
    """

    def __init__(self, mapFiles: System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.MapFile]) -> None:
        """
        Initializes a new instance of the MapFileResolver by reading
        in all files in the specified directory.
        
        :param mapFiles: The data used to initialize this resolver.
        """
        ...

    def get_by_permtick(self, permtick: str) -> QuantConnect.Data.Auxiliary.MapFile:
        """
        Gets the map file matching the specified permtick
        
        :param permtick: The permtick to match on
        :returns: The map file matching the permtick, or null if not found.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Auxiliary.MapFile]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    def resolve_map_file(self, symbol: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Auxiliary.MapFile:
        """
        Resolves the map file path containing the mapping information for the symbol defined at
        
        :param symbol: The symbol as of  to be mapped
        :param date: The date associated with the
        :returns: The map file responsible for mapping the symbol, if no map file is found, null is returned.
        """
        ...


class TickerDateRange:
    """Represents stock data for a specific ticker within a date range."""

    @property
    def ticker(self) -> str:
        """Ticker simple name of stock"""
        ...

    @property
    def start_date_time_local(self) -> datetime.datetime:
        """Ticker Start Date Time in Local"""
        ...

    @property
    def end_date_time_local(self) -> datetime.datetime:
        """Ticker End Date Time in Local"""
        ...

    def __init__(self, ticker: str, startDateTimeLocal: typing.Union[datetime.datetime, datetime.date], endDateTimeLocal: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Create the instance of TickerDateRange struct.
        
        :param ticker: Name of ticker
        :param startDateTimeLocal: Start Date Time Local
        :param endDateTimeLocal: End Date Time Local
        """
        ...


class SymbolDateRange:
    """Represents security identifier within a date range."""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Represents a unique security identifier."""
        ...

    @property
    def start_date_time_local(self) -> datetime.datetime:
        """Ticker Start Date Time in Local"""
        ...

    @property
    def end_date_time_local(self) -> datetime.datetime:
        """Ticker End Date Time in Local"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], startDateTimeLocal: typing.Union[datetime.datetime, datetime.date], endDateTimeLocal: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Create the instance of SymbolDateRange struct.
        
        :param symbol: The unique security identifier
        :param startDateTimeLocal: Start Date Time Local
        :param endDateTimeLocal: End Date Time Local
        """
        ...


class MappingExtensions(System.Object):
    """Mapping extensions helper methods"""

    @staticmethod
    @overload
    def resolve_map_file(map_file_provider: QuantConnect.Interfaces.IMapFileProvider, data_config: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.Auxiliary.MapFile:
        """
        Helper method to resolve the mapping file to use.
        
        :param map_file_provider: The map file provider
        :param data_config: The configuration to fetch the map file for
        :returns: The mapping file to use.
        """
        ...

    @staticmethod
    @overload
    def resolve_map_file(map_file_resolver: QuantConnect.Data.Auxiliary.MapFileResolver, symbol: typing.Union[QuantConnect.Symbol, str], data_type: str = None) -> QuantConnect.Data.Auxiliary.MapFile:
        """
        Helper method to resolve the mapping file to use.
        
        :param map_file_resolver: The map file resolver
        :param symbol: The symbol that we want to map
        :param data_type: The string data type name if any
        :returns: The mapping file to use.
        """
        ...

    @staticmethod
    def retrieve_all_mapped_symbol_in_date_range(map_file_provider: QuantConnect.Interfaces.IMapFileProvider, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.SymbolDateRange]:
        """
        Retrieves all Symbol from map files based on specific Symbol.
        
        :param map_file_provider: The provider for map files containing ticker data.
        :param symbol: The symbol to get MapFileResolver and generate new Symbol.
        :returns: An enumerable collection of SymbolDateRange.
        """
        ...

    @staticmethod
    def retrieve_symbol_historical_definitions_in_date_range(map_file_provider: QuantConnect.Interfaces.IMapFileProvider, symbol: typing.Union[QuantConnect.Symbol, str], start_date_time: typing.Union[datetime.datetime, datetime.date], end_date_time: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.TickerDateRange]:
        """
        Some historical provider supports ancient data. In fact, the ticker could be restructured to new one.
        
        :param map_file_provider: Provides instances of MapFileResolver at run time
        :param symbol: Represents a unique security identifier
        :param start_date_time: The date since we began our search for the historical name of the symbol.
        :param end_date_time: The end date and time of the historical data range.
        :returns: An enumerable collection of tuples containing symbol ticker, start date and time, and end date and time representing the historical definitions of the symbol within the specified time range.
        """
        ...


class TradeConditionFlags(Enum):
    """Flag system for trade conditions"""

    NONE = 0
    """No Condition"""

    REGULAR = ...
    """A trade made without stated conditions is deemed regular way for settlement on the third business day following the transaction date."""

    CASH = ...
    """A transaction which requires delivery of securities and payment on the same day the trade takes place."""

    NEXT_DAY = ...
    """A transaction that requires the delivery of securities on the first business day following the trade date."""

    SELLER = ...
    """
    A Seller’s Option transaction gives the seller the right to deliver the security at any time within a specific period,
    ranging from not less than two calendar days, to not more than sixty calendar days.
    """

    YELLOW_FLAG = ...
    """
    Market Centers will have the ability to identify regular trades being reported during specific events as out of the ordinary
    by appending a new sale condition code Yellow Flag (Y) on each transaction reported to the UTP SIP.
    The new sale condition will be eligible to update all market center and consolidated statistics.
    """

    INTERMARKET_SWEEP = ...
    """The transaction that constituted the trade-through was the execution of an order identified as an Intermarket Sweep Order."""

    OPENING_PRINTS = ...
    """The trade that constituted the trade-through was a single priced opening transaction by the Market Center."""

    CLOSING_PRINTS = ...
    """The transaction that constituted the trade-through was a single priced closing transaction by the Market Center."""

    RE_OPENING_PRINTS = ...
    """The trade that constituted the trade-through was a single priced reopening transaction by the Market Center."""

    DERIVATIVELY_PRICED = ...
    """
    The transaction that constituted the trade-through was the execution of an order at a price that was not based, directly or indirectly,
    on the quoted price of the security at the time of execution and for which the material terms were not reasonably determinable
    at the time the commitment to execute the order was made.
    """

    FORM_T = ...
    """
    Trading in extended hours enables investors to react quickly to events that typically occur outside regular market hours, such as earnings reports.
    However, liquidity may be constrained during such Form T trading, resulting in wide bid-ask spreads.
    """

    SOLD = ...
    """Sold Last is used when a trade prints in sequence but is reported late or printed in conformance to the One or Two Point Rule."""

    STOPPED = ...
    """
    The transaction that constituted the trade-through was the execution by a trading center of an order for which, at the time
    of receipt of the order, the execution at no worse than a specified price a 'stopped order'
    """

    EXTENDED_HOURS = ...
    """Identifies a trade that was executed outside of regular primary market hours and is reported as an extended hours trade."""

    OUT_OF_SEQUENCE = ...
    """Identifies a trade that takes place outside of regular market hours."""

    SPLIT = ...
    """
    An execution in two markets when the specialist or Market Maker in the market first receiving the order agrees to execute a portion of it
    at whatever price is realized in another market to which the balance of the order is forwarded for execution.
    """

    ACQUISITION = ...
    """A transaction made on the Exchange as a result of an Exchange acquisition."""

    BUNCHED = ...
    """
    A trade representing an aggregate of two or more regular trades in a security occurring at the same price either simultaneously
    or within the same 60-second period, with no individual trade exceeding 10,000 shares.
    """

    STOCK_OPTION = ...
    """
    Stock-Option Trade is used to identify cash equity transactions which are related to options transactions and therefore
    potentially subject to cancellation if market conditions of the options leg(s) prevent the execution of the stock-option
    order at the price agreed upon.
    """

    DISTRIBUTION = ...
    """Sale of a large block of stock in such a manner that the price is not adversely affected."""

    AVERAGE_PRICE = ...
    """A trade where the price reported is based upon an average of the prices for transactions in a security during all or any portion of the trading day."""

    CROSS = ...
    """Indicates that the trade resulted from a Market Center’s crossing session."""

    PRICE_VARIATION = ...
    """Indicates a regular market session trade transaction that carries a price that is significantly away from the prevailing consolidated or primary market value at the time of the transaction."""

    RULE_155 = ...
    """To qualify as a NYSE AMEX Rule 155"""

    OFFICIAL_CLOSE = ...
    """Indicates the ‘Official’ closing value as determined by a Market Center. This transaction report will contain the market center generated closing price."""

    PRIOR_REFERENCE_PRICE = ...
    """
    A sale condition that identifies a trade based on a price at a prior point in time i.e. more than 90 seconds prior to the time of the trade report.
    The execution time of the trade will be the time of the prior reference price.
    """

    OFFICIAL_OPEN = ...
    """Indicates the ‘Official’ open value as determined by a Market Center. This transaction report will contain the market"""

    CAP_ELECTION = ...
    """
    The CAP Election Trade highlights sales as a result of a sweep execution on the NYSE, whereby CAP orders have been elected and executed
    outside the best price bid or offer and the orders appear as repeat trades at subsequent execution prices.
    This indicator provides additional information to market participants that an automatic sweep transaction has occurred with repeat
    trades as one continuous electronic transaction.
    """

    AUTO_EXECUTION = ...
    """A sale condition code that identifies a NYSE trade that has been automatically executed without the potential benefit of price improvement."""

    TRADE_THROUGH_EXEMPT = ...
    """
    Denotes whether or not a trade is exempt (Rule 611) and when used jointly with certain Sale Conditions,
    will more fully describe the characteristics of a particular trade.
    """

    UNDOCUMENTED_FLAG = ...
    """This flag is present in raw data, but AlgoSeek document does not describe it."""

    ODD_LOT = ...
    """Denotes the trade is an odd lot less than a 100 shares."""


class AuxiliaryDataKey(System.Object):
    """Unique definition key for a collection of auxiliary data for a Market and SecurityType"""

    EQUITY_USA: QuantConnect.Data.Auxiliary.AuxiliaryDataKey
    """USA equities market corporate actions key definition"""

    @property
    def market(self) -> str:
        """The market associated with these corporate actions"""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """The associated security type"""
        ...

    def __init__(self, market: str, securityType: QuantConnect.SecurityType) -> None:
        """Creates a new instance"""
        ...

    @staticmethod
    @overload
    def create(symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Auxiliary.AuxiliaryDataKey:
        """Helper method to create a new instance from a Symbol"""
        ...

    @staticmethod
    @overload
    def create(security_identifier: QuantConnect.SecurityIdentifier) -> QuantConnect.Data.Auxiliary.AuxiliaryDataKey:
        """Helper method to create a new instance from a SecurityIdentifier"""
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified System.Object is equal to the current System.Object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """Serves as a hash function for a particular type."""
        ...

    def to_string(self) -> str:
        """Returns a string containing the market and security type"""
        ...


class LocalZipMapFileProvider(System.Object, QuantConnect.Interfaces.IMapFileProvider):
    """Provides an implementation of IMapFileProvider that reads from a local zip file"""

    @property
    def cache_refresh_period(self) -> datetime.timedelta:
        """
        The cached refresh period for the map files
        
        This property is protected.
        """
        ...

    def __init__(self) -> None:
        """Creates a new instance of the LocalDiskFactorFileProvider"""
        ...

    def get(self, auxiliary_data_key: QuantConnect.Data.Auxiliary.AuxiliaryDataKey) -> QuantConnect.Data.Auxiliary.MapFileResolver:
        """
        Gets a MapFileResolver representing all the map files for the specified market
        
        :param auxiliary_data_key: Key used to fetch a map file resolver. Specifying market and security type
        :returns: A MapFileResolver containing all map files for the specified market.
        """
        ...

    def initialize(self, data_provider: QuantConnect.Interfaces.IDataProvider) -> None:
        """
        Initializes our MapFileProvider by supplying our data_provider
        
        :param data_provider: DataProvider to use
        """
        ...

    def start_expiration_task(self) -> None:
        """
        Helper method that will clear any cached factor files in a daily basis, this is useful for live trading
        
        This method is protected.
        """
        ...


class IFactorProvider(metaclass=abc.ABCMeta):
    """Providers price scaling factors for a permanent tick"""

    @property
    @abc.abstractmethod
    def permtick(self) -> str:
        """Gets the symbol this factor file represents"""
        ...

    @property
    @abc.abstractmethod
    def factor_file_minimum_date(self) -> typing.Optional[datetime.datetime]:
        """The minimum tradeable date for the symbol"""
        ...

    @property.setter
    def factor_file_minimum_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    def get_price_factor(self, search_date: typing.Union[datetime.datetime, datetime.date], data_normalization_mode: QuantConnect.DataNormalizationMode, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, contract_offset: int = 0) -> float:
        """Gets the price factor for the specified search date"""
        ...


class IFactorRow(metaclass=abc.ABCMeta):
    """Factor row abstraction. IFactorProvider"""

    @property
    @abc.abstractmethod
    def date(self) -> datetime.datetime:
        """Gets the date associated with this data"""
        ...

    def get_file_format(self, source: str = None) -> str:
        """Writes factor file row into it's file format"""
        ...


class FactorFile(typing.Generic[QuantConnect_Data_Auxiliary_FactorFile_T], System.Object, QuantConnect.Data.Auxiliary.IFactorProvider, typing.Iterable[QuantConnect.Data.Auxiliary.IFactorRow], metaclass=abc.ABCMeta):
    """Represents an entire factor file for a specified symbol"""

    @property
    def reversed_factor_file_dates(self) -> System.Collections.Generic.List[datetime.datetime]:
        """
        Keeping a reversed version is more performant that reversing it each time we need it
        
        This property is protected.
        """
        ...

    @property
    def sorted_factor_file_data(self) -> System.Collections.Generic.SortedList[datetime.datetime, System.Collections.Generic.List[QuantConnect_Data_Auxiliary_FactorFile_T]]:
        """The factor file data rows sorted by date"""
        ...

    @property.setter
    def sorted_factor_file_data(self, value: System.Collections.Generic.SortedList[datetime.datetime, System.Collections.Generic.List[QuantConnect_Data_Auxiliary_FactorFile_T]]) -> None:
        ...

    @property
    def factor_file_minimum_date(self) -> typing.Optional[datetime.datetime]:
        """The minimum tradeable date for the symbol"""
        ...

    @property.setter
    def factor_file_minimum_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def most_recent_factor_change(self) -> datetime.datetime:
        """Gets the most recent factor change in the factor file"""
        ...

    @property
    def permtick(self) -> str:
        """Gets the symbol this factor file represents"""
        ...

    def __init__(self, permtick: str, data: System.Collections.Generic.IEnumerable[QuantConnect_Data_Auxiliary_FactorFile_T], factorFileMinimumDate: typing.Optional[datetime.datetime] = None) -> None:
        """
        Initializes a new instance of the FactorFile{T} class.
        
        This method is protected.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Auxiliary.IFactorRow]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    def get_file_format(self) -> System.Collections.Generic.IEnumerable[str]:
        """
        Writes this factor file data to an enumerable of csv lines
        
        :returns: An enumerable of lines representing this factor file.
        """
        ...

    def get_price_factor(self, search_date: typing.Union[datetime.datetime, datetime.date], data_normalization_mode: QuantConnect.DataNormalizationMode, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, contract_offset: int = 0) -> float:
        """Gets the price scale factor for the specified search date"""
        ...

    def write_to_file(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Write the factor file to the correct place in the default Data folder
        
        :param symbol: The symbol this factor file represents
        """
        ...


class CorporateFactorRow(System.Object, QuantConnect.Data.Auxiliary.IFactorRow):
    """Defines a single row in a factor_factor file. This is a csv file ordered as {date, price factor, split factor, reference price}"""

    @property
    def date(self) -> datetime.datetime:
        """Gets the date associated with this data"""
        ...

    @property
    def price_factor(self) -> float:
        """Gets the price factor associated with this data"""
        ...

    @property.setter
    def price_factor(self, value: float) -> None:
        ...

    @property
    def split_factor(self) -> float:
        """Gets the split factor associated with the date"""
        ...

    @property.setter
    def split_factor(self, value: float) -> None:
        ...

    @property
    def price_scale_factor(self) -> float:
        """Gets the combined factor used to create adjusted prices from raw prices"""
        ...

    @property
    def reference_price(self) -> float:
        """Gets the raw closing value from the trading date before the updated factor takes effect"""
        ...

    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], priceFactor: float, splitFactor: float, referencePrice: float = 0) -> None:
        """Initializes a new instance of the CorporateFactorRow class"""
        ...

    @overload
    def apply(self, dividend: QuantConnect.Data.Market.Dividend, exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> QuantConnect.Data.Auxiliary.CorporateFactorRow:
        """
        Applies the dividend to this factor file row.
        This dividend date must be on or before the factor
        file row date
        
        :param dividend: The dividend to apply with reference price and distribution specified
        :param exchange_hours: Exchange hours used for resolving the previous trading day
        :returns: A new factor file row that applies the dividend to this row's factors.
        """
        ...

    @overload
    def apply(self, split: QuantConnect.Data.Market.Split, exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> QuantConnect.Data.Auxiliary.CorporateFactorRow:
        """
        Applies the split to this factor file row.
        This split date must be on or before the factor
        file row date
        
        :param split: The split to apply with reference price and split factor specified
        :param exchange_hours: Exchange hours used for resolving the previous trading day
        :returns: A new factor file row that applies the split to this row's factors.
        """
        ...

    def get_dividend(self, next_corporate_factor_row: QuantConnect.Data.Auxiliary.CorporateFactorRow, symbol: typing.Union[QuantConnect.Symbol, str], exchange_hours: QuantConnect.Securities.SecurityExchangeHours, decimal_places: int = 2) -> QuantConnect.Data.Market.Dividend:
        """
        Creates a new dividend from this factor file row and the one chronologically in front of it
        This dividend may have a distribution of zero if this row doesn't represent a dividend
        
        :param next_corporate_factor_row: The next factor file row in time
        :param symbol: The symbol to use for the dividend
        :param exchange_hours: Exchange hours used for resolving the previous trading day
        :param decimal_places: The number of decimal places to round the dividend's distribution to, defaulting to 2
        :returns: A new dividend instance.
        """
        ...

    def get_file_format(self, source: str = None) -> str:
        """Writes factor file row into it's file format"""
        ...

    def get_split(self, next_corporate_factor_row: QuantConnect.Data.Auxiliary.CorporateFactorRow, symbol: typing.Union[QuantConnect.Symbol, str], exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> QuantConnect.Data.Market.Split:
        """
        Creates a new split from this factor file row and the one chronologically in front of it
        This split may have a split factor of one if this row doesn't represent a split
        
        :param next_corporate_factor_row: The next factor file row in time
        :param symbol: The symbol to use for the split
        :param exchange_hours: Exchange hours used for resolving the previous trading day
        :returns: A new split instance.
        """
        ...

    @staticmethod
    def parse(lines: System.Collections.Generic.IEnumerable[str], factor_file_minimum_date: typing.Optional[typing.Optional[datetime.datetime]]) -> typing.Union[System.Collections.Generic.List[QuantConnect.Data.Auxiliary.CorporateFactorRow], typing.Optional[datetime.datetime]]:
        """
        Parses the lines as factor files rows while properly handling inf entries
        
        :param lines: The lines from the factor file to be parsed
        :param factor_file_minimum_date: The minimum date from the factor file
        :returns: An enumerable of factor file rows.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class CorporateFactorProvider(QuantConnect.Data.Auxiliary.FactorFile[QuantConnect.Data.Auxiliary.CorporateFactorRow]):
    """Corporate related factor provider. Factors based on splits and dividends"""

    def __init__(self, permtick: str, data: System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.CorporateFactorRow], factorFileMinimumDate: typing.Optional[datetime.datetime] = None) -> None:
        """Creates a new instance"""
        ...

    def apply(self, data: System.Collections.Generic.List[QuantConnect.Data.BaseData], exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> QuantConnect.Data.Auxiliary.CorporateFactorProvider:
        """
        Creates a new factor file with the specified data applied.
        Only Dividend and Split data types
        will be used.
        
        :param data: The data to apply
        :param exchange_hours: Exchange hours used for resolving the previous trading day
        :returns: A new factor file that incorporates the specified dividend.
        """
        ...

    def get_price_factor(self, search_date: typing.Union[datetime.datetime, datetime.date], data_normalization_mode: QuantConnect.DataNormalizationMode, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, contract_offset: int = 0) -> float:
        """Gets the price scale factor that includes dividend and split adjustments for the specified search date"""
        ...

    def get_scaling_factors(self, search_date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Auxiliary.CorporateFactorRow:
        """Gets price and split factors to be applied at the specified date"""
        ...

    def get_splits_and_dividends(self, symbol: typing.Union[QuantConnect.Symbol, str], exchange_hours: QuantConnect.Securities.SecurityExchangeHours, decimal_places: int = 2) -> System.Collections.Generic.List[QuantConnect.Data.BaseData]:
        """
        Gets all of the splits and dividends represented by this factor file
        
        :param symbol: The symbol to ues for the dividend and split objects
        :param exchange_hours: Exchange hours used for resolving the previous trading day
        :param decimal_places: The number of decimal places to round the dividend's distribution to, defaulting to 2
        :returns: All splits and dividends represented by this factor file in chronological order.
        """
        ...

    def has_dividend_event_on_next_trading_day(self, date: typing.Union[datetime.datetime, datetime.date], price_factor_ratio: typing.Optional[float], reference_price: typing.Optional[float]) -> typing.Union[bool, float, float]:
        """
        Returns true if the specified date is the last trading day before a dividend event
        is to be fired
        
        :param date: The date to check the factor file for a dividend event
        :param price_factor_ratio: When this function returns true, this value will be populated with the price factor ratio required to scale the closing value (pf_i/pf_i+1)
        :param reference_price: When this function returns true, this value will be populated with the reference raw price, which is the close of the provided date
        """
        ...

    def has_split_event_on_next_trading_day(self, date: typing.Union[datetime.datetime, datetime.date], split_factor: typing.Optional[float], reference_price: typing.Optional[float]) -> typing.Union[bool, float, float]:
        """
        Returns true if the specified date is the last trading day before a split event
        is to be fired
        
        :param date: The date to check the factor file for a split event
        :param split_factor: When this function returns true, this value will be populated with the split factor ratio required to scale the closing value
        :param reference_price: When this function returns true, this value will be populated with the reference raw price, which is the close of the provided date
        """
        ...


class MappingContractFactorRow(System.Object, QuantConnect.Data.Auxiliary.IFactorRow):
    """Collection of factors for continuous contracts and their back months contracts for a specific mapping mode DataMappingMode and date"""

    @property
    def date(self) -> datetime.datetime:
        """Gets the date associated with this data"""
        ...

    @property.setter
    def date(self, value: datetime.datetime) -> None:
        ...

    @property
    def backwards_ratio_scale(self) -> System.Collections.Generic.IReadOnlyList[float]:
        """
        Backwards ratio price scaling factors for the front month [index 0] and it's 'i' back months [index 0 + i]
        DataNormalizationMode.BackwardsRatio
        """
        ...

    @property.setter
    def backwards_ratio_scale(self, value: System.Collections.Generic.IReadOnlyList[float]) -> None:
        ...

    @property
    def backwards_panama_canal_scale(self) -> System.Collections.Generic.IReadOnlyList[float]:
        """
        Backwards Panama Canal price scaling factors for the front month [index 0] and it's 'i' back months [index 0 + i]
        DataNormalizationMode.BackwardsPanamaCanal
        """
        ...

    @property.setter
    def backwards_panama_canal_scale(self, value: System.Collections.Generic.IReadOnlyList[float]) -> None:
        ...

    @property
    def forward_panama_canal_scale(self) -> System.Collections.Generic.IReadOnlyList[float]:
        """
        Forward Panama Canal price scaling factors for the front month [index 0] and it's 'i' back months [index 0 + i]
        DataNormalizationMode.ForwardPanamaCanal
        """
        ...

    @property.setter
    def forward_panama_canal_scale(self, value: System.Collections.Generic.IReadOnlyList[float]) -> None:
        ...

    @property
    def data_mapping_mode(self) -> typing.Optional[QuantConnect.DataMappingMode]:
        """Allows the consumer to specify a desired mapping mode"""
        ...

    @property.setter
    def data_mapping_mode(self, value: typing.Optional[QuantConnect.DataMappingMode]) -> None:
        ...

    def __init__(self) -> None:
        """Empty constructor for json converter"""
        ...

    def get_file_format(self, source: str = None) -> str:
        """Writes factor file row into it's file format"""
        ...

    @staticmethod
    def parse(lines: System.Collections.Generic.IEnumerable[str], factor_file_minimum_date: typing.Optional[typing.Optional[datetime.datetime]]) -> typing.Union[System.Collections.Generic.List[QuantConnect.Data.Auxiliary.MappingContractFactorRow], typing.Optional[datetime.datetime]]:
        """
        Parses the lines as factor files rows while properly handling inf entries
        
        :param lines: The lines from the factor file to be parsed
        :param factor_file_minimum_date: The minimum date from the factor file
        :returns: An enumerable of factor file rows.
        """
        ...


class MappingContractFactorProvider(QuantConnect.Data.Auxiliary.FactorFile[QuantConnect.Data.Auxiliary.MappingContractFactorRow]):
    """Mapping related factor provider. Factors based on price differences on mapping dates"""

    def __init__(self, permtick: str, data: System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.MappingContractFactorRow], factorFileMinimumDate: typing.Optional[datetime.datetime] = None) -> None:
        """Creates a new instance"""
        ...

    def get_price_factor(self, search_date: typing.Union[datetime.datetime, datetime.date], data_normalization_mode: QuantConnect.DataNormalizationMode, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, contract_offset: int = 0) -> float:
        """Gets the price scale factor for the specified search date"""
        ...


class ZipEntryName(QuantConnect.Data.BaseData):
    """Defines a data type that just produces data points from the zip entry names in a zip file"""

    @property
    def end_time(self) -> datetime.datetime:
        """Gets or sets the end time of this data"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the ZipEntryName class"""
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
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def should_cache_to_security(self) -> bool:
        """
        Indicates whether this contains data that should be stored in the security cache
        
        :returns: Whether this contains data that should be stored in the security cache.
        """
        ...


class QuoteConditionFlags(Enum):
    """Flag system for quote conditions"""

    NONE = 0
    """No Condition"""

    REGULAR = ...
    """This condition is used for the majority of quotes to indicate a normal trading environment."""

    SLOW = ...
    """
    This condition is used to indicate that the quote is a Slow Quote on both the Bid and Offer
    sides due to a Set Slow List that includes High Price securities.
    """

    GAP = ...
    """
    While in this mode, auto-execution is not eligible, the quote is then considered manual and non-firm in the Bid and Offer and
    either or both sides can be traded through as per Regulation NMS.
    """

    CLOSING = ...
    """This condition can be disseminated to indicate that this quote was the last quote for a security for that Participant."""

    NEWS_DISSEMINATION = ...
    """
    This regulatory Opening Delay or Trading Halt is used when relevant news influencing the security is being disseminated.
    Trading is suspended until the primary market determines that an adequate publication or disclosure of information has occurred.
    """

    NEWS_PENDING = ...
    """
    This condition is used to indicate a regulatory Opening Delay or Trading Halt due to an expected news announcement,
    which may influence the security. An Opening Delay or Trading Halt may be continued once the news has been disseminated.
    """

    TRADING_RANGE_INDICATION = ...
    """
    The condition is used to denote the probable trading range (bid and offer prices, no sizes) of a security that is not Opening Delayed or
    Trading Halted. The Trading Range Indication is used prior to or after the opening of a security.
    """

    ORDER_IMBALANCE = ...
    """This non-regulatory Opening Delay or Trading Halt is used when there is a significant imbalance of buy or sell orders."""

    CLOSED_MARKET_MAKER = ...
    """
    This condition is disseminated by each individual FINRA Market Maker to signify either the last quote of the day or
    the premature close of an individual Market Maker for the day.
    """

    VOLATILITY_TRADING_PAUSE = ...
    """
    This quote condition indicates a regulatory Opening Delay or Trading Halt due to conditions in which
    a security experiences a 10 % or more change in price over a five minute period.
    """

    NON_FIRM_QUOTE = ...
    """This quote condition suspends a Participant's firm quote obligation for a quote for a security."""

    OPENING_QUOTE = ...
    """This condition can be disseminated to indicate that this quote was the opening quote for a security for that Participant."""

    DUE_TO_RELATED_SECURITY = ...
    """
    This non-regulatory Opening Delay or Trading Halt is used when events relating to one security will affect the price and performance of
    another related security. This non-regulatory Opening Delay or Trading Halt is also used when non-regulatory halt reasons such as
    Order Imbalance, Order Influx and Equipment Changeover are combined with Due to Related Security on CTS.
    """

    RESUME = ...
    """
    This quote condition along with zero-filled bid, offer and size fields is used to indicate that trading for a Participant is no longer
    suspended in a security which had been Opening Delayed or Trading Halted.
    """

    IN_VIEW_OF_COMMON = ...
    """
    This quote condition is used when matters affecting the common stock of a company affect the performance of the non-common
    associated securities, e.g., warrants, rights, preferred, classes, etc.
    """

    EQUIPMENT_CHANGEOVER = ...
    """
    This non-regulatory Opening Delay or Trading Halt is used when the ability to trade a security by a Participant is temporarily
    inhibited due to a systems, equipment or communications facility problem or for other technical reasons.
    """

    SUB_PENNY_TRADING = ...
    """
    This non-regulatory Opening Delay or Trading Halt is used to indicate an Opening Delay or Trading Halt for a security whose price
    may fall below $1.05, possibly leading to a sub-penny execution.
    """

    NO_OPEN_NO_RESUME = ...
    """
    This quote condition is used to indicate that an Opening Delay or a Trading Halt is to be in effect for the rest
    of the trading day in a security for a Participant.
    """

    LIMIT_UP_LIMIT_DOWN_PRICE_BAND = ...
    """This quote condition is used to indicate that a Limit Up-Limit Down Price Band is applicable for a security."""

    REPUBLISHED_LIMIT_UP_LIMIT_DOWN_PRICE_BAND = ...
    """
    This quote condition is used to indicate that a Limit Up-Limit Down Price Band that is being disseminated " +
    is a ‘republication’ of the latest Price Band for a security.
    """

    MANUAL = ...
    """
    This indicates that the market participant is in a manual mode on both the Bid and Ask. While in this mode,
    automated execution is not eligible on the Bid and Ask side and can be traded through pursuant to Regulation NMS requirements.
    """

    FAST_TRADING = ...
    """For extremely active periods of short duration. While in this mode, the UTP participant will enter quotations on a “best efforts” basis."""

    ORDER_INFLUX = ...
    """A halt condition used when there is a sudden order influx. To prevent a disorderly market, trading is temporarily suspended by the UTP participant."""


class FactorFileZipHelper(System.Object):
    """Provides methods for reading factor file zips"""

    @staticmethod
    def get_factor_file_zip_file_name(market: str, date: typing.Union[datetime.datetime, datetime.date], security_type: QuantConnect.SecurityType) -> str:
        """Gets the factor file zip filename for the specified date"""
        ...

    @staticmethod
    def get_relative_factor_file_path(market: str, security_type: QuantConnect.SecurityType) -> str:
        """
        Constructs the factor file path for the specified market and security type
        
        :param market: The market this symbol belongs to
        :param security_type: The security type
        :returns: The relative file path.
        """
        ...

    @staticmethod
    def read_factor_file_zip(file: System.IO.Stream, map_file_resolver: QuantConnect.Data.Auxiliary.MapFileResolver, market: str, security_type: QuantConnect.SecurityType) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.Auxiliary.IFactorProvider]]:
        """Reads the zip bytes as text and parses as FactorFileRows to create FactorFiles"""
        ...


class LocalZipFactorFileProvider(System.Object, QuantConnect.Interfaces.IFactorFileProvider):
    """Provides an implementation of IFactorFileProvider that searches the local disk for a zip file containing all factor files"""

    @property
    def cache_refresh_period(self) -> datetime.timedelta:
        """
        The cached refresh period for the factor files
        
        This property is protected.
        """
        ...

    def __init__(self) -> None:
        """Creates a new instance of the LocalZipFactorFileProvider class."""
        ...

    def get(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Auxiliary.IFactorProvider:
        """
        Gets a FactorFile{T} instance for the specified symbol, or null if not found
        
        :param symbol: The security's symbol whose factor file we seek
        :returns: The resolved factor file, or null if not found.
        """
        ...

    def initialize(self, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider) -> None:
        """
        Initializes our FactorFileProvider by supplying our map_file_provider
        and data_provider
        
        :param map_file_provider: MapFileProvider to use
        :param data_provider: DataProvider to use
        """
        ...

    def start_expiration_task(self) -> None:
        """
        Helper method that will clear any cached factor files in a daily basis, this is useful for live trading
        
        This method is protected.
        """
        ...


class LocalDiskMapFileProvider(System.Object, QuantConnect.Interfaces.IMapFileProvider):
    """
    Provides a default implementation of IMapFileProvider that reads from
    the local disk
    """

    def __init__(self) -> None:
        """Creates a new instance of the LocalDiskFactorFileProvider"""
        ...

    def get(self, auxiliary_data_key: QuantConnect.Data.Auxiliary.AuxiliaryDataKey) -> QuantConnect.Data.Auxiliary.MapFileResolver:
        """
        Gets a MapFileResolver representing all the map
        files for the specified market
        
        :param auxiliary_data_key: Key used to fetch a map file resolver. Specifying market and security type
        :returns: A MapFileRow containing all map files for the specified market.
        """
        ...

    def initialize(self, data_provider: QuantConnect.Interfaces.IDataProvider) -> None:
        """
        Initializes our MapFileProvider by supplying our data_provider
        
        :param data_provider: DataProvider to use
        """
        ...


class MapFileZipHelper(System.Object):
    """Helper class for handling mapfile zip files"""

    @staticmethod
    def get_map_file_zip_file_name(market: str, date: typing.Union[datetime.datetime, datetime.date], security_type: QuantConnect.SecurityType) -> str:
        """Gets the mapfile zip filename for the specified date"""
        ...

    @staticmethod
    def read_map_file_zip(file: System.IO.Stream, market: str, security_type: QuantConnect.SecurityType) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Auxiliary.MapFile]:
        """Reads the zip bytes as text and parses as MapFileRows to create MapFiles"""
        ...


class LocalDiskFactorFileProvider(System.Object, QuantConnect.Interfaces.IFactorFileProvider):
    """Provides an implementation of IFactorFileProvider that searches the local disk"""

    def __init__(self) -> None:
        """Creates a new instance of the LocalDiskFactorFileProvider"""
        ...

    def get(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Auxiliary.IFactorProvider:
        """
        Gets a FactorFile{T} instance for the specified symbol, or null if not found
        
        :param symbol: The security's symbol whose factor file we seek
        :returns: The resolved factor file, or null if not found.
        """
        ...

    def initialize(self, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider) -> None:
        """
        Initializes our FactorFileProvider by supplying our map_file_provider
        and data_provider
        
        :param map_file_provider: MapFileProvider to use
        :param data_provider: DataProvider to use
        """
        ...


class PriceScalingExtensions(System.Object):
    """Set of helper methods for factor files and price scaling operations"""

    @staticmethod
    def get_empty_factor_file(symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Auxiliary.IFactorProvider:
        """Helper method to return an empty factor file"""
        ...

    @staticmethod
    def get_factor_file_symbol(symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Symbol:
        """Determines the symbol to use to fetch it's factor file"""
        ...

    @staticmethod
    def get_price_scale(factor_file: QuantConnect.Data.Auxiliary.IFactorProvider, date_time: typing.Union[datetime.datetime, datetime.date], normalization_mode: QuantConnect.DataNormalizationMode, contract_offset: int = 0, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, end_date_time: typing.Optional[datetime.datetime] = None) -> float:
        """
        Resolves the price scale for a date given a factor file and required settings
        
        :param factor_file: The factor file to use
        :param date_time: The date for the price scale lookup
        :param normalization_mode: The price normalization mode requested
        :param contract_offset: The contract offset, useful for continuous contracts
        :param data_mapping_mode: The data mapping mode used, useful for continuous contracts
        :param end_date_time: The reference end date for scaling prices.
        :returns: The price scale to use.
        """
        ...

    @staticmethod
    def safe_read(permtick: str, contents: System.Collections.Generic.IEnumerable[str], security_type: QuantConnect.SecurityType) -> QuantConnect.Data.Auxiliary.IFactorProvider:
        """Parses the contents as a FactorFile, if error returns a new empty factor file"""
        ...


class MapFilePrimaryExchangeProvider(System.Object, QuantConnect.Interfaces.IPrimaryExchangeProvider):
    """Implementation of IPrimaryExchangeProvider from map files."""

    def __init__(self, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider) -> None:
        """
        Constructor for Primary Exchange Provider from MapFiles
        
        :param mapFileProvider: MapFile to use
        """
        ...

    def get_primary_exchange(self, security_identifier: QuantConnect.SecurityIdentifier) -> QuantConnect.Exchange:
        """
        Gets the primary exchange for a given security identifier
        
        :param security_identifier: The security identifier to get the primary exchange for
        :returns: Returns the primary exchange or null if not found.
        """
        ...


