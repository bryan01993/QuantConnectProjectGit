from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Selection
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.DataSource
import QuantConnect.Orders
import QuantConnect.Util
import System
import System.Collections.Generic

JsonConverter = typing.Any
QuantConnect_DataSource_BrainCompanyFilingLanguageMetrics10K = typing.Any
QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsAll = typing.Any
QuantConnect_DataSource_BrainStockRanking10Day = typing.Any
QuantConnect_DataSource_BrainStockRanking2Day = typing.Any
QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsUniverseAll = typing.Any
QuantConnect_DataSource_BrainStockRanking3Day = typing.Any
QuantConnect_DataSource_BrainStockRanking5Day = typing.Any
QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsUniverse10K = typing.Any
QuantConnect_DataSource_BrainSentimentIndicator30Day = typing.Any
QuantConnect_DataSource_BrainStockRanking21Day = typing.Any
QuantConnect_DataSource_BrainSentimentIndicator7Day = typing.Any

QuantConnect_DataSource_BrainSentimentIndicatorBase_T = typing.TypeVar("QuantConnect_DataSource_BrainSentimentIndicatorBase_T")
QuantConnect_DataSource_BrainStockRankingBase_T = typing.TypeVar("QuantConnect_DataSource_BrainStockRankingBase_T")
QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsUniverse_T = typing.TypeVar("QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsUniverse_T")
QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsBase_T = typing.TypeVar("QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsBase_T")


class RegalyticsRegulatoryArticle(QuantConnect.Data.BaseData):
    """Regalytics Regulatory articles"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def id(self) -> str:
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    @property
    def title(self) -> str:
        ...

    @property.setter
    def title(self, value: str) -> None:
        ...

    @property
    def summary(self) -> str:
        ...

    @property.setter
    def summary(self, value: str) -> None:
        ...

    @property
    def status(self) -> str:
        ...

    @property.setter
    def status(self, value: str) -> None:
        ...

    @property
    def classification(self) -> str:
        ...

    @property.setter
    def classification(self, value: str) -> None:
        ...

    @property
    def filing_type(self) -> str:
        ...

    @property.setter
    def filing_type(self, value: str) -> None:
        ...

    @property
    def in_federal_register(self) -> bool:
        ...

    @property.setter
    def in_federal_register(self, value: bool) -> None:
        ...

    @property
    def federal_register_number(self) -> str:
        ...

    @property.setter
    def federal_register_number(self, value: str) -> None:
        ...

    @property
    def docket_file_number(self) -> str:
        ...

    @property.setter
    def docket_file_number(self, value: str) -> None:
        ...

    @property
    def sec_release_number(self) -> str:
        ...

    @property.setter
    def sec_release_number(self, value: str) -> None:
        ...

    @property
    def proposed_comments_due_date(self) -> typing.Optional[datetime.datetime]:
        ...

    @property.setter
    def proposed_comments_due_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def original_publication_date(self) -> typing.Optional[datetime.datetime]:
        ...

    @property.setter
    def original_publication_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def federal_register_publication_date(self) -> typing.Optional[datetime.datetime]:
        ...

    @property.setter
    def federal_register_publication_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def rule_effective_date(self) -> typing.Optional[datetime.datetime]:
        ...

    @property.setter
    def rule_effective_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def sourced_at(self) -> typing.Optional[datetime.datetime]:
        ...

    @property.setter
    def sourced_at(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def latest_update(self) -> datetime.datetime:
        ...

    @property.setter
    def latest_update(self, value: datetime.datetime) -> None:
        ...

    @property
    def alert_type(self) -> str:
        ...

    @property.setter
    def alert_type(self, value: str) -> None:
        ...

    @property
    def states(self) -> System.Collections.Generic.Dictionary[str, System.Collections.Generic.List[str]]:
        ...

    @property.setter
    def states(self, value: System.Collections.Generic.Dictionary[str, System.Collections.Generic.List[str]]) -> None:
        ...

    @property
    def agencies(self) -> System.Collections.Generic.List[str]:
        ...

    @property.setter
    def agencies(self, value: System.Collections.Generic.List[str]) -> None:
        ...

    @property
    def sector(self) -> System.Collections.Generic.List[System.Collections.Generic.Dictionary[str, str]]:
        ...

    @property.setter
    def sector(self, value: System.Collections.Generic.List[System.Collections.Generic.Dictionary[str, str]]) -> None:
        ...

    @property
    def announcement_url(self) -> str:
        ...

    @property.setter
    def announcement_url(self, value: str) -> None:
        ...

    @property
    def created_at(self) -> datetime.datetime:
        ...

    @property.setter
    def created_at(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class RegalyticsRegulatoryArticles(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Regalytics Regulatory articles collection"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Formats a string with QuiverCNBC data
        
        :returns: string containing QuiverCNBC information.
        """
        ...


class TradingEconomicsEventFilter(System.Object):
    """Provides methods to filter and standardize Trading Economics calendar event names."""

    @staticmethod
    def filter_event(event_name: str) -> str:
        """
        Convert and normalizes the Trading Economics calendar "Event" field.
        
        :param event_name: Raw event name
        :returns: Event name normalized.
        """
        ...


class TradingEconomics(System.Object):
    """TradingEconomics static class contains shortcut definitions of major Trading Economics Indicators available");"""

    class Indicator(System.Object):
        """Indicator group"""

        class Afghanistan(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDAFN"
            """Afghanistan Currency"""

        class Albania(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDALL"
            """Albania Currency"""

        class Algeria(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDDZD"
            """Algeria Currency"""

        class Angola(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDAOA"
            """Angola Currency"""

        class Argentina(System.Object):
            """This class has no documentation."""

            INTEREST_RATE: str = "APDR1T"
            """Argentina Interest Rate"""

            DEPOSIT_INTEREST_RATE: str = "ARGFRINRDPST"
            """Argentina Deposit Interest Rate"""

            STOCK_MARKET: str = "MERVAL"
            """Argentina Stock Market"""

            CURRENCY: str = "USDARS"
            """Argentina Currency"""

        class Armenia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDAMD"
            """Armenia Currency"""

        class Australia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "AS51"
            """Australia Stock Market"""

            CURRENCY: str = "AUDUSD"
            """Australia Currency"""

            TWO_YEAR_NOTE_YIELD: str = "AUSTRALIA2YNY"
            """Australia 2 Year Note Yield"""

            CENTRAL_BANK_BALANCE_SHEET: str = "AUSTRALIACENBANBALSH"
            """Australia Central Bank Balance Sheet"""

            INFLATION_EXPECTATIONS: str = "AUSTRALIAINFEXP"
            """Australia Inflation Expectations"""

            GOVERNMENT_BOND_10Y: str = "GACGB10"
            """Australia Government Bond 10Y"""

            CONSUMER_CONFIDENCE: str = "WMCCCONPCT"
            """Australia Consumer Confidence"""

        class Austria(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "ATX"
            """Austria Stock Market"""

            CURRENCY: str = "EURUSD"
            """Austria Currency"""

            GOVERNMENT_BOND_10Y: str = "GAGB10YR"
            """Austria Government Bond 10Y"""

        class Bahamas(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDBSD"
            """Bahamas Currency"""

        class Bahrain(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "BAHRAININTRAT"
            """Bahrain Interbank Rate"""

            STOCK_MARKET: str = "BHSEEI"
            """Bahrain Stock Market"""

            CURRENCY: str = "USDBHD"
            """Bahrain Currency"""

        class Bangladesh(System.Object):
            """This class has no documentation."""

            INTEREST_RATE: str = "BANGLADESHINTRATE"
            """Bangladesh Interest Rate"""

            STOCK_MARKET: str = "DHAKA"
            """Bangladesh Stock Market"""

            CURRENCY: str = "USDBDT"
            """Bangladesh Currency"""

        class Belarus(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDBYR"
            """Belarus Currency"""

        class Belgium(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BEL20"
            """Belgium Stock Market"""

            GOVERNMENT_BOND_10Y: str = "GBGB10YR"
            """Belgium Government Bond 10Y"""

        class Bermuda(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BSX"
            """Bermuda Stock Market"""

        class Bolivia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDBOB"
            """Bolivia Currency"""

        class BosniaAndHerzegovina(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "SASX10"
            """BosniaAndHerzegovina Stock Market"""

            CURRENCY: str = "USDBIH"
            """BosniaAndHerzegovina Currency"""

        class Botswana(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BGSMDC"
            """Botswana Stock Market"""

            CURRENCY: str = "USDBWP"
            """Botswana Currency"""

        class Brazil(System.Object):
            """This class has no documentation."""

            CASH_RESERVE_RATIO: str = "BRAZILCASRESRAT"
            """Brazil Cash Reserve Ratio"""

            INTERBANK_RATE: str = "BRAZILINTRAT"
            """Brazil Interbank Rate"""

            MINIMUM_WAGES: str = "BRAZILMINWAG"
            """Brazil Minimum Wages"""

            GOVERNMENT_BOND_10Y: str = "GEBU10Y"
            """Brazil Government Bond 10Y"""

            STOCK_MARKET: str = "IBOV"
            """Brazil Stock Market"""

            CURRENCY: str = "USDBRL"
            """Brazil Currency"""

        class Brunei(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDBND"
            """Brunei Currency"""

        class Bulgaria(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "BULGARIAGOVBON10Y"
            """Bulgaria Government Bond 10Y"""

            INTERBANK_RATE: str = "BULGARIAINTRAT"
            """Bulgaria Interbank Rate"""

            STOCK_MARKET: str = "SOFIX"
            """Bulgaria Stock Market"""

            CURRENCY: str = "USDBGN"
            """Bulgaria Currency"""

        class Burundi(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDBIF"
            """Burundi Currency"""

        class Cambodia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDKHR"
            """Cambodia Currency"""

        class Canada(System.Object):
            """This class has no documentation."""

            BANK_LENDING_RATE: str = "CANADABANLENRAT"
            """Canada Bank Lending Rate"""

            INTERBANK_RATE: str = "CANADAINTRAT"
            """Canada Interbank Rate"""

            DEPOSIT_INTEREST_RATE: str = "CANFRINRDPST"
            """Canada Deposit Interest Rate"""

            INTEREST_RATE: str = "CCLR"
            """Canada Interest Rate"""

            GOVERNMENT_BOND_10Y: str = "GCAN10YR"
            """Canada Government Bond 10Y"""

            CONSUMER_CONFIDENCE: str = "OECAI001"
            """Canada Consumer Confidence"""

            STOCK_MARKET: str = "SPTSX"
            """Canada Stock Market"""

            CURRENCY: str = "USDCAD"
            """Canada Currency"""

        class CapeVerde(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDCVE"
            """CapeVerde Currency"""

        class CaymanIslands(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDKYD"
            """CaymanIslands Currency"""

        class Chile(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "CHILEGOVBON10Y"
            """Chile Government Bond 10y"""

            INTERBANK_RATE: str = "CHILEINTRAT"
            """Chile Interbank Rate"""

            STOCK_MARKET: str = "IGPA"
            """Chile Stock Market"""

            CURRENCY: str = "USDCLP"
            """Chile Currency"""

        class China(System.Object):
            """This class has no documentation."""

            CASH_RESERVE_RATIO: str = "CHINACASRESRAT"
            """China Cash Reserve Ratio"""

            INTERBANK_RATE: str = "CHINAINTRAT"
            """China Interbank Rate"""

            REVERSE_REPO_RATE: str = "CHINAREVREPRAT"
            """China Reverse Repo Rate"""

            GOVERNMENT_BOND_10Y: str = "GCNY10YR"
            """China Government Bond 10Y"""

            STOCK_MARKET: str = "SHCOMP"
            """China Stock Market"""

            CURRENCY: str = "USDCNY"
            """China Currency"""

        class Colombia(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "COGR10Y"
            """Colombia Government Bond 10Y"""

            STOCK_MARKET: str = "COLCAP"
            """Colombia Stock Market"""

            INTERBANK_RATE: str = "COLOMBIAINTRAT"
            """Colombia Interbank Rate"""

            CURRENCY: str = "USDCOP"
            """Colombia Currency"""

        class Commodity(System.Object):
            """This class has no documentation."""

            BALTIC_EXCHANGE_DRY_INDEX: str = "BALTIC"
            """Commodity Baltic Exchange Dry Index"""

            BEEF: str = "BEEF"
            """Commodity Beef"""

            BITUMEN: str = "BIT"
            """Commodity Bitumen"""

            CORN: str = "C-1"
            """Commodity Corn"""

            COCOA: str = "CC1"
            """Commodity Cocoa"""

            CHEESE: str = "CHEESE1"
            """Commodity Cheese"""

            CRUDE_OIL: str = "CL1"
            """Commodity Crude oil"""

            BRENT_CRUDE_OIL: str = "CO1"
            """Commodity Brent crude oil"""

            COAL: str = "COAL"
            """Commodity Coal"""

            COBALT: str = "COBALT"
            """Commodity Cobalt"""

            CRB_COMMODITY_INDEX: str = "CRB"
            """Commodity CRB Commodity Index"""

            COTTON: str = "CT1"
            """Commodity Cotton"""

            ETHANOL: str = "DL1"
            """Commodity Ethanol"""

            FEEDER_CATTLE: str = "FC1"
            """Commodity Feeder Cattle"""

            GSCI_COMMODITY_INDEX: str = "GSCI"
            """Commodity GSCI Commodity Index"""

            COPPER: str = "HG1"
            """Commodity Copper"""

            HEATING_OIL: str = "HO1"
            """Commodity Heating oil"""

            MANGANESE_ORE: str = "IMR"
            """Commodity Manganese Ore"""

            IRON_ORE: str = "IRONORE"
            """Commodity Iron Ore"""

            RUBBER: str = "JN1"
            """Commodity Rubber"""

            ORANGE_JUICE: str = "JO1"
            """Commodity Orange Juice"""

            COFFEE: str = "KC1"
            """Commodity Coffee"""

            LUMBER: str = "LB1"
            """Commodity Lumber"""

            LIVE_CATTLE: str = "LC1"
            """Commodity Live Cattle"""

            LEAN_HOGS: str = "LH1"
            """Commodity Lean Hogs"""

            LITHIUM: str = "LITHIUM"
            """Commodity Lithium"""

            ALUMINUM: str = "LMAHDS03"
            """Commodity Aluminum"""

            LME_INDEX: str = "LME"
            """Commodity LME Index"""

            MOLYBDENUM: str = "LMMLDS03"
            """Commodity Molybdenum"""

            NICKEL: str = "LMNIDS03"
            """Commodity Nickel"""

            LEAD: str = "LMPBDS03"
            """Commodity Lead"""

            TIN: str = "LMSNDS03"
            """Commodity Tin"""

            ZINC: str = "LMZSDS03"
            """Commodity Zinc"""

            MILK: str = "MILK"
            """Commodity Milk"""

            NAPHTHA: str = "NAPHTHA"
            """Commodity Naphtha"""

            NATURAL_GAS: str = "NG1"
            """Commodity Natural gas"""

            OAT: str = "O-1"
            """Commodity Oat"""

            WOOL: str = "OL1"
            """Commodity Wool"""

            PALM_OIL: str = "PALMOIL"
            """Commodity Palm Oil"""

            PROPANE: str = "PROPANE"
            """Commodity Propane"""

            RHODIUM: str = "RHODIUM"
            """Commodity RHODIUM"""

            RICE: str = "RR1"
            """Commodity Rice"""

            CANOLA: str = "RS1"
            """Commodity Canola"""

            SOYBEANS: str = "S-1"
            """Commodity Soybeans"""

            SUGAR: str = "SB1"
            """Commodity Sugar"""

            SODA_ASH: str = "SODASH"
            """Commodity Soda Ash"""

            NEODYMIUM: str = "SREMNDM"
            """Commodity Neodymium"""

            STEEL: str = "STEEL"
            """Commodity Steel"""

            IRON_ORE_62_PERCENT_FE: str = "TIOC"
            """Commodity Iron Ore 62% FE"""

            URANIUM: str = "URANIUM"
            """Commodity Uranium"""

            WHEAT: str = "W-1"
            """Commodity Wheat"""

            SILVER: str = "XAGUSD"
            """Commodity Silver"""

            GOLD: str = "XAUUSD"
            """Commodity Gold"""

            GASOLINE: str = "XB1"
            """Commodity Gasoline"""

            PALLADIUM: str = "XPDUSD"
            """Commodity Palladium"""

            PLATINUM: str = "XPTUSD"
            """Commodity Platinum"""

        class Comoros(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDKMF"
            """Comoros Currency"""

        class Congo(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDCDF"
            """Congo Currency"""

        class CostaRica(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "CRSMBCT"
            """CostaRica Stock Market"""

            CURRENCY: str = "USDCRC"
            """CostaRica Currency"""

        class Croatia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "CRO"
            """Croatia Stock Market"""

            GOVERNMENT_BOND_10Y: str = "CROATIAGOVD10Y"
            """Croatia Government Bond 10Y"""

            INTERBANK_RATE: str = "CROATIAINTRAT"
            """Croatia Interbank Rate"""

            CURRENCY: str = "USDHRV"
            """Croatia Currency"""

        class Cuba(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDCUC"
            """Cuba Currency"""

        class Cyprus(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "CYSMMAPA"
            """Cyprus Stock Market"""

        class CzechRepublic(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "CZECHREPUINTRAT"
            """CzechRepublic Interbank Rate"""

            GOVERNMENT_BOND_10Y: str = "CZGB10YR"
            """CzechRepublic Government Bond 10Y"""

            STOCK_MARKET: str = "PX"
            """CzechRepublic Stock Market"""

            CURRENCY: str = "USDCZK"
            """CzechRepublic Currency"""

        class Denmark(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "DENMARKINTRAT"
            """Denmark Interbank Rate"""

            GOVERNMENT_BOND_10Y: str = "GDGB10YR"
            """Denmark Government Bond 10Y"""

            STOCK_MARKET: str = "KFX"
            """Denmark Stock Market"""

            CURRENCY: str = "USDDKK"
            """Denmark Currency"""

        class Djibouti(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDDJF"
            """Djibouti Currency"""

        class DominicanRepublic(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDDOP"
            """DominicanRepublic Currency"""

        class Ecuador(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "ECU"
            """Ecuador Stock Market"""

            INTERBANK_RATE: str = "ECUADORINTRATI"
            """Ecuador Interbank Rate"""

        class Egypt(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "CASE"
            """Egypt Stock Market"""

            INTERBANK_RATE: str = "EGYPTINTRAT"
            """Egypt Interbank Rate"""

            INTEREST_RATE: str = "EGYPTINTRATE"
            """Egypt Interest Rate"""

            LENDING_RATE: str = "EGYPTLENRAT"
            """Egypt Lending Rate"""

            CURRENCY: str = "USDEGP"
            """Egypt Currency"""

        class Eritrea(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDERN"
            """Eritrea Currency"""

        class Estonia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "TALSE"
            """Estonia Stock Market"""

        class Ethiopia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDETB"
            """Ethiopia Currency"""

        class EuroArea(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "EMUEVOLVINTRAT"
            """EuroArea Interbank Rate"""

            LENDING_RATE: str = "EUROAREALENRAT"
            """EuroArea Lending Rate"""

            ZEW_ECONOMIC_SENTIMENT_INDEX: str = "EUROAREAZEWECOSENIND"
            """EuroArea Zew Economic Sentiment Index"""

            STOCK_MARKET: str = "SX5E"
            """EuroArea Stock Market"""

        class Fiji(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDFJD"
            """Fiji Currency"""

        class Finland(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "FINLANDINTRAT"
            """Finland Interbank Rate"""

            GOVERNMENT_BOND_10Y: str = "GFIN10YR"
            """Finland Government Bond 10Y"""

            STOCK_MARKET: str = "HEX25"
            """Finland Stock Market"""

        class France(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "CAC"
            """France Stock Market"""

            GOVERNMENT_BOND_10Y: str = "GFRN10"
            """France Government Bond 10Y"""

        class Gambia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDGMD"
            """Gambia Currency"""

        class Georgia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDGEL"
            """Georgia Currency"""

        class Germany(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "DAX"
            """Germany Stock Market"""

            GOVERNMENT_BOND_10Y: str = "GDBR10"
            """Germany Government Bond 10Y"""

            TWO_YEAR_NOTE_YIELD: str = "GERMANY2YNY"
            """Germany 2 Year Note Yield"""

            ZEW_ECONOMIC_SENTIMENT_INDEX: str = "GERMANYZEWECOSENIND"
            """Germany Zew Economic Sentiment Index"""

            CONSUMER_CONFIDENCE: str = "GRCCI"
            """Germany Consumer Confidence"""

        class Ghana(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "GGSECI"
            """Ghana Stock Market"""

            CURRENCY: str = "USDGHS"
            """Ghana Currency"""

        class Greece(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "ASE"
            """Greece Stock Market"""

            GOVERNMENT_BOND_10Y: str = "GGGB10YR"
            """Greece Government Bond 10Y"""

            TWO_YEAR_NOTE_YIELD: str = "GREECE2YNY"
            """Greece 2 Year Note Yield"""

        class Guatemala(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDGTQ"
            """Guatemala Currency"""

        class Guinea(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDGNF"
            """Guinea Currency"""

        class Guyana(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDGYD"
            """Guyana Currency"""

        class Haiti(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDHTG"
            """Haiti Currency"""

        class Honduras(System.Object):
            """This class has no documentation."""

            INTEREST_RATE: str = "HONURASINTTRATE"
            """Honduras Interest Rate"""

            CURRENCY: str = "USDHNL"
            """Honduras Currency"""

        class HongKong(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GHKGB10Y"
            """HongKong Government Bond 10Y"""

            INTERBANK_RATE: str = "HONGKONGINTRAT"
            """HongKong Interbank Rate"""

            STOCK_MARKET: str = "HSI"
            """HongKong Stock Market"""

            CURRENCY: str = "USDHKD"
            """HongKong Currency"""

        class Hungary(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BUX"
            """Hungary Stock Market"""

            GOVERNMENT_BOND_10Y: str = "GHGB10YR"
            """Hungary Government Bond 10Y"""

            INTERBANK_RATE: str = "HUNGARYINTRAT"
            """Hungary Interbank Rate"""

            CURRENCY: str = "USDHUF"
            """Hungary Currency"""

        class Iceland(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "ICELANDGOVBON10Y"
            """Iceland Government Bond 10y"""

            INTERBANK_RATE: str = "ICELANDINTRAT"
            """Iceland Interbank Rate"""

            STOCK_MARKET: str = "ICEXI"
            """Iceland Stock Market"""

            CURRENCY: str = "USDISK"
            """Iceland Currency"""

        class India(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GIND10YR"
            """India Government Bond 10Y"""

            CASH_RESERVE_RATIO: str = "INDIACASRESRAT"
            """India Cash Reserve Ratio"""

            INTEREST_RATE: str = "RSPOYLD"
            """India Interest Rate"""

            STOCK_MARKET: str = "SENSEX"
            """India Stock Market"""

            CURRENCY: str = "USDINR"
            """India Currency"""

        class Indonesia(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GIDN10YR"
            """Indonesia Government Bond 10Y"""

            INTERBANK_RATE: str = "INDONESIAINTRAT"
            """Indonesia Interbank Rate"""

            STOCK_MARKET: str = "JCI"
            """Indonesia Stock Market"""

            CURRENCY: str = "USDIDR"
            """Indonesia Currency"""

        class Iraq(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDIQD"
            """Iraq Currency"""

        class Ireland(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GIGB10YR"
            """Ireland Government Bond 10Y"""

            STOCK_MARKET: str = "ISEQ"
            """Ireland Stock Market"""

        class Israel(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GISR10YR"
            """Israel Government Bond 10Y"""

            INTEREST_RATE: str = "ISBRATE"
            """Israel Interest Rate"""

            INTERBANK_RATE: str = "ISRAELINTRAT"
            """Israel Interbank Rate"""

            STOCK_MARKET: str = "TA-100"
            """Israel Stock Market"""

            CURRENCY: str = "USDILS"
            """Israel Currency"""

        class Italy(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "FTSEMIB"
            """Italy Stock Market"""

            GOVERNMENT_BOND_10Y: str = "GBTPGR10"
            """Italy Government Bond 10Y"""

            TWO_YEAR_NOTE_YIELD: str = "ITALY2YNY"
            """Italy 2 Year Note Yield"""

        class IvoryCoast(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDXOF"
            """IvoryCoast Currency"""

        class Jamaica(System.Object):
            """This class has no documentation."""

            INTEREST_RATE: str = "JAMAICAINTTRATE"
            """Jamaica Interest Rate"""

            STOCK_MARKET: str = "JMSMX"
            """Jamaica Stock Market"""

            CURRENCY: str = "USDJMD"
            """Jamaica Currency"""

        class Japan(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GJGB10"
            """Japan Government Bond 10Y"""

            TWO_YEAR_NOTE_YIELD: str = "JAPAN2YNY"
            """Japan 2 Year Note Yield"""

            INTERBANK_RATE: str = "JAPANINTRAT"
            """Japan Interbank Rate"""

            DEPOSIT_INTEREST_RATE: str = "JPNFRINRDPST"
            """Japan Deposit Interest Rate"""

            STOCK_MARKET: str = "NKY"
            """Japan Stock Market"""

            CURRENCY: str = "USDJPY"
            """Japan Currency"""

        class Jordan(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "JOSMGNFF"
            """Jordan Stock Market"""

            CURRENCY: str = "USDJOR"
            """Jordan Currency"""

        class Kazakhstan(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "KAZAKHSTANINTRAT"
            """Kazakhstan Interbank Rate"""

            INTEREST_RATE: str = "KAZAKHSTANINTRATE"
            """Kazakhstan Interest Rate"""

            STOCK_MARKET: str = "KZKAK"
            """Kazakhstan Stock Market"""

            CURRENCY: str = "USDKZT"
            """Kazakhstan Currency"""

        class Kenya(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "KENYAGOVBON10Y"
            """Kenya Government Bond 10y"""

            STOCK_MARKET: str = "KNSMIDX"
            """Kenya Stock Market"""

            CURRENCY: str = "USDKES"
            """Kenya Currency"""

        class Kuwait(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "KUWAITINTRAT"
            """Kuwait Interbank Rate"""

            CURRENCY: str = "USDKWD"
            """Kuwait Currency"""

        class Kyrgyzstan(System.Object):
            """This class has no documentation."""

            INTEREST_RATE: str = "KYRSTANINTTRATE"
            """Kyrgyzstan Interest Rate"""

            CURRENCY: str = "USDKGS"
            """Kyrgyzstan Currency"""

        class Laos(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "LSXC"
            """Laos Stock Market"""

            CURRENCY: str = "USDLAK"
            """Laos Currency"""

        class Latvia(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "LATVIAGOVBON10Y"
            """Latvia Government Bond 10y"""

            INTERBANK_RATE: str = "LATVIAINTRAT"
            """Latvia Interbank Rate"""

            STOCK_MARKET: str = "RIGSE"
            """Latvia Stock Market"""

        class Lebanon(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BLOM"
            """Lebanon Stock Market"""

            CURRENCY: str = "USDLBP"
            """Lebanon Currency"""

        class Lesotho(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDLSL"
            """Lesotho Currency"""

        class Liberia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDLRD"
            """Liberia Currency"""

        class Libya(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDLYD"
            """Libya Currency"""

        class Lithuania(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "LITHUANIAGOVBON10Y"
            """Lithuania Government Bond 10y"""

            STOCK_MARKET: str = "VILSE"
            """Lithuania Stock Market"""

        class Luxembourg(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "LUXXX"
            """Luxembourg Stock Market"""

        class Macau(System.Object):
            """This class has no documentation."""

            INTERBANK_RATE: str = "MACAOINTRAT"
            """Macau Interbank Rate"""

            CURRENCY: str = "USDMOP"
            """Macau Currency"""

        class Macedonia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "MBI"
            """Macedonia Stock Market"""

            CURRENCY: str = "USDMKD"
            """Macedonia Currency"""

        class Madagascar(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDMGA"
            """Madagascar Currency"""

        class Malawi(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDMWK"
            """Malawi Currency"""

        class Malaysia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "FBMKLCI"
            """Malaysia Stock Market"""

            INTERBANK_RATE: str = "MALAYSIAINTRAT"
            """Malaysia Interbank Rate"""

            INTEREST_RATE: str = "MAOPRATE"
            """Malaysia Interest Rate"""

            GOVERNMENT_BOND_10Y: str = "MGIY10Y"
            """Malaysia Government Bond 10Y"""

            CURRENCY: str = "USDMYR"
            """Malaysia Currency"""

        class Maldives(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDMVR"
            """Maldives Currency"""

        class Malta(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "MALTEX"
            """Malta Stock Market"""

        class Mauritius(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "SEMDEX"
            """Mauritius Stock Market"""

            CURRENCY: str = "USDMUR"
            """Mauritius Currency"""

        class Mexico(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GMXN10YR"
            """Mexico Government Bond 10Y"""

            STOCK_MARKET: str = "MEXBOL"
            """Mexico Stock Market"""

            INTEREST_RATE: str = "MXONBR"
            """Mexico Interest Rate"""

            CURRENCY: str = "USDMXN"
            """Mexico Currency"""

        class Moldova(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDMDL"
            """Moldova Currency"""

        class Mongolia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "MSETOP"
            """Mongolia Stock Market"""

            CURRENCY: str = "USDMNT"
            """Mongolia Currency"""

        class Morocco(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "MOSENEW"
            """Morocco Stock Market"""

            CURRENCY: str = "USDMAD"
            """Morocco Currency"""

        class Mozambique(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDMZN"
            """Mozambique Currency"""

        class Myanmar(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDMMK"
            """Myanmar Currency"""

        class Namibia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "FTN098"
            """Namibia Stock Market"""

            CURRENCY: str = "USDNAD"
            """Namibia Currency"""

        class Nepal(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDNPR"
            """Nepal Currency"""

        class Netherlands(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "AEX"
            """Netherlands Stock Market"""

            GOVERNMENT_BOND_10Y: str = "GNTH10YR"
            """Netherlands Government Bond 10Y"""

        class NewCaledonia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDXPF"
            """NewCaledonia Currency"""

        class NewZealand(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GNZGB10"
            """NewZealand Government Bond 10Y"""

            GLOBAL_DAIRY_TRADE_PRICE_INDEX: str = "NEWZEALANGDTPI"
            """NewZealand Global Dairy Trade Price Index"""

            CURRENCY: str = "NZDUSD"
            """NewZealand Currency"""

            DEPOSIT_INTEREST_RATE: str = "NZLFRINRDPST"
            """NewZealand Deposit Interest Rate"""

            INTEREST_RATE: str = "NZOCRS"
            """NewZealand Interest Rate"""

            STOCK_MARKET: str = "NZSE50FG"
            """NewZealand Stock Market"""

        class Nicaragua(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDNIO"
            """Nicaragua Currency"""

        class Nigeria(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "NGSEINDX"
            """Nigeria Stock Market"""

            CASH_RESERVE_RATIO: str = "NIGERIACASRESRAT"
            """Nigeria Cash Reserve Ratio"""

            GOVERNMENT_BOND_10Y: str = "NIGERIAGOVBON10Y"
            """Nigeria Government Bond 10y"""

            INTERBANK_RATE: str = "NIGERIAINTRAT"
            """Nigeria Interbank Rate"""

            CURRENCY: str = "USDNGN"
            """Nigeria Currency"""

        class NorthKorea(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "NORTHKORECUR"
            """NorthKorea Currency"""

        class Norway(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GNOR10YR"
            """Norway Government Bond 10Y"""

            INTERBANK_RATE: str = "NORWAYINTRAT"
            """Norway Interbank Rate"""

            STOCK_MARKET: str = "OSEAX"
            """Norway Stock Market"""

            CURRENCY: str = "USDNOK"
            """Norway Currency"""

        class Oman(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "MSM30"
            """Oman Stock Market"""

            CURRENCY: str = "USDOMR"
            """Oman Currency"""

        class Pakistan(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "KSE100"
            """Pakistan Stock Market"""

            INTEREST_RATE: str = "PAPRSBP"
            """Pakistan Interest Rate"""

            GOVERNMENT_BOND_10Y: str = "PKIB10YR"
            """Pakistan Government Bond 10Y"""

            CURRENCY: str = "USDPKR"
            """Pakistan Currency"""

        class Panama(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BVPSBVPS"
            """Panama Stock Market"""

            CURRENCY: str = "USDPAB"
            """Panama Currency"""

        class PapuaNewGuinea(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDPGK"
            """PapuaNewGuinea Currency"""

        class Paraguay(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDPYG"
            """Paraguay Currency"""

        class Peru(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GRPE10Y"
            """Peru Government Bond 10Y"""

            STOCK_MARKET: str = "IGBVL"
            """Peru Stock Market"""

            INTERBANK_RATE: str = "PERUINTRAT"
            """Peru Interbank Rate"""

            INTEREST_RATE: str = "PRRRONUS"
            """Peru Interest Rate"""

            CURRENCY: str = "USDPEN"
            """Peru Currency"""

        class Philippines(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "PCOMP"
            """Philippines Stock Market"""

            GOVERNMENT_BOND_10Y: str = "PHILIPPINEGOVBON10Y"
            """Philippines Government Bond 10y"""

            INTERBANK_RATE: str = "PHILIPPINEINTRAT"
            """Philippines Interbank Rate"""

            INTEREST_RATE: str = "PHILIPPINESINTRATE"
            """Philippines Interest Rate"""

            CURRENCY: str = "USDPHP"
            """Philippines Currency"""

        class Poland(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "POGB10YR"
            """Poland Government Bond 10Y"""

            INTERBANK_RATE: str = "POLANDINTRAT"
            """Poland Interbank Rate"""

            DEPOSIT_INTEREST_RATE: str = "POLFRINRDPST"
            """Poland Deposit Interest Rate"""

            CURRENCY: str = "USDPLN"
            """Poland Currency"""

            STOCK_MARKET: str = "WIG"
            """Poland Stock Market"""

        class Portugal(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GSPT10YR"
            """Portugal Government Bond 10Y"""

            TWO_YEAR_NOTE_YIELD: str = "PORTUGAL2YNY"
            """Portugal 2 Year Note Yield"""

            STOCK_MARKET: str = "PSI20"
            """Portugal Stock Market"""

        class Qatar(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "DSM"
            """Qatar Stock Market"""

            GOVERNMENT_BOND_10Y: str = "QATARGOVBON10Y"
            """Qatar Government Bond 10y"""

            REVERSE_REPO_RATE: str = "QATARREVREPRAT"
            """Qatar Reverse Repo Rate"""

            CURRENCY: str = "USDQAR"
            """Qatar Currency"""

        class Romania(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BET"
            """Romania Stock Market"""

            GOVERNMENT_BOND_10Y: str = "ROMANIAGOVBON10Y"
            """Romania Government Bond 10Y"""

            INTERBANK_RATE: str = "ROMANIAINTRAT"
            """Romania Interbank Rate"""

            CURRENCY: str = "USDRON"
            """Romania Currency"""

        class Russia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "INDEXCF"
            """Russia Stock Market"""

            GOVERNMENT_BOND_10Y: str = "RUGE10Y"
            """Russia Government Bond 10Y"""

            CENTRAL_BANK_BALANCE_SHEET: str = "RUSSIACENBANBALSHE"
            """Russia Central Bank Balance Sheet"""

            CURRENCY: str = "USDRUB"
            """Russia Currency"""

        class Rwanda(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDRWF"
            """Rwanda Currency"""

        class SaoTomeAndPrincipe(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSTD"
            """SaoTomeAndPrincipe Currency"""

        class SaudiArabia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "SASEIDX"
            """SaudiArabia Stock Market"""

            REVERSE_REPO_RATE: str = "SAUDIARABREVREPRAT"
            """SaudiArabia Reverse Repo Rate"""

            DEPOSIT_INTEREST_RATE: str = "SAUFRINRDPST"
            """SaudiArabia Deposit Interest Rate"""

            CURRENCY: str = "USDSAR"
            """SaudiArabia Currency"""

        class Serbia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "BELEX15"
            """Serbia Stock Market"""

            INTERBANK_RATE: str = "SERBIAINTRAT"
            """Serbia Interbank Rate"""

            INTEREST_RATE: str = "SERRBIAINTTRATE"
            """Serbia Interest Rate"""

            DEPOSIT_INTEREST_RATE: str = "SRBFRINRDPST"
            """Serbia Deposit Interest Rate"""

            CURRENCY: str = "USDSRB"
            """Serbia Currency"""

        class Seychelles(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSCR"
            """Seychelles Currency"""

        class SierraLeone(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSLL"
            """SierraLeone Currency"""

        class Singapore(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "FSSTI"
            """Singapore Stock Market"""

            GOVERNMENT_BOND_10Y: str = "MASB10Y"
            """Singapore Government Bond 10Y"""

            INTERBANK_RATE: str = "SINGAPOREINTRAT"
            """Singapore Interbank Rate"""

            CURRENCY: str = "USDSGD"
            """Singapore Currency"""

        class Slovakia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "SKSM"
            """Slovakia Stock Market"""

            GOVERNMENT_BOND_10Y: str = "SLOVAKIAGOVBON10Y"
            """Slovakia Government Bond 10y"""

        class Slovenia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "SBITOP"
            """Slovenia Stock Market"""

            GOVERNMENT_BOND_10Y: str = "SLOVENIAGOVBON10Y"
            """Slovenia Government Bond 10y"""

        class Somalia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSOS"
            """Somalia Currency"""

        class SouthAfrica(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GSAB10YR"
            """SouthAfrica Government Bond 10Y"""

            STOCK_MARKET: str = "JALSH"
            """SouthAfrica Stock Market"""

            INTERBANK_RATE: str = "SOUTHAFRIINTRAT"
            """SouthAfrica Interbank Rate"""

            CURRENCY: str = "USDZAR"
            """SouthAfrica Currency"""

        class SouthKorea(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GVSK10YR"
            """SouthKorea Government Bond 10Y"""

            STOCK_MARKET: str = "KOSPI"
            """SouthKorea Stock Market"""

            INTERBANK_RATE: str = "SOUTHKOREINTRAT"
            """SouthKorea Interbank Rate"""

            CURRENCY: str = "USDKRW"
            """SouthKorea Currency"""

        class Spain(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GSPG10YR"
            """Spain Government Bond 10Y"""

            STOCK_MARKET: str = "IBEX"
            """Spain Stock Market"""

            INTERBANK_RATE: str = "SPAININTRAT"
            """Spain Interbank Rate"""

        class SriLanka(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "CSEALL"
            """SriLanka Stock Market"""

            INTEREST_RATE: str = "SRI-LANKAINTRATE"
            """SriLanka Interest Rate"""

            CASH_RESERVE_RATIO: str = "SRILANKACASRESRAT"
            """SriLanka Cash Reserve Ratio"""

            INTERBANK_RATE: str = "SRILANKAINTRAT"
            """SriLanka Interbank Rate"""

            LENDING_RATE: str = "SRILANKALENRAT"
            """SriLanka Lending Rate"""

            CURRENCY: str = "USDLKR"
            """SriLanka Currency"""

        class Sudan(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSDG"
            """Sudan Currency"""

        class Suriname(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSRD"
            """Suriname Currency"""

        class Swaziland(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSZL"
            """Swaziland Currency"""

        class Sweden(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GSGB10YR"
            """Sweden Government Bond 10Y"""

            STOCK_MARKET: str = "OMX"
            """Sweden Stock Market"""

            INTERBANK_RATE: str = "SWEDENINTRAT"
            """Sweden Interbank Rate"""

            CURRENCY: str = "USDSEK"
            """Sweden Currency"""

        class Switzerland(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "GSWISS10"
            """Switzerland Government Bond 10Y"""

            STOCK_MARKET: str = "SMI"
            """Switzerland Stock Market"""

            INTERBANK_RATE: str = "SWITZERLANINTRAT"
            """Switzerland Interbank Rate"""

            CURRENCY: str = "USDCHF"
            """Switzerland Currency"""

        class Syria(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDSYP"
            """Syria Currency"""

        class Taiwan(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "TAIWANGOVBON10Y"
            """Taiwan Government Bond 10y"""

            INTERBANK_RATE: str = "TAIWANINTRAT"
            """Taiwan Interbank Rate"""

            INTEREST_RATE: str = "TAIWANIR"
            """Taiwan Interest Rate"""

            STOCK_MARKET: str = "TWSE"
            """Taiwan Stock Market"""

            CURRENCY: str = "USDTWD"
            """Taiwan Currency"""

        class Tajikistan(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDTJS"
            """Tajikistan Currency"""

        class Tanzania(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "DARSDSEI"
            """Tanzania Stock Market"""

            CURRENCY: str = "USDTZS"
            """Tanzania Currency"""

        class Thailand(System.Object):
            """This class has no documentation."""

            INTEREST_RATE: str = "BTRR1DAY"
            """Thailand Interest Rate"""

            GOVERNMENT_BOND_10Y: str = "GVTL10YR"
            """Thailand Government Bond 10Y"""

            STOCK_MARKET: str = "SET50"
            """Thailand Stock Market"""

            INTERBANK_RATE: str = "THAILANDINTRAT"
            """Thailand Interbank Rate"""

            CURRENCY: str = "USDTHB"
            """Thailand Currency"""

        class TrinidadAndTobago(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDTTD"
            """TrinidadAndTobago Currency"""

        class Tunisia(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "TUSISE"
            """Tunisia Stock Market"""

            CURRENCY: str = "USDTND"
            """Tunisia Currency"""

        class Turkey(System.Object):
            """This class has no documentation."""

            GOVERNMENT_BOND_10Y: str = "TURKEYGOVBON10Y"
            """Turkey Government Bond 10y"""

            INTERBANK_RATE: str = "TURKEYINTRAT"
            """Turkey Interbank Rate"""

            CURRENCY: str = "USDTRY"
            """Turkey Currency"""

            STOCK_MARKET: str = "XU100"
            """Turkey Stock Market"""

        class Turkmenistan(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDTMT"
            """Turkmenistan Currency"""

        class Uganda(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDUGX"
            """Uganda Currency"""

        class Ukraine(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "PFTS"
            """Ukraine Stock Market"""

            INTERBANK_RATE: str = "UKRAINEINTRAT"
            """Ukraine Interbank Rate"""

            CURRENCY: str = "USDUAH"
            """Ukraine Currency"""

        class UnitedArabEmirates(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "ADSMI"
            """UnitedArabEmirates Stock Market"""

            INTERBANK_RATE: str = "UNITEDARAINTRAT"
            """UnitedArabEmirates Interbank Rate"""

            CURRENCY: str = "USDAED"
            """UnitedArabEmirates Currency"""

        class UnitedKingdom(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "GBPUSD"
            """UnitedKingdom Currency"""

            GOVERNMENT_BOND_10Y: str = "GUKG10"
            """UnitedKingdom Government Bond 10Y"""

            STOCK_MARKET: str = "UKX"
            """UnitedKingdom Stock Market"""

            TWO_YEAR_NOTE_YIELD: str = "UNITEDKIN2YNY"
            """UnitedKingdom 2 Year Note Yield"""

            INTERBANK_RATE: str = "UNITEDKININTRAT"
            """UnitedKingdom Interbank Rate"""

        class UnitedStates(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "DXY"
            """UnitedStates Currency"""

            INTEREST_RATE: str = "FDTR"
            """UnitedStates Interest Rate"""

            STOCK_MARKET: str = "INDU"
            """UnitedStates Stock Market"""

            TWO_YEAR_NOTE_YIELD: str = "UNITEDSTA2YEANOTYIE"
            """UnitedStates 2 Year Note Yield"""

            ECONOMIC_OPTIMISM_INDEX: str = "UNITEDSTAECOOPTIND"
            """UnitedStates Economic Optimism Index"""

            FOREIGN_DIRECT_INVESTMENT: str = "UNITEDSTAFORDIRINV"
            """UnitedStates Foreign Direct Investment"""

            INTERBANK_RATE: str = "UNITEDSTAINTRAT"
            """UnitedStates Interbank Rate"""

            NAHB_HOUSING_MARKET_INDEX: str = "UNITEDSTANAHHOUMARIN"
            """UnitedStates Nahb Housing Market Index"""

            NY_EMPIRE_STATE_MANUFACTURING_INDEX: str = "UNITEDSTANYEMPSTAMAN"
            """UnitedStates NY Empire State Manufacturing Index"""

            REDBOOK_INDEX: str = "UNITEDSTAREDIND"
            """UnitedStates Redbook Index"""

            GOVERNMENT_BOND_10Y: str = "USGG10YR"
            """UnitedStates Government Bond 10Y"""

            CRUDE_OIL_RIGS: str = "USOILRIGS"
            """UnitedStates Crude Oil Rigs"""

        class Uruguay(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDURY"
            """Uruguay Currency"""

        class Uzbekistan(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDUZS"
            """Uzbekistan Currency"""

        class Venezuela(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "IBVC"
            """Venezuela Stock Market"""

            CURRENCY: str = "USDVES"
            """Venezuela Currency"""

            GOVERNMENT_BOND_10Y: str = "VENEZUELAGOVBON10Y"
            """Venezuela Government Bond 10y"""

            DEPOSIT_INTEREST_RATE: str = "VENFRINRDPST"
            """Venezuela Deposit Interest Rate"""

        class Vietnam(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDVND"
            """Vietnam Currency"""

            GOVERNMENT_BOND_10Y: str = "VIETNAMGOVBON10Y"
            """Vietnam Government Bond 10y"""

            INTERBANK_RATE: str = "VIETNAMINTRAT"
            """Vietnam Interbank Rate"""

            STOCK_MARKET: str = "VNINDEX"
            """Vietnam Stock Market"""

        class Yemen(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDYER"
            """Yemen Currency"""

        class Zambia(System.Object):
            """This class has no documentation."""

            CURRENCY: str = "USDZMK"
            """Zambia Currency"""

            GOVERNMENT_BOND_10Y: str = "ZAMBIAGOVBON10Y"
            """Zambia Government Bond 10y"""

            INTEREST_RATE: str = "ZAMMBIAINTTRATE"
            """Zambia Interest Rate"""

        class Zimbabwe(System.Object):
            """This class has no documentation."""

            STOCK_MARKET: str = "INDZI"
            """Zimbabwe Stock Market"""

    class Event(System.Object):
        """The Event class contains all events normalized for your convenience"""

        class Australia(System.Object):
            """Australia"""

            AIG_PERFORMANCE_CONSTRUCTION_INDEX: str = "aig performance construction index"
            """AiG Performance Construction Index"""

            AIG_PERFORMANCE_MANUFACTURING_INDEX: str = "aig performance manufacturing index"
            """AiG Performance of Mfg Index"""

            AIG_PERFORMANCE_SERVICES_INDEX: str = "aig performance services index"
            """AiG Performance of Services Index"""

            ANZAC_DAY: str = "anzac day"
            """ANZAC Day"""

            ANZ_INTERNET_JOB_ADVERTISEMENTS_MO_M: str = "anz internet job advertisements mom"
            """ANZ Internet Job Ads MoM"""

            ANZ_JOB_ADVERTISEMENTS: str = "anz job advertisements"
            """ANZ Job Advertisements"""

            ANZ_JOB_ADVERTISEMENTS_MO_M: str = "anz job advertisements mom"
            """ANZ Job Advertisement MoM"""

            ANZ_NEWSPAPER_JOB_ADVERTISEMENTS_MO_M: str = "anz newspaper job advertisements mom"
            """ANZ Newspaper Job Ads MoM"""

            AUSTRALIA_DAY: str = "australia day"
            """Australia Day"""

            AUSTRALIA_DAY_OBSERVED: str = "australia day observed"
            """Australia Day (Observed)"""

            AUSTRALIA_DAY_SUBSTITUTE_DAY: str = "australia day substitute day"
            """Australia Day (substitute day)"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUILDING_PERMITS_MO_M: str = "building permits mom"
            """Building Permits (MoM)"""

            BUILDING_PERMITS_YO_Y: str = "building permits yoy"
            """Building Permits (YoY)"""

            BUSINESS_INVENTORIES_QO_Q: str = "business inventories qoq"
            """Business Inventories QoQ"""

            CAPITAL_EXPENDITURE_QO_Q: str = "capital expenditure qoq"
            """Capital Expenditure QoQ"""

            CB_LEADING_ECONOMIC_INDEX: str = "cb leading economic index"
            """CB Leading Index"""

            CB_LEADING_ECONOMIC_INDEX_MO_M: str = "cb leading economic index mom"
            """CB Leading Index MoM"""

            CB_LEADING_ECONOMIC_INDICATORS: str = "cb leading economic indicators"
            """CB Leading Indicator"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            COMMBANK_COMPOSITE_PURCHASING_MANAGERS_INDEX_FINAL: str = "commbank composite purchasing managers index final"
            """CommBank Composite PMI Final"""

            COMMBANK_COMPOSITE_PURCHASING_MANAGERS_INDEX_FLASH: str = "commbank composite purchasing managers index flash"
            """CommBank Composite PMI Flash"""

            COMMBANK_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "commbank manufacturing purchasing managers index final"
            """CommBank Manufacturing PMI Final"""

            COMMBANK_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "commbank manufacturing purchasing managers index flash"
            """CommBank Manufacturing PMI Flash"""

            COMMBANK_SERVICES_PURCHASING_MANAGERS_INDEX_FINAL: str = "commbank services purchasing managers index final"
            """CommBank Services PMI Final"""

            COMMBANK_SERVICES_PURCHASING_MANAGERS_INDEX_FLASH: str = "commbank services purchasing managers index flash"
            """CommBank Services PMI Flash"""

            COMPANY_GROSS_OPERATING_PROFITS_QO_Q: str = "company gross operating profits qoq"
            """Company Gross Operating Profits (QoQ)"""

            COMPANY_GROSS_PROFITS_QO_Q: str = "company gross profits qoq"
            """Company Gross Profits QoQ"""

            CONSTRUCTION_WORK_DONE: str = "construction work done"
            """Construction Work Done"""

            CONSTRUCTION_WORK_DONE_QO_Q: str = "construction work done qoq"
            """Construction Work Done QoQ"""

            CONSUMER_INFLATION_EXPECTATIONS: str = "consumer inflation expectations"
            """Consumer Inflation Expectation"""

            CONSUMER_PRICE_INDEX: str = "consumer price index"
            """Consumer Price Index"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SATURDAY: str = "easter saturday"
            """Easter Saturday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            EMPLOYMENT_CHANGE: str = "employment change"
            """Employment Change"""

            EMPLOYMENT_CHANGE_SEASONALLY_ADJUSTED: str = "employment change seasonally adjusted"
            """Employment Change s.a."""

            EXPORT_PRICES_QO_Q: str = "export prices qoq"
            """Export Price Index QoQ"""

            EXPORTS_MO_M: str = "exports mom"
            """Exports MoM"""

            EXPORTS_YO_Y: str = "exports yoy"
            """Exports YoY"""

            FAMILY_DAY: str = "family day"
            """Family Day"""

            FEDERAL_ELECTION: str = "federal election"
            """Federal Election"""

            FULL_TIME_EMPLOYMENT_CHANGE: str = "full time employment change"
            """Fulltime Employment"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_CAPITAL_EXPENDITURE: str = "gdp capital expenditure"
            """GDP Capital Expenditure"""

            GDP_CAPITAL_EXPENDITURE_QO_Q: str = "gdp capital expenditure qoq"
            """GDP Capital Expenditure QoQ"""

            GDP_DEFLATOR: str = "gdp deflator"
            """GDP Deflator"""

            GDP_DEFLATOR_QO_Q: str = "gdp deflator qoq"
            """GDP Deflator QoQ"""

            GDP_FINAL_CONSUMPTION: str = "gdp final consumption"
            """GDP Final Consumption"""

            GDP_FINAL_CONSUMPTION_QO_Q: str = "gdp final consumption qoq"
            """GDP Final Consumption QoQ"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            G_TWENTY_MEETING: str = "g20 meeting"
            """G20 Meeting"""

            HIA_NEW_HOME_SALES_MO_M: str = "hia new home sales mom"
            """HIA New Home Sales (MoM)"""

            HOME_LOANS_MO_M: str = "home loans mom"
            """Home Loans MoM"""

            HOUSE_PRICE_INDEX_QO_Q: str = "house price index qoq"
            """House Price Index QoQ"""

            HOUSE_PRICE_INDEX_YO_Y: str = "house price index yoy"
            """House Price Index YoY"""

            IMPORT_PRICES_QO_Q: str = "import prices qoq"
            """Import Price Index QoQ"""

            IMPORTS_MO_M: str = "imports mom"
            """Imports MoM"""

            IMPORTS_YO_Y: str = "imports yoy"
            """Imports YoY"""

            INFLATION_RATE_QO_Q: str = "inflation rate qoq"
            """Inflation Rate QoQ"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INVESTMENT_LENDING_FOR_HOMES: str = "investment lending for homes"
            """Investment Lending for Homes"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            MID_YEAR_ECONOMIC_AND_FISCAL_OUTLOOK: str = "mid year economic and fiscal outlook"
            """Mid-Year Economic and Fiscal Outlook"""

            NAB_BUSINESS_CONFIDENCE: str = "nab business confidence"
            """NAB Business Confidence"""

            NAB_BUSINESS_SURVEY: str = "nab business survey"
            """NAB Business Survey"""

            NEW_MOTOR_VEHICLE_SALES_MO_M: str = "new motor vehicle sales mom"
            """New Motor Vehicle Sales (MoM)"""

            NEW_MOTOR_VEHICLE_SALES_YO_Y: str = "new motor vehicle sales yoy"
            """New Motor Vehicle Sales (YoY)"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_DAY_SUBSTITUTE_DAY: str = "new years day substitute day"
            """New Year's Day (Substitute Day)"""

            PARTICIPATION_RATE: str = "participation rate"
            """Participation Rate"""

            PART_TIME_EMPLOYMENT_CHANGE: str = "part time employment change"
            """Part Time Employment Chg"""

            PRIVATE_CAPITAL_EXPENDITURE_QO_Q: str = "private capital expenditure qoq"
            """Private Capital Expenditure QoQ"""

            PRIVATE_NEW_CAPITAL_EXPENDITURE_QO_Q: str = "private new capital expenditure qoq"
            """Private New Capital Expenditure QoQ"""

            PRIVATE_SECTOR_CREDIT_MO_M: str = "private sector credit mom"
            """Private Sector Credit (MoM)"""

            PRIVATE_SECTOR_CREDIT_YO_Y: str = "private sector credit yoy"
            """Private Sector Credit (YoY)"""

            PRODUCER_PRICE_INDEX_QO_Q: str = "producer price index qoq"
            """Producer Price Index QoQ"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            QUEENS_BIRTHDAY: str = "queens birthday"
            """Queen's Birthday"""

            QUEENS_BIRTHDAY_DAY: str = "queens birthday day"
            """Queen's Birthday Day"""

            RBA_ASSIST_GOV_EDEY_SPEECH: str = "rba assist gov edey speech"
            """RBA Assist Gov Edey Speech"""

            RBA_ASSIST_GOV_KENT_SPEECH: str = "rba assist gov kent speech"
            """RBA Assist Gov Kent Speech"""

            RBA_AYLMER_SPEECH: str = "rba aylmer speech"
            """RBA Aylmer Speech"""

            RBA_BOULTON_SPEECH: str = "rba boulton speech"
            """RBA Boulton Speech"""

            RBA_BULLETIN: str = "rba bulletin"
            """RBA Bulletin"""

            RBA_BULLOCK_SPEECH: str = "rba bullock speech"
            """RBA Bullock Speech"""

            RBA_CHART_PACK: str = "rba chart pack"
            """RBA Chart Pack"""

            RBA_COMMODITY_INDEX_SDR_YO_Y: str = "rba commodity index sdr yoy"
            """RBA Commodity Index SDR (YoY)"""

            RBA_COOMBS_SPEECH: str = "rba coombs speech"
            """RBA Coombs Speech"""

            RBA_DEBELLE_SPEECH: str = "rba debelle speech"
            """RBA Debelle Speech"""

            RBA_DEPUTY_GOV_LOWE_SPEECH: str = "rba deputy gov lowe speech"
            """RBA Deputy Gov Lowe Speech"""

            RBA_EDEY_SPEECH: str = "rba edey speech"
            """RBA Edey Speech"""

            RBA_ELLIS_SPEECH: str = "rba ellis speech"
            """RBA Ellis Speech"""

            RBA_FINANCIAL_STABILITY_REVIEW: str = "rba financial stability review"
            """RBA Financial Stability Review"""

            RBA_GIRN_SPEECH: str = "rba girn speech"
            """RBA Girn Speech"""

            RBA_GOV_DEBELLE_SPEECH: str = "rba gov debelle speech"
            """RBA Gov Debelle Speech"""

            RBA_GOVERNOR_STEVENS_SPEAKS: str = "rba governor stevens speaks"
            """RBA Governor Stevens Speaks"""

            RBA_GOV_GLENN_SPEECH: str = "rba gov glenn speech"
            """RBA Gov Glenn Speech"""

            RBA_GOV_GLENN_STEVENS_SPEECH: str = "rba gov glenn stevens speech"
            """RBA Gov. Glenn Stevens Speech"""

            RBA_GOV_KENT_SPEECH: str = "rba gov kent speech"
            """RBA Gov Kent Speech"""

            RBA_GOV_LOWE_SPEECH: str = "rba gov lowe speech"
            """RBA Gov Lowe Speech"""

            RBA_HEATH_SPEECH: str = "rba heath speech"
            """RBA Heath Speech"""

            RBA_INTEREST_RATE_DECISION: str = "rba interest rate decision"
            """RBA Interest Rate Decision"""

            RBA_KENT_SPEECH: str = "rba kent speech"
            """RBA Kent Speech"""

            RBA_KOHLER_SPEECH: str = "rba kohler speech"
            """RBA Kohler Speech"""

            RBA_LOWE_SPEAKS_BEFORE_PARLIAMENT: str = "rba lowe speaks before parliament"
            """RBA Lowe Speaks before Parliament"""

            RBA_LOWE_SPEECH: str = "rba lowe speech"
            """RBA Lowe Speech"""

            RBA_MEETING_MINUTES: str = "rba meeting minutes"
            """RBA Meeting Minutes"""

            RBA_MEETINGS_MINUTES: str = "rba meetings minutes"
            """RBA Meetings Minutes"""

            RBA_MONETARY_POLICY_STATEMENT: str = "rba monetary policy statement"
            """RBA Monetary Policy Statement"""

            RBA_RATE_STATEMENT: str = "rba rate statement"
            """RBA Rate Statement"""

            RBA_RICHARDS_SPEECH: str = "rba richards speech"
            """RBA Richards Speech"""

            RBA_RYAN_SPEECH: str = "rba ryan speech"
            """RBA Ryan Speech"""

            RBAS_GOVERNOR_GLENN_STEVENS_SPEECH: str = "rbas governor glenn stevens speech"
            """RBA's Governor Glenn Stevens Speech"""

            RBAS_GOV_STEVENS_SPEECH: str = "rbas gov stevens speech"
            """RBA's Gov Stevens Speech"""

            RBA_SIMON_SPEECH: str = "rba simon speech"
            """RBA Simon Speech"""

            RBA_STATEMENT_ON_MONETARY_POLICY: str = "rba statement on monetary policy"
            """RBA Statement on Monetary Policy"""

            RBA_TRIMMED_MEAN_CONSUMER_PRICE_INDEX_QO_Q: str = "rba trimmed mean consumer price index qoq"
            """RBA trimmed mean CPI QoQ"""

            RBA_TRIMMED_MEAN_CONSUMER_PRICE_INDEX_YO_Y: str = "rba trimmed mean consumer price index yoy"
            """RBA trimmed mean CPI YoY"""

            RBA_WEIGHTED_MEAN_CONSUMER_PRICE_INDEX_QO_Q: str = "rba weighted mean consumer price index qoq"
            """RBA Weighted Mean CPI QoQ"""

            RBA_WEIGHTED_MEAN_CONSUMER_PRICE_INDEX_YO_Y: str = "rba weighted mean consumer price index yoy"
            """RBA Weighted Mean CPI YoY"""

            RECONCILIATION_DAY: str = "reconciliation day"
            """Reconciliation Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            STATEMENT_ON_MONETARY_POLICY: str = "statement on monetary policy"
            """Statement on Monetary Policy"""

            TD_MELBOURNE_INSTITUTE_INFLATION_GAUGE_MO_M: str = "td melbourne institute inflation gauge mom"
            """TD-MI Inflation Gauge MoM"""

            TD_SECURITIES_INFLATION_MO_M: str = "td securities inflation mom"
            """TD Securities Inflation MoM"""

            TD_SECURITIES_INFLATION_YO_Y: str = "td securities inflation yoy"
            """TD Securities Inflation (YoY)"""

            TWO_THOUSAND_SEVENTEEN_EIGHTEEN_BUDGET_RELEASE: str = "2017 18 budget release"
            """2017-18 Budget Release"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WAGE_PRICE_INDEX_QO_Q: str = "wage price index qoq"
            """Wage Price Index QoQ"""

            WAGE_PRICE_INDEX_YO_Y: str = "wage price index yoy"
            """Wage Price Index YoY"""

            WESTPAC_CONSUMER_CONFIDENCE: str = "westpac consumer confidence"
            """Westpac Consumer Confidence"""

            WESTPAC_CONSUMER_CONFIDENCE_CHANGE: str = "westpac consumer confidence change"
            """Westpac Cons. Conf. Change"""

            WESTPAC_CONSUMER_CONFIDENCE_MO_M: str = "westpac consumer confidence mom"
            """Westpac Consumer Confidence MoM"""

            WESTPAC_LEADING_INDEX: str = "westpac leading index"
            """Westpac Leading Index"""

            WESTPAC_LEADING_INDEX_MO_M: str = "westpac leading index mom"
            """Westpac Leading Index MoM"""

        class Austria(System.Object):
            """Austria"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saint's Day"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BANK_OF_AUSTRIA_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "bank of austria manufacturing purchasing managers index"
            """Bank Austria Manufacturing PMI"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CORPUS_CHRISTI: str = "corpus christi"
            """Corpus Christi"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            FINANCE_MINISTER_SCHELLING_SPEECH: str = "finance minister schelling speech"
            """Finance Minister Schelling Speech"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            HARMONIZED_INFLATION_RATE_MO_M: str = "harmonized inflation rate mom"
            """Harmonised Inflation Rate MoM"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonised Inflation Rate YoY"""

            IMF_LAGARDE_SPEECH: str = "imf lagarde speech"
            """IMF Lagarde Speech"""

            IMMACULATE_CONCEPTION: str = "immaculate conception"
            """Immaculate Conception"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            OENB_GOV_NOWOTNY_SPEECH: str = "oenb gov nowotny speech"
            """OeNB Gov Nowotny Speech"""

            OPEC_MEETING: str = "opec meeting"
            """OPEC Meeting"""

            PRESIDENTIAL_ELECTION: str = "presidential election"
            """Presidential Election"""

            PRESIDENTIAL_ELECTIONS: str = "presidential elections"
            """Presidential Elections"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            PURCHASING_MANAGERS_INDEX_MANUFACTURING: str = "purchasing managers index manufacturing"
            """PMI Manufacturing"""

            REGIONAL_ELECTIONS: str = "regional elections"
            """Regional Elections"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            UNEMPLOYED_PERSONS: str = "unemployed persons"
            """Unemployed Persons"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WHIT_MONDAY: str = "whit monday"
            """Whit Monday"""

            WHOLESALE_PRICES_MO_M: str = "wholesale prices mom"
            """Wholesale Prices MoM"""

            WHOLESALE_PRICES_NOT_SEASONALLY_ADJUSTED_MO_M: str = "wholesale prices not seasonally adjusted mom"
            """Wholesale Prices n.s.a (MoM)"""

            WHOLESALE_PRICES_NOT_SEASONALLY_ADJUSTED_YO_Y: str = "wholesale prices not seasonally adjusted yoy"
            """Wholesale Prices n.s.a (YoY)"""

            WHOLESALE_PRICES_YO_Y: str = "wholesale prices yoy"
            """Wholesale Prices YoY"""

        class Belgium(System.Object):
            """Belgium"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saints' Day"""

            ARMISTICE_DAY: str = "armistice day"
            """Armistice Day"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EU_CHINA_SUMMIT: str = "eu china summit"
            """EU-China Summit"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_ADV: str = "gdp growth rate qoq adv"
            """GDP Growth Rate QoQ Adv"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_ADV: str = "gdp growth rate yoy adv"
            """GDP Growth Rate YoY Adv"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LOCAL_ELECTIONS: str = "local elections"
            """Local Elections"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NATO_SUMMIT: str = "nato summit"
            """NATO Summit"""

            NBB_BUSINESS_CLIMATE: str = "nbb business climate"
            """NBB Business Climate"""

            NBB_BUSINESS_CONFIDENCE: str = "nbb business confidence"
            """NBB Business Confidence"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year’s Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WHIT_MONDAY: str = "whit monday"
            """Whit Monday"""

        class Canada(System.Object):
            """Canada"""

            ADP_EMPLOYMENT_CHANGE: str = "adp employment change"
            """ADP Employment Change"""

            ALBERTA_GENERAL_ELECTION: str = "alberta general election"
            """Alberta General Election"""

            AVERAGE_HOURLY_WAGES_YO_Y: str = "average hourly wages yoy"
            """Average Hourly Wages YoY"""

            AVERAGE_WEEKLY_EARNINGS_YO_Y: str = "average weekly earnings yoy"
            """Average Weekly Earnings YoY"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BANK_OF_CANADA_BEAUDRY_SPEECH: str = "bank of canada beaudry speech"
            """BoC Beaudry Speech"""

            BANK_OF_CANADA_BUSINESS_OUTLOOK_SURVEY: str = "bank of canada business outlook survey"
            """Bank of Canada Business Outlook Survey"""

            BANK_OF_CANADA_CONSUMER_PRICE_INDEX_CORE_MO_M: str = "bank of canada consumer price index core mom"
            """Bank of Canada Consumer Price Index Core MoM"""

            BANK_OF_CANADA_CONSUMER_PRICE_INDEX_CORE_YO_Y: str = "bank of canada consumer price index core yoy"
            """Bank of Canada Consumer Price Index Core YoY"""

            BANK_OF_CANADA_CORE_INFLATION_MO_M: str = "bank of canada core inflation mom"
            """Bank of Canada Core Inflation MoM"""

            BANK_OF_CANADA_CORE_INFLATION_YO_Y: str = "bank of canada core inflation yoy"
            """Bank of Canada Core Inflation YoY"""

            BANK_OF_CANADA_DEPUTY_GOV_PATTERSON_SPEECH: str = "bank of canada deputy gov patterson speech"
            """BoC Deputy Gov Patterson Speech"""

            BANK_OF_CANADA_DEPUTY_GOV_SCHEMBRI_SPEECH: str = "bank of canada deputy gov schembri speech"
            """BoC Deputy Gov Schembri Speech"""

            BANK_OF_CANADA_DEPUTY_GOV_WILKINS_SPEECH: str = "bank of canada deputy gov wilkins speech"
            """BoC Deputy Gov Wilkins Speech"""

            BANK_OF_CANADA_FINANCIAL_SYSTEM_REVIEW: str = "bank of canada financial system review"
            """BoC Financial System Review"""

            BANK_OF_CANADA_GOV_CARNEY_SPEAKS: str = "bank of canada gov carney speaks"
            """BoC Gov Carney Speaks"""

            BANK_OF_CANADA_GOV_POLOZ_PRESS_CONFERENCE: str = "bank of canada gov poloz press conference"
            """BoC Gov Poloz Press Conference"""

            BANK_OF_CANADA_GOV_POLOZ_SPEAKS: str = "bank of canada gov poloz speaks"
            """BoC Gov Poloz Speaks"""

            BANK_OF_CANADA_GOV_POLOZ_SPEECH: str = "bank of canada gov poloz speech"
            """BoC Gov Poloz Speech"""

            BANK_OF_CANADA_GRAVELLE_SPEECH: str = "bank of canada gravelle speech"
            """BoC Gravelle Speech"""

            BANK_OF_CANADA_INTEREST_RATE_DECISION: str = "bank of canada interest rate decision"
            """BoC Interest Rate Decision"""

            BANK_OF_CANADA_LANE_SPEECH: str = "bank of canada lane speech"
            """BoC Lane Speech"""

            BANK_OF_CANADA_LEDUC_SPEECH: str = "bank of canada leduc speech"
            """BoC Leduc Speech"""

            BANK_OF_CANADA_MONETARY_POLICY_REPORT: str = "bank of canada monetary policy report"
            """BoC Monetary Policy Report"""

            BANK_OF_CANADA_PATTERSON_SPEECH: str = "bank of canada patterson speech"
            """BoC Patterson Speech"""

            BANK_OF_CANADA_PRESS_CONFERENCE: str = "bank of canada press conference"
            """BoC Press Conference"""

            BANK_OF_CANADA_RATE_STATEMENT: str = "bank of canada rate statement"
            """BoC Rate Statement"""

            BANK_OF_CANADA_REVIEW: str = "bank of canada review"
            """BoC Review"""

            BANK_OF_CANADA_SCHEMBRI_SPEECH: str = "bank of canada schembri speech"
            """BoC Schembri Speech"""

            BANK_OF_CANADA_WILKINS_SPEECH: str = "bank of canada wilkins speech"
            """BoC Wilkins Speech"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUDGET_BALANCE: str = "budget balance"
            """Budget Balance"""

            BUILDING_PERMITS_MO_M: str = "building permits mom"
            """Building Permits (MoM)"""

            CANADA_DAY: str = "canada day"
            """Canada Day"""

            CANADA_DAY_SUBSTITUTE_DAY: str = "canada day substitute day"
            """Canada Day (Substitute Day)"""

            CANADIAN_INVESTMENT_IN_FOREIGN_SECURITIES: str = "canadian investment in foreign securities"
            """Canadian portfolio investment in foreign securities"""

            CAPACITY_UTILIZATION: str = "capacity utilization"
            """Capacity Utilization"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CIVIC_HOLIDAY: str = "civic holiday"
            """Civic Holiday"""

            CONSUMER_PRICE_INDEX_CORE_MO_M: str = "consumer price index core mom"
            """Consumer Price Index - Core MoM"""

            CORE_CONSUMER_PRICE_INDEX_YO_Y: str = "core consumer price index yoy"
            """Core CPI YoY"""

            CORE_INFLATION_RATE_MO_M: str = "core inflation rate mom"
            """Core Inflation Rate MoM"""

            CORE_INFLATION_RATE_YO_Y: str = "core inflation rate yoy"
            """Core Inflation Rate YoY"""

            CORE_RETAIL_SALES_MO_M: str = "core retail sales mom"
            """Core Retail Sales MoM"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EMPLOYMENT_CHANGE: str = "employment change"
            """Employment Change"""

            EXPORTS: str = "exports"
            """Exports"""

            FAMILY_DAY: str = "family day"
            """Family Day"""

            FEDERAL_ELECTION: str = "federal election"
            """Federal Election"""

            FINANCE_MINISTER_MORNEAU_SPEECH: str = "finance minister morneau speech"
            """Finance Minister Morneau Speech"""

            FOREIGN_INVESTMENT_IN_CANADIAN_SECURITIES: str = "foreign investment in canadian securities"
            """Foreign portfolio investment in Canadian securities"""

            FOREIGN_SECURITIES_PURCHASES: str = "foreign securities purchases"
            """Foreign Securities Purchases"""

            FOREIGN_SECURITIES_PURCHASES_BY_CANADIANS: str = "foreign securities purchases by canadians"
            """Foreign Securities Purchases by Canadians"""

            FULL_EMPLOYMENT_CHANGE: str = "full employment change"
            """Full Employment Change"""

            FULL_TIME_EMPLOYMENT_CHANGE: str = "full time employment change"
            """Full Time Employment Chg"""

            GDP_GROWTH_RATE_ANNUALIZED: str = "gdp growth rate annualized"
            """GDP Growth Rate Annualized"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_IMPLICIT_PRICE_QO_Q: str = "gdp implicit price qoq"
            """GDP Implicit Price QoQ"""

            GDP_MO_M: str = "gdp mom"
            """GDP MoM"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            GROSS_DOMESTIC_PRODUCT_MO_M: str = "gross domestic product mom"
            """Gross Domestic Product (MoM)"""

            G_SEVEN_SUMMIT: str = "g7 summit"
            """G7 Summit"""

            HOUSING_STARTS: str = "housing starts"
            """Housing Starts"""

            HOUSING_STARTS_SEASONALLY_ADJUSTED_YO_Y: str = "housing starts seasonally adjusted yoy"
            """Housing Starts s.a YoY"""

            HOUSING_STARTS_YO_Y: str = "housing starts yoy"
            """Housing Starts YoY"""

            IMPORTS: str = "imports"
            """Imports"""

            INDUSTRIAL_PRODUCT_PRICE_MO_M: str = "industrial product price mom"
            """Industrial Product Price MoM"""

            INDUSTRIAL_PRODUCT_PRICE_YO_Y: str = "industrial product price yoy"
            """Industrial Product Price YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INVESTMENT_IN_FOREIGN_SECURITIES: str = "investment in foreign securities"
            """Portfolio investment in foreign securities"""

            IVEY_PURCHASING_MANAGERS_INDEX_SEASONALLY_ADJUSTED: str = "ivey purchasing managers index seasonally adjusted"
            """Ivey PMI s.a"""

            JOB_VACANCIES: str = "job vacancies"
            """Job Vacancies"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LABOR_PRODUCTIVITY_QO_Q: str = "labor productivity qoq"
            """Labor Productivity QoQ"""

            MANUFACTURING_SALES_MO_M: str = "manufacturing sales mom"
            """Manufacturing Sales MoM"""

            MANUFACTURING_SALES_YO_Y: str = "manufacturing sales yoy"
            """Manufacturing Sales YoY"""

            MANUFACTURING_SHIPMENTS_MO_M: str = "manufacturing shipments mom"
            """Manufacturing Shipments MoM"""

            MANUFACTURING_SHIPMENTS_YO_Y: str = "manufacturing shipments yoy"
            """Manufacturing Shipments YoY"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit manufacturing purchasing managers index"
            """Markit Manufacturing PMI"""

            NET_CHANGE_IN_EMPLOYMENT: str = "net change in employment"
            """Net Change in Employment"""

            NEW_BRUNSWICK_PROVINCIAL_ELECTIONS: str = "new brunswick provincial elections"
            """New Brunswick Provincial Elections"""

            NEW_HOUSING_PRICE_INDEX_MO_M: str = "new housing price index mom"
            """New Housing Price Index (MoM)"""

            NEW_HOUSING_PRICE_INDEX_YO_Y: str = "new housing price index yoy"
            """New Housing Price Index (YoY)"""

            NEW_MOTOR_VEHICLE_SALES: str = "new motor vehicle sales"
            """New Motor Vehicle Sales"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_DAY_SUBSTITUTE_DAY: str = "new years day substitute day"
            """New Year's Day (Substitute Day)"""

            ONTARIO_PROVINCIAL_ELECTIONS: str = "ontario provincial elections"
            """Ontario Provincial Elections"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PARTICIPATION_RATE: str = "participation rate"
            """Participation rate"""

            PART_TIME_EMPLOYMENT_CHANGE: str = "part time employment change"
            """Part Time Employment Chg"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            QUEBEC_PROVINCIAL_ELECTIONS: str = "quebec provincial elections"
            """Quebec Provincial Elections"""

            RAW_MATERIALS_PRICE_INDEX_MO_M: str = "raw materials price index mom"
            """Raw Materials Price Index MoM"""

            RAW_MATERIALS_PRICE_INDEX_YO_Y: str = "raw materials price index yoy"
            """Raw Materials Price Index YoY"""

            RBC_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "rbc manufacturing purchasing managers index"
            """RBC Manufacturing PMI"""

            REMEMBRANCE_DAY: str = "remembrance day"
            """Remembrance Day"""

            RETAIL_SALES_EXCLUDING_AUTOS_MO_M: str = "retail sales excluding autos mom"
            """Retail Sales Ex Autos MoM"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            STOCK_INVESTMENT_BY_FOREIGNERS: str = "stock investment by foreigners"
            """Stock Investment by Foreigners"""

            THANKSGIVING_DAY: str = "thanksgiving day"
            """Thanksgiving Day"""

            TWO_THOUSAND_SIXTEEN_BUDGET_ANNOUNCEMENT: str = "2016 budget announcement"
            """2016 Budget Announcement"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            VICTORIA_DAY: str = "victoria day"
            """Victoria Day"""

            WHOLESALE_SALES_MO_M: str = "wholesale sales mom"
            """Wholesale Sales MoM"""

            WHOLESALE_SALES_YO_Y: str = "wholesale sales yoy"
            """Wholesale Sales YoY"""

        class China(System.Object):
            """China"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BELT_AND_ROAD_FORUM: str = "belt and road forum"
            """Belt and Road Forum"""

            CAIXIN_COMPOSITE_PURCHASING_MANAGERS_INDEX: str = "caixin composite purchasing managers index"
            """Caixin Composite PMI"""

            CAIXIN_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "caixin manufacturing purchasing managers index"
            """Caixin Manufacturing PMI"""

            CAIXIN_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "caixin manufacturing purchasing managers index final"
            """Caixin Manufacturing PMI Final"""

            CAIXIN_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "caixin manufacturing purchasing managers index flash"
            """Caixin Manufacturing PMI Flash"""

            CAIXIN_SERVICES_PURCHASING_MANAGERS_INDEX: str = "caixin services purchasing managers index"
            """Caixin Services PMI"""

            CAPITAL_FLOWS: str = "capital flows"
            """Capital Flows"""

            CB_LEADING_ECONOMIC_INDEX: str = "cb leading economic index"
            """CB Leading Economic Index"""

            CENTRAL_ECONOMIC_WORK_CONFERENCE: str = "central economic work conference"
            """Central Economic Work Conference"""

            CHINESE_NEW_YEAR: str = "chinese new year"
            """Chinese New Year"""

            CHINESE_PEOPLES_POLITICAL_CONSULTATIVE_CONFERENCE: str = "chinese peoples political consultative conference"
            """Chinese People’s Political Consultative Conference"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DRAGON_BOAT_FESTIVAL: str = "dragon boat festival"
            """Dragon Boat Festival"""

            EU_CHINA_SUMMIT: str = "eu china summit"
            """EU-China Summit"""

            EXPORTS: str = "exports"
            """Exports"""

            EXPORTS_YO_Y: str = "exports yoy"
            """Exports YoY"""

            FIRST_DAY_NATIONAL_PEOPLES_CONGRESS: str = "first day national peoples congress"
            """1st Day National People's Congress"""

            FIXED_ASSET_INVESTMENT_YTD_YO_Y: str = "fixed asset investment ytd yoy"
            """Fixed Asset Investment (YTD) YoY"""

            FOREIGN_DIRECT_INVESTMENT_YTD_YO_Y: str = "foreign direct investment ytd yoy"
            """FDI (YTD) YoY"""

            FOREIGN_EXCHANGE_RESERVES: str = "foreign exchange reserves"
            """Foreign Exchange Reserves"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            G_TWENTY_FIN_MINISTERS_AND_CB_GOVERNORS_MEETING: str = "g20 fin ministers and cb governors meeting"
            """G20 Fin Ministers and CB Governors Meeting"""

            G_TWENTY_MEETING: str = "g20 meeting"
            """G20 Meeting"""

            HOUSE_PRICE_INDEX_MO_M: str = "house price index mom"
            """House Price Index MoM"""

            HOUSE_PRICE_INDEX_YO_Y: str = "house price index yoy"
            """House Price Index YoY"""

            HSBC_CHINA_SERVICES_PURCHASING_MANAGERS_INDEX: str = "hsbc china services purchasing managers index"
            """HSBC China Services PMI"""

            HSBC_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "hsbc manufacturing purchasing managers index"
            """HSBC Manufacturing PMI"""

            HSBC_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "hsbc manufacturing purchasing managers index final"
            """HSBC Manufacturing PMI Final"""

            HSBC_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "hsbc manufacturing purchasing managers index flash"
            """HSBC Manufacturing PMI Flash"""

            HSBC_MANUFACTURING_PURCHASING_MANAGERS_INDEX_PRELIMINARY: str = "hsbc manufacturing purchasing managers index preliminary"
            """HSBC Manufacturing PMI Prel."""

            HSBC_SERVICES_PURCHASING_MANAGERS_INDEX: str = "hsbc services purchasing managers index"
            """HSBC Services PMI"""

            IMPORTS: str = "imports"
            """Imports"""

            IMPORTS_YO_Y: str = "imports yoy"
            """Imports YoY"""

            INDUSTRIAL_CAPACITY_UTILIZATION: str = "industrial capacity utilization"
            """Industrial Capacity Capacity Utilization"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INDUSTRIAL_PROFITS_YTD_YO_Y: str = "industrial profits ytd yoy"
            """Industrial Profits (YTD) YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INTEREST_RATE_DECISION: str = "interest rate decision"
            """Interest Rate Decision"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LOAN_PRIME_RATE_FIVE_YEAR: str = "loan prime rate 5y"
            """Loan Prime Rate 5Y"""

            LOAN_PRIME_RATE_ONE_YEAR: str = "loan prime rate 1y"
            """Loan Prime Rate 1Y"""

            MID_AUTUMN_FESTIVAL: str = "mid autumn festival"
            """Mid-Autumn Festival"""

            MID_AUTUMN_HOLIDAY: str = "mid autumn holiday"
            """Mid-Autumn Holiday"""

            MNI_BUSINESS_SENTIMENT: str = "mni business sentiment"
            """MNI Business Sentiment"""

            M_TWO_MONEY_SUPPLY_YO_Y: str = "m2 money supply yoy"
            """M2 Money Supply YoY"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NATIONAL_PEOPLES_CONGRESS: str = "national peoples congress"
            """National People’s Congress"""

            NBS_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "nbs manufacturing purchasing managers index"
            """NBS Manufacturing PMI"""

            NBS_PRESS_CONFERENCE: str = "nbs press conference"
            """NBS Press Conference"""

            NEW_LOANS: str = "new loans"
            """New Loans"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YUAN_LOANS: str = "new yuan loans"
            """New Yuan Loans"""

            NON_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "non manufacturing purchasing managers index"
            """Non Manufacturing PMI"""

            OUTSTANDING_LOAN_GROWTH_YO_Y: str = "outstanding loan growth yoy"
            """Outstanding Loan Growth YoY"""

            PRESIDENT_JINPING_SPEECH_AT_BOAO_FORUM: str = "president jinping speech at boao forum"
            """President Jinping Speech at Boao Forum"""

            PRESIDENT_XI_JINPING_SPEECH: str = "president xi jinping speech"
            """President Xi Jinping Speech"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            QING_MING_JIE: str = "qing ming jie"
            """Qing Ming Jie"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            TOTAL_SOCIAL_FINANCING: str = "total social financing"
            """Total Social Financing"""

            URBAN_INVESTMENT_YO_Y: str = "urban investment yoy"
            """Urban Investment YoY"""

            URBAN_INVESTMENT_YTD: str = "urban investment ytd"
            """Urban Investment YTD"""

            URBAN_INVESTMENT_YTD_YO_Y: str = "urban investment ytd yoy"
            """Urban investment (YTD) (YoY)"""

            US_CHINA_TRADE_TALKS: str = "us china trade talks"
            """US-China Trade Talks"""

            VEHICLE_SALES_YO_Y: str = "vehicle sales yoy"
            """Vehicle Sales YoY"""

            VICTORY_DAY: str = "victory day"
            """Victory Day"""

            WESTPAC_MNI_CONSUMER_SENTIMENT: str = "westpac mni consumer sentiment"
            """Westpac MNI Consumer Sentiment Indicator"""

        class Cyprus(System.Object):
            """Cyprus"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CATHOLIC_CHRISTMAS_DAY: str = "catholic christmas day"
            """Catholic Christmas Day"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CLEAN_MONDAY: str = "clean monday"
            """Clean Monday"""

            CONSTRUCTION_OUTPUT_YO_Y: str = "construction output yoy"
            """Construction Output YoY"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_GROWTH_RATE_FINAL: str = "gdp growth rate final"
            """GDP Growth Rate - Final"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GREEK_INDEPENDENCE_DAY: str = "greek independence day"
            """Greek Independence Day"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonised Inflation Rate YoY"""

            INDEPENDENCE_DAY: str = "independence day"
            """Independence Day"""

            INDUSTRIAL_PRODUCTION: str = "industrial production"
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            OCHI_DAY: str = "ochi day"
            """Ochi Day"""

            ORTHODOX_EASTER_MONDAY: str = "orthodox easter monday"
            """Orthodox Easter Monday"""

            ORTHODOX_EASTER_SUNDAY: str = "orthodox easter sunday"
            """Orthodox Easter Sunday"""

            ORTHODOX_EASTER_TUESDAY: str = "orthodox easter tuesday"
            """Orthodox Easter Tuesday"""

            ORTHODOX_GOOD_FRIDAY: str = "orthodox good friday"
            """Orthodox Good Friday"""

            ORTHODOX_WHIT_MONDAY: str = "orthodox whit monday"
            """Orthodox Whit Monday"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PARLIAMENT_VOTE_ON_DEPOSIT_LEVY_FOR_BAILOUT_PLAN: str = "parliament vote on deposit levy for bailout plan"
            """Parliament Vote on Deposit Levy for Bailout Plan"""

            PRESIDENTIAL_ELECTION: str = "presidential election"
            """Presidential Election"""

            PRESIDENTIAL_ELECTION_ROUND_TWO: str = "presidential election round 2"
            """Presidential Election Round 2"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WAGE_GROWTH_YO_Y: str = "wage growth yoy"
            """Wage Growth YoY"""

        class Estonia(System.Object):
            """Estonia"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            EESTI_PANK_ECONOMIC_FORECAST: str = "eesti pank economic forecast"
            """Eesti Pank Economic Forecast"""

            EESTI_PANK_GOV_HANSSON_SPEECH: str = "eesti pank gov hansson speech"
            """Eesti Pank Gov Hansson Speech"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ Second Estimate"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            IMPORTS: str = "imports"
            """Imports"""

            INDEPENDENCE_DAY: str = "independence day"
            """Independence Day"""

            INDEPENDENCE_RESTORATION_DAY: str = "independence restoration day"
            """Independence Restoration Day"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            MIDSUMMER_DAY: str = "midsummer day"
            """Midsummer Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PENTECOST: str = "pentecost"
            """Pentecost"""

            PRESIDENTIAL_ELECTIONS: str = "presidential elections"
            """Presidential Elections"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SPRING_DAY: str = "spring day"
            """Spring Day"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            VICTORY_DAY: str = "victory day"
            """Victory Day"""

        class Finland(System.Object):
            """Finland"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saints' Day"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOF_GOV_LIIKANEN_SPEECH: str = "bof gov liikanen speech"
            """BoF Gov Liikanen Speech"""

            BOF_LIIKANEN_SPEECH: str = "bof liikanen speech"
            """BoF Liikanen Speech"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            EPIPHANY_DAY: str = "epiphany day"
            """Epiphany Day"""

            EXPORT_PRICES_YO_Y: str = "export prices yoy"
            """Export Prices YoY"""

            GDP_GROWTH_RATE: str = "gdp growth rate"
            """GDP Growth Rate"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ - Flash"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_YO_Y: str = "gdp yoy"
            """GDP YoY"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            IMPORT_PRICES: str = "import prices"
            """Import Prices"""

            IMPORT_PRICES_YO_Y: str = "import prices yoy"
            """Import Prices YoY"""

            INDEPENDENCE_DAY: str = "independence day"
            """Independence Day"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            MIDSUMMER_DAY: str = "midsummer day"
            """Midsummer Day"""

            MIDSUMMER_EVE: str = "midsummer eve"
            """Midsummer Eve"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PENTECOST: str = "pentecost"
            """Pentecost"""

            PRESIDENTIAL_ELECTION: str = "presidential election"
            """Presidential Election"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            VAPPU_MAY_DAY: str = "vappu may day"
            """Vappu (May Day)"""

        class France(System.Object):
            """France"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saints' Day"""

            ARMISTICE_DAY: str = "armistice day"
            """Armistice Day"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BASTILLE_DAY: str = "bastille day"
            """Bastille Day"""

            BUDGET_BALANCE: str = "budget balance"
            """Budget balance"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CONSUMER_SPENDING_MO_M: str = "consumer spending mom"
            """Consumer Spending MoM"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            FINANCE_SUMMIT_TWO_THOUSAND_NINETEEN: str = "finance summit 2019"
            """Finance Summit 2019"""

            FIVE_YEAR_BTAN_AUCTION: str = "5 year btan auction"
            """5-Year BTAN Auction"""

            FOUR_YEAR_BTAN_AUCTION: str = "4 year btan auction"
            """4-Year BTAN Auction"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FIRST_ESTIMATE: str = "gdp growth rate qoq first estimate"
            """GDP Growth Rate QoQ 1st Est"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FIRST_ESTIMATE: str = "gdp growth rate yoy first estimate"
            """GDP Growth Rate YoY 1st Est"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            G_SEVEN_FINANCE_MINISTERS_AND_CENTRAL_BANK_GOVERNORS_MEETING: str = "g7 finance ministers and central bank governors meeting"
            """G7 Finance Ministers and Central Bank Governors Meeting"""

            G_SEVEN_SUMMIT: str = "g7 summit"
            """G7 Summit"""

            HARMONIZED_INFLATION_RATE_MO_M: str = "harmonized inflation rate mom"
            """Harmonised Inflation Rate MoM"""

            HARMONIZED_INFLATION_RATE_MO_M_FINAL: str = "harmonized inflation rate mom final"
            """Harmonised Inflation Rate MoM Final"""

            HARMONIZED_INFLATION_RATE_MO_M_PRELIMINARY: str = "harmonized inflation rate mom preliminary"
            """Harmonised Inflation Rate MoM Prel"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonised Inflation Rate YoY"""

            HARMONIZED_INFLATION_RATE_YO_Y_FINAL: str = "harmonized inflation rate yoy final"
            """Harmonised Inflation Rate YoY Final"""

            HARMONIZED_INFLATION_RATE_YO_Y_PRELIMINARY: str = "harmonized inflation rate yoy preliminary"
            """Harmonised Inflation Rate YoY Prel"""

            HOUSEHOLD_CONSUMPTION_MO_M: str = "household consumption mom"
            """Household Consumption MoM"""

            IEA_OIL_MARKET_REPORT: str = "iea oil market report"
            """IEA Oil Market Report"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_MO_M_FINAL: str = "inflation rate mom final"
            """Inflation Rate MoM Final"""

            INFLATION_RATE_MO_M_PRELIMINARY: str = "inflation rate mom preliminary"
            """Inflation Rate MoM Prel"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INFLATION_RATE_YO_Y_FINAL: str = "inflation rate yoy final"
            """Inflation Rate YoY Final"""

            INFLATION_RATE_YO_Y_PRELIMINARY: str = "inflation rate yoy preliminary"
            """Inflation Rate YoY Prel"""

            JOBSEEKERS_TOTAL: str = "jobseekers total"
            """Jobseekers Total"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "manufacturing purchasing managers index"
            """Manufacturing PMI"""

            MARKIT_COMPOSITE_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit composite purchasing managers index final"
            """Markit Composite PMI Final"""

            MARKIT_COMPOSITE_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit composite purchasing managers index flash"
            """Markit Composite PMI Flash"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit manufacturing purchasing managers index"
            """Markit Manufacturing PMI"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit manufacturing purchasing managers index final"
            """Markit Manufacturing Pmi Final"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit manufacturing purchasing managers index flash"
            """Markit Manufacturing PMI Flash"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit services purchasing managers index"
            """Markit Services PMI"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit services purchasing managers index final"
            """Markit Services PMI Final"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit services purchasing managers index flash"
            """Markit Services PMI Flash"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NON_FARM_PAYROLLS_QO_Q: str = "non farm payrolls qoq"
            """Nonfarm Payrolls QoQ"""

            NON_FARM_PAYROLLS_QO_Q_FINAL: str = "non farm payrolls qoq final"
            """Non Farm Payrolls QoQ Final"""

            NON_FARM_PAYROLLS_QO_Q_PRELIMINARY: str = "non farm payrolls qoq preliminary"
            """Non Farm Payrolls QoQ Prel"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PENTECOST: str = "pentecost"
            """Pentecost"""

            PRESIDENTIAL_ELECTIONS: str = "presidential elections"
            """Presidential Elections"""

            PRIVATE_NON_FARM_PAYROLLS_QO_Q_FINAL: str = "private non farm payrolls qoq final"
            """Private Non Farm Payrolls QoQ Final"""

            PRIVATE_NON_FARM_PAYROLLS_QO_Q_PRELIMINARY: str = "private non farm payrolls qoq preliminary"
            """Private Non Farm Payrolls QoQ Prel"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SERVICES_PURCHASING_MANAGERS_INDEX: str = "services purchasing managers index"
            """Services PMI"""

            SIX_MONTH_BTF_AUCTION: str = "6 month btf auction"
            """6-Month BTF Auction"""

            TEN_YEAR_OAT_AUCTION: str = "10 year oat auction"
            """10-Year OAT Auction"""

            THREE_MONTH_BTF_AUCTION: str = "3 month btf auction"
            """3-Month BTF Auction"""

            THREE_YEAR_BTAN_AUCTION: str = "3 year btan auction"
            """3-Year BTAN Auction"""

            TWELVE_MONTH_BTF_AUCTION: str = "12 month btf auction"
            """12-Month BTF Auction"""

            TWO_YEAR_BTAN_AUCTION: str = "2 year btan auction"
            """2-Year BTAN Auction"""

            UNEMPLOYMENT_BENEFIT_CLAIMS: str = "unemployment benefit claims"
            """Unemployment Benefit Claims"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WHIT_MONDAY: str = "whit monday"
            """Whit Monday"""

            WWII_VICTORY_DAY: str = "wwii victory day"
            """WWII Victory Day"""

        class Germany(System.Object):
            """Germany"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saints' Day"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            ASIAN_DEVELOPMENT_BANK_ANNUAL_MEETING: str = "asian development bank annual meeting"
            """Asian Development Bank Annual Meeting"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BADEN_WRTTEMBERG_STATE_ELECTION: str = "baden wrttemberg state election"
            """Baden-Württemberg State Election"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BALANCE_OF_TRADE_SEASONALLY_ADJUSTED: str = "balance of trade seasonally adjusted"
            """Balance of Trade s.a"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUNDESBANK_ANNUAL_REPORT: str = "bundesbank annual report"
            """Bundesbank Annual Report"""

            BUNDESBANK_ANNUAL_REPORT_TWO_THOUSAND_SEVENTEEN: str = "bundesbank annual report 2017"
            """Bundesbank Annual Report 2017"""

            BUNDESBANK_BALZ_SPEECH: str = "bundesbank balz speech"
            """Bundesbank Balz Speech"""

            BUNDESBANK_BEERMANN_SPEECH: str = "bundesbank beermann speech"
            """Bundesbank Beermann Speech"""

            BUNDESBANK_BUCH_SPEECH: str = "bundesbank buch speech"
            """Bundesbank Buch Speech"""

            BUNDESBANK_DOMBRET_SPEECH: str = "bundesbank dombret speech"
            """Bundesbank Dombret Speech"""

            BUNDESBANK_MAUDERER_SPEECH: str = "bundesbank mauderer speech"
            """Bundesbank Mauderer Speech"""

            BUNDESBANK_MONTHLY_REPORT: str = "bundesbank monthly report"
            """Bundesbank Monthly Report"""

            BUNDESBANK_PRESIDENT_WEIDMANN_SPEECH: str = "bundesbank president weidmann speech"
            """Bundesbank President Weidmann Speech"""

            BUNDESBANK_SEMI_ANNUAL_FORECASTS: str = "bundesbank semi annual forecasts"
            """Bundesbank Semi-Annual Forecasts"""

            BUNDESBANK_THIELE_SPEECH: str = "bundesbank thiele speech"
            """Bundesbank Thiele Speech"""

            BUNDESBANK_WEIDMANN_SPEECH: str = "bundesbank weidmann speech"
            """Bundesbank Weidmann Speech"""

            BUNDESBANK_WUERMELING_SPEECH: str = "bundesbank wuermeling speech"
            """Bundesbank Wuermeling Speech"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSTRUCTION_PURCHASING_MANAGERS_INDEX: str = "construction purchasing managers index"
            """Construction PMI"""

            CORPUS_CHRISTI: str = "corpus christi"
            """Corpus Christi"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DAY_OF_GERMAN_UNITY: str = "day of german unity"
            """Day of German Unity"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EMPLOYED_PERSONS: str = "employed persons"
            """Employed Persons"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            EURO_FINANCE_WEEK: str = "euro finance week"
            """Euro Finance Week"""

            EURO_FINANCE_WEEK_TWO_THOUSAND_SEVENTEEN: str = "euro finance week 2017"
            """Euro Finance Week 2017"""

            EXPORTS_MO_M: str = "exports mom"
            """Exports MoM"""

            EXPORTS_MO_M_SEASONALLY_ADJUSTED: str = "exports mom seasonally adjusted"
            """Exports MoM s.a"""

            FACTORY_ORDERS_MO_M: str = "factory orders mom"
            """Factory Orders MoM"""

            FACTORY_ORDERS_YO_Y: str = "factory orders yoy"
            """Factory Orders YoY"""

            FEDERAL_ELECTION: str = "federal election"
            """Federal election"""

            FINANCE_MINISTER_SCHUBLE_SPEECH: str = "finance minister schuble speech"
            """Finance Minister Schäuble Speech"""

            FIVE_YEAR_BOBL_AUCTION: str = "5 year bobl auction"
            """5-Year Bobl Auction"""

            FRANKFURT_FINANCE_SUMMIT_TWO_THOUSAND_SEVENTEEN: str = "frankfurt finance summit 2017"
            """Frankfurt Finance Summit 2017"""

            FRANKFURT_FINANCE_SUMMIT_TWO_THOUSAND_SIXTEEN: str = "frankfurt finance summit 2016"
            """Frankfurt Finance Summit 2016"""

            FULL_YEAR_GDP_GROWTH: str = "full year gdp growth"
            """Full Year GDP Growth"""

            GDP_GROWTH_RATE: str = "gdp growth rate"
            """GDP Growth Rate"""

            GDP_GROWTH_RATE_FLASH: str = "gdp growth rate flash"
            """GDP Growth Rate 2015 Flash"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GERMAN_BUBA_PRESIDENT_WEIDMANN_SPEECH: str = "german buba president weidmann speech"
            """German Buba President Weidmann speech"""

            GFK_CONSUMER_CONFIDENCE: str = "gfk consumer confidence"
            """Gfk Consumer Confidence"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            GOVERNMENT_BUDGET: str = "government budget"
            """Government Budget"""

            G_SEVEN_FINANCE_MINISTERS_MEETING: str = "g7 finance ministers meeting"
            """G7 Finance Ministers' Meeting"""

            G_TWENTY_CONFERENCE: str = "g20 conference"
            """G20-Conference"""

            G_TWENTY_FINANCE_MINISTERS_AND_CB_GOVERNORS_MEETING: str = "g20 finance ministers and cb governors meeting"
            """G20 Finance Ministers and CB Governors Meeting"""

            G_TWENTY_FOREIGN_MINISTERS_MEETING: str = "g20 foreign ministers meeting"
            """G20 Foreign Ministers Meeting"""

            G_TWENTY_SUMMIT: str = "g20 summit"
            """G20 Summit"""

            HARMONIZED_INFLATION_RATE_MO_M: str = "harmonized inflation rate mom"
            """Harmonised Inflation Rate MoM"""

            HARMONIZED_INFLATION_RATE_MO_M_FINAL: str = "harmonized inflation rate mom final"
            """Harmonised Inflation Rate MoM Final"""

            HARMONIZED_INFLATION_RATE_MO_M_PRELIMINARY: str = "harmonized inflation rate mom preliminary"
            """Harmonised Inflation Rate MoM Prel"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonised Inflation Rate YoY"""

            HARMONIZED_INFLATION_RATE_YO_Y_FINAL: str = "harmonized inflation rate yoy final"
            """Harmonised Inflation Rate YoY Final"""

            HARMONIZED_INFLATION_RATE_YO_Y_PRELIMINARY: str = "harmonized inflation rate yoy preliminary"
            """Harmonised Inflation Rate YoY Prel"""

            IFO_BUSINESS_CLIMATE: str = "ifo business climate"
            """IFO Business Climate"""

            IFO_CURRENT_ASSESSMENT: str = "ifo current assessment"
            """IFO - Current Assessment"""

            IFO_CURRENT_CONDITIONS: str = "ifo current conditions"
            """IFO Current Conditions"""

            IFO_EXPECTATIONS: str = "ifo expectations"
            """IFO Expectations"""

            IMF_LAGARDE_SPEECH: str = "imf lagarde speech"
            """IMF Lagarde Speech"""

            IMPORT_PRICES_MO_M: str = "import prices mom"
            """Import Prices MoM"""

            IMPORT_PRICES_YO_Y: str = "import prices yoy"
            """Import Prices YoY"""

            IMPORTS_MO_M_SEASONALLY_ADJUSTED: str = "imports mom seasonally adjusted"
            """Imports MoM s.a"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_MO_M_FINAL: str = "inflation rate mom final"
            """Inflation Rate MoM Final"""

            INFLATION_RATE_MO_M_FLASH: str = "inflation rate mom flash"
            """Inflation Rate MoM Flash"""

            INFLATION_RATE_MO_M_PRELIMINARY: str = "inflation rate mom preliminary"
            """Inflation Rate MoM Prel"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INFLATION_RATE_YO_Y_FINAL: str = "inflation rate yoy final"
            """Inflation Rate YoY Final"""

            INFLATION_RATE_YO_Y_PRELIMINARY: str = "inflation rate yoy preliminary"
            """Inflation Rate YoY Prel"""

            JOB_VACANCIES: str = "job vacancies"
            """Job Vacancies"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            MARKIT_BME_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit bme manufacturing purchasing managers index final"
            """Markit/BME Manufacturing Pmi Final"""

            MARKIT_BME_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit bme manufacturing purchasing managers index flash"
            """Markit/BME Manufacturing PMI Flash"""

            MARKIT_COMPOSITE_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit composite purchasing managers index final"
            """Markit Composite PMI Final"""

            MARKIT_COMPOSITE_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit composite purchasing managers index flash"
            """Markit Composite PMI Flash"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit manufacturing purchasing managers index"
            """Markit Manufacturing PMI"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit manufacturing purchasing managers index final"
            """Markit Manufacturing PMI Final"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit manufacturing purchasing managers index flash"
            """Markit Manufacturing PMI Flash"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit services purchasing managers index"
            """Markit Services PMI"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit services purchasing managers index final"
            """Markit Services PMI Final"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit services purchasing managers index flash"
            """Markit Services PMI Flash"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PRESIDENTIAL_ELECTIONS: str = "presidential elections"
            """Presidential Elections"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            REFORMATION_DAY: str = "reformation day"
            """Reformation Day"""

            REPENTANCE_DAY: str = "repentance day"
            """Repentance Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            RHINELAND_PALATINATE_STATE_ELECTION: str = "rhineland palatinate state election"
            """Rhineland-Palatinate State Election"""

            SAXONY_ANHALT_STATE_ELECTION: str = "saxony anhalt state election"
            """Saxony-Anhalt State Election"""

            SERVICES_PURCHASING_MANAGERS_INDEX: str = "services purchasing managers index"
            """Services PMI"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            TEN_YEAR_BUND_AUCTION: str = "10 year bund auction"
            """10-Year Bund Auction"""

            THIRTY_YEAR_BUND_AUCTION: str = "30 year bund auction"
            """30-Year Bund Auction"""

            TWELVE_MONTH_BUBILL_AUCTION: str = "12 month bubill auction"
            """12-Month Bubill Auction"""

            TWO_YEAR_SCHATZ_AUCTION: str = "2 year schatz auction"
            """2-Year Schatz Auction"""

            UNEMPLOYED_PERSONS_NOT_SEASONALLY_ADJUSTED: str = "unemployed persons not seasonally adjusted"
            """Unemployed Persons NSA"""

            UNEMPLOYMENT_CHANGE: str = "unemployment change"
            """Unemployment Change"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            UNEMPLOYMENT_RATE_HARMONIZED: str = "unemployment rate harmonized"
            """Unemployment Rate Harmonised"""

            WHIT_MONDAY: str = "whit monday"
            """Whit Monday"""

            WHOLESALE_PRICES_MO_M: str = "wholesale prices mom"
            """Wholesale Prices MoM"""

            WHOLESALE_PRICES_YO_Y: str = "wholesale prices yoy"
            """Wholesale Prices YoY"""

            ZEW_CURRENT_CONDITIONS: str = "zew current conditions"
            """ZEW Current Conditions"""

            ZEW_ECONOMIC_SENTIMENT_INDEX: str = "zew economic sentiment index"
            """ZEW Economic Sentiment Index"""

        class Greece(System.Object):
            """Greece"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CLEAN_MONDAY: str = "clean monday"
            """Clean Monday"""

            CONSTRUCTION_OUTPUT_YO_Y: str = "construction output yoy"
            """Construction Output YoY"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CREDIT_EXPANSION_YO_Y: str = "credit expansion yoy"
            """Credit Expansion YoY"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DEBT_REPAYMENT_OF_EUR_THIRTY_FIVE_B_DUE_TO_ECB: str = "debt repayment of eur 35b due to ecb"
            """Debt Repayment of EUR 3.5B Due to ECB"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            EPIPHANY_DAY: str = "epiphany day"
            """Epiphany Day"""

            EU_BAILOUT_EXPIRATION: str = "eu bailout expiration"
            """EU Bailout Expiration"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp annual growth rate yoy preliminary"
            """GDP Annual Growth Rate YoY - Preliminary"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_ADV: str = "gdp growth rate yoy adv"
            """GDP Growth Rate YoY Adv"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY - P."""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GREEK_PARLIAMENT_ELECTIONS: str = "greek parliament elections"
            """Greek Parliament Elections"""

            GREEK_THIRD_BAILOUT_PROGRAMS_VOTE: str = "greek third bailout programs vote"
            """Greek Third Bailout Program's Vote"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonized Inflation Rate YoY"""

            HOLY_SPIRIT_MONDAY: str = "holy spirit monday"
            """Holy Spirit Monday"""

            INDEPENDENCE_DAY: str = "independence day"
            """Independence Day"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LABOR_DAY_SUBSTITUTE_DAY: str = "labor day substitute day"
            """Labour Day (Substitute Day)"""

            LOANS_TO_PRIVATE_SECTOR: str = "loans to private sector"
            """Loans to Private Sector"""

            LOANS_TO_PRIVATE_SECTOR_YO_Y: str = "loans to private sector yoy"
            """Loans to Private Sector YoY"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit manufacturing purchasing managers index"
            """Markit Manufacturing PMI"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            OCHI_DAY: str = "ochi day"
            """Ochi Day"""

            ORTHODOX_EASTER_MONDAY: str = "orthodox easter monday"
            """Orthodox Easter Monday"""

            ORTHODOX_EASTER_SUNDAY: str = "orthodox easter sunday"
            """Orthodox Easter Sunday"""

            ORTHODOX_GOOD_FRIDAY: str = "orthodox good friday"
            """Orthodox Good Friday"""

            ORTHODOX_WHIT_MONDAY: str = "orthodox whit monday"
            """Orthodox Whit Monday"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            REFERENDUM_ON_BAILOUT_TERMS: str = "referendum on bailout terms"
            """Referendum on Bailout Terms"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            THE_OCHI_DAY: str = "the ochi day"
            """The Ochi Day"""

            THIRTEEN_WEEK_BILL_AUCTION: str = "13 week bill auction"
            """13-Weeks Bill Auction"""

            TOTAL_CREDIT_YO_Y: str = "total credit yoy"
            """Total Credit YoY"""

            TWENTY_SIX_WEEK_BILL_AUCTION: str = "26 week bill auction"
            """26-Weeks Bill Auction"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class Ireland(System.Object):
            """Ireland"""

            AIB_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "aib manufacturing purchasing managers index"
            """AIB Manufacturing PMI"""

            AIB_SERVICES_PURCHASING_MANAGERS_INDEX: str = "aib services purchasing managers index"
            """AIB Services PMI"""

            AUGUST_BANK_HOLIDAY: str = "august bank holiday"
            """August Bank Holiday"""

            AVERAGE_WEEKLY_EARNINGS_YO_Y: str = "average weekly earnings yoy"
            """Average Weekly Earnings YoY"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BALANCE_OF_TRADE_FINAL: str = "balance of trade final"
            """Balance of Trade-Final"""

            BANK_HOLIDAY: str = "bank holiday"
            """Bank Holiday"""

            CBI_GOV_LANE_SPEECH: str = "cbi gov lane speech"
            """CBI Gov Lane Speech"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSTRUCTION_OUTPUT_YO_Y: str = "construction output yoy"
            """Construction Output YoY"""

            CONSTRUCTION_PURCHASING_MANAGERS_INDEX: str = "construction purchasing managers index"
            """Construction PMI"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CORE_INFLATION_RATE: str = "core inflation rate"
            """Core Inflation Rate"""

            CORE_INFLATION_RATE_YO_Y: str = "core inflation rate yoy"
            """Core Inflation Rate YoY"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            ESRI_CONSUMER_SENTIMENT_INDEX: str = "esri consumer sentiment index"
            """ESRI Consumer Sentiment Index"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GNP_QO_Q: str = "gnp qoq"
            """GNP QoQ"""

            GNP_YO_Y: str = "gnp yoy"
            """GNP YoY"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            HARMONIZED_INFLATION_RATE_MO_M: str = "harmonized inflation rate mom"
            """Harmonised Inflation Rate MoM"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonised Inflation Rate YoY"""

            HOUSEHOLD_SAVING_RATIO: str = "household saving ratio"
            """Household Saving Ratio"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE: str = "inflation rate"
            """Inflation Rate"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INVESTEC_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "investec manufacturing purchasing managers index"
            """Investec Manufacturing Pmi"""

            INVESTEC_SERVICES_PURCHASING_MANAGERS_INDEX: str = "investec services purchasing managers index"
            """Investec Services PMI"""

            JUNE_BANK_HOLIDAY: str = "june bank holiday"
            """June Bank Holiday"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit services purchasing managers index"
            """Markit Services PMI"""

            MAY_BANK_HOLIDAY: str = "may bank holiday"
            """May Bank Holiday"""

            MAY_DAY: str = "may day"
            """May Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year’s Day"""

            NEW_YEARS_DAY_SUBSTITUTE_DAY: str = "new years day substitute day"
            """New Year’s Day (Substitute Day)"""

            OCTOBER_BANK_HOLIDAY: str = "october bank holiday"
            """October Bank Holiday"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PURCHASING_MANAGER_INDEX_MANUFACTURING: str = "purchasing manager index manufacturing"
            """Purchasing Manager Index Manufacturing"""

            PURCHASING_MANAGER_INDEX_SERVICES: str = "purchasing manager index services"
            """Purchasing Manager Index Services"""

            PURCHASING_MANAGERS_INDEX_SERVICES: str = "purchasing managers index services"
            """PMI services"""

            RESIDENTIAL_PROPERTY_PRICES_MO_M: str = "residential property prices mom"
            """Residential Property Prices MoM"""

            RESIDENTIAL_PROPERTY_PRICES_YO_Y: str = "residential property prices yoy"
            """Residential Property Prices YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            ST_PATRICKS_DAY: str = "st patricks day"
            """St. Patricks Day"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WHOLESALE_PRICES_MO_M: str = "wholesale prices mom"
            """Wholesale Prices MoM"""

            WHOLESALE_PRICES_YO_Y: str = "wholesale prices yoy"
            """Wholesale Prices YoY"""

        class Italy(System.Object):
            """Italy"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saints' Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOI_ROSSI_SPEECH: str = "boi rossi speech"
            """BoI Rossi Speech"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSTRUCTION_OUTPUT_YO_Y: str = "construction output yoy"
            """Construction Output YoY"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CONSUMER_PRICE_INDEX_EU_NORM_MO_M: str = "consumer price index eu norm mom"
            """Consumer Price Index (EU Norm) (MoM)"""

            CONSUMER_PRICE_INDEX_EU_NORM_YO_Y: str = "consumer price index eu norm yoy"
            """Consumer Price Index (EU Norm) (YoY)"""

            CONSUMER_PRICE_INDEX_MO_M: str = "consumer price index mom"
            """Consumer Price Index (MoM)"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            ECONOMY_AND_FINANCE_MINISTER_PADOAN_SPEECH: str = "economy and finance minister padoan speech"
            """Economy and Finance Minister Padoan Speech"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            FIVE_Y_BOND_AUCTION: str = "5 y bond auction"
            """5-y Bond Auction"""

            FIVE_YEAR_BTP_AUCTION: str = "5 year btp auction"
            """5-Year BTP Auction"""

            FULL_YEAR_GDP_GROWTH: str = "full year gdp growth"
            """Full Year GDP Growth"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_GROWTH_RATE: str = "gdp growth rate"
            """GDP Growth Rate 2015"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_ADV: str = "gdp growth rate qoq adv"
            """GDP Growth Rate QoQ Adv"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_ADV: str = "gdp growth rate yoy adv"
            """GDP Growth Rate YoY Adv"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GENERAL_ELECTIONS: str = "general elections"
            """General Elections"""

            GOVERNMENT_BUDGET: str = "government budget"
            """Government Budget"""

            G_SEVEN_FIN_MINISTERS_AND_CB_GOVERNORS_MEETING: str = "g7 fin ministers and cb governors meeting"
            """G7 Fin Ministers and CB Governors Meeting"""

            G_SEVEN_FOREIGN_MINISTERS_MEETING: str = "g7 foreign ministers meeting"
            """G7 Foreign Ministers Meeting"""

            G_SEVEN_SUMMIT: str = "g7 summit"
            """G7 Summit"""

            HARMONIZED_INFLATION_RATE_MO_M_FINAL: str = "harmonized inflation rate mom final"
            """Harmonised Inflation Rate MoM Final"""

            HARMONIZED_INFLATION_RATE_MO_M_PRELIMINARY: str = "harmonized inflation rate mom preliminary"
            """Harmonised Inflation Rate MoM Prel"""

            HARMONIZED_INFLATION_RATE_YO_Y_FINAL: str = "harmonized inflation rate yoy final"
            """Harmonised Inflation Rate YoY Final"""

            HARMONIZED_INFLATION_RATE_YO_Y_PRELIMINARY: str = "harmonized inflation rate yoy preliminary"
            """Harmonised Inflation Rate YoY Prel"""

            IMMACULATE_CONCEPTION: str = "immaculate conception"
            """Immaculate Conception"""

            INDUSTRIAL_ORDERS_MO_M: str = "industrial orders mom"
            """Industrial Orders MoM"""

            INDUSTRIAL_ORDERS_YO_Y: str = "industrial orders yoy"
            """Industrial Orders YoY"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INDUSTRIAL_SALES_MO_M: str = "industrial sales mom"
            """Industrial Sales MoM"""

            INDUSTRIAL_SALES_YO_Y: str = "industrial sales yoy"
            """Industrial Sales YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_MO_M_FINAL: str = "inflation rate mom final"
            """Inflation Rate MoM Final"""

            INFLATION_RATE_MO_M_PRELIMINARY: str = "inflation rate mom preliminary"
            """Inflation Rate MoM Prel"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INFLATION_RATE_YO_Y_FINAL: str = "inflation rate yoy final"
            """Inflation Rate YoY Final"""

            INFLATION_RATE_YO_Y_PRELIMINARY: str = "inflation rate yoy preliminary"
            """Inflation Rate YoY Prel"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LIBERATION_DAY: str = "liberation day"
            """Liberation Day"""

            MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "manufacturing purchasing managers index"
            """Manufacturing PMI"""

            MARKIT_ADACI_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit adaci manufacturing purchasing managers index"
            """Markit/ADACI Manufacturing PMI"""

            MARKIT_ADACI_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit adaci services purchasing managers index"
            """Markit/ADACI Services PMI"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year’s Day"""

            PM_CONTE_PRESS_CONFERENCE: str = "pm conte press conference"
            """PM Conte Press Conference"""

            PM_CONTE_SPEECH_IN_THE_SENATE: str = "pm conte speech in the senate"
            """PM Conte Speech in the Senate"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            REFERENDUM_ON_CONSTITUTIONAL_REFORM: str = "referendum on constitutional reform"
            """Referendum on Constitutional Reform"""

            REGIONAL_ELECTIONS: str = "regional elections"
            """Regional Elections"""

            RENZI_MERKEL_HOLLANDE_MEET_ON_BREXIT: str = "renzi merkel hollande meet on brexit"
            """Renzi, Merkel, Hollande Meet on Brexit"""

            REPUBLIC_DAY: str = "republic day"
            """Republic Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SEVEN_YEAR_BTP_AUCTION: str = "7 year btp auction"
            """7-Year BTP Auction"""

            SIX_MONTH_BOT_AUCTION: str = "6 month bot auction"
            """6-Month BOT Auction"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            TEN_YEAR_BOND_AUCTION: str = "10 year bond auction"
            """10-Year Bond Auction"""

            TEN_YEAR_BTP_AUCTION: str = "10 year btp auction"
            """10-Year BTP Auction"""

            THIRTY_YEAR_BTP_AUCTION: str = "30 year btp auction"
            """30-Year BTP Auction"""

            THREE_YEAR_BTP_AUCTION: str = "3 year btp auction"
            """3-Year BTP Auction"""

            TWELVE_MONTH_BOT_AUCTION: str = "12 month bot auction"
            """12-Month BOT Auction"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WAGE_INFLATION_MO_M: str = "wage inflation mom"
            """Wage Inflation MoM"""

            WAGE_INFLATION_YO_Y: str = "wage inflation yoy"
            """Wage Inflation YoY"""

        class Japan(System.Object):
            """Japan"""

            ALL_INDUSTRY_ACTIVITY_INDEX_MO_M: str = "all industry activity index mom"
            """All Industry Activity Index MoM"""

            AUTUMN_EQUINOX_DAY: str = "autumn equinox day"
            """Autumn Equinox Day"""

            AVERAGE_CASH_EARNINGS_YO_Y: str = "average cash earnings yoy"
            """Average Cash Earnings YoY"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BANK_HOLIDAY: str = "bank holiday"
            """Bank Holiday"""

            BANK_LENDING_YO_Y: str = "bank lending yoy"
            """Bank lending YoY"""

            BANK_OF_JAPAN_AMAMIYA_SPEECH: str = "bank of japan amamiya speech"
            """BoJ Amamiya Speech"""

            BANK_OF_JAPAN_DEPUTY_GOV_IWATA_SPEECH: str = "bank of japan deputy gov iwata speech"
            """BoJ Deputy Gov Iwata Speech"""

            BANK_OF_JAPAN_DEPUTY_GOV_NAKASO_SPEECH: str = "bank of japan deputy gov nakaso speech"
            """BoJ Deputy Gov Nakaso Speech"""

            BANK_OF_JAPAN_FUNO_SPEECH: str = "bank of japan funo speech"
            """BoJ Funo Speech"""

            BANK_OF_JAPAN_GOV_KURODA_SPEAKS: str = "bank of japan gov kuroda speaks"
            """BoJ Gov Kuroda Speaks"""

            BANK_OF_JAPAN_GOV_KURODA_SPEECH: str = "bank of japan gov kuroda speech"
            """BoJ Gov Kuroda Speech"""

            BANK_OF_JAPAN_HARADA_SPEECH: str = "bank of japan harada speech"
            """BoJ Harada Speech"""

            BANK_OF_JAPAN_INTEREST_RATE_DECISION: str = "bank of japan interest rate decision"
            """BoJ Interest Rate Decision"""

            BANK_OF_JAPAN_IWATA_SPEECH: str = "bank of japan iwata speech"
            """BoJ Iwata Speech"""

            BANK_OF_JAPAN_KATAOKA_SPEECH: str = "bank of japan kataoka speech"
            """BoJ Kataoka Speech"""

            BANK_OF_JAPAN_KIUCHI_SPEECH: str = "bank of japan kiuchi speech"
            """BoJ Kiuchi Speech"""

            BANK_OF_JAPAN_KURODA_SPEECH: str = "bank of japan kuroda speech"
            """BoJ Kuroda Speech"""

            BANK_OF_JAPAN_KUWABARA_SPEECH: str = "bank of japan kuwabara speech"
            """BoJ Kuwabara Speech"""

            BANK_OF_JAPAN_MASAI_SPEECH: str = "bank of japan masai speech"
            """BoJ Masai Speech"""

            BANK_OF_JAPAN_MONETARY_POLICY_MEETING_MINUTES: str = "bank of japan monetary policy meeting minutes"
            """BoJ Monetary Policy Meeting Minutes"""

            BANK_OF_JAPAN_MONETARY_POLICY_STATEMENT: str = "bank of japan monetary policy statement"
            """BOJ Monetary Policy Statement"""

            BANK_OF_JAPAN_MONETARY_POLICY_STATEMENT_AND_PRESS_CONFERENCE: str = "bank of japan monetary policy statement and press conference"
            """BoJ Monetary Policy Statement and press conference"""

            BANK_OF_JAPAN_MONTHLY_REPORT: str = "bank of japan monthly report"
            """BoJ Monthly Report"""

            BANK_OF_JAPAN_NAKASO_SPEECH: str = "bank of japan nakaso speech"
            """BoJ Nakaso Speech"""

            BANK_OF_JAPAN_PRESS_CONFERENCE: str = "bank of japan press conference"
            """BoJ Press Conference"""

            BANK_OF_JAPAN_QUARTERLY_OUTLOOK_REPORT: str = "bank of japan quarterly outlook report"
            """BoJ Quarterly Outlook Report"""

            BANK_OF_JAPAN_QUARTERLY_REPORT: str = "bank of japan quarterly report"
            """BoJ Quarterly Report"""

            BANK_OF_JAPAN_SAKURAI_SPEECH: str = "bank of japan sakurai speech"
            """BoJ Sakurai Speech"""

            BANK_OF_JAPAN_SATO_SPEECH: str = "bank of japan sato speech"
            """BoJ Sato Speech"""

            BANK_OF_JAPAN_SUMMARY_OF_OPINIONS: str = "bank of japan summary of opinions"
            """BoJ Summary of Opinions"""

            BANK_OF_JAPAN_SUZUKI_SPEECH: str = "bank of japan suzuki speech"
            """BoJ Suzuki Speech"""

            BANK_OF_JAPAN_WAKATABE_SPEECH: str = "bank of japan wakatabe speech"
            """BoJ Wakatabe Speech"""

            BUSINESS_SURVEY_INDEX_LARGE_MANUFACTURING_QO_Q: str = "business survey index large manufacturing qoq"
            """BSI Large Manufacturing QoQ"""

            CAPACITY_UTILIZATION_MO_M: str = "capacity utilization mom"
            """Capacity Utilization MoM"""

            CAPITAL_SPENDING_YO_Y: str = "capital spending yoy"
            """Capital Spending YoY"""

            CHILDRENS_DAY: str = "childrens day"
            """Children's Day"""

            COINCIDENT_INDEX: str = "coincident index"
            """Coincident Index"""

            COINCIDENT_INDEX_FINAL: str = "coincident index final"
            """Coincident Index Final"""

            COINCIDENT_INDEX_PRELIMINARY: str = "coincident index preliminary"
            """Coincident Index Prel"""

            COMING_OF_AGE_DAY: str = "coming of age day"
            """Coming of Age Day"""

            CONSTITUTION_DAY: str = "constitution day"
            """Constitution Day"""

            CONSTRUCTION_ORDERS_YO_Y: str = "construction orders yoy"
            """Construction Orders YoY"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CONSUMER_CONFIDENCE_HOUSEHOLDS: str = "consumer confidence households"
            """Consumer Confidence Households"""

            CONSUMER_PRICE_INDEX_EXCLUDING_FRESH_FOOD_YO_Y: str = "consumer price index excluding fresh food yoy"
            """CPI Ex-Fresh Food YoY"""

            CORE_INFLATION_RATE_YO_Y: str = "core inflation rate yoy"
            """Core Inflation Rate YoY"""

            CORPORATE_SERVICE_PRICE_YO_Y: str = "corporate service price yoy"
            """Corporate Service Price YoY"""

            CULTURE_DAY: str = "culture day"
            """Culture Day"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DOMESTIC_CORPORATE_GOODS_PRICE_INDEX_MO_M: str = "domestic corporate goods price index mom"
            """Domestic Corporate Goods Price Index (MoM)"""

            DOMESTIC_CORPORATE_GOODS_PRICE_INDEX_YO_Y: str = "domestic corporate goods price index yoy"
            """Domestic Corporate Goods Price Index (YoY)"""

            ECO_WATCHERS_SURVEY_CURRENT: str = "eco watchers survey current"
            """Eco Watchers Survey Current"""

            ECO_WATCHERS_SURVEY_OUTLOOK: str = "eco watchers survey outlook"
            """Eco Watchers Survey Outlook"""

            EMPERORS_BIRTHDAY: str = "emperors birthday"
            """Emperor's Birthday"""

            EU_JAPAN_SUMMIT: str = "eu japan summit"
            """EU-Japan Summit"""

            EXPORTS: str = "exports"
            """Exports"""

            EXPORTS_YO_Y: str = "exports yoy"
            """Exports YoY"""

            FINANCE_MINISTER_ASO_SPEECH: str = "finance minister aso speech"
            """Finance Minister Aso Speech"""

            FOREIGN_BOND_INVESTMENT: str = "foreign bond investment"
            """Foreign bond investment"""

            FOREIGN_EXCHANGE_RESERVES: str = "foreign exchange reserves"
            """Foreign Exchange Reserves"""

            FOREIGN_INVESTMENT_IN_JAPAN_STOCKS: str = "foreign investment in japan stocks"
            """Foreign investment in Japan stocks"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y_FINAL: str = "gdp annual growth rate yoy final"
            """GDP Annual Growth Rate YoY Final"""

            GDP_CAPITAL_EXPENDITURE_QO_Q: str = "gdp capital expenditure qoq"
            """GDP Capital Expenditure QoQ"""

            GDP_CAPITAL_EXPENDITURE_QO_Q_FINAL: str = "gdp capital expenditure qoq final"
            """GDP Capital Expenditure QoQ Final"""

            GDP_CAPITAL_EXPENDITURE_QO_Q_PRELIMINARY: str = "gdp capital expenditure qoq preliminary"
            """GDP Capital Expenditure QoQ Prel"""

            GDP_DEFLATOR_YO_Y_FINAL: str = "gdp deflator yoy final"
            """GDP Deflator YoY Final"""

            GDP_DEFLATOR_YO_Y_PRELIMINARY: str = "gdp deflator yoy preliminary"
            """GDP Deflator YoY Prel"""

            GDP_EXTERNAL_DEMAND_QO_Q: str = "gdp external demand qoq"
            """GDP External Demand QoQ"""

            GDP_EXTERNAL_DEMAND_QO_Q_FINAL: str = "gdp external demand qoq final"
            """GDP External Demand QoQ Final"""

            GDP_EXTERNAL_DEMAND_QO_Q_PRELIMINARY: str = "gdp external demand qoq preliminary"
            """GDP External Demand QoQ Prel"""

            GDP_GROWTH_ANNUALIZED_FINAL: str = "gdp growth annualized final"
            """Gdp Growth Annualized Final"""

            GDP_GROWTH_ANNUALIZED_PRELIMINARY: str = "gdp growth annualized preliminary"
            """Gdp Growth Annualized Prel."""

            GDP_GROWTH_ANNUALIZED_QO_Q: str = "gdp growth annualized qoq"
            """GDP Growth Annualized QoQ"""

            GDP_GROWTH_ANNUALIZED_QO_Q_FINAL: str = "gdp growth annualized qoq final"
            """GDP Growth Annualized QoQ Final"""

            GDP_GROWTH_ANNUALIZED_QO_Q_PRELIMINARY: str = "gdp growth annualized qoq preliminary"
            """GDP Growth Annualized QoQ Prel."""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_PRICE_INDEX_YO_Y_FINAL: str = "gdp price index yoy final"
            """GDP Price Index YoY Final"""

            GDP_PRICE_INDEX_YO_Y_PRELIMINARY: str = "gdp price index yoy preliminary"
            """GDP Price Index YoY Prel"""

            GDP_PRIVATE_CONSUMPTION_QO_Q: str = "gdp private consumption qoq"
            """GDP Private Consumption QoQ"""

            GDP_PRIVATE_CONSUMPTION_QO_Q_FINAL: str = "gdp private consumption qoq final"
            """GDP Private Consumption QoQ Final"""

            GDP_PRIVATE_CONSUMPTION_QO_Q_PRELIMINARY: str = "gdp private consumption qoq preliminary"
            """GDP Private Consumption QoQ Prel"""

            GENERAL_ELECTIONS: str = "general elections"
            """General Elections"""

            GREENERY_DAY: str = "greenery day"
            """Greenery Day"""

            GROSS_DOMESTIC_PRODUCT_ANNUALIZED_FINAL: str = "gross domestic product annualized final"
            """Gross Domestic Product Annualized Final"""

            GROSS_DOMESTIC_PRODUCT_ANNUALIZED_REVISED: str = "gross domestic product annualized revised"
            """Gross Domestic Product Annualized (R)"""

            G_SEVEN_FINANCE_MINISTERS_AND_CENTRAL_BANK_GOVERNORS_MEETING: str = "g7 finance ministers and central bank governors meeting"
            """G7 Finance Ministers and Central Bank Governors’ Meeting"""

            G_SEVEN_SUMMIT: str = "g7 summit"
            """G7 Summit"""

            G_TWENTY_MEETING: str = "g20 meeting"
            """G20 Meeting"""

            G_TWENTY_SUMMIT_MEETING: str = "g20 summit meeting"
            """G20 Summit Meeting"""

            HEALTH_SPORTS_DAY: str = "health sports day"
            """Health-Sports Day"""

            HOLIDAY: str = "holiday"
            """Holiday"""

            HOUSEHOLD_SPENDING_MO_M: str = "household spending mom"
            """Household Spending MoM"""

            HOUSEHOLD_SPENDING_YO_Y: str = "household spending yoy"
            """Household Spending YoY"""

            HOUSE_OF_COUNCILLORS_ELECTION: str = "house of councillors election"
            """House of Councillors Election"""

            HOUSING_STARTS_YO_Y: str = "housing starts yoy"
            """Housing Starts YoY"""

            IMPORTS: str = "imports"
            """Imports"""

            IMPORTS_YO_Y: str = "imports yoy"
            """Imports YoY"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_MO_M_FINAL: str = "industrial production mom final"
            """Industrial Production MoM Final"""

            INDUSTRIAL_PRODUCTION_MO_M_PRELIMINARY: str = "industrial production mom preliminary"
            """Industrial Production MoM Prel."""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INDUSTRIAL_PRODUCTION_YO_Y_FINAL: str = "industrial production yoy final"
            """Industrial Production YoY Final"""

            INDUSTRIAL_PRODUCTION_YO_Y_PRELIMINARY: str = "industrial production yoy preliminary"
            """Industrial Production YoY Prel"""

            INFLATION_RATE_EXCLUDING_FOOD_AND_ENERGY_YO_Y: str = "inflation rate excluding food and energy yoy"
            """Inflation Rate Ex-Food and Energy YoY"""

            INFLATION_RATE_EXCLUDING_FRESH_FOOD_YO_Y: str = "inflation rate excluding fresh food yoy"
            """Inflation Rate Ex-Fresh Food YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            JIBUN_BANK_COMPOSITE_PURCHASING_MANAGERS_INDEX_FINAL: str = "jibun bank composite purchasing managers index final"
            """Jibun Bank Composite PMI Final"""

            JIBUN_BANK_COMPOSITE_PURCHASING_MANAGERS_INDEX_FLASH: str = "jibun bank composite purchasing managers index flash"
            """Jibun Bank Composite PMI Flash"""

            JIBUN_BANK_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "jibun bank manufacturing purchasing managers index final"
            """Jibun Bank Manufacturing PMI Final"""

            JIBUN_BANK_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "jibun bank manufacturing purchasing managers index flash"
            """Jibun Bank Manufacturing PMI Flash"""

            JIBUN_BANK_SERVICES_PURCHASING_MANAGERS_INDEX: str = "jibun bank services purchasing managers index"
            """Jibun Bank Services PMI"""

            JIBUN_BANK_SERVICES_PURCHASING_MANAGERS_INDEX_FINAL: str = "jibun bank services purchasing managers index final"
            """Jibun Bank Services PMI Final"""

            JIBUN_BANK_SERVICES_PURCHASING_MANAGERS_INDEX_FLASH: str = "jibun bank services purchasing managers index flash"
            """Jibun Bank Services PMI Flash"""

            JOBS_APPLICATIONS_RATIO: str = "jobs applications ratio"
            """Jobs/applications ratio"""

            JP_FOREIGN_RESERVES: str = "jp foreign reserves"
            """JP Foreign Reserves"""

            LABOR_THANKSGIVING_DAY: str = "labor thanksgiving day"
            """Labour Thanksgiving Day"""

            LARGE_RETAILER_SALES: str = "large retailer sales"
            """Large Retailer Sales"""

            LARGE_RETAILERS_SALES: str = "large retailers sales"
            """Large Retailer's Sales"""

            LEADING_COMPOSITE_INDEX_FINAL: str = "leading composite index final"
            """Leading Composite Index Final"""

            LEADING_COMPOSITE_INDEX_PRELIMINARY: str = "leading composite index preliminary"
            """Leading Composite Index Prel"""

            LEADING_ECONOMIC_INDEX: str = "leading economic index"
            """Leading Economic Index"""

            LEADING_ECONOMIC_INDEX_FINAL: str = "leading economic index final"
            """Leading Economic Index Final"""

            LEADING_ECONOMIC_INDEX_PRELIMINARY: str = "leading economic index preliminary"
            """Leading Economic Index Prel"""

            MACHINERY_ORDERS_MO_M: str = "machinery orders mom"
            """Machinery Orders (MoM)"""

            MACHINERY_ORDERS_YO_Y: str = "machinery orders yoy"
            """Machinery Orders (YoY)"""

            MACHINE_TOOL_ORDERS_YO_Y: str = "machine tool orders yoy"
            """Machine Tool Orders YoY"""

            MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "manufacturing purchasing managers index"
            """Manufacturing PMI"""

            MARKIT_JMMA_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit jmma manufacturing purchasing managers index"
            """Markit/JMMA Manufacturing PMI"""

            MARKIT_JMMA_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit jmma manufacturing purchasing managers index final"
            """Markit/JMMA Manufacturing PMI Final"""

            MARKIT_JMMA_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit jmma manufacturing purchasing managers index flash"
            """Markit/JMMA Manufacturing PMI Flash"""

            MARKIT_NIKKEI_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit nikkei services purchasing managers index"
            """Nikkei Markit Services PMI"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit services purchasing managers index"
            """Markit Services PMI"""

            MOF_ASAKAWA_SPEECH: str = "mof asakawa speech"
            """MOF Asakawa Speech"""

            MONETARY_BASE_YO_Y: str = "monetary base yoy"
            """Monetary Base (YoY)"""

            MONEY_SUPPLY_M_TWOCD_YO_Y: str = "money supply m2cd yoy"
            """Money Supply M2+CD (YoY)"""

            MOUNTAIN_DAY: str = "mountain day"
            """Mountain Day"""

            NATIONAL_CORE_INFLATION_RATE_YO_Y: str = "national core inflation rate yoy"
            """National Core Inflation Rate YoY"""

            NATIONAL_FOUNDING_DAY: str = "national founding day"
            """National Founding Day"""

            NATIONAL_HOLIDAY: str = "national holiday"
            """National Holiday"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARSS_DAY: str = "new yearss day"
            """New Years's Day"""

            NIKKEI_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "nikkei manufacturing purchasing managers index final"
            """Nikkei Manufacturing PMI Final"""

            NIKKEI_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "nikkei manufacturing purchasing managers index flash"
            """Nikkei Manufacturing PMI Flash"""

            NIKKEI_SERVICES_PURCHASING_MANAGERS_INDEX: str = "nikkei services purchasing managers index"
            """Nikkei Services PMI"""

            NOMURA_JMMA_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "nomura jmma manufacturing purchasing managers index"
            """Nomura/JMMA Manufacturing PMI"""

            OCEAN_DAY: str = "ocean day"
            """Ocean Day"""

            OECD_HEAD_ANGEL_GURRIA_SPEECH: str = "oecd head angel gurria speech"
            """OECD Head Angel Gurria Speech"""

            OVERALL_HOUSEHOLD_SPENDING_YO_Y: str = "overall household spending yoy"
            """Overall Household Spending YoY"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PM_SHINZO_ABE_TO_DISSOLVE_PARLIAMENT: str = "pm shinzo abe to dissolve parliament"
            """PM Shinzo Abe to Dissolve Parliament"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RESPECT_FOR_THE_AGED_DAY: str = "respect for the aged day"
            """Respect for the Aged Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            RETAIL_TRADE_SEASONALLY_ADJUSTED_MO_M: str = "retail trade seasonally adjusted mom"
            """Retail Trade s.a (MoM)"""

            RETAIL_TRADE_YO_Y: str = "retail trade yoy"
            """Retail Trade (YoY)"""

            REUTERS_TANKAN_INDEX: str = "reuters tankan index"
            """Reuters Tankan Index"""

            SHOWA_DAY: str = "showa day"
            """Showa Day"""

            SPRING_EQUINOX_DAY: str = "spring equinox day"
            """Spring Equinox Day"""

            STOCK_INVESTMENT_BY_FOREIGNERS: str = "stock investment by foreigners"
            """Stock Investment by Foreigners"""

            TANKAN_ALL_LARGE_INDUSTRY_CAPITAL_EXPENDITURE: str = "tankan all large industry capital expenditure"
            """Tankan Large All Industry Capex"""

            TANKAN_ALL_SMALL_INDUSTRY_CAPITAL_EXPENDITURE: str = "tankan all small industry capital expenditure"
            """Tankan All Small Industry CAPEX"""

            TANKAN_LARGE_MANUFACTURING_INDEX: str = "tankan large manufacturing index"
            """Tankan Large Manufacturers Index"""

            TANKAN_LARGE_MANUFACTURING_OUTLOOK: str = "tankan large manufacturing outlook"
            """Tankan Large Manufacturing Outlook"""

            TANKAN_LARGE_NON_MANUFACTURING_INDEX: str = "tankan large non manufacturing index"
            """Tankan Large Non-Manufacturing Index"""

            TANKAN_NON_MANUFACTURING_INDEX: str = "tankan non manufacturing index"
            """Tankan Non-Manufacturing Index"""

            TANKAN_NON_MANUFACTURING_OUTLOOK: str = "tankan non manufacturing outlook"
            """Tankan Non-Manufacturing Outlook"""

            TANKAN_SMALL_MANUFACTURING_INDEX: str = "tankan small manufacturing index"
            """Tankan Small Manufacturers Index"""

            TANKAN_SMALL_MANUFACTURING_OUTLOOK: str = "tankan small manufacturing outlook"
            """Tankan Small Manufacturing Outlook"""

            TANKAN_SMALL_NON_MANUFACTURING_INDEX: str = "tankan small non manufacturing index"
            """Tankan Small Non-Manufacturing Index"""

            TANKAN_SMALL_NON_MANUFACTURING_OUTLOOK: str = "tankan small non manufacturing outlook"
            """Tankan Small Non-Manufacturing Outlook"""

            TEN_YEAR_JGB_AUCTION: str = "10 year jgb auction"
            """10-Year JGB Auction"""

            TERTIARY_INDUSTRY_INDEX_MO_M: str = "tertiary industry index mom"
            """Tertiary Industry Index MoM"""

            THE_EMPERORS_BIRTHDAY: str = "the emperors birthday"
            """The Emperor's Birthday"""

            THIRTY_YEAR_JGB_AUCTION: str = "30 year jgb auction"
            """30-Year JGB Auction"""

            TOKYO_CONSUMER_PRICE_INDEX_YO_Y: str = "tokyo consumer price index yoy"
            """Tokyo CPI YoY"""

            TOKYO_CORE_CONSUMER_PRICE_INDEX_YO_Y: str = "tokyo core consumer price index yoy"
            """Tokyo Core CPI YoY"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            UPPER_HOUSE_ELECTIONS: str = "upper house elections"
            """Upper House Elections"""

            US_JAPAN_TRADE_TALKS: str = "us japan trade talks"
            """US-Japan Trade Talks"""

            VEHICLE_SALES_YO_Y: str = "vehicle sales yoy"
            """Vehicle Sales (YoY)"""

            YUTAKA_HARADA_SPEECH: str = "yutaka harada speech"
            """Yutaka Harada Speech"""

        class Latvia(System.Object):
            """Latvia"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BANK_HOLIDAY: str = "bank holiday"
            """Bank Holiday"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DECLARATION_OF_INDEPENDENCE: str = "declaration of independence"
            """Declaration of Independence"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            MIDSUMMER_DAY: str = "midsummer day"
            """Midsummer Day"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_EVE: str = "new years eve"
            """New Year's Eve"""

            PROCLEMATION_OF_THE_REPUBLIC: str = "proclemation of the republic"
            """Proclemation of The Republic"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            ST_JOHNS_DAY: str = "st johns day"
            """St John's Day"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class Lithuania(System.Object):
            """Lithuania"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saint's Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CHRISTMAS_HOLIDAY: str = "christmas holiday"
            """Christmas Holiday"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            FATHERS_DAY: str = "fathers day"
            """Father’s Day"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ - F."""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY - F."""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            INDEPENDENCE_DAY: str = "independence day"
            """Independence Day"""

            INDEPENDENCE_RESTORATION_DAY: str = "independence restoration day"
            """Independence Restoration Day"""

            INDUSTRIAL_PRODUCTION: str = "industrial production"
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            KING_MINDAUGAS_CORONATION_DAY: str = "king mindaugas coronation day"
            """King Mindaugas’ Coronation Day"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            MOTHERS_DAY: str = "mothers day"
            """Mother’s Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PARLIAMENTARY_ELECTIONS_SECOND_ROUND: str = "parliamentary elections second round"
            """Parliamentary Elections 2nd Round"""

            PRESIDENTIAL_ELECTION: str = "presidential election"
            """Presidential Election"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RESTORATION_OF_INDEPENDENCE_DAY: str = "restoration of independence day"
            """Restoration of Independence Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SECOND_DAY_OF_CHRISTMAS: str = "second day of christmas"
            """2nd Day of Christmas"""

            ST_JOHNS_DAY: str = "st johns day"
            """St John's Day"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class Luxembourg(System.Object):
            """Luxembourg"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saint's Day"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EUROPE_DAY: str = "europe day"
            """Europe Day"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WHIT_MONDAY: str = "whit monday"
            """Whit Monday"""

        class Malta(System.Object):
            """Malta"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            FEAST_OF_OUR_LADY_OF_VICTORIES: str = "feast of our lady of victories"
            """Feast of our Lady of Victories"""

            FEAST_OF_ST_JOSEPH: str = "feast of st joseph"
            """Feast of St Joseph"""

            FEAST_OF_ST_PAULS_SHIPWRECK: str = "feast of st pauls shipwreck"
            """Feast of St Paul's Shipwreck"""

            FEAST_OF_ST_PETER_AND_ST_PAUL: str = "feast of st peter and st paul"
            """Feast of St Peter and St Paul"""

            FREEDOM_DAY: str = "freedom day"
            """Freedom Day"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            IMMACULATE_CONCEPTION: str = "immaculate conception"
            """Immaculate Conception"""

            INDEPENDENCE_DAY: str = "independence day"
            """Independence Day"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE: str = "inflation rate"
            """Inflation Rate"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            REPUBLIC_DAY: str = "republic day"
            """Republic Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SETTE_GIUGNO: str = "sette giugno"
            """Sette Giugno"""

            ST_JOSEPHS_DAY: str = "st josephs day"
            """St Joseph's Day"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class Netherlands(System.Object):
            """Netherlands"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CONSUMER_SPENDING_VOLUME: str = "consumer spending volume"
            """Consumer Spending Volume"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            HOUSEHOLD_CONSUMPTION_YO_Y: str = "household consumption yoy"
            """Household Consumption YoY"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            KINGS_DAY: str = "kings day"
            """King's Day"""

            LIBERATION_DAY: str = "liberation day"
            """Liberation Day"""

            LOCAL_ELECTIONS: str = "local elections"
            """Local Elections"""

            MANUFACTURING_CONFIDENCE: str = "manufacturing confidence"
            """Manufacturing Confidence"""

            MANUFACTURING_PRODUCTION_YO_Y: str = "manufacturing production yoy"
            """Manufacturing Prod YoY"""

            NEVI_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "nevi manufacturing purchasing managers index"
            """NEVI Manufacturing PMI"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PENTECOST: str = "pentecost"
            """Pentecost"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SIX_MONTH_BILL_AUCTION: str = "6 month bill auction"
            """6-Month Bill Auction"""

            TEN_YEAR_BOND_AUCTION: str = "10 year bond auction"
            """10-Year Bond Auction"""

            THREE_MONTH_BILL_AUCTION: str = "3 month bill auction"
            """3-Month Bill Auction"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WHIT_MONDAY: str = "whit monday"
            """Whit Monday"""

        class NewZealand(System.Object):
            """New Zealand"""

            ANZAC_DAY: str = "anzac day"
            """ANZAC Day"""

            ANZ_BUSINESS_CONFIDENCE: str = "anz business confidence"
            """ANZ Business Confidence"""

            ANZ_COMMODITY_PRICE: str = "anz commodity price"
            """ANZ Commodity Price"""

            ANZ_ROY_MORGAN_CONSUMER_CONFIDENCE: str = "anz roy morgan consumer confidence"
            """ANZ Roy Morgan Consumer Confidence"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUILDING_PERMITS_MO_M: str = "building permits mom"
            """Building Permits MoM"""

            BUILDING_PERMITS_SEASONALLY_ADJUSTED_MO_M: str = "building permits seasonally adjusted mom"
            """Building Permits s.a. (MoM)"""

            BUSINESS_INFLATION_EXPECTATIONS: str = "business inflation expectations"
            """Business Inflation Expectations"""

            BUSINESS_NZ_PURCHASING_MANAGERS_INDEX: str = "business nz purchasing managers index"
            """Business NZ PMI"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DAY_AFTER_NEW_YEARS_DAY: str = "day after new years day"
            """Day After New Year's Day"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            ELECTRONIC_CARD_RETAIL_SALES_MO_M: str = "electronic card retail sales mom"
            """Electronic Card Retail Sales  (MoM)"""

            ELECTRONIC_CARD_RETAIL_SALES_YO_Y: str = "electronic card retail sales yoy"
            """Electronic Card Retail Sales (YoY)"""

            ELECTRONIC_RETAIL_CARD_SPENDING_MO_M: str = "electronic retail card spending mom"
            """Electronic Retail Card Spending MoM"""

            ELECTRONIC_RETAIL_CARD_SPENDING_YO_Y: str = "electronic retail card spending yoy"
            """Electronic Retail Card Spending YoY"""

            EMPLOYMENT_CHANGE_QO_Q: str = "employment change qoq"
            """Employment Change QoQ"""

            EXPORT_PRICES_QO_Q: str = "export prices qoq"
            """Export Prices QoQ"""

            EXPORTS: str = "exports"
            """Exports"""

            FINANCIAL_STABILITY_REPORT: str = "financial stability report"
            """Financial Stability Report"""

            FIRST_DAY_FLAG_REFERENDUM: str = "first day flag referendum"
            """1st Day Flag Referendum"""

            FOOD_INFLATION_YO_Y: str = "food inflation yoy"
            """Food Inflation YoY"""

            FOOD_PRICE_INDEX_MO_M: str = "food price index mom"
            """Food Price Index (MoM)"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GENERAL_ELECTIONS: str = "general elections"
            """General Elections"""

            GLOBAL_DAIRY_TRADE_PRICE_INDEX: str = "global dairy trade price index"
            """Global Dairy Trade Price Index"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            IMPORT_PRICES_QO_Q: str = "import prices qoq"
            """Import Prices QoQ"""

            IMPORTS: str = "imports"
            """Imports"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_QO_Q: str = "inflation rate qoq"
            """Inflation Rate QoQ"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INTEREST_RATE_DECISION: str = "interest rate decision"
            """Interest Rate Decision"""

            LABOR_COSTS_INDEX_QO_Q: str = "labor costs index qoq"
            """Labour cost index QoQ"""

            LABOR_COSTS_INDEX_YO_Y: str = "labor costs index yoy"
            """Labour cost index YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LAST_DAY_FLAG_REFERENDUM: str = "last day flag referendum"
            """Last Day Flag Referendum"""

            MANUFACTURING_PRODUCTION_YO_Y: str = "manufacturing production yoy"
            """Manufacturing Production YoY"""

            MANUFACTURING_SALES: str = "manufacturing sales"
            """Manufacturing sales"""

            MANUFACTURING_SALES_YO_Y: str = "manufacturing sales yoy"
            """Manufacturing Sales YoY"""

            MARKIT_BUSINESS_NZ_PURCHASING_MANAGERS_INDEX: str = "markit business nz purchasing managers index"
            """Business NZ/Markit PMI"""

            MONETARY_POLICY_STATEMENT: str = "monetary policy statement"
            """Monetary Policy Statement"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NZIER_BUSINESS_CONFIDENCE: str = "nzier business confidence"
            """NZIER Business Confidence"""

            NZIER_BUSINESS_CONFIDENCE_QO_Q: str = "nzier business confidence qoq"
            """NZIER Business Confidence QoQ"""

            NZIER_CAPACITY_UTILIZATION: str = "nzier capacity utilization"
            """NZIER Capacity Utilization"""

            NZIER_QSBO_CAPACITY_UTILIZATION: str = "nzier qsbo capacity utilization"
            """NZIER QSBO Capacity Utilization"""

            PARTICIPATION_RATE: str = "participation rate"
            """Participation Rate"""

            PRODUCER_PRICE_INDEX_INPUT_QO_Q: str = "producer price index input qoq"
            """PPI Input QoQ"""

            PRODUCER_PRICE_INDEX_OUTPUT_QO_Q: str = "producer price index output qoq"
            """PPI Output QoQ"""

            QUEENS_BIRTHDAY_DAY: str = "queens birthday day"
            """Queen's Birthday Day"""

            RBNZ_ECONOMIC_ASSESMENT: str = "rbnz economic assesment"
            """RBNZ Economic Assesment"""

            RBNZ_FINANCIAL_STABILITY_REPORT: str = "rbnz financial stability report"
            """RBNZ Financial Stability Report"""

            RBNZ_GOV_ORR_SPEECH: str = "rbnz gov orr speech"
            """RBNZ Gov Orr Speech"""

            RBNZ_GOV_WHEELER_SPEECH: str = "rbnz gov wheeler speech"
            """RBNZ Gov Wheeler Speech"""

            RBNZ_INFLATION_EXPECTATIONS_YO_Y: str = "rbnz inflation expectations yoy"
            """RBNZ Inflation Expectations (YoY)"""

            RBNZ_MCDERMOTT_SPEECH: str = "rbnz mcdermott speech"
            """RBNZ McDermott Speech"""

            RBNZ_PRESS_CONFERENCE: str = "rbnz press conference"
            """RBNZ Press Conference"""

            RBNZ_WHEELER_SPEECH: str = "rbnz wheeler speech"
            """RBNZ Wheeler Speech"""

            REINZ_HOUSE_PRICE_INDEX_MO_M: str = "reinz house price index mom"
            """REINZ House Price Index MoM"""

            RETAIL_SALES_QO_Q: str = "retail sales qoq"
            """Retail Sales QoQ"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SERVICES_NZ_PERFORMANCE_OF_SERVICES_INDEX: str = "services nz performance of services index"
            """Services NZ PSI"""

            TERMS_OF_TRADE_QO_Q: str = "terms of trade qoq"
            """Terms of Trade QoQ"""

            TRADE_BALANCE_MO_M: str = "trade balance mom"
            """Trade Balance (MoM)"""

            TRADE_BALANCE_YO_Y: str = "trade balance yoy"
            """Trade Balance (YoY)"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            VISITOR_ARRIVALS_MO_M: str = "visitor arrivals mom"
            """Visitor Arrivals MoM"""

            VISITOR_ARRIVALS_YO_Y: str = "visitor arrivals yoy"
            """Visitor Arrivals (YoY)"""

            WAITANGI_DAY: str = "waitangi day"
            """Waitangi Day"""

            WESTPAC_CONSUMER_CONFIDENCE: str = "westpac consumer confidence"
            """Consumer Confidence WESTPAC"""

            WESTPAC_CONSUMER_SURVEY: str = "westpac consumer survey"
            """Westpac consumer survey"""

        class Portugal(System.Object):
            """Portugal"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saints' Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BDP_GOV_COSTA_SPEECH: str = "bdp gov costa speech"
            """BdP Gov Costa Speech"""

            BUDGET_BALANCE: str = "budget balance"
            """Budget Balance"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CORPUS_CHRISTI: str = "corpus christi"
            """Corpus Christi"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            ECB_FORUM_ON_CENTRAL_BANKING: str = "ecb forum on central banking"
            """ECB Forum on Central Banking"""

            ECONOMIC_ACTIVITY_YO_Y: str = "economic activity yoy"
            """Economic Activity YoY"""

            EXPORTS: str = "exports"
            """Exports"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            IMMACULATE_CONCEPTION: str = "immaculate conception"
            """Immaculate Conception"""

            IMPORTS: str = "imports"
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = "industrial production"
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_MO_M_FINAL: str = "inflation rate mom final"
            """Inflation Rate MoM Final"""

            INFLATION_RATE_MO_M_PRELIMINARY: str = "inflation rate mom preliminary"
            """Inflation Rate MoM Prel"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INFLATION_RATE_YO_Y_FINAL: str = "inflation rate yoy final"
            """Inflation Rate YoY Final"""

            INFLATION_RATE_YO_Y_PRELIMINARY: str = "inflation rate yoy preliminary"
            """Inflation Rate YoY Prel"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LIBERTY_DAY: str = "liberty day"
            """Liberty Day"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PRIVATE_CONSUMPTION_YO_Y: str = "private consumption yoy"
            """Private Consumption YoY"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            REPUBLIC_IMPLANTATION: str = "republic implantation"
            """Republic Implantation"""

            RESTORATION_OF_INDEPENDENCE: str = "restoration of independence"
            """Restoration of Independence"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class Slovakia(System.Object):
            """Slovakia"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saint's Day"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CONSTITUTION_DAY: str = "constitution day"
            """Constitution Day"""

            CONSTRUCTION_OUTPUT_YO_Y: str = "construction output yoy"
            """Construction Output YoY"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CORE_INFLATION_RATE_MO_M: str = "core inflation rate mom"
            """Core Inflation Rate MoM"""

            CORE_INFLATION_RATE_YO_Y: str = "core inflation rate yoy"
            """Core Inflation Rate YoY"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DAY_OF_OUR_LADY_OF_SORROWS: str = "day of our lady of sorrows"
            """Day of Our Lady of Sorrows"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            END_OF_WORLD_WAR_II: str = "end of world war ii"
            """End of World War II"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            EPIPHANY_DAY: str = "epiphany day"
            """Epiphany Day"""

            ESTABLISHMENT_OF_THE_SLOVAK_REPUBLIC: str = "establishment of the slovak republic"
            """Establishment of the Slovak Republic"""

            EUROPEAN_COUNCIL_MEETING: str = "european council meeting"
            """European Council Meeting"""

            EXPORTS: str = "exports"
            """Exports"""

            FINANCE_MINISTRY_ECONOMIC_FORECASTS: str = "finance ministry economic forecasts"
            """Finance Ministry Economic Forecasts"""

            GDP_ANNUAL_GROWTH_RATE_YO_Y: str = "gdp annual growth rate yoy"
            """GDP Annual Growth Rate YoY"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GDP_GROWTH_RATE_YO_Y_SECOND_FINAL: str = "gdp growth rate yoy second final"
            """GDP Growth Rate YoY 2nd Final"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            HARMONIZED_INFLATION_RATE_MO_M: str = "harmonized inflation rate mom"
            """Harmonised Inflation Rate MoM"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonised Inflation Rate YoY"""

            IMPORTS: str = "imports"
            """Imports"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INFORMAL_ECOFIN_MEETING: str = "informal ecofin meeting"
            """Informal Ecofin Meeting"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            NATIONAL_UPRISING_DAY: str = "national uprising day"
            """National Uprising Day"""

            NBS_GOV_MAKUCH_SPEECH: str = "nbs gov makuch speech"
            """NBS Gov Makuch Speech"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PRESIDENTIAL_ELECTION: str = "presidential election"
            """Presidential Election"""

            REAL_WAGES_YO_Y: str = "real wages yoy"
            """Real Wages YoY"""

            REPUBLIC_DAY: str = "republic day"
            """Republic Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            ST_CYRIL_AND_METHODIUS_DAY: str = "st cyril and methodius day"
            """St Cyril and Methodius Day"""

            STRUGGLE_FOR_FREEDOM_AND_DEMOCRACY_DAY: str = "struggle for freedom and democracy day"
            """Struggle for Freedom and Democracy Day"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class Slovenia(System.Object):
            """Slovenia"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saint's Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOS_FESTIC_SPEECH: str = "bos festic speech"
            """BoS Festic Speech"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            DAY_OF_UPRISING_AGAINST_OCCUPATION: str = "day of uprising against occupation"
            """Day of Uprising Against Occupation"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            FINANCE_MINISTER_MRAMOR_SPEECH: str = "finance minister mramor speech"
            """Finance Minister Mramor Speech"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            HARMONIZED_INFLATION_RATE_YO_Y: str = "harmonized inflation rate yoy"
            """Harmonised Inflation Rate YoY"""

            INDEPENDENCE_AND_UNIT_DAY: str = "independence and unit day"
            """Independence and Unit Day"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LABOR_DAY_SUBSTITUTE_DAY: str = "labor day substitute day"
            """Labour Day (Substitute Day)"""

            MAY_DAY: str = "may day"
            """May Day"""

            MAY_DAY_HOLIDAY: str = "may day holiday"
            """May Day Holiday"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_HOLIDAY: str = "new years holiday"
            """New Year's Holiday"""

            PENTECOST: str = "pentecost"
            """Pentecost"""

            PREEREN_DAY: str = "preeren day"
            """Prešeren Day"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            REFORMATION_DAY: str = "reformation day"
            """Reformation Day"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            RETHINKING_MONETARY_FISCAL_POLICY_COORDINATION_SEMINAR: str = "rethinking monetary fiscal policy coordination seminar"
            """Rethinking Monetary-Fiscal Policy Coordination Seminar"""

            TOURIST_ARRIVALS_YO_Y: str = "tourist arrivals yoy"
            """Tourist Arrivals YoY"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            UPRISING_AGAINST_THE_OCCUPATION_DAY: str = "uprising against the occupation day"
            """Uprising Against the Occupation Day"""

        class Spain(System.Object):
            """Spain"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saints' Day"""

            ASSUMPTION_OF_MARY: str = "assumption of mary"
            """Assumption of Mary"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BDE_GOV_LINDE_SPEECH: str = "bde gov linde speech"
            """BdE Gov Linde Speech"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CATALONIAN_PARLIMENTARY_ELECTIONS: str = "catalonian parlimentary elections"
            """Catalonian Parlimentary Elections"""

            CATALONIA_PARLIAMENTARY_ELECTION: str = "catalonia parliamentary election"
            """Catalonia Parliamentary Election"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSTITUTION_DAY: str = "constitution day"
            """Constitution Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            EPIPHANY_HOLIDAY: str = "epiphany holiday"
            """Epiphany Holiday"""

            FINANCE_MINISTER_GUINDOS_SPEECH: str = "finance minister guindos speech"
            """Finance Minister Guindos Speech"""

            FIVE_YEAR_BONOS_AUCTION: str = "5 year bonos auction"
            """5-Year Bonos Auction"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GENERAL_ELECTION: str = "general election"
            """General Election"""

            GENERAL_ELECTIONS: str = "general elections"
            """General Elections"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            HARMONIZED_INFLATION_RATE_MO_M_FINAL: str = "harmonized inflation rate mom final"
            """Harmonised Inflation Rate MoM Final"""

            HARMONIZED_INFLATION_RATE_MO_M_PRELIMINARY: str = "harmonized inflation rate mom preliminary"
            """Harmonised Inflation Rate MoM Prel"""

            HARMONIZED_INFLATION_RATE_YO_Y_FINAL: str = "harmonized inflation rate yoy final"
            """Harmonised Inflation Rate YoY Final"""

            HARMONIZED_INFLATION_RATE_YO_Y_PRELIMINARY: str = "harmonized inflation rate yoy preliminary"
            """Harmonised Inflation Rate YoY Prel"""

            HISPANIC_DAY: str = "hispanic day"
            """Hispanic Day"""

            IIF_SPRING_MEMBERSHIP_MEETING_TWO_THOUSAND_SIXTEEN: str = "iif spring membership meeting 2016"
            """IIF Spring Membership Meeting 2016"""

            IMMACULATE_CONCEPTION: str = "immaculate conception"
            """Immaculate Conception"""

            INDUSTRIAL_ORDERS_YO_Y: str = "industrial orders yoy"
            """Industrial Orders YoY"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_MO_M_FINAL: str = "inflation rate mom final"
            """Inflation Rate MoM Final"""

            INFLATION_RATE_MO_M_PRELIMINARY: str = "inflation rate mom preliminary"
            """Inflation Rate MoM Prel"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INFLATION_RATE_YO_Y_FINAL: str = "inflation rate yoy final"
            """Inflation Rate YoY Final"""

            INFLATION_RATE_YO_Y_PRELIMINARY: str = "inflation rate yoy preliminary"
            """Inflation Rate YoY Prel"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LABOR_DAY_SUBSTITUTE_DAY: str = "labor day substitute day"
            """Labour Day (Substitute Day)"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit manufacturing purchasing managers index"
            """Markit Manufacturing PMI"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit services purchasing managers index"
            """Markit Services PMI"""

            MAUNDY_THURSDAY: str = "maundy thursday"
            """Maundy Thursday"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_CAR_SALES_YO_Y: str = "new car sales yoy"
            """New Car Sales YoY"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_DAY_SUBSTITUTE_DAY: str = "new years day substitute day"
            """New Year's Day (Substitute Day)"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PARLIAMENTARY_VOTE_ON_TWO_THOUSAND_NINETEEN_BUDGET: str = "parliamentary vote on 2019 budget"
            """Parliamentary Vote on 2019 Budget"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SERVICES_PURCHASING_MANAGERS_INDEX: str = "services purchasing managers index"
            """Services PMI"""

            SIX_MONTH_LETRAS_AUCTION: str = "6 month letras auction"
            """6-Month Letras Auction"""

            ST_JOSEPHS_DAY: str = "st josephs day"
            """St. Joseph's Day"""

            TEN_YEAR_OBLIGACION_AUCTION: str = "10 year obligacion auction"
            """10-Year Obligacion Auction"""

            THREE_MONTH_LETRAS_AUCTION: str = "3 month letras auction"
            """3-Month Letras Auction"""

            THREE_YEAR_BONOS_AUCTION: str = "3 year bonos auction"
            """3-Year Bonos Auction"""

            TOURIST_ARRIVALS_YO_Y: str = "tourist arrivals yoy"
            """Tourist Arrivals YoY"""

            TWELVE_MONTH_LETRAS_AUCTION: str = "12 month letras auction"
            """12-Month Letras Auction"""

            UNEMPLOYMENT_CHANGE: str = "unemployment change"
            """Unemployment Change"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class Sweden(System.Object):
            """Sweden"""

            ALL_SAINTS_DAY: str = "all saints day"
            """All Saint's Day"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CAPACITY_UTILIZATION_QO_Q: str = "capacity utilization qoq"
            """Capacity Utilization QoQ"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_EVE: str = "christmas eve"
            """Christmas Eve"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CONSUMER_INFLATION_EXPECTATIONS: str = "consumer inflation expectations"
            """Consumer Inflation Expectations"""

            CONSUMER_PRICE_INDEX_FIXED_INTEREST_RATE_MO_M: str = "consumer price index fixed interest rate mom"
            """CPIF MoM"""

            CONSUMER_PRICE_INDEX_FIXED_INTEREST_RATE_YO_Y: str = "consumer price index fixed interest rate yoy"
            """CPIF YoY"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_EVE: str = "easter eve"
            """Easter Eve"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EASTER_SUNDAY: str = "easter sunday"
            """Easter Sunday"""

            EPIPHANY: str = "epiphany"
            """Epiphany"""

            EPIPHANY_DAY: str = "epiphany day"
            """Epiphany Day"""

            FINANCIAL_STABILITY_REPORT_TWO_THOUSAND_EIGHTEEN: str = "financial stability report 2018"
            """Financial Stability Report 2018"""

            FINANCIAL_STABILITY_REPORT_TWO_THOUSAND_SEVENTEEN: str = "financial stability report 2017"
            """Financial Stability Report 2017"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_FLASH: str = "gdp growth rate qoq flash"
            """GDP Growth Rate QoQ Flash"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_FLASH: str = "gdp growth rate yoy flash"
            """GDP Growth Rate YoY Flash"""

            GENERAL_ELECTIONS: str = "general elections"
            """General Elections"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            HOUSEHOLD_CONSUMPTION_MO_M: str = "household consumption mom"
            """Household Consumption MM"""

            HOUSEHOLD_LENDING_GROWTH_YO_Y: str = "household lending growth yoy"
            """Household Lending Growth YoY"""

            INDUSTRIAL_INVENTORIES_QO_Q: str = "industrial inventories qoq"
            """Industrial Inventories QoQ"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            LENDING_TO_HOUSEHOLDS_YO_Y: str = "lending to households yoy"
            """Lending to Households YoY"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit services purchasing managers index"
            """Markit Services PMI"""

            MIDSUMMER_DAY: str = "midsummer day"
            """Midsummer Day"""

            MIDSUMMER_EVE: str = "midsummer eve"
            """Midsummer Eve"""

            MONETARY_POLICY_MEETING_MINUTES: str = "monetary policy meeting minutes"
            """Monetary Policy Meeting Minutes"""

            MONETARY_POLICY_REPORT: str = "monetary policy report"
            """Monetary Policy Report"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_ORDERS: str = "new orders"
            """New Orders"""

            NEW_ORDERS_YO_Y: str = "new orders yoy"
            """New Orders Manufacturing YoY"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_EVE: str = "new years eve"
            """New Year's Eve"""

            PENTECOST: str = "pentecost"
            """Pentecost"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            PURCHASING_MANAGERS_INDEX_SERVICES: str = "purchasing managers index services"
            """PMI Services"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            RIKSBANK_GOV_INGVES_SPEECH: str = "riksbank gov ingves speech"
            """Riksbank Gov Ingves Speech"""

            RIKSBANK_INGVES_SPEAKS_BEFORE_PARLIAMENT: str = "riksbank ingves speaks before parliament"
            """Riksbank Ingves Speaks before Parliament"""

            RIKSBANK_INGVES_SPEECH: str = "riksbank ingves speech"
            """Riksbank Ingves Speech"""

            RIKSBANK_INTEREST_RATE: str = "riksbank interest rate"
            """Riksbank Interest Rate"""

            RIKSBANK_MEETING_MINUTES: str = "riksbank meeting minutes"
            """Riksbank Meeting Minutes"""

            RIKSBANK_MONETARY_POLICY_REPORT: str = "riksbank monetary policy report"
            """Riksbank Monetary Policy Report"""

            RIKSBANK_RATE_DECISION: str = "riksbank rate decision"
            """Riksbank Rate Decision"""

            RIKSBANK_SKINGSLEY_SPEECH: str = "riksbank skingsley speech"
            """Riksbank Skingsley Speech"""

            SERVICES_PURCHASING_MANAGERS_INDEX: str = "services purchasing managers index"
            """Services PMI"""

            SWEDBANK_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "swedbank manufacturing purchasing managers index"
            """Swedbank Manufacturing PMI"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            WHITSUN: str = "whitsun"
            """Whitsun"""

        class Switzerland(System.Object):
            """Switzerland"""

            ASCENSION_DAY: str = "ascension day"
            """Ascension Day"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            ECONOMIC_SENTIMENT_INDEX: str = "economic sentiment index"
            """Economic Sentiment Index"""

            EMPLOYMENT_LEVEL_QO_Q: str = "employment level qoq"
            """Employment Level (QoQ)"""

            FEDERAL_FAST_DAY: str = "federal fast day"
            """Federal Fast Day"""

            FOREIGN_CURRENCY_RESERVES: str = "foreign currency reserves"
            """Foreign Currency Reserves"""

            FOREIGN_EXCHANGE_RESERVES: str = "foreign exchange reserves"
            """Foreign Exchange Reserves"""

            FX_RESERVES: str = "fx reserves"
            """FX Reserves"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            INDUSTRIAL_ORDERS_YO_Y: str = "industrial orders yoy"
            """Industrial Orders YoY"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            KOF_LEADING_INDICATORS: str = "kof leading indicators"
            """KOF Leading Indicator"""

            LABOR_DAY: str = "labor day"
            """Labour Day"""

            NATIONAL_DAY: str = "national day"
            """National Day"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NON_FARM_PAYROLLS: str = "non farm payrolls"
            """Non Farm Payrolls"""

            NUCLEAR_WITHDRAWAL_INITIATIVE_REFERENDUM: str = "nuclear withdrawal initiative referendum"
            """Nuclear Withdrawal Initiative Referendum"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PROCURECH_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "procurech manufacturing purchasing managers index"
            """procure.ch Manufacturing PMI"""

            PRODUCER_AND_IMPORT_PRICES_MO_M: str = "producer and import prices mom"
            """Producer and Import Prices MoM"""

            PRODUCER_AND_IMPORT_PRICES_YO_Y: str = "producer and import prices yoy"
            """Producer and Import Prices YoY"""

            PRODUCER_IMPORT_PRICES_MO_M: str = "producer import prices mom"
            """Producer/Import Prices MoM"""

            PRODUCER_IMPORT_PRICES_YO_Y: str = "producer import prices yoy"
            """Producer/Import Prices YoY"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            REFERENDUM_ON_CORPORATE_TAX_UNIFICATION: str = "referendum on corporate tax unification"
            """Referendum on Corporate Tax Unification"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            SECO_ECONOMIC_FORECASTS: str = "seco economic forecasts"
            """SECO Economic Forecasts"""

            SNB_ANNUAL_REPORT: str = "snb annual report"
            """SNB Annual Report"""

            SNB_CHAIR_JORDAN_SPEAKS: str = "snb chair jordan speaks"
            """SNB Chair Jordan Speaks"""

            SNB_CHAIR_JORDAN_SPEECH: str = "snb chair jordan speech"
            """SNB Chair Jordan Speech"""

            SNB_CHAIRMAN_JORDAN_SPEECH: str = "snb chairman jordan speech"
            """SNB Chairman Jordan Speech"""

            SNB_FINANCIAL_STABILITY_REPORT: str = "snb financial stability report"
            """SNB Financial Stability Report"""

            SNB_INTEREST_RATE_DECISON: str = "snb interest rate decison"
            """SNB Interest Rate Decison"""

            SNB_JORDAN_SPEECH: str = "snb jordan speech"
            """SNB Jordan Speech"""

            SNB_MAECHLER_SPEECH: str = "snb maechler speech"
            """SNB Maechler Speech"""

            SNB_MONTHLY_BULLETIN: str = "snb monthly bulletin"
            """SNB Monthly Bulletin"""

            SNB_MOSER_SPEECH: str = "snb moser speech"
            """SNB Moser Speech"""

            SNB_PRESIDENT_STUDER_SPEECH: str = "snb president studer speech"
            """SNB President Studer Speech"""

            SNB_PRESS_CONFERENCE: str = "snb press conference"
            """SNB press conference"""

            SNB_QUARTERLY_BULLETIN: str = "snb quarterly bulletin"
            """SNB Quarterly Bulletin"""

            SNB_STUDER_SPEECH: str = "snb studer speech"
            """SNB Studer Speech"""

            SNB_ZURBRGG_SPEECH: str = "snb zurbrgg speech"
            """SNB Zurbrügg Speech"""

            SNB_ZURBRUEGG_SPEECH: str = "snb zurbruegg speech"
            """SNB Zurbruegg Speech"""

            ST_BERCHTOLD: str = "st berchtold"
            """St. Berchtold"""

            ST_STEPHENS_DAY: str = "st stephens day"
            """St Stephen's Day"""

            SVME_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "svme manufacturing purchasing managers index"
            """SVME - Purchasing Managers Index"""

            SVME_PURCHASING_MANAGERS_INDEX: str = "svme manufacturing purchasing managers index"
            """SVME - Purchasing Managers  Index"""

            UBS_CONSUMPTION_INDICATORS: str = "ubs consumption indicators"
            """UBS Consumption Indicator"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            USD_CONSUMPTION_INDICATORS: str = "usd consumption indicators"
            """USD Consumption Indicator"""

            US_PRESIDENT_TRUMP_SPEECH: str = "us president trump speech"
            """US President Trump Speech"""

            WHIT_MONDAY: str = "whit monday"
            """Whit Monday"""

            WORLD_ECONOMIC_FORUM_ANNUAL_MEETING: str = "world economic forum annual meeting"
            """World Economic Forum Annual Meeting"""

            WORLD_ECONOMIC_FORUM_DAVOS: str = "world economic forum davos"
            """World Economic Forum - Davos"""

            ZEW_ECONOMIC_SENTIMENT_INDEX: str = "zew economic sentiment index"
            """ZEW Economic Sentiment Index"""

            ZEW_EXPECTATIONS: str = "zew expectations"
            """ZEW Expectations"""

            ZEW_INVESTOR_SENTIMENT: str = "zew investor sentiment"
            """ZEW investor sentiment"""

            ZEW_SURVEY_EXPECTATIONS: str = "zew survey expectations"
            """ZEW Survey - Expectations"""

        class UnitedKingdom(System.Object):
            """United Kingdom"""

            ARTICLE_FIFTY_BREXIT_PROCESS_STARTS: str = "article 50 brexit process starts"
            """Article 50 Brexit Process Starts"""

            AUTUMN_BUDGET: str = "autumn budget"
            """Autumn Budget"""

            AUTUMN_BUDGET_TWO_THOUSAND_EIGHTEEN: str = "autumn budget 2018"
            """Autumn Budget 2018"""

            AVERAGE_EARNINGS_EXCLUDING_BONUS: str = "average earnings excluding bonus"
            """Average Earnings excl. Bonus"""

            AVERAGE_EARNINGS_INCLUDING_BONUS: str = "average earnings including bonus"
            """Average Earnings incl. Bonus"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BANK_HOLIDAY: str = "bank holiday"
            """Bank Holiday"""

            BANK_OF_ENGLAND_ASSET_PURCHASE_FACILITY: str = "bank of england asset purchase facility"
            """BoE Asset Purchase Facility"""

            BANK_OF_ENGLAND_BAILEY_SPEECH: str = "bank of england bailey speech"
            """BoE Bailey Speech"""

            BANK_OF_ENGLAND_BRAZIER_SPEECH: str = "bank of england brazier speech"
            """BoE Brazier Speech"""

            BANK_OF_ENGLAND_BREEDEN_SPEECH: str = "bank of england breeden speech"
            """BoE Breeden Speech"""

            BANK_OF_ENGLAND_BROADBENT_SPEECH: str = "bank of england broadbent speech"
            """BoE Broadbent Speech"""

            BANK_OF_ENGLAND_CARNEY_SPEAKS: str = "bank of england carney speaks"
            """BoE Carney Speaks"""

            BANK_OF_ENGLAND_CARNEY_SPEAKS_IN_PARLIAMENT_ON_BREXIT: str = "bank of england carney speaks in parliament on brexit"
            """BoE Carney Speaks in Parliament on Brexit"""

            BANK_OF_ENGLAND_CARNEY_SPEECH: str = "bank of england carney speech"
            """BoE Carney Speech"""

            BANK_OF_ENGLAND_CHIEF_ECONOMIST_HALDANE_SPEECH: str = "bank of england chief economist haldane speech"
            """BoE Chief Economist Haldane Speech"""

            BANK_OF_ENGLAND_CHURM_SPEECH: str = "bank of england churm speech"
            """BoE Churm Speech"""

            BANK_OF_ENGLAND_CLELAND_SPEECH: str = "bank of england cleland speech"
            """BoE Cleland Speech"""

            BANK_OF_ENGLAND_CONSUMER_CREDIT: str = "bank of england consumer credit"
            """BoE Consumer Credit"""

            BANK_OF_ENGLAND_CREDIT_CONDITIONS_SURVEY: str = "bank of england credit conditions survey"
            """BOE Credit Conditions Survey"""

            BANK_OF_ENGLAND_CUNLIFFE_SPEECH: str = "bank of england cunliffe speech"
            """BoE Cunliffe Speech"""

            BANK_OF_ENGLAND_DEPUTY_GOV_BAILEY_SPEECH: str = "bank of england deputy gov bailey speech"
            """BoE Deputy Gov Bailey Speech"""

            BANK_OF_ENGLAND_DEPUTY_GOV_BROADBENT_SPEECH: str = "bank of england deputy gov broadbent speech"
            """BoE Deputy Gov Broadbent Speech"""

            BANK_OF_ENGLAND_DEPUTY_GOV_CUNLIFFE_SPEECH: str = "bank of england deputy gov cunliffe speech"
            """BoE Deputy Gov Cunliffe Speech"""

            BANK_OF_ENGLAND_DEPUTY_GOV_WOODS_SPEECH: str = "bank of england deputy gov woods speech"
            """BoE Deputy Gov Woods Speech"""

            BANK_OF_ENGLAND_FINANCIAL_STABILITY_REPORT: str = "bank of england financial stability report"
            """BoE Financial Stability Report"""

            BANK_OF_ENGLAND_FORBES_SPEECH: str = "bank of england forbes speech"
            """BoE Forbes Speech"""

            BANK_OF_ENGLAND_FPC_MEETING: str = "bank of england fpc meeting"
            """BoE FPC Meeting"""

            BANK_OF_ENGLAND_FPC_MINUTES: str = "bank of england fpc minutes"
            """BoE FPC Minutes"""

            BANK_OF_ENGLAND_FPC_RECORD: str = "bank of england fpc record"
            """BoE FPC Record"""

            BANK_OF_ENGLAND_FPC_STATEMENT: str = "bank of england fpc statement"
            """BoE FPC Statement"""

            BANK_OF_ENGLAND_GOV_CARNEY_SPEECH: str = "bank of england gov carney speech"
            """BoE Gov Carney Speech"""

            BANK_OF_ENGLAND_GOVERNOR_KING_SPEECH: str = "bank of england governor king speech"
            """BoE Governor King Speech"""

            BANK_OF_ENGLAND_HALDANE_SPEECH: str = "bank of england haldane speech"
            """BoE Haldane Speech"""

            BANK_OF_ENGLAND_HASKEL_SPEECH: str = "bank of england haskel speech"
            """BoE Haskel Speech"""

            BANK_OF_ENGLAND_HAUSER_SPEECH: str = "bank of england hauser speech"
            """BoE Hauser Speech"""

            BANK_OF_ENGLAND_HOGG_SPEECH: str = "bank of england hogg speech"
            """BoE Hogg Speech"""

            BANK_OF_ENGLAND_INFLATION_REPORT: str = "bank of england inflation report"
            """BoE Inflation Report"""

            BANK_OF_ENGLAND_INFLATION_REPORT_HEARINGS: str = "bank of england inflation report hearings"
            """BoE Inflation Report Hearings"""

            BANK_OF_ENGLAND_INTEREST_RATE_DECISION: str = "bank of england interest rate decision"
            """BoE Interest Rate Decision"""

            BANK_OF_ENGLAND_KOHN_SPEECH: str = "bank of england kohn speech"
            """BoE Kohn Speech"""

            BANK_OF_ENGLAND_MCCAFFERTY_SPEECH: str = "bank of england mccafferty speech"
            """BoE McCafferty Speech"""

            BANK_OF_ENGLAND_MOULDER_SPEECH: str = "bank of england moulder speech"
            """BoE Moulder Speech"""

            BANK_OF_ENGLAND_MPC_VOTE_CUT: str = "bank of england mpc vote cut"
            """BoE MPC Vote Cut"""

            BANK_OF_ENGLAND_MPC_VOTE_HIKE: str = "bank of england mpc vote hike"
            """BoE MPC Vote Hike"""

            BANK_OF_ENGLAND_MPC_VOTE_UNCHANGED: str = "bank of england mpc vote unchanged"
            """BoE MPC Vote Unchanged"""

            BANK_OF_ENGLAND_PRESS_CONFERENCE: str = "bank of england press conference"
            """BoE Press Conference"""

            BANK_OF_ENGLAND_PROUDMAN_SPEECH: str = "bank of england proudman speech"
            """BoE Proudman Speech"""

            BANK_OF_ENGLAND_QUANTITATIVE_EASING: str = "bank of england quantitative easing"
            """BOE Quantitative Easing"""

            BANK_OF_ENGLAND_QUARTERLY_BULLETIN: str = "bank of england quarterly bulletin"
            """BoE Quarterly Bulletin"""

            BANK_OF_ENGLAND_QUARTERLY_BULLETIN_Q_TWO: str = "bank of england quarterly bulletin q2"
            """BoE Quarterly Bulletin Q2"""

            BANK_OF_ENGLAND_QUARTERLY_INFLATION_REPORT: str = "bank of england quarterly inflation report"
            """Bank of England Quarterly Inflation Report"""

            BANK_OF_ENGLAND_RAMSDEN_SPEECH: str = "bank of england ramsden speech"
            """BoE Ramsden Speech"""

            BANK_OF_ENGLAND_REPORT_ON_EU_WITHDRAWAL_SCENARIOS: str = "bank of england report on eu withdrawal scenarios"
            """BoE Report on EU Withdrawal Scenarios"""

            BANK_OF_ENGLAND_RULE_SPEECH: str = "bank of england rule speech"
            """BoE Rule Speech"""

            BANK_OF_ENGLAND_SALMON_SPEECH: str = "bank of england salmon speech"
            """BoE Salmon Speech"""

            BANK_OF_ENGLAND_SAPORTA_SPEECH: str = "bank of england saporta speech"
            """BoE Saporta Speech"""

            BANK_OF_ENGLAND_SAUNDERS_SPEECH: str = "bank of england saunders speech"
            """BoE Saunders Speech"""

            BANK_OF_ENGLAND_SHAFIK_SPEECH: str = "bank of england shafik speech"
            """BoE Shafik Speech"""

            BANK_OF_ENGLAND_SHARP_SPEECH: str = "bank of england sharp speech"
            """BoE Sharp Speech"""

            BANK_OF_ENGLAND_STRESS_TEST_RESULTS: str = "bank of england stress test results"
            """BoE Stress Test Results"""

            BANK_OF_ENGLAND_SYSTEMIC_RISK_SURVEY_RESULTS: str = "bank of england systemic risk survey results"
            """BoE Systemic Risk Survey Results"""

            BANK_OF_ENGLAND_TENREYRO_SPEECH: str = "bank of england tenreyro speech"
            """BoE Tenreyro Speech"""

            BANK_OF_ENGLAND_VLIEGHE_SPEECH: str = "bank of england vlieghe speech"
            """BoE Vlieghe Speech"""

            BANK_OF_ENGLAND_WEALE_SPEECH: str = "bank of england weale speech"
            """BoE Weale Speech"""

            BANK_OF_ENGLAND_WOODS_SPEECH: str = "bank of england woods speech"
            """BoE Woods Speech"""

            BANK_STRESS_TESTS: str = "bank stress tests"
            """Bank Stress Tests"""

            BBA_MORTGAGE_APPROVALS: str = "bba mortgage approvals"
            """BBA Mortgage Approvals"""

            BCC_QUARTERLY_ECONOMIC_SURVEY: str = "bcc quarterly economic survey"
            """BCC Quarterly Economic Survey"""

            BENN_BILL_DEBATE: str = "benn bill debate"
            """Benn Bill Debate"""

            BOES_CARNEY_AND_CUNLIFFE_SPEAK_IN_PARLIAMENT: str = "boes carney and cunliffe speak in parliament"
            """BoE's Carney and Cunliffe Speak in Parliament"""

            BOES_GOV_CARNEY_SPEECH: str = "boes gov carney speech"
            """BOE's Gov Carney speech"""

            BOES_GOVERNOR_CARNEY_SPEAKS: str = "boes governor carney speaks"
            """BoE's Governor Carney Speaks"""

            BOES_GOVERNOR_CARNEY_SPEAKS_AT_PARLIAMENT: str = "boes governor carney speaks at parliament"
            """BoE's Governor Carney Speaks at Parliament"""

            BOES_GOVERNOR_CARNEY_SPEECH: str = "boes governor carney speech"
            """BOE's Governor Carney Speech"""

            BOES_GOVERNOR_KING_SPEECH: str = "boes governor king speech"
            """BoEs Governor King Speech"""

            BOXING_DAY: str = "boxing day"
            """Boxing Day"""

            BRC_RETAIL_SALES_YO_Y: str = "brc retail sales yoy"
            """BRC Retail Sales Monitor - All (YoY)"""

            BRC_SHOP_PRICE_INDEX_MO_M: str = "brc shop price index mom"
            """BRC Shop Price Index (MoM)"""

            BRC_SHOP_PRICE_INDEX_YO_Y: str = "brc shop price index yoy"
            """BRC Shop Price Index YoY"""

            BREXIT_BILL_DEBATE: str = "brexit bill debate"
            """Brexit Bill Debate"""

            BUDGET_REPORT: str = "budget report"
            """Budget Report"""

            BUSINESS_CONFIDENCE: str = "business confidence"
            """Business Confidence"""

            BUSINESS_INVESTMENT_QO_Q: str = "business investment qoq"
            """Business Investment QoQ"""

            BUSINESS_INVESTMENT_QO_Q_FINAL: str = "business investment qoq final"
            """Business Investment QoQ Final"""

            BUSINESS_INVESTMENT_QO_Q_PRELIMINARY: str = "business investment qoq preliminary"
            """Business Investment QoQ Prel"""

            BUSINESS_INVESTMENT_YO_Y: str = "business investment yoy"
            """Business Investment YoY"""

            BUSINESS_INVESTMENT_YO_Y_FINAL: str = "business investment yoy final"
            """Business Investment YoY Final"""

            BUSINESS_INVESTMENT_YO_Y_PRELIMINARY: str = "business investment yoy preliminary"
            """Business Investment YoY Prel"""

            CABINET_MEETING_ON_BREXIT_DRAFT_DEAL: str = "cabinet meeting on brexit draft deal"
            """Cabinet Meeting on Brexit Draft Deal"""

            CBI_BUSINESS_OPTIMISM_INDEX: str = "cbi business optimism index"
            """CBI Business Optimism Index"""

            CBI_DISTRIBUTIVE_TRADES: str = "cbi distributive trades"
            """CBI Distributive Trades"""

            CBI_INDUSTRIAL_TRENDS_ORDERS: str = "cbi industrial trends orders"
            """CBI Industrial Trends Orders"""

            CB_LEADING_ECONOMIC_INDEX: str = "cb leading economic index"
            """CB Leading Index"""

            CB_LEADING_ECONOMIC_INDEX_MO_M: str = "cb leading economic index mom"
            """CB Leading Economic Index MoM"""

            CHANCELLOR_HAMMOND_BUDGET_STATEMENT: str = "chancellor hammond budget statement"
            """Chancellor Hammond Budget Statement"""

            CHANCELLOR_OSBORNE_BUDGET_STATEMENT: str = "chancellor osborne budget statement"
            """Chancellor Osborne Budget Statement"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_DAY_SUBSTITUTE_DAY: str = "christmas day substitute day"
            """Christmas Day (Substitute Day)"""

            CLAIMANT_COUNT_CHANGE: str = "claimant count change"
            """Claimant Count Change"""

            CLAIMANT_COUNT_RATE: str = "claimant count rate"
            """Claimant Count Rate"""

            CONSTRUCTION_ORDERS_YO_Y: str = "construction orders yoy"
            """Construction Orders YoY"""

            CONSTRUCTION_OUTPUT_YO_Y: str = "construction output yoy"
            """Construction Output YoY"""

            CONSTRUCTION_PURCHASING_MANAGERS_INDEX: str = "construction purchasing managers index"
            """Construction PMI"""

            CONSUMER_INFLATION_EXPECTATIONS: str = "consumer inflation expectations"
            """Consumer Inflation Expectations"""

            CORE_INFLATION_RATE_MO_M: str = "core inflation rate mom"
            """Core Inflation Rate MoM"""

            CORE_INFLATION_RATE_YO_Y: str = "core inflation rate yoy"
            """Core Inflation Rate YoY"""

            CORE_RETAIL_PRICE_INDEX_MO_M: str = "core retail price index mom"
            """Core RPI MoM"""

            CORE_RETAIL_PRICE_INDEX_YO_Y: str = "core retail price index yoy"
            """Core RPI YoY"""

            CORE_RETAIL_SALES_YO_Y: str = "core retail sales yoy"
            """Core Retail Sales YoY"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            EARLY_MAY_BANK_HOLIDAY: str = "early may bank holiday"
            """Early May Bank Holiday"""

            EASTER_MONDAY: str = "easter monday"
            """Easter Monday"""

            EMPLOYMENT_CHANGE: str = "employment change"
            """Employment Change"""

            EU_MEMBERSHIP_REFERENDUM_FINAL_RESULTS: str = "eu membership referendum final results"
            """EU Membership Referendum - Final Results"""

            EUROPEAN_UNION_MEMBERSHIP_REFERENDUM: str = "european union membership referendum"
            """European Union Membership Referendum"""

            FINANCE_MINISTER_OSBORNE_SPEECH: str = "finance minister osborne speech"
            """Finance Minister Osborne Speech"""

            FINANCE_MIN_OSBORNE_SPEAKS_ON_BREXIT: str = "finance min osborne speaks on brexit"
            """Finance Min Osborne Speaks on Brexit"""

            FINANCIAL_STABILITY_REPORT: str = "financial stability report"
            """Financial Stability Report"""

            FIN_MINISTER_HAMMOND_SPEECH: str = "fin minister hammond speech"
            """Fin Minister Hammond Speech"""

            FIN_MINISTER_OSBORNE_SPEAKS_IN_PARLIAMENT: str = "fin minister osborne speaks in parliament"
            """Fin Minister Osborne Speaks in Parliament"""

            FIVE_YEAR_TREASURY_GILT_AUCTION: str = "5 year treasury gilt auction"
            """5-Year Treasury Gilt Auction"""

            GDP_GROWTH_RATE: str = "gdp growth rate"
            """GDP Growth Rate"""

            GDP_GROWTH_RATE_QO_Q: str = "gdp growth rate qoq"
            """GDP Growth Rate QoQ"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_PRELIMINARY: str = "gdp growth rate qoq preliminary"
            """GDP Growth Rate QoQ Prel"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_YO_Y: str = "gdp growth rate yoy"
            """GDP Growth Rate YoY"""

            GDP_GROWTH_RATE_YO_Y_FINAL: str = "gdp growth rate yoy final"
            """GDP Growth Rate YoY Final"""

            GDP_GROWTH_RATE_YO_Y_PRELIMINARY: str = "gdp growth rate yoy preliminary"
            """GDP Growth Rate YoY Prel"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY 2nd Est"""

            GDP_GROWTH_YO_Y: str = "gdp growth yoy"
            """GDP Growth YoY"""

            GDP_MO_M: str = "gdp mom"
            """GDP MoM"""

            GDP_THREE_MONTH_AVG: str = "gdp 3 month avg"
            """GDP 3-Month Avg"""

            GDP_YO_Y: str = "gdp yoy"
            """GDP YoY"""

            GENERAL_ELECTION: str = "general election"
            """General Election"""

            GFK_CONSUMER_CONFIDENCE: str = "gfk consumer confidence"
            """Gfk Consumer Confidence"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            GOODS_TRADE_BALANCE: str = "goods trade balance"
            """Goods Trade Balance"""

            GOVERNMENT_AUTUMN_FORECASTS: str = "government autumn forecasts"
            """Government Autumn Forecasts"""

            HALIFAX_HOUSE_PRICE_INDEX_MO_M: str = "halifax house price index mom"
            """Halifax House Price Index MoM"""

            HALIFAX_HOUSE_PRICE_INDEX_YO_Y: str = "halifax house price index yoy"
            """Halifax House Price Index YoY"""

            HAMMOND_PRESENTS_AUTUMN_STATEMENT: str = "hammond presents autumn statement"
            """Hammond Presents Autumn Statement"""

            HOMETRACK_HOUSING_PRICES_MO_M: str = "hometrack housing prices mom"
            """Hometrack Housing Prices MoM"""

            HOMETRACK_HOUSING_PRICES_SEASONALLY_ADJUSTED: str = "hometrack housing prices seasonally adjusted"
            """Hometrack Housing Prices s.a"""

            HOUSE_PRICE_INDEX_MO_M: str = "house price index mom"
            """House Price Index MoM"""

            HOUSE_PRICE_INDEX_YO_Y: str = "house price index yoy"
            """House Price Index YoY"""

            INDEX_OF_SERVICES_THREE_M_THREE_M: str = "index of services 3m 3m"
            """Index of Services (3M/3M)"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INFLATION_REPORT_HEARINGS: str = "inflation report hearings"
            """Inflation Report Hearings"""

            INTEREST_RATE_DECISION: str = "interest rate decision"
            """Interest Rate Decision"""

            LABOR_COSTS_INDEX_QO_Q: str = "labor costs index qoq"
            """Labour Costs QoQ"""

            LABOR_PRODUCTIVITY_QO_Q: str = "labor productivity qoq"
            """Labour Productivity QoQ"""

            LABOR_PRODUCTIVITY_QO_Q_FINAL: str = "labor productivity qoq final"
            """Labour Productivity QoQ Final"""

            LABOR_PRODUCTIVITY_QO_Q_PRELIMINARY: str = "labor productivity qoq preliminary"
            """Labour Productivity QoQ Prel"""

            LOCAL_ELECTIONS: str = "local elections"
            """Local Elections"""

            LONDON_ASSEMBLY_ELECTION: str = "london assembly election"
            """London Assembly Election"""

            LONDON_MAYORAL_ELECTION: str = "london mayoral election"
            """London Mayoral Election"""

            MANUFACTURING_PRODUCTION_MO_M: str = "manufacturing production mom"
            """Manufacturing Production MoM"""

            MANUFACTURING_PRODUCTION_YO_Y: str = "manufacturing production yoy"
            """Manufacturing Production YoY"""

            MARK_CARNEY_WILL_BECOME_THE_NEW_BANK_OF_ENGLAND_GOVERNOR: str = "mark carney will become the new bank of england governor"
            """Mark Carney will become the new Bank of England Governor"""

            MARKIT_CIPS_COMPOSITE_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit cips composite purchasing managers index final"
            """Markit/CIPS Composite PMI Final"""

            MARKIT_CIPS_COMPOSITE_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit cips composite purchasing managers index flash"
            """Markit/CIPS Composite PMI Flash"""

            MARKIT_CIPS_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit cips manufacturing purchasing managers index"
            """Markit/CIPS Manufacturing PMI"""

            MARKIT_CIPS_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit cips manufacturing purchasing managers index final"
            """Markit/CIPS Manufacturing PMI Final"""

            MARKIT_CIPS_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit cips manufacturing purchasing managers index flash"
            """Markit/CIPS Manufacturing PMI Flash"""

            MARKIT_CIPS_UK_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit cips uk services purchasing managers index"
            """Markit/CIPS UK Services PMI"""

            MARKIT_CIPS_UK_SERVICES_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit cips uk services purchasing managers index final"
            """Markit/CIPS UK Services PMI Final"""

            MARKIT_CIPS_UK_SERVICES_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit cips uk services purchasing managers index flash"
            """Markit/CIPS UK Services PMI Flash"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit manufacturing purchasing managers index"
            """Markit Manufacturing PMI"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX: str = "markit services purchasing managers index"
            """Markit Services PMI"""

            MAY_DAY: str = "may day"
            """May Day"""

            MAY_NO_CONFIDENCE_VOTE_RESULT: str = "may no confidence vote result"
            """May No Confidence Vote Result"""

            M_FOUR_MONEY_SUPPLY_MO_M: str = "m4 money supply mom"
            """M4 Money Supply (MoM)"""

            M_FOUR_MONEY_SUPPLY_YO_Y: str = "m4 money supply yoy"
            """M4 Money Supply (YoY)"""

            MONTHLY_GDP: str = "monthly gdp"
            """Monthly GDP"""

            MONTHLY_GDP_THREE_MONTH_AVG: str = "monthly gdp 3 month avg"
            """Monthly GDP 3-Month Avg"""

            MORTGAGE_APPROVALS: str = "mortgage approvals"
            """Mortgage Approvals"""

            MORTGAGE_LENDING: str = "mortgage lending"
            """Mortgage Lending"""

            MPC_MEETING_MINUTES: str = "mpc meeting minutes"
            """MPC Meeting Minutes"""

            MPC_MEMBER_BEAN_SPEECH: str = "mpc member bean speech"
            """MPC Member Bean Speech"""

            MPC_MEMBER_PAUL_FISHER_SPEECH: str = "mpc member paul fisher speech"
            """MPC Member Paul Fisher Speech"""

            MPS_VOTE_ON_BENN_BILL: str = "mps vote on benn bill"
            """MPs Vote on Benn Bill"""

            MPS_VOTE_ON_BREXIT_BILL: str = "mps vote on brexit bill"
            """MPs Vote on Brexit Bill"""

            MPS_VOTE_ON_BREXIT_TIMETABLE: str = "mps vote on brexit timetable"
            """MPs Vote on Brexit Timetable"""

            MPS_VOTE_ON_PM_ELECTION_CALL: str = "mps vote on pm election call"
            """MPs Vote on PM Election Call"""

            MPS_VOTE_ON_WITHDRAWAL_AGREEMENT_BILL: str = "mps vote on withdrawal agreement bill"
            """MPs Vote on Withdrawal Agreement Bill"""

            NATIONAL_ASSEMBLY_FOR_WALES_ELECTIONS: str = "national assembly for wales elections"
            """National Assembly for Wales Elections"""

            NATIONWIDE_HOUSING_PRICES_MO_M: str = "nationwide housing prices mom"
            """Nationwide Housing Prices MoM"""

            NATIONWIDE_HOUSING_PRICES_YO_Y: str = "nationwide housing prices yoy"
            """Nationwide Housing Prices YoY"""

            NET_LENDING_TO_INDIVIDUALS_MO_M: str = "net lending to individuals mom"
            """Net Lending to Individuals MoM"""

            NEW_CAR_SALES_YO_Y: str = "new car sales yoy"
            """New Car Sales YoY"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_DAY_SUBSTITUTE_DAY: str = "new years day substitute day"
            """New Year’s Day (Substitute Day)"""

            NIESR_GDP_ESTIMATE_THREE_MONTHS: str = "niesr gdp estimate 3m"
            """NIESR GDP Est (3M)"""

            NIESR_MONTHLY_GDP_TRACKER: str = "niesr monthly gdp tracker"
            """NIESR Monthly GDP Tracker"""

            NORTHERN_IRELAND_ASSEMBLY_ELECTION: str = "northern ireland assembly election"
            """Northern Ireland Assembly Election"""

            OBR_FISCAL_FORECASTS: str = "obr fiscal forecasts"
            """OBR Fiscal Forecasts"""

            OBR_FISCAL_RISKS_REPORT: str = "obr fiscal risks report"
            """OBR Fiscal Risks Report"""

            OECD_GURRIA_SPEECH_ON_UK_REFERENDUM: str = "oecd gurria speech on uk referendum"
            """OECD Gurria Speech on UK Referendum"""

            PARLIAMENTARY_DEBATE_AND_VOTE_ON_PART_OF_BREXIT_DEAL: str = "parliamentary debate and vote on part of brexit deal"
            """Parliamentary Debate & Vote on Part of Brexit Deal"""

            PARLIAMENTARY_ELECTIONS: str = "parliamentary elections"
            """Parliamentary Elections"""

            PARLIAMENTARY_VOTE_ON_ART_FIFTY_EXTENSION: str = "parliamentary vote on art 50 extension"
            """Parliamentary Vote on Art 50 Extension"""

            PARLIAMENTARY_VOTE_ON_BREXIT_AMENDMENTS: str = "parliamentary vote on brexit amendments"
            """Parliamentary Vote on Brexit Amendments"""

            PARLIAMENTARY_VOTE_ON_BREXIT_DEAL: str = "parliamentary vote on brexit deal"
            """Parliamentary Vote on Brexit Deal"""

            PARLIAMENTARY_VOTE_ON_NO_DEAL_BREXIT: str = "parliamentary vote on no deal brexit"
            """Parliamentary Vote on No-Deal Brexit"""

            PARLIAMENTARY_VOTES_ON_BREXIT_ALTERNATIVES: str = "parliamentary votes on brexit alternatives"
            """Parliamentary Votes on Brexit Alternatives"""

            PARLIAMENT_DEBATE_ON_BREXIT: str = "parliament debate on brexit"
            """Parliament Debate on Brexit"""

            PARLIAMENT_DEBATE_ON_BREXIT_ALTERNATIVES: str = "parliament debate on brexit alternatives"
            """Parliament Debate on Brexit Alternatives"""

            PM_MAY_NO_CONFIDENCE_VOTE: str = "pm may no confidence vote"
            """PM May No Confidence Vote"""

            PM_MAYS_PLAN_B_STATEMENT_ON_BREXIT: str = "pm mays plan b statement on brexit"
            """PM May's Plan B Statement on Brexit"""

            PM_MAYS_STATEMENT_ON_BREXIT: str = "pm mays statement on brexit"
            """PM May's Statement on Brexit"""

            PM_MAY_STATEMENT_ON_NEW_BREXIT_DEAL: str = "pm may statement on new brexit deal"
            """PM May Statement on New Brexit Deal"""

            PRIME_MINISTER_MAY_SPEECH: str = "prime minister may speech"
            """Prime Minister May Speech"""

            PRIME_MINISTER_MAY_SPEECH_ON_BREXIT: str = "prime minister may speech on brexit"
            """Prime Minister May Speech on Brexit"""

            PRIME_MINISTER_THERESA_MAY_SPEECH: str = "prime minister theresa may speech"
            """Prime Minister Theresa May Speech"""

            PRODUCER_PRICE_INDEX_CORE_OUTPUT_MO_M: str = "producer price index core output mom"
            """PPI Core Output MoM"""

            PRODUCER_PRICE_INDEX_CORE_OUTPUT_YO_Y: str = "producer price index core output yoy"
            """PPI Core Output YoY"""

            PRODUCER_PRICE_INDEX_INPUT_MO_M: str = "producer price index input mom"
            """PPI Input MoM"""

            PRODUCER_PRICE_INDEX_INPUT_YO_Y: str = "producer price index input yoy"
            """PPI Input YoY"""

            PRODUCER_PRICE_INDEX_OUTPUT_MO_M: str = "producer price index output mom"
            """PPI Output MoM"""

            PRODUCER_PRICE_INDEX_OUTPUT_YO_Y: str = "producer price index output yoy"
            """PPI Output YoY"""

            PUBLIC_SECTOR_BORROWING_MO_M: str = "public sector borrowing mom"
            """Public Sector Borrowing MoM"""

            PUBLIC_SECTOR_NET_BORROWING: str = "public sector net borrowing"
            """Public Sector Net Borrowing"""

            QUEENS_SPEECH_AT_THE_PARLIAMENT: str = "queens speech at the parliament"
            """Queen's Speech at The Parliament"""

            RETAIL_PRICE_INDEX_MO_M: str = "retail price index mom"
            """Retail Price Index MoM"""

            RETAIL_PRICE_INDEX_YO_Y: str = "retail price index yoy"
            """Retail Price Index YoY"""

            RETAIL_SALES_EXCLUDING_FUEL_MO_M: str = "retail sales excluding fuel mom"
            """Retail Sales ex Fuel MoM"""

            RETAIL_SALES_EXCLUDING_FUEL_YO_Y: str = "retail sales excluding fuel yoy"
            """Retail Sales ex Fuel YoY"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            RICS_HOUSE_PRICE_BALANCE: str = "rics house price balance"
            """RICS House Price Balance"""

            SCOTTISH_INDEPENDENCE_REFERENDUM: str = "scottish independence referendum"
            """Scottish Independence Referendum"""

            SCOTTISH_PARLIAMENT_ELECTION: str = "scottish parliament election"
            """Scottish Parliament Election"""

            SPRING_BANK_HOLIDAY: str = "spring bank holiday"
            """Spring Bank Holiday"""

            SPRING_BUDGET_TWO_THOUSAND_EIGHTEEN: str = "spring budget 2018"
            """Spring Budget 2018"""

            SPRING_BUDGET_TWO_THOUSAND_NINETEEN: str = "spring budget 2019"
            """Spring Budget 2019"""

            SUMMER_BANK_HOLIDAY: str = "summer bank holiday"
            """Summer Bank Holiday"""

            TEN_YEAR_TREASURY_GILT_AUCTION: str = "10 year treasury gilt auction"
            """10-Year Treasury Gilt Auction"""

            THIRTY_YEAR_TREASURY_GILT_AUCTION: str = "30 year treasury gilt auction"
            """30-Year Treasury Gilt Auction"""

            TOTAL_BUSINESS_INVESTMENT_QO_Q: str = "total business investment qoq"
            """Total Business Investment (QoQ)"""

            TOTAL_BUSINESS_INVESTMENT_YO_Y: str = "total business investment yoy"
            """Total Business Investment (YoY)"""

            TREASURY_COMMITTEE_HEARING_INFLATION_REPORT: str = "treasury committee hearing inflation report"
            """Treasury Committee Hearing – Inflation Report"""

            TREASURY_SELECT_COMMITTEE_HEARING: str = "treasury select committee hearing"
            """Treasury Select Committee Hearing"""

            TWO_THOUSAND_SIXTEEN_ANNUAL_BUDGET_ANNOUNCEMENT: str = "2016 annual budget announcement"
            """2016 Annual Budget Announcement"""

            UK_FINANCE_MORTGAGE_APPROVALS: str = "uk finance mortgage approvals"
            """UK Finance Mortgage Approvals"""

            UK_GENERAL_ELECTION: str = "uk general election"
            """UK General Election"""

            UK_MAY_EU_JUNCKER_MEETING: str = "uk may eu juncker meeting"
            """UK May - EU Juncker Meeting"""

            UK_PM_STATEMENT_ON_BREXIT: str = "uk pm statement on brexit"
            """UK PM Statement on Brexit"""

            UK_SUPREME_COURT_RULING_ON_ARTICLE_FIFTY: str = "uk supreme court ruling on article 50"
            """UK Supreme Court Ruling On Article 50"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

        class UnitedStates(System.Object):
            """United States"""

            ADP_EMPLOYMENT_CHANGE: str = "adp employment change"
            """ADP Employment Change"""

            ALL_CAR_SALES: str = "all car sales"
            """All Car Sales"""

            ALL_TRUCK_SALES: str = "all truck sales"
            """All Truck Sales"""

            API_WEEKLY_CRUDE_STOCK_CHANGE: str = "api weekly crude stock change"
            """API Weekly Crude Stock Change"""

            API_WEEKLY_GASOLINE_STOCK_CHANGE: str = "api weekly gasoline stock change"
            """API Weekly Gasoline Stock Change"""

            AVERAGE_HOURLY_EARNINGS_MO_M: str = "average hourly earnings mom"
            """Average Hourly Earnings MoM"""

            AVERAGE_HOURLY_EARNINGS_YO_Y: str = "average hourly earnings yoy"
            """Average Hourly Earnings YoY"""

            AVERAGE_WEEKLY_HOURS: str = "average weekly hours"
            """Average Weekly Hours"""

            BAKER_HUGHES_OIL_RIG_COUNT: str = "baker hughes oil rig count"
            """Baker Hughes Oil Rig Count"""

            BALANCE_OF_TRADE: str = "balance of trade"
            """Balance of Trade"""

            BEIGE_BOOK: str = "beige book"
            """Beige Book"""

            BIRTHDAY_OF_MARTIN_LUTHER_KING_JR: str = "birthday of martin luther king jr"
            """Birthday of Martin Luther King, Jr."""

            BUILDING_PERMITS: str = "building permits"
            """Building Permits"""

            BUILDING_PERMITS_MO_M: str = "building permits mom"
            """Building Permits MoM"""

            BUSINESS_INVENTORIES_MO_M: str = "business inventories mom"
            """Business Inventories MoM"""

            CAPACITY_UTILIZATION: str = "capacity utilization"
            """Capacity Utilization"""

            CB_CONSUMER_CONFIDENCE: str = "cb consumer confidence"
            """CB Consumer Confidence"""

            CB_EMPLOYMENT_TRENDS_INDEX: str = "cb employment trends index"
            """CB Employment Trends Index"""

            CB_LEADING_ECONOMIC_INDEX_MO_M: str = "cb leading economic index mom"
            """CB Leading Index MoM"""

            CHAIN_STORES_SALES_WO_W: str = "chain stores sales wow"
            """Chain stores WoW"""

            CHAIN_STORES_SALES_YO_Y: str = "chain stores sales yoy"
            """Chain Stores Sales YoY"""

            CHALLENGER_JOB_CUTS: str = "challenger job cuts"
            """Challenger Job Cuts"""

            CHICAGO_FED_NATIONAL_ACTIVITY_INDEX: str = "chicago fed national activity index"
            """Chicago Fed National Activity Index"""

            CHICAGO_PURCHASING_MANAGERS_INDEX: str = "chicago purchasing managers index"
            """Chicago PMI"""

            CHRISTMAS_DAY: str = "christmas day"
            """Christmas Day"""

            CHRISTMAS_DAY_SUBSTITUTE_DAY: str = "christmas day substitute day"
            """Christmas Day (Substitute Day)"""

            COLUMBUS_DAY: str = "columbus day"
            """Columbus Day"""

            CONSTRUCTION_SPENDING_MO_M: str = "construction spending mom"
            """Construction Spending MoM"""

            CONSUMER_CONFIDENCE: str = "consumer confidence"
            """Consumer Confidence"""

            CONSUMER_CREDIT_CHANGE: str = "consumer credit change"
            """Consumer Credit Change"""

            CONSUMER_INFLATION_EXPECTATIONS: str = "consumer inflation expectations"
            """Consumer Inflation Expectations"""

            CONSUMER_PRICE_INDEX: str = "consumer price index"
            """Consumer Price Index"""

            CONSUMER_PRICE_INDEX_EXCLUDING_FOOD_AND_ENERGY_MO_M: str = "consumer price index excluding food and energy mom"
            """Consumer Price Index Ex Food & Energy (MoM)"""

            CONSUMER_PRICE_INDEX_EXCLUDING_FOOD_AND_ENERGY_YO_Y: str = "consumer price index excluding food and energy yoy"
            """Consumer Price Index Ex Food & Energy (YoY)"""

            CONSUMER_PRICE_INDEX_REAL_EARNINGS_MO_M: str = "consumer price index real earnings mom"
            """CPI Real Earnings MoM"""

            CONTINUING_JOBLESS_CLAIMS: str = "continuing jobless claims"
            """Continuing Jobless Claims"""

            CORE_CONSUMER_PRICE_INDEX: str = "core consumer price index"
            """Core Consumer Price Index"""

            CORE_DURABLE_GOODS_ORDERS: str = "core durable goods orders"
            """Core Durable Goods Orders"""

            CORE_DURABLE_GOODS_ORDERS_MO_M: str = "core durable goods orders mom"
            """Core Durable Goods Orders MoM"""

            CORE_INFLATION_RATE_MO_M: str = "core inflation rate mom"
            """Core Inflation Rate MoM"""

            CORE_INFLATION_RATE_YO_Y: str = "core inflation rate yoy"
            """Core Inflation Rate YoY"""

            CORE_PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_MO_M: str = "core personal consumption expenditure price index mom"
            """Core Personal Consumption Expenditure - Price Index (MoM)"""

            CORE_PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q: str = "core personal consumption expenditure price index qoq"
            """Core Personal Consumption Expenditures QoQ"""

            CORE_PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q_ADV: str = "core personal consumption expenditure price index qoq adv"
            """Core PCE Prices QoQ Adv"""

            CORE_PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q_FINAL: str = "core personal consumption expenditure price index qoq final"
            """Core PCE Prices QoQ Final"""

            CORE_PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q_SECOND_ESTIMATE: str = "core personal consumption expenditure price index qoq second estimate"
            """Core PCE Prices QoQ 2 Est"""

            CORE_PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_YO_Y: str = "core personal consumption expenditure price index yoy"
            """Core PCE Price Index YoY"""

            CORE_PRODUCER_PRICE_INDEX_MO_M: str = "core producer price index mom"
            """Core PPI MoM"""

            CORE_PRODUCER_PRICE_INDEX_YO_Y: str = "core producer price index yoy"
            """Core PPI YoY"""

            CORE_RETAIL_SALES_MO_M: str = "core retail sales mom"
            """Core Retail Sales MoM"""

            CORPORATE_PROFITS_QO_Q: str = "corporate profits qoq"
            """Corporate Profits QoQ"""

            CORPORATE_PROFITS_QO_Q_FINAL: str = "corporate profits qoq final"
            """Corporate Profits QoQ Final"""

            CORPORATE_PROFITS_QO_Q_PRELIMINARY: str = "corporate profits qoq preliminary"
            """Corporate Profits QoQ Prel"""

            CURRENT_ACCOUNT: str = "current account"
            """Current Account"""

            DALLAS_FED_MANUFACTURING_INDEX: str = "dallas fed manufacturing index"
            """Dallas Fed Manufacturing Index"""

            DEADLINE_FOR_FUNDING_FOR_NEW_FISCAL_YEAR: str = "deadline for funding for new fiscal year"
            """Deadline for Funding For New Fiscal Year"""

            DOMESTIC_CAR_SALES: str = "domestic car sales"
            """Domestic Car Sales"""

            DOMESTIC_TRUCK_SALES: str = "domestic truck sales"
            """Domestic Truck Sales"""

            DURABLE_GOODS_ORDERS_EXCLUDING_DEFENSE_MO_M: str = "durable goods orders excluding defense mom"
            """Durable Goods Orders Ex Defense MoM"""

            DURABLE_GOODS_ORDERS_EXCLUDING_TRANSPORTATION_MO_M: str = "durable goods orders excluding transportation mom"
            """Durable Goods Orders Ex Transp MoM"""

            DURABLE_GOODS_ORDERS_MO_M: str = "durable goods orders mom"
            """Durable Goods Orders MoM"""

            EIA_CRUDE_OIL_IMPORTS: str = "eia crude oil imports"
            """EIA Crude Oil Imports"""

            EIA_CRUDE_OIL_IMPORTS_CHANGE: str = "eia crude oil imports change"
            """EIA Crude Oil Imports Change"""

            EIA_CRUDE_OIL_STOCKS_CHANGE: str = "eia crude oil stocks change"
            """EIA Crude Oil Stocks Change"""

            EIA_CUSHING_CRUDE_OIL_STOCKS_CHANGE: str = "eia cushing crude oil stocks change"
            """EIA Cushing Crude Oil Stocks Change"""

            EIA_DISTILLATE_FUEL_PRODUCTION_CHANGE: str = "eia distillate fuel production change"
            """EIA Distillate Fuel Production Change"""

            EIA_DISTILLATE_STOCKS: str = "eia distillate stocks"
            """EIA Distillate Stocks"""

            EIA_DISTILLATE_STOCKS_CHANGE: str = "eia distillate stocks change"
            """EIA Distillate Stocks Change"""

            EIA_GASOLINE_PRODUCTION: str = "eia gasoline production"
            """EIA Gasoline Production"""

            EIA_GASOLINE_PRODUCTION_CHANGE: str = "eia gasoline production change"
            """EIA Gasoline Production Change"""

            EIA_GASOLINE_STOCKS_CHANGE: str = "eia gasoline stocks change"
            """EIA Gasoline Stocks Change"""

            EIA_NATURAL_GAS_STOCKS_CHANGE: str = "eia natural gas stocks change"
            """EIA Natural Gas Stocks Change"""

            EIA_REFINERY_CRUDE_RUNS_CHANGE: str = "eia refinery crude runs change"
            """EIA Refinery Crude Runs Change"""

            EIGHT_WEEK_BILL_AUCTION: str = "8 week bill auction"
            """8-Week Bill Auction"""

            EMPLOYMENT_BENEFITS_QO_Q: str = "employment benefits qoq"
            """Employment Benefits QoQ"""

            EMPLOYMENT_COSTS_BENEFITS_QO_Q: str = "employment costs benefits qoq"
            """Employment Cost - Benefits QoQ"""

            EMPLOYMENT_COSTS_INDEX_QO_Q: str = "employment costs index qoq"
            """Employment Cost Index QoQ"""

            EMPLOYMENT_COSTS_WAGES_QO_Q: str = "employment costs wages qoq"
            """Employment Cost - Wages QoQ"""

            EMPLOYMENT_WAGES_QO_Q: str = "employment wages qoq"
            """Employment Wages QoQ"""

            EXISTING_HOME_SALES: str = "existing home sales"
            """Existing Home Sales"""

            EXISTING_HOME_SALES_MO_M: str = "existing home sales mom"
            """Existing Home Sales MoM"""

            EXPORT_PRICES_MO_M: str = "export prices mom"
            """Export Prices MoM"""

            EXPORT_PRICES_YO_Y: str = "export prices yoy"
            """Export Prices YoY"""

            EXPORTS: str = "exports"
            """Exports"""

            FACTORY_ORDERS_EXCLUDING_TRANSPORTATION: str = "factory orders excluding transportation"
            """Factory Orders ex Transportation"""

            FACTORY_ORDERS_MO_M: str = "factory orders mom"
            """Factory Orders MoM"""

            FED_BARKIN_SPEECH: str = "fed barkin speech"
            """Fed Barkin Speech"""

            FED_BEIGE_BOOK: str = "fed beige book"
            """Fed Beige Book"""

            FED_BERNANKE_SPEECH: str = "fed bernanke speech"
            """Fed Bernanke Speech"""

            FED_BERNANKE_TESTIFIES: str = "fed bernanke testifies"
            """Fed Bernanke testifies"""

            FED_BOSTIC_SPEECH: str = "fed bostic speech"
            """Fed Bostic Speech"""

            FED_BOWMAN_SPEECH: str = "fed bowman speech"
            """Fed Bowman Speech"""

            FED_BOWMAN_TESTIMONY: str = "fed bowman testimony"
            """Fed Bowman Testimony"""

            FED_BRAINARD_SPEAKS: str = "fed brainard speaks"
            """Fed Brainard Speaks"""

            FED_BRAINARD_SPEECH: str = "fed brainard speech"
            """Fed Brainard Speech"""

            FED_BRAINARD_TESTIMONY: str = "fed brainard testimony"
            """Fed Brainard Testimony"""

            FED_BULLARD_SPEAKS: str = "fed bullard speaks"
            """Fed Bullard Speaks"""

            FED_BULLARD_SPEECH: str = "fed bullard speech"
            """Fed Bullard Speech"""

            FED_CCAR_FOR_BIG_BANKS: str = "fed ccar for big banks"
            """Fed CCAR For Big Banks"""

            FED_CCAR_RESULTS_FOR_BIG_BANKS: str = "fed ccar results for big banks"
            """Fed CCAR Results For Big Banks"""

            FED_CHAIRMAN_BERNANKE_SPEAKS: str = "fed chairman bernanke speaks"
            """Fed Chairman Bernanke Speaks"""

            FED_CHAIRMAN_BERNANKE_SPEECH: str = "fed chairman bernanke speech"
            """Fed Chairman Bernanke Speech"""

            FED_CHAIRMAN_BERNANKE_TESTIFIES: str = "fed chairman bernanke testifies"
            """Fed Chairman Bernanke Testifies"""

            FED_CHAIRMAN_NOMINATION_VOTE: str = "fed chairman nomination vote"
            """Fed Chairman Nomination Vote"""

            FED_CHAIRMAN_YELLEN_SPEAKS: str = "fed chairman yellen speaks"
            """Fed Chairman Yellen Speaks"""

            FED_CHAIR_POWELL_SPEECH: str = "fed chair powell speech"
            """Fed Chair Powell Speech"""

            FED_CHAIR_POWELL_TESTIMONY: str = "fed chair powell testimony"
            """Fed Chair Powell Testimony"""

            FED_CHAIR_YELLEN_SPEAKS: str = "fed chair yellen speaks"
            """Fed Chair Yellen Speaks"""

            FED_CLARIDA_SPEECH: str = "fed clarida speech"
            """Fed Clarida Speech"""

            FED_DALY_SPEECH: str = "fed daly speech"
            """Fed Daly Speech"""

            FED_DUDLEY_SPEECH: str = "fed dudley speech"
            """Fed Dudley Speech"""

            FED_DUKE_SPEECH: str = "fed duke speech"
            """Fed Duke Speech"""

            FEDERAL_BUDGET_BALANCE: str = "federal budget balance"
            """Federal Budget Balance"""

            FED_EVANS_SPEAKS: str = "fed evans speaks"
            """Fed Evans Speaks"""

            FED_EVANS_SPEECH: str = "fed evans speech"
            """Fed Evans Speech"""

            FED_FISCHER_SPEECH: str = "fed fischer speech"
            """Fed Fischer Speech"""

            FED_GEORGE_SPEECH: str = "fed george speech"
            """Fed George Speech"""

            FED_GEORGE_TESTIMONY: str = "fed george testimony"
            """Fed George Testimony"""

            FED_HARKER_MESTER_AND_LOCKHART_SPEECH: str = "fed harker mester and lockhart speech"
            """Fed Harker, Mester & Lockhart Speech"""

            FED_HARKER_SPEECH: str = "fed harker speech"
            """Fed Harker Speech"""

            FED_INTEREST_RATE_DECISION: str = "fed interest rate decision"
            """Fed Interest Rate Decision"""

            FED_KAPLAN_SPEECH: str = "fed kaplan speech"
            """Fed Kaplan Speech"""

            FED_KASHKARI_SPEECH: str = "fed kashkari speech"
            """Fed Kashkari Speech"""

            FED_KOCHERLAKOTA_SPEECH: str = "fed kocherlakota speech"
            """Fed Kocherlakota Speech"""

            FED_LABOR_MARKET_CONDITIONS_INDEX_MO_M: str = "fed labor market conditions index mom"
            """Fed Labor Market Conditions Index (MoM)"""

            FED_LACKER_SPEECH: str = "fed lacker speech"
            """Fed Lacker Speech"""

            FED_LOCKHART_SPEECH: str = "fed lockhart speech"
            """Fed Lockhart speech"""

            FED_MEETING_UNDER_EXPEDITED_PROCEDURES: str = "fed meeting under expedited procedures"
            """Fed Meeting under Expedited Procedures"""

            FED_MESTER_SPEECH: str = "fed mester speech"
            """Fed Mester Speech"""

            FED_MONETARY_POLICY_STATEMENT_AND_PRESS_CONFERENCE: str = "fed monetary policy statement and press conference"
            """Fed Monetary Policy Statement and press conference"""

            FED_OPEN_BOARD_MEETING: str = "fed open board meeting"
            """Fed Open Board Meeting"""

            FED_PACE_OF_MORTGAGE_BACKED_SECURITIES_PURCHASE_PROGRAM: str = "fed pace of mortgage backed securities purchase program"
            """Fed Pace of MBS Purchase Program"""

            FED_PACE_OF_TREASURY_PURCHASE_PROGRAM: str = "fed pace of treasury purchase program"
            """Fed Pace of Treasury Purchase Program"""

            FED_POWELL_SPEECH: str = "fed powell speech"
            """Fed Powell Speech"""

            FED_PRESS_CONFERENCE: str = "fed press conference"
            """Fed press conference"""

            FED_QUARLES_SPEECH: str = "fed quarles speech"
            """Fed Quarles Speech"""

            FED_QUARLES_TESTIMONY: str = "fed quarles testimony"
            """Fed Quarles Testimony"""

            FED_RICHARD_FISHER_SPEECH: str = "fed richard fisher speech"
            """Fed Richard Fisher speech"""

            FED_ROSENGREN_SPEECH: str = "fed rosengren speech"
            """Fed Rosengren Speech"""

            FEDS_BEIGE_BOOK: str = "feds beige book"
            """FED´s Beige Book"""

            FED_STRESS_TEST_RESULTS_FOR_BIG_BANKS: str = "fed stress test results for big banks"
            """Fed Stress Test Results For Big Banks"""

            FED_TARULLO_SPEECH: str = "fed tarullo speech"
            """Fed Tarullo Speech"""

            FED_TARULLO_TESTIFIES: str = "fed tarullo testifies"
            """Fed Tarullo Testifies"""

            FED_WILLIAMS_SPEECH: str = "fed williams speech"
            """Fed Williams Speech"""

            FED_YELLEN_AND_IMFS_LAGARDE_SPEECH: str = "fed yellen and imfs lagarde speech"
            """Fed Yellen & IMF's Lagarde Speech"""

            FED_YELLEN_SPEAKS: str = "fed yellen speaks"
            """Fed Yellen Speaks"""

            FED_YELLEN_SPEAKS_AT_JACKSON_HOLE: str = "fed yellen speaks at jackson hole"
            """Fed Yellen Speaks At Jackson Hole"""

            FED_YELLEN_SPEECH: str = "fed yellen speech"
            """Fed Yellen Speech"""

            FED_YELLEN_TESTIFIES: str = "fed yellen testifies"
            """Fed Yellen testifies"""

            FED_YELLEN_TESTIMONY: str = "fed yellen testimony"
            """Fed Yellen Testimony"""

            FED_YELLEN_TESTIMONY_BEFORE_CONGRESS: str = "fed yellen testimony before congress"
            """Fed Yellen Testimony Before Congress"""

            FED_YELLEN_TESTIMONY_HFSC: str = "fed yellen testimony hfsc"
            """Fed Yellen Testimony HFSC"""

            FED_YELLEN_TESTIMONY_SBC: str = "fed yellen testimony sbc"
            """Fed Yellen Testimony SBC"""

            FED_YELLEN_TESTIMONY_TO_THE_CONGRESS: str = "fed yellen testimony to the congress"
            """Fed Yellen Testimony to the Congress"""

            FED_YELLEN_TESTIMONY_TO_THE_SENATE: str = "fed yellen testimony to the senate"
            """Fed Yellen Testimony to the Senate"""

            FED_YELLEN_TESTYMONY_HOUSE: str = "fed yellen testymony house"
            """Fed Yellen Testymony - House"""

            FED_YELLEN_TESTYMONY_SENATE: str = "fed yellen testymony senate"
            """Fed Yellen Testymony - Senate"""

            FIFTY_TWO_WEEK_BILL_AUCTION: str = "52 week bill auction"
            """52-Week Bill Auction"""

            FINANCIAL_ACCOUNTS_OF_THE_US: str = "financial accounts of the us"
            """Financial Accounts of the US"""

            FIVE_YEAR_NOTE_AUCTION: str = "5 year note auction"
            """5-Year Note Auction"""

            FIVE_YEAR_TIPS_AUCTION: str = "5 year tips auction"
            """5-Year TIPS Auction"""

            FOMC_ECONOMIC_PROJECTIONS: str = "fomc economic projections"
            """FOMC Economic Projections"""

            FOMC_MEMBER_YELLEN_SPEECH: str = "fomc member yellen speech"
            """FOMC Member Yellen Speech"""

            FOMC_MINUTES: str = "fomc minutes"
            """FOMC Minutes"""

            FOMC_POLICY_STATEMENT_AND_PRESS_CONFERENCE: str = "fomc policy statement and press conference"
            """FOMC Policy Statement and press conference"""

            FOMC_PRESS_CONFERENCE: str = "fomc press conference"
            """FOMC Press Conference"""

            FOREIGN_BOND_INVESTMENT: str = "foreign bond investment"
            """Foreign Bond Investment"""

            FOUR_WEEK_BILL_AUCTION: str = "4 week bill auction"
            """4-Week Bill Auction"""

            GASOLINE_INVENTORIES: str = "gasoline inventories"
            """Gasoline Inventories"""

            GDP_CONSUMER_SPENDING_QO_Q_ADV: str = "gdp consumer spending qoq adv"
            """GDP Consumer Spending QoQ Adv"""

            GDP_CONSUMER_SPENDING_QO_Q_FINAL: str = "gdp consumer spending qoq final"
            """GDP Consumer Spending QoQ Final"""

            GDP_CONSUMER_SPENDING_YO_Y: str = "gdp consumer spending yoy"
            """GDP Consumer Spending YoY"""

            GDP_DEFLATOR_QO_Q: str = "gdp deflator qoq"
            """GDP Deflator QoQ"""

            GDP_GROWTH_RATE: str = "gdp growth rate"
            """GDP Growth Rate"""

            GDP_GROWTH_RATE_QO_Q_ADV: str = "gdp growth rate qoq adv"
            """GDP Growth Rate QoQ Adv"""

            GDP_GROWTH_RATE_QO_Q_FINAL: str = "gdp growth rate qoq final"
            """GDP Growth Rate QoQ Final"""

            GDP_GROWTH_RATE_QO_Q_SECOND_ESTIMATE: str = "gdp growth rate qoq second estimate"
            """GDP Growth Rate QoQ 2nd Est"""

            GDP_GROWTH_RATE_SECOND_ESTIMATE: str = "gdp growth rate second estimate"
            """GDP Growth Rate 2nd Est"""

            GDP_GROWTH_RATE_YO_Y_ADV: str = "gdp growth rate yoy adv"
            """GDP Growth Rate YoY Adv"""

            GDP_GROWTH_RATE_YO_Y_SECOND_ESTIMATE: str = "gdp growth rate yoy second estimate"
            """GDP Growth Rate YoY Second Est"""

            GDP_GROWTH_RATE_YO_Y_THIRD_ESTIMATE: str = "gdp growth rate yoy third estimate"
            """GDP Growth Rate YoY Third Estimate"""

            GDP_PRICE_INDEX: str = "gdp price index"
            """GDP Price Index"""

            GDP_PRICE_INDEX_QO_Q: str = "gdp price index qoq"
            """GDP Price Index QoQ"""

            GDP_PRICE_INDEX_QO_Q_ADV: str = "gdp price index qoq adv"
            """GDP Price Index QoQ Adv"""

            GDP_PRICE_INDEX_QO_Q_FINAL: str = "gdp price index qoq final"
            """GDP Price Index QoQ Final"""

            GDP_PRICE_INDEX_QO_Q_SECOND_ESTIMATE: str = "gdp price index qoq second estimate"
            """GDP Price Index QoQ 2nd Est"""

            GOOD_FRIDAY: str = "good friday"
            """Good Friday"""

            GOODS_TRADE_BALANCE: str = "goods trade balance"
            """Goods Trade Balance"""

            GOODS_TRADE_BALANCE_ADV: str = "goods trade balance adv"
            """Goods Trade Balance Adv"""

            GOVERNMENT_PAYROLLS: str = "government payrolls"
            """Government Payrolls"""

            GROSS_DOMESTIC_PRODUCT_PRICE_INDEX: str = "gross domestic product price index"
            """Gross Domestic Product Price Index"""

            G_THIRTY_INTERNATIONAL_BANKING_SEMINAR: str = "g30 international banking seminar"
            """G30 International Banking Seminar"""

            G_TWENTY_FINANCE_MINISTERS_AND_CB_GOVERNORS_MEETING: str = "g20 finance ministers and cb governors meeting"
            """G20 Finance Ministers and CB Governors Meeting"""

            G_TWENTY_FIN_MINISTERS_AND_CB_GOVERNORS_MEETING: str = "g20 fin ministers and cb governors meeting"
            """G20 Fin Ministers and CB Governors Meeting"""

            G_TWENTY_MEETING: str = "g20 meeting"
            """G20 Meeting"""

            HOUSE_PRICE_INDEX_MO_M: str = "house price index mom"
            """House Price Index MoM"""

            HOUSE_PRICE_INDEX_YO_Y: str = "house price index yoy"
            """House Price Index YoY"""

            HOUSING_STARTS: str = "housing starts"
            """Housing Starts"""

            HOUSING_STARTS_MO_M: str = "housing starts mom"
            """Housing Starts MoM"""

            HSBC_SERVICES_PURCHASING_MANAGERS_INDEX: str = "hsbc services purchasing managers index"
            """HSBC Services PMI"""

            IBD_TIPP_ECONOMIC_OPTIMISM: str = "ibd tipp economic optimism"
            """IBD/TIPP Economic Optimism"""

            IEA_OIL_MARKET_REPORT: str = "iea oil market report"
            """IEA Oil Market Report"""

            IMF_MEETING: str = "imf meeting"
            """IMF Meeting"""

            IMF_SPRING_MEETING: str = "imf spring meeting"
            """IMF Spring Meeting"""

            IMF_WORLD_BANK_ANNUAL_MEETINGS: str = "imf world bank annual meetings"
            """IMF/World Bank Annual Meetings"""

            IMPORT_PRICES_MO_M: str = "import prices mom"
            """Import Prices MoM"""

            IMPORT_PRICES_YO_Y: str = "import prices yoy"
            """Import Prices YoY"""

            IMPORTS: str = "imports"
            """Imports"""

            INDEPENDENCE_DAY: str = "independence day"
            """Independence Day"""

            INDEPENDENCE_DAY_OBSERVED: str = "independence day observed"
            """Independence Day Observed"""

            INDUSTRIAL_PRODUCTION_MO_M: str = "industrial production mom"
            """Industrial Production MoM"""

            INDUSTRIAL_PRODUCTION_YO_Y: str = "industrial production yoy"
            """Industrial Production YoY"""

            INFLATION_RATE_MO_M: str = "inflation rate mom"
            """Inflation Rate MoM"""

            INFLATION_RATE_YO_Y: str = "inflation rate yoy"
            """Inflation Rate YoY"""

            INITIAL_JOBLESS_CLAIMS: str = "initial jobless claims"
            """Initial Jobless Claims"""

            ISM_MANUFACTURING_EMPLOYMENT: str = "ism manufacturing employment"
            """ISM Manufacturing Employment"""

            ISM_MANUFACTURING_NEW_ORDERS: str = "ism manufacturing new orders"
            """ISM Manufacturing New Orders"""

            ISM_MANUFACTURING_PRICES: str = "ism manufacturing prices"
            """ISM Manufacturing Prices"""

            ISM_MANUFACTURING_PRICES_PAID: str = "ism manufacturing prices paid"
            """ISM Manufacturing Prices Paid"""

            ISM_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "ism manufacturing purchasing managers index"
            """ISM Manufacturing PMI"""

            ISM_NEW_YORK_INDEX: str = "ism new york index"
            """ISM New York index"""

            ISM_NON_MANUFACTURING_BUSINESS_ACTIVITY: str = "ism non manufacturing business activity"
            """ISM Non-Manufacturing Business Activity"""

            ISM_NON_MANUFACTURING_EMPLOYMENT: str = "ism non manufacturing employment"
            """ISM Non-Manufacturing Employment"""

            ISM_NON_MANUFACTURING_NEW_ORDERS: str = "ism non manufacturing new orders"
            """ISM Non-Manufacturing New Orders"""

            ISM_NON_MANUFACTURING_PRICES: str = "ism non manufacturing prices"
            """ISM Non-Manufacturing Prices"""

            ISM_NON_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "ism non manufacturing purchasing managers index"
            """ISM Non-Manufacturing PMI"""

            ISM_PRICES_PAID: str = "ism prices paid"
            """ISM Prices Paid"""

            JACKSON_HOLE_ECONOMIC_POLICY_SYMPOSIUM: str = "jackson hole economic policy symposium"
            """Jackson Hole Economic Policy Symposium"""

            JACKSON_HOLE_SYMPOSIUM: str = "jackson hole symposium"
            """Jackson Hole Symposium"""

            JOLTS_JOB_OPENINGS: str = "jolts job openings"
            """JOLTs Job Openings"""

            KANSAS_FED_MANUFACTURING_INDEX: str = "kansas fed manufacturing index"
            """Kansas Fed Manufacturing Index"""

            LABOR_COSTS_INDEX_QO_Q: str = "labor costs index qoq"
            """Labor Costs QoQ"""

            LABOR_DAY: str = "labor day"
            """Labor Day"""

            LOAN_OFFICER_SURVEY: str = "loan officer survey"
            """Loan Officer Survey"""

            MANUFACTURING_PAYROLLS: str = "manufacturing payrolls"
            """Manufacturing Payrolls"""

            MANUFACTURING_PRODUCTION_MO_M: str = "manufacturing production mom"
            """Manufacturing Production MoM"""

            MANUFACTURING_PRODUCTION_YO_Y: str = "manufacturing production yoy"
            """Manufacturing Production YoY"""

            MARKIT_COMPOSITE_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit composite purchasing managers index final"
            """Markit Composite PMI Final"""

            MARKIT_COMPOSITE_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit composite purchasing managers index flash"
            """Markit Composite PMI Flash"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX: str = "markit manufacturing purchasing managers index"
            """Markit Manufacturing PMI"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit manufacturing purchasing managers index final"
            """Markit Manufacturing PMI Final"""

            MARKIT_MANUFACTURING_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit manufacturing purchasing managers index flash"
            """Markit Manufacturing PMI Flash"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX_FINAL: str = "markit services purchasing managers index final"
            """Markit Services PMI Final"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX_FLASH: str = "markit services purchasing managers index flash"
            """Markit Services PMI Flash"""

            MARKIT_SERVICES_PURCHASING_MANAGERS_INDEX_PRELIMINARY: str = "markit services purchasing managers index preliminary"
            """Markit Services PMI Prel"""

            MARTIN_L_KING_DAY: str = "martin l king day"
            """Martin L. King Day"""

            MARTIN_L_KINGS_BIRTHDAY: str = "martin l kings birthday"
            """Martin L. King's Birthday"""

            MARTIN_LUTHER_KING_JR_DAY: str = "martin luther king jr day"
            """Martin Luther King, Jr. Day"""

            MASS_LAYOFFS: str = "mass layoffs"
            """Mass Layoffs"""

            MBA_MORTGAGE_APPLICATIONS: str = "mba mortgage applications"
            """MBA Mortgage Applications"""

            MBA_MORTGAGE_APPLICATIONS_WO_W: str = "mba mortgage applications wow"
            """MBA Mortgage Applications WoW"""

            MBA_THIRTY_YEAR_MORTGAGE_RATE: str = "mba 30 year mortgage rate"
            """MBA 30-Year Mortgage Rate"""

            MEMORIAL_DAY: str = "memorial day"
            """Memorial Day"""

            MEMORIAL_DAY_HOLIDAY: str = "memorial day holiday"
            """Memorial Day Holiday"""

            MICHIGAN_CONSUMER_EXPECTATIONS_FINAL: str = "michigan consumer expectations final"
            """Michigan Consumer Expectations Final"""

            MICHIGAN_CONSUMER_EXPECTATIONS_PRELIMINARY: str = "michigan consumer expectations preliminary"
            """Michigan Consumer Expectations Prel"""

            MICHIGAN_CONSUMER_SENTIMENT_FINAL: str = "michigan consumer sentiment final"
            """Michigan Consumer Sentiment Final"""

            MICHIGAN_CONSUMER_SENTIMENT_PRELIMINARY: str = "michigan consumer sentiment preliminary"
            """Michigan Consumer Sentiment Prel"""

            MICHIGAN_CURRENT_CONDITIONS_FINAL: str = "michigan current conditions final"
            """Michigan Current Conditions Final"""

            MICHIGAN_CURRENT_CONDITIONS_PRELIMINARY: str = "michigan current conditions preliminary"
            """Michigan Current Conditions Prel"""

            MICHIGAN_FIVE_YEAR_INFLATION_EXPECTATIONS_FINAL: str = "michigan 5 year inflation expectations final"
            """Michigan 5 Year Inflation Expectations Final"""

            MICHIGAN_FIVE_YEAR_INFLATION_EXPECTATIONS_PRELIMINARY: str = "michigan 5 year inflation expectations preliminary"
            """Michigan 5 Year Inflation Expectations Prel"""

            MICHIGAN_INFLATION_EXPECTATIONS_FINAL: str = "michigan inflation expectations final"
            """Michigan Inflation Expectations Final"""

            MICHIGAN_INFLATION_EXPECTATIONS_PRELIMINARY: str = "michigan inflation expectations preliminary"
            """Michigan Inflation Expectations Prel"""

            MIDTERM_ELECTIONS: str = "midterm elections"
            """Midterm Elections"""

            MID_TERM_ELECTIONS: str = "mid term elections"
            """Mid-Term Elections"""

            MONETARY_POLICY_REPORT: str = "monetary policy report"
            """Monetary Policy Report"""

            MONTHLY_BUDGET_STATEMENT: str = "monthly budget statement"
            """Monthly Budget Statement"""

            NAHB_HOUSING_MARKET_INDEX: str = "nahb housing market index"
            """NAHB Housing Market Index"""

            NATIONAL_ACTIVITY_INDEX: str = "national activity index"
            """National activity index"""

            NET_LONG_TERM_TIC_FLOWS: str = "net long term tic flows"
            """Net Long-Term Tic Flows"""

            NEW_HOME_SALES: str = "new home sales"
            """New Home Sales"""

            NEW_HOME_SALES_MO_M: str = "new home sales mom"
            """New Home Sales MoM"""

            NEW_YEARS_DAY: str = "new years day"
            """New Year's Day"""

            NEW_YEARS_DAY_SUBSTITUTE_DAY: str = "new years day substitute day"
            """New Year's Day (Substitute Day)"""

            NFIB_BUSINESS_OPTIMISM_INDEX: str = "nfib business optimism index"
            """NFIB Business Optimism Index"""

            NON_FARM_PAYROLLS: str = "non farm payrolls"
            """Non Farm Payrolls"""

            NON_FARM_PAYROLLS_PRIVATE: str = "non farm payrolls private"
            """Nonfarm Payrolls Private"""

            NON_FARM_PRODUCTIVITY_QO_Q: str = "non farm productivity qoq"
            """Nonfarm Productivity QoQ"""

            NON_FARM_PRODUCTIVITY_QO_Q_FINAL: str = "non farm productivity qoq final"
            """Nonfarm Productivity QoQ Final"""

            NON_FARM_PRODUCTIVITY_QO_Q_PRELIMINARY: str = "non farm productivity qoq preliminary"
            """Nonfarm Productivity QoQ Prel"""

            NON_FARM_PRODUCTIVITY_YO_Y: str = "non farm productivity yoy"
            """Nonfarm Productivity YoY"""

            NON_MANUFACTURING_BUSINESS_ACTIVITY: str = "non manufacturing business activity"
            """Non-Manufacturing Business Activity"""

            NY_EMPIRE_STATE_MANUFACTURING_INDEX: str = "ny empire state manufacturing index"
            """NY Empire State Manufacturing Index"""

            OBAMACARE_REPEAL_VOTE_PULLED: str = "obamacare repeal vote pulled"
            """Obamacare Repeal Vote - Pulled"""

            OVERALL_NET_CAPITAL_FLOWS: str = "overall net capital flows"
            """Overall Net Capital Flows"""

            PARTICIPATION_RATE: str = "participation rate"
            """Participation Rate"""

            PENDING_HOME_SALES_MO_M: str = "pending home sales mom"
            """Pending Home Sales MoM"""

            PENDING_HOME_SALES_YO_Y: str = "pending home sales yoy"
            """Pending Home Sales YoY"""

            PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_MO_M: str = "personal consumption expenditure price index mom"
            """PCE Price Index MoM"""

            PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q: str = "personal consumption expenditure price index qoq"
            """PCE Prices QoQ"""

            PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q_ADV: str = "personal consumption expenditure price index qoq adv"
            """PCE Prices QoQ Adv"""

            PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q_FINAL: str = "personal consumption expenditure price index qoq final"
            """PCE Prices QoQ Final"""

            PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_QO_Q_SECOND_ESTIMATE: str = "personal consumption expenditure price index qoq second estimate"
            """PCE Prices QoQ 2 Est"""

            PERSONAL_CONSUMPTION_EXPENDITURE_PRICE_INDEX_YO_Y: str = "personal consumption expenditure price index yoy"
            """PCE Price Index YoY"""

            PERSONAL_INCOME_MO_M: str = "personal income mom"
            """Personal Income (MoM)"""

            PERSONAL_SPENDING_MO_M: str = "personal spending mom"
            """Personal Spending MoM"""

            PHILADELPHIA_FED_MANUFACTURING_INDEX: str = "philadelphia fed manufacturing index"
            """Philadelphia Fed Manufacturing Index"""

            PHILADELPHIA_FED_PLOSSER_SPEECH: str = "philadelphia fed plosser speech"
            """Philadelphia Fed Plosser speech"""

            PRESIDENT_ELECT_TRUMP_SPEECH: str = "president elect trump speech"
            """President-Elect Trump Speech"""

            PRESIDENTIAL_ELECTION_RESULTS: str = "presidential election results"
            """Presidential Election Results"""

            PRESIDENTIAL_ELECTIONS: str = "presidential elections"
            """Presidential Elections"""

            PRESIDENT_OBAMA_SPEECH: str = "president obama speech"
            """President Obama Speech"""

            PRESIDENT_OBAMA_STATEMENT_ON_THE_ECONOMY: str = "president obama statement on the economy"
            """President Obama Statement on the Economy"""

            PRESIDENTS_DAY: str = "presidents day"
            """President's Day"""

            PRESIDENT_TRUMP_AND_PRESIDENT_XI_JINPING_MEETING: str = "president trump and president xi jinping meeting"
            """President Trump and President Xi Jinping Meeting"""

            PRESIDENT_TRUMP_SPEECH: str = "president trump speech"
            """President Trump Speech"""

            PRESIDENT_TRUMP_SPEECH_ON_IRAN_DEAL: str = "president trump speech on iran deal"
            """President Trump Speech on Iran Deal"""

            PRESIDENT_TRUMP_STATE_OF_THE_UNION_SPEECH: str = "president trump state of the union speech"
            """President Trump State of the Union Speech"""

            PRESIDENT_TRUMP_TAX_SPEECH: str = "president trump tax speech"
            """President Trump tax speech"""

            PRODUCER_PRICE_INDEX_EXCLUDING_FOOD_AND_ENERGY_MO_M: str = "producer price index excluding food and energy mom"
            """Producer Price Index ex Food & Energy (MoM)"""

            PRODUCER_PRICE_INDEX_EXCLUDING_FOOD_AND_ENERGY_YO_Y: str = "producer price index excluding food and energy yoy"
            """Producer Price Index ex Food & Energy (YoY)"""

            PRODUCER_PRICE_INDEX_MO_M: str = "producer price index mom"
            """PPI MoM"""

            PRODUCER_PRICE_INDEX_YO_Y: str = "producer price index yoy"
            """PPI YoY"""

            QUANTITATIVE_EASING_MORTGAGE_BACKED_SECURITIES: str = "quantitative easing mortgage backed securities"
            """QE MBS"""

            QUANTITATIVE_EASING_TOTAL: str = "quantitative easing total"
            """QE total"""

            QUANTITATIVE_EASING_TREASURIES: str = "quantitative easing treasuries"
            """QE Treasuries"""

            REAL_CONSUMER_SPENDING: str = "real consumer spending"
            """Real Consumer Spending"""

            REDBOOK_MO_M: str = "redbook mom"
            """Redbook MoM"""

            REDBOOK_YO_Y: str = "redbook yoy"
            """Redbook YoY"""

            RETAIL_SALES_EXCLUDING_AUTOS_MO_M: str = "retail sales excluding autos mom"
            """Retail Sales Ex Autos MoM"""

            RETAIL_SALES_EXCLUDING_GAS_AUTOS_MO_M: str = "retail sales excluding gas autos mom"
            """Retail Sales Ex Gas/Autos  MoM"""

            RETAIL_SALES_MO_M: str = "retail sales mom"
            """Retail Sales MoM"""

            RETAIL_SALES_YO_Y: str = "retail sales yoy"
            """Retail Sales YoY"""

            REUTERS_MICHIGAN_CONSUMER_EXPECTATIONS: str = "reuters michigan consumer expectations"
            """Reuters Michigan Consumer Expectations"""

            REUTERS_MICHIGAN_CONSUMER_EXPECTATIONS_FINAL: str = "reuters michigan consumer expectations final"
            """Reuters Michigan Consumer Expectations Final"""

            REUTERS_MICHIGAN_CONSUMER_EXPECTATIONS_PRELIMINARY: str = "reuters michigan consumer expectations preliminary"
            """Reuters Michigan Consumer Expectations Prel"""

            REUTERS_MICHIGAN_CONSUMER_SENTIMENT_FINAL: str = "reuters michigan consumer sentiment final"
            """Reuters Michigan Consumer Sentiment Final"""

            REUTERS_MICHIGAN_CONSUMER_SENTIMENT_INDEX: str = "reuters michigan consumer sentiment index"
            """Reuters/Michigan Consumer Sentiment Index"""

            REUTERS_MICHIGAN_CONSUMER_SENTIMENT_PRELIMINARY: str = "reuters michigan consumer sentiment preliminary"
            """Reuters Michigan Consumer Sentiment  Prel"""

            REUTERS_MICHIGAN_CURRENT_CONDITIONS: str = "reuters michigan current conditions"
            """Reuters Michigan Current Conditions"""

            REUTERS_MICHIGAN_CURRENT_CONDITIONS_FINAL: str = "reuters michigan current conditions final"
            """Reuters Michigan Current Conditions Final"""

            REUTERS_MICHIGAN_CURRENT_CONDITIONS_PRELIMINARY: str = "reuters michigan current conditions preliminary"
            """Reuters Michigan Current Conditions Prel"""

            REUTERS_MICHIGAN_INFLATION_EXPECTATIONS_PRELIMINARY: str = "reuters michigan inflation expectations preliminary"
            """Reuters Michigan Inflation Expectations Prel"""

            RICHMOND_FED_MANUFACTURING_INDEX: str = "richmond fed manufacturing index"
            """Richmond Fed Manufacturing Index"""

            SANDP_CASE_SHILLER_HOME_PRICE_MO_M: str = "sandp case shiller home price mom"
            """S&P/Case-Shiller Home Price MoM"""

            SANDP_CASE_SHILLER_HOME_PRICE_YO_Y: str = "sandp case shiller home price yoy"
            """S&P/Case-Shiller Home Price YoY"""

            SEVEN_YEAR_NOTE_AUCTION: str = "7 year note auction"
            """7-Year Note Auction"""

            SIX_MONTH_BILL_AUCTION: str = "6 month bill auction"
            """6-Month Bill Auction"""

            SPRING_MEETING_OF_THE_WORLD_BANK_GROUP_IMF: str = "spring meeting of the world bank group imf"
            """Spring Meeting of the World Bank Group-IMF"""

            TEN_YEAR_NOTE_AUCTION: str = "10 year note auction"
            """10-Year Note Auction"""

            TEN_YEAR_TIPS_AUCTION: str = "10 year tips auction"
            """10-Year TIPS Auction"""

            THANKSGIVING_DAY: str = "thanksgiving day"
            """Thanksgiving Day"""

            THIRTY_YEAR_BOND_AUCTION: str = "30 year bond auction"
            """30-Year Bond Auction"""

            THIRTY_YEAR_NOTE_AUCTION: str = "30 year note auction"
            """30-Year Note Auction"""

            THREE_MONTH_BILL_AUCTION: str = "3 month bill auction"
            """3-Month Bill Auction"""

            THREE_YEAR_NOTE_AUCTION: str = "3 year note auction"
            """3-Year Note Auction"""

            TOTAL_NET_TIC_FLOWS: str = "total net tic flows"
            """Total Net TIC Flows"""

            TOTAL_VEHICLE_SALES: str = "total vehicle sales"
            """Total Vehicle Sales"""

            TREASURY_SEC_LEW_SPEAKS: str = "treasury sec lew speaks"
            """Treasury Sec Lew Speaks"""

            TREASURY_SECRETARY_LEW_SPEAKS: str = "treasury secretary lew speaks"
            """Treasury Secretary Lew Speaks"""

            TREASURY_SECRETARY_MNUCHIN_SPEECH: str = "treasury secretary mnuchin speech"
            """Treasury Secretary Mnuchin Speech"""

            TWO_THOUSAND_NINETEEN_US_MONETARY_POLICY_FORUM: str = "2019 us monetary policy forum"
            """2019 US Monetary Policy Forum"""

            TWO_YEAR_FRN_AUCTION: str = "2 year frn auction"
            """2-Year FRN Auction"""

            TWO_YEAR_NOTE_AUCTION: str = "2 year note auction"
            """2-Year Note Auction"""

            UNEMPLOYMENT_RATE: str = "unemployment rate"
            """Unemployment Rate"""

            UN_GENERAL_ASSEMBLY: str = "un general assembly"
            """UN General Assembly"""

            UNIT_LABOR_COSTS_INDEX_QO_Q: str = "unit labor costs index qoq"
            """Unit Labor Costs QoQ"""

            UNIT_LABOR_COSTS_INDEX_QO_Q_FINAL: str = "unit labor costs index qoq final"
            """Unit Labor Costs QoQ Final"""

            UNIT_LABOR_COSTS_INDEX_QO_Q_PRELIMINARY: str = "unit labor costs index qoq preliminary"
            """Unit Labor Costs QoQ Prel"""

            UNIT_LABOR_COSTS_YO_Y: str = "unit labor costs yoy"
            """Unit Labor Costs YoY"""

            US_CHINA_PHASE_ONE_TRADE_DEAL_SIGNATURE: str = "us china phase 1 trade deal signature"
            """US-China Phase 1 Trade Deal Signature"""

            US_CHINA_TRADE_TALKS: str = "us china trade talks"
            """US-China Trade Talks"""

            US_GOV_TEMPORARY_FUNDING_EXPIRES: str = "us gov temporary funding expires"
            """US Gov Temporary Funding Expires"""

            USMCA_TRADE_DEAL_SIGNATURE: str = "usmca trade deal signature"
            """USMCA Trade Deal Signature"""

            US_MEXICO_TRADE_TALKS: str = "us mexico trade talks"
            """US-Mexico Trade Talks"""

            US_MONETARY_POLICY_FORUM: str = "us monetary policy forum"
            """US Monetary Policy Forum"""

            US_NORTH_KOREA_SUMMIT: str = "us north korea summit"
            """US-North Korea Summit"""

            US_RUSSIA_SUMMIT: str = "us russia summit"
            """US-Russia Summit"""

            VETERANS_DAY: str = "veterans day"
            """Veterans Day"""

            VETERANS_DAY_SUBSTITUTE_DAY: str = "veterans day substitute day"
            """Veterans Day (Substitute Day)"""

            WASDE_REPORT: str = "wasde report"
            """WASDE Report"""

            WASHINGTONS_BIRTHDAY: str = "washingtons birthday"
            """Washington's Birthday"""

            WHITE_HOUSE_JOBS_ANNOUNCEMENT: str = "white house jobs announcement"
            """White House Jobs Announcement"""

            WHOLESALE_INVENTORIES_MO_M: str = "wholesale inventories mom"
            """Wholesale Inventories MoM"""

            WHOLESALE_INVENTORIES_MO_M_ADV: str = "wholesale inventories mom adv"
            """Wholesale Inventories MoM Adv"""

    class Calendar(System.Object):
        """Calendar group"""

        class Australia(System.Object):
            """Australia"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUILDING_PERMITS: str = ...
            """Building Permits"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            BUSINESS_INVENTORIES: str = ...
            """Business Inventories"""

            CALENDAR: str = ...
            """Calendar"""

            CAR_REGISTRATIONS: str = ...
            """Car Registrations"""

            COMPOSITE_PMI: str = ...
            """Composite Pmi"""

            CONSTRUCTION_OUTPUT: str = ...
            """Construction Output"""

            CONSTRUCTION_PMI: str = ...
            """Construction Pmi"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CONSUMER_PRICE_INDEX_CPI: str = ...
            """Consumer Price Index (CPI)"""

            CONSUMER_SPENDING: str = ...
            """Consumer Spending"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CORPORATE_PROFITS: str = ...
            """Corporate Profits"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EMPLOYMENT_CHANGE: str = ...
            """Employment Change"""

            EXPORT_PRICES: str = ...
            """Export Prices"""

            EXPORTS: str = ...
            """Exports"""

            FULL_TIME_EMPLOYMENT: str = ...
            """Full Time Employment"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_DEFLATOR: str = ...
            """GDP Deflator"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GROSS_FIXED_CAPITAL_FORMATION: str = ...
            """Gross Fixed Capital Formation"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOME_LOANS: str = ...
            """Home Loans"""

            HOUSING_INDEX: str = ...
            """Housing Index"""

            IMPORT_PRICES: str = ...
            """Import Prices"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_SENTIMENT: str = ...
            """Industrial Sentiment"""

            INFLATION_EXPECTATIONS: str = ...
            """Inflation Expectations"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            JOB_ADVERTISEMENTS: str = ...
            """Job Advertisements"""

            LABOR_FORCE_PARTICIPATION_RATE: str = ...
            """Labor Force Participation Rate"""

            LEADING_ECONOMIC_INDEX: str = ...
            """Leading Economic Index"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            NEW_HOME_SALES: str = ...
            """New Home Sales"""

            PART_TIME_EMPLOYMENT: str = ...
            """Part Time Employment"""

            PRIVATE_INVESTMENT: str = ...
            """Private Investment"""

            PRIVATE_SECTOR_CREDIT: str = ...
            """Private Sector Credit"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            SERVICES_SENTIMENT: str = ...
            """Services Sentiment"""

            TOTAL_VEHICLE_SALES: str = ...
            """Total Vehicle Sales"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

        class Austria(System.Object):
            """Austria"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYED_PERSONS: str = ...
            """Unemployed Persons"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WHOLESALE_PRICES: str = ...
            """Wholesale Prices"""

        class Belgium(System.Object):
            """Belgium"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Canada(System.Object):
            """Canada"""

            ADP_EMPLOYMENT_CHANGE: str = ...
            """Adp Employment Change"""

            AVERAGE_HOURLY_EARNINGS: str = ...
            """Average Hourly Earnings"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUILDING_PERMITS: str = ...
            """Building Permits"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CAPACITY_UTILIZATION: str = ...
            """Capacity Utilization"""

            CAR_REGISTRATIONS: str = ...
            """Car Registrations"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EMPLOYMENT_CHANGE: str = ...
            """Employment Change"""

            EXPORTS: str = ...
            """Exports"""

            FOREIGN_STOCK_INVESTMENT: str = ...
            """Foreign Stock Investment"""

            FULL_TIME_EMPLOYMENT: str = ...
            """Full Time Employment"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_DEFLATOR: str = ...
            """GDP Deflator"""

            GDP_GROWTH_ANNUALIZED: str = ...
            """Gdp Growth Annualized"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BUDGET_VALUE: str = ...
            """Government Budget Value"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOUSING_INDEX: str = ...
            """Housing Index"""

            HOUSING_STARTS: str = ...
            """Housing Starts"""

            IMPORTS: str = ...
            """Imports"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            JOB_VACANCIES: str = ...
            """Job Vacancies"""

            LABOR_FORCE_PARTICIPATION_RATE: str = ...
            """Labor Force Participation Rate"""

            LEADING_ECONOMIC_INDEX: str = ...
            """Leading Economic Index"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing PMI"""

            MANUFACTURING_SALES: str = ...
            """Manufacturing Sales"""

            PART_TIME_EMPLOYMENT: str = ...
            """Part Time Employment"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            PRODUCTIVITY: str = ...
            """Productivity"""

            RETAIL_SALES_EX_AUTOS: str = ...
            """Retail Sales Ex Autos"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

            WHOLESALE_PRICES: str = ...
            """Wholesale Prices"""

            WHOLESALE_SALES: str = ...
            """Wholesale Sales"""

        class China(System.Object):
            """China"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BANKS_BALANCE_SHEET: str = ...
            """Banks Balance Sheet"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CAPACITY_UTILIZATION: str = ...
            """Capacity Utilization"""

            CAPITAL_FLOWS: str = ...
            """Capital Flows"""

            COMPOSITE_PMI: str = ...
            """Composite Pmi"""

            CORPORATE_PROFITS: str = ...
            """Corporate Profits"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EXPORTS: str = ...
            """Exports"""

            FIXED_ASSET_INVESTMENT: str = ...
            """Fixed Asset Investment"""

            FOREIGN_DIRECT_INVESTMENT: str = ...
            """Foreign Direct Investment"""

            FOREIGN_EXCHANGE_RESERVES: str = ...
            """Foreign Exchange Reserves"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOUSING_INDEX: str = ...
            """Housing Index"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            LOAN_GROWTH: str = ...
            """Loan Growth"""

            LOANS_TO_PRIVATE_SECTOR: str = ...
            """Loans to Private Sector"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            MNI_BUSINESS_SENTIMENT: str = ...
            """Mni Business Sentiment"""

            MNI_CONSUMER_SENTIMENT: str = ...
            """Mni Consumer Sentiment"""

            MONEY_SUPPLY_M_TWO: str = ...
            """Money Supply M2"""

            NON_MANUFACTURING_PMI: str = ...
            """Non Manufacturing Pmi"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            TOTAL_VEHICLE_SALES: str = ...
            """Total Vehicle Sales"""

        class Cyprus(System.Object):
            """Cyprus"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSTRUCTION_OUTPUT: str = ...
            """Construction Output"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

        class Estonia(System.Object):
            """Estonia"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Finland(System.Object):
            """Finland"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EXPORT_PRICES: str = ...
            """Export Prices"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            IMPORT_PRICES: str = ...
            """Import Prices"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            LEADING_ECONOMIC_INDEX: str = ...
            """Leading Economic Index"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales Mom"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales Yoy"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class France(System.Object):
            """France"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            COMPOSITE_PMI: str = ...
            """Composite Pmi"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            FIFTY_TWO_WEEK_BILL_YIELD: str = ...
            """52 Week Bill Yield"""

            FIVE_YEAR_NOTE_YIELD: str = ...
            """5 Year Note Yield"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            GOVERNMENT_BUDGET_VALUE: str = ...
            """Government Budget Value"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INITIAL_JOBLESS_CLAIMS: str = ...
            """Initial Jobless Claims"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            NON_FARM_PAYROLLS: str = ...
            """Non Farm Payrolls"""

            NONFARM_PAYROLLS_PRIVATE: str = ...
            """Nonfarm Payrolls Private"""

            PERSONAL_SPENDING: str = ...
            """Personal Spending"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            SIX_MONTH_BILL_YIELD: str = ...
            """6 Month Bill Yield"""

            THREE_MONTH_BILL_YIELD: str = ...
            """3 Month Bill Yield"""

            THREE_YEAR_NOTE_YIELD: str = ...
            """3 Year Note Yield"""

            UNEMPLOYED_PERSONS: str = ...
            """Unemployed Persons"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Germany(System.Object):
            """Germany"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            COMPOSITE_PMI: str = ...
            """Composite Pmi"""

            CONSTRUCTION_PMI: str = ...
            """Construction Pmi"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EMPLOYED_PERSONS: str = ...
            """Employed Persons"""

            EXPORTS: str = ...
            """Exports"""

            FACTORY_ORDERS: str = ...
            """Factory Orders"""

            FIFTY_TWO_WEEK_BILL_YIELD: str = ...
            """52 Week Bill Yield"""

            FIVE_YEAR_NOTE_YIELD: str = ...
            """5 Year Note Yield"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            GOVERNMENT_BUDGET: str = ...
            """Government Budget"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            IMPORT_PRICES: str = ...
            """Import Prices"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            JOB_VACANCIES: str = ...
            """Job Vacancies"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            THIRTY_YEAR_BOND_YIELD: str = ...
            """30 Year Bond Yield"""

            TWO_YEAR_NOTE_YIELD: str = ...
            """2 Year Note Yield"""

            UNEMPLOYED_PERSONS: str = ...
            """Unemployed Persons"""

            UNEMPLOYMENT_CHANGE: str = ...
            """Unemployment Change"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WHOLESALE_PRICES: str = ...
            """Wholesale Prices"""

            ZEW_ECONOMIC_SENTIMENT_INDEX: str = ...
            """Zew Economic Sentiment Index"""

        class Greece(System.Object):
            """Greece"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSTRUCTION_OUTPUT: str = ...
            """Construction Output"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            LOAN_GROWTH: str = ...
            """Loan Growth"""

            LOANS_TO_PRIVATE_SECTOR: str = ...
            """Loans to Private Sector"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            PRIVATE_SECTOR_CREDIT: str = ...
            """Private Sector Credit"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SIX_MONTH_BILL_YIELD: str = ...
            """6 Month Bill Yield"""

            THREE_MONTH_BILL_YIELD: str = ...
            """3 Month Bill Yield"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Ireland(System.Object):
            """Ireland"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            CALENDAR: str = ...
            """Calendar"""

            CONSTRUCTION_OUTPUT: str = ...
            """Construction Output"""

            CONSTRUCTION_PMI: str = ...
            """Construction Pmi"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GROSS_NATIONAL_PRODUCT: str = ...
            """Gross National Product"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOUSING_INDEX: str = ...
            """Housing Index"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            PERSONAL_SAVINGS: str = ...
            """Personal Savings"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

        class Italy(System.Object):
            """Italy"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSTRUCTION_OUTPUT: str = ...
            """Construction Output"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            FACTORY_ORDERS: str = ...
            """Factory Orders"""

            FIFTY_TWO_WEEK_BILL_YIELD: str = ...
            """52 Week Bill Yield"""

            FIVE_YEAR_NOTE_YIELD: str = ...
            """5 Year Note Yield"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            GOVERNMENT_BUDGET: str = ...
            """Government Budget"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            MANUFACTURING_SALES: str = ...
            """Manufacturing Sales"""

            NEW_ORDERS: str = ...
            """New Orders"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            SEVEN_YEAR_NOTE_YIELD: str = ...
            """7 Year Note Yield"""

            SIX_MONTH_BILL_YIELD: str = ...
            """6 Month Bill Yield"""

            THIRTY_YEAR_BOND_YIELD: str = ...
            """30 Year Bond Yield"""

            THREE_YEAR_NOTE_YIELD: str = ...
            """3 Year Note Yield"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

        class Japan(System.Object):
            """Japan"""

            ALL_INDUSTRY_ACTIVITY_INDEX: str = ...
            """All Industry Activity Index"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CAPACITY_UTILIZATION: str = ...
            """Capacity Utilization"""

            COINCIDENT_INDEX: str = ...
            """Coincident Index"""

            COMPOSITE_PMI: str = ...
            """Composite Pmi"""

            CONSTRUCTION_ORDERS: str = ...
            """Construction Orders"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CONSUMER_SPENDING: str = ...
            """Consumer Spending"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            ECONOMY_WATCHERS_SURVEY: str = ...
            """Economy Watchers Survey"""

            EXPORTS: str = ...
            """Exports"""

            FOREIGN_BOND_INVESTMENT: str = ...
            """Foreign Bond Investment"""

            FOREIGN_EXCHANGE_RESERVES: str = ...
            """Foreign Exchange Reserves"""

            FOREIGN_STOCK_INVESTMENT: str = ...
            """Foreign Stock Investment"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_DEFLATOR: str = ...
            """GDP Deflator"""

            GDP_GROWTH_ANNUALIZED: str = ...
            """Gdp Growth Annualized"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            GROSS_FIXED_CAPITAL_FORMATION: str = ...
            """Gross Fixed Capital Formation"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOUSEHOLD_SPENDING: str = ...
            """Household Spending"""

            HOUSING_STARTS: str = ...
            """Housing Starts"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            JOBS_TO_APPLICATIONS_RATIO: str = ...
            """Jobs To Applications Ratio"""

            LEADING_COMPOSITE_INDEX: str = ...
            """Leading Composite Index"""

            LEADING_ECONOMIC_INDEX: str = ...
            """Leading Economic Index"""

            LOAN_GROWTH: str = ...
            """Loan Growth"""

            MACHINERY_ORDERS: str = ...
            """Machinery Orders"""

            MACHINE_TOOL_ORDERS: str = ...
            """Machine Tool Orders"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            NON_MANUFACTURING_PMI: str = ...
            """Non Manufacturing Pmi"""

            PRIVATE_INVESTMENT: str = ...
            """Private Investment"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            REUTERS_TANKAN_INDEX: str = ...
            """Reuters Tankan Index"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            SMALL_BUSINESS_SENTIMENT: str = ...
            """Small Business Sentiment"""

            TERTIARY_INDUSTRY_INDEX: str = ...
            """Tertiary Industry Index"""

            THIRTY_YEAR_BOND_YIELD: str = ...
            """30 Year Bond Yield"""

            TOKYO_CPI: str = ...
            """Tokyo Cpi"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

        class Latvia(System.Object):
            """Latvia"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            CALENDAR: str = ...
            """Calendar"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Lithuania(System.Object):
            """Lithuania"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Luxembourg(System.Object):
            """Luxembourg"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales Mom"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Malta(System.Object):
            """Malta"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Netherlands(System.Object):
            """Netherlands"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            MANUFACTURING_PRODUCTION: str = ...
            """Manufacturing Production"""

            PERSONAL_SPENDING: str = ...
            """Personal Spending"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SIX_MONTH_BILL_YIELD: str = ...
            """6 Month Bill Yield"""

            THREE_MONTH_BILL_YIELD: str = ...
            """3 Month Bill Yield"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class NewZealand(System.Object):
            """New Zealand"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUILDING_PERMITS: str = ...
            """Building Permits"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CAPACITY_UTILIZATION: str = ...
            """Capacity Utilization"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CREDIT_CARD_SPENDING: str = ...
            """Credit Card Spending"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EMPLOYMENT_CHANGE: str = ...
            """Employment Change"""

            EXPORT_PRICES: str = ...
            """Export Prices"""

            EXPORTS: str = ...
            """Exports"""

            FOOD_INFLATION: str = ...
            """Food Inflation"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GLOBAL_DAIRY_TRADE_PRICE_INDEX: str = ...
            """Global Dairy Trade Price Index"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOUSING_INDEX: str = ...
            """Housing Index"""

            IMPORT_PRICES: str = ...
            """Import Prices"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_EXPECTATIONS: str = ...
            """Inflation Expectations"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            LABOR_FORCE_PARTICIPATION_RATE: str = ...
            """Labor Force Participation Rate"""

            LABOUR_COSTS: str = ...
            """Labour Costs"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            TERMS_OF_TRADE: str = ...
            """Terms of Trade"""

            TOURIST_ARRIVALS: str = ...
            """Tourist Arrivals"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Portugal(System.Object):
            """Portugal"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EXPORTS: str = ...
            """Exports"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BUDGET_VALUE: str = ...
            """Government Budget Value"""

            HOLIDAYS: str = ...
            """Holidays"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            LEADING_ECONOMIC_INDEX: str = ...
            """Leading Economic Index"""

            PERSONAL_SPENDING: str = ...
            """Personal Spending"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Slovakia(System.Object):
            """Slovakia"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSTRUCTION_OUTPUT: str = ...
            """Construction Output"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CORE_CONSUMER_PRICES: str = ...
            """Core Consumer Prices"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            EXPORTS: str = ...
            """Exports"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

        class Slovenia(System.Object):
            """Slovenia"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            TOURIST_ARRIVALS: str = ...
            """Tourist Arrivals"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Spain(System.Object):
            """Spain"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            FACTORY_ORDERS: str = ...
            """Factory Orders"""

            FIFTY_TWO_WEEK_BILL_YIELD: str = ...
            """52 Week Bill Yield"""

            FIVE_YEAR_NOTE_YIELD: str = ...
            """5 Year Note Yield"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            HARMONISED_CONSUMER_PRICES: str = ...
            """Harmonised Consumer Prices"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            SIX_MONTH_BILL_YIELD: str = ...
            """6 Month Bill Yield"""

            THREE_MONTH_BILL_YIELD: str = ...
            """3 Month Bill Yield"""

            THREE_YEAR_NOTE_YIELD: str = ...
            """3 Year Note Yield"""

            TOTAL_VEHICLE_SALES: str = ...
            """Total Vehicle Sales"""

            TOURIST_ARRIVALS: str = ...
            """Tourist Arrivals"""

            UNEMPLOYMENT_CHANGE: str = ...
            """Unemployment Change"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Sweden(System.Object):
            """Sweden"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            BUSINESS_INVENTORIES: str = ...
            """Business Inventories"""

            CALENDAR: str = ...
            """Calendar"""

            CAPACITY_UTILIZATION: str = ...
            """Capacity Utilization"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CORE_CONSUMER_PRICES: str = ...
            """Core Consumer Prices"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOUSEHOLD_SPENDING: str = ...
            """Household Spending"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_EXPECTATIONS: str = ...
            """Inflation Expectations"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            LOAN_GROWTH: str = ...
            """Loan Growth"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            NEW_ORDERS: str = ...
            """New Orders"""

            PRIVATE_SECTOR_CREDIT: str = ...
            """Private Sector Credit"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

        class Switzerland(System.Object):
            """Switzerland"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            FACTORY_ORDERS: str = ...
            """Factory Orders"""

            FOREIGN_EXCHANGE_RESERVES: str = ...
            """Foreign Exchange Reserves"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            HOLIDAYS: str = ...
            """Holidays"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            NON_FARM_PAYROLLS: str = ...
            """Non Farm Payrolls"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            ZEW_ECONOMIC_SENTIMENT_INDEX: str = ...
            """Zew Economic Sentiment Index"""

        class UnitedKingdom(System.Object):
            """United Kingdom"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            CALENDAR: str = ...
            """Calendar"""

            CAR_REGISTRATIONS: str = ...
            """Car Registrations"""

            CBI_DISTRIBUTIVE_TRADES: str = ...
            """CBI Distributive Trades"""

            CLAIMANT_COUNT_CHANGE: str = ...
            """Claimant Count Change"""

            COMPOSITE_PMI: str = ...
            """Composite Pmi"""

            CONSTRUCTION_ORDERS: str = ...
            """Construction Orders"""

            CONSTRUCTION_OUTPUT: str = ...
            """Construction Output"""

            CONSTRUCTION_PMI: str = ...
            """Construction Pmi"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CONSUMER_CREDIT: str = ...
            """Consumer Credit"""

            CORE_CONSUMER_PRICES: str = ...
            """Core Consumer Prices"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CORE_PRODUCER_PRICES: str = ...
            """Core Producer Prices"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            ECONOMIC_ACTIVITY_INDEX: str = ...
            """Economic Activity Index"""

            EMPLOYMENT_CHANGE: str = ...
            """Employment Change"""

            FACTORY_ORDERS: str = ...
            """Factory Orders"""

            FIVE_YEAR_NOTE_YIELD: str = ...
            """5 Year Note Yield"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOODS_TRADE_BALANCE: str = ...
            """Goods Trade Balance"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            GOVERNMENT_DEBT: str = ...
            """Government Debt"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOME_LOANS: str = ...
            """Home Loans"""

            HOUSING_INDEX: str = ...
            """Housing Index"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_EXPECTATIONS: str = ...
            """Inflation Expectations"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            LABOUR_COSTS: str = ...
            """Labour Costs"""

            LEADING_ECONOMIC_INDEX: str = ...
            """Leading Economic Index"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            MANUFACTURING_PRODUCTION: str = ...
            """Manufacturing Production"""

            MORTGAGE_APPLICATIONS: str = ...
            """Mortgage Applications"""

            MORTGAGE_APPROVALS: str = ...
            """Mortgage Approvals"""

            NATIONWIDE_HOUSING_PRICES: str = ...
            """Nationwide Housing Prices"""

            PRIVATE_INVESTMENT: str = ...
            """Private Investment"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            PRODUCTIVITY: str = ...
            """Productivity"""

            RETAIL_PRICE_INDEX: str = ...
            """Retail Price Index"""

            RETAIL_SALES_EX_FUEL: str = ...
            """Retail Sales Ex Fuel"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            THIRTY_YEAR_BOND_YIELD: str = ...
            """30 Year Bond Yield"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WAGE_GROWTH: str = ...
            """Wage Growth"""

        class UnitedStates(System.Object):
            """United States"""

            ADP_EMPLOYMENT_CHANGE: str = ...
            """Adp Employment Change"""

            API_CRUDE_OIL_STOCK_CHANGE: str = ...
            """API Crude Oil Stock Change"""

            AVERAGE_HOURLY_EARNINGS: str = ...
            """Average Hourly Earnings"""

            AVERAGE_WEEKLY_HOURS: str = ...
            """Average Weekly Hours"""

            BALANCE_OF_TRADE: str = ...
            """Balance of Trade"""

            BUILDING_PERMITS: str = ...
            """Building Permits"""

            BUSINESS_CONFIDENCE: str = ...
            """Business Confidence"""

            BUSINESS_INVENTORIES: str = ...
            """Business Inventories"""

            CALENDAR: str = ...
            """Calendar"""

            CAPACITY_UTILIZATION: str = ...
            """Capacity Utilization"""

            CAPITAL_FLOWS: str = ...
            """Capital Flows"""

            CASE_SHILLER_HOME_PRICE_INDEX: str = ...
            """Case Shiller Home Price Index"""

            CHAIN_STORE_SALES: str = ...
            """Chain Store Sales"""

            CHALLENGER_JOB_CUTS: str = ...
            """Challenger Job Cuts"""

            CHICAGO_FED_NATIONAL_ACTIVITY_INDEX: str = ...
            """Chicago Fed National Activity Index"""

            CHICAGO_PMI: str = ...
            """Chicago Pmi"""

            COMPOSITE_PMI: str = ...
            """Composite Pmi"""

            CONSTRUCTION_SPENDING: str = ...
            """Construction Spending"""

            CONSUMER_CONFIDENCE: str = ...
            """Consumer Confidence"""

            CONSUMER_CREDIT: str = ...
            """Consumer Credit"""

            CONSUMER_PRICE_INDEX_CPI: str = ...
            """Consumer Price Index (CPI)"""

            CONSUMER_SPENDING: str = ...
            """Consumer Spending"""

            CONTINUING_JOBLESS_CLAIMS: str = ...
            """Continuing Jobless Claims"""

            CORE_CONSUMER_PRICES: str = ...
            """Core Consumer Prices"""

            CORE_INFLATION_RATE: str = ...
            """Core Inflation Rate"""

            CORE_PCE_PRICE_INDEX: str = ...
            """Core Pce Price Index"""

            CORE_PRODUCER_PRICES: str = ...
            """Core Producer Prices"""

            CORPORATE_PROFITS: str = ...
            """Corporate Profits"""

            CRUDE_OIL_IMPORTS: str = ...
            """Crude Oil Imports"""

            CRUDE_OIL_RIGS: str = ...
            """Crude Oil Rigs"""

            CRUDE_OIL_STOCKS_CHANGE: str = ...
            """Crude Oil Stocks Change"""

            CURRENT_ACCOUNT: str = ...
            """Current Account"""

            CUSHING_CRUDE_OIL_STOCKS: str = ...
            """Cushing Crude Oil Stocks"""

            DALLAS_FED_MANUFACTURING_INDEX: str = ...
            """Dallas Fed Manufacturing Index"""

            DISTILLATE_FUEL_PRODUCTION: str = ...
            """Distillate Fuel Production"""

            DISTILLATE_STOCKS: str = ...
            """Distillate Stocks"""

            DURABLE_GOODS_ORDERS: str = ...
            """Durable Goods Orders"""

            DURABLE_GOODS_ORDERS_EX_DEFENSE: str = ...
            """Durable Goods Orders Ex Defense"""

            DURABLE_GOODS_ORDERS_EX_TRANSPORTATION: str = ...
            """Durable Goods Orders Ex Transportation"""

            ECONOMIC_OPTIMISM_INDEX: str = ...
            """Economic Optimism Index"""

            EMPLOYMENT_COST_INDEX: str = ...
            """Employment Cost Index"""

            EXISTING_HOME_SALES: str = ...
            """Existing Home Sales"""

            EXPORT_PRICES: str = ...
            """Export Prices"""

            EXPORTS: str = ...
            """Exports"""

            FACTORY_ORDERS: str = ...
            """Factory Orders"""

            FACTORY_ORDERS_EX_TRANSPORTATION: str = ...
            """Factory Orders Ex Transportation"""

            FIFTY_TWO_WEEK_BILL_YIELD: str = ...
            """52 Week Bill Yield"""

            FIVE_YEAR_NOTE_YIELD: str = ...
            """5 Year Note Yield"""

            FOREIGN_BOND_INVESTMENT: str = ...
            """Foreign Bond Investment"""

            FOUR_WEEK_BILL_YIELD: str = ...
            """4 Week Bill Yield"""

            GASOLINE_PRODUCTION: str = ...
            """Gasoline Production"""

            GASOLINE_STOCKS_CHANGE: str = ...
            """Gasoline Stocks Change"""

            GDP_ANNUAL_GROWTH_RATE: str = ...
            """GDP Annual Growth Rate"""

            GDP_DEFLATOR: str = ...
            """Gdp Deflator"""

            GDP_GROWTH_RATE: str = ...
            """GDP Growth Rate"""

            GOODS_TRADE_BALANCE: str = ...
            """Goods Trade Balance"""

            GOVERNMENT_BOND_TEN_Y: str = ...
            """Government Bond 10Y"""

            GOVERNMENT_BUDGET_VALUE: str = ...
            """Government Budget Value"""

            GOVERNMENT_PAYROLLS: str = ...
            """Government Payrolls"""

            HOLIDAYS: str = ...
            """Holidays"""

            HOUSING_INDEX: str = ...
            """Housing Index"""

            HOUSING_STARTS: str = ...
            """Housing Starts"""

            IMPORT_PRICES: str = ...
            """Import Prices"""

            IMPORTS: str = ...
            """Imports"""

            INDUSTRIAL_PRODUCTION: str = ...
            """Industrial Production"""

            INDUSTRIAL_PRODUCTION_MOM: str = ...
            """Industrial Production Mom"""

            INFLATION_EXPECTATIONS: str = ...
            """Inflation Expectations"""

            INFLATION_RATE: str = ...
            """Inflation Rate"""

            INFLATION_RATE_MOM: str = ...
            """Inflation Rate Mom"""

            INITIAL_JOBLESS_CLAIMS: str = ...
            """Initial Jobless Claims"""

            INTEREST_RATE: str = ...
            """Interest Rate"""

            ISM_NEW_YORK_INDEX: str = ...
            """Ism New York Index"""

            JOB_OFFERS: str = ...
            """Job Offers"""

            KANSAS_FED_MANUFACTURING_INDEX: str = ...
            """Kansas Fed Manufacturing Index"""

            LABOR_FORCE_PARTICIPATION_RATE: str = ...
            """Labor Force Participation Rate"""

            LABOR_MARKET_CONDITIONS_INDEX: str = ...
            """Labor Market Conditions Index"""

            LABOUR_COSTS: str = ...
            """Labour Costs"""

            LEADING_ECONOMIC_INDEX: str = ...
            """Leading Economic Index"""

            MANUFACTURING_PAYROLLS: str = ...
            """Manufacturing Payrolls"""

            MANUFACTURING_PMI: str = ...
            """Manufacturing Pmi"""

            MANUFACTURING_PRODUCTION: str = ...
            """Manufacturing Production"""

            MORTGAGE_APPLICATIONS: str = ...
            """Mortgage Applications"""

            MORTGAGE_RATE: str = ...
            """Mortgage Rate"""

            NAHB_HOUSING_MARKET_INDEX: str = ...
            """Nahb Housing Market Index"""

            NATURAL_GAS_STOCKS_CHANGE: str = ...
            """Natural Gas Stocks Change"""

            NET_LONG_TERM_TIC_FLOWS: str = ...
            """Net Long-term Tic Flows"""

            NEW_HOME_SALES: str = ...
            """New Home Sales"""

            NFIB_BUSINESS_OPTIMISM_INDEX: str = ...
            """Nfib Business Optimism Index"""

            NON_FARM_PAYROLLS: str = ...
            """Non Farm Payrolls"""

            NONFARM_PAYROLLS_PRIVATE: str = ...
            """Nonfarm Payrolls - Private"""

            NON_MANUFACTURING_PMI: str = ...
            """Non Manufacturing Pmi"""

            NY_EMPIRE_STATE_MANUFACTURING_INDEX: str = ...
            """Ny Empire State Manufacturing Index"""

            PCE_PRICE_INDEX: str = ...
            """Pce Price Index"""

            PENDING_HOME_SALES: str = ...
            """Pending Home Sales"""

            PERSONAL_INCOME: str = ...
            """Personal Income"""

            PERSONAL_SPENDING: str = ...
            """Personal Spending"""

            PHILADELPHIA_FED_MANUFACTURING_INDEX: str = ...
            """Philadelphia Fed Manufacturing Index"""

            PRODUCER_PRICES: str = ...
            """Producer Prices"""

            PRODUCER_PRICES_CHANGE: str = ...
            """Producer Prices Change"""

            PRODUCTIVITY: str = ...
            """Productivity"""

            REDBOOK_INDEX: str = ...
            """Redbook Index"""

            REFINERY_CRUDE_RUNS: str = ...
            """Refinery Crude Runs"""

            RETAIL_SALES_EX_AUTOS: str = ...
            """Retail Sales Ex Autos"""

            RETAIL_SALES_MOM: str = ...
            """Retail Sales MoM"""

            RETAIL_SALES_YOY: str = ...
            """Retail Sales YoY"""

            RICHMOND_FED_MANUFACTURING_INDEX: str = ...
            """Richmond Fed Manufacturing Index"""

            SERVICES_PMI: str = ...
            """Services Pmi"""

            SEVEN_YEAR_NOTE_YIELD: str = ...
            """7 Year Note Yield"""

            SIX_MONTH_BILL_YIELD: str = ...
            """6 Month Bill Yield"""

            THIRTY_YEAR_BOND_YIELD: str = ...
            """30 Year Bond Yield"""

            THREE_MONTH_BILL_YIELD: str = ...
            """3 Month Bill Yield"""

            THREE_YEAR_NOTE_YIELD: str = ...
            """3 Year Note Yield"""

            TOTAL_VEHICLE_SALES: str = ...
            """Total Vehicle Sales"""

            TWO_YEAR_NOTE_YIELD: str = ...
            """2 Year Note Yield"""

            UNEMPLOYMENT_RATE: str = ...
            """Unemployment Rate"""

            WHOLESALE_INVENTORIES: str = ...
            """Wholesale Inventories"""

        DELIMITER: str = "//"
        """Delimiter used to separate country from ticker in TradingEconomics.Calendar entries"""


class TradingEconomicsIndicator(QuantConnect.Data.BaseData):
    """
    Represents the Trading Economics Indicator information.
    https://docs.tradingeconomics.com/#indicators
    """

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def country(self) -> str:
        """Country name"""
        ...

    @property.setter
    def country(self, value: str) -> None:
        ...

    @property
    def category(self) -> str:
        """Indicator category name"""
        ...

    @property.setter
    def category(self, value: str) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Release time and date in UTC"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def value(self) -> float:
        """Value"""
        ...

    @property.setter
    def value(self, value: float) -> None:
        ...

    @property
    def frequency(self) -> str:
        """Frequency of the indicator"""
        ...

    @property.setter
    def frequency(self, value: str) -> None:
        ...

    @property
    def last_update(self) -> datetime.datetime:
        """Time when new data was inserted or changed"""
        ...

    @property.setter
    def last_update(self, value: datetime.datetime) -> None:
        ...

    @property
    def historical_data_symbol(self) -> str:
        """Unique symbol used by Trading Economics"""
        ...

    @property.setter
    def historical_data_symbol(self, value: str) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data. This is required for some custom data
        
        :returns: A new cloned instance.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, content: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param content: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Collection of TradingEconomicsIndicator objects.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the Trading Economics Indicator information."""
        ...


class TradingEconomicsDateTimeConverter(JsonConverter):
    """DateTime JSON Converter that handles null value"""

    def can_convert(self, object_type: typing.Type) -> bool:
        """Indicate if we can convert this object."""
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """Parse Trading Economics DateTime to C# DateTime"""
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Write DateTime objects to JSON"""
        ...


class TradingEconomicsImportance(Enum):
    """Importance of a TradingEconomics information"""

    LOW = 0
    """Low importance"""

    MEDIUM = 1
    """Medium importance"""

    HIGH = 2
    """High importance"""


class TradingEconomicsCalendar(QuantConnect.Data.BaseData):
    """
    Represents the Trading Economics Calendar information:
    The economic calendar covers around 1600 events for more than 150 countries a month.
    https://docs.tradingeconomics.com/#events
    """

    DATA_SOURCE_ID: int
    """Data source ID"""

    is_auth_code_set: bool
    """Determines if the API key has been set"""

    auth_code: str
    """API key for Trading Economics"""

    @property
    def calendar_id(self) -> str:
        """Unique calendar ID used by Trading Economics"""
        ...

    @property.setter
    def calendar_id(self, value: str) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Release time and date in UTC"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def country(self) -> str:
        """Country name"""
        ...

    @property.setter
    def country(self, value: str) -> None:
        ...

    @property
    def category(self) -> str:
        """Indicator category name"""
        ...

    @property.setter
    def category(self, value: str) -> None:
        ...

    @property
    def event(self) -> str:
        """Specific event name in the calendar"""
        ...

    @property.setter
    def event(self, value: str) -> None:
        ...

    @property
    def event_raw(self) -> str:
        """Raw event name as provided by Trading Economics"""
        ...

    @property.setter
    def event_raw(self, value: str) -> None:
        ...

    @property
    def reference(self) -> str:
        """The period for which released data refers to"""
        ...

    @property.setter
    def reference(self, value: str) -> None:
        ...

    @property
    def source(self) -> str:
        """Source of data"""
        ...

    @property.setter
    def source(self, value: str) -> None:
        ...

    @property
    def actual(self) -> typing.Optional[float]:
        """Latest released value"""
        ...

    @property.setter
    def actual(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def previous(self) -> typing.Optional[float]:
        """Value for the previous period after the revision (if revision is applicable)"""
        ...

    @property.setter
    def previous(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def forecast(self) -> typing.Optional[float]:
        """Average forecast among a representative group of economists"""
        ...

    @property.setter
    def forecast(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trading_economics_forecast(self) -> typing.Optional[float]:
        """TradingEconomics own projections"""
        ...

    @property.setter
    def trading_economics_forecast(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def date_span(self) -> str:
        """
        0 indicates that the time of the event is known,
        1 indicates that we only know the date of event, the exact time of event is unknown
        """
        ...

    @property.setter
    def date_span(self, value: str) -> None:
        ...

    @property
    def importance(self) -> QuantConnect.DataSource.TradingEconomicsImportance:
        """Importance of a TradingEconomics information"""
        ...

    @property.setter
    def importance(self, value: QuantConnect.DataSource.TradingEconomicsImportance) -> None:
        ...

    @property
    def last_update(self) -> datetime.datetime:
        """Time when new data was inserted or changed"""
        ...

    @property.setter
    def last_update(self, value: datetime.datetime) -> None:
        ...

    @property
    def revised(self) -> typing.Optional[float]:
        """Value reported in the previous period after revision"""
        ...

    @property.setter
    def revised(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def o_country(self) -> str:
        """Country's original name"""
        ...

    @property.setter
    def o_country(self, value: str) -> None:
        ...

    @property
    def o_category(self) -> str:
        """Category's original name"""
        ...

    @property.setter
    def o_category(self, value: str) -> None:
        ...

    @property
    def ticker(self) -> str:
        """Unique ticker used by Trading Economics"""
        ...

    @property.setter
    def ticker(self, value: str) -> None:
        ...

    @property
    def is_percentage(self) -> bool:
        """Indicates whether the Actual, Previous, Forecast, TradingEconomicsForecast fields are reported as percent values"""
        ...

    @property.setter
    def is_percentage(self, value: bool) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data. This is required for some custom data
        
        :returns: A new cloned instance.
        """
        ...

    @staticmethod
    def country_to_currency_code(country: str) -> str:
        """
        Converts country name to currency code (ISO 4217)
        
        :param country: Country name
        :returns: ISO 4217 currency code.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    @staticmethod
    def parse_decimal(value: str, in_percent: bool) -> typing.Optional[float]:
        """
        Parse decimal from calendar data
        
        :param value: Value to parse
        :param in_percent: Is the value a percentage
        :returns: Nullable decimal.
        """
        ...

    @staticmethod
    def process_api_response(content: str) -> System.Collections.Generic.List[QuantConnect.DataSource.TradingEconomicsCalendar]:
        """
        Parses the raw Trading Economics calendar API result
        
        :param content: Contents of returned data
        :returns: List of instances of the current class.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Line from the data source
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: TradingEconomicsCalendar or BaseDataCollection object containing TradingEconomicsCalendar as its Data.
        """
        ...

    @staticmethod
    def set_auth_code(auth_code: str) -> None:
        """
        Sets the Trading Economics API key.
        
        :param auth_code: The Trading Economics API key
        """
        ...

    def to_csv(self) -> str:
        """
        Convert this instance to a CSV file
        
        :returns: string as CSV.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the Trading Economics Calendar information."""
        ...


class EarningsType(Enum):
    """Earnings type: earnings, ipo, dividends"""

    EARNINGS = 0
    """Earnings"""

    IPO = 1
    """IPO"""

    DIVIDENDS = 2
    """Dividends"""

    SPLIT = 3
    """Stock Splits"""


class TradingEconomicsEarnings(QuantConnect.Data.BaseData):
    """
    Represents the Trading Economics Earnings information.
    https://docs.tradingeconomics.com/#earnings
    """

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def end_time(self) -> datetime.datetime:
        """Release time and date in UTC"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def symbol(self) -> str:
        """Unique symbol used by Trading Economics"""
        ...

    @property.setter
    def symbol(self, value: str) -> None:
        ...

    @property
    def earnings_type(self) -> QuantConnect.DataSource.EarningsType:
        """Earnings type: earnings, ipo, dividends"""
        ...

    @property.setter
    def earnings_type(self, value: QuantConnect.DataSource.EarningsType) -> None:
        ...

    @property
    def name(self) -> str:
        """Company name"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def actual(self) -> typing.Optional[float]:
        """Earnings per share"""
        ...

    @property.setter
    def actual(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def value(self) -> float:
        """Earnings per share"""
        ...

    @property
    def forecast(self) -> typing.Optional[float]:
        """Average forecast among a representative group of analysts"""
        ...

    @property.setter
    def forecast(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def fiscal_tag(self) -> str:
        """Fiscal year and quarter"""
        ...

    @property.setter
    def fiscal_tag(self, value: str) -> None:
        ...

    @property
    def fiscal_reference(self) -> str:
        """Fiscal year and quarter in different format"""
        ...

    @property.setter
    def fiscal_reference(self, value: str) -> None:
        ...

    @property
    def calendar_reference(self) -> str:
        """Calendar quarter for the release"""
        ...

    @property.setter
    def calendar_reference(self, value: str) -> None:
        ...

    @property
    def country(self) -> str:
        """Country name"""
        ...

    @property.setter
    def country(self, value: str) -> None:
        ...

    @property
    def currency(self) -> str:
        """Currency"""
        ...

    @property.setter
    def currency(self, value: str) -> None:
        ...

    @property
    def last_update(self) -> datetime.datetime:
        """Time when new data was inserted or changed"""
        ...

    @property.setter
    def last_update(self, value: datetime.datetime) -> None:
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...


class EstimizeEstimate(QuantConnect.Data.BaseData):
    """Financial estimates for the specified company"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def id(self) -> str:
        """The unique identifier for the estimate"""
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    @property
    def ticker(self) -> str:
        """The ticker of the company being estimated"""
        ...

    @property.setter
    def ticker(self, value: str) -> None:
        ...

    @property
    def fiscal_year(self) -> int:
        """The fiscal year of the quarter being estimated"""
        ...

    @property.setter
    def fiscal_year(self, value: int) -> None:
        ...

    @property
    def fiscal_quarter(self) -> int:
        """The fiscal quarter of the quarter being estimated"""
        ...

    @property.setter
    def fiscal_quarter(self, value: int) -> None:
        ...

    @property
    def created_at(self) -> datetime.datetime:
        """The time that the estimate was created (UTC)"""
        ...

    @property.setter
    def created_at(self, value: datetime.datetime) -> None:
        ...

    @property
    def eps(self) -> typing.Optional[float]:
        """The estimated earnings per share for the company in the specified fiscal quarter"""
        ...

    @property.setter
    def eps(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def revenue(self) -> typing.Optional[float]:
        """The estimated revenue for the company in the specified fiscal quarter"""
        ...

    @property.setter
    def revenue(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def user_name(self) -> str:
        """The unique identifier for the author of the estimate"""
        ...

    @property.setter
    def user_name(self, value: str) -> None:
        ...

    @property
    def analyst_id(self) -> str:
        """The author of the estimate"""
        ...

    @property.setter
    def analyst_id(self, value: str) -> None:
        ...

    @property
    def flagged(self) -> bool:
        """
        A boolean value which indicates whether we have flagged this estimate internally as erroneous
        (spam, wrong accounting standard, etc)
        """
        ...

    @property.setter
    def flagged(self, value: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Required for successful Json.NET deserialization"""
        ...

    @overload
    def __init__(self, csvLine: str) -> None:
        """
        Creates a new instance of EstimizeEstimate from a CSV line
        
        :param csvLine: CSV line
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Estimize Estimate object.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the Estimize Estimate information."""
        ...


class EstimizeRelease(QuantConnect.Data.BaseData):
    """Financial releases for the specified company"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def id(self) -> str:
        """The unique identifier for the release"""
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    @property
    def fiscal_year(self) -> int:
        """The fiscal year for the release"""
        ...

    @property.setter
    def fiscal_year(self, value: int) -> None:
        ...

    @property
    def fiscal_quarter(self) -> int:
        """The fiscal quarter for the release"""
        ...

    @property.setter
    def fiscal_quarter(self, value: int) -> None:
        ...

    @property
    def release_date(self) -> datetime.datetime:
        """The date of the release"""
        ...

    @property.setter
    def release_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def eps(self) -> typing.Optional[float]:
        """The earnings per share for the specified fiscal quarter"""
        ...

    @property.setter
    def eps(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def revenue(self) -> typing.Optional[float]:
        """The revenue for the specified fiscal quarter"""
        ...

    @property.setter
    def revenue(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def wall_street_eps_estimate(self) -> typing.Optional[float]:
        """The estimated EPS from Wall Street"""
        ...

    @property.setter
    def wall_street_eps_estimate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def wall_street_revenue_estimate(self) -> typing.Optional[float]:
        """The estimated revenue from Wall Street"""
        ...

    @property.setter
    def wall_street_revenue_estimate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def consensus_eps_estimate(self) -> typing.Optional[float]:
        """The mean EPS consensus by the Estimize community"""
        ...

    @property.setter
    def consensus_eps_estimate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def consensus_revenue_estimate(self) -> typing.Optional[float]:
        """The mean revenue consensus by the Estimize community"""
        ...

    @property.setter
    def consensus_revenue_estimate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def consensus_weighted_eps_estimate(self) -> typing.Optional[float]:
        """The weighted EPS consensus by the Estimize community"""
        ...

    @property.setter
    def consensus_weighted_eps_estimate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def consensus_weighted_revenue_estimate(self) -> typing.Optional[float]:
        """The weighted revenue consensus by the Estimize community"""
        ...

    @property.setter
    def consensus_weighted_revenue_estimate(self, value: typing.Optional[float]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Without a default constructor, Json.NET will call the
        other constructor with `null` for the string parameter
        """
        ...

    @overload
    def __init__(self, csvLine: str) -> None:
        """
        Creates EstimizeRelease instance from a line of CSV
        
        :param csvLine: CSV line
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Estimize Release object.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the Estimize Release information."""
        ...


class EstimizeConsensus(QuantConnect.Data.BaseData):
    """Consensus of the specified release"""

    class ConsensusSource(Enum):
        """Source of the Consensus"""

        WALL_STREET = 0
        """Consensus from Wall Street"""

        ESTIMIZE = 1
        """Consensus from Estimize"""

    class ConsensusType(Enum):
        """Type of the consensus"""

        EPS = 0
        """Consensus on earnings per share value"""

        REVENUE = 1
        """Consensus on revenue value"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def id(self) -> str:
        """The unique identifier for the estimate"""
        ...

    @property.setter
    def id(self, value: str) -> None:
        ...

    @property
    def source(self) -> typing.Optional[QuantConnect.DataSource.EstimizeConsensus.ConsensusSource]:
        """Consensus source (Wall Street or Estimize)"""
        ...

    @property.setter
    def source(self, value: typing.Optional[QuantConnect.DataSource.EstimizeConsensus.ConsensusSource]) -> None:
        ...

    @property
    def type(self) -> typing.Optional[QuantConnect.DataSource.EstimizeConsensus.ConsensusType]:
        """Type of Consensus (EPS or Revenue)"""
        ...

    @property.setter
    def type(self, value: typing.Optional[QuantConnect.DataSource.EstimizeConsensus.ConsensusType]) -> None:
        ...

    @property
    def mean(self) -> typing.Optional[float]:
        """The mean of the distribution of estimates (the "consensus")"""
        ...

    @property.setter
    def mean(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def value(self) -> float:
        """The mean of the distribution of estimates (the "consensus")"""
        ...

    @property
    def high(self) -> typing.Optional[float]:
        """The highest estimate in the distribution"""
        ...

    @property.setter
    def high(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def low(self) -> typing.Optional[float]:
        """The lowest estimate in the distribution"""
        ...

    @property.setter
    def low(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def standard_deviation(self) -> typing.Optional[float]:
        """The standard deviation of the distribution"""
        ...

    @property.setter
    def standard_deviation(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def count(self) -> typing.Optional[int]:
        """The number of estimates in the distribution"""
        ...

    @property.setter
    def count(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def updated_at(self) -> datetime.datetime:
        """The timestamp of this consensus (UTC)"""
        ...

    @property.setter
    def updated_at(self, value: datetime.datetime) -> None:
        ...

    @property
    def fiscal_year(self) -> typing.Optional[int]:
        """The fiscal year for the release"""
        ...

    @property.setter
    def fiscal_year(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def fiscal_quarter(self) -> typing.Optional[int]:
        """The fiscal quarter for the release"""
        ...

    @property.setter
    def fiscal_quarter(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The timestamp of this consensus (UTC)"""
        ...

    @overload
    def __init__(self) -> None:
        """Empty constructor required for successful Json.NET deserialization"""
        ...

    @overload
    def __init__(self, csvLine: str) -> None:
        """
        Creates an instance from CSV lines
        
        :param csvLine: CSV file
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Estimize consensus object.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the Estimize Estimate information."""
        ...


class BenzingaNews(QuantConnect.Data.IndexedBaseData):
    """News data powered by Benzinga - https://docs.benzinga.io/benzinga/newsfeed-v2.html"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def id(self) -> int:
        """Unique ID assigned to the article by Benzinga"""
        ...

    @property.setter
    def id(self, value: int) -> None:
        ...

    @property
    def author(self) -> str:
        """Author of the article"""
        ...

    @property.setter
    def author(self, value: str) -> None:
        ...

    @property
    def created_at(self) -> datetime.datetime:
        """Date the article was published"""
        ...

    @property.setter
    def created_at(self, value: datetime.datetime) -> None:
        ...

    @property
    def updated_at(self) -> datetime.datetime:
        """Date that the article was revised on"""
        ...

    @property.setter
    def updated_at(self, value: datetime.datetime) -> None:
        ...

    @property
    def title(self) -> str:
        """Title of the article published"""
        ...

    @property.setter
    def title(self, value: str) -> None:
        ...

    @property
    def teaser(self) -> str:
        """Summary of the article's contents"""
        ...

    @property.setter
    def teaser(self, value: str) -> None:
        ...

    @property
    def contents(self) -> str:
        """Contents of the article"""
        ...

    @property.setter
    def contents(self, value: str) -> None:
        ...

    @property
    def categories(self) -> System.Collections.Generic.List[str]:
        """Categories that relate to the article"""
        ...

    @property.setter
    def categories(self, value: System.Collections.Generic.List[str]) -> None:
        ...

    @property
    def symbols(self) -> System.Collections.Generic.List[QuantConnect.Symbol]:
        """Symbols that this news article mentions"""
        ...

    @property.setter
    def symbols(self, value: System.Collections.Generic.List[QuantConnect.Symbol]) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.List[str]:
        """
        Additional tags that are not channels/categories, but are reoccuring
        themes including, but not limited to; analyst names, bills being talked
        about in Congress (Dodd-Frank), specific products (iPhone), politicians,
        celebrities, stock movements (i.e. 'Mid-day Losers' & 'Mid-day Gainers').
        """
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.List[str]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Date that the article was revised on"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Creates a clone of the instance
        
        :returns: A clone of the instance.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Gets the source of the index file
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: Is live mode
        :returns: SubscriptionDataSource indicating where data is located and how it's stored.
        """
        ...

    def get_source_for_an_index(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], index: str, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Determines the actual source from an index contained within a ticker folder
        
        :param config: Subscription configuration
        :param date: Date
        :param index: File to load data from
        :param is_live_mode: Is live mode
        :returns: SubscriptionDataSource pointing to the article.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Creates an instance from a line of JSON containing article information read from the `content` directory
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance of BenzingaNews.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...

    def to_string(self) -> str:
        """
        Converts the instance to string
        
        :returns: Article title and contents.
        """
        ...


class BenzingaNewsJsonConverter(JsonConverter):
    """
    Helper json converter class used to convert Benzinga news data
    into BenzingaNews
    
    An example schema of the data in a serialized format is provided
    to help you better understand this converter.
    """

    SHARE_CLASS_MAPPED_TICKERS: System.Collections.Generic.Dictionary[str, System.Collections.Generic.HashSet[str]] = ...
    """
    Sometimes "Berkshire Hathaway" is mentioned as "BRK" in the raw data, although it is
    separated into class A and B shares and should appear as BRK.A and BRK.B. Because our
    map file system does not perform the conversion from BRK -> { BRK.A, BRK.B }, we must
    provide them manually. Note that we don't dynamically try to locate class A and B shares
    because there can exist companies with the same base ticker that class A and B shares have.
    For example, CBS trades under "CBS" and "CBS.A", which means that if "CBS" appears, it will
    be automatically mapped to CBS. However, if we dynamically selected "CBS.A" - we might select
    a different company not associated with the ticker being referenced.
    """

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str] = None, liveMode: bool = False) -> None:
        """
        Creates a new instance of the json converter
        
        :param symbol: The Symbol instance associated with this news
        :param liveMode: True if live mode, false for backtesting
        """
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    @staticmethod
    def deserialize_news(item: typing.Any, enable_logging: bool = False) -> QuantConnect.DataSource.BenzingaNews:
        """
        Helper method to deserialize a single json Benzinga news
        
        :param item: The json token containing the Benzinga news to deserialize
        :param enable_logging: true to enable logging (for debug purposes)
        :returns: The deserialized BenzingaNews instance.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class USTreasuryYieldCurveRate(QuantConnect.Data.BaseData):
    """U.S. Treasury yield curve data"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def one_month(self) -> typing.Optional[float]:
        """One month yield curve"""
        ...

    @property.setter
    def one_month(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def two_month(self) -> typing.Optional[float]:
        """Two month yield curve"""
        ...

    @property.setter
    def two_month(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def three_month(self) -> typing.Optional[float]:
        """Three month yield curve"""
        ...

    @property.setter
    def three_month(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def six_month(self) -> typing.Optional[float]:
        """Six month yield curve"""
        ...

    @property.setter
    def six_month(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def one_year(self) -> typing.Optional[float]:
        """One year yield curve"""
        ...

    @property.setter
    def one_year(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def two_year(self) -> typing.Optional[float]:
        """Two year yield curve"""
        ...

    @property.setter
    def two_year(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def three_year(self) -> typing.Optional[float]:
        """Three year yield curve"""
        ...

    @property.setter
    def three_year(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def five_year(self) -> typing.Optional[float]:
        """Five year yield curve"""
        ...

    @property.setter
    def five_year(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def seven_year(self) -> typing.Optional[float]:
        """Seven year yield curve"""
        ...

    @property.setter
    def seven_year(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def ten_year(self) -> typing.Optional[float]:
        """Ten year yield curve"""
        ...

    @property.setter
    def ten_year(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def twenty_year(self) -> typing.Optional[float]:
        """Twenty year yield curve"""
        ...

    @property.setter
    def twenty_year(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def thirty_year(self) -> typing.Optional[float]:
        """Thirty year yield curve"""
        ...

    @property.setter
    def thirty_year(self, value: typing.Optional[float]) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the object. This method implementation is required
        so that we don't have any null values for our properties
        when the user attempts to use it in backtesting/live trading
        
        :returns: Cloned instance.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Specifies the location of the data and directs LEAN where to load the data from
        
        :param config: Subscription configuration
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Subscription data source object pointing LEAN to the data location.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reads and parses yield curve data from a csv file
        
        :param config: Subscription configuration
        :param line: CSV line containing yield curve data
        :param date: Date request was made for
        :param is_live_mode: Is live mode
        :returns: YieldCurve instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...


class CryptoUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Crypto Coarse Fundamental object for crpyto universe selection"""

    @property
    def open(self) -> float:
        """Daily Open Price (UTC 00:00)"""
        ...

    @property.setter
    def open(self, value: float) -> None:
        ...

    @property
    def high(self) -> float:
        """Daily High Price"""
        ...

    @property.setter
    def high(self, value: float) -> None:
        ...

    @property
    def low(self) -> float:
        """Daily Low Price"""
        ...

    @property.setter
    def low(self, value: float) -> None:
        ...

    @property
    def close(self) -> float:
        """Daily Close Price"""
        ...

    @property.setter
    def close(self, value: float) -> None:
        ...

    @property
    def volume(self) -> float:
        """
        Daily Trade Volume
        Note that this only includes the volume traded in the selected market
        """
        ...

    @property.setter
    def volume(self, value: float) -> None:
        ...

    @property
    def volume_in_quote_currency(self) -> float:
        """
        Daily Volume in Quote Currency
        Note that this only includes the volume traded in the selected market
        """
        ...

    @property.setter
    def volume_in_quote_currency(self, value: float) -> None:
        ...

    @property
    def volume_in_usd(self) -> typing.Optional[float]:
        """
        Daily Volume in USD
        Note that this only includes the volume traded in the selected market
        """
        ...

    @property.setter
    def volume_in_usd(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def price(self) -> float:
        """Alias of close price"""
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    @staticmethod
    @overload
    def binance(selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CryptoUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def binance(selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def binance_us(selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CryptoUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def binance_us(selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def bitfinex(selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CryptoUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def bitfinex(selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def bybit(selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CryptoUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def bybit(selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    @staticmethod
    @overload
    def coinbase(selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CryptoUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def coinbase(selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    @staticmethod
    @overload
    def kraken(selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CryptoUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    @staticmethod
    @overload
    def kraken(selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new crypto universe
        
        :param selector: Returns the symbols that should be included in the universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...

    def universe_symbol(self, market: str = None) -> QuantConnect.Symbol:
        """
        Creates the universe symbol
        
        :returns: A crypto coarse universe symbol.
        """
        ...


class CryptoCoarseFundamental(QuantConnect.DataSource.CryptoUniverse):
    """'CryptoCoarseFundamental' was renamed to 'CryptoUniverse'"""


class KavoutCompositeFactorBundle(QuantConnect.Data.BaseData):
    """
    Kavout signals are machine-learning enhanced scores that capture the returns
    of systematic factors such as Quality, Value, Momentum, Growth, and Low Volatility.
    There are many different anomalies discovered by researchers and practitioners across
    these factor categories, and there is no good common definition of each style
    across the literature.
    
    Kavout creates an ensemble score for each style that gauges the different factors
    considered in the literature and industry practice.
    
    Each signal is generated by an ensemble model consisting of inputs from hundreds of anomalies.
    """

    @property
    def growth(self) -> float:
        """Growth factor score"""
        ...

    @property.setter
    def growth(self, value: float) -> None:
        ...

    @property
    def value_factor(self) -> float:
        """Value factor score"""
        ...

    @property.setter
    def value_factor(self, value: float) -> None:
        ...

    @property
    def quality(self) -> float:
        """Quality factor score"""
        ...

    @property.setter
    def quality(self, value: float) -> None:
        ...

    @property
    def momentum(self) -> float:
        """Momentum factor score"""
        ...

    @property.setter
    def momentum(self, value: float) -> None:
        ...

    @property
    def low_volatility(self) -> float:
        """Low volatility factor score"""
        ...

    @property.setter
    def low_volatility(self, value: float) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time that the data became available to the algorithm"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
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

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """
        Formats a string with Cross-asset model data
        
        :returns: string containing Cross-asset model information.
        """
        ...


class USEnergy(QuantConnect.Data.BaseData):
    """United States Energy Information Administration (EIA). This loads U.S. Energy data from QuantConnect's cache."""

    class Petroleum(System.Object):
        """Petroleum"""

        class UnitedStates(System.Object):
            """United States"""

            WEEKLY_REFINER_AND_BLENDER_ADJUSTED_NET_PRODUCTION_OF_FINISHED_MOTOR_GASOLINE: str = "PET.WGFRPUS2.W"
            """U.S. Refiner and Blender Adjusted Net Production of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_FINISHED_MOTOR_GASOLINE: str = "PET.WGFSTUS1.W"
            """U.S. Ending Stocks of Finished Motor Gasoline in Thousand Barrels (Mbbl)"""

            WEEKLY_PRODUCT_SUPPLIED_OF_FINISHED_MOTOR_GASOLINE: str = "PET.WGFUPUS2.W"
            """U.S. Product Supplied of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CRUDE_OIL_IN_SPR: str = "PET.WCSSTUS1.W"
            """U.S. Ending Stocks of Crude Oil in SPR in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_500_PPM_SULFUR: str = "PET.WDGRPUS2.W"
            """U.S.  Refiner and Blender Net Production of Distillate Fuel Oil Greater than 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_500_PPM_SULFUR: str = "PET.WDGSTUS1.W"
            """U.S. Ending Stocks of Distillate Fuel Oil, Greater Than 500 ppm Sulfur in Thousand Barrels (Mbbl)"""

            WEEKLY_EXPORTS_OF_TOTAL_DISTILLATE: str = "PET.WDIEXUS2.W"
            """U.S. Exports of Total Distillate in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_DISTILLATE_FUEL_OIL: str = "PET.WDIIMUS2.W"
            """U.S. Imports of Distillate Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL: str = "PET.WDIRPUS2.W"
            """U.S. Refiner and Blender Net Production of Distillate Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.WKJSTUS1.W"
            """U.S. Ending Stocks of Kerosene-Type Jet Fuel in Thousand Barrels (Mbbl)"""

            WEEKLY_PRODUCT_SUPPLIED_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.WKJUPUS2.W"
            """U.S. Product Supplied of Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_TOTAL_GASOLINE: str = "PET.WGTIMUS2.W"
            """U.S. Imports of Total Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_TOTAL_GASOLINE: str = "PET.WGTSTUS1.W"
            """U.S. Ending Stocks of Total Gasoline in Thousand Barrels (Mbbl)"""

            WEEKLY_GROSS_INPUTS_INTO_REFINERIES: str = "PET.WGIRIUS2.W"
            """U.S. Gross Inputs into Refineries in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_REFORMULATED_MOTOR_GASOLINE: str = "PET.WGRIMUS2.W"
            """U.S. Imports of Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_REFORMULATED_MOTOR_GASOLINE: str = "PET.WGRRPUS2.W"
            """U.S. Refiner and Blender Net Production of Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_REFORMULATED_MOTOR_GASOLINE: str = "PET.WGRSTUS1.W"
            """U.S. Ending Stocks of Reformulated Motor Gasoline in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_DISTILLATE_FUEL_OIL: str = "PET.WDISTUS1.W"
            """U.S. Ending Stocks of Distillate Fuel Oil in Thousand Barrels (Mbbl)"""

            WEEKLY_PRODUCT_SUPPLIED_OF_DISTILLATE_FUEL_OIL: str = "PET.WDIUPUS2.W"
            """U.S. Product Supplied of Distillate Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_MILITARY_KEROSENE_TYPE_JET_FUEL: str = "PET.WKMRPUS2.W"
            """U.S.  Refiner and Blender Net Production of Military Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_OPERABLE_CRUDE_OIL_DISTILLATION_CAPACITY: str = "PET.WOCLEUS2.W"
            """U. S. Operable Crude Oil Distillation Capacity in Thousand Barrels per Calendar Day (Mbbl/d)"""

            WEEKLY_PROPYLENE_NONFUEL_USE_STOCKS_AT_BULK_TERMINALS: str = "PET.WPLSTUS1.W"
            """U.S. Propylene Nonfuel Use Stocks at Bulk Terminals in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_PROPANE_AND_PROPYLENE: str = "PET.WPRSTUS1.W"
            """U.S. Ending Stocks of Propane and Propylene in Thousand Barrels (Mbbl)"""

            WEEKLY_PERCENT_UTILIZATION_OF_REFINERY_OPERABLE_CAPACITY: str = "PET.WPULEUS3.W"
            """U.S. Percent Utilization of Refinery Operable Capacity in Percent (%)"""

            WEEKLY_EXPORTS_OF_RESIDUAL_FUEL_OIL: str = "PET.WREEXUS2.W"
            """U.S. Exports of Residual Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_RESIDUAL_FUEL_OIL: str = "PET.WREIMUS2.W"
            """U.S. Imports of Residual Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_COMMERCIAL_KEROSENE_TYPE_JET_FUEL: str = "PET.WKCRPUS2.W"
            """U.S.  Refiner and Blender Net Production of Commercial Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_EXPORTS_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.WKJEXUS2.W"
            """U.S. Exports of Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.WKJIMUS2.W"
            """U.S. Imports of Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.WKJRPUS2.W"
            """U.S. Refiner and Blender Net Production of Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_EXCLUDING_SPR_OF_CRUDE_OIL: str = "PET.WCESTUS1.W"
            """U.S. Ending Stocks excluding SPR of Crude Oil in Thousand Barrels (Mbbl)"""

            WEEKLY_EXPORTS_OF_CRUDE_OIL: str = "PET.WCREXUS2.W"
            """U.S. Exports of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_FIELD_PRODUCTION_OF_CRUDE_OIL: str = "PET.WCRFPUS2.W"
            """U.S. Field Production of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_CRUDE_OIL: str = "PET.WCRIMUS2.W"
            """U.S. Imports of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_NET_IMPORTS_OF_CRUDE_OIL: str = "PET.WCRNTUS2.W"
            """U.S. Net Imports of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_INPUT_OF_CRUDE_OIL: str = "PET.WCRRIUS2.W"
            """U.S. Refiner Net Input of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_RESIDUAL_FUEL_OIL: str = "PET.WRERPUS2.W"
            """U.S. Refiner and Blender Net Production of Residual Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_RESIDUAL_FUEL_OIL: str = "PET.WRESTUS1.W"
            """U.S. Ending Stocks of Residual Fuel Oil in Thousand Barrels (Mbbl)"""

            WEEKLY_PRODUCT_SUPPLIED_OF_RESIDUAL_FUEL_OIL: str = "PET.WREUPUS2.W"
            """U.S. Product Supplied of Residual Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_EXPORTS_OF_TOTAL_PETROLEUM_PRODUCTS: str = "PET.WRPEXUS2.W"
            """U.S. Exports of Total Petroleum Products in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_TOTAL_PETROLEUM_PRODUCTS: str = "PET.WRPIMUS2.W"
            """U.S. Imports of Total Petroleum Products in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_NET_IMPORTS_OF_TOTAL_PETROLEUM_PRODUCTS: str = "PET.WRPNTUS2.W"
            """U.S. Net Imports of Total Petroleum Products in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_PRODUCT_SUPPLIED_OF_PETROLEUM_PRODUCTS: str = "PET.WRPUPUS2.W"
            """U.S. Product Supplied of Petroleum Products in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_EXCLUDING_SPR_OF_CRUDE_OIL_AND_PETROLEUM_PRODUCTS: str = "PET.WTESTUS1.W"
            """U.S. Ending Stocks excluding SPR of Crude Oil and Petroleum Products in Thousand Barrels (Mbbl)"""

            WEEKLY_EXPORTS_OF_CRUDE_OIL_AND_PETROLEUM_PRODUCTS: str = "PET.WTTEXUS2.W"
            """U.S. Exports of Crude Oil and Petroleum Products in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_CRUDE_OIL_AND_PETROLEUM_PRODUCTS: str = "PET.WTTIMUS2.W"
            """U.S. Imports of Crude Oil and Petroleum Products in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_NET_IMPORTS_OF_CRUDE_OIL_AND_PETROLEUM_PRODUCTS: str = "PET.WTTNTUS2.W"
            """U.S. Net Imports of Crude Oil and Petroleum Products in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CRUDE_OIL_AND_PETROLEUM_PRODUCTS: str = "PET.WTTSTUS1.W"
            """U.S. Ending Stocks of Crude Oil and Petroleum Products in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_UNFINISHED_OILS: str = "PET.WUOSTUS1.W"
            """U.S. Ending Stocks of Unfinished Oils in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_OTHER_FINISHED_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.WG6TP_NUS_2.W"
            """U.S. Refiner and Blender Net Production of Other Finished Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_0_TO_15_PPM_SULFUR: str = "PET.WD0TP_NUS_2.W"
            """U.S. Refiner and Blender Net Production of Distillate Fuel Oil, 0 to 15 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_15_TO_500_PPM_SULFUR: str = "PET.WD1ST_NUS_1.W"
            """U.S. Ending Stocks of Distillate Fuel Oil, Greater than 15 to 500 ppm Sulfur in Thousand Barrels (Mbbl)"""

            WEEKLY_PRODUCTION_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_15_TO_500_PPM_SULFUR: str = "PET.WD1TP_NUS_2.W"
            """U.S. Production of Distillate Fuel Oil, Greater than 15 to 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_REFORMULATED_MOTOR_GASOLINE_WITH_FUEL_ALCOHOL: str = "PET.WG1ST_NUS_1.W"
            """U.S. Ending Stocks of Reformulated Motor Gasoline with Fuel ALcohol in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_CRUDE_OIL: str = "PET.WCRSTUS1.W"
            """U.S. Ending Stocks of Crude Oil in Thousand Barrels (Mbbl)"""

            WEEKLY_CRUDE_OIL_IMPORTS_BY_SPR: str = "PET.WCSIMUS2.W"
            """U.S. Crude Oil Imports by SPR in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_GASOLINE_BLENDING_COMPONENTS: str = "PET.WBCIMUS2.W"
            """U.S. Imports of Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_GASOLINE_BLENDING_COMPONENTS: str = "PET.WBCSTUS1.W"
            """U.S. Ending Stocks of Gasoline Blending Components in Thousand Barrels (Mbbl)"""

            WEEKLY_COMMERCIAL_CRUDE_OIL_IMPORTS_EXCLUDING_SPR: str = "PET.WCEIMUS2.W"
            """U.S. Commercial Crude Oil Imports Excluding SPR in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_BLENDER_AND_GAS_PLANT_NET_PRODUCTION_OF_PROPANE_AND_PROPYLENE: str = "PET.WPRTP_NUS_2.W"
            """U.S. Refiner, Blender, and Gas Plant Net Production of Propane and Propylene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_FINISHED_REFORMULATED_MOTOR_GASOLINE_WITH_ETHANOL: str = "PET.WG1TP_NUS_2.W"
            """U.S. Refiner and Blender Net Production of Finished Reformulated Motor Gasoline with Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_REFORMULATED_MOTOR_GASOLINE_NON_OXYGENTATED: str = "PET.WG3ST_NUS_1.W"
            """U.S. Ending Stocks of Reformulated Motor Gasoline, Non-Oxygentated in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.WG4ST_NUS_1.W"
            """U.S. Ending Stocks of Conventional Motor Gasoline in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.WG4TP_NUS_2.W"
            """U.S. Refiner and Blender Net Production of Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CONVENTIONAL_MOTOR_GASOLINE_WITH_FUEL_ETHANOL: str = "PET.WG5ST_NUS_1.W"
            """U.S. Ending Stocks of Conventional Motor Gasoline with Fuel Ethanol in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_FINISHED_CONVENTIONAL_MOTOR_GASOLINE_WITH_ETHANOL: str = "PET.WG5TP_NUS_2.W"
            """U.S. Refiner and Blender Net Production of Finished Conventional Motor Gasoline with Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_OTHER_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.WG6ST_NUS_1.W"
            """U.S. Ending Stocks of Other Conventional Motor Gasoline in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_INPUT_OF_CONVENTIONAL_CBOB_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO6RI_NUS_2.W"
            """U.S. Refiner and Blender Net Input of Conventional CBOB Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CONVENTIONAL_CBOB_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO6ST_NUS_1.W"
            """U.S. Ending Stocks of Conventional CBOB Gasoline Blending Components in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_INPUT_OF_CONVENTIONAL_GTAB_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO7RI_NUS_2.W"
            """U.S. Refiner and Blender Net Input of Conventional GTAB Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CONVENTIONAL_GTAB_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO7ST_NUS_1.W"
            """U.S. Ending Stocks of Conventional GTAB Gasoline Blending Components in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_INPUT_OF_CONVENTIONAL_OTHER_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO9RI_NUS_2.W"
            """U.S. Refiner and Blender Net Input of Conventional Other Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CONVENTIONAL_OTHER_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO9ST_NUS_1.W"
            """U.S. Ending Stocks of Conventional Other Gasoline Blending Components in Thousand Barrels (Mbbl)"""

            WEEKLY_NO_2_HEATING_OIL_WHOLESALE_RESALE_PRICE: str = "PET.W_EPD2F_PWR_NUS_DPG.W"
            """U.S. No. 2 Heating Oil Wholesale/Resale Price in Dollars per Gallon ($/gal)"""

            WEEKLY_CRUDE_OIL_STOCKS_IN_TRANSIT_ON_SHIPS_FROM_ALASKA: str = "PET.W_EPC0_SKA_NUS_MBBL.W"
            """U.S. Crude Oil Stocks in Transit (on Ships) from Alaska in Thousand Barrels (Mbbl)"""

            WEEKLY_DAYS_OF_SUPPLY_OF_CRUDE_OIL_EXCLUDING_SPR: str = "PET.W_EPC0_VSD_NUS_DAYS.W"
            """U.S. Days of Supply of Crude Oil excluding SPR in Number of Days (Days)"""

            WEEKLY_DAYS_OF_SUPPLY_OF_TOTAL_DISTILLATE: str = "PET.W_EPD0_VSD_NUS_DAYS.W"
            """U.S. Days of Supply of Total Distillate in Number of Days (Days)"""

            WEEKLY_WEEKLY_NO_2_HEATING_OIL_RESIDENTIAL_PRICE: str = "PET.W_EPD2F_PRS_NUS_DPG.W"
            """U.S. Weekly No. 2 Heating Oil Residential Price in Dollars per Gallon ($/gal)"""

            WEEKLY_PRODUCT_SUPPLIED_OF_PROPANE_AND_PROPYLENE: str = "PET.WPRUP_NUS_2.W"
            """U.S. Product Supplied of Propane and Propylene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_PRODUCT_SUPPLIED_OF_OTHER_OILS: str = "PET.WWOUP_NUS_2.W"
            """U.S. Product Supplied of Other Oils in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_INPUT_OF_GASOLINE_BLENDING_COMPONENTS: str = "PET.WBCRI_NUS_2.W"
            """U.S. Refiner and Blender Net Input of Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_DISTILLATE_FUEL_OIL_0_TO_15_PPM_SULFUR: str = "PET.WD0ST_NUS_1.W"
            """U.S. Ending Stocks of Distillate Fuel Oil, 0 to 15 ppm Sulfur in Thousand Barrels (Mbbl)"""

            WEEKLY_DAYS_OF_SUPPLY_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.W_EPJK_VSD_NUS_DAYS.W"
            """U.S. Days of Supply of Kerosene-Type Jet Fuel in Number of Days (Days)"""

            WEEKLY_DAYS_OF_SUPPLY_OF_TOTAL_GASOLINE: str = "PET.W_EPM0_VSD_NUS_DAYS.W"
            """U.S. Days of Supply of Total Gasoline in Number of Days (Days)"""

            WEEKLY_ENDING_STOCKS_OF_ASPHALT_AND_ROAD_OIL: str = "PET.W_EPPA_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of Asphalt and Road Oil in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_KEROSENE: str = "PET.W_EPPK_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of Kerosene in Thousand Barrels (Mbbl)"""

            WEEKLY_SUPPLY_ADJUSTMENT_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_15_TO_500_PPM_SULFUR: str = "PET.W_EPDM10_VUA_NUS_2.W"
            """U.S. Supply Adjustment of Distillate Fuel Oil, Greater than 15 to 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_CONVENTIONAL_MOTOR_GASOLINE_WITH_FUEL_ETHANOL: str = "PET.WG5IM_NUS-Z00_2.W"
            """U.S. Imports of Conventional Motor Gasoline with Fuel Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_OTHER_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.WG6IM_NUS-Z00_2.W"
            """U.S. Imports of Other Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_DISTILLATE_FUEL_OIL_0_TO_15_PPM_SULFUR: str = "PET.WD0IM_NUS-Z00_2.W"
            """U.S. Imports of Distillate Fuel Oil, 0 to 15 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_15_TO_500_PPM_SULFUR: str = "PET.WD1IM_NUS-Z00_2.W"
            """U.S. Imports of Distillate Fuel Oil, Greater than 15 to 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_500_TO_2000_PPM_SULFUR: str = "PET.WD2IM_NUS-Z00_2.W"
            """U.S. Imports of Distillate Fuel Oil, Greater than 500 to 2000 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_PROPANE_AND_PROPYLENE: str = "PET.WPRIM_NUS-Z00_2.W"
            """U.S. Imports of Propane and Propylene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_CONVENTIONAL_GTAB_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO7IM_NUS-Z00_2.W"
            """U.S. Imports of Conventional GTAB Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_2000_PPM_SULFUR: str = "PET.WD3IM_NUS-Z00_2.W"
            """U.S. Imports of Distillate Fuel Oil, Greater than 2000 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_REFORMULATED_MOTOR_GASOLINE_WITH_FUEL_ALCOHOL: str = "PET.WG1IM_NUS-Z00_2.W"
            """U.S. Imports of Reformulated Motor Gasoline with Fuel ALcohol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.WG4IM_NUS-Z00_2.W"
            """U.S. Imports of Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_CONVENTIONAL_OTHER_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO9IM_NUS-Z00_2.W"
            """U.S. Imports of Conventional Other Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_CONVENTIONAL_CBOB_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO6IM_NUS-Z00_2.W"
            """U.S. Imports of Conventional CBOB Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_KEROSENE: str = "PET.W_EPPK_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Kerosene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_KEROSENE: str = "PET.W_EPPK_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Kerosene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_OTHER_OILS_EXCLUDING_FUEL_ETHANOL: str = "PET.W_EPPO6_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of Other Oils (Excluding Fuel Ethanol) in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_RESIDUAL_FUEL_OIL: str = "PET.W_EPPR_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Residual Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_REFORMULATED_MOTOR_GASOLINE: str = "PET.W_EPM0R_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_REFORMULATED_MOTOR_GASOLINE: str = "PET.W_EPM0R_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_FUEL_ETHANOL: str = "PET.W_EPOOXE_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of Fuel Ethanol in Thousand Barrels (Mbbl)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL: str = "PET.W_EPD0_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Distillate Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL: str = "PET.W_EPD0_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Distillate Fuel Oil in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.W_EPJK_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_KEROSENE_TYPE_JET_FUEL: str = "PET.W_EPJK_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Kerosene-Type Jet Fuel in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_PROPANE_RESIDENTIAL_PRICE: str = "PET.W_EPLLPA_PRS_NUS_DPG.W"
            """U.S. Propane Residential Price in Dollars per Gallon ($/gal)"""

            WEEKLY_PROPANE_WHOLESALE_RESALE_PRICE: str = "PET.W_EPLLPA_PWR_NUS_DPG.W"
            """U.S. Propane Wholesale/Resale Price in Dollars per Gallon ($/gal)"""

            WEEKLY_REFINER_AND_BLENDER_NET_INPUT_OF_MOTOR_GASOLINE_BLENDING_COMPONENTS_RBOB: str = "PET.W_EPOBGRR_YIR_NUS_MBBLD.W"
            """U.S. Refiner and Blender Net Input of Motor Gasoline Blending Components, RBOB in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_NGPLS_LRGS_EXCLUDING_PROPANE_PROPYLENE: str = "PET.W_EPL0XP_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of NGPLs/LRGs (Excluding Propane/Propylene) in Thousand Barrels (Mbbl)"""

            WEEKLY_DAYS_OF_SUPPLY_OF_PROPANE_PROPYLENE: str = "PET.W_EPLLPZ_VSD_NUS_DAYS.W"
            """U.S. Days of Supply of Propane/Propylene in Number of Days (Days)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.W_EPM0C_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.W_EPM0C_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_SUPPLY_ADJUSTMENT_OF_FINISHED_MOTOR_GASOLINE: str = "PET.W_EPM0F_VUA_NUS_MBBLD.W"
            """U.S. Supply Adjustment of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_FINISHED_MOTOR_GASOLINE: str = "PET.W_EPM0F_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_FINISHED_MOTOR_GASOLINE: str = "PET.W_EPM0F_YPR_NUS_MBBLD.W"
            """U.S. Refiner and Blender Net Production of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_FINISHED_MOTOR_GASOLINE: str = "PET.W_EPM0F_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_500_PPM_SULFUR: str = "PET.W_EPD00H_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Distillate Fuel Oil, Greater Than 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_500_PPM_SULFUR: str = "PET.W_EPD00H_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Distillate Fuel Oil, Greater Than 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_15_TO_500_PPM_SULFUR: str = "PET.W_EPDM10_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Distillate Fuel Oil, Greater than 15 to 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_GREATER_THAN_15_TO_500_PPM_SULFUR: str = "PET.W_EPDM10_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Distillate Fuel Oil, Greater than 15 to 500 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_0_TO_15_PPM_SULFUR: str = "PET.W_EPDXL0_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Distillate Fuel Oil, 0 to 15 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_DISTILLATE_FUEL_OIL_0_TO_15_PPM_SULFUR: str = "PET.W_EPDXL0_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Distillate Fuel Oil, 0 to 15 ppm Sulfur in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_CONVENTIONAL_MOTOR_GASOLINE_WITH_FUEL_ETHANOL: str = "PET.W_EPM0CA_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Conventional Motor Gasoline with Fuel Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_CONVENTIONAL_MOTOR_GASOLINE_WITH_FUEL_ETHANOL: str = "PET.W_EPM0CA_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Conventional Motor Gasoline with Fuel Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_OTHER_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.W_EPM0CO_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Other Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_OTHER_CONVENTIONAL_MOTOR_GASOLINE: str = "PET.W_EPM0CO_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Other Conventional Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_REFORMULATED_MOTOR_GASOLINE_WITH_FUEL_ALCOHOL: str = "PET.W_EPM0RA_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Reformulated Motor Gasoline with Fuel ALcohol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_REFORMULATED_MOTOR_GASOLINE_WITH_FUEL_ALCOHOL: str = "PET.W_EPM0RA_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Reformulated Motor Gasoline with Fuel ALcohol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_OXYGENATE_PLANT_PRODUCTION_OF_FUEL_ETHANOL: str = "PET.W_EPOOXE_YOP_NUS_MBBLD.W"
            """U.S. Oxygenate Plant Production of Fuel Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_MOTOR_GASOLINE_FINISHED_CONVENTIONAL_ED_55_AND_LOWER: str = "PET.W_EPM0CAL55_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Motor Gasoline, Finished, Conventional, Ed55 and Lower in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_FINISHED_CONVENTIONAL_MOTOR_GASOLINE_ED_55_AND_LOWER: str = "PET.W_EPM0CAL55_YPT_NUS_MBBLD.W"
            """U.S. Refiner and Blender Net Production of Finished Conventional Motor Gasoline, Ed 55 and Lower in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_MOTOR_GASOLINE_FINISHED_CONVENTIONAL_ED_55_AND_LOWER: str = "PET.W_EPM0CAL55_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Motor Gasoline, Finished, Conventional, Ed55 and Lower in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_EXPORTS_OF_FINISHED_MOTOR_GASOLINE: str = "PET.W_EPM0F_EEX_NUS-Z00_MBBLD.W"
            """U.S. Exports of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_FINISHED_MOTOR_GASOLINE: str = "PET.W_EPM0F_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Finished Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_OTHER_REFORMULATED_MOTOR_GASOLINE: str = "PET.W_EPM0RO_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Other Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_OTHER_FINISHED_REFORMULATED_MOTOR_GASOLINE: str = "PET.W_EPM0RO_YPT_NUS_MBBLD.W"
            """U.S. Refiner and Blender Net Production of Other Finished Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_OTHER_REFORMULATED_MOTOR_GASOLINE: str = "PET.W_EPM0RO_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Other Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_MOTOR_GASOLINE_BLENDING_COMPONENTS_RBOB: str = "PET.W_EPOBGRR_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of Motor Gasoline Blending Components, RBOB in Thousand Barrels (Mbbl)"""

            WEEKLY_REFINER_AND_BLENDER_NET_INPUT_OF_FUEL_ETHANOL: str = "PET.W_EPOOXE_YIR_NUS_MBBLD.W"
            """U.S. Refiner and Blender Net Input of Fuel Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_MOTOR_GASOLINE_FINISHED_CONVENTIONAL_GREATER_THAN_ED_55: str = "PET.W_EPM0CAG55_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Motor Gasoline, Finished, Conventional, Greater than Ed55 in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_MOTOR_GASOLINE_FINISHED_CONVENTIONAL_ED_55_AND_LOWER: str = "PET.W_EPM0CAL55_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Motor Gasoline, Finished, Conventional, Ed55 and Lower in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_CRUDE_OIL_IMPORTS_FOR_SPR_BY_OTHERS: str = "PET.W_EPC0_IMU_NUS-Z00_MBBLD.W"
            """U.S. Crude Oil Imports for SPR by Others in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CONVENTIONAL_MOTOR_GASOLINE_GREATER_THAN_ED_55: str = "PET.W_EPM0CAG55_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of Conventional Motor Gasoline, Greater than Ed55 in Thousand Barrels (Mbbl)"""

            WEEKLY_IMPORTS_OF_FUEL_ETHANOL: str = "PET.W_EPOOXE_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Fuel Ethanol in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_LIQUEFIED_PETROLEUM_GASSES_LESS_PROPANE_PROPYLENE: str = "PET.W_EPL0XP_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Liquefied Petroleum Gasses Less Propane/Propylene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_EXPORTS_OF_PROPANE_AND_PROPYLENE: str = "PET.W_EPLLPZ_EEX_NUS-Z00_MBBLD.W"
            """U.S. Exports of Propane and Propylene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_OTHER_REFORMULATED_MOTOR_GASOLINE: str = "PET.W_EPM0RO_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Other Reformulated Motor Gasoline in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_BLENDER_NET_PRODUCTION_OF_MOTOR_GASOLINE_FINISHED_CONVENTIONAL_GREATER_THAN_ED_55: str = "PET.W_EPM0CAG55_YPB_NUS_MBBLD.W"
            """U.S. Blender Net Production of Motor Gasoline, Finished, Conventional, Greater Than Ed55 in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_AND_BLENDER_NET_PRODUCTION_OF_FINISHED_CONVENTIONAL_MOTOR_GASOLINE_GREATER_THAN_ED_55: str = "PET.W_EPM0CAG55_YPT_NUS_MBBLD.W"
            """U.S. Refiner and Blender Net Production of Finished Conventional Motor Gasoline, Greater than Ed 55 in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REFINER_NET_PRODUCTION_OF_FINISHED_CONVENTIONAL_MOTOR_GASOLINE_GREATER_THAN_ED_55: str = "PET.W_EPM0CAG55_YPY_NUS_MBBLD.W"
            """U.S. Refiner Net Production of Finished Conventional Motor Gasoline, Greater than Ed 55 in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_CONVENTIONAL_MOTOR_GASOLINE_ED_55_AND_LOWER: str = "PET.W_EPM0CAL55_SAE_NUS_MBBL.W"
            """U.S. Ending Stocks of Conventional Motor Gasoline, Ed55 and Lower in Thousand Barrels (Mbbl)"""

            WEEKLY_IMPORTS_OF_KEROSENE: str = "PET.W_EPPK_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Kerosene in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_EXPORTS_OF_OTHER_OILS: str = "PET.W_EPPO4_EEX_NUS-Z00_MBBLD.W"
            """U.S. Exports of Other Oils in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_OTHER_OILS_EXCLUDING_FUEL_ETHANOL: str = "PET.W_EPPO6_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports of Other Oils (Excluding Fuel Ethanol) in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_FROM_ALL_COUNTRIES_OF_MOTOR_GASOLINE_BLENDING_COMPONENTS_RBOB: str = "PET.W_EPOBGRR_IM0_NUS-Z00_MBBLD.W"
            """U.S. Imports from  All Countries of Motor Gasoline Blending Components, RBOB in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_REGULAR_ALL_FORMULATIONS_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMR_PTE_NUS_DPG.W"
            """U.S. Regular All Formulations Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_MIDGRADE_ALL_FORMULATIONS_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMM_PTE_NUS_DPG.W"
            """U.S. Midgrade All Formulations Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_PREMIUM_ALL_FORMULATIONS_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMP_PTE_NUS_DPG.W"
            """U.S. Premium All Formulations Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_ALL_GRADES_ALL_FORMULATIONS_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPM0_PTE_NUS_DPG.W"
            """U.S. All Grades All Formulations Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_ALL_GRADES_REFORMULATED_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPM0R_PTE_NUS_DPG.W"
            """U.S. All Grades Reformulated Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_MIDGRADE_REFORMULATED_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMMR_PTE_NUS_DPG.W"
            """U.S. Midgrade Reformulated Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_PREMIUM_REFORMULATED_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMPR_PTE_NUS_DPG.W"
            """U.S. Premium Reformulated Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_REGULAR_CONVENTIONAL_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMRU_PTE_NUS_DPG.W"
            """U.S. Regular Conventional Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_REGULAR_REFORMULATED_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMRR_PTE_NUS_DPG.W"
            """U.S. Regular Reformulated Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_NO_2_DIESEL_RETAIL_PRICES: str = "PET.EMD_EPD2D_PTE_NUS_DPG.W"
            """U.S. No 2 Diesel Retail Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_PREMIUM_CONVENTIONAL_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMPU_PTE_NUS_DPG.W"
            """U.S. Premium Conventional Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_MIDGRADE_CONVENTIONAL_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPMMU_PTE_NUS_DPG.W"
            """U.S. Midgrade Conventional Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_ALL_GRADES_CONVENTIONAL_RETAIL_GASOLINE_PRICES: str = "PET.EMM_EPM0U_PTE_NUS_DPG.W"
            """U.S. All Grades Conventional Retail Gasoline Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_NO_2_DIESEL_ULTRA_LOW_SULFUR_015_PPM_RETAIL_PRICES: str = "PET.EMD_EPD2DXL0_PTE_NUS_DPG.W"
            """U.S. No 2 Diesel Ultra Low Sulfur (0-15 ppm) Retail Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_ENDING_STOCKS_EXCLUDING_SPR_AND_INCLUDING_LEASE_STOCK_OF_CRUDE_OIL: str = "PET.W_EPC0_SAX_NUS_MBBL.W"
            """U.S. Ending Stocks excluding SPR and including Lease Stock of Crude Oil in Thousand Barrels (Mbbl)"""

            WEEKLY_NO_2_DIESEL_LOW_SULFUR_15500_PPM_RETAIL_PRICES: str = "PET.EMD_EPD2DM10_PTE_NUS_DPG.W"
            """U.S. No 2 Diesel Low Sulfur (15-500 ppm) Retail Prices in Dollars per Gallon ($/gal)"""

            WEEKLY_IMPORTS_OF_REFORMULATED_RBOB_WITH_ALCOHOL_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO3IM_NUS-Z00_2.W"
            """U.S. Imports of Reformulated RBOB with Alcohol Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_IMPORTS_OF_REFORMULATED_RBOB_WITH_ETHER_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO4IM_NUS-Z00_2.W"
            """U.S. Imports of Reformulated RBOB with Ether Gasoline Blending Components in Thousand Barrels per Day (Mbbl/d)"""

            WEEKLY_ENDING_STOCKS_OF_REFORMULATED_GTAB_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO2ST_NUS_1.W"
            """U.S. Ending Stocks of Reformulated GTAB Gasoline Blending Components in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_REFORMULATED_RBOB_WITH_ALCOHOL_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO3ST_NUS_1.W"
            """U.S. Ending Stocks of Reformulated RBOB with Alcohol Gasoline Blending Components in Thousand Barrels (Mbbl)"""

            WEEKLY_ENDING_STOCKS_OF_REFORMULATED_RBOB_WITH_ETHER_GASOLINE_BLENDING_COMPONENTS: str = "PET.WO4ST_NUS_1.W"
            """U.S. Ending Stocks of Reformulated RBOB with Ether Gasoline Blending Components in Thousand Barrels (Mbbl)"""

        class EquatorialGuinea(System.Object):
            """Equatorial Guinea"""

            WEEKLY_IMPORTS_FROM_EQUATORIAL_GUINEA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NEK_MBBLD.W"
            """U.S. Imports from Equatorial Guinea of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Iraq(System.Object):
            """Iraq"""

            WEEKLY_IMPORTS_FROM_IRAQ_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NIZ_MBBLD.W"
            """U.S. Imports from Iraq of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Kuwait(System.Object):
            """Kuwait"""

            WEEKLY_IMPORTS_FROM_KUWAIT_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NKU_MBBLD.W"
            """U.S. Imports from Kuwait of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Mexico(System.Object):
            """Mexico"""

            WEEKLY_IMPORTS_FROM_MEXICO_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NMX_MBBLD.W"
            """U.S. Imports from Mexico of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Nigeria(System.Object):
            """Nigeria"""

            WEEKLY_IMPORTS_FROM_NIGERIA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NNI_MBBLD.W"
            """U.S. Imports from Nigeria of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Norway(System.Object):
            """Norway"""

            WEEKLY_IMPORTS_FROM_NORWAY_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NNO_MBBLD.W"
            """U.S. Imports from Norway of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Russia(System.Object):
            """Russia"""

            WEEKLY_IMPORTS_FROM_RUSSIA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NRS_MBBLD.W"
            """U.S. Imports from Russia of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class SaudiArabia(System.Object):
            """Saudi Arabia"""

            WEEKLY_IMPORTS_FROM_SAUDI_ARABIA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NSA_MBBLD.W"
            """U.S. Imports from Saudi Arabia of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class UnitedKingdom(System.Object):
            """United Kingdom"""

            WEEKLY_IMPORTS_FROM_UNITED_KINGDOM_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NUK_MBBLD.W"
            """U.S. Imports from United Kingdom of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Venezuela(System.Object):
            """Venezuela"""

            WEEKLY_IMPORTS_FROM_VENEZUELA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NVE_MBBLD.W"
            """U.S. Imports from Venezuela of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Algeria(System.Object):
            """Algeria"""

            WEEKLY_IMPORTS_FROM_ALGERIA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NAG_MBBLD.W"
            """U.S. Imports from Algeria of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Angola(System.Object):
            """Angola"""

            WEEKLY_IMPORTS_FROM_ANGOLA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NAO_MBBLD.W"
            """U.S. Imports from Angola of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Brazil(System.Object):
            """Brazil"""

            WEEKLY_IMPORTS_FROM_BRAZIL_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NBR_MBBLD.W"
            """U.S. Imports from Brazil of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Canada(System.Object):
            """Canada"""

            WEEKLY_IMPORTS_FROM_CANADA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NCA_MBBLD.W"
            """U.S. Imports from Canada of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Congo(System.Object):
            """Congo"""

            WEEKLY_IMPORTS_FROM_CONGO_BRAZZAVILLE_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NCF_MBBLD.W"
            """U.S. Imports from Congo (Brazzaville) of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Colombia(System.Object):
            """Colombia"""

            WEEKLY_IMPORTS_FROM_COLOMBIA_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NCO_MBBLD.W"
            """U.S. Imports from Colombia of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

        class Ecuador(System.Object):
            """Ecuador"""

            WEEKLY_IMPORTS_FROM_ECUADOR_OF_CRUDE_OIL: str = "PET.W_EPC0_IM0_NUS-NEC_MBBLD.W"
            """U.S. Imports from Ecuador of Crude Oil in Thousand Barrels per Day (Mbbl/d)"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Determines the location of the data
        
        :param config: Subscription configuration
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: Location of the data as a SubscriptionDataSource.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance of USEnergy.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied
        to an underlying symbol and requires that corporate
        events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverLobbyingUniverse(QuantConnect.Data.BaseData):
    """Example custom data type"""

    @property
    def client(self) -> str:
        """Full name of the lobbying client"""
        ...

    @property.setter
    def client(self, value: str) -> None:
        ...

    @property
    def issue(self) -> str:
        """Category of legislation that is being lobbied for"""
        ...

    @property.setter
    def issue(self, value: str) -> None:
        ...

    @property
    def specific_issue(self) -> str:
        """Specific piece of legislation being lobbied for"""
        ...

    @property.setter
    def specific_issue(self, value: str) -> None:
        ...

    @property
    def amount(self) -> typing.Optional[float]:
        """The Size of spending instance (USD)"""
        ...

    @property.setter
    def amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverLobbyings(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Collection of Quiver Lobbying data"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Formats a string with QuiverLobbying data
        
        :returns: string containing QuiverLobbying information.
        """
        ...


class QuiverLobbying(QuantConnect.Data.BaseData):
    """Quiver Lobbying data"""

    @property
    def client(self) -> str:
        """Full name of the lobbying client"""
        ...

    @property.setter
    def client(self, value: str) -> None:
        ...

    @property
    def issue(self) -> str:
        """Category of legislation that is being lobbied for"""
        ...

    @property.setter
    def issue(self, value: str) -> None:
        ...

    @property
    def specific_issue(self) -> str:
        """Specific piece of legislation being lobbied for"""
        ...

    @property.setter
    def specific_issue(self, value: str) -> None:
        ...

    @property
    def amount(self) -> typing.Optional[float]:
        """The Size of spending instance (USD)"""
        ...

    @property.setter
    def amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class CBOE(QuantConnect.Data.Market.TradeBar):
    """CBOE data source"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    def __init__(self) -> None:
        """Creates a new instance of the object"""
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """Gets the source location of the CBOE file"""
        ...

    def is_sparse_data(self) -> bool:
        """
        Determines if data source is sparse
        
        :returns: false.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reads the data from the source and creates a BaseData instance
        
        :param config: Configuration
        :param line: Line of data
        :param date: Date we're requesting data for
        :param is_live_mode: Is live mode
        :returns: New BaseData instance to be used in the algorithm.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Determines whether the data source requires mapping
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Converts the instance to a string
        
        :returns: String containing open, high, low, close.
        """
        ...


class VIXCentralContango(QuantConnect.Data.BaseData):
    """VIXCentral Contango"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def front_month(self) -> int:
        """The month of the front month contract (possible values: 1 - 12)"""
        ...

    @property.setter
    def front_month(self, value: int) -> None:
        ...

    @property
    def f_1(self) -> float:
        """Front month contract"""
        ...

    @property.setter
    def f_1(self, value: float) -> None:
        ...

    @property
    def f_2(self) -> float:
        """Contract 1 month away from the front month contract"""
        ...

    @property.setter
    def f_2(self, value: float) -> None:
        ...

    @property
    def f_3(self) -> float:
        """Contract 2 months away from the front month contract"""
        ...

    @property.setter
    def f_3(self, value: float) -> None:
        ...

    @property
    def f_4(self) -> float:
        """Contract 3 months away from the front month contract"""
        ...

    @property.setter
    def f_4(self, value: float) -> None:
        ...

    @property
    def f_5(self) -> float:
        """Contract 4 months away from the front month contract"""
        ...

    @property.setter
    def f_5(self, value: float) -> None:
        ...

    @property
    def f_6(self) -> float:
        """Contract 5 months away from the front month contract"""
        ...

    @property.setter
    def f_6(self, value: float) -> None:
        ...

    @property
    def f_7(self) -> float:
        """Contract 6 months away from the front month contract"""
        ...

    @property.setter
    def f_7(self, value: float) -> None:
        ...

    @property
    def f_8(self) -> float:
        """Contract 7 months away from the front month contract"""
        ...

    @property.setter
    def f_8(self, value: float) -> None:
        ...

    @property
    def f_9(self) -> typing.Optional[float]:
        """Contract 8 months away from the front month contract"""
        ...

    @property.setter
    def f_9(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def f_10(self) -> typing.Optional[float]:
        """Contract 9 months away from the front month contract"""
        ...

    @property.setter
    def f_10(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def f_11(self) -> typing.Optional[float]:
        """Contract 10 months away from the front month contract"""
        ...

    @property.setter
    def f_11(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def f_12(self) -> typing.Optional[float]:
        """Contract 11 months away from the front month contract"""
        ...

    @property.setter
    def f_12(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def contango_f_2_minus_f_1(self) -> float:
        """Percentage change between contract F2 and F1, calculated as: (F2 - F1) / F1"""
        ...

    @property.setter
    def contango_f_2_minus_f_1(self, value: float) -> None:
        ...

    @property
    def contango_f_7_minus_f_4(self) -> float:
        """Percentage change between contract F7 and F4, calculated as: (F7 - F4) / F4"""
        ...

    @property.setter
    def contango_f_7_minus_f_4(self, value: float) -> None:
        ...

    @property
    def contango_f_7_minus_f_4_div_3(self) -> float:
        """Percentage change between contract F7 and F4 divided by 3, calculated as: ((F7 - F4) / F4) / 3"""
        ...

    @property.setter
    def contango_f_7_minus_f_4_div_3(self, value: float) -> None:
        ...

    @property
    def period(self) -> datetime.timedelta:
        """The timespan that each data point covers"""
        ...

    @property.setter
    def period(self, value: datetime.timedelta) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The ending time of the data point"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    def __init__(self) -> None:
        """Creates a new instance of the object"""
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """Gets the source location of the VIXCentral data"""
        ...

    def is_sparse_data(self) -> bool:
        """
        Determines if data source is sparse
        
        :returns: false.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reads the data from the source and creates a BaseData instance
        
        :param config: Configuration
        :param line: Line of data
        :param date: Date we're requesting data for
        :param is_live_mode: Is live mode
        :returns: New BaseData instance to be used in the algorithm.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Determines whether the data source requires mapping
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Converts the instance to a string
        
        :returns: String containing open, high, low, close.
        """
        ...


class TransactionDirectionJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[QuantConnect.Orders.OrderDirection, str]):
    """Converts Quiver Quantitative QuiverCongressDataPoint.Transaction to OrderDirection"""

    @overload
    def convert(self, value: QuantConnect.Orders.OrderDirection) -> str:
        """
        Convert OrderDirection to string
        
        This method is protected.
        
        :param value: OrderDirection to convert
        :returns: Resulting string.
        """
        ...

    @overload
    def convert(self, value: str) -> QuantConnect.Orders.OrderDirection:
        """
        Convert string to OrderDirection
        
        This method is protected.
        
        :param value: string to convert
        :returns: Resulting OrderDirection.
        """
        ...

    @overload
    def convert(self, value: QuantConnect.Orders.OrderDirection) -> str:
        """
        Convert OrderDirection to string
        
        This method is protected.
        
        :param value: OrderDirection to convert
        :returns: Resulting string.
        """
        ...

    @overload
    def convert(self, value: str) -> QuantConnect.Orders.OrderDirection:
        """
        Convert string to OrderDirection
        
        This method is protected.
        
        :param value: string to convert
        :returns: Resulting OrderDirection.
        """
        ...


class QuiverCongress(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Personal stock transactions by U.S. Representatives"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
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

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Formats a string with the Quiver Congress information.
        
        :returns: string containing Quiver Congress information.
        """
        ...


class QuiverQuantCongressUniverse(QuantConnect.DataSource.QuiverCongress):
    """Universe Selection helper class for QuiverQuant Congress dataset"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class Party(Enum):
    """Political Parties of the United States of America"""

    INDEPENDENT = 0
    """Not affiliated with any political party."""

    REPUBLICAN = 1
    """Republican Party. https://en.wikipedia.org/wiki/Republican_Party_(United_States)"""

    DEMOCRATIC = 2
    """Democratic Party. https://en.wikipedia.org/wiki/Democratic_Party_(United_States)"""


class Congress(Enum):
    """United States of America Legislative Branch House of Congress"""

    SENATE = 0
    """The United States Senate"""

    REPRESENTATIVES = 1
    """The United States House of Representatives"""


class QuiverCongressDataPoint(QuantConnect.Data.BaseData):
    """Single data point for QuiverCongress data"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def record_date(self) -> datetime.datetime:
        """The date the transaction was recorded by QuiverQuant. Value will always exist."""
        ...

    @property.setter
    def record_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def updated_at(self) -> datetime.datetime:
        """The date the recorded transaction was updated by QuiverQuant. Alias for EndTime."""
        ...

    @property
    def report_date(self) -> typing.Optional[datetime.datetime]:
        """The date the transaction was reported. Value will always exist."""
        ...

    @property.setter
    def report_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def transaction_date(self) -> datetime.datetime:
        """The date the transaction took place"""
        ...

    @property.setter
    def transaction_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def representative(self) -> str:
        """The Representative making the transaction"""
        ...

    @property.setter
    def representative(self, value: str) -> None:
        ...

    @property
    def transaction(self) -> QuantConnect.Orders.OrderDirection:
        """The type of transaction"""
        ...

    @property.setter
    def transaction(self, value: QuantConnect.Orders.OrderDirection) -> None:
        ...

    @property
    def amount(self) -> typing.Optional[float]:
        """The amount of the transaction (in USD). The Representative can report a range (see MaximumAmount)."""
        ...

    @property.setter
    def amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def maximum_amount(self) -> typing.Optional[float]:
        """The maximum amount of the transaction (in USD). The Representative can report a range (see Amount)."""
        ...

    @property.setter
    def maximum_amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def house(self) -> QuantConnect.DataSource.Congress:
        """The Chamber of Congress that the trader belongs to"""
        ...

    @property.setter
    def house(self, value: QuantConnect.DataSource.Congress) -> None:
        ...

    @property
    def party(self) -> QuantConnect.DataSource.Party:
        """The political party that the trader belongs to"""
        ...

    @property.setter
    def party(self, value: QuantConnect.DataSource.Party) -> None:
        ...

    @property
    def district(self) -> str:
        """The district that the trader belongs to (null or empty for Senators)"""
        ...

    @property.setter
    def district(self, value: str) -> None:
        ...

    @property
    def state(self) -> str:
        """The state that the trader belongs to"""
        ...

    @property.setter
    def state(self, value: str) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time the data point ends at and becomes available to the algorithm"""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of QuiverCongressDataPoint"""
        ...

    @overload
    def __init__(self, csvLine: str) -> None:
        """
        Creates a new instance of QuiverCongressDataPoint from a CSV line
        
        :param csvLine: CSV line
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
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

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Quiver Congress object.
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

    def to_string(self) -> str:
        """Formats a string with the Quiver Congress information."""
        ...


class QuiverGovernmentContractUniverse(QuantConnect.Data.BaseData):
    """Universe Selection helper class for QuiverQuant Government Contracts dataset"""

    @property
    def description(self) -> str:
        """Contract description"""
        ...

    @property.setter
    def description(self, value: str) -> None:
        ...

    @property
    def agency(self) -> str:
        """Awarding Agency Name"""
        ...

    @property.setter
    def agency(self, value: str) -> None:
        ...

    @property
    def amount(self) -> typing.Optional[float]:
        """Total dollars obligated under the given contract"""
        ...

    @property.setter
    def amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverGovernmentContracts(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Collection of Government Contracts by Agencies"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
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

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Formats a string with QuiverGovernmentContract data
        
        :returns: string containing QuiverGovernmentContract information.
        """
        ...


class QuiverGovernmentContract(QuantConnect.Data.BaseData):
    """Government Contract by Agencies"""

    @property
    def description(self) -> str:
        """Contract description"""
        ...

    @property.setter
    def description(self, value: str) -> None:
        ...

    @property
    def agency(self) -> str:
        """Awarding Agency Name"""
        ...

    @property.setter
    def agency(self, value: str) -> None:
        ...

    @property
    def amount(self) -> float:
        """Total dollars obligated under the given contract"""
        ...

    @property.setter
    def amount(self, value: float) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time the data point ends at and becomes available to the algorithm"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverWikipedia(QuantConnect.Data.BaseData):
    """Wikipedia Page Views for the specified company"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def date(self) -> datetime.datetime:
        """The date of the Page View count"""
        ...

    @property.setter
    def date(self, value: datetime.datetime) -> None:
        ...

    @property
    def page_views(self) -> typing.Optional[float]:
        """The company's Wikipedia Page Views on the given date"""
        ...

    @property.setter
    def page_views(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def week_percent_change(self) -> typing.Optional[float]:
        """
        The view count % change over the week prior to the date.
        Represented as a whole number (e.g. 100% = 100.0)
        """
        ...

    @property.setter
    def week_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def month_percent_change(self) -> typing.Optional[float]:
        """
        The view count % change over the month prior to the date
        Represented as a whole number (e.g. 100% = 100.0)
        """
        ...

    @property.setter
    def month_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time the data point ends at and becomes available to the algorithm"""
        ...

    @overload
    def __init__(self) -> None:
        """Required for successful Json.NET deserialization"""
        ...

    @overload
    def __init__(self, csvLine: str) -> None:
        """
        Creates a new instance of QuiverWikipedia from a CSV line
        
        :param csvLine: CSV line
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Quiver Wikipedia object.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the Quiver Wikipedia information."""
        ...


class QuiverWikipediaUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Universe Selection helper class for QuiverWikipedia dataset"""

    @property
    def date(self) -> datetime.datetime:
        """The date of the Page View count"""
        ...

    @property.setter
    def date(self, value: datetime.datetime) -> None:
        ...

    @property
    def page_views(self) -> typing.Optional[float]:
        """The company's Wikipedia Page Views on the given date"""
        ...

    @property.setter
    def page_views(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def week_percent_change(self) -> typing.Optional[float]:
        """
        The view count % change over the week prior to the date.
        Represented as a whole number (e.g. 100% = 100.0)
        """
        ...

    @property.setter
    def week_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def month_percent_change(self) -> typing.Optional[float]:
        """
        The view count % change over the month prior to the date
        Represented as a whole number (e.g. 100% = 100.0)
        """
        ...

    @property.setter
    def month_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time the data point ends at and becomes available to the algorithm"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clones this instance"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...


class CryptoSlamNFTSales(QuantConnect.Data.BaseData):
    """CryptoSlam NFT Sales dataset"""

    @property
    def total_transactions(self) -> int:
        """The number of NFT transaction made within this blockchain"""
        ...

    @property.setter
    def total_transactions(self, value: int) -> None:
        ...

    @property
    def unique_buyers(self) -> int:
        """The number of unique buyers of NFT within this blockchain"""
        ...

    @property.setter
    def unique_buyers(self, value: int) -> None:
        ...

    @property
    def unique_sellers(self) -> int:
        """The number of unique sellers of NFT within this blockchain"""
        ...

    @property.setter
    def unique_sellers(self, value: int) -> None:
        ...

    @property
    def total_price_usd(self) -> float:
        """The total transaction value (in USD) of NFT within this blockchain"""
        ...

    @property.setter
    def total_price_usd(self, value: float) -> None:
        ...

    @property
    def period(self) -> datetime.timedelta:
        """Time passed between the date of the data and the time the data became available to us"""
        ...

    @property.setter
    def period(self, value: datetime.timedelta) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class NasdaqDataLink(QuantConnect.Data.DynamicData):
    """Nasdaq Data Link dataset"""

    @property
    def value_column_name(self) -> str:
        """
        Name of the column is going to be used for the field Value
        
        This property is protected.
        """
        ...

    @property.setter
    def value_column_name(self, value: str) -> None:
        ...

    is_auth_code_set: bool
    """Flag indicating whether or not the Nasdaq Data Link auth code has been set yet"""

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
        """Gets a time span of one day"""
        ...

    @overload
    def __init__(self) -> None:
        """Default NasdaqDataLink constructor uses Close as its value column"""
        ...

    @overload
    def __init__(self, valueColumnName: str) -> None:
        """
        Constructor for creating customized NasdaqDataLink instance which doesn't use close, price, settle or value as its value item.
        
        This method is protected.
        
        :param valueColumnName: The name of the column we want to use as reference, the Value property
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Using the Nasdaq Data Link V3 API automatically set the URL for the dataset.
        
        :param config: Subscription configuration object
        :param date: Date of the data file we're looking for
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: STRING API Url for Nasdaq Data Link.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: CSV line of data from the souce
        :param date: Date of the requested line
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    @staticmethod
    def set_auth_code(auth_code: str) -> None:
        """Set the auth code for the Nasdaq Data Link set to the QuantConnect auth code."""
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...


class QuandlBitfinexDownloaderProgram(System.Object):
    """This class has no documentation."""

    @staticmethod
    def quandl_bitfinex_downloader(from_date: typing.Union[datetime.datetime, datetime.date], api_key: str) -> None:
        """Quandl Bitfinex Toolbox Project For LEAN Algorithmic Trading Engine."""
        ...


class NasdaqBitfinexDownloader(System.Object, QuantConnect.IDataDownloader):
    """Nasdaq Bitfinex Data Downloader class"""

    @property
    def _api_key(self) -> str:
        """This field is protected."""
        ...

    def __init__(self, apiKey: str) -> None:
        """
        Initializes a new instance of the NasdaqBitfinexDownloader class
        
        :param apiKey: The nasdaq api key
        """
        ...

    def get(self, data_downloader_get_parameters: QuantConnect.DataDownloaderGetParameters) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Get historical data enumerable for Bitfinex from Nasdaq
        
        :param data_downloader_get_parameters: model class for passing in parameters for historical data
        :returns: Enumerable of base data for this symbol.
        """
        ...


class QuandlBitfinexDownloader(QuantConnect.DataSource.NasdaqBitfinexDownloader):
    """Quandl Bitfinex Data Downloader class"""

    def __init__(self, apiKey: str) -> None:
        """
        Initializes a new instance of the QuandlBitfinexDownloader class
        
        :param apiKey: The quandl api key
        """
        ...


class NasdaqBitfinexDownloaderProgram(System.Object):
    """This class has no documentation."""

    @staticmethod
    def nasdaq_bitfinex_downloader(from_date: typing.Union[datetime.datetime, datetime.date], api_key: str) -> None:
        """Nasdaq Bitfinex Toolbox Project For LEAN Algorithmic Trading Engine."""
        ...


class BitcoinMetadata(QuantConnect.Data.BaseData):
    """Blockchain Bitcoin Metadata dataset"""

    @property
    def difficulty(self) -> float:
        """A relative measure of how difficult it is to find a new block. The difficulty is adjusted periodically as a function of how much hashing power has been deployed by the network of miners."""
        ...

    @property.setter
    def difficulty(self, value: float) -> None:
        ...

    @property
    def my_wallet_numberof_users(self) -> float:
        """Number of wallets hosts using our My Wallet Service."""
        ...

    @property.setter
    def my_wallet_numberof_users(self, value: float) -> None:
        ...

    @property
    def average_block_size(self) -> float:
        """The average block size in MB."""
        ...

    @property.setter
    def average_block_size(self, value: float) -> None:
        ...

    @property
    def blockchain_size(self) -> float:
        """The total size of all block headers and transactions. Not including database indexes."""
        ...

    @property.setter
    def blockchain_size(self, value: float) -> None:
        ...

    @property
    def median_transaction_confirmation_time(self) -> float:
        """The median time for a transaction to be accepted into a mined block and added to the public ledger (note: only includes transactions with miner fees)."""
        ...

    @property.setter
    def median_transaction_confirmation_time(self, value: float) -> None:
        ...

    @property
    def miners_revenue(self) -> float:
        """Total value of coinbase block rewards and transaction fees paid to miners."""
        ...

    @property.setter
    def miners_revenue(self, value: float) -> None:
        ...

    @property
    def hash_rate(self) -> float:
        """The estimated number of tera hashes per second (trillions of hashes per second) the Bitcoin network is performing"""
        ...

    @property.setter
    def hash_rate(self, value: float) -> None:
        ...

    @property
    def cost_per_transaction(self) -> float:
        """The miners revenue divided by the number of transactions."""
        ...

    @property.setter
    def cost_per_transaction(self, value: float) -> None:
        ...

    @property
    def cost_percentof_transaction_volume(self) -> float:
        """The miners revenue as percentage of the transaction volume."""
        ...

    @property.setter
    def cost_percentof_transaction_volume(self, value: float) -> None:
        ...

    @property
    def estimated_transaction_volume_usd(self) -> float:
        """The Estimated Transaction Value in USD value."""
        ...

    @property.setter
    def estimated_transaction_volume_usd(self, value: float) -> None:
        ...

    @property
    def estimated_transaction_volume(self) -> float:
        """The total estimated value of transactions on the Bitcoin blockchain (does not include coins returned to sender as change)."""
        ...

    @property.setter
    def estimated_transaction_volume(self, value: float) -> None:
        ...

    @property
    def total_output_volume(self) -> float:
        """The total value of all transaction outputs per day (includes coins returned to the sender as change)."""
        ...

    @property.setter
    def total_output_volume(self, value: float) -> None:
        ...

    @property
    def numberof_transactionper_block(self) -> float:
        """The average number of transactions per block."""
        ...

    @property.setter
    def numberof_transactionper_block(self, value: float) -> None:
        ...

    @property
    def numberof_unique_bitcoin_addresses_used(self) -> float:
        """The total number of unique addresses used on the Bitcoin blockchain."""
        ...

    @property.setter
    def numberof_unique_bitcoin_addresses_used(self, value: float) -> None:
        ...

    @property
    def numberof_transactions_excluding_popular_addresses(self) -> float:
        """The total number of Bitcoin transactions, excluding those involving any of the network's 100 most popular addresses."""
        ...

    @property.setter
    def numberof_transactions_excluding_popular_addresses(self, value: float) -> None:
        ...

    @property
    def total_numberof_transactions(self) -> float:
        """The Total Number of transactions."""
        ...

    @property.setter
    def total_numberof_transactions(self, value: float) -> None:
        ...

    @property
    def numberof_transactions(self) -> float:
        """The number of daily confirmed Bitcoin transactions."""
        ...

    @property.setter
    def numberof_transactions(self, value: float) -> None:
        ...

    @property
    def total_transaction_fees_usd(self) -> float:
        """The total value of all transaction fees in USD paid to miners (not including the coinbase value of block rewards)."""
        ...

    @property.setter
    def total_transaction_fees_usd(self, value: float) -> None:
        ...

    @property
    def total_transaction_fees(self) -> float:
        """The total value of all transaction fees in Bitcoin paid to miners (not including the coinbase value of block rewards)."""
        ...

    @property.setter
    def total_transaction_fees(self, value: float) -> None:
        ...

    @property
    def market_capitalization(self) -> float:
        """The total USD value of bitcoin supply in circulation, as calculated by the daily average market price across major exchanges."""
        ...

    @property.setter
    def market_capitalization(self, value: float) -> None:
        ...

    @property
    def total_bitcoins(self) -> float:
        """The total number of bitcoins that have already been mined; in other words, the current supply of bitcoins on the network."""
        ...

    @property.setter
    def total_bitcoins(self, value: float) -> None:
        ...

    @property
    def my_wallet_numberof_transaction_per_day(self) -> float:
        """Number of transactions made by My Wallet Users per day."""
        ...

    @property.setter
    def my_wallet_numberof_transaction_per_day(self, value: float) -> None:
        ...

    @property
    def my_wallet_transaction_volume(self) -> float:
        """24hr Transaction Volume of our web wallet service."""
        ...

    @property.setter
    def my_wallet_transaction_volume(self, value: float) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverWallStreetBets(QuantConnect.Data.BaseData):
    """Mentions of the given company's ticker in the WallStreetBets daily discussion thread"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def date(self) -> datetime.datetime:
        """Date of the daily discussion thread"""
        ...

    @property.setter
    def date(self, value: datetime.datetime) -> None:
        ...

    @property
    def mentions(self) -> int:
        """The number of mentions on the given date"""
        ...

    @property.setter
    def mentions(self, value: int) -> None:
        ...

    @property
    def rank(self) -> int:
        """This ticker's rank on the given date (as determined by total number of mentions)"""
        ...

    @property.setter
    def rank(self, value: int) -> None:
        ...

    @property
    def sentiment(self) -> float:
        """
        Average sentiment of all comments containing the given ticker on this date. Sentiment is calculated using VADER sentiment analysis.
        The value can range between -1 and +1. Negative values imply negative sentiment, whereas positive values imply positive sentiment.
        """
        ...

    @property.setter
    def sentiment(self, value: float) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time the data point ends at and becomes available to the algorithm"""
        ...

    @overload
    def __init__(self) -> None:
        """Required for successful Json.NET deserialization"""
        ...

    @overload
    def __init__(self, csvLine: str) -> None:
        """
        Creates a new instance of QuiverWallStreetBets from a CSV line
        
        :param csvLine: CSV line
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source gained from the URL
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Quiver WallStreetBets object.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """Formats a string with the Quiver WallStreetBets information."""
        ...


class QuiverWallStreetBetsUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Universe Selection helper class for QuiverWallStreetBets dataset"""

    @property
    def mentions(self) -> int:
        """The number of mentions on the given date"""
        ...

    @property.setter
    def mentions(self, value: int) -> None:
        ...

    @property
    def rank(self) -> int:
        """This ticker's rank on the given date (as determined by total number of mentions)"""
        ...

    @property.setter
    def rank(self, value: int) -> None:
        ...

    @property
    def sentiment(self) -> float:
        """
        Average sentiment of all comments containing the given ticker on this date. Sentiment is calculated using VADER sentiment analysis.
        The value can range between -1 and +1. Negative values imply negative sentiment, whereas positive values imply positive sentiment.
        """
        ...

    @property.setter
    def sentiment(self, value: float) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time the data point ends at and becomes available to the algorithm"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clones this instance"""
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...


class QuiverCNBCs(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Collection of personal stock advices by CNBC"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
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

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """
        Formats a string with QuiverCNBC data
        
        :returns: string containing QuiverCNBC information.
        """
        ...


class QuiverCNBC(QuantConnect.Data.BaseData):
    """Personal stock advice by CNBC"""

    @property
    def notes(self) -> str:
        """Contract description"""
        ...

    @property.setter
    def notes(self, value: str) -> None:
        ...

    @property
    def direction(self) -> QuantConnect.Orders.OrderDirection:
        """Direction of trade"""
        ...

    @property.setter
    def direction(self, value: QuantConnect.Orders.OrderDirection) -> None:
        ...

    @property
    def traders(self) -> str:
        """Individual Name"""
        ...

    @property.setter
    def traders(self, value: str) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverCNBCsUniverse(QuantConnect.Data.BaseData):
    """Universe Selection helper class for QuiverQuant Congress dataset"""

    @property
    def notes(self) -> str:
        """Extra Information"""
        ...

    @property.setter
    def notes(self, value: str) -> None:
        ...

    @property
    def direction(self) -> QuantConnect.Orders.OrderDirection:
        """Direction of trade"""
        ...

    @property.setter
    def direction(self, value: QuantConnect.Orders.OrderDirection) -> None:
        ...

    @property
    def traders(self) -> str:
        """Individual Name"""
        ...

    @property.setter
    def traders(self, value: str) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class BrainSentimentIndicatorBase(typing.Generic[QuantConnect_DataSource_BrainSentimentIndicatorBase_T], QuantConnect.Data.BaseData):
    """Brain sentiment on news"""

    @property
    def total_article_mentions(self) -> int:
        ...

    @property.setter
    def total_article_mentions(self, value: int) -> None:
        ...

    @property
    def sentimental_article_mentions(self) -> float:
        ...

    @property.setter
    def sentimental_article_mentions(self, value: float) -> None:
        ...

    @property
    def sentiment(self) -> float:
        ...

    @property.setter
    def sentiment(self, value: float) -> None:
        ...

    @property
    def total_buzz_volume(self) -> typing.Optional[float]:
        ...

    @property.setter
    def total_buzz_volume(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sentimental_buzz_volume(self) -> typing.Optional[float]:
        ...

    @property.setter
    def sentimental_buzz_volume(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...

    def clone_data(self) -> QuantConnect_DataSource_BrainSentimentIndicatorBase_T:
        """
        Clones the data
        
        This method is protected.
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class BrainStockRankingBase(typing.Generic[QuantConnect_DataSource_BrainStockRankingBase_T], QuantConnect.Data.BaseData):
    """Brain sentiment on 10-K/10-Q SEC reports"""

    @property
    def rank(self) -> float:
        ...

    @property.setter
    def rank(self, value: float) -> None:
        ...

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def clone_data(self) -> QuantConnect_DataSource_BrainStockRankingBase_T:
        """This method is protected."""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class BrainCompanyFilingLanguageMetricsSimilarityDifference(System.Object):
    """This class has no documentation."""

    @property
    def all(self) -> typing.Optional[float]:
        ...

    @property
    def positive(self) -> typing.Optional[float]:
        ...

    @property.setter
    def positive(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def negative(self) -> typing.Optional[float]:
        ...

    @property.setter
    def negative(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def uncertainty(self) -> typing.Optional[float]:
        ...

    @property.setter
    def uncertainty(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def litigious(self) -> typing.Optional[float]:
        ...

    @property.setter
    def litigious(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def constraining(self) -> typing.Optional[float]:
        ...

    @property.setter
    def constraining(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def interesting(self) -> typing.Optional[float]:
        ...

    @property.setter
    def interesting(self, value: typing.Optional[float]) -> None:
        ...

    @staticmethod
    def parse(similarity_values: System.Collections.Generic.List[str]) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetricsSimilarityDifference:
        ...


class BrainCompanyFilingLanguageMetrics(System.Object):
    """This class has no documentation."""

    @property
    def sentence_count(self) -> typing.Optional[int]:
        ...

    @property.setter
    def sentence_count(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def mean_sentence_length(self) -> typing.Optional[float]:
        ...

    @property.setter
    def mean_sentence_length(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sentiment(self) -> typing.Optional[float]:
        ...

    @property.setter
    def sentiment(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def uncertainty(self) -> typing.Optional[float]:
        ...

    @property.setter
    def uncertainty(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def litigious(self) -> typing.Optional[float]:
        ...

    @property.setter
    def litigious(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def constraining(self) -> typing.Optional[float]:
        ...

    @property.setter
    def constraining(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def interesting(self) -> typing.Optional[float]:
        ...

    @property.setter
    def interesting(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def readability(self) -> typing.Optional[float]:
        ...

    @property.setter
    def readability(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def lexical_richness(self) -> typing.Optional[float]:
        ...

    @property.setter
    def lexical_richness(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def lexical_density(self) -> typing.Optional[float]:
        ...

    @property.setter
    def lexical_density(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def specific_density(self) -> typing.Optional[float]:
        ...

    @property.setter
    def specific_density(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def similarity(self) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetricsSimilarityDifference:
        ...

    @property.setter
    def similarity(self, value: QuantConnect.DataSource.BrainCompanyFilingLanguageMetricsSimilarityDifference) -> None:
        ...

    @staticmethod
    def parse(metrics: System.Collections.Generic.List[str], similarity: System.Collections.Generic.List[str] = None) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics:
        ...


class BrainCompanyFilingLanguageMetricsBase(typing.Generic[QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsBase_T], QuantConnect.Data.BaseData):
    """Brain sentiment on 10-K/10-Q SEC reports"""

    @property
    def report_date(self) -> datetime.datetime:
        ...

    @property.setter
    def report_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def report_category(self) -> str:
        ...

    @property.setter
    def report_category(self, value: str) -> None:
        ...

    @property
    def report_period(self) -> typing.Optional[int]:
        ...

    @property.setter
    def report_period(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def previous_report_date(self) -> typing.Optional[datetime.datetime]:
        ...

    @property.setter
    def previous_report_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def previous_report_category(self) -> str:
        ...

    @property.setter
    def previous_report_category(self, value: str) -> None:
        ...

    @property
    def previous_report_period(self) -> typing.Optional[int]:
        ...

    @property.setter
    def previous_report_period(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def report_sentiment(self) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics:
        ...

    @property.setter
    def report_sentiment(self, value: QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics) -> None:
        ...

    @property
    def risk_factors_statement_sentiment(self) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics:
        ...

    @property.setter
    def risk_factors_statement_sentiment(self, value: QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics) -> None:
        ...

    @property
    def management_discussion_analyasis_of_financial_condition_and_results_of_operations(self) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics:
        ...

    @property.setter
    def management_discussion_analyasis_of_financial_condition_and_results_of_operations(self, value: QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics) -> None:
        ...

    @property
    def report_type(self) -> str:
        """This property is protected."""
        ...

    @property.setter
    def report_type(self, value: str) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        ...

    def clone_data(self) -> QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsBase_T:
        """
        Clones the data
        
        This method is protected.
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class BrainCompanyFilingLanguageMetrics10K(QuantConnect.DataSource.BrainCompanyFilingLanguageMetricsBase[QuantConnect_DataSource_BrainCompanyFilingLanguageMetrics10K]):
    """Brain sentiment on only 10-K SEC reports"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def report_type(self) -> str:
        """This property is protected."""
        ...

    @property.setter
    def report_type(self, value: str) -> None:
        ...


class BrainCompanyFilingLanguageMetricsAll(QuantConnect.DataSource.BrainCompanyFilingLanguageMetricsBase[QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsAll]):
    """Brain sentiment on 10-K/10-Q SEC reports"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def report_type(self) -> str:
        """This property is protected."""
        ...

    @property.setter
    def report_type(self, value: str) -> None:
        ...


class BrainStockRanking10Day(QuantConnect.DataSource.BrainStockRankingBase[QuantConnect_DataSource_BrainStockRanking10Day]):
    """Brain universe stock rankings on expected returns in the next 10 days"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...


class BrainStockRanking2Day(QuantConnect.DataSource.BrainStockRankingBase[QuantConnect_DataSource_BrainStockRanking2Day]):
    """Brain universe stock rankings on expected returns in the next 2 days"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...


class BrainCompanyFilingLanguageMetricsUniverse(typing.Generic[QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsUniverse_T], QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Universe Selection helper class for BrainCompanyFilingLanguageMetrics dataset"""

    @property
    def report_sentiment(self) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics:
        """Language Metric score by report part"""
        ...

    @property.setter
    def report_sentiment(self, value: QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics) -> None:
        ...

    @property
    def risk_factors_statement_sentiment(self) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics:
        """Language Metric score by risk factor statement part"""
        ...

    @property.setter
    def risk_factors_statement_sentiment(self, value: QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics) -> None:
        ...

    @property
    def management_discussion_analyasis_of_financial_condition_and_results_of_operations(self) -> QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics:
        """Language Metric score by Management Discussion Analyasis Of Financial Condition And Results Of Operations"""
        ...

    @property.setter
    def management_discussion_analyasis_of_financial_condition_and_results_of_operations(self, value: QuantConnect.DataSource.BrainCompanyFilingLanguageMetrics) -> None:
        ...

    @property
    def report_type(self) -> str:
        """
        Report Type of which the language metric came from
        
        This property is protected.
        """
        ...

    @property.setter
    def report_type(self, value: str) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class BrainSentimentIndicatorUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Universe Selection helper class for Brain Sentiment dataset"""

    @property
    def total_article_mentions_7_days(self) -> typing.Optional[int]:
        """Total Article Mentions in 7 days"""
        ...

    @property.setter
    def total_article_mentions_7_days(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def sentimental_article_mentions_7_days(self) -> typing.Optional[float]:
        """Sentimental Article Mentions in 7 days"""
        ...

    @property.setter
    def sentimental_article_mentions_7_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sentiment_7_days(self) -> typing.Optional[float]:
        """Setiment Score in 7 days"""
        ...

    @property.setter
    def sentiment_7_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def total_buzz_volume_7_days(self) -> typing.Optional[float]:
        """Total Buzz Volume in 7 days"""
        ...

    @property.setter
    def total_buzz_volume_7_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sentimental_buzz_volume_7_days(self) -> typing.Optional[float]:
        """Sentimental Buzz Volume in 7 days"""
        ...

    @property.setter
    def sentimental_buzz_volume_7_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def total_article_mentions_30_days(self) -> typing.Optional[int]:
        """Total Article Mentions in 30 days"""
        ...

    @property.setter
    def total_article_mentions_30_days(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def sentimental_article_mentions_30_days(self) -> typing.Optional[float]:
        """Sentimental Article Mentions in 30 days"""
        ...

    @property.setter
    def sentimental_article_mentions_30_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sentiment_30_days(self) -> typing.Optional[float]:
        """Setiment Score in 30 days"""
        ...

    @property.setter
    def sentiment_30_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def total_buzz_volume_30_days(self) -> typing.Optional[float]:
        """Total Buzz Volume in 30 days"""
        ...

    @property.setter
    def total_buzz_volume_30_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sentimental_buzz_volume_30_days(self) -> typing.Optional[float]:
        """Sentimental Buzz Volume in 30 days"""
        ...

    @property.setter
    def sentimental_buzz_volume_30_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clones this instance"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class BrainCompanyFilingLanguageMetricsUniverseAll(QuantConnect.DataSource.BrainCompanyFilingLanguageMetricsUniverse[QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsUniverseAll]):
    """Brain sentiment universe on 10-K/10-Q SEC reports"""

    @property
    def report_type(self) -> str:
        """This property is protected."""
        ...

    @property.setter
    def report_type(self, value: str) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clones this instance"""
        ...


class BrainStockRanking3Day(QuantConnect.DataSource.BrainStockRankingBase[QuantConnect_DataSource_BrainStockRanking3Day]):
    """Brain universe stock rankings on expected returns in the next 3 days"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...


class BrainStockRanking5Day(QuantConnect.DataSource.BrainStockRankingBase[QuantConnect_DataSource_BrainStockRanking5Day]):
    """Brain universe stock rankings on expected returns in the next 5 days"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...


class BrainCompanyFilingLanguageMetricsUniverse10K(QuantConnect.DataSource.BrainCompanyFilingLanguageMetricsUniverse[QuantConnect_DataSource_BrainCompanyFilingLanguageMetricsUniverse10K]):
    """Brain sentiment universe on only 10-K SEC reports"""

    @property
    def report_type(self) -> str:
        """This property is protected."""
        ...

    @property.setter
    def report_type(self, value: str) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clones this instance"""
        ...


class BrainSentimentIndicator30Day(QuantConnect.DataSource.BrainSentimentIndicatorBase[QuantConnect_DataSource_BrainSentimentIndicator30Day]):
    """Brain sentiment indicator on 30 days of news"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...


class BrainStockRanking21Day(QuantConnect.DataSource.BrainStockRankingBase[QuantConnect_DataSource_BrainStockRanking21Day]):
    """Brain universe stock rankings on expected returns in the next 30 days"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...


class BrainSentimentIndicator7Day(QuantConnect.DataSource.BrainSentimentIndicatorBase[QuantConnect_DataSource_BrainSentimentIndicator7Day]):
    """Brain sentiment indicator on 7 days of news"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def lookback_days(self) -> int:
        """This property is protected."""
        ...

    @property.setter
    def lookback_days(self, value: int) -> None:
        ...


class BrainStockRankingUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Universe Selection helper class for Brain ML Stock Ranking dataset"""

    @property
    def rank_2_days(self) -> typing.Optional[float]:
        """Rank prediction score in 2 days"""
        ...

    @property.setter
    def rank_2_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def rank_3_days(self) -> typing.Optional[float]:
        """Rank prediction score in 3 days"""
        ...

    @property.setter
    def rank_3_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def rank_5_days(self) -> typing.Optional[float]:
        """Rank prediction score in 5 days"""
        ...

    @property.setter
    def rank_5_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def rank_10_days(self) -> typing.Optional[float]:
        """Rank prediction score in 10 days"""
        ...

    @property.setter
    def rank_10_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def rank_21_days(self) -> typing.Optional[float]:
        """Rank prediction score in 21 days"""
        ...

    @property.setter
    def rank_21_days(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clones this instance"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class CoinGeckoUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Universe Selection Data for Coin Gecko data which contains Price, Volume, and Market Cap in USD for cryptocurrencies"""

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...


class CoinGecko(QuantConnect.Data.BaseData):
    """Coin Gecko data which contains Price, Volume, and Market Cap in USD for cryptocurrencies"""

    @property
    def coin(self) -> str:
        """Coin Name"""
        ...

    @property
    def volume(self) -> float:
        """Volume in USD of the coin for that day"""
        ...

    @property.setter
    def volume(self, value: float) -> None:
        ...

    @property
    def market_cap(self) -> float:
        """Market Cap in USD of the coin for that day"""
        ...

    @property.setter
    def market_cap(self, value: float) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def create_symbol(self, market: str, quote_currency: str = "USD", security_type: QuantConnect.SecurityType = ...) -> QuantConnect.Symbol:
        """
        Creates a Symbol object for a given market and quote currency
        
        :param market: The market the ticker resides in
        :param quote_currency: The quote currency of the crypto-currency pair. E.g. USD for BTCUSD
        :param security_type: The security type of the ticker resides in
        :returns: A new Symbol object for the specified ticker.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class CoinGeckoUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Universe Selection Model for Coin Gecko data which contains Price, Volume and Market Cap"""

    @overload
    def __init__(self, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CoinGecko]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the CoinGeckoUniverseSelectionModel class
        
        :param selector: Returns the symbols that should be included in the universe
        :param universeSettings: The settings used for new subscriptions generated by this universe
        """
        ...

    @overload
    def __init__(self, selector: typing.Any, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the CoinGeckoUniverseSelectionModel class
        
        :param selector: Returns the symbols that should be included in the universe
        :param universeSettings: The settings used for new subscriptions generated by this universe
        """
        ...

    @overload
    def __init__(self, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the CoinGeckoUniverseSelectionModel class
        
        :param universeSettings: The settings used for new subscriptions generated by this universe
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates a new fundamental universe using this class's selection functions
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universe defined by this model.
        """
        ...

    def selector(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, data: System.Collections.Generic.IEnumerable[QuantConnect.DataSource.CoinGecko]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Defines the CoinGecko selection function.
        
        :param algorithm: The algorithm instance
        :param data: The CoinGecko Universe data used to perform filtering
        :returns: An enumerable of symbols passing the filter.
        """
        ...


class QuiverInsiderTradingUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Universe Selection helper class for QuiverQuant InsiderTrading dataset"""

    @property
    def name(self) -> str:
        """Name"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def shares(self) -> typing.Optional[float]:
        """Shares amount in transaction"""
        ...

    @property.setter
    def shares(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def price_per_share(self) -> typing.Optional[float]:
        """PricePerShare of transaction"""
        ...

    @property.setter
    def price_per_share(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def shares_owned_following(self) -> typing.Optional[float]:
        """Shares Owned after transcation"""
        ...

    @property.setter
    def shares_owned_following(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clone implementation"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverInsiderTrading(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Insider Trading by private businesses"""

    @property
    def name(self) -> str:
        """Name"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def shares(self) -> typing.Optional[float]:
        """Shares amount in transaction"""
        ...

    @property.setter
    def shares(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def price_per_share(self) -> typing.Optional[float]:
        """PricePerShare of transaction"""
        ...

    @property.setter
    def price_per_share(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def shares_owned_following(self) -> typing.Optional[float]:
        """Shares Owned after transcation"""
        ...

    @property.setter
    def shares_owned_following(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time the data point ends at and becomes available to the algorithm"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clone implementation"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class Fred(QuantConnect.Data.BaseData):
    """Federal Reserve Economic Data"""

    class CBOE(System.Object):
        """Chicago Board Options Exchange"""

        VIX_ON_GOOGLE: str = "VXGOGCLS"
        """CBOE Equity VIX on Google (in Index)"""

        VXD: str = "VXDCLS"
        """CBOE DJIA Volatility Index (in Index)"""

        VIX_ON_GOLDMAN_SACHS: str = "VXGSCLS"
        """CBOE Equity VIX on Goldman Sachs (in Index)"""

        VIX_ON_IBM: str = "VXIBMCLS"
        """CBOE Equity VIX on IBM (in Index)"""

        VIX_ON_AMAZON: str = "VXAZNCLS"
        """CBOE Equity VIX on Amazon (in Index)"""

        VXO: str = "VXOCLS"
        """CBOE S&P 100 Volatility Index: VXO (in Index)"""

        VXN: str = "VXNCLS"
        """CBOE NASDAQ 100 Volatility Index (in Index)"""

        TEN_YEAR_TREASURY_NOTE_VOLATILITY_FUTURES: str = "VXTYN"
        """CBOE 10-Year Treasury Note Volatility Futures (in Index)"""

        RVX: str = "RVXCLS"
        """CBOE Russell 2000 Volatility Index (in Index)"""

        SP_500_THREE_MONTH_VOLATILITY_INDEX: str = "VXVCLS"
        """CBOE S&P 500 3-Month Volatility Index (in Index)"""

        VIX_ON_APPLE: str = "VXAPLCLS"
        """CBOE Equity VIX on Apple (in Index)"""

        GOLD_MINERS_ETF_VOLATILITY_INDEX: str = "VXGDXCLS"
        """CBOE Gold Miners ETF Volatility Index (in Index)"""

        CHINA_ETF_VOLATILITY_INDEX: str = "VXFXICLS"
        """CBOE China ETF Volatility Index (in Index)"""

        BRAZIL_ETF_VOLATILITY_INDEX: str = "VXEWZCLS"
        """CBOE Brazil ETF Volatility Index (in Index)"""

        EMERGING_MARKETS_ETF_VOLATILITY_INDEX: str = "VXEEMCLS"
        """CBOE Emerging Markets ETF Volatility Index (in Index)"""

        EURO_CURRENCY_ETF_VOLATILITY_INDEX: str = "EVZCLS"
        """CBOE EuroCurrency ETF Volatility Index (in Index)"""

        GOLD_ETF_VOLATILITY_INDEX: str = "GVZCLS"
        """CBOE Gold ETF Volatility Index (in Index)"""

        CRUDE_OIL_ETF_VOLATILITY_INDEX: str = "OVXCLS"
        """CBOE Crude Oil ETF Volatility Index (in Index)"""

        SILVER_ETF_VOLATILITY_INDEX: str = "VXSLVCLS"
        """CBOE Silver ETF Volatility Index (in Index)"""

        ENERGY_SECTOR_ETF_VOLATILITY_INDEX: str = "VXXLECLS"
        """CBOE Energy Sector ETF Volatility Index (in Index)"""

        VIX: str = "VIXCLS"
        """CBOE Volatility Index: VIX (in Index)"""

    class CommercialPaper(System.Object):
        """
        Commercial paper (CP) consists of short-term, promissory notes issued primarily by corporations. Maturities range up to 270 days but average about 30 days. Many companies use CP to raise cash needed for current transactions, and many find it to be a lower-cost alternative to bank loans.
        The Federal Reserve Board disseminates information on CP primarily through its World Wide Web site. In addition, the Board publishes one-, two-, and three-month rates on AA nonfinancial and AA financial CP weekly in its H.15 Statistical Release.
        The Federal Reserve Board's CP release is derived from data supplied by The Depository Trust & Clearing Corporation (DTCC), a national clearinghouse for the settlement of securities trades and a custodian for securities. DTCC performs these functions for almost all activity in the domestic CP market. The Federal Reserve Board only considers maturities of 270 days or less. CP is exempt from SEC registration if its maturity does not exceed 270 days.
        Data on CP issuance rates and volumes typically are updated daily and typically posted with a one-day lag. Data on CP outstanding usually are available as of the close of business each Wednesday and as of the last business day of the month; these data are also posted with a one-day lag. The daily CP release will usually be available at 9:45 a.m. EST. However, the Federal Reserve Board makes no guarantee regarding the timing of the daily CP release. This policy is subject to change at any time without notice.
        """

        THREE_MONTH_AA_NONFINANCIAL_COMMERCIAL_PAPER_RATE: str = "DCPN3M"
        """3-Month AA Nonfinancial Commercial Paper Rate (in Percent)"""

        ONE_MONTH_AA_NONFINANCIAL_COMMERCIAL_PAPER_RATE: str = "DCPN30"
        """1-Month AA Nonfinancial Commercial Paper Rate (in Percent)"""

        TWO_MONTH_AA_NONFINANCIAL_COMMERCIAL_PAPER_RATE: str = "DCPN2M"
        """2-Month AA Nonfinancial Commercial Paper Rate (in Percent)"""

        THREE_MONTH_AA_FINANCIAL_COMMERCIAL_PAPER_RATE: str = "DCPF3M"
        """3-Month AA Financial Commercial Paper Rate (in Percent)"""

        TWO_MONTH_AA_FINANCIAL_COMMERCIAL_PAPER_RATE: str = "DCPF2M"
        """2-Month AA Financial Commercial Paper Rate (in Percent)"""

        ONE_MONTH_AA_FINANCIAL_COMMERCIAL_PAPER_RATE: str = "DCPF1M"
        """1-Month AA Financial Commercial Paper Rate (in Percent)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN14A2P2VOL"
        """Number of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Number)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN59A2P2VOL"
        """Number of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN59A2P2AMT"
        """Total Value of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN4180AAVOL"
        """Number of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_AA_ASSET_BACKED: str = "ABGT80AAAMT"
        """Total Value of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Millions of Dollars)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN4180AAAMT"
        """Total Value of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN4180A2P2VOL"
        """Number of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN4180A2P2AMT"
        """Total Value of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN2140AAVOL"
        """Number of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN2140AAAMT"
        """Total Value of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN2140A2P2VOL"
        """Number of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN2140A2P2AMT"
        """Total Value of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN14AAVOL"
        """Number of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Number)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN1020A2P2VOL"
        """Number of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN1020AAAMT"
        """Total Value of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB2140AAAMT"
        """Total Value of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN1020AAVOL"
        """Number of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN14A2P2AMT"
        """Total Value of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN14AAAMT"
        """Total Value of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        TOTAL_VALUEOF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_BETWEEN_1_AND_4_DAYS: str = "MKT14MKTAMT"
        """Total Value of Commercial Paper Issues with a Maturity Between 1 and 4 Days (in Millions of Dollars)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFIN1020A2P2AMT"
        """Total Value of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_AA_FINANCIAL: str = "FINGT80AAVOL"
        """Number of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Number)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN1020AAVOL"
        """Number of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN14AAAMT"
        """Total Value of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN14AAVOL"
        """Number of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Number)"""

        TOTAL_VALUEOF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_BETWEEN_10_AND_20_DAYS: str = "MKT1020MKTAMT"
        """Total Value of Commercial Paper Issues with a Maturity Between 10 and 20 Days (in Millions of Dollars)"""

        NUMBEROF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_BETWEEN_10_AND_20_DAYS: str = "MKT1020MKTVOL"
        """Number of Commercial Paper Issues with a Maturity Between 10 and 20 Days (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN2140AAAMT"
        """Total Value of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBEROF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_BETWEEN_1_AND_4_DAYS: str = "MKT14MKTVOL"
        """Number of Commercial Paper Issues with a Maturity Between 1 and 4 Days (in Number)"""

        TOTAL_VALUEOF_ISSUERSOF_COMMERCIAL_PAPERWITHA_MATURITY_BETWEEN_21_AND_40_DAYS: str = "MKT2140MKTAMT"
        """Total Value of Issuers of Commercial Paper with a Maturity Between 21 and 40 Days (in Millions of Dollars)"""

        NUMBEROF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_BETWEEN_21_AND_40_DAYS: str = "MKT2140MKTVOL"
        """Number of Commercial Paper Issues with a Maturity Between 21 and 40 Days (in Number)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN2140AAVOL"
        """Number of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Number)"""

        TOTAL_VALUEOF_ISSUERSOF_COMMERCIAL_PAPERWITHA_MATURITY_BETWEEN_41_AND_80_DAYS: str = "MKT4180MKTAMT"
        """Total Value of Issuers of Commercial Paper with a Maturity Between 41 and 80 Days (in Millions of Dollars)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN59AAAMT"
        """Total Value of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBEROF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_BETWEEN_41_AND_80_DAYS: str = "MKT4180MKTVOL"
        """Number of Commercial Paper Issues with a Maturity Between 41 and 80 Days (in Number)"""

        NUMBEROF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_BETWEEN_5_AND_9_DAYS: str = "MKT59MKTVOL"
        """Number of Commercial Paper Issues with a Maturity Between 5 and 9 Days (in Number)"""

        TOTAL_VALUEOF_ISSUERSOF_COMMERCIAL_PAPERWITHA_MATURITY_GREATER_THAN_80_DAYS: str = "MKTGT80MKTAMT"
        """Total Value of Issuers of Commercial Paper with a Maturity Greater Than 80 Days (in Millions of Dollars)"""

        NUMBEROF_COMMERCIAL_PAPER_ISSUESWITHA_MATURITY_GREATER_THAN_80_DAYS: str = "MKTGT80MKTVOL"
        """Number of Commercial Paper Issues with a Maturity Greater Than 80 Days (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN4180AAAMT"
        """Total Value of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN4180AAVOL"
        """Number of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB4180AAAMT"
        """Total Value of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Millions of Dollars)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN59AAAMT"
        """Total Value of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN59AAVOL"
        """Number of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_AA_FINANCIAL: str = "FINGT80AAAMT"
        """Total Value of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Millions of Dollars)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_AA_FINANCIAL: str = "FIN1020AAAMT"
        """Total Value of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the AA Financial Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_21_AND_40_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB2140AAVOL"
        """Number of Issues, with a Maturity Between 21 and 40 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Number)"""

        TOTAL_VALUEOF_ISSUERSOF_COMMERCIAL_PAPERWITHA_MATURITY_BETWEEN_5_AND_9_DAYS: str = "MKT59MKTAMT"
        """Total Value of Issuers of Commercial Paper with a Maturity Between 5 and 9 Days (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_AA_ASSET_BACKED: str = "ABGT80AAVOL"
        """Number of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Number)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFIN59AAVOL"
        """Number of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Number)"""

        FIFTEEN_DAY_AA_ASSETBACKED_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPAAAD15NB"
        """15-Day AA Asset-backed Commercial Paper Interest Rate (in Percent)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB59AAAMT"
        """Total Value of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Millions of Dollars)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_41_AND_80_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB4180AAVOL"
        """Number of Issues, with a Maturity Between 41 and 80 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Number)"""

        FIFTEEN_DAY_A_2_P_2_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNA2P2D15NB"
        """15-Day A2/P2 Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        SEVEN_DAY_A_2_P_2_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNA2P2D07NB"
        """7-Day A2/P2 Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        OVERNIGHT_A_2_P_2_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNA2P2D01NB"
        """Overnight A2/P2 Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        NINETY_DAY_AA_FINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPFAAD90NB"
        """90-Day AA Financial Commercial Paper Interest Rate (in Percent)"""

        OVERNIGHT_AA_ASSETBACKED_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPAAAD01NB"
        """Overnight AA Asset-backed Commercial Paper Interest Rate (in Percent)"""

        THREE_0_DAY_A_2_P_2_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNA2P2D30NB"
        """30-Day A2/P2 Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        SIXTY_DAY_AA_FINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPFAAD60NB"
        """60-Day AA Financial Commercial Paper Interest Rate (in Percent)"""

        THREE_0_DAY_AA_FINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPFAAD30NB"
        """30-Day AA Financial Commercial Paper Interest Rate (in Percent)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFINGT80A2P2AMT"
        """Total Value of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        THREE_0_DAY_AA_ASSETBACKED_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPAAAD30NB"
        """30-Day AA Asset-backed Commercial Paper Interest Rate (in Percent)"""

        SIXTY_DAY_AA_ASSETBACKED_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPAAAD60NB"
        """60-Day AA Asset-backed Commercial Paper Interest Rate (in Percent)"""

        NINETY_DAY_AA_ASSETBACKED_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPAAAD90NB"
        """90-Day AA Asset-backed Commercial Paper Interest Rate (in Percent)"""

        FIFTEEN_DAY_AA_FINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPFAAD15NB"
        """15-Day AA Financial Commercial Paper Interest Rate (in Percent)"""

        SEVEN_DAY_AA_FINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPFAAD07NB"
        """7-Day AA Financial Commercial Paper Interest Rate (in Percent)"""

        SEVEN_DAY_AA_ASSETBACKED_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPAAAD07NB"
        """7-Day AA Asset-backed Commercial Paper Interest Rate (in Percent)"""

        OVERNIGHT_AA_FINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPFAAD01NB"
        """Overnight AA Financial Commercial Paper Interest Rate (in Percent)"""

        SIXTY_DAY_A_2_P_2_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNA2P2D60NB"
        """60-Day A2/P2 Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_5_AND_9_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB59AAVOL"
        """Number of Issues, with a Maturity Between 5 and 9 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Number)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB14AAVOL"
        """Number of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Number)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_A_2_P_2_NONFINANCIAL: str = "NONFINGT80A2P2VOL"
        """Number of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the A2/P2 Nonfinancial Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_1_AND_4_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB14AAAMT"
        """Total Value of Issues, with a Maturity Between 1 and 4 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Millions of Dollars)"""

        NINETY_DAY_A_2_P_2_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNA2P2D90NB"
        """90-Day A2/P2 Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB1020AAVOL"
        """Number of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Number)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFINGT80AAAMT"
        """Total Value of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Millions of Dollars)"""

        OVERNIGHT_AA_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNAAD01NB"
        """Overnight AA Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        TOTAL_VALUE_OF_ISSUES_WITH_MATURITY_BETWEEN_10_AND_20_DAYS_USED_FOR_AA_ASSET_BACKED: str = "AB1020AAAMT"
        """Total Value of Issues, with a Maturity Between 10 and 20 Days, Used in Calculating the AA Asset-Backed Commercial Paper Rates (in Millions of Dollars)"""

        SEVEN_DAY_AA_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNAAD07NB"
        """7-Day AA Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        NINETY_DAY_AA_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNAAD90NB"
        """90-Day AA Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        FIFTEEN_DAY_AA_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNAAD15NB"
        """15-Day AA Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        THREE_0_DAY_AA_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNAAD30NB"
        """30-Day AA Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        SIXTY_DAY_AA_NONFINANCIAL_COMMERCIAL_PAPER_INTEREST_RATE: str = "RIFSPPNAAD60NB"
        """60-Day AA Nonfinancial Commercial Paper Interest Rate (in Percent)"""

        NUMBER_OF_ISSUES_WITH_MATURITY_GREATER_THAN_80_DAYS_USED_FOR_AA_NONFINANCIAL: str = "NONFINGT80AAVOL"
        """Number of Issues, with a Maturity Greater Than 80 Days, Used in Calculating the AA Nonfinancial Commercial Paper Rates (in Number)"""

        THREE_MONTH_COMMERCIAL_PAPER_MINUS_FEDERAL_FUNDS_RATE: str = "CPFF"
        """3-Month Commercial Paper Minus Federal Funds Rate (in Percent)"""

    class Wilshire(System.Object):
        """Wilshire Indexes help clients, investment professionals and researchers accurately measure and better understand the market. The Wilshire Index family leverages more than 40 years of Wilshire performance measurement expertise and employs unbiased construction rules."""

        US_SMALL_CAP_VALUE_PRICE: str = "WILLSMLCAPVALPR"
        """Wilshire US Small-Cap Value Price Index (in Index)"""

        PRICE_2500: str = "WILL2500PR"
        """Wilshire 2500 Price Index (in Index)"""

        PRICE_4500: str = "WILL4500PR"
        """Wilshire 4500 Price Index (in Index)"""

        VALUE_PRICE_2500: str = "WILL2500PRVAL"
        """Wilshire 2500 Value Price Index (in Index)"""

        GROWTH_PRICE_2500: str = "WILL2500PRGR"
        """Wilshire 2500 Growth Price Index (in Index)"""

        US_SMALL_CAP_PRICE: str = "WILLSMLCAPPR"
        """Wilshire US Small-Cap Price Index (in Index)"""

        PRICE_5000: str = "WILL5000PR"
        """Wilshire 5000 Price Index (in Index)"""

        US_SMALL_CAP_GROWTH_PRICE: str = "WILLSMLCAPGRPR"
        """Wilshire US Small-Cap Growth Price Index (in Index)"""

        US_MID_CAP_VALUE_PRICE: str = "WILLMIDCAPVALPR"
        """Wilshire US Mid-Cap Value Price Index (in Index)"""

        US_REAL_ESTATE_SECURITIES_PRICE: str = "WILLRESIPR"
        """Wilshire US Real Estate Securities Price Index (Wilshire US RESI) (in Index)"""

        US_LARGE_CAP_PRICE: str = "WILLLRGCAPPR"
        """Wilshire US Large-Cap Price Index (in Index)"""

        US_MID_CAP_PRICE: str = "WILLMIDCAPPR"
        """Wilshire US Mid-Cap Price Index (in Index)"""

        US_MID_CAP_GROWTH_PRICE: str = "WILLMIDCAPGRPR"
        """Wilshire US Mid-Cap Growth Price Index (in Index)"""

        US_MICRO_CAP_PRICE: str = "WILLMICROCAPPR"
        """Wilshire US Micro-Cap Price Index (in Index)"""

        US_REAL_ESTATE_INVESTMENT_TRUST_PRICE: str = "WILLREITPR"
        """Wilshire US Real Estate Investment Trust Price Index (Wilshire US REIT) (in Index)"""

        US_LARGE_CAP_VALUE_PRICE: str = "WILLLRGCAPVALPR"
        """Wilshire US Large-Cap Value Price Index (in Index)"""

        US_LARGE_CAP_GROWTH_PRICE: str = "WILLLRGCAPGRPR"
        """Wilshire US Large-Cap Growth Price Index (in Index)"""

        FULL_CAP_PRICE_5000: str = "WILL5000PRFC"
        """Wilshire 5000 Full Cap Price Index (in Index)"""

        US_MID_CAP_VALUE: str = "WILLMIDCAPVAL"
        """Wilshire US Mid-Cap Value Total Market Index (in Index)"""

        US_MID_CAP_GROWTH: str = "WILLMIDCAPGR"
        """Wilshire US Mid-Cap Growth Total Market Index (in Index)"""

        US_MID_CAP: str = "WILLMIDCAP"
        """Wilshire US Mid-Cap Total Market Index (in Index)"""

        US_REAL_ESTATE_SECURITIES: str = "WILLRESIND"
        """Wilshire US Real Estate Securities Total Market Index (Wilshire US RESI) (in Index)"""

        INDEX_4500: str = "WILL4500IND"
        """Wilshire 4500 Total Market Index (in Index)"""

        INDEX_5000: str = "WILL5000IND"
        """Wilshire 5000 Total Market Index (in Index)"""

        US_LARGE_CAP_GROWTH: str = "WILLLRGCAPGR"
        """Wilshire US Large-Cap Growth Total Market Index (in Index)"""

        US_MICRO_CAP: str = "WILLMICROCAP"
        """Wilshire US Micro-Cap Total Market Index (in Index)"""

        VALUE_2500: str = "WILL2500INDVAL"
        """Wilshire 2500 Value Total Market Index (in Index)"""

        US_SMALL_CAP_GROWTH: str = "WILLSMLCAPGR"
        """Wilshire US Small-Cap Growth Total Market Index (in Index)"""

        US_SMALL_CAP_VALUE: str = "WILLSMLCAPVAL"
        """Wilshire US Small-Cap Value Total Market Index (in Index)"""

        US_LARGE_CAP_VALUE: str = "WILLLRGCAPVAL"
        """Wilshire US Large-Cap Value Total Market Index (in Index)"""

        US_REAL_ESTATE_INVESTMENT_TRUST: str = "WILLREITIND"
        """Wilshire US Real Estate Investment Trust Total Market Index (Wilshire US REIT) (in Index)"""

        INDEX_2500: str = "WILL2500IND"
        """Wilshire 2500 Total Market Index (in Index)"""

        US_SMALL_CAP: str = "WILLSMLCAP"
        """Wilshire US Small-Cap Total Market Index (in Index)"""

        US_LARGE_CAP: str = "WILLLRGCAP"
        """Wilshire US Large-Cap Total Market Index (in Index)"""

        GROWTH_2500: str = "WILL2500INDGR"
        """Wilshire 2500 Growth Total Market Index (in Index)"""

        TOTAL_MARKET_FULL_CAP_5000: str = "WILL5000INDFC"
        """Wilshire 5000 Total Market Full Cap Index (in Index)"""

    class CentralBankInterventions(System.Object):
        """Central Bank Interventions"""

        JAPANESE_BANK_PURCHASES_OF_DM_EURO_AGAINST_JPY: str = "JPINTDDMEJPY"
        """Japan Intervention: Japanese Bank purchases of DM/Euro against JPY (in 100 Million Yen)"""

        JAPANESE_BANK_PURCHASES_OF_USD_AGAINST_DM: str = "JPINTDEXR"
        """Japan Intervention: Japanese Bank purchases of USD against DM (in 100 Million Yen)"""

        JAPANESE_BANK_PURCHASES_OF_USD_AGAINST_RUPIAH: str = "JPINTDUSDRP"
        """Japan Intervention: Japanese Bank purchases of USD against Rupiah (in 100 Million Yen)"""

        US_INTERVENTION_IN_MARKET_TRANSACTIONS_IN_THE_JPY_USD: str = "USINTDMRKTJPY"
        """U.S. Intervention: in Market Transactions in the JPY/USD (Millions of USD) (in Millions of USD)"""

        US_INTERVENTION_WITH_CUSTOMER_TRANSACTIONS_IN_OTHER_CURRENCIES: str = "USINTDCSOTH"
        """U.S. Intervention: With-Customer Transactions in Other Currencies (Millions of USD) (in Millions of USD)"""

        US_INTERVENTION_WITH_CUSTOMER_TRANSACTIONS_IN_THE_JPY_USD: str = "USINTDCSJPY"
        """U.S. Intervention: With-Customer Transactions in the JPY/USD (Millions of USD) (in Millions of USD)"""

        US_INTERVENTION_WITH_CUSTOMER_TRANSACTIONS_IN_THE_DEM_USD_EURO: str = "USINTDCSDM"
        """U.S. Intervention: With-Customer Transactions in the DEM/USD (Euro since 1999) (Millions of USD) (in Millions of USD)"""

        US_INTERVENTION_IN_MARKET_TRANSACTIONS_IN_OTHER_CURRENCIES: str = "USINTDMRKTOTH"
        """U.S. Intervention: in Market Transactions in Other Currencies (Millions of USD) (in Millions of USD)"""

        CENTRAL_BANK_OF_TURKEY_PURCHASES_OF_USD: str = "TRINTDEXR"
        """Turkish Intervention: Central Bank of Turkey Purchases of USD (Millions of USD) (in Millions of USD)"""

        JAPANESE_BANK_PURCHASES_OF_USD_AGAINST_JPY: str = "JPINTDUSDJPY"
        """Japan Intervention: Japanese Bank purchases of USD against JPY (in 100 Million Yen)"""

        US_INTERVENTION_IN_MARKET_TRANSACTIONS_IN_THE_DEM_USD_EURO: str = "USINTDMRKTDM"
        """U.S. Intervention: in Market Transactions in the DEM/USD (Euro since 1999) (Millions of USD) (in Millions of USD)"""

        SWISS_NATIONAL_BANK_PURCHASES_OF_DEM_AGAINST_CHF_MILLIONS_OF_DEM: str = "CHINTDCHFDM"
        """Swiss Intervention: Swiss National Bank Purchases of DEM against CHF (Millions of DEM) (in Millions of DEM)"""

        SWISS_NATIONAL_BANK_PURCHASES_OF_USD_AGAINST_DEM: str = "CHINTDUSDDM"
        """Swiss Intervention: Swiss National Bank Purchases of USD against DEM (Millions of USD) (in Millions of USD)"""

        SWISS_NATIONAL_BANK_PURCHASES_OF_USD_AGAINST_JPY: str = "CHINTDUSDJPY"
        """Swiss Intervention: Swiss National Bank Purchases of USD against JPY (Millions of USD) (in Millions of USD)"""

        SWISS_NATIONAL_BANK_PURCHASES_OF_USD_AGAINST_CHF: str = "CHINTDCHFUSD"
        """Swiss Intervention: Swiss National Bank Purchases of USD against CHF (Millions of USD) (in Millions of USD)"""

        BANCO_DE_MEXICO_PURCHASE_ON_THE_USD: str = "MEXINTDUSD"
        """Mexican Intervention: Banco de Mexico Purchase on the USD (in Millions of USD)"""

    class OECDRecessionIndicators(System.Object):
        """
        These time series is an interpretation of Organisation of Economic Development (OECD) Composite Leading Indicators: Reference Turning Points and Component Series data, which can be found at http://www.oecd.org/std/leading-indicators/oecdcompositeleadingindicatorsreferenceturningpointsandcomponentseries.htm. The OECD identifies months of turning points without designating a date within the month that turning points occurred. The dummy variable adopts an arbitrary convention that the turning point occurred at a specific date within the month. The arbitrary convention does not reflect any judgment on this issue by the OECD. Our time series is composed of dummy variables that represent periods of expansion and recession. A value of 1 is a recessionary period, while a value of 0 is an expansionary period. For this time series, the recession begins on the 15th day of the month of the peak and ends on the 15th day of the month of the trough. This time series is a disaggregation of the monthly series. For more options on recession shading, see the note and links below.
        The recession shading data that we provide initially comes from the source as a list of dates that are either an economic peak or trough. We interpret dates into recession shading data using one of three arbitrary methods. All of our recession shading data is available using all three interpretations. The period between a peak and trough is always shaded as a recession. The peak and trough are collectively extrema. Depending on the application, the extrema, both individually and collectively, may be included in the recession period in whole or in part. In situations where a portion of a period is included in the recession, the whole period is deemed to be included in the recession period.
        The first interpretation, known as the midpoint method, is to show a recession from the midpoint of the peak through the midpoint of the trough for monthly and quarterly data. For daily data, the recession begins on the 15th of the month of the peak and ends on the 15th of the month of the trough. Daily data is a disaggregation of monthly data. For monthly and quarterly data, the entire peak and trough periods are included in the recession shading. This method shows the maximum number of periods as a recession for monthly and quarterly data. The Federal Reserve Bank of St. Louis uses this method in its own publications. The midpoint method is used for this series.
        The second interpretation, known as the trough method, is to show a recession from the period following the peak through the trough (i.e. the peak is not included in the recession shading, but the trough is). For daily data, the recession begins on the first day of the first month following the peak and ends on the last day of the month of the trough. Daily data is a disaggregation of monthly data. The trough method is used when displaying data on FRED graphs. A version of this time series represented using the trough method can be found at:
        The third interpretation, known as the peak method, is to show a recession from the period of the peak to the trough (i.e. the peak is included in the recession shading, but the trough is not). For daily data, the recession begins on the first day of the month of the peak and ends on the last day of the month preceding the trough. Daily data is a disaggregation of monthly data. A version of this time series represented using the peak method can be found at:
        The OECD CLI system is based on the "growth cycle" approach, where business cycles and turning points are measured and identified in the deviation-from-trend series. The main reference series used in the OECD CLI system for the majority of countries is industrial production (IIP) covering all industry sectors excluding construction. This series is used because of its cyclical sensitivity and monthly availability, while the broad based Gross Domestic Product (GDP) is used to supplement the IIP series for identification of the final reference turning points in the growth cycle.
        Zones aggregates of the CLIs and the reference series are calculated as weighted averages of the corresponding zone member series (i.e. CLIs and IIPs).
        Up to December 2008 the turning points chronologies shown for regional/zone area aggregates or individual countries are determined by the rules established by the National Bureau of Economic Research (NBER) in the United States, which have been formalized and incorporated in a computer routine (Bry and Boschan) and included in the Phase-Average Trend (PAT) de-trending procedure. Starting from December 2008 the turning point detection algorithm is decoupled from the de-trending procedure, and is a simplified version of the original Bry and Boschan routine. (The routine parses local minima and maxima in the cycle series and applies censor rules to guarantee alternating peaks and troughs, as well as phase and cycle length constraints.)
        The components of the CLI are time series which exhibit leading relationship with the reference series (IIP) at turning points. Country CLIs are compiled by combining de-trended smoothed and normalized components. The component series for each country are selected based on various criteria such as economic significance; cyclical behavior; data quality; timeliness and availability.
        OECD data should be cited as follows: OECD Composite Leading Indicators, "Composite Leading Indicators: Reference Turning Points and Component Series", http://www.oecd.org/std/leading-indicators/oecdcompositeleadingindicatorsreferenceturningpointsandcomponentseries.htm
        """

        FOUR_BIG_EUROPEAN_COUNTRIES_FROM_PEAK_THROUGH_THE_TROUGH: str = "4BIGEURORECDM"
        """OECD based Recession Indicators for Four Big European Countries from the Peak through the Trough (in +1 or 0)"""

        AUSTRALIA_FROM_PEAK_THROUGH_THE_TROUGH: str = "AUSRECDM"
        """OECD based Recession Indicators for Australia from the Peak through the Trough (in +1 or 0)"""

        AUSTRIA_FROM_PEAK_THROUGH_THE_TROUGH: str = "AUTRECDM"
        """OECD based Recession Indicators for Austria from the Peak through the Trough (in +1 or 0)"""

        BELGIUM_FROM_PEAK_THROUGH_THE_TROUGH: str = "BELRECDM"
        """OECD based Recession Indicators for Belgium from the Peak through the Trough (in +1 or 0)"""

        BRAZIL_FROM_PEAK_THROUGH_THE_TROUGH: str = "BRARECDM"
        """OECD based Recession Indicators for Brazil from the Peak through the Trough (in +1 or 0)"""

        CANADA_FROM_PEAK_THROUGH_THE_TROUGH: str = "CANRECDM"
        """OECD based Recession Indicators for Canada from the Peak through the Trough (in +1 or 0)"""

        SWITZERLAND_FROM_PEAK_THROUGH_THE_TROUGH: str = "CHERECDM"
        """OECD based Recession Indicators for Switzerland from the Peak through the Trough (in +1 or 0)"""

        CHILE_FROM_PEAK_THROUGH_THE_TROUGH: str = "CHLRECDM"
        """OECD based Recession Indicators for Chile from the Peak through the Trough (in +1 or 0)"""

        CHINA_FROM_PEAK_THROUGH_THE_TROUGH: str = "CHNRECDM"
        """OECD based Recession Indicators for China from the Peak through the Trough (in +1 or 0)"""

        CZECH_REPUBLIC_FROM_PEAK_THROUGH_THE_TROUGH: str = "CZERECDM"
        """OECD based Recession Indicators for the Czech Republic from the Peak through the Trough (in +1 or 0)"""

        GERMANY_FROM_PEAK_THROUGH_THE_TROUGH: str = "DEURECDM"
        """OECD based Recession Indicators for Germany from the Peak through the Trough (in +1 or 0)"""

        DENMARK_FROM_PEAK_THROUGH_THE_TROUGH: str = "DNKRECDM"
        """OECD based Recession Indicators for Denmark from the Peak through the Trough (in +1 or 0)"""

        SPAIN_FROM_PEAK_THROUGH_THE_TROUGH: str = "ESPRECDM"
        """OECD based Recession Indicators for Spain from the Peak through the Trough (in +1 or 0)"""

        ESTONIA_FROM_PEAK_THROUGH_THE_TROUGH: str = "ESTRECDM"
        """OECD based Recession Indicators for Estonia from the Peak through the Trough (in +1 or 0)"""

        EURO_AREA_FROM_PEAK_THROUGH_THE_TROUGH: str = "EURORECDM"
        """OECD based Recession Indicators for Euro Area from the Peak through the Trough (in +1 or 0)"""

        FINLAND_FROM_PEAK_THROUGH_THE_TROUGH: str = "FINRECDM"
        """OECD based Recession Indicators for Finland from the Peak through the Trough (in +1 or 0)"""

        FRANCE_FROM_PEAK_THROUGH_THE_TROUGH: str = "FRARECDM"
        """OECD based Recession Indicators for France from the Peak through the Trough (in +1 or 0)"""

        UNITED_KINGDOM_FROM_PEAK_THROUGH_THE_TROUGH: str = "GBRRECDM"
        """OECD based Recession Indicators for the United Kingdom from the Peak through the Trough (in +1 or 0)"""

        GREECE_FROM_PEAK_THROUGH_THE_TROUGH: str = "GRCRECDM"
        """OECD based Recession Indicators for Greece from the Peak through the Trough (in +1 or 0)"""

        HUNGARY_FROM_PEAK_THROUGH_THE_TROUGH: str = "HUNRECDM"
        """OECD based Recession Indicators for Hungary from the Peak through the Trough (in +1 or 0)"""

        INDONESIA_FROM_PEAK_THROUGH_THE_TROUGH: str = "IDNRECDM"
        """OECD based Recession Indicators for Indonesia from the Peak through the Trough (in +1 or 0)"""

        INDIA_FROM_PEAK_THROUGH_THE_TROUGH: str = "INDRECDM"
        """OECD based Recession Indicators for India from the Peak through the Trough (in +1 or 0)"""

        IRELAND_FROM_PEAK_THROUGH_THE_TROUGH: str = "IRLRECDM"
        """OECD based Recession Indicators for Ireland from the Peak through the Trough (in +1 or 0)"""

        ISRAEL_FROM_PEAK_THROUGH_THE_TROUGH: str = "ISRRECDM"
        """OECD based Recession Indicators for Israel from the Peak through the Trough (in +1 or 0)"""

        ITALY_FROM_PEAK_THROUGH_THE_TROUGH: str = "ITARECDM"
        """OECD based Recession Indicators for Italy from the Peak through the Trough (in +1 or 0)"""

        JAPAN_FROM_PEAK_THROUGH_THE_TROUGH: str = "JPNRECDM"
        """OECD based Recession Indicators for Japan from the Peak through the Trough (in +1 or 0)"""

        KOREA_FROM_PEAK_THROUGH_THE_TROUGH: str = "KORRECDM"
        """OECD based Recession Indicators for Korea from the Peak through the Trough (in +1 or 0)"""

        LUXEMBOURG_FROM_PEAK_THROUGH_THE_TROUGH: str = "LUXRECDM"
        """OECD based Recession Indicators for Luxembourg from the Peak through the Trough (in +1 or 0)"""

        MAJOR_FIVE_ASIA_FROM_PEAK_THROUGH_THE_TROUGH: str = "MAJOR5ASIARECDM"
        """OECD based Recession Indicators for Major 5 Asia from the Peak through the Trough (in +1 or 0)"""

        MEXICO_FROM_PEAK_THROUGH_THE_TROUGH: str = "MEXRECDM"
        """OECD based Recession Indicators for Mexico from the Peak through the Trough (in +1 or 0)"""

        MAJOR_SEVEN_COUNTRIES_FROM_PEAK_THROUGH_THE_TROUGH: str = "MSCRECDM"
        """OECD based Recession Indicators for Major Seven Countries from the Peak through the Trough (in +1 or 0)"""

        NAFTA_AREA_FROM_PEAK_THROUGH_THE_TROUGH: str = "NAFTARECDM"
        """OECD based Recession Indicators for NAFTA Area from the Peak through the Trough (in +1 or 0)"""

        NETHERLANDS_FROM_PEAK_THROUGH_THE_TROUGH: str = "NDLRECDM"
        """OECD based Recession Indicators for Netherlands from the Peak through the Trough (in +1 or 0)"""

        NORWAY_FROM_PEAK_THROUGH_THE_TROUGH: str = "NORRECDM"
        """OECD based Recession Indicators for Norway from the Peak through the Trough (in +1 or 0)"""

        NEW_ZEALAND_FROM_PEAK_THROUGH_THE_TROUGH: str = "NZLRECDM"
        """OECD based Recession Indicators for New Zealand from the Peak through the Trough (in +1 or 0)"""

        OECD_EUROPE_FROM_PEAK_THROUGH_THE_TROUGH: str = "OECDEUROPERECDM"
        """OECD based Recession Indicators for OECD Europe from the Peak through the Trough (in +1 or 0)"""

        OECD_AND_NONMEMBER_ECONOMIES_FROM_PEAK_THROUGH_THE_TROUGH: str = "OECDNMERECDM"
        """OECD based Recession Indicators for OECD and Non-member Economies from the Peak through the Trough (in +1 or 0)"""

        OECD_TOTAL_AREA_FROM_PEAK_THROUGH_THE_TROUGH: str = "OECDRECDM"
        """OECD based Recession Indicators for the OECD Total Area from the Peak through the Trough (in +1 or 0)"""

        POLAND_FROM_PEAK_THROUGH_THE_TROUGH: str = "POLRECDM"
        """OECD based Recession Indicators for Poland from the Peak through the Trough (in +1 or 0)"""

        PORTUGAL_FROM_PEAK_THROUGH_THE_TROUGH: str = "PRTRECDM"
        """OECD based Recession Indicators for Portugal from the Peak through the Trough (in +1 or 0)"""

        RUSSIAN_FEDERATION_FROM_PEAK_THROUGH_THE_TROUGH: str = "RUSRECDM"
        """OECD based Recession Indicators for Russian Federation from the Peak through the Trough (in +1 or 0)"""

        SLOVAK_REPUBLIC_FROM_PEAK_THROUGH_THE_TROUGH: str = "SVKRECDM"
        """OECD based Recession Indicators for the Slovak Republic from the Peak through the Trough (in +1 or 0)"""

        SLOVENIA_FROM_PEAK_THROUGH_THE_TROUGH: str = "SVNRECDM"
        """OECD based Recession Indicators for Slovenia from the Peak through the Trough (in +1 or 0)"""

        SWEDEN_FROM_PEAK_THROUGH_THE_TROUGH: str = "SWERECDM"
        """OECD based Recession Indicators for Sweden from the Peak through the Trough (in +1 or 0)"""

        TURKEY_FROM_PEAK_THROUGH_THE_TROUGH: str = "TURRECDM"
        """OECD based Recession Indicators for Turkey from the Peak through the Trough (in +1 or 0)"""

        UNITED_STATES_FROM_PEAK_THROUGH_THE_TROUGH: str = "USARECDM"
        """OECD based Recession Indicators for the United States from the Peak through the Trough (in +1 or 0)"""

        SOUTH_AFRICA_FROM_PEAK_THROUGH_THE_TROUGH: str = "ZAFRECDM"
        """OECD based Recession Indicators for South Africa from the Peak through the Trough (in +1 or 0)"""

        FOUR_BIG_EUROPEAN_COUNTRIES_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "4BIGEURORECD"
        """OECD based Recession Indicators for Four Big European Countries from the Period following the Peak through the Trough (in +1 or 0)"""

        AUSTRALIA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "AUSRECD"
        """OECD based Recession Indicators for Australia from the Period following the Peak through the Trough (in +1 or 0)"""

        AUSTRIA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "AUTRECD"
        """OECD based Recession Indicators for Austria from the Period following the Peak through the Trough (in +1 or 0)"""

        BELGIUM_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "BELRECD"
        """OECD based Recession Indicators for Belgium from the Period following the Peak through the Trough (in +1 or 0)"""

        BRAZIL_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "BRARECD"
        """OECD based Recession Indicators for Brazil from the Period following the Peak through the Trough (in +1 or 0)"""

        CANADA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "CANRECD"
        """OECD based Recession Indicators for Canada from the Period following the Peak through the Trough (in +1 or 0)"""

        SWITZERLAND_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "CHERECD"
        """OECD based Recession Indicators for Switzerland from the Period following the Peak through the Trough (in +1 or 0)"""

        CHILE_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "CHLRECD"
        """OECD based Recession Indicators for Chile from the Period following the Peak through the Trough (in +1 or 0)"""

        CHINA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "CHNRECD"
        """OECD based Recession Indicators for China from the Period following the Peak through the Trough (in +1 or 0)"""

        CZECH_REPUBLIC_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "CZERECD"
        """OECD based Recession Indicators for the Czech Republic from the Period following the Peak through the Trough (in +1 or 0)"""

        GERMANY_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "DEURECD"
        """OECD based Recession Indicators for Germany from the Period following the Peak through the Trough (in +1 or 0)"""

        DENMARK_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "DNKRECD"
        """OECD based Recession Indicators for Denmark from the Period following the Peak through the Trough (in +1 or 0)"""

        SPAIN_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "ESPRECD"
        """OECD based Recession Indicators for Spain from the Period following the Peak through the Trough (in +1 or 0)"""

        ESTONIA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "ESTRECD"
        """OECD based Recession Indicators for Estonia from the Period following the Peak through the Trough (in +1 or 0)"""

        EURO_AREA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "EURORECD"
        """OECD based Recession Indicators for Euro Area from the Period following the Peak through the Trough (in +1 or 0)"""

        FINLAND_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "FINRECD"
        """OECD based Recession Indicators for Finland from the Period following the Peak through the Trough (in +1 or 0)"""

        FRANCE_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "FRARECD"
        """OECD based Recession Indicators for France from the Period following the Peak through the Trough (in +1 or 0)"""

        UNITED_KINGDOM_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "GBRRECD"
        """OECD based Recession Indicators for the United Kingdom from the Period following the Peak through the Trough (in +1 or 0)"""

        GREECE_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "GRCRECD"
        """OECD based Recession Indicators for Greece from the Period following the Peak through the Trough (in +1 or 0)"""

        HUNGARY_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "HUNRECD"
        """OECD based Recession Indicators for Hungary from the Period following the Peak through the Trough (in +1 or 0)"""

        INDONESIA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "IDNRECD"
        """OECD based Recession Indicators for Indonesia from the Period following the Peak through the Trough (in +1 or 0)"""

        INDIA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "INDRECD"
        """OECD based Recession Indicators for India from the Period following the Peak through the Trough (in +1 or 0)"""

        IRELAND_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "IRLRECD"
        """OECD based Recession Indicators for Ireland from the Period following the Peak through the Trough (in +1 or 0)"""

        ISRAEL_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "ISRRECD"
        """OECD based Recession Indicators for Israel from the Period following the Peak through the Trough (in +1 or 0)"""

        ITALY_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "ITARECD"
        """OECD based Recession Indicators for Italy from the Period following the Peak through the Trough (in +1 or 0)"""

        JAPAN_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "JPNRECD"
        """OECD based Recession Indicators for Japan from the Period following the Peak through the Trough (in +1 or 0)"""

        KOREA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "KORRECD"
        """OECD based Recession Indicators for Korea from the Period following the Peak through the Trough (in +1 or 0)"""

        LUXEMBOURG_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "LUXRECD"
        """OECD based Recession Indicators for Luxembourg from the Period following the Peak through the Trough (in +1 or 0)"""

        MAJOR_FIVE_ASIA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "MAJOR5ASIARECD"
        """OECD based Recession Indicators for Major 5 Asia from the Period following the Peak through the Trough (in +1 or 0)"""

        MEXICO_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "MEXRECD"
        """OECD based Recession Indicators for Mexico from the Period following the Peak through the Trough (in +1 or 0)"""

        MAJOR_SEVEN_COUNTRIES_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "MSCRECD"
        """OECD based Recession Indicators for Major Seven Countries from the Period following the Peak through the Trough (in +1 or 0)"""

        NAFTA_AREA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "NAFTARECD"
        """OECD based Recession Indicators for NAFTA Area from the Period following the Peak through the Trough (in +1 or 0)"""

        NETHERLANDS_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "NDLRECD"
        """OECD based Recession Indicators for Netherlands from the Period following the Peak through the Trough (in +1 or 0)"""

        NORWAY_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "NORRECD"
        """OECD based Recession Indicators for Norway from the Period following the Peak through the Trough (in +1 or 0)"""

        NEW_ZEALAND_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "NZLRECD"
        """OECD based Recession Indicators for New Zealand from the Period following the Peak through the Trough (in +1 or 0)"""

        OECD_EUROPE_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "OECDEUROPERECD"
        """OECD based Recession Indicators for OECD Europe from the Period following the Peak through the Trough (in +1 or 0)"""

        OEC_DAND_NONMEMBER_ECONOMIES_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "OECDNMERECD"
        """OECD based Recession Indicators for OECD and Non-member Economies from the Period following the Peak through the Trough (in +1 or 0)"""

        OECD_TOTAL_AREA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "OECDRECD"
        """OECD based Recession Indicators for the OECD Total Area from the Period following the Peak through the Trough (in +1 or 0)"""

        POLAND_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "POLRECD"
        """OECD based Recession Indicators for Poland from the Period following the Peak through the Trough (in +1 or 0)"""

        PORTUGAL_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "PRTRECD"
        """OECD based Recession Indicators for Portugal from the Period following the Peak through the Trough (in +1 or 0)"""

        RUSSIAN_FEDERATION_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "RUSRECD"
        """OECD based Recession Indicators for Russian Federation from the Period following the Peak through the Trough (in +1 or 0)"""

        SLOVAK_REPUBLIC_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "SVKRECD"
        """OECD based Recession Indicators for the Slovak Republic from the Period following the Peak through the Trough (in +1 or 0)"""

        SLOVENIA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "SVNRECD"
        """OECD based Recession Indicators for Slovenia from the Period following the Peak through the Trough (in +1 or 0)"""

        SWEDEN_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "SWERECD"
        """OECD based Recession Indicators for Sweden from the Period following the Peak through the Trough (in +1 or 0)"""

        TURKEY_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "TURRECD"
        """OECD based Recession Indicators for Turkey from the Period following the Peak through the Trough (in +1 or 0)"""

        UNITED_STATES_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "USARECD"
        """OECD based Recession Indicators for the United States from the Period following the Peak through the Trough (in +1 or 0)"""

        SOUTH_AFRICA_FROM_PERIOD_FOLLOWING_PEAK_THROUGH_THE_TROUGH: str = "ZAFRECD"
        """OECD based Recession Indicators for South Africa from the Period following the Peak through the Trough (in +1 or 0)"""

        FOUR_BIG_EUROPEAN_COUNTRIES_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "4BIGEURORECDP"
        """OECD based Recession Indicators for Four Big European Countries from the Peak through the Period preceding the Trough (in +1 or 0)"""

        AUSTRALIA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "AUSRECDP"
        """OECD based Recession Indicators for Australia from the Peak through the Period preceding the Trough (in +1 or 0)"""

        AUSTRIA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "AUTRECDP"
        """OECD based Recession Indicators for Austria from the Peak through the Period preceding the Trough (in +1 or 0)"""

        BELGIUM_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "BELRECDP"
        """OECD based Recession Indicators for Belgium from the Peak through the Period preceding the Trough (in +1 or 0)"""

        BRAZIL_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "BRARECDP"
        """OECD based Recession Indicators for Brazil from the Peak through the Period preceding the Trough (in +1 or 0)"""

        CANADA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "CANRECDP"
        """OECD based Recession Indicators for Canada from the Peak through the Period preceding the Trough (in +1 or 0)"""

        SWITZERLAND_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "CHERECDP"
        """OECD based Recession Indicators for Switzerland from the Peak through the Period preceding the Trough (in +1 or 0)"""

        CHILE_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "CHLRECDP"
        """OECD based Recession Indicators for Chile from the Peak through the Period preceding the Trough (in +1 or 0)"""

        CHINA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "CHNRECDP"
        """OECD based Recession Indicators for China from the Peak through the Period preceding the Trough (in +1 or 0)"""

        CZECH_REPUBLIC_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "CZERECDP"
        """OECD based Recession Indicators for the Czech Republic from the Peak through the Period preceding the Trough (in +1 or 0)"""

        GERMANY_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "DEURECDP"
        """OECD based Recession Indicators for Germany from the Peak through the Period preceding the Trough (in +1 or 0)"""

        DENMARK_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "DNKRECDP"
        """OECD based Recession Indicators for Denmark from the Peak through the Period preceding the Trough (in +1 or 0)"""

        SPAIN_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "ESPRECDP"
        """OECD based Recession Indicators for Spain from the Peak through the Period preceding the Trough (in +1 or 0)"""

        ESTONIA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "ESTRECDP"
        """OECD based Recession Indicators for Estonia from the Peak through the Period preceding the Trough (in +1 or 0)"""

        EURO_AREA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "EURORECDP"
        """OECD based Recession Indicators for Euro Area from the Peak through the Period preceding the Trough (in +1 or 0)"""

        FINLAND_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "FINRECDP"
        """OECD based Recession Indicators for Finland from the Peak through the Period preceding the Trough (in +1 or 0)"""

        FRANCE_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "FRARECDP"
        """OECD based Recession Indicators for France from the Peak through the Period preceding the Trough (in +1 or 0)"""

        UNITED_KINGDOM_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "GBRRECDP"
        """OECD based Recession Indicators for the United Kingdom from the Peak through the Period preceding the Trough (in +1 or 0)"""

        GREECE_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "GRCRECDP"
        """OECD based Recession Indicators for Greece from the Peak through the Period preceding the Trough (in +1 or 0)"""

        HUNGARY_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "HUNRECDP"
        """OECD based Recession Indicators for Hungary from the Peak through the Period preceding the Trough (in +1 or 0)"""

        INDONESIA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "IDNRECDP"
        """OECD based Recession Indicators for Indonesia from the Peak through the Period preceding the Trough (in +1 or 0)"""

        INDIA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "INDRECDP"
        """OECD based Recession Indicators for India from the Peak through the Period preceding the Trough (in +1 or 0)"""

        IRELAND_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "IRLRECDP"
        """OECD based Recession Indicators for Ireland from the Peak through the Period preceding the Trough (in +1 or 0)"""

        ISRAEL_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "ISRRECDP"
        """OECD based Recession Indicators for Israel from the Peak through the Period preceding the Trough (in +1 or 0)"""

        ITALY_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "ITARECDP"
        """OECD based Recession Indicators for Italy from the Peak through the Period preceding the Trough (in +1 or 0)"""

        JAPAN_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "JPNRECDP"
        """OECD based Recession Indicators for Japan from the Peak through the Period preceding the Trough (in +1 or 0)"""

        KOREA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "KORRECDP"
        """OECD based Recession Indicators for Korea from the Peak through the Period preceding the Trough (in +1 or 0)"""

        LUXEMBOURG_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "LUXRECDP"
        """OECD based Recession Indicators for Luxembourg from the Peak through the Period preceding the Trough (in +1 or 0)"""

        MAJOR_FIVE_ASIA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "MAJOR5ASIARECDP"
        """OECD based Recession Indicators for Major 5 Asia from the Peak through the Period preceding the Trough (in +1 or 0)"""

        MEXICO_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "MEXRECDP"
        """OECD based Recession Indicators for Mexico from the Peak through the Period preceding the Trough (in +1 or 0)"""

        MAJOR_SEVEN_COUNTRIES_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "MSCRECDP"
        """OECD based Recession Indicators for Major Seven Countries from the Peak through the Period preceding the Trough (in +1 or 0)"""

        NAFTA_AREA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "NAFTARECDP"
        """OECD based Recession Indicators for NAFTA Area from the Peak through the Period preceding the Trough (in +1 or 0)"""

        NETHERLANDS_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "NDLRECDP"
        """OECD based Recession Indicators for Netherlands from the Peak through the Period preceding the Trough (in +1 or 0)"""

        NORWAY_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "NORRECDP"
        """OECD based Recession Indicators for Norway from the Peak through the Period preceding the Trough (in +1 or 0)"""

        NEW_ZEALAND_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "NZLRECDP"
        """OECD based Recession Indicators for New Zealand from the Peak through the Period preceding the Trough (in +1 or 0)"""

        OECD_EUROPE_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "OECDEUROPERECDP"
        """OECD based Recession Indicators for OECD Europe from the Peak through the Period preceding the Trough (in +1 or 0)"""

        OEC_DAND_NONMEMBER_ECONOMIES_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "OECDNMERECDP"
        """OECD based Recession Indicators for OECD and Non-member Economies from the Peak through the Period preceding the Trough (in +1 or 0)"""

        OECD_TOTAL_AREA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "OECDRECDP"
        """OECD based Recession Indicators for the OECD Total Area from the Peak through the Period preceding the Trough (in +1 or 0)"""

        POLAND_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "POLRECDP"
        """OECD based Recession Indicators for Poland from the Peak through the Period preceding the Trough (in +1 or 0)"""

        PORTUGAL_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "PRTRECDP"
        """OECD based Recession Indicators for Portugal from the Peak through the Period preceding the Trough (in +1 or 0)"""

        RUSSIAN_FEDERATION_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "RUSRECDP"
        """OECD based Recession Indicators for Russian Federation from the Peak through the Period preceding the Trough (in +1 or 0)"""

        SLOVAK_REPUBLIC_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "SVKRECDP"
        """OECD based Recession Indicators for the Slovak Republic from the Peak through the Period preceding the Trough (in +1 or 0)"""

        SLOVENIA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "SVNRECDP"
        """OECD based Recession Indicators for Slovenia from the Peak through the Period preceding the Trough (in +1 or 0)"""

        SWEDEN_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "SWERECDP"
        """OECD based Recession Indicators for Sweden from the Peak through the Period preceding the Trough (in +1 or 0)"""

        TURKEY_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "TURRECDP"
        """OECD based Recession Indicators for Turkey from the Peak through the Period preceding the Trough (in +1 or 0)"""

        UNITED_STATES_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "USARECDP"
        """OECD based Recession Indicators for the United States from the Peak through the Period preceding the Trough (in +1 or 0)"""

        SOUTH_AFRICA_FROM_PEAK_THROUGH_THE_PERIOD_PRECEDINGTHE_TROUGH: str = "ZAFRECDP"
        """OECD based Recession Indicators for South Africa from the Peak through the Period preceding the Trough (in +1 or 0)"""

    class LIBOR(System.Object):
        """London InterBank Offered Rate"""

        SPOT_NEXT_BASED_ON_SWISS_FRANC: str = "CHFONTD156N"
        """Spot Next London Interbank Offered Rate (LIBOR), based on Swiss Franc (in Percent)"""

        SPOT_NEXT_BASED_ON_JAPANESE_YEN: str = "JPYONTD156N"
        """Spot Next London Interbank Offered Rate (LIBOR), based on Japanese Yen (in Percent)"""

        SIX_MONTH_BASED_ON_JAPANESE_YEN: str = "JPY6MTD156N"
        """6-Month London Interbank Offered Rate (LIBOR), based on Japanese Yen (in Percent)"""

        THREE_MONTH_BASED_ON_JAPANESE_YEN: str = "JPY3MTD156N"
        """3-Month London Interbank Offered Rate (LIBOR), based on Japanese Yen (in Percent)"""

        SIX_MONTH_BASED_ON_USD: str = "USD6MTD156N"
        """6-Month London Interbank Offered Rate (LIBOR), based on U.S. Dollar (in Percent)"""

        ONE_MONTH_BASED_ON_JAPANESE_YEN: str = "JPY1MTD156N"
        """1-Month London Interbank Offered Rate (LIBOR), based on Japanese Yen (in Percent)"""

        TWELVE_MONTH_BASED_ON_JAPANESE_YEN: str = "JPY12MD156N"
        """12-Month London Interbank Offered Rate (LIBOR), based on Japanese Yen (in Percent)"""

        TWELVE_MONTH_BASED_ON_BRITISH_POUND: str = "GBP12MD156N"
        """12-Month London Interbank Offered Rate (LIBOR), based on British Pound (in Percent)"""

        ONE_MONTH_BASED_ON_BRITISH_POUND: str = "GBP1MTD156N"
        """1-Month London Interbank Offered Rate (LIBOR), based on British Pound (in Percent)"""

        ONE_WEEK_BASED_ON_BRITISH_POUND: str = "GBP1WKD156N"
        """1-Week London Interbank Offered Rate (LIBOR), based on British Pound (in Percent)"""

        TWO_MONTH_BASED_ON_BRITISH_POUND: str = "GBP2MTD156N"
        """2-Month London Interbank Offered Rate (LIBOR), based on British Pound (in Percent)"""

        THREE_MONTH_BASED_ON_BRITISH_POUND: str = "GBP3MTD156N"
        """3-Month London Interbank Offered Rate (LIBOR), based on British Pound (in Percent)"""

        ONE_WEEK_BASED_ON_JAPANESE_YEN: str = "JPY1WKD156N"
        """1-Week London Interbank Offered Rate (LIBOR), based on Japanese Yen (in Percent)"""

        TWO_MONTH_BASED_ON_JAPANESE_YEN: str = "JPY2MTD156N"
        """2-Month London Interbank Offered Rate (LIBOR), based on Japanese Yen (in Percent)"""

        SIX_MONTH_BASED_ON_SWISS_FRANC: str = "CHF6MTD156N"
        """6-Month London Interbank Offered Rate (LIBOR), based on Swiss Franc (in Percent)"""

        THREE_MONTH_BASED_ON_SWISS_FRANC: str = "CHF3MTD156N"
        """3-Month London Interbank Offered Rate (LIBOR), based on Swiss Franc (in Percent)"""

        ONE_MONTH_BASED_ON_USD: str = "USD1MTD156N"
        """1-Month London Interbank Offered Rate (LIBOR), based on U.S. Dollar (in Percent)"""

        TWELVE_MONTH_BASED_ON_SWISS_FRANC: str = "CHF12MD156N"
        """12-Month London Interbank Offered Rate (LIBOR), based on Swiss Franc (in Percent)"""

        TWELVE_MONTH_BASED_ON_USD: str = "USD12MD156N"
        """12-Month London Interbank Offered Rate (LIBOR), based on U.S. Dollar (in Percent)"""

        ONE_MONTH_BASED_ON_SWISS_FRANC: str = "CHF1MTD156N"
        """1-Month London Interbank Offered Rate (LIBOR), based on Swiss Franc (in Percent)"""

        ONE_WEEK_BASED_ON_SWISS_FRANC: str = "CHF1WKD156N"
        """1-Week London Interbank Offered Rate (LIBOR), based on Swiss Franc (in Percent)"""

        TWO_MONTH_BASED_ON_SWISS_FRANC: str = "CHF2MTD156N"
        """2-Month London Interbank Offered Rate (LIBOR), based on Swiss Franc (in Percent)"""

        TWELVE_MONTH_BASED_ON_EURO: str = "EUR12MD156N"
        """12-Month London Interbank Offered Rate (LIBOR), based on Euro (in Percent)"""

        SIX_MONTH_BASED_ON_BRITISH_POUND: str = "GBP6MTD156N"
        """6-Month London Interbank Offered Rate (LIBOR), based on British Pound (in Percent)"""

        ONE_MONTH_BASED_ON_EURO: str = "EUR1MTD156N"
        """1-Month London Interbank Offered Rate (LIBOR), based on Euro (in Percent)"""

        TWO_MONTH_BASED_ON_EURO: str = "EUR2MTD156N"
        """2-Month London Interbank Offered Rate (LIBOR), based on Euro (in Percent)"""

        THREE_MONTH_BASED_ON_EURO: str = "EUR3MTD156N"
        """3-Month London Interbank Offered Rate (LIBOR), based on Euro (in Percent)"""

        SIX_MONTH_BASED_ON_EURO: str = "EUR6MTD156N"
        """6-Month London Interbank Offered Rate (LIBOR), based on Euro (in Percent)"""

        OVERNIGHT_BASED_ON_EURO: str = "EURONTD156N"
        """Overnight London Interbank Offered Rate (LIBOR), based on Euro (in Percent)"""

        ONE_WEEK_BASED_ON_USD: str = "USD1WKD156N"
        """1-Week London Interbank Offered Rate (LIBOR), based on U.S. Dollar (in Percent)"""

        TWO_MONTH_BASED_ON_USD: str = "USD2MTD156N"
        """2-Month London Interbank Offered Rate (LIBOR), based on U.S. Dollar (in Percent)"""

        THREE_MONTH_BASED_ON_USD: str = "USD3MTD156N"
        """3-Month London Interbank Offered Rate (LIBOR), based on U.S. Dollar (in Percent)"""

        OVERNIGHT_BASED_ON_USD: str = "USDONTD156N"
        """Overnight London Interbank Offered Rate (LIBOR), based on U.S. Dollar (in Percent)"""

        ONE_WEEK_BASED_ON_EURO: str = "EUR1WKD156N"
        """1-Week London Interbank Offered Rate (LIBOR), based on Euro (in Percent)"""

        OVERNIGHT_BASED_ON_BRITISH_POUND: str = "GBPONTD156N"
        """Overnight London Interbank Offered Rate (LIBOR), based on British Pound (in Percent)"""

    class ICEBofAML(System.Object):
        """ICE BofAML"""

        AAAA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM1BRRAAA2ACRPITRIV"
        """ICE BofAML AAA-A Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        AAAAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM1RAAA2ALCRPIUSTRIV"
        """ICE BofAML AAA-A US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        ASIA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMRACRPIASIATRIV"
        """ICE BofAML Asia Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        ASIA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMALLCRPIASIAUSTRIV"
        """ICE BofAML Asia US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        BAND_LOWER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM4BRRBLCRPITRIV"
        """ICE BofAML B and Lower Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        BAND_LOWER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM4RBLLCRPIUSTRIV"
        """ICE BofAML B and Lower US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        BB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM3BRRBBCRPITRIV"
        """ICE BofAML BB Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        BBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM3RBBLCRPIUSTRIV"
        """ICE BofAML BB US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        BBB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM2BRRBBBCRPITRIV"
        """ICE BofAML BBB Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        BBBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM2RBBBLCRPIUSTRIV"
        """ICE BofAML BBB US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        CROSSOVER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEM5BCOCRPITRIV"
        """ICE BofAML Crossover Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        CROSSOVER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMXOCOLCRPIUSTRIV"
        """ICE BofAML Crossover US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        EMERGING_MARKETS_CORPORATE_PLUS_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMCBPITRIV"
        """ICE BofAML Emerging Markets Corporate Plus Index Total Return Index Value (in Index)"""

        EURO_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMEBCRPIETRIV"
        """ICE BofAML Euro Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        EMEA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMRECRPIEMEATRIV"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        EMEAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMELLCRPIEMEAUSTRIV"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMFSFCRPITRIV"
        """ICE BofAML Financial Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMFLFLCRPIUSTRIV"
        """ICE BofAML Financial US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        HIGH_GRADE_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMIBHGCRPITRIV"
        """ICE BofAML High Grade Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        HIGH_GRADE_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMHGHGLCRPIUSTRIV"
        """ICE BofAML High Grade US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        HIGH_YIELD_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMHBHYCRPITRIV"
        """ICE BofAML High Yield Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        HIGH_YIELD_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMHYHYLCRPIUSTRIV"
        """ICE BofAML High Yield US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        LATIN_AMERICA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMRLCRPILATRIV"
        """ICE BofAML Latin America Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        LATIN_AMERICA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMLLLCRPILAUSTRIV"
        """ICE BofAML Latin America US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        NON_FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMNSNFCRPITRIV"
        """ICE BofAML Non-Financial Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        NON_FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMNFNFLCRPIUSTRIV"
        """ICE BofAML Non-Financial US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        US_CORPORATE_MASTER_OPTION_ADJUSTED_SPREAD: str = "BAMLC0A0CM"
        """ICE BofAML US Corporate Master Option-Adjusted Spread (in Percent)"""

        US_HIGH_YIELD_MASTER_II_OPTION_ADJUSTED_SPREAD: str = "BAMLH0A0HYM2"
        """ICE BofAML US High Yield Master II Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_1_TO_3_YEAR_OPTION_ADJUSTED_SPREAD: str = "BAMLC1A0C13Y"
        """ICE BofAML US Corporate 1-3 Year Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_10_TO_15_YEAR_OPTION_ADJUSTED_SPREAD: str = "BAMLC7A0C1015Y"
        """ICE BofAML US Corporate 10-15 Year Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_MORE_THAN_15_YEAR_OPTION_ADJUSTED_SPREAD: str = "BAMLC8A0C15PY"
        """ICE BofAML US Corporate 15+ Year Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_3_TO_5_YEAR_OPTION_ADJUSTED_SPREAD: str = "BAMLC2A0C35Y"
        """ICE BofAML US Corporate 3-5 Year Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_5_TO_7_YEAR_OPTION_ADJUSTED_SPREAD: str = "BAMLC3A0C57Y"
        """ICE BofAML US Corporate 5-7 Year Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_7_TO_10_YEAR_OPTION_ADJUSTED_SPREAD: str = "BAMLC4A0C710Y"
        """ICE BofAML US Corporate 7-10 Year Option-Adjusted Spread (in Percent)"""

        PUBLIC_SECTOR_ISSUERS_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMPUPUBSLCRPIUSTRIV"
        """ICE BofAML Public Sector Issuers US Emerging Markets Liquid Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        US_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMUBCRPIUSTRIV"
        """ICE BofAML US Emerging Markets Corporate Plus Sub-Index Total Return Index Value (in Index)"""

        US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLEMCLLCRPIUSTRIV"
        """ICE BofAML US Emerging Markets Liquid Corporate Plus Index Total Return Index Value (in Index)"""

        EURO_HIGH_YIELD_INDEX_TOTAL_RETURN_INDEX_VALUE: str = "BAMLHE00EHYITRIV"
        """ICE BofAML Euro High Yield Index Total Return Index Value (in Index)"""

        US_CORP_1_TO_3_YEARS_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC1A013YTRIV"
        """ICE BofAML US Corp 1-3yr Total Return Index Value (in Index)"""

        US_CORP_10_TO_15_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC7A01015YTRIV"
        """ICE BofAML US Corp 10-15yr Total Return Index Value (in Index)"""

        US_CORP_MORE_THAN_15_YEARS_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC8A015PYTRIV"
        """ICE BofAML US Corp 15+yr Total Return Index Value (in Index)"""

        US_CORPE_TO_5_YEARS_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC2A035YTRIV"
        """ICE BofAML US Corp 3-5yr Total Return Index Value (in Index)"""

        US_CORP_5_TO_7_YEARS_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC3A057YTRIV"
        """ICE BofAML US Corp 5-7yr Total Return Index Value (in Index)"""

        US_CORPORATE_7_TO_10_YEARS_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC4A0710YTRIV"
        """ICE BofAML US Corporate 7-10yr Total Return Index Value (in Index)"""

        US_CORP_A_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC0A3ATRIV"
        """ICE BofAML US Corp A Total Return Index Value (in Index)"""

        US_CORP_AA_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC0A2AATRIV"
        """ICE BofAML US Corp AA Total Return Index Value (in Index)"""

        US_CORP_AAA_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC0A1AAATRIV"
        """ICE BofAML US Corp AAA Total Return Index Value (in Index)"""

        US_HIGH_YIELD_B_TOTAL_RETURN_INDEX_VALUE: str = "BAMLHYH0A2BTRIV"
        """ICE BofAML US High Yield B Total Return Index Value (in Index)"""

        US_HIGH_YIELD_BB_TOTAL_RETURN_INDEX_VALUE: str = "BAMLHYH0A1BBTRIV"
        """ICE BofAML US High Yield BB Total Return Index Value (in Index)"""

        US_CORP_BBB_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC0A4BBBTRIV"
        """ICE BofAML US Corp BBB Total Return Index Value (in Index)"""

        US_HIGH_YIELD_CC_COR_BELOW_TOTAL_RETURN_INDEX_VALUE: str = "BAMLHYH0A3CMTRIV"
        """ICE BofAML US High Yield CCC or Below Total Return Index Value (in Index)"""

        US_CORP_MASTER_TOTAL_RETURN_INDEX_VALUE: str = "BAMLCC0A0CMTRIV"
        """ICE BofAML US Corp Master Total Return Index Value (in Index)"""

        US_HIGH_YIELD_MASTER_II_TOTAL_RETURN_INDEX_VALUE: str = "BAMLHYH0A0HYM2TRIV"
        """ICE BofAML US High Yield Master II Total Return Index Value (in Index)"""

        AAAA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM1BRRAAA2ACRPIOAS"
        """ICE BofAML AAA-A Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        AAAAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM1RAAA2ALCRPIUSOAS"
        """ICE BofAML AAA-A US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        ASIA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMRACRPIASIAOAS"
        """ICE BofAML Asia Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        ASIA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMALLCRPIASIAUSOAS"
        """ICE BofAML Asia US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        BAND_LOWER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM4BRRBLCRPIOAS"
        """ICE BofAML B and Lower Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        BAND_LOWER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM4RBLLCRPIUSOAS"
        """ICE BofAML B and Lower US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        BB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM3BRRBBCRPIOAS"
        """ICE BofAML BB Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        BBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM3RBBLCRPIUSOAS"
        """ICE BofAML BB US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        BBB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM2BRRBBBCRPIOAS"
        """ICE BofAML BBB Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        BBBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM2RBBBLCRPIUSOAS"
        """ICE BofAML BBB US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        CROSSOVER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEM5BCOCRPIOAS"
        """ICE BofAML Crossover Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        CROSSOVER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMXOCOLCRPIUSOAS"
        """ICE BofAML Crossover US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        EMERGING_MARKETS_CORPORATE_PLUS_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMCBPIOAS"
        """ICE BofAML Emerging Markets Corporate Plus Index Option-Adjusted Spread (in Percent)"""

        EURO_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMEBCRPIEOAS"
        """ICE BofAML Euro Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        EMEA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMRECRPIEMEAOAS"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        EMEAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMELLCRPIEMEAUSOAS"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMFSFCRPIOAS"
        """ICE BofAML Financial Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMFLFLCRPIUSOAS"
        """ICE BofAML Financial US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        HIGH_GRADE_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMIBHGCRPIOAS"
        """ICE BofAML High Grade Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        HIGH_GRADE_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMHGHGLCRPIUSOAS"
        """ICE BofAML High Grade US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        HIGH_YIELD_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMHBHYCRPIOAS"
        """ICE BofAML High Yield Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        HIGH_YIELD_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMHYHYLCRPIUSOAS"
        """ICE BofAML High Yield US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        LATIN_AMERICA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMRLCRPILAOAS"
        """ICE BofAML Latin America Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        LATIN_AMERICA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMLLLCRPILAUSOAS"
        """ICE BofAML Latin America US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        NON_FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMNSNFCRPIOAS"
        """ICE BofAML Non-Financial Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        NON_FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMNFNFLCRPIUSOAS"
        """ICE BofAML Non-Financial US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        PUBLIC_SECTOR_ISSUERS_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMPUPUBSLCRPIUSOAS"
        """ICE BofAML Public Sector Issuers US Emerging Markets Liquid Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        US_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMUBCRPIUSOAS"
        """ICE BofAML US Emerging Markets Corporate Plus Sub-Index Option-Adjusted Spread (in Percent)"""

        US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLEMCLLCRPIUSOAS"
        """ICE BofAML US Emerging Markets Liquid Corporate Plus Index Option-Adjusted Spread (in Percent)"""

        EURO_HIGH_YIELD_INDEX_OPTION_ADJUSTED_SPREAD: str = "BAMLHE00EHYIOAS"
        """ICE BofAML Euro High Yield Index Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_A_OPTION_ADJUSTED_SPREAD: str = "BAMLC0A3CA"
        """ICE BofAML US Corporate A Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_AA_OPTION_ADJUSTED_SPREAD: str = "BAMLC0A2CAA"
        """ICE BofAML US Corporate AA Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_AAA_OPTION_ADJUSTED_SPREAD: str = "BAMLC0A1CAAA"
        """ICE BofAML US Corporate AAA Option-Adjusted Spread (in Percent)"""

        US_HIGH_YIELD_B_OPTION_ADJUSTED_SPREAD: str = "BAMLH0A2HYB"
        """ICE BofAML US High Yield B Option-Adjusted Spread (in Percent)"""

        US_HIGH_YIELD_BB_OPTION_ADJUSTED_SPREAD: str = "BAMLH0A1HYBB"
        """ICE BofAML US High Yield BB Option-Adjusted Spread (in Percent)"""

        US_CORPORATE_BBB_OPTION_ADJUSTED_SPREAD: str = "BAMLC0A4CBBB"
        """ICE BofAML US Corporate BBB Option-Adjusted Spread (in Percent)"""

        US_HIGH_YIELD_CC_COR_BELOW_OPTION_ADJUSTED_SPREAD: str = "BAMLH0A3HYC"
        """ICE BofAML US High Yield CCC or Below Option-Adjusted Spread (in Percent)"""

        AAAA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM1BRRAAA2ACRPIEY"
        """ICE BofAML AAA-A Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        AAAAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM1RAAA2ALCRPIUSEY"
        """ICE BofAML AAA-A US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        ASIA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMRACRPIASIAEY"
        """ICE BofAML Asia Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        ASIA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMALLCRPIASIAUSEY"
        """ICE BofAML Asia US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        BAND_LOWER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM4BRRBLCRPIEY"
        """ICE BofAML B and Lower Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        BAND_LOWER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM4RBLLCRPIUSEY"
        """ICE BofAML B and Lower US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        BB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM3BRRBBCRPIEY"
        """ICE BofAML BB Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        BBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM3RBBLCRPIUSEY"
        """ICE BofAML BB US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        BBB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM2BRRBBBCRPIEY"
        """ICE BofAML BBB Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        BBBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM2RBBBLCRPIUSEY"
        """ICE BofAML BBB US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        CROSSOVER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEM5BCOCRPIEY"
        """ICE BofAML Crossover Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        CROSSOVER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMXOCOLCRPIUSEY"
        """ICE BofAML Crossover US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        EMERGING_MARKETS_CORPORATE_PLUS_INDEX_EFFECTIVE_YIELD: str = "BAMLEMCBPIEY"
        """ICE BofAML Emerging Markets Corporate Plus Index Effective Yield (in Percent)"""

        EURO_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMEBCRPIEEY"
        """ICE BofAML Euro Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        EURO_HIGH_YIELD_INDEX_EFFECTIVE_YIELD: str = "BAMLHE00EHYIEY"
        """ICE BofAML Euro High Yield Index Effective Yield (in Percent)"""

        EMEA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMRECRPIEMEAEY"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        EMEAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMELLCRPIEMEAUSEY"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMFSFCRPIEY"
        """ICE BofAML Financial Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMFLFLCRPIUSEY"
        """ICE BofAML Financial US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        HIGH_GRADE_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMIBHGCRPIEY"
        """ICE BofAML High Grade Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        HIGH_GRADE_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMHGHGLCRPIUSEY"
        """ICE BofAML High Grade US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        HIGH_YIELD_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMHBHYCRPIEY"
        """ICE BofAML High Yield Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        HIGH_YIELD_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMHYHYLCRPIUSEY"
        """ICE BofAML High Yield US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        LATIN_AMERICA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMRLCRPILAEY"
        """ICE BofAML Latin America Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        LATIN_AMERICA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMLLLCRPILAUSEY"
        """ICE BofAML Latin America US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        NON_FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMNSNFCRPIEY"
        """ICE BofAML Non-Financial Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        NON_FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMNFNFLCRPIUSEY"
        """ICE BofAML Non-Financial US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        PUBLIC_SECTOR_ISSUERS_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMPUPUBSLCRPIUSEY"
        """ICE BofAML Public Sector Issuers US Emerging Markets Liquid Corporate Plus Sub-Index Effective Yield (in Percent)"""

        US_CORPORATE_1_THREE_YEAR_EFFECTIVE_YIELD: str = "BAMLC1A0C13YEY"
        """ICE BofAML US Corporate 1-3 Year Effective Yield (in Percent)"""

        US_CORPORATE_10_TO_15_YEAR_EFFECTIVE_YIELD: str = "BAMLC7A0C1015YEY"
        """ICE BofAML US Corporate 10-15 Year Effective Yield (in Percent)"""

        US_CORPORATE_MORE_THAN_15_YEAR_EFFECTIVE_YIELD: str = "BAMLC8A0C15PYEY"
        """ICE BofAML US Corporate 15+ Year Effective Yield (in Percent)"""

        US_CORPORATE_3_TO_5_YEAR_EFFECTIVE_YIELD: str = "BAMLC2A0C35YEY"
        """ICE BofAML US Corporate 3-5 Year Effective Yield (in Percent)"""

        US_CORPORATE_5_TO_7_YEAR_EFFECTIVE_YIELD: str = "BAMLC3A0C57YEY"
        """ICE BofAML US Corporate 5-7 Year Effective Yield (in Percent)"""

        US_CORPORATE_7_TO_10_YEAR_EFFECTIVE_YIELD: str = "BAMLC4A0C710YEY"
        """ICE BofAML US Corporate 7-10 Year Effective Yield (in Percent)"""

        US_CORPORATE_A_EFFECTIVE_YIELD: str = "BAMLC0A3CAEY"
        """ICE BofAML US Corporate A Effective Yield (in Percent)"""

        US_CORPORATE_AA_EFFECTIVE_YIELD: str = "BAMLC0A2CAAEY"
        """ICE BofAML US Corporate AA Effective Yield (in Percent)"""

        US_CORPORATE_AAA_EFFECTIVE_YIELD: str = "BAMLC0A1CAAAEY"
        """ICE BofAML US Corporate AAA Effective Yield (in Percent)"""

        US_HIGH_YIELD_B_EFFECTIVE_YIELD: str = "BAMLH0A2HYBEY"
        """ICE BofAML US High Yield B Effective Yield (in Percent)"""

        US_HIGH_YIELD_BB_EFFECTIVE_YIELD: str = "BAMLH0A1HYBBEY"
        """ICE BofAML US High Yield BB Effective Yield (in Percent)"""

        US_CORPORATE_BBB_EFFECTIVE_YIELD: str = "BAMLC0A4CBBBEY"
        """ICE BofAML US Corporate BBB Effective Yield (in Percent)"""

        US_HIGH_YIELD_CC_COR_BELOW_EFFECTIVE_YIELD: str = "BAMLH0A3HYCEY"
        """ICE BofAML US High Yield CCC or Below Effective Yield (in Percent)"""

        US_CORPORATE_MASTER_EFFECTIVE_YIELD: str = "BAMLC0A0CMEY"
        """ICE BofAML US Corporate Master Effective Yield (in Percent)"""

        US_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_EFFECTIVE_YIELD: str = "BAMLEMUBCRPIUSEY"
        """ICE BofAML US Emerging Markets Corporate Plus Sub-Index Effective Yield (in Percent)"""

        US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_INDEX_EFFECTIVE_YIELD: str = "BAMLEMCLLCRPIUSEY"
        """ICE BofAML US Emerging Markets Liquid Corporate Plus Index Effective Yield (in Percent)"""

        US_HIGH_YIELD_MASTER_II_EFFECTIVE_YIELD: str = "BAMLH0A0HYM2EY"
        """ICE BofAML US High Yield Master II Effective Yield (in Percent)"""

        AAAA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM1BRRAAA2ACRPISYTW"
        """ICE BofAML AAA-A Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        AAAAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM1RAAA2ALCRPIUSSYTW"
        """ICE BofAML AAA-A US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        ASIA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMRACRPIASIASYTW"
        """ICE BofAML Asia Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        ASIA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMALLCRPIASIAUSSYTW"
        """ICE BofAML Asia US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        BAND_LOWER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM4BRRBLCRPISYTW"
        """ICE BofAML B and Lower Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        BAND_LOWER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM4RBLLCRPIUSSYTW"
        """ICE BofAML B and Lower US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        BB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM3BRRBBCRPISYTW"
        """ICE BofAML BB Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        BBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM3RBBLCRPIUSSYTW"
        """ICE BofAML BB US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        BBB_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM2BRRBBBCRPISYTW"
        """ICE BofAML BBB Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        BBBUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM2RBBBLCRPIUSSYTW"
        """ICE BofAML BBB US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        CROSSOVER_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEM5BCOCRPISYTW"
        """ICE BofAML Crossover Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        CROSSOVER_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMXOCOLCRPIUSSYTW"
        """ICE BofAML Crossover US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        EMERGING_MARKETS_CORPORATE_PLUS_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMCBPISYTW"
        """ICE BofAML Emerging Markets Corporate Plus Index Semi-Annual Yield to Worst (in Percent)"""

        EURO_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMEBCRPIESYTW"
        """ICE BofAML Euro Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        EURO_HIGH_YIELD_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLHE00EHYISYTW"
        """ICE BofAML Euro High Yield Index Semi-Annual Yield to Worst (in Percent)"""

        EMEA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMRECRPIEMEASYTW"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        EMEAUS_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMELLCRPIEMEAUSSYTW"
        """ICE BofAML Europe, the Middle East, and Africa (EMEA) US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMFSFCRPISYTW"
        """ICE BofAML Financial Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMFLFLCRPIUSSYTW"
        """ICE BofAML Financial US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        HIGH_GRADE_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMIBHGCRPISYTW"
        """ICE BofAML High Grade Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        HIGH_GRADE_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMHGHGLCRPIUSSYTW"
        """ICE BofAML High Grade US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        HIGH_YIELD_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMHBHYCRPISYTW"
        """ICE BofAML High Yield Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        HIGH_YIELD_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMHYHYLCRPIUSSYTW"
        """ICE BofAML High Yield US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        LATIN_AMERICA_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMRLCRPILASYTW"
        """ICE BofAML Latin America Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        LATIN_AMERICA_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMLLLCRPILAUSSYTW"
        """ICE BofAML Latin America US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        NON_FINANCIAL_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMNSNFCRPISYTW"
        """ICE BofAML Non-Financial Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        NON_FINANCIAL_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMNFNFLCRPIUSSYTW"
        """ICE BofAML Non-Financial US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        PRIVATE_SECTOR_ISSUERS_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMPTPRVICRPISYTW"
        """ICE BofAML Private Sector Issuers Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        PRIVATE_SECTOR_ISSUERS_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMPVPRIVSLCRPIUSSYTW"
        """ICE BofAML Private Sector Issuers US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        PUBLIC_SECTOR_ISSUERS_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMPBPUBSICRPISYTW"
        """ICE BofAML Public Sector Issuers Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        PUBLIC_SECTOR_ISSUERS_US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMPUPUBSLCRPIUSSYTW"
        """ICE BofAML Public Sector Issuers US Emerging Markets Liquid Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_1_TO_3_YEAR_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC1A0C13YSYTW"
        """ICE BofAML US Corporate 1-3 Year Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_10_TO_15_YEAR_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC7A0C1015YSYTW"
        """ICE BofAML US Corporate 10-15 Year Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_MORE_THAN_15_YEAR_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC8A0C15PYSYTW"
        """ICE BofAML US Corporate 15+ Year Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_3_TO_5_YEAR_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC2A0C35YSYTW"
        """ICE BofAML US Corporate 3-5 Year Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_5_TO_7_YEAR_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC3A0C57YSYTW"
        """ICE BofAML US Corporate 5-7 Year Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_7_TO_10_YEAR_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC4A0C710YSYTW"
        """ICE BofAML US Corporate 7-10 Year Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_A_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC0A3CASYTW"
        """ICE BofAML US Corporate A Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_AA_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC0A2CAASYTW"
        """ICE BofAML US Corporate AA Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_AAA_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC0A1CAAASYTW"
        """ICE BofAML US Corporate AAA Semi-Annual Yield to Worst (in Percent)"""

        US_HIGH_YIELD_B_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLH0A2HYBSYTW"
        """ICE BofAML US High Yield B Semi-Annual Yield to Worst (in Percent)"""

        US_HIGH_YIELD_BB_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLH0A1HYBBSYTW"
        """ICE BofAML US High Yield BB Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_BBB_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC0A4CBBBSYTW"
        """ICE BofAML US Corporate BBB Semi-Annual Yield to Worst (in Percent)"""

        US_HIGH_YIELD_CC_COR_BELOW_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLH0A3HYCSYTW"
        """ICE BofAML US High Yield CCC or Below Semi-Annual Yield to Worst (in Percent)"""

        US_CORPORATE_MASTER_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLC0A0CMSYTW"
        """ICE BofAML US Corporate Master Semi-Annual Yield to Worst (in Percent)"""

        US_EMERGING_MARKETS_CORPORATE_PLUS_SUB_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMUBCRPIUSSYTW"
        """ICE BofAML US Emerging Markets Corporate Plus Sub-Index Semi-Annual Yield to Worst (in Percent)"""

        US_EMERGING_MARKETS_LIQUID_CORPORATE_PLUS_INDEX_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLEMCLLCRPIUSSYTW"
        """ICE BofAML US Emerging Markets Liquid Corporate Plus Index Semi-Annual Yield to Worst (in Percent)"""

        US_HIGH_YIELD_MASTER_II_SEMI_ANNUAL_YIELDTO_WORST: str = "BAMLH0A0HYM2SYTW"
        """ICE BofAML US High Yield Master II Semi-Annual Yield to Worst (in Percent)"""

    class TradeWeightedIndexes(System.Object):
        """Trade Weight Indexes"""

        MAJOR_CURRENCIES_GOODS: str = "DTWEXM"
        """Trade Weighted U.S. Dollar Index: Major Currencies, Goods (in Index Mar 1973=100)"""

        OTHER_IMPORTANT_TRADING_PARTNERS_GOODS: str = "DTWEXO"
        """Trade Weighted U.S. Dollar Index: Other Important Trading Partners, Goods (in Index Jan 1997=100)"""

        BROAD_GOODS: str = "DTWEXB"
        """Trade Weighted U.S. Dollar Index: Broad, Goods (in Index Jan 1997=100)"""

        ADVANCED_FOREIGN_ECONOMIES_GOODS_AND_SERVICES: str = "DTWEXAFEGS"
        """Trade Weighted U.S. Dollar Index: Advanced Foreign Economies, Goods and Services (in Index Jan 2006=100)"""

        BROAD_GOODS_AND_SERVICES: str = "DTWEXBGS"
        """Trade Weighted U.S. Dollar Index: Broad, Goods and Services (in Index Jan 2006=100)"""

        EMERGING_MARKETS_ECONOMIES_GOODS_AND_SERVICES: str = "DTWEXEMEGS"
        """Trade Weighted U.S. Dollar Index: Emerging Markets Economies, Goods and Services (in Index Jan 2006=100)"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    is_auth_code_set: bool
    """Flag indicating whether or not the FRED auth code has been set yet"""

    def __init__(self) -> None:
        """Default Fred constructor"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance of FRED data.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied
        to an underlying symbol and requires that corporate
        events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    @staticmethod
    def set_auth_code(auth_code: str) -> None:
        """Set the FRED authentication code to request the data."""
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class FredApi(QuantConnect.Data.BaseData):
    """This class has no documentation."""

    class Observation(System.Object):
        """This class has no documentation."""

        @property
        def realtime_start(self) -> str:
            ...

        @property.setter
        def realtime_start(self, value: str) -> None:
            ...

        @property
        def realtime_end(self) -> str:
            ...

        @property.setter
        def realtime_end(self, value: str) -> None:
            ...

        @property
        def date(self) -> datetime.datetime:
            ...

        @property.setter
        def date(self, value: datetime.datetime) -> None:
            ...

        @property
        def value(self) -> str:
            ...

        @property.setter
        def value(self, value: str) -> None:
            ...

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def realtime_start(self) -> str:
        ...

    @property.setter
    def realtime_start(self, value: str) -> None:
        ...

    @property
    def realtime_end(self) -> str:
        ...

    @property.setter
    def realtime_end(self, value: str) -> None:
        ...

    @property
    def observation_start(self) -> str:
        ...

    @property.setter
    def observation_start(self, value: str) -> None:
        ...

    @property
    def observation_end(self) -> str:
        ...

    @property.setter
    def observation_end(self, value: str) -> None:
        ...

    @property
    def units(self) -> str:
        ...

    @property.setter
    def units(self, value: str) -> None:
        ...

    @property
    def output_type(self) -> int:
        ...

    @property.setter
    def output_type(self, value: int) -> None:
        ...

    @property
    def file_type(self) -> str:
        ...

    @property.setter
    def file_type(self, value: str) -> None:
        ...

    @property
    def order_by(self) -> str:
        ...

    @property.setter
    def order_by(self, value: str) -> None:
        ...

    @property
    def sort_order(self) -> str:
        ...

    @property.setter
    def sort_order(self, value: str) -> None:
        ...

    @property
    def count(self) -> int:
        ...

    @property.setter
    def count(self, value: int) -> None:
        ...

    @property
    def offset(self) -> int:
        ...

    @property.setter
    def offset(self, value: int) -> None:
        ...

    @property
    def limit(self) -> int:
        ...

    @property.setter
    def limit(self, value: int) -> None:
        ...

    @property
    def observations(self) -> System.Collections.Generic.IList[QuantConnect.DataSource.FredApi.Observation]:
        ...

    @property.setter
    def observations(self, value: System.Collections.Generic.IList[QuantConnect.DataSource.FredApi.Observation]) -> None:
        ...

    auth_code: str
    """Gets the FRED API token."""

    is_auth_code_set: bool
    """Returns true if the FRED API token has been set."""

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, content: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Readers the specified configuration.
        
        :param config: The configuration.
        :param content: The content.
        :param date: The date.
        :param is_live_mode: if set to true [is live mode].
        """
        ...

    @staticmethod
    def set_auth_code(auth_code: str) -> None:
        """
        Sets the EIA API token.
        
        :param auth_code: The EIA API token
        """
        ...


class SmartInsiderExecutionEntity(Enum):
    """Entity that intends to or executed the transaction"""

    ISSUER = 0
    """Issuer of the stock"""

    SUBSIDIARY = 1
    """Subsidiary of the issuer"""

    BROKER = 2
    """
    Brokers are commonly used to repurchase shares under mandate to avoid insider
    information rules and to allow repurchases to carry on through close periods
    """

    EMPLOYER_BENEFIT_TRUST = 3
    """Unknown - Transaction"""

    EMPLOYEE_BENEFIT_TRUST = 4
    """To cater for shares which will need to be transferred to employees as part of remunerative plans"""

    THIRD_PARTY = 5
    """Undisclosed independent third party. Likely to be a broker."""

    ERROR = 6
    """The field was not found in this enum"""


class SmartInsiderEventType(Enum):
    """Describes what will or has taken place in an execution"""

    AUTHORIZATION = 0
    """Notification that the board has gained the authority to repurchase"""

    INTENTION = 1
    """Notification of the board that shares will be repurchased."""

    TRANSACTION = 2
    """Repurchase transactions that have been actioned."""

    UPWARDS_REVISION = 3
    """Increase in the scope of the existing plan (extended date, increased value, etc.)"""

    DOWNWARDS_REVISION = 4
    """Decrease in the scope of the existing plan (shortened date, reduced value, etc.)"""

    REVISED_DETAILS = 5
    """General change of details of the plan (max/min price alteration, etc.)"""

    CANCELLATION = 6
    """Total cancellation of the plan"""

    SEEK_AUTHORIZATION = 7
    """Announcement by a company that the board of directors or management will be seeking to obtain authorisation for a repurchase plan."""

    PLAN_SUSPENSION = 8
    """Announcement by a company that a plan of repurchase has been suspended. Further details of the suspension are included in the note."""

    PLAN_RE_STARTED = 9
    """Announcement by a company that a suspended plan has been re-started. Further details of the suspension are included in the note."""

    NOT_SPECIFIED = 10
    """Announcement by a company not specified and/or not documented in the other categories. Further details are included in the note."""


class SmartInsiderEvent(QuantConnect.Data.BaseData, metaclass=abc.ABCMeta):
    """
    SmartInsider Intention and Transaction events. These are fields
    that are shared between intentions and transactions.
    """

    @property
    def transaction_id(self) -> str:
        """Proprietary unique field. Not nullable"""
        ...

    @property.setter
    def transaction_id(self, value: str) -> None:
        ...

    @property
    def event_type(self) -> typing.Optional[QuantConnect.DataSource.SmartInsiderEventType]:
        """Description of what has or will take place in an execution"""
        ...

    @property.setter
    def event_type(self, value: typing.Optional[QuantConnect.DataSource.SmartInsiderEventType]) -> None:
        ...

    @property
    def last_update(self) -> datetime.datetime:
        """The date when a transaction is updated after it has been reported. Not nullable"""
        ...

    @property.setter
    def last_update(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_i_ds_update(self) -> typing.Optional[datetime.datetime]:
        """Date that company identifiers were changed. Can be a name, Ticker Symbol or ISIN change"""
        ...

    @property.setter
    def last_i_ds_update(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def isin(self) -> str:
        """Industry classification number"""
        ...

    @property.setter
    def isin(self, value: str) -> None:
        ...

    @property
    def usd_market_cap(self) -> typing.Optional[float]:
        """The market capitalization at the time of the transaction stated in US Dollars"""
        ...

    @property.setter
    def usd_market_cap(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def company_id(self) -> typing.Optional[int]:
        """Smart Insider proprietary identifier for the company"""
        ...

    @property.setter
    def company_id(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def icb_industry(self) -> str:
        """FTSE Russell Sector Classification"""
        ...

    @property.setter
    def icb_industry(self, value: str) -> None:
        ...

    @property
    def icb_super_sector(self) -> str:
        """FTSE Russell Sector Classification"""
        ...

    @property.setter
    def icb_super_sector(self, value: str) -> None:
        ...

    @property
    def icb_sector(self) -> str:
        """FTSE Russell Sector Classification"""
        ...

    @property.setter
    def icb_sector(self, value: str) -> None:
        ...

    @property
    def icb_sub_sector(self) -> str:
        """FTSE Russell Sector Classification"""
        ...

    @property.setter
    def icb_sub_sector(self, value: str) -> None:
        ...

    @property
    def icb_code(self) -> typing.Optional[int]:
        """Numeric code that is the most granular level in ICB classification"""
        ...

    @property.setter
    def icb_code(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def company_name(self) -> str:
        """Company name. PLC is always excluded"""
        ...

    @property.setter
    def company_name(self, value: str) -> None:
        ...

    @property
    def previous_results_announcement_date(self) -> typing.Optional[datetime.datetime]:
        """Announcement date of last results, this will be the end date of the last "Close Period\""""
        ...

    @property.setter
    def previous_results_announcement_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def next_results_announcements_date(self) -> typing.Optional[datetime.datetime]:
        """Announcement date of next results, this will be the end date of the next "Close Period\""""
        ...

    @property.setter
    def next_results_announcements_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def next_close_begin(self) -> typing.Optional[datetime.datetime]:
        """Start date of next trading embargo ahead of scheduled results announcment"""
        ...

    @property.setter
    def next_close_begin(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def last_close_ended(self) -> typing.Optional[datetime.datetime]:
        """Date trading embargo (Close Period) is lifted as results are made public"""
        ...

    @property.setter
    def last_close_ended(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def security_description(self) -> str:
        """Type of security. Does not contain nominal value"""
        ...

    @property.setter
    def security_description(self, value: str) -> None:
        ...

    @property
    def ticker_country(self) -> str:
        """Country of local identifier, denoting where the trade took place"""
        ...

    @property.setter
    def ticker_country(self, value: str) -> None:
        ...

    @property
    def ticker_symbol(self) -> str:
        """Local market identifier"""
        ...

    @property.setter
    def ticker_symbol(self, value: str) -> None:
        ...

    @property
    def announcement_date(self) -> typing.Optional[datetime.datetime]:
        """Date Transaction was entered onto our system. Where a transaction is after the London market close (usually 4.30pm) this will be stated as the next day"""
        ...

    @property.setter
    def announcement_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def time_released(self) -> typing.Optional[datetime.datetime]:
        """Time the announcement first appeared on a Regulatory News Service or other disclosure system and became available to the market, time stated is local market time"""
        ...

    @property.setter
    def time_released(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def time_processed(self) -> typing.Optional[datetime.datetime]:
        """Time the transaction was entered into Smart Insider systems and appeared on their website, time stated is local to London, UK"""
        ...

    @property.setter
    def time_processed(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def time_released_utc(self) -> typing.Optional[datetime.datetime]:
        """Time the announcement first appeared on a Regulatory News Service or other disclosure system and became available to the market. Time stated is GMT standard"""
        ...

    @property.setter
    def time_released_utc(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def time_processed_utc(self) -> typing.Optional[datetime.datetime]:
        """Time the transaction was entered onto our systems and appeared on our website. Time stated is GMT standard"""
        ...

    @property.setter
    def time_processed_utc(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def announced_in(self) -> str:
        """Market in which the transaction was announced, this can reference more than one country"""
        ...

    @property.setter
    def announced_in(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Empty constructor required for cloning"""
        ...

    @overload
    def __init__(self, tsvLine: str) -> None:
        """
        Parses a line of TSV (tab delimited) from Smart Insider data
        
        This method is protected.
        
        :param tsvLine: Tab delimited line of data
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the timezone of this data source
        
        :returns: Timezone.
        """
        ...

    def from_raw_data(self, line: str, indexes: System.Collections.Generic.Dictionary[str, int]) -> bool:
        """
        Derived class instances populate their fields from raw TSV
        
        :param line: Line of raw TSV (raw with fields 46, 36, 14, 7 removed in descending order)
        :param indexes: Index per header column
        :returns: success of the parsing task.
        """
        ...

    @staticmethod
    def parse_date(date: str) -> datetime.datetime:
        """
        Attempts to normalize and parse SmartInsider dates that include a time component.
        
        :param date: Date string to parse
        :returns: DateTime object.
        """
        ...

    def to_line(self) -> str:
        """
        Converts data to TSV
        
        :returns: String of TSV.
        """
        ...


class SmartInsiderExecution(Enum):
    """Describes how the transaction was executed"""

    MARKET = 0
    """Took place via the open market"""

    TENDER_OFFER = 1
    """Via a companywide tender offer to all shareholders"""

    OFF_MARKET = 2
    """Under a specific agreement between the issuer and shareholder"""

    ERROR = 3
    """Field is not in this enum"""


class SmartInsiderExecutionHolding(Enum):
    """Details regarding the way holdings will be or were processed in a buyback execution"""

    TREASURY = 0
    """Held in treasury until they are sold back to the market"""

    CANCELLATION = 1
    """Immediately cancelled"""

    TRUST = 2
    """Held in trust, generally to cover employee renumerative plans"""

    SATISFY_EMPLOYEE_TAX = 3
    """Shares will be used to satisfy employee tax liabilities"""

    NOT_REPORTED = 4
    """Not disclosed by the issuer in the announcements"""

    SATISFY_STOCK_VESTING = 5
    """Shares will be used to satisfy vesting of employee stock"""

    ERROR = 6
    """The field was not found in the enum, or is representative of a SatisfyStockVesting entry."""


class SmartInsiderTransaction(QuantConnect.DataSource.SmartInsiderEvent):
    """Smart Insider Transaction - Execution of a stock buyback and details about the event occurred"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def buyback_date(self) -> typing.Optional[datetime.datetime]:
        """Date traded through the market"""
        ...

    @property.setter
    def buyback_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def execution(self) -> typing.Optional[QuantConnect.DataSource.SmartInsiderExecution]:
        """Describes how transaction was executed"""
        ...

    @property.setter
    def execution(self, value: typing.Optional[QuantConnect.DataSource.SmartInsiderExecution]) -> None:
        ...

    @property
    def execution_entity(self) -> typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionEntity]:
        """Describes which entity carried out the transaction"""
        ...

    @property.setter
    def execution_entity(self, value: typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionEntity]) -> None:
        ...

    @property
    def execution_holding(self) -> typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionHolding]:
        """Describes what will be done with those shares following repurchase"""
        ...

    @property.setter
    def execution_holding(self, value: typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionHolding]) -> None:
        ...

    @property
    def currency(self) -> str:
        """Currency of transation (ISO Code)"""
        ...

    @property.setter
    def currency(self, value: str) -> None:
        ...

    @property
    def execution_price(self) -> typing.Optional[float]:
        """Denominated in Currency of Transaction"""
        ...

    @property.setter
    def execution_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def amount(self) -> typing.Optional[float]:
        """Number of shares traded"""
        ...

    @property.setter
    def amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def gbp_value(self) -> typing.Optional[float]:
        """Currency conversion rates are updated daily and values are calculated at rate prevailing on the trade date"""
        ...

    @property.setter
    def gbp_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def eur_value(self) -> typing.Optional[float]:
        """Currency conversion rates are updated daily and values are calculated at rate prevailing on the trade date"""
        ...

    @property.setter
    def eur_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def usd_value(self) -> typing.Optional[float]:
        """Currency conversion rates are updated daily and values are calculated at rate prevailing on the trade date"""
        ...

    @property.setter
    def usd_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def note_text(self) -> str:
        """Free text which expains futher details about the trade"""
        ...

    @property.setter
    def note_text(self, value: str) -> None:
        ...

    @property
    def buyback_percentage(self) -> typing.Optional[float]:
        """Percentage of value of the trade as part of the issuers total Market Cap"""
        ...

    @property.setter
    def buyback_percentage(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def volume_percentage(self) -> typing.Optional[float]:
        """Percentage of the volume traded on the day of the buyback."""
        ...

    @property.setter
    def volume_percentage(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def conversion_rate(self) -> typing.Optional[float]:
        """Rate used to calculate 'Value (GBP)' from 'Price' multiplied by 'Amount'. Will be 1 where Currency is also 'GBP'"""
        ...

    @property.setter
    def conversion_rate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def amount_adjusted_factor(self) -> typing.Optional[float]:
        """Multiplier which can be applied to 'Amount' field to account for subsequent corporate action"""
        ...

    @property.setter
    def amount_adjusted_factor(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def price_adjusted_factor(self) -> typing.Optional[float]:
        """Multiplier which can be applied to 'Price' and 'LastClose' fields to account for subsequent corporate actions"""
        ...

    @property.setter
    def price_adjusted_factor(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def treasury_holding(self) -> typing.Optional[int]:
        """Post trade holding of the Treasury or Trust in the security traded"""
        ...

    @property.setter
    def treasury_holding(self, value: typing.Optional[int]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Empty contsructor required for Slice.Get{T}()"""
        ...

    @overload
    def __init__(self, line: str) -> None:
        """
        Creates an instance of the object by taking a formatted TSV line
        
        :param line: Line of formatted TSV
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the object to a new instance. This method
        is required for custom data sources that make use
        of properties with more complex types since otherwise
        the values will default to null using the default clone method
        
        :returns: A new cloned instance of this object.
        """
        ...

    def from_raw_data(self, line: str, indexes: System.Collections.Generic.Dictionary[str, int]) -> bool:
        """
        Creates an instance of the object by taking a formatted TSV line
        
        :param line: Line of formatted TSV
        :param indexes: Index per header column
        :returns: success of the parsing task.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Specifies the location of the data and directs LEAN where to load the data from
        
        :param config: Subscription configuration
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: Subscription data source object pointing LEAN to the data location.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reads the data into LEAN for use in algorithms
        
        :param config: Subscription configuration
        :param line: Line of TSV
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Instance of the object.
        """
        ...

    def to_line(self) -> str:
        """
        Converts the data to TSV
        
        :returns: String of TSV.
        """
        ...


class SmartInsiderIntention(QuantConnect.DataSource.SmartInsiderEvent):
    """Smart Insider Intentions - Intention to execute a stock buyback and details about the future event"""

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def execution(self) -> typing.Optional[QuantConnect.DataSource.SmartInsiderExecution]:
        """Describes how the transaction was executed"""
        ...

    @property.setter
    def execution(self, value: typing.Optional[QuantConnect.DataSource.SmartInsiderExecution]) -> None:
        ...

    @property
    def execution_entity(self) -> typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionEntity]:
        """Describes which entity intends to execute the transaction"""
        ...

    @property.setter
    def execution_entity(self, value: typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionEntity]) -> None:
        ...

    @property
    def execution_holding(self) -> typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionHolding]:
        """Describes what will be done with those shares following repurchase"""
        ...

    @property.setter
    def execution_holding(self, value: typing.Optional[QuantConnect.DataSource.SmartInsiderExecutionHolding]) -> None:
        ...

    @property
    def amount(self) -> typing.Optional[int]:
        """Number of shares to be or authorised to be traded"""
        ...

    @property.setter
    def amount(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def value_currency(self) -> str:
        """Currency of the value of shares to be/Authorised to be traded (ISO Code)"""
        ...

    @property.setter
    def value_currency(self, value: str) -> None:
        ...

    @property
    def amount_value(self) -> typing.Optional[int]:
        """Value of shares to be authorised to be traded"""
        ...

    @property.setter
    def amount_value(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def percentage(self) -> typing.Optional[float]:
        """Percentage of oustanding shares to be authorised to be traded"""
        ...

    @property.setter
    def percentage(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def authorization_start_date(self) -> typing.Optional[datetime.datetime]:
        """start of the period the intention/authorisation applies to"""
        ...

    @property.setter
    def authorization_start_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def authorization_end_date(self) -> typing.Optional[datetime.datetime]:
        """End of the period the intention/authorisation applies to"""
        ...

    @property.setter
    def authorization_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def price_currency(self) -> str:
        """Currency of min/max prices (ISO Code)"""
        ...

    @property.setter
    def price_currency(self, value: str) -> None:
        ...

    @property
    def minimum_price(self) -> typing.Optional[float]:
        """Minimum price shares will or may be purchased at"""
        ...

    @property.setter
    def minimum_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def maximum_price(self) -> typing.Optional[float]:
        """Maximum price shares will or may be purchased at"""
        ...

    @property.setter
    def maximum_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def note_text(self) -> str:
        """Free text which explains further details about the trade"""
        ...

    @property.setter
    def note_text(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Empty constructor required for Slice.Get{T}()"""
        ...

    @overload
    def __init__(self, line: str) -> None:
        """
        Constructs instance of this via a *formatted* TSV line (tab delimited)
        
        :param line: Line of formatted TSV data
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the object to a new instance. This method
        is required for custom data sources that make use
        of properties with more complex types since otherwise
        the values will default to null using the default clone method
        
        :returns: A new cloned instance of this object.
        """
        ...

    def from_raw_data(self, line: str, indexes: System.Collections.Generic.Dictionary[str, int]) -> bool:
        """
        Constructs a new instance from unformatted TSV data
        
        :param line: Line of raw TSV (raw with fields 46, 36, 14, 7 removed in descending order)
        :param indexes: Index per header column
        :returns: success of the parsing task.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Specifies the location of the data and directs LEAN where to load the data from
        
        :param config: Subscription configuration
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Subscription data source object pointing LEAN to the data location.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Loads and reads the data to be used in LEAN
        
        :param config: Subscription configuration
        :param line: TSV line
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Instance of the object.
        """
        ...

    def to_line(self) -> str:
        """
        Converts the data to TSV
        
        :returns: String of TSV.
        """
        ...


class SmartInsiderIntentionUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Smart Insider Intentions Universe"""

    @property
    def amount(self) -> typing.Optional[int]:
        """Number of shares to be or authorised to be traded"""
        ...

    @property.setter
    def amount(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def amount_value(self) -> typing.Optional[int]:
        """Value of shares to be authorised to be traded"""
        ...

    @property.setter
    def amount_value(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def percentage(self) -> typing.Optional[float]:
        """Percentage of oustanding shares to be authorised to be traded"""
        ...

    @property.setter
    def percentage(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def minimum_price(self) -> typing.Optional[float]:
        """Minimum price shares will or may be purchased at"""
        ...

    @property.setter
    def minimum_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def maximum_price(self) -> typing.Optional[float]:
        """Maximum price shares will or may be purchased at"""
        ...

    @property.setter
    def maximum_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def usd_market_cap(self) -> typing.Optional[float]:
        """Market Capitalization in USD"""
        ...

    @property.setter
    def usd_market_cap(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clone implementation"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the timezone of this data source
        
        :returns: Timezone.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Specifies the location of the data and directs LEAN where to load the data from
        
        :param config: Subscription configuration
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Subscription data source object pointing LEAN to the data location.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Loads and reads the data to be used in LEAN
        
        :param config: Subscription configuration
        :param line: TSV line
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Instance of the object.
        """
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class SmartInsiderTransactionUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """Smart Insider Transaction Universe"""

    @property
    def amount(self) -> typing.Optional[float]:
        """Number of shares traded"""
        ...

    @property.setter
    def amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def minimum_execution_price(self) -> typing.Optional[float]:
        """Minimum Value of Denominated in Currency of Transaction"""
        ...

    @property.setter
    def minimum_execution_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def maximum_execution_price(self) -> typing.Optional[float]:
        """Maximum Value of Denominated in Currency of Transaction"""
        ...

    @property.setter
    def maximum_execution_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def usd_value(self) -> typing.Optional[float]:
        """Currency conversion rates are updated daily and values are calculated at rate prevailing on the trade date"""
        ...

    @property.setter
    def usd_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def buyback_percentage(self) -> typing.Optional[float]:
        """Percentage of value of the trade as part of the issuers total Market Cap"""
        ...

    @property.setter
    def buyback_percentage(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def volume_percentage(self) -> typing.Optional[float]:
        """Percentage of the volume traded on the day of the buyback."""
        ...

    @property.setter
    def volume_percentage(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def usd_market_cap(self) -> typing.Optional[float]:
        """Market Capitalization in USD"""
        ...

    @property.setter
    def usd_market_cap(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """Clone implementation"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the timezone of this data source
        
        :returns: Timezone.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Specifies the location of the data and directs LEAN where to load the data from
        
        :param config: Subscription configuration
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Subscription data source object pointing LEAN to the data location.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Loads and reads the data to be used in LEAN
        
        :param config: Subscription configuration
        :param line: TSV line
        :param date: Algorithm date
        :param is_live_mode: Is live mode
        :returns: Instance of the object.
        """
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverTwitterFollowers(QuantConnect.Data.BaseData):
    """Example custom data type"""

    @property
    def followers(self) -> int:
        """Number of followers of the company's Twitter page on the given date"""
        ...

    @property.setter
    def followers(self, value: int) -> None:
        ...

    @property
    def day_percent_change(self) -> typing.Optional[float]:
        """Day-over-day change in company's follower count"""
        ...

    @property.setter
    def day_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def week_percent_change(self) -> typing.Optional[float]:
        """Week-over-week change in company's follower count"""
        ...

    @property.setter
    def week_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def month_percent_change(self) -> typing.Optional[float]:
        """Month-over-month change in company's follower count"""
        ...

    @property.setter
    def month_percent_change(self, value: typing.Optional[float]) -> None:
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
        """Time the data became available"""
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Clones the data
        
        :returns: A clone of the object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data is sparse.
        If true, we disable logging for missing files
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source is tied to an underlying symbol and requires that corporate events be applied to it as well, such as renames and delistings
        
        :returns: false.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverQuantTwitterFollowers(QuantConnect.DataSource.QuiverTwitterFollowers):
    """Obsoleted QuiverQuantTwitterFollowers class"""

    def __init__(self) -> None:
        """Obsolete QuiverTwitterFollowers constructor"""
        ...


class QuiverTwitterFollowersUniverse(QuantConnect.Data.BaseData):
    """Universe Selection helper class for QuiverQuant Twitter Followers dataset"""

    @property
    def followers(self) -> int:
        """Number of followers of the company's Twitter page on the given date"""
        ...

    @property.setter
    def followers(self, value: int) -> None:
        ...

    @property
    def day_percent_change(self) -> typing.Optional[float]:
        """Day-over-day change in company's follower count"""
        ...

    @property.setter
    def day_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def week_percent_change(self) -> typing.Optional[float]:
        """Week-over-week change in company's follower count"""
        ...

    @property.setter
    def week_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def month_percent_change(self) -> typing.Optional[float]:
        """Month-over-month change in company's follower count"""
        ...

    @property.setter
    def month_percent_change(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time the data became available"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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
        Parses the data from the line provided and loads it into LEAN
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        :returns: New instance.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def to_string(self) -> str:
        """Converts the instance to string"""
        ...


class QuiverQuantTwitterFollowersUniverse(QuantConnect.DataSource.QuiverTwitterFollowersUniverse):
    """Obsoleted QuiverQuantTwitterFollowersUniverse class"""

    def __init__(self) -> None:
        """Obsolete QuiverTwitterFollowersUniverse constructor"""
        ...


class TiingoNews(QuantConnect.Data.IndexedBaseData):
    """
    Tiingo news data
    https://api.tiingo.com/documentation/news
    """

    DATA_SOURCE_ID: int
    """Data source ID"""

    @property
    def source(self) -> str:
        """The domain the news source is from."""
        ...

    @property.setter
    def source(self, value: str) -> None:
        ...

    @property
    def crawl_date(self) -> datetime.datetime:
        """
        The datetime the news story was added to Tiingos database in UTC.
        This is always recorded by Tiingo and the news source has no input on this date.
        """
        ...

    @property.setter
    def crawl_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def url(self) -> str:
        """URL of the news article."""
        ...

    @property.setter
    def url(self, value: str) -> None:
        ...

    @property
    def published_date(self) -> datetime.datetime:
        """
        The datetime the news story was published in UTC. This is usually reported by the news source and not by Tiingo.
        If the news source does not declare a published date, Tiingo will use the time the news story was discovered by our crawler farm.
        """
        ...

    @property.setter
    def published_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.List[str]:
        """Tags that are mapped and discovered by Tiingo."""
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.List[str]) -> None:
        ...

    @property
    def description(self) -> str:
        """Long-form description of the news story."""
        ...

    @property.setter
    def description(self, value: str) -> None:
        ...

    @property
    def title(self) -> str:
        """Title of the news article."""
        ...

    @property.setter
    def title(self, value: str) -> None:
        ...

    @property
    def article_id(self) -> str:
        """Unique identifier specific to the news article."""
        ...

    @property.setter
    def article_id(self, value: str) -> None:
        ...

    @property
    def symbols(self) -> System.Collections.Generic.List[QuantConnect.Symbol]:
        """What symbols are mentioned in the news story."""
        ...

    @property.setter
    def symbols(self, value: System.Collections.Generic.List[QuantConnect.Symbol]) -> None:
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        For backtesting returns the index source for a date
        For live trading will return the source url to use, not using the index mechanism
        
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

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, content: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method,
            and returns a new instance of the object
            each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param content: Content of the source document
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


class TiingoNewsJsonConverter(JsonConverter):
    """
    Helper json converter class used to convert a list of Tiingo news data
    into List{TiingoNews}
    """

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str] = None) -> None:
        """
        Creates a new instance of the json converter
        
        :param symbol: The Symbol instance associated with this news
        """
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    @staticmethod
    def deserialize_news(token: typing.Any) -> QuantConnect.DataSource.TiingoNews:
        """
        Helper method to deserialize a single json Tiingo news
        
        :param token: The json token containing the Tiingo news to deserialize
        :returns: The deserialized TiingoNews instance.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class ExtractAlphaFiscalPeriod(System.Object):
    """Fiscal period that the ExtractAlphaTrueBeat instance has forecasts for."""

    @property
    def fiscal_year(self) -> int:
        """Fiscal year (i.e. the year that the financial report applies to in 10-Q and/or 10-K SEC filings)"""
        ...

    @property.setter
    def fiscal_year(self, value: int) -> None:
        ...

    @property
    def fiscal_quarter(self) -> typing.Optional[int]:
        """
        Fiscal quarter (i.e. the quarter that the financial report applies to in 10-Q filings).
        If this is null, then the fiscal period being reported is for the full year of the FiscalYear
        """
        ...

    @property.setter
    def fiscal_quarter(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def end(self) -> typing.Optional[datetime.datetime]:
        """The date that the fiscal quarter ends"""
        ...

    @property.setter
    def end(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def expected_report_date(self) -> typing.Optional[datetime.datetime]:
        """The date that the SEC report for the fiscal period is expected to be released publicly"""
        ...

    @property.setter
    def expected_report_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def annual(self) -> bool:
        """Returns true if the fiscal period is for the whole fiscal year (all quarters)"""
        ...

    @property
    def quarterly(self) -> bool:
        """Returns true if the fiscal period is for a single quarter only"""
        ...


class ExtractAlphaTrueBeatEarningsMetric(Enum):
    """The earnings metric/type being forecasted"""

    EPS = 0
    """Earnings per share"""

    REVENUE = 1
    """Revenue"""


class ExtractAlphaTrueBeat(QuantConnect.Data.BaseData):
    """
    EPS/Revenue earnings surprise forecasting for upcoming financial reports released
    by regulatory agencies (e.g. United States SEC)
    """

    @property
    def fiscal_period(self) -> QuantConnect.DataSource.ExtractAlphaFiscalPeriod:
        """The fiscal period that is being forecasted"""
        ...

    @property.setter
    def fiscal_period(self, value: QuantConnect.DataSource.ExtractAlphaFiscalPeriod) -> None:
        ...

    @property
    def earnings_metric(self) -> QuantConnect.DataSource.ExtractAlphaTrueBeatEarningsMetric:
        """The earnings metric being forecasted (e.g. EPS, revenue)"""
        ...

    @property.setter
    def earnings_metric(self, value: QuantConnect.DataSource.ExtractAlphaTrueBeatEarningsMetric) -> None:
        ...

    @property
    def analyst_estimates_count(self) -> int:
        """The number of analyst estimates that the TrueBeat used in its calculation"""
        ...

    @property.setter
    def analyst_estimates_count(self, value: int) -> None:
        ...

    @property
    def true_beat(self) -> float:
        """
        The forecasted earnings surprise percentage, relative to consensus estimates.
        TrueBeat is calculated as the total sum of the ExpertBeat, TrendBeat, and ManagementBeat metrics.
        """
        ...

    @property.setter
    def true_beat(self, value: float) -> None:
        ...

    @property
    def expert_beat(self) -> typing.Optional[float]:
        """The component of TrueBeat that is derived from top analyst estimates"""
        ...

    @property.setter
    def expert_beat(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trend_beat(self) -> typing.Optional[float]:
        """The component of TrueBeat that is derived from trends in stock and peer surprises"""
        ...

    @property.setter
    def trend_beat(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def management_beat(self) -> typing.Optional[float]:
        """The component of TrueBeat that is derived from management activity (e.g. guidance)"""
        ...

    @property.setter
    def management_beat(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The time that the data became available to the algorithm"""
        ...

    @property.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
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

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """
        Formats a string with TrueBeat data
        
        :returns: string containing TrueBeat information.
        """
        ...


class ExtractAlphaTrueBeats(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """A collection of Extra Alpha True Beats for a Symbol and date"""

    def add(self, new_data_point: QuantConnect.Data.BaseData) -> None:
        """
        Adds a new data point to this collection
        
        :param new_data_point: The new data point to add
        """
        ...

    def add_range(self, new_data_points: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]) -> None:
        """
        Adds a new data points to this collection
        
        :param new_data_points: The new data points to add
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The NodaTime.DateTimeZone of this data type.
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

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
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

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def to_string(self) -> str:
        """
        Formats a string with TrueBeat data
        
        :returns: string containing TrueBeat information.
        """
        ...


class NullData(QuantConnect.Data.BaseData):
    """Represents a custom data type place holder"""


