from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Custom.Tiingo
import QuantConnect.Data.Market
import System
import System.Collections.Generic


class TiingoSymbolMapper(System.Object):
    """Helper class to map a Lean format ticker to Tiingo format"""

    @staticmethod
    def get_lean_ticker(ticker: str) -> str:
        """Maps a given Tiingo ticker to Lean equivalent"""
        ...

    @staticmethod
    def get_tiingo_ticker(symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """Maps a given Symbol instance to it's Tiingo equivalent"""
        ...


class TiingoPrice(QuantConnect.Data.Market.TradeBar):
    """
    Tiingo daily price data
    https://api.tiingo.com/docs/tiingo/daily
    """

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
    def period(self) -> datetime.timedelta:
        """The period of this trade bar, (second, minute, daily, ect...)"""
        ...

    @property
    def date(self) -> datetime.datetime:
        """The date this data pertains to"""
        ...

    @property.setter
    def date(self, value: datetime.datetime) -> None:
        ...

    @property
    def open(self) -> float:
        """The actual (not adjusted) open price of the asset on the specific date"""
        ...

    @property.setter
    def open(self, value: float) -> None:
        ...

    @property
    def high(self) -> float:
        """The actual (not adjusted) high price of the asset on the specific date"""
        ...

    @property.setter
    def high(self, value: float) -> None:
        ...

    @property
    def low(self) -> float:
        """The actual (not adjusted) low price of the asset on the specific date"""
        ...

    @property.setter
    def low(self, value: float) -> None:
        ...

    @property
    def close(self) -> float:
        """The actual (not adjusted) closing price of the asset on the specific date"""
        ...

    @property.setter
    def close(self, value: float) -> None:
        ...

    @property
    def volume(self) -> float:
        """The actual (not adjusted) number of shares traded during the day"""
        ...

    @property.setter
    def volume(self, value: float) -> None:
        ...

    @property
    def adjusted_open(self) -> float:
        """The adjusted opening price of the asset on the specific date. Returns null if not available."""
        ...

    @property.setter
    def adjusted_open(self, value: float) -> None:
        ...

    @property
    def adjusted_high(self) -> float:
        """The adjusted high price of the asset on the specific date. Returns null if not available."""
        ...

    @property.setter
    def adjusted_high(self, value: float) -> None:
        ...

    @property
    def adjusted_low(self) -> float:
        """The adjusted low price of the asset on the specific date. Returns null if not available."""
        ...

    @property.setter
    def adjusted_low(self, value: float) -> None:
        ...

    @property
    def adjusted_close(self) -> float:
        """The adjusted close price of the asset on the specific date. Returns null if not available."""
        ...

    @property.setter
    def adjusted_close(self, value: float) -> None:
        ...

    @property
    def adjusted_volume(self) -> int:
        """The adjusted number of shares traded during the day - adjusted for splits. Returns null if not available"""
        ...

    @property.setter
    def adjusted_volume(self, value: int) -> None:
        ...

    @property
    def dividend(self) -> float:
        """The dividend paid out on "date" (note that "date" will be the "exDate" for the dividend)"""
        ...

    @property.setter
    def dividend(self, value: float) -> None:
        ...

    @property
    def split_factor(self) -> float:
        """
        A factor used when a company splits or reverse splits. On days where there is ONLY a split (no dividend payment),
        you can calculate the adjusted close as follows: adjClose = "Previous Close"/splitFactor
        """
        ...

    @property.setter
    def split_factor(self, value: float) -> None:
        ...

    def __init__(self) -> None:
        """Initializes an instance of the TiingoPrice class."""
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
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method,
            and returns a new instance of the object
            each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...


class TiingoDailyData(QuantConnect.Data.Custom.Tiingo.TiingoPrice):
    """
    Tiingo daily price data
    https://api.tiingo.com/docs/tiingo/daily
    
    This is kept for backwards compatibility, please use TiingoPrice
    """


class Tiingo(System.Object):
    """Helper class for Tiingo configuration"""

    auth_code: str
    """Gets the Tiingo API token."""

    is_auth_code_set: bool
    """Returns true if the Tiingo API token has been set."""

    @staticmethod
    def set_auth_code(auth_code: str) -> None:
        """
        Sets the Tiingo API token.
        
        :param auth_code: The Tiingo API token
        """
        ...


