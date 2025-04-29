from typing import overload
from enum import Enum
import QuantConnect.Securities.FutureOption.Api
import System
import System.Collections.Generic


class CMEOptionExpirationEntry(System.Object):
    """Chicago Mercantile Exchange Option Expiration Entry"""

    @property
    def month(self) -> int:
        """Month of expiry"""
        ...

    @property
    def year(self) -> int:
        """Year of expiry"""
        ...

    @property
    def code(self) -> str:
        """Expiration code (two letter)"""
        ...

    @property
    def two_digits_code(self) -> str:
        """Expiration code (three letter)"""
        ...


class CMEOptionsExpiration(System.Object):
    """
    Future options Expiration entries. These are useful because we can derive the
    future chain from this data, since FOP and FUT share a 1-1 expiry code.
    """

    @property
    def label(self) -> str:
        """Date of expiry"""
        ...

    @property
    def product_id(self) -> int:
        """Product ID of the expiring asset (usually future option)"""
        ...

    @property
    def contract_id(self) -> str:
        """Contract ID of the asset"""
        ...

    @property
    def expiration(self) -> QuantConnect.Securities.FutureOption.Api.CMEOptionExpirationEntry:
        """Contract month code formatted as [FUTURE_MONTH_LETTER(1)][YEAR(1)]"""
        ...


class CMEOptionsTradeDatesAndExpiration(System.Object):
    """CME options trades, dates, and expiration list API call root response"""

    @property
    def label(self) -> str:
        """Describes the type of future option this entry is"""
        ...

    @property
    def name(self) -> str:
        """Name of the product"""
        ...

    @property
    def option_type(self) -> str:
        """
        Option type. "AME" for American, "EUR" for European.
        Note that there are other types such as weekly, but we
        only support American options for now.
        """
        ...

    @property
    def product_id(self) -> int:
        """Product ID of the option"""
        ...

    @property
    def daily(self) -> bool:
        """Is Daily option"""
        ...

    @property
    def sto(self) -> bool:
        """???"""
        ...

    @property
    def weekly(self) -> bool:
        """Is weekly option"""
        ...

    @property
    def expirations(self) -> System.Collections.Generic.List[QuantConnect.Securities.FutureOption.Api.CMEOptionsExpiration]:
        """Expirations of the future option"""
        ...


class CMEOptionChainQuoteEntry(System.Object):
    """Option chain entry quotes, containing strike price"""

    @property
    def strike_price(self) -> float:
        """Strike price of the future option quote entry"""
        ...


class CMEOptionChainQuotes(System.Object):
    """CME Option Chain Quotes API call root response"""

    @property
    def quotes(self) -> System.Collections.Generic.List[QuantConnect.Securities.FutureOption.Api.CMEOptionChainQuoteEntry]:
        """The future options contracts with/without settlements"""
        ...


class CMEProductSlateV2ListEntry(System.Object):
    """Product entry describing the asset matching the search criteria"""

    @property
    def id(self) -> int:
        """CME ID for the asset"""
        ...

    @property
    def name(self) -> str:
        """Name of the product (e.g. E-mini NASDAQ futures)"""
        ...

    @property
    def clearing(self) -> str:
        """Clearing code"""
        ...

    @property
    def globex(self) -> str:
        """GLOBEX ticker"""
        ...

    @property
    def globex_traded(self) -> bool:
        """Is traded in the GLOBEX venue"""
        ...

    @property
    def venues(self) -> str:
        """Venues this asset trades on"""
        ...

    @property
    def cleared(self) -> str:
        """Asset type this product is cleared as (i.e. "Futures", "Options")"""
        ...

    @property
    def exchange(self) -> str:
        """Exchange the asset trades on (i.e. CME, NYMEX, COMEX, CBOT)"""
        ...

    @property
    def group_id(self) -> int:
        """Asset class group ID - describes group of asset class (e.g. equities, agriculture, etc.)"""
        ...

    @property
    def sub_group_id(self) -> int:
        """More specific ID describing product"""
        ...


class CMEProductSlateV2ListResponse(System.Object):
    """Product slate API call root response"""

    @property
    def products(self) -> System.Collections.Generic.List[QuantConnect.Securities.FutureOption.Api.CMEProductSlateV2ListEntry]:
        """Products matching the search criteria"""
        ...


