from typing import overload
from enum import Enum
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Algorithm.Framework.Execution
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Algorithm.Framework.Portfolio.SignalExports
import QuantConnect.Algorithm.Framework.Risk
import QuantConnect.Algorithm.Framework.Selection
import QuantConnect.Benchmarks
import QuantConnect.Brokerages
import QuantConnect.Commands
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Fundamental
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Indicators
import QuantConnect.Indicators.CandlestickPatterns
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Orders
import QuantConnect.Python
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Cfd
import QuantConnect.Securities.Crypto
import QuantConnect.Securities.CryptoFuture
import QuantConnect.Securities.Equity
import QuantConnect.Securities.Forex
import QuantConnect.Securities.Future
import QuantConnect.Securities.Index
import QuantConnect.Securities.IndexOption
import QuantConnect.Securities.Option
import QuantConnect.Statistics
import QuantConnect.Storage
import System
import System.Collections.Concurrent
import System.Collections.Generic
import pandas

QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T = typing.TypeVar("QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T")
QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T = typing.TypeVar("QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T")
QuantConnect_Algorithm_QCAlgorithm_Consolidate_T = typing.TypeVar("QuantConnect_Algorithm_QCAlgorithm_Consolidate_T")
QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T = typing.TypeVar("QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T")
QuantConnect_Algorithm_QCAlgorithm_GetDataTypedHistory_T = typing.TypeVar("QuantConnect_Algorithm_QCAlgorithm_GetDataTypedHistory_T")
QuantConnect_Algorithm__EventContainer_Callable = typing.TypeVar("QuantConnect_Algorithm__EventContainer_Callable")
QuantConnect_Algorithm__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Algorithm__EventContainer_ReturnType")


class ConstituentUniverseDefinitions(System.Object):
    """
    Provides helpers for defining constituent universes based on the Morningstar
    asset classification AssetClassification https://www.morningstar.com/
    """

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Initializes a new instance of the ConstituentUniverseDefinitions class
        
        :param algorithm: The algorithm instance, used for obtaining the default UniverseSettings
        """
        ...

    def aerospace_and_defense(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar AerospaceAndDefense industry group MorningstarIndustryGroupCode"""
        ...

    def aggressive_growth(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies whose revenues and earnings have both been growing significantly faster than
        the general economy.
        """
        ...

    def agriculture(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Agriculture industry group MorningstarIndustryGroupCode"""
        ...

    def asset_management(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar AssetManagement industry group MorningstarIndustryGroupCode"""
        ...

    def banks(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Banks industry group MorningstarIndustryGroupCode"""
        ...

    def beverages_alcoholic(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar BeveragesAlcoholic industry group MorningstarIndustryGroupCode"""
        ...

    def beverages_non_alcoholic(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar BeveragesNonAlcoholic industry group MorningstarIndustryGroupCode"""
        ...

    def biotechnology(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Biotechnology industry group MorningstarIndustryGroupCode"""
        ...

    def building_materials(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar BuildingMaterials industry group MorningstarIndustryGroupCode"""
        ...

    def business_services(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar BusinessServices industry group MorningstarIndustryGroupCode"""
        ...

    def capital_markets(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar CapitalMarkets industry group MorningstarIndustryGroupCode"""
        ...

    def chemicals(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Chemicals industry group MorningstarIndustryGroupCode"""
        ...

    def classic_growth(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies that are growing respectably faster than the general economy, and often pay a
        steady dividend. They tend to be mature and solidly profitable businesses.
        """
        ...

    def conglomerates(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Conglomerates industry group MorningstarIndustryGroupCode"""
        ...

    def construction(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Construction industry group MorningstarIndustryGroupCode"""
        ...

    def consumer_packaged_goods(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar ConsumerPackagedGoods industry group MorningstarIndustryGroupCode"""
        ...

    def credit_services(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar CreditServices industry group MorningstarIndustryGroupCode"""
        ...

    def cyclicals(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies in the cyclicals and durables sectors, except those in the three types below.
        The profits of cyclicals tend to rise and fall with the general economy.
        """
        ...

    def distressed(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies that have had consistently declining cash flows and earnings over the past
        three years, and/or very high debt.
        """
        ...

    def diversified_financial_services(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar DiversifiedFinancialServices industry group MorningstarIndustryGroupCode"""
        ...

    def drug_manufacturers(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar DrugManufacturers industry group MorningstarIndustryGroupCode"""
        ...

    def education(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Education industry group MorningstarIndustryGroupCode"""
        ...

    def farm_and_heavy_construction_machinery(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar FarmAndHeavyConstructionMachinery industry group MorningstarIndustryGroupCode"""
        ...

    def fixtures_and_appliances(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar FixturesAndAppliances industry group MorningstarIndustryGroupCode"""
        ...

    def forest_products(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar ForestProducts industry group MorningstarIndustryGroupCode"""
        ...

    def hard_asset(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies that deal in assets such as oil, metals, and real estate, which tend to do
        well in inflationary environments.
        """
        ...

    def hardware(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Hardware industry group MorningstarIndustryGroupCode"""
        ...

    def healthcare_plans(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar HealthcarePlans industry group MorningstarIndustryGroupCode"""
        ...

    def healthcare_providers_and_services(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar HealthcareProvidersAndServices industry group MorningstarIndustryGroupCode"""
        ...

    def high_yield(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies that have dividend yields at least twice the average for large-cap stocks.
        They tend to be mature, slow-growing companies.
        """
        ...

    def homebuilding_and_construction(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar HomebuildingAndConstruction industry group MorningstarIndustryGroupCode"""
        ...

    def industrial_distribution(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar IndustrialDistribution industry group MorningstarIndustryGroupCode"""
        ...

    def industrial_products(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar IndustrialProducts industry group MorningstarIndustryGroupCode"""
        ...

    def insurance(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Insurance industry group MorningstarIndustryGroupCode"""
        ...

    def interactive_media(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar InteractiveMedia industry group MorningstarIndustryGroupCode"""
        ...

    def large_core(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def large_growth(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def large_value(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def manufacturing_apparel_and_accessories(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar ManufacturingApparelAndAccessories industry group MorningstarIndustryGroupCode"""
        ...

    def media_diversified(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar MediaDiversified industry group MorningstarIndustryGroupCode"""
        ...

    def medical_devices_and_instruments(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar MedicalDevicesAndInstruments industry group MorningstarIndustryGroupCode"""
        ...

    def medical_diagnostics_and_research(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar MedicalDiagnosticsAndResearch industry group MorningstarIndustryGroupCode"""
        ...

    def medical_distribution(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar MedicalDistribution industry group MorningstarIndustryGroupCode"""
        ...

    def metals_and_mining(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar MetalsAndMining industry group MorningstarIndustryGroupCode"""
        ...

    def mid_core(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def mid_growth(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def mid_value(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def oil_and_gas(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar OilAndGas industry group MorningstarIndustryGroupCode"""
        ...

    def other_energy_sources(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar OtherEnergySources industry group MorningstarIndustryGroupCode"""
        ...

    def packaging_and_containers(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar PackagingAndContainers industry group MorningstarIndustryGroupCode"""
        ...

    def personal_services(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar PersonalServices industry group MorningstarIndustryGroupCode"""
        ...

    def real_estate(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar RealEstate industry group MorningstarIndustryGroupCode"""
        ...

    def rei_ts(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar REITs industry group MorningstarIndustryGroupCode"""
        ...

    def restaurants(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Restaurants industry group MorningstarIndustryGroupCode"""
        ...

    def retail_cyclical(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar RetailCyclical industry group MorningstarIndustryGroupCode"""
        ...

    def retail_defensive(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar RetailDefensive industry group MorningstarIndustryGroupCode"""
        ...

    def semiconductors(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Semiconductors industry group MorningstarIndustryGroupCode"""
        ...

    def slow_growth(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies that have shown slow revenue and earnings growth (typically less than the rate
        of GDP growth) over at least three years.
        """
        ...

    def small_core(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def small_growth(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def small_value(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Classifies securities according to market capitalization and growth and value factor"""
        ...

    def software(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Software industry group MorningstarIndustryGroupCode"""
        ...

    def speculative_growth(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Universe which selects companies that have shown strong revenue growth but slower or spotty earnings growth.
        Very small or young companies also tend to fall into this class.
        """
        ...

    def steel(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Steel industry group MorningstarIndustryGroupCode"""
        ...

    def telecommunication_services(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar TelecommunicationServices industry group MorningstarIndustryGroupCode"""
        ...

    def tobacco_products(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar TobaccoProducts industry group MorningstarIndustryGroupCode"""
        ...

    def transportation(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar Transportation industry group MorningstarIndustryGroupCode"""
        ...

    def travel_and_leisure(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar TravelAndLeisure industry group MorningstarIndustryGroupCode"""
        ...

    def utilities_independent_power_producers(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar UtilitiesIndependentPowerProducers industry group MorningstarIndustryGroupCode"""
        ...

    def utilities_regulated(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar UtilitiesRegulated industry group MorningstarIndustryGroupCode"""
        ...

    def vehicles_and_parts(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar VehiclesAndParts industry group MorningstarIndustryGroupCode"""
        ...

    def waste_management(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """Morningstar WasteManagement industry group MorningstarIndustryGroupCode"""
        ...


class UniverseDefinitions(System.Object):
    """Provides helpers for defining universes in algorithms"""

    @property
    def dollar_volume(self) -> QuantConnect.Algorithm.DollarVolumeUniverseDefinitions:
        """Gets a helper that provides methods for creating universes based on daily dollar volumes"""
        ...

    @property.setter
    def dollar_volume(self, value: QuantConnect.Algorithm.DollarVolumeUniverseDefinitions) -> None:
        ...

    @property
    def unchanged(self) -> QuantConnect.Data.UniverseSelection.Universe.UnchangedUniverse:
        """Specifies that universe selection should not make changes on this iteration"""
        ...

    @property
    def qc_500(self) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new fine universe that contains the constituents of QC500 index based onthe company fundamentals
        The algorithm creates a default tradable and liquid universe containing 500 US equities
        which are chosen at the first trading day of each month.
        """
        ...

    def __init__(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> None:
        """
        Initializes a new instance of the UniverseDefinitions class
        
        :param algorithm: The algorithm instance, used for obtaining the default UniverseSettings
        """
        ...

    @overload
    def etf(self, etf_ticker: str, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param etf_ticker: Ticker of the ETF to get constituents for
        :param market: Market of the ETF
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, etf_ticker: str, market: str, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param etf_ticker: Ticker of the ETF to get constituents for
        :param market: Market of the ETF
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, etf_ticker: str, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param etf_ticker: Ticker of the ETF to get constituents for
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, etf_ticker: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param etf_ticker: Ticker of the ETF to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, etf_ticker: str, market: str = None, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, universe_filter_func: typing.Any = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param etf_ticker: Ticker of the ETF to get constituents for
        :param market: Market of the ETF
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, etf_ticker: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param etf_ticker: Ticker of the ETF to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, symbol: typing.Union[QuantConnect.Symbol, str], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided ETF
        
        :param symbol: ETF Symbol to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, symbol: typing.Union[QuantConnect.Symbol, str], universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided ETF
        
        :param symbol: ETF Symbol to get constituents for
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def etf(self, symbol: typing.Union[QuantConnect.Symbol, str], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, universe_filter_func: typing.Any = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided ETF
        
        :param symbol: ETF Symbol to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New ETF constituents Universe.
        """
        ...

    @overload
    def index(self, index_ticker: str, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_ticker: Ticker of the index to get constituents for
        :param market: Market of the index
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_ticker: str, market: str, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_ticker: Ticker of the index to get constituents for
        :param market: Market of the index
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_ticker: str, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_ticker: Ticker of the index to get constituents for
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_ticker: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_ticker: Ticker of the index to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_ticker: str, market: str = None, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, universe_filter_func: typing.Any = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_ticker: Ticker of the index to get constituents for
        :param market: Market of the index
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_ticker: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_ticker: Ticker of the index to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_symbol: typing.Union[QuantConnect.Symbol, str], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_symbol: Index Symbol to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_symbol: typing.Union[QuantConnect.Symbol, str], universe_filter_func: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_symbol: Index Symbol to get constituents for
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    @overload
    def index(self, index_symbol: typing.Union[QuantConnect.Symbol, str], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, universe_filter_func: typing.Any = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a universe for the constituents of the provided
        
        :param index_symbol: Index Symbol to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        :returns: New index constituents Universe.
        """
        ...

    def top(self, count: int, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new coarse universe that contains the top count of stocks
        by daily dollar volume
        
        :param count: The number of stock to select
        :param universe_settings: The settings for stocks added by this universe. Defaults to QCAlgorithm.UniverseSettings
        :returns: A new coarse universe for the top count of stocks by dollar volume.
        """
        ...


class QCAlgorithm(System.MarshalByRefObject, QuantConnect.Interfaces.IAlgorithm):
    """
    QC Algorithm Base Class - Handle the basic requirements of a trading algorithm,
    allowing user to focus on event methods. The QCAlgorithm class implements Portfolio,
    Securities, Transactions and Data Subscription Management.
    """

    @property
    def history_provider(self) -> QuantConnect.Interfaces.IHistoryProvider:
        """Gets or sets the history provider for the algorithm"""
        ...

    @property.setter
    def history_provider(self, value: QuantConnect.Interfaces.IHistoryProvider) -> None:
        ...

    @property
    def is_warming_up(self) -> bool:
        """Gets whether or not this algorithm is still warming up"""
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, str]:
        """Access to the runtime statistics property. User provided statistics."""
        ...

    @property
    def universe_manager(self) -> QuantConnect.Securities.UniverseManager:
        """Gets universe manager which holds universes keyed by their symbol"""
        ...

    @property
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the universe settings to be used when adding securities via universe selection"""
        ...

    @property
    def universe(self) -> QuantConnect.Algorithm.UniverseDefinitions:
        """Gets a helper that provides pre-defined universe definitions, such as top dollar volume"""
        ...

    @property
    def pandas_converter(self) -> QuantConnect.Python.PandasConverter:
        """PandasConverter for this Algorithm"""
        ...

    @property
    def transactions(self) -> QuantConnect.Securities.SecurityTransactionManager:
        """Transaction Manager - Process transaction fills and order management."""
        ...

    @property.setter
    def transactions(self, value: QuantConnect.Securities.SecurityTransactionManager) -> None:
        ...

    @property
    def enable_automatic_indicator_warm_up(self) -> bool:
        """
        Gets whether or not WarmUpIndicator is allowed to warm up indicators
        
        Please use Settings.AutomaticIndicatorWarmUp
        """
        warnings.warn("Please use Settings.AutomaticIndicatorWarmUp", DeprecationWarning)

    @property.setter
    def enable_automatic_indicator_warm_up(self, value: bool) -> None:
        warnings.warn("Please use Settings.AutomaticIndicatorWarmUp", DeprecationWarning)

    MAX_NAME_AND_TAGS_LENGTH: int = 200
    """
    Maximum length of the name or tags of a backtest
    
    This field is protected.
    """

    MAX_TAGS_COUNT: int = 100
    """
    Maximum number of tags allowed for a backtest
    
    This field is protected.
    """

    @property
    def market_hours_database(self) -> QuantConnect.Securities.MarketHoursDatabase:
        """
        Gets the market hours database in use by this algorithm
        
        This property is protected.
        """
        ...

    @property
    def symbol_properties_database(self) -> QuantConnect.Securities.SymbolPropertiesDatabase:
        """
        Gets the symbol properties database in use by this algorithm
        
        This property is protected.
        """
        ...

    @property
    def insights_generated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, QuantConnect.Algorithm.Framework.Alphas.GeneratedInsightsCollection], None], None]:
        """Event fired when the algorithm generates insights"""
        ...

    @property
    def securities(self) -> QuantConnect.Securities.SecurityManager:
        """
        Security collection is an array of the security objects such as Equities and FOREX. Securities data
        manages the properties of tradeable assets such as price, open and close time and holdings information.
        """
        ...

    @property.setter
    def securities(self, value: QuantConnect.Securities.SecurityManager) -> None:
        ...

    @property
    def active_securities(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Symbol, QuantConnect.Securities.Security]:
        """
        Read-only dictionary containing all active securities. An active security is
        a security that is currently selected by the universe or has holdings or open orders.
        """
        ...

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """
        Portfolio object provieds easy access to the underlying security-holding properties; summed together in a way to make them useful.
        This saves the user time by providing common portfolio requests in a single
        """
        ...

    @property.setter
    def portfolio(self, value: QuantConnect.Securities.SecurityPortfolioManager) -> None:
        ...

    @property
    def account_currency(self) -> str:
        """Gets the account currency"""
        ...

    @property
    def time_keeper(self) -> QuantConnect.Interfaces.ITimeKeeper:
        """Gets the time keeper instance"""
        ...

    @property
    def subscription_manager(self) -> QuantConnect.Data.SubscriptionManager:
        """
        Generic Data Manager - Required for compiling all data feeds in order, and passing them into algorithm event methods.
        The subscription manager contains a list of the data feed's we're subscribed to and properties of each data feed.
        """
        ...

    @property.setter
    def subscription_manager(self, value: QuantConnect.Data.SubscriptionManager) -> None:
        ...

    @property
    def signal_export(self) -> QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportManager:
        """
        SignalExport - Allows sending export signals to different 3rd party API's. For example, it allows to send signals
        to Collective2, CrunchDAO and Numerai API's
        """
        ...

    @property
    def project_id(self) -> int:
        """The project id associated with this algorithm if any"""
        ...

    @property.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def brokerage_model(self) -> QuantConnect.Brokerages.IBrokerageModel:
        """Gets the brokerage model - used to model interactions with specific brokerages."""
        ...

    @property
    def brokerage_name(self) -> QuantConnect.Brokerages.BrokerageName:
        """Gets the brokerage name."""
        ...

    @property
    def brokerage_message_handler(self) -> QuantConnect.Brokerages.IBrokerageMessageHandler:
        """
        Gets the brokerage message handler used to decide what to do
        with each message sent from the brokerage
        """
        ...

    @property.setter
    def brokerage_message_handler(self, value: QuantConnect.Brokerages.IBrokerageMessageHandler) -> None:
        ...

    @property
    def risk_free_interest_rate_model(self) -> QuantConnect.Data.IRiskFreeInterestRateModel:
        """Gets the risk free interest rate model used to get the interest rates"""
        ...

    @property
    def notify(self) -> QuantConnect.Notifications.NotificationManager:
        """Notification Manager for Sending Live Runtime Notifications to users about important events."""
        ...

    @property.setter
    def notify(self, value: QuantConnect.Notifications.NotificationManager) -> None:
        ...

    @property
    def schedule(self) -> QuantConnect.Scheduling.ScheduleManager:
        """Gets schedule manager for adding/removing scheduled events"""
        ...

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Gets or sets the current status of the algorithm"""
        ...

    @property.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    def security_initializer(self) -> QuantConnect.Securities.ISecurityInitializer:
        """Gets an instance that is to be used to initialize newly created securities."""
        ...

    @property
    def trade_builder(self) -> QuantConnect.Interfaces.ITradeBuilder:
        """Gets the Trade Builder to generate trades from executions"""
        ...

    @property
    def candlestick_patterns(self) -> QuantConnect.Algorithm.CandlestickPatterns:
        """Gets an instance to access the candlestick pattern helper methods"""
        ...

    @property
    def date_rules(self) -> QuantConnect.Scheduling.DateRules:
        """Gets the date rules helper object to make specifying dates for events easier"""
        ...

    @property
    def time_rules(self) -> QuantConnect.Scheduling.TimeRules:
        """Gets the time rules helper object to make specifying times for events easier"""
        ...

    @property
    def trading_calendar(self) -> QuantConnect.TradingCalendar:
        """Gets trading calendar populated with trading events"""
        ...

    @property
    def settings(self) -> QuantConnect.Interfaces.IAlgorithmSettings:
        """Gets the user settings for the algorithm"""
        ...

    @property
    def option_chain_provider(self) -> QuantConnect.Interfaces.IOptionChainProvider:
        """
        Gets the option chain provider, used to get the list of option contracts for an underlying symbol
        
        OptionChainProvider property is will soon be deprecated. " +
                    "The new OptionChain() method should be used to fetch equity and index option chains, " +
                    "which will contain additional data per contract, like daily price data, implied volatility and greeks.
        """
        warnings.warn("OptionChainProvider property is will soon be deprecated. " +
                    "The new OptionChain() method should be used to fetch equity and index option chains, " +
                    "which will contain additional data per contract, like daily price data, implied volatility and greeks.", DeprecationWarning)

    @property
    def future_chain_provider(self) -> QuantConnect.Interfaces.IFutureChainProvider:
        """Gets the future chain provider, used to get the list of future contracts for an underlying symbol"""
        ...

    @property
    def default_order_properties(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Gets the default order properties"""
        ...

    @property.setter
    def default_order_properties(self, value: QuantConnect.Interfaces.IOrderProperties) -> None:
        ...

    @property
    def name(self) -> str:
        """
        Public name for the algorithm as automatically generated by the IDE. Intended for helping distinguish logs by noting
        the algorithm-id.
        """
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.HashSet[str]:
        """A list of tags associated with the algorithm or the backtest, useful for categorization"""
        ...

    @property.setter
    def tags(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @property
    def name_updated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, str], None], None]:
        """Event fired algorithm's name is changed"""
        ...

    @property
    def tags_updated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, System.Collections.Generic.HashSet[str]], None], None]:
        """Event fired when the tag collection is updated"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Read-only value for current time frontier of the algorithm in terms of the TimeZone"""
        ...

    @property
    def utc_time(self) -> datetime.datetime:
        """Current date/time in UTC."""
        ...

    @property
    def time_zone(self) -> typing.Any:
        """
        Gets the time zone used for the Time property. The default value
        is TimeZones.NewYork
        """
        ...

    @property
    def start_date(self) -> datetime.datetime:
        """Value of the user set start-date from the backtest."""
        ...

    @property
    def end_date(self) -> datetime.datetime:
        """Value of the user set start-date from the backtest. Controls the period of the backtest."""
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm Id for this backtest or live algorithm."""
        ...

    @property
    def live_mode(self) -> bool:
        """Boolean property indicating the algorithm is currently running in live mode."""
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    @property
    def deployment_target(self) -> QuantConnect.DeploymentTarget:
        """Deployment target, either local or cloud."""
        ...

    @property
    def debug_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Storage for debugging messages before the event handler has passed control back to the Lean Engine."""
        ...

    @property.setter
    def debug_messages(self, value: System.Collections.Concurrent.ConcurrentQueue[str]) -> None:
        ...

    @property
    def log_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Storage for log messages before the event handlers have passed control back to the Lean Engine."""
        ...

    @property.setter
    def log_messages(self, value: System.Collections.Concurrent.ConcurrentQueue[str]) -> None:
        ...

    @property
    def run_time_error(self) -> System.Exception:
        """Gets the run time error from the algorithm, or null if none was encountered."""
        ...

    @property.setter
    def run_time_error(self, value: System.Exception) -> None:
        ...

    @property
    def error_messages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """List of error messages generated by the user's code calling the "Error" function."""
        ...

    @property.setter
    def error_messages(self, value: System.Collections.Concurrent.ConcurrentQueue[str]) -> None:
        ...

    @property
    def current_slice(self) -> QuantConnect.Data.Slice:
        """Returns the current Slice object"""
        ...

    @property
    def object_store(self) -> QuantConnect.Storage.ObjectStore:
        """Gets the object store, used for persistence"""
        ...

    @property
    def statistics(self) -> QuantConnect.Statistics.StatisticsResults:
        """The current statistics for the running algorithm."""
        ...

    @property
    def benchmark(self) -> QuantConnect.Benchmarks.IBenchmark:
        """Benchmark"""
        ...

    @property
    def debug_mode(self) -> bool:
        """
        Enables additional logging of framework models including:
        All insights, portfolio targets, order events, and any risk management altered targets
        """
        ...

    @property.setter
    def debug_mode(self, value: bool) -> None:
        ...

    @property
    def universe_selection(self) -> QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel:
        """Gets or sets the universe selection model."""
        ...

    @property.setter
    def universe_selection(self, value: QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel) -> None:
        ...

    @property
    def alpha(self) -> QuantConnect.Algorithm.Framework.Alphas.IAlphaModel:
        """Gets or sets the alpha model"""
        ...

    @property.setter
    def alpha(self, value: QuantConnect.Algorithm.Framework.Alphas.IAlphaModel) -> None:
        ...

    @property
    def insights(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightManager:
        """Gets the insight manager"""
        ...

    @property
    def portfolio_construction(self) -> QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel:
        """Gets or sets the portfolio construction model"""
        ...

    @property.setter
    def portfolio_construction(self, value: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel) -> None:
        ...

    @property
    def execution(self) -> QuantConnect.Algorithm.Framework.Execution.IExecutionModel:
        """Gets or sets the execution model"""
        ...

    @property.setter
    def execution(self, value: QuantConnect.Algorithm.Framework.Execution.IExecutionModel) -> None:
        ...

    @property
    def risk_management(self) -> QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel:
        """Gets or sets the risk management model"""
        ...

    @property.setter
    def risk_management(self, value: QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel) -> None:
        ...

    def __init__(self) -> None:
        """
        QCAlgorithm Base Class Constructor - Initialize the underlying QCAlgorithm components.
        QCAlgorithm manages the transactions, portfolio, charting and security subscriptions for the users algorithms.
        """
        ...

    def a(self, target: typing.Union[QuantConnect.Symbol, str], reference: typing.Union[QuantConnect.Symbol, str], alpha_period: int = 1, beta_period: int = 252, resolution: typing.Optional[QuantConnect.Resolution] = None, risk_free_rate: typing.Optional[float] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.Alpha:
        """
        Creates a Alpha indicator for the given target symbol in relation with the reference used.
        The indicator will be automatically updated on the given resolution.
        
        :param target: The target symbol whose Alpha value we want
        :param reference: The reference symbol to compare with the target symbol
        :param alpha_period: The period of the Alpha indicator
        :param beta_period: The period of the Beta indicator
        :param resolution: The resolution
        :param risk_free_rate: The risk free rate
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Alpha indicator for the given parameters.
        """
        ...

    def abands(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, width: float = 4, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.AccelerationBands:
        """
        Creates a new Acceleration Bands indicator.
        
        :param symbol: The symbol whose Acceleration Bands we want.
        :param period: The period of the three moving average (middle, upper and lower band).
        :param width: A coefficient specifying the distance between the middle band and upper or lower bands.
        :param moving_average_type: Type of the moving average.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar.
        """
        ...

    def ad(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.AccumulationDistribution:
        """
        Creates a new AccumulationDistribution indicator.
        
        :param symbol: The symbol whose AD we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The AccumulationDistribution indicator for the requested symbol over the specified period.
        """
        ...

    def add_alpha(self, alpha: QuantConnect.Algorithm.Framework.Alphas.IAlphaModel) -> None:
        """
        Adds a new alpha model
        
        :param alpha: Model that generates alpha to add
        """
        ...

    def add_cfd(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ...) -> QuantConnect.Securities.Cfd.Cfd:
        """
        Creates and adds a new Cfd security to the algorithm
        
        :param ticker: The currency pair
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The cfd trading market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :returns: The new Cfd security.
        """
        ...

    def add_chart(self, chart: QuantConnect.Chart) -> None:
        """
        Add a Chart object to algorithm collection
        
        :param chart: Chart object to add to collection.
        """
        ...

    @overload
    def add_command(self, type: typing.Type) -> None:
        """
        Register a command type to be used
        
        :param type: The command type
        """
        ...

    @overload
    def add_command(self) -> None:
        """Register a command type to be used"""
        ...

    def add_crypto(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ...) -> QuantConnect.Securities.Crypto.Crypto:
        """
        Creates and adds a new Crypto security to the algorithm
        
        :param ticker: The currency pair
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The cfd trading market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :returns: The new Crypto security.
        """
        ...

    def add_crypto_future(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ...) -> QuantConnect.Securities.CryptoFuture.CryptoFuture:
        """
        Creates and adds a new CryptoFuture security to the algorithm
        
        :param ticker: The currency pair
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The cfd trading market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :returns: The new CryptoFuture security.
        """
        ...

    @overload
    def add_data(self, type: typing.Type, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        The data is added with a default time zone of NewYork (Eastern Daylight Savings Time).
        This method is meant for custom data types that require a ticker, but have no underlying Symbol.
        Examples of data sources that meet this criteria are U.S. Treasury Yield Curve Rates and Trading Economics data
        
        :param type: Data source type
        :param ticker: Key/Ticker for data
        :param resolution: Resolution of the data
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, type: typing.Type, underlying: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        The data is added with a default time zone of NewYork (Eastern Daylight Savings Time).
        This adds a Symbol to the `Underlying` property in the custom data Symbol object.
        Use this method when adding custom data with a ticker from the past, such as "AOL"
        before it became "TWX", or if you need to filter using custom data and place trades on the
        Symbol associated with the custom data.
        
        :param type: Data source type
        :param underlying: The underlying symbol for the custom data
        :param resolution: Resolution of the data
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, type: typing.Type, ticker: str, resolution: typing.Optional[QuantConnect.Resolution], time_zone: typing.Any, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        This method is meant for custom data types that require a ticker, but have no underlying Symbol.
        Examples of data sources that meet this criteria are U.S. Treasury Yield Curve Rates and Trading Economics data
        
        :param type: Data source type
        :param ticker: Key/Ticker for data
        :param resolution: Resolution of the Data Required
        :param time_zone: Specifies the time zone of the raw data
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, type: typing.Type, underlying: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution], time_zone: typing.Any, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        This adds a Symbol to the `Underlying` property in the custom data Symbol object.
        Use this method when adding custom data with a ticker from the past, such as "AOL"
        before it became "TWX", or if you need to filter using custom data and place trades on the
        Symbol associated with the custom data.
        
        :param type: Data source type
        :param underlying: The underlying symbol for the custom data
        :param resolution: Resolution of the Data Required
        :param time_zone: Specifies the time zone of the raw data
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, data_type: typing.Type, ticker: str, resolution: typing.Optional[QuantConnect.Resolution], time_zone: typing.Any, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        This method is meant for custom data types that require a ticker, but have no underlying Symbol.
        Examples of data sources that meet this criteria are U.S. Treasury Yield Curve Rates and Trading Economics data
        
        :param data_type: Data source type
        :param ticker: Key/Ticker for data
        :param resolution: Resolution of the Data Required
        :param time_zone: Specifies the time zone of the raw data
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, data_type: typing.Type, underlying: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, time_zone: typing.Any = None, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        This adds a Symbol to the `Underlying` property in the custom data Symbol object.
        Use this method when adding custom data with a ticker from the past, such as "AOL"
        before it became "TWX", or if you need to filter using custom data and place trades on the
        Symbol associated with the custom data.
        
        :param data_type: Data source type
        :param resolution: Resolution of the Data Required
        :param time_zone: Specifies the time zone of the raw data
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, type: typing.Type, ticker: str, properties: QuantConnect.Securities.SymbolProperties, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source including symbol properties and exchange hours,
        all other vars are not required and will use defaults.
        This overload reflects the C# equivalent for custom properties and market hours
        
        :param type: Data source type
        :param ticker: Key/Ticker for data
        :param properties: The properties of this new custom data
        :param exchange_hours: The Exchange hours of this symbol
        :param resolution: Resolution of the Data Required
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        The data is added with a default time zone of NewYork (Eastern Daylight Savings Time)
        
        :param ticker: Key/Ticker for data
        :param resolution: Resolution of the data
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, underlying: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        The data is added with a default time zone of NewYork (Eastern Daylight Savings Time)
        
        :param underlying: The underlying symbol for the custom data
        :param resolution: Resolution of the data
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution], fill_forward: bool, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        The data is added with a default time zone of NewYork (Eastern Daylight Savings Time)
        
        :param ticker: Key/Ticker for data
        :param resolution: Resolution of the Data Required
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, underlying: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution], fill_forward: bool, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        The data is added with a default time zone of NewYork (Eastern Daylight Savings Time)
        
        :param underlying: The underlying symbol for the custom data
        :param resolution: Resolution of the Data Required
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution], time_zone: typing.Any, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        
        :param ticker: Key/Ticker for data
        :param resolution: Resolution of the Data Required
        :param time_zone: Specifies the time zone of the raw data
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, underlying: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution], time_zone: typing.Any, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source, requiring only the minimum config options.
        
        :param underlying: The underlying symbol for the custom data
        :param resolution: Resolution of the Data Required
        :param time_zone: Specifies the time zone of the raw data
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    @overload
    def add_data(self, ticker: str, properties: QuantConnect.Securities.SymbolProperties, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = False, leverage: float = 1.0) -> QuantConnect.Securities.Security:
        """
        AddData a new user defined data source including symbol properties and exchange hours,
        all other vars are not required and will use defaults.
        
        :param ticker: Key/Ticker for data
        :param properties: The properties of this new custom data
        :param exchange_hours: The Exchange hours of this symbol
        :param resolution: Resolution of the Data Required
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :returns: The new Security.
        """
        ...

    def add_equity(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ..., extended_market_hours: bool = False, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> QuantConnect.Securities.Equity.Equity:
        """
        Creates and adds a new Equity security to the algorithm
        
        :param ticker: The equity ticker symbol
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The equity's market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extended_market_hours: True to send data during pre and post market sessions. Default is false
        :param data_normalization_mode: The price scaling mode to use for the equity
        :returns: The new Equity security.
        """
        ...

    def add_forex(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ...) -> QuantConnect.Securities.Forex.Forex:
        """
        Creates and adds a new Forex security to the algorithm
        
        :param ticker: The currency pair
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The foreign exchange trading market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :returns: The new Forex security.
        """
        ...

    def add_future(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ..., extended_market_hours: bool = False, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: int = 0) -> QuantConnect.Securities.Future.Future:
        """
        Creates and adds a new Future security to the algorithm
        
        :param ticker: The future ticker
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The futures market, . Default is value null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extended_market_hours: Use extended market hours data
        :param data_mapping_mode: The contract mapping mode to use for the continuous future contract
        :param data_normalization_mode: The price scaling mode to use for the continuous future contract
        :param contract_depth_offset: The continuous future contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        :returns: The new Future security.
        """
        ...

    def add_future_contract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, leverage: float = ..., extended_market_hours: bool = False) -> QuantConnect.Securities.Future.Future:
        """
        Creates and adds a new single Future contract to the algorithm
        
        :param symbol: The futures contract symbol
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extended_market_hours: Use extended market hours data
        :returns: The new Future security.
        """
        ...

    def add_future_option(self, symbol: typing.Union[QuantConnect.Symbol, str], option_filter: typing.Callable[[QuantConnect.Securities.OptionFilterUniverse], QuantConnect.Securities.OptionFilterUniverse] = None) -> None:
        """
        Creates and adds a new Future Option contract to the algorithm.
        
        :param symbol: The Future canonical symbol (i.e. Symbol returned from AddFuture)
        :param option_filter: Filter to apply to option contracts loaded as part of the universe
        :returns: The new Option security, containing a Future as its underlying.
        """
        ...

    def add_future_option_contract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, leverage: float = ..., extended_market_hours: bool = False) -> QuantConnect.Securities.Option.Option:
        """
        Adds a future option contract to the algorithm.
        
        :param symbol: Option contract Symbol
        :param resolution: Resolution of the option contract, i.e. the granularity of the data
        :param fill_forward: If true, this will fill in missing data points with the previous data point
        :param leverage: The leverage to apply to the option contract
        :param extended_market_hours: Use extended market hours data
        :returns: Option security.
        """
        ...

    def addiff(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.AdvanceDeclineDifference:
        """
        Creates a new Advance/Decline Difference indicator
        
        :param symbols: The symbols whose A/D Difference we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Advance/Decline Difference indicator for the requested symbol over the specified period.
        """
        ...

    def add_index(self, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True) -> QuantConnect.Securities.Index.Index:
        """
        Creates and adds a new Index security to the algorithm
        
        :param ticker: The currency pair
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The index trading market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :returns: The new Index security.
        """
        ...

    @overload
    def add_index_option(self, underlying: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True) -> QuantConnect.Securities.IndexOption.IndexOption:
        """
        Creates and adds index options to the algorithm.
        
        :param underlying: The underlying ticker of the Index Option
        :param resolution: Resolution of the index option contracts, i.e. the granularity of the data
        :param market: The foreign exchange trading market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, this will fill in missing data points with the previous data point
        :returns: Canonical Option security.
        """
        ...

    @overload
    def add_index_option(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True) -> QuantConnect.Securities.IndexOption.IndexOption:
        """
        Creates and adds index options to the algorithm.
        
        :param symbol: The Symbol of the Security returned from AddIndex
        :param resolution: Resolution of the index option contracts, i.e. the granularity of the data
        :param fill_forward: If true, this will fill in missing data points with the previous data point
        :returns: Canonical Option security.
        """
        ...

    @overload
    def add_index_option(self, symbol: typing.Union[QuantConnect.Symbol, str], target_option: str, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True) -> QuantConnect.Securities.IndexOption.IndexOption:
        """
        Creates and adds index options to the algorithm.
        
        :param symbol: The Symbol of the Security returned from AddIndex
        :param target_option: The target option ticker. This is useful when the option ticker does not match the underlying, e.g. SPX index and the SPXW weekly option. If null is provided will use underlying
        :param resolution: Resolution of the index option contracts, i.e. the granularity of the data
        :param fill_forward: If true, this will fill in missing data points with the previous data point
        :returns: Canonical Option security.
        """
        ...

    @overload
    def add_index_option(self, underlying: str, target_option: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True) -> QuantConnect.Securities.IndexOption.IndexOption:
        """
        Creates and adds index options to the algorithm.
        
        :param underlying: The underlying ticker of the Index Option
        :param target_option: The target option ticker. This is useful when the option ticker does not match the underlying, e.g. SPX index and the SPXW weekly option. If null is provided will use underlying
        :param resolution: Resolution of the index option contracts, i.e. the granularity of the data
        :param market: The foreign exchange trading market, . Default value is null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, this will fill in missing data points with the previous data point
        :returns: Canonical Option security.
        """
        ...

    def add_index_option_contract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True) -> QuantConnect.Securities.IndexOption.IndexOption:
        """
        Adds an index option contract to the algorithm.
        
        :param symbol: Symbol of the index option contract
        :param resolution: Resolution of the index option contract, i.e. the granularity of the data
        :param fill_forward: If true, this will fill in missing data points with the previous data point
        :returns: Index Option Contract.
        """
        ...

    @overload
    def add_option(self, underlying: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ...) -> QuantConnect.Securities.Option.Option:
        """
        Creates and adds a new equity Option security to the algorithm
        
        :param underlying: The underlying equity ticker
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The equity's market, . Default is value null and looked up using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :returns: The new Option security.
        """
        ...

    @overload
    def add_option(self, underlying: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ...) -> QuantConnect.Securities.Option.Option:
        """
        Creates and adds a new Option security to the algorithm.
        This method can be used to add options with non-equity asset classes
        to the algorithm (e.g. Future Options).
        
        :param underlying: Underlying asset Symbol to use as the option's underlying
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The option's market, . Default value is null, but will be resolved using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, data will be provided to the algorithm every Second, Minute, Hour, or Day, while the asset is open and depending on the Resolution this option was configured to use.
        :param leverage: The requested leverage for the
        :returns: The new option security instance.
        """
        ...

    @overload
    def add_option(self, underlying: typing.Union[QuantConnect.Symbol, str], target_option: str, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, fill_forward: bool = True, leverage: float = ...) -> QuantConnect.Securities.Option.Option:
        """
        Creates and adds a new Option security to the algorithm.
        This method can be used to add options with non-equity asset classes
        to the algorithm (e.g. Future Options).
        
        :param underlying: Underlying asset Symbol to use as the option's underlying
        :param target_option: The target option ticker. This is useful when the option ticker does not match the underlying, e.g. SPX index and the SPXW weekly option. If null is provided will use underlying
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param market: The option's market, . Default value is null, but will be resolved using BrokerageModel.DefaultMarkets in AddSecurity{T}
        :param fill_forward: If true, data will be provided to the algorithm every Second, Minute, Hour, or Day, while the asset is open and depending on the Resolution this option was configured to use.
        :param leverage: The requested leverage for the
        :returns: The new option security instance.
        """
        ...

    def add_option_contract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, leverage: float = ..., extended_market_hours: bool = False) -> QuantConnect.Securities.Option.Option:
        """
        Creates and adds a new single Option contract to the algorithm
        
        :param symbol: The option contract symbol
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param fill_forward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extended_market_hours: Use extended market hours data
        :returns: The new Option security.
        """
        ...

    def add_risk_management(self, risk_management: QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel) -> None:
        """
        Adds a new risk management model
        
        :param risk_management: Model defining how risk is managed to add
        """
        ...

    @overload
    def add_security(self, security_type: QuantConnect.SecurityType, ticker: str, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, extended_market_hours: bool = False, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> QuantConnect.Securities.Security:
        """
        Add specified data to our data subscriptions. QuantConnect will funnel this data to the handle data routine.
        
        :param security_type: MarketType Type: Equity, Commodity, Future, FOREX or Crypto
        :param ticker: The security ticker
        :param resolution: Resolution of the Data Required
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param extended_market_hours: Use extended market hours data
        :param data_mapping_mode: The contract mapping mode to use for the security
        :param data_normalization_mode: The price scaling mode to use for the security
        """
        ...

    @overload
    def add_security(self, security_type: QuantConnect.SecurityType, ticker: str, resolution: typing.Optional[QuantConnect.Resolution], fill_forward: bool, leverage: float, extended_market_hours: bool, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> QuantConnect.Securities.Security:
        """
        Add specified data to required list. QC will funnel this data to the handle data routine.
        
        :param security_type: MarketType Type: Equity, Commodity, Future, FOREX or Crypto
        :param ticker: The security ticker
        :param resolution: Resolution of the Data Required
        :param fill_forward: When no data available on a tradebar, return the last data that was generated
        :param leverage: Custom leverage per security
        :param extended_market_hours: Use extended market hours data
        :param data_mapping_mode: The contract mapping mode to use for the security
        :param data_normalization_mode: The price scaling mode to use for the security
        """
        ...

    @overload
    def add_security(self, security_type: QuantConnect.SecurityType, ticker: str, resolution: typing.Optional[QuantConnect.Resolution], market: str, fill_forward: bool, leverage: float, extended_market_hours: bool, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> QuantConnect.Securities.Security:
        """
        Set a required SecurityType-symbol and resolution for algorithm
        
        :param security_type: MarketType Type: Equity, Commodity, Future, FOREX or Crypto
        :param ticker: The security ticker, e.g. AAPL
        :param resolution: Resolution of the MarketType required: MarketData, Second or Minute
        :param market: The market the requested security belongs to, such as 'usa' or 'fxcm'
        :param fill_forward: If true, returns the last available data even if none in that timeslice.
        :param leverage: leverage for this security
        :param extended_market_hours: Use extended market hours data
        :param data_mapping_mode: The contract mapping mode to use for the security
        :param data_normalization_mode: The price scaling mode to use for the security
        """
        ...

    @overload
    def add_security(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, leverage: float = ..., extended_market_hours: bool = False, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: int = 0) -> QuantConnect.Securities.Security:
        """
        Set a required SecurityType-symbol and resolution for algorithm
        
        :param symbol: The security Symbol
        :param resolution: Resolution of the MarketType required: MarketData, Second or Minute
        :param fill_forward: If true, returns the last available data even if none in that timeslice.
        :param leverage: leverage for this security
        :param extended_market_hours: Use extended market hours data
        :param data_mapping_mode: The contract mapping mode to use for the security
        :param data_normalization_mode: The price scaling mode to use for the security
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        :returns: The new Security that was added to the algorithm.
        """
        ...

    def add_series(self, chart: str, series: str, series_type: QuantConnect.SeriesType, unit: str = "$") -> None:
        """
        Add a series object for charting. This is useful when initializing charts with
        series other than type = line. If a series exists in the chart with the same name,
        then it is replaced.
        
        :param chart: The chart name
        :param series: The series name
        :param series_type: The type of series, i.e, Scatter
        :param unit: The unit of the y axis, usually $
        """
        ...

    def add_tag(self, tag: str) -> None:
        """
        Adds a tag to the algorithm
        
        :param tag: The tag to add
        """
        ...

    @overload
    def add_universe(self, universe: QuantConnect.Data.UniverseSelection.Universe) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Adds the universe to the algorithm
        
        :param universe: The universe to be added
        """
        ...

    @overload
    def add_universe(self, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Resolution.Daily, Market.USA, and UniverseSettings
        
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Resolution.Daily, Market.USA, and UniverseSettings
        
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Resolution.Daily, Market.USA, and UniverseSettings
        
        :param name: A unique name for this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Resolution.Daily, Market.USA, and UniverseSettings
        
        :param name: A unique name for this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Resolution.Daily, and Market.USA
        
        :param name: A unique name for this universe
        :param universe_settings: The settings used for securities added by this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Resolution.Daily, and Market.USA
        
        :param name: A unique name for this universe
        :param universe_settings: The settings used for securities added by this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, resolution: QuantConnect.Resolution, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Market.USA and UniverseSettings
        
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, resolution: QuantConnect.Resolution, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, Market.USA and UniverseSettings
        
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, resolution: QuantConnect.Resolution, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, and Market.USA
        
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param universe_settings: The settings used for securities added by this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, resolution: QuantConnect.Resolution, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property. This universe will use the defaults
        of SecurityType.Equity, and Market.USA
        
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param universe_settings: The settings used for securities added by this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str, resolution: QuantConnect.Resolution, market: str, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property.
        
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param market: The market for selected symbols
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, security_type: QuantConnect.SecurityType, name: str, resolution: QuantConnect.Resolution, market: str, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This will use the default universe settings
        specified via the UniverseSettings property.
        
        :param security_type: The security type the universe produces
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param market: The market for selected symbols
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, security_type: QuantConnect.SecurityType, name: str, resolution: QuantConnect.Resolution, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm
        
        :param security_type: The security type the universe produces
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param market: The market for selected symbols
        :param universe_settings: The subscription settings to use for newly created subscriptions
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, name: str = None, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]] = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm
        
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param market: The market for selected symbols
        :param universe_settings: The subscription settings to use for newly created subscriptions
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.Fundamental.Fundamental]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This is for coarse fundamental US Equity data and
        will be executed on day changes in the NewYork time zone (TimeZones.NewYork)
        
        :param selector: Defines an initial coarse selection
        """
        ...

    @overload
    def add_universe(self, date_rule: QuantConnect.Scheduling.IDateRule, selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.Fundamental.Fundamental]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This is for coarse fundamental US Equity data and
        will be executed based on the provided IDateRule in the NewYork time zone (TimeZones.NewYork)
        
        :param date_rule: Date rule that will be used to set the Data.UniverseSelection.UniverseSettings.Schedule
        :param selector: Defines an initial coarse selection
        """
        ...

    @overload
    def add_universe(self, coarse_selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.CoarseFundamental]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]], fine_selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.Fundamental.FineFundamental]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This is for coarse and fine fundamental US Equity data and
        will be executed on day changes in the NewYork time zone (TimeZones.NewYork)
        
        :param coarse_selector: Defines an initial coarse selection
        :param fine_selector: Defines a more detailed selection with access to more data
        """
        ...

    @overload
    def add_universe(self, universe: QuantConnect.Data.UniverseSelection.Universe, fine_selector: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.Fundamental.Fundamental]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This is for fine fundamental US Equity data and
        will be executed on day changes in the NewYork time zone (TimeZones.NewYork)
        
        :param universe: The universe to be filtered with fine fundamental selection
        :param fine_selector: Defines a more detailed selection with access to more data
        """
        ...

    @overload
    def add_universe(self, name: str, selector: typing.Callable[[datetime.datetime], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This can be used to return a list of string
        symbols retrieved from anywhere and will loads those symbols under the US Equity market.
        
        :param name: A unique name for this universe
        :param selector: Function delegate that accepts a DateTime and returns a collection of string symbols
        """
        ...

    @overload
    def add_universe(self, name: str, resolution: QuantConnect.Resolution, selector: typing.Callable[[datetime.datetime], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. This can be used to return a list of string
        symbols retrieved from anywhere and will loads those symbols under the US Equity market.
        
        :param name: A unique name for this universe
        :param resolution: The resolution this universe should be triggered on
        :param selector: Function delegate that accepts a DateTime and returns a collection of string symbols
        """
        ...

    @overload
    def add_universe(self, security_type: QuantConnect.SecurityType, name: str, resolution: QuantConnect.Resolution, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[datetime.datetime], System.Collections.Generic.IEnumerable[str]]) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new user defined universe that will fire on the requested resolution during market hours.
        
        :param security_type: The security type of the universe
        :param name: A unique name for this universe
        :param resolution: The resolution this universe should be triggered on
        :param market: The market of the universe
        :param universe_settings: The subscription settings used for securities added from this universe
        :param selector: Function delegate that accepts a DateTime and returns a collection of string symbols
        """
        ...

    @overload
    def add_universe(self, t: typing.Type, name: str, selector: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. this will use the default universe settings
        specified via the UniverseSettings property. this universe will use the defaults
        of Securitytype.Equity, Resolution.Daily, Market.USA, and UniverseSettings
        
        :param t: the data type
        :param name: A unique name for this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, t: typing.Type, name: str, resolution: QuantConnect.Resolution, selector: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. this will use the default universe settings
        specified via the UniverseSettings property. this universe will use the defaults
        of Securitytype.Equity, Market.USA and UniverseSettings
        
        :param t: the data type
        :param name: A unique name for this universe
        :param resolution: the expected resolution of the universe data
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, t: typing.Type, name: str, resolution: QuantConnect.Resolution, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. this will use the default universe settings
        specified via the UniverseSettings property. this universe will use the defaults
        of Securitytype.Equity, and Market.USA
        
        :param t: the data type
        :param name: A unique name for this universe
        :param resolution: the expected resolution of the universe data
        :param universe_settings: the settings used for securities added by this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, t: typing.Type, name: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. this will use the default universe settings
        specified via the UniverseSettings property. this universe will use the defaults
        of Securitytype.Equity, Resolution.Daily, and Market.USA
        
        :param t: the data type
        :param name: A unique name for this universe
        :param universe_settings: the settings used for securities added by this universe
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, t: typing.Type, security_type: QuantConnect.SecurityType, name: str, resolution: QuantConnect.Resolution, market: str, selector: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm. this will use the default universe settings
        specified via the UniverseSettings property.
        
        :param t: the data type
        :param securitytype: the security type the universe produces
        :param name: A unique name for this universe
        :param resolution: the expected resolution of the universe data
        :param market: the market for selected symbols
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, t: typing.Type, security_type: QuantConnect.SecurityType, name: str, resolution: QuantConnect.Resolution, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm
        
        :param t: the data type
        :param securitytype: the security type the universe produces
        :param name: A unique name for this universe
        :param resolution: the expected resolution of the universe data
        :param market: the market for selected symbols
        :param universe_settings: the subscription settings to use for newly created subscriptions
        :param selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe(self, data_type: typing.Type, security_type: typing.Optional[QuantConnect.SecurityType] = None, name: str = None, resolution: typing.Optional[QuantConnect.Resolution] = None, market: str = None, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, py_selector: typing.Any = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe and adds it to the algorithm
        
        :param data_type: The data type
        :param security_type: The security type the universe produces
        :param name: A unique name for this universe
        :param resolution: The expected resolution of the universe data
        :param market: The market for selected symbols
        :param universe_settings: The subscription settings to use for newly created subscriptions
        :param py_selector: Function delegate that performs selection on the universe data
        """
        ...

    @overload
    def add_universe_options(self, underlying_symbol: typing.Union[QuantConnect.Symbol, str], option_filter: typing.Callable[[QuantConnect.Securities.OptionFilterUniverse], QuantConnect.Securities.OptionFilterUniverse]) -> None:
        """
        Adds a new universe that creates options of the security by monitoring any changes in the Universe the provided security is in.
        Additionally, a filter can be applied to the options generated when the universe of the security changes.
        
        :param underlying_symbol: Underlying Symbol to add as an option. For Futures, the option chain constructed will be per-contract, as long as a canonical Symbol is provided.
        :param option_filter: User-defined filter used to select the options we want out of the option chain provided.
        """
        ...

    @overload
    def add_universe_options(self, universe: QuantConnect.Data.UniverseSelection.Universe, option_filter: typing.Callable[[QuantConnect.Securities.OptionFilterUniverse], QuantConnect.Securities.OptionFilterUniverse]) -> None:
        """
        Creates a new universe selection model and adds it to the algorithm. This universe selection model will chain to the security
        changes of a given Universe selection output and create a new OptionChainUniverse for each of them
        
        :param universe: The universe we want to chain an option universe selection model too
        :param option_filter: The option filter universe to use
        """
        ...

    def add_universe_selection(self, universe_selection: QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel) -> None:
        """
        Adds a new universe selection model
        
        :param universe_selection: Model defining universes for the algorithm to add
        """
        ...

    def adosc(self, symbol: typing.Union[QuantConnect.Symbol, str], fast_period: int, slow_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.AccumulationDistributionOscillator:
        """
        Creates a new AccumulationDistributionOscillator indicator.
        
        :param symbol: The symbol whose ADOSC we want
        :param fast_period: The fast moving average period
        :param slow_period: The slow moving average period
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The AccumulationDistributionOscillator indicator for the requested symbol over the specified period.
        """
        ...

    def adr(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.AdvanceDeclineRatio:
        """
        Creates a new Advance/Decline Ratio indicator
        
        :param symbols: The symbols whose A/D Ratio we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Advance/Decline Ratio indicator for the requested symbol over the specified period.
        """
        ...

    def advr(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.AdvanceDeclineVolumeRatio:
        """
        Creates a new Advance/Decline Volume Ratio indicator
        
        :param symbols: The symbol whose A/D Volume Rate we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Advance/Decline Volume Ratio indicator for the requested symbol over the specified period.
        """
        ...

    def adx(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.AverageDirectionalIndex:
        """
        Creates a new Average Directional Index indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose Average Directional Index we seek
        :param period: The period over which to compute the Average Directional Index
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Average Directional Index indicator for the requested symbol.
        """
        ...

    def adxr(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.AverageDirectionalMovementIndexRating:
        """
        Creates a new AverageDirectionalMovementIndexRating indicator.
        
        :param symbol: The symbol whose ADXR we want
        :param period: The period over which to compute the ADXR
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The AverageDirectionalMovementIndexRating indicator for the requested symbol over the specified period.
        """
        ...

    def alma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, sigma: int = 6, offset: float = 0.85, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.ArnaudLegouxMovingAverage:
        """
        Creates a new ArnaudLegouxMovingAverage indicator.
        
        :param symbol: The symbol whose ALMA we want
        :param period: int - the number of periods to calculate the ALMA
        :param sigma: int - this parameter is responsible for the shape of the curve coefficients.
        :param offset: decimal - This parameter allows regulating the smoothness and high sensitivity of the Moving Average. The range for this parameter is [0, 1].
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The ArnaudLegouxMovingAverage indicator for the requested symbol over the specified period.
        """
        ...

    def ao(self, symbol: typing.Union[QuantConnect.Symbol, str], fast_period: int, slow_period: int, type: QuantConnect.Indicators.MovingAverageType, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.AwesomeOscillator:
        """
        Creates a new Awesome Oscillator from the specified periods.
        
        :param symbol: The symbol whose Awesome Oscillator we seek
        :param fast_period: The period of the fast moving average associated with the AO
        :param slow_period: The period of the slow moving average associated with the AO
        :param type: The type of moving average used when computing the fast and slow term. Defaults to simple moving average.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        """
        ...

    def apo(self, symbol: typing.Union[QuantConnect.Symbol, str], fast_period: int, slow_period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.AbsolutePriceOscillator:
        """
        Creates a new AbsolutePriceOscillator indicator.
        
        :param symbol: The symbol whose APO we want
        :param fast_period: The fast moving average period
        :param slow_period: The slow moving average period
        :param moving_average_type: The type of moving average to use
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The AbsolutePriceOscillator indicator for the requested symbol over the specified period.
        """
        ...

    def aps(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int = 3, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.AugenPriceSpike:
        """
        Creates an AugenPriceSpike indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose APS we want
        :param period: The period of the APS
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The AugenPriceSpike indicator for the given parameters.
        """
        ...

    def ar(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.AverageRange:
        """
        Creates a new Average Range (AR) indicator.
        
        :param symbol: The symbol whose Average Range we want to calculate
        :param period: The period over which to compute the Average Range
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator. If null, defaults to the Value property of BaseData (x => x.Value).
        :returns: The Average Range indicator for the requested symbol over the specified period.
        """
        ...

    def arima(self, symbol: typing.Union[QuantConnect.Symbol, str], ar_order: int, diff_order: int, ma_order: int, period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.AutoRegressiveIntegratedMovingAverage:
        """
        Creates a new ARIMA indicator.
        
        :param symbol: The symbol whose ARIMA indicator we want
        :param ar_order: AR order (p) -- defines the number of past values to consider in the AR component of the model.
        :param diff_order: Difference order (d) -- defines how many times to difference the model before fitting parameters.
        :param ma_order: MA order (q) -- defines the number of past values to consider in the MA component of the model.
        :param period: Size of the rolling series to fit onto
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The ARIMA indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def aroon(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.AroonOscillator:
        """
        Creates a new AroonOscillator indicator which will compute the AroonUp and AroonDown (as well as the delta)
        
        :param symbol: The symbol whose Aroon we seek
        :param period: The look back period for computing number of periods since maximum and minimum
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: An AroonOscillator configured with the specified periods.
        """
        ...

    @overload
    def aroon(self, symbol: typing.Union[QuantConnect.Symbol, str], up_period: int, down_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.AroonOscillator:
        """
        Creates a new AroonOscillator indicator which will compute the AroonUp and AroonDown (as well as the delta)
        
        :param symbol: The symbol whose Aroon we seek
        :param up_period: The look back period for computing number of periods since maximum
        :param down_period: The look back period for computing number of periods since minimum
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: An AroonOscillator configured with the specified periods.
        """
        ...

    def asi(self, symbol: typing.Union[QuantConnect.Symbol, str], limit_move: float, resolution: typing.Optional[QuantConnect.Resolution] = ..., selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.WilderAccumulativeSwingIndex:
        """
        Creates a Wilder Accumulative Swing Index (ASI) indicator for the symbol.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose ASI we want
        :param limit_move: The maximum daily change in price for the ASI
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The WilderAccumulativeSwingIndex for the given parameters.
        """
        ...

    def atr(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.AverageTrueRange:
        """
        Creates a new AverageTrueRange indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose ATR we want
        :param period: The smoothing period used to smooth the computed TrueRange values
        :param type: The type of smoothing to use
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new AverageTrueRange indicator with the specified smoothing type and period.
        """
        ...

    def b(self, target: typing.Union[QuantConnect.Symbol, str], reference: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.Beta:
        """
        Creates a Beta indicator for the given target symbol in relation with the reference used.
        The indicator will be automatically updated on the given resolution.
        
        :param target: The target symbol whose Beta value we want
        :param reference: The reference symbol to compare with the target symbol
        :param period: The period of the Beta indicator
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Beta indicator for the given parameters.
        """
        ...

    def bb(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, k: float, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.BollingerBands:
        """
        Creates a new BollingerBands indicator which will compute the MiddleBand, UpperBand, LowerBand, and StandardDeviation
        
        :param symbol: The symbol whose BollingerBands we seek
        :param period: The period of the standard deviation and moving average (middle band)
        :param k: The number of standard deviations specifying the distance between the middle band and upper or lower bands
        :param moving_average_type: The type of moving average to be used
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: A BollingerBands configured with the specified period.
        """
        ...

    def bop(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.BalanceOfPower:
        """
        Creates a new Balance Of Power indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose Balance Of Power we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Balance Of Power indicator for the requested symbol.
        """
        ...

    @overload
    def buy(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int) -> QuantConnect.Orders.OrderTicket:
        """
        Buy Stock (Alias of Order)
        
        :param symbol: string Symbol of the asset to trade
        :param quantity: int Quantity of the asset to trade
        :returns: The order ticket instance.
        """
        ...

    @overload
    def buy(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Buy Stock (Alias of Order)
        
        :param symbol: string Symbol of the asset to trade
        :param quantity: double Quantity of the asset to trade
        :returns: The order ticket instance.
        """
        ...

    @overload
    def buy(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Buy Stock (Alias of Order)
        
        :param symbol: string Symbol of the asset to trade
        :param quantity: decimal Quantity of the asset to trade
        :returns: The order ticket instance.
        """
        ...

    @overload
    def buy(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Buy Stock (Alias of Order)
        
        :param symbol: string Symbol of the asset to trade
        :param quantity: float Quantity of the asset to trade
        :returns: The order ticket instance.
        """
        ...

    @overload
    def buy(self, strategy: QuantConnect.Securities.Option.OptionStrategy, quantity: int, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Buy Option Strategy (Alias of Order)
        
        :param strategy: Specification of the strategy to trade
        :param quantity: Quantity of the strategy to trade
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: Sequence of order tickets.
        """
        ...

    def c(self, target: typing.Union[QuantConnect.Symbol, str], reference: typing.Union[QuantConnect.Symbol, str], period: int, correlation_type: QuantConnect.Indicators.CorrelationType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.Correlation:
        """
        Creates a Correlation indicator for the given target symbol in relation with the reference used.
        The indicator will be automatically updated on the given resolution.
        
        :param target: The target symbol of this indicator
        :param reference: The reference symbol of this indicator
        :param period: The period of this indicator
        :param correlation_type: Correlation type
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Correlation indicator for the given parameters.
        """
        ...

    @overload
    def calculate_order_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str], target: float) -> float:
        """
        Calculate the order quantity to achieve target-percent holdings.
        
        :param symbol: Security object we're asking for
        :param target: Target percentage holdings
        :returns: Order quantity to achieve this percentage.
        """
        ...

    @overload
    def calculate_order_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str], target: float) -> float:
        """
        Calculate the order quantity to achieve target-percent holdings.
        
        :param symbol: Security object we're asking for
        :param target: Target percentage holdings, this is an unleveraged value, so if you have 2x leverage and request 100% holdings, it will utilize half of the available margin
        :returns: Order quantity to achieve this percentage.
        """
        ...

    def cc(self, symbol: typing.Union[QuantConnect.Symbol, str], short_roc_period: int = 11, long_roc_period: int = 14, lwma_period: int = 10, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.CoppockCurve:
        """
        Initializes a new instance of the CoppockCurve indicator
        
        :param symbol: The symbol whose Coppock Curve we want
        :param short_roc_period: The period for the short ROC
        :param long_roc_period: The period for the long ROC
        :param lwma_period: The period for the LWMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Coppock Curve indicator for the requested symbol over the specified period.
        """
        ...

    def cci(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CommodityChannelIndex:
        """
        Creates a new CommodityChannelIndex indicator. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose CCI we want
        :param period: The period over which to compute the CCI
        :param moving_average_type: The type of moving average to use in computing the typical price average
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The CommodityChannelIndex indicator for the requested symbol over the specified period.
        """
        ...

    def chop(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.ChoppinessIndex:
        """
        Creates a new ChoppinessIndex indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose CHOP we want
        :param period: The input window period used to calculate max high and min low
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new ChoppinessIndex indicator with the window period.
        """
        ...

    @overload
    def cik(self, cik: int, trading_date: typing.Optional[datetime.datetime] = None) -> typing.List[QuantConnect.Symbol]:
        """
        Converts a CIK identifier into Symbol array
        
        :param cik: The CIK identifier of an asset
        :param trading_date: The date that the stock being looked up is/was traded at. The date is used to create a Symbol with the ticker set to the ticker the asset traded under on the trading date.
        :returns: Symbols corresponding to the CIK. If no Symbol with a matching CIK was found, returns empty array.
        """
        ...

    @overload
    def cik(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> typing.Optional[int]:
        """
        Converts a Symbol into a CIK identifier
        
        :param symbol: The Symbol
        :returns: CIK corresponding to the Symbol. If no matching CIK is found, returns null.
        """
        ...

    def cks(self, symbol: typing.Union[QuantConnect.Symbol, str], atr_period: int, atr_mult: float, period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.ChandeKrollStop:
        """
        Creates a new Chande Kroll Stop indicator which will compute the short and lower stop.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose Chande Kroll Stop we seek.
        :param atr_period: The period over which to compute the average true range.
        :param atr_mult: The ATR multiplier to be used to compute stops distance.
        :param period: The period over which to compute the max of high stop and min of low stop.
        :param moving_average_type: The type of smoothing used to smooth the true range values
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Chande Kroll Stop indicator for the requested symbol.
        """
        ...

    def cmf(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.ChaikinMoneyFlow:
        """
        Creates a new ChaikinMoneyFlow indicator.
        
        :param symbol: The symbol whose CMF we want
        :param period: The period over which to compute the CMF
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The ChaikinMoneyFlow indicator for the requested symbol over the specified period.
        """
        ...

    def cmo(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.ChandeMomentumOscillator:
        """
        Creates a new ChandeMomentumOscillator indicator.
        
        :param symbol: The symbol whose CMO we want
        :param period: The period over which to compute the CMO
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The ChandeMomentumOscillator indicator for the requested symbol over the specified period.
        """
        ...

    def combo_leg_limit_order(self, legs: System.Collections.Generic.List[QuantConnect.Orders.Leg], quantity: int, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Issue a combo leg limit order/trade for multiple assets, each having its own limit price.
        
        :param legs: The list of legs the order consists of
        :param quantity: The total quantity for the order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: Sequence of order tickets, one for each leg.
        """
        ...

    def combo_limit_order(self, legs: System.Collections.Generic.List[QuantConnect.Orders.Leg], quantity: int, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Issue a combo limit order/trade for multiple assets.
        A single limit price is defined for the combo order and will fill only if the sum of the assets price compares properly to the limit price, depending on the direction.
        
        :param legs: The list of legs the order consists of
        :param quantity: The total quantity for the order
        :param limit_price: The compound limit price to use for a ComboLimit order. This limit price will compared to the sum of the assets price in order to fill the order.
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: Sequence of order tickets, one for each leg.
        """
        ...

    def combo_market_order(self, legs: System.Collections.Generic.List[QuantConnect.Orders.Leg], quantity: int, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Issue a combo market order/trade for multiple assets
        
        :param legs: The list of legs the order consists of
        :param quantity: The total quantity for the order
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: Sequence of order tickets, one for each leg.
        """
        ...

    @overload
    def composite_figi(self, composite_figi: str, trading_date: typing.Optional[datetime.datetime] = None) -> QuantConnect.Symbol:
        """
        Converts a composite FIGI identifier into a Symbol
        
        :param composite_figi: The composite Financial Instrument Global Identifier (FIGI) of an asset
        :param trading_date: The date that the stock being looked up is/was traded at. The date is used to create a Symbol with the ticker set to the ticker the asset traded under on the trading date.
        :returns: Symbol corresponding to the composite FIGI. If no Symbol with a matching composite FIGI was found, returns null.
        """
        ...

    @overload
    def composite_figi(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Symbol into a composite FIGI identifier
        
        :param symbol: The Symbol
        :returns: Composite FIGI corresponding to the Symbol. If no matching composite FIGI is found, returns null.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], period: QuantConnect.Resolution, handler: typing.Callable[[QuantConnect.Data.Market.TradeBar], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol
        
        :param symbol: The symbol who's data is to be consolidated
        :param period: The consolidation period
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], period: datetime.timedelta, handler: typing.Callable[[QuantConnect.Data.Market.TradeBar], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol
        
        :param symbol: The symbol who's data is to be consolidated
        :param period: The consolidation period
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], period: QuantConnect.Resolution, handler: typing.Callable[[QuantConnect.Data.Market.QuoteBar], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol
        
        :param symbol: The symbol who's data is to be consolidated
        :param period: The consolidation period
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], period: datetime.timedelta, handler: typing.Callable[[QuantConnect.Data.Market.QuoteBar], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol
        
        :param symbol: The symbol who's data is to be consolidated
        :param period: The consolidation period
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], period: datetime.timedelta, handler: typing.Callable[[QuantConnect_Algorithm_QCAlgorithm_Consolidate_T], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol and tick type.
        The handler and tick type must match.
        
        :param symbol: The symbol who's data is to be consolidated
        :param period: The consolidation period
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], period: QuantConnect.Resolution, tick_type: typing.Optional[QuantConnect.TickType], handler: typing.Callable[[QuantConnect_Algorithm_QCAlgorithm_Consolidate_T], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol and tick type.
        The handler and tick type must match.
        
        :param symbol: The symbol who's data is to be consolidated
        :param period: The consolidation period
        :param tick_type: The tick type of subscription used as data source for consolidator. Specify null to use first subscription found.
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], period: datetime.timedelta, tick_type: typing.Optional[QuantConnect.TickType], handler: typing.Callable[[QuantConnect_Algorithm_QCAlgorithm_Consolidate_T], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol and tick type.
        The handler and tick type must match.
        
        :param symbol: The symbol who's data is to be consolidated
        :param period: The consolidation period
        :param tick_type: The tick type of subscription used as data source for consolidator. Specify null to use first subscription found.
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], calendar: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo], handler: typing.Callable[[QuantConnect.Data.Market.QuoteBar], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol
        
        :param symbol: The symbol who's data is to be consolidated
        :param calendar: The consolidation calendar
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], calendar: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo], handler: typing.Callable[[QuantConnect.Data.Market.TradeBar], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol
        
        :param symbol: The symbol who's data is to be consolidated
        :param calendar: The consolidation calendar
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], calendar: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo], handler: typing.Callable[[QuantConnect_Algorithm_QCAlgorithm_Consolidate_T], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol and tick type.
        The handler and tick type must match.
        
        :param symbol: The symbol who's data is to be consolidated
        :param calendar: The consolidation calendar
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @overload
    def consolidate(self, symbol: typing.Union[QuantConnect.Symbol, str], calendar: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo], tick_type: typing.Optional[QuantConnect.TickType], handler: typing.Callable[[QuantConnect_Algorithm_QCAlgorithm_Consolidate_T], None]) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Registers the  to receive consolidated data for the specified symbol and tick type.
        The handler and tick type must match.
        
        :param symbol: The symbol who's data is to be consolidated
        :param calendar: The consolidation calendar
        :param tick_type: The tick type of subscription used as data source for consolidator. Specify null to use first subscription found.
        :param handler: Data handler receives new consolidated data when generated
        :returns: A new consolidator matching the requested parameters with the handler already registered.
        """
        ...

    @staticmethod
    def create_consolidator(period: datetime.timedelta, consolidator_input_type: typing.Type, tick_type: typing.Optional[QuantConnect.TickType] = None) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Creates a new consolidator for the specified period, generating the requested output type.
        
        :param period: The consolidation period
        :param consolidator_input_type: The desired input type of the consolidator, such as TradeBar or QuoteBar
        :param tick_type: Trade or Quote. Optional, defaults to trade
        :returns: A new consolidator matching the requested parameters.
        """
        ...

    @overload
    def create_date_range_history_requests(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], start_algo_tz: typing.Union[datetime.datetime, datetime.date], end_algo_tz: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Helper method to create history requests from a date range
        
        This method is protected.
        """
        ...

    @overload
    def create_date_range_history_requests(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], requested_type: typing.Type, start_algo_tz: typing.Union[datetime.datetime, datetime.date], end_algo_tz: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Helper method to create history requests from a date range with custom data type
        
        This method is protected.
        """
        ...

    @overload
    def create_indicator_name(self, symbol: typing.Union[QuantConnect.Symbol, str], type: System.FormattableString, resolution: typing.Optional[QuantConnect.Resolution]) -> str:
        """
        Creates a new name for an indicator created with the convenience functions (SMA, EMA, ect...)
        
        :param symbol: The symbol this indicator is registered to
        :param type: The indicator type, for example, 'SMA(5)'
        :param resolution: The resolution requested
        :returns: A unique for the given parameters.
        """
        ...

    @overload
    def create_indicator_name(self, symbol: typing.Union[QuantConnect.Symbol, str], type: str, resolution: typing.Optional[QuantConnect.Resolution]) -> str:
        """
        Creates a new name for an indicator created with the convenience functions (SMA, EMA, ect...)
        
        :param symbol: The symbol this indicator is registered to
        :param type: The indicator type, for example, 'SMA(5)'
        :param resolution: The resolution requested
        :returns: A unique for the given parameters.
        """
        ...

    def crsi(self, symbol: typing.Union[QuantConnect.Symbol, str], rsi_period: int, rsi_period_streak: int, look_back_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.ConnorsRelativeStrengthIndex:
        """
        Creates a new Connors Relative Strength Index (CRSI) indicator, which combines the traditional Relative Strength Index (RSI),
        Streak RSI (SRSI), and Percent Rank to provide a more robust measure of market strength.
        This indicator oscillates based on momentum, streak behavior, and price change over the specified periods.
        
        :param symbol: The symbol whose CRSI is to be calculated.
        :param rsi_period: The period for the traditional RSI calculation.
        :param rsi_periodStreak: The period for the Streak RSI calculation (SRSI).
        :param look_back_period: The look-back period for calculating the Percent Rank.
        :param resolution: The resolution of the data (optional).
        :param selector: Function to select a value from the BaseData to input into the indicator. Defaults to using the 'Value' property of BaseData if null.
        :returns: The Connors Relative Strength Index (CRSI) for the specified symbol and periods.
        """
        ...

    @overload
    def cusip(self, cusip: str, trading_date: typing.Optional[datetime.datetime] = None) -> QuantConnect.Symbol:
        """
        Converts a CUSIP identifier into a Symbol
        
        :param cusip: The CUSIP number of an asset
        :param trading_date: The date that the stock being looked up is/was traded at. The date is used to create a Symbol with the ticker set to the ticker the asset traded under on the trading date.
        :returns: Symbol corresponding to the CUSIP. If no Symbol with a matching CUSIP was found, returns null.
        """
        ...

    @overload
    def cusip(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Symbol into a CUSIP identifier
        
        :param symbol: The Symbol
        :returns: CUSIP corresponding to the Symbol. If no matching CUSIP is found, returns null.
        """
        ...

    def d(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Delta:
        """
        Creates a new Delta indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Delta
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Delta indicator for the specified symbol.
        """
        ...

    @overload
    def dch(self, symbol: typing.Union[QuantConnect.Symbol, str], upper_period: int, lower_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.DonchianChannel:
        """
        Creates a new Donchian Channel indicator which will compute the Upper Band and Lower Band.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose Donchian Channel we seek.
        :param upper_period: The period over which to compute the upper Donchian Channel.
        :param lower_period: The period over which to compute the lower Donchian Channel.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Donchian Channel indicator for the requested symbol.
        """
        ...

    @overload
    def dch(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.DonchianChannel:
        """
        Overload shorthand to create a new symmetric Donchian Channel indicator which
        has the upper and lower channels set to the same period length.
        
        :param symbol: The symbol whose Donchian Channel we seek.
        :param period: The period over which to compute the Donchian Channel.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Donchian Channel indicator for the requested symbol.
        """
        ...

    @overload
    def debug(self, message: typing.Any) -> None:
        """
        Send a debug message to the web console:
        
        :param message: Message to send to debug console
        """
        ...

    @overload
    def debug(self, message: str) -> None:
        """
        Send a debug message to the web console:
        
        :param message: Message to send to debug console
        """
        ...

    @overload
    def debug(self, message: int) -> None:
        """
        Send a debug message to the web console:
        
        :param message: Message to send to debug console
        """
        ...

    @overload
    def debug(self, message: float) -> None:
        """
        Send a debug message to the web console:
        
        :param message: Message to send to debug console
        """
        ...

    @overload
    def debug(self, message: float) -> None:
        """
        Send a debug message to the web console:
        
        :param message: Message to send to debug console
        """
        ...

    def dem(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, type: QuantConnect.Indicators.MovingAverageType, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.DeMarkerIndicator:
        """
        Creates a new DeMarker Indicator (DEM), an oscillator-type indicator measuring changes in terms of an asset's
        High and Low tradebar values.
        
        :param symbol: The symbol whose DEM we seek.
        :param period: The period of the moving average implemented
        :param type: Specifies the type of moving average to be used
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The DeMarker indicator for the requested symbol.
        """
        ...

    def dema(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.DoubleExponentialMovingAverage:
        """
        Creates a new DoubleExponentialMovingAverage indicator.
        
        :param symbol: The symbol whose DEMA we want
        :param period: The period over which to compute the DEMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The DoubleExponentialMovingAverage indicator for the requested symbol over the specified period.
        """
        ...

    def deregister_indicator(self, indicator: QuantConnect.Indicators.IndicatorBase) -> None:
        """
        Will deregister an indicator and it's associated consolidator instance so they stop receiving data updates
        
        :param indicator: The indicator instance to deregister
        """
        ...

    def do(self, symbol: typing.Union[QuantConnect.Symbol, str], rsi_period: int, smoothing_rsi_period: int, double_smoothing_rsi_period: int, signal_line_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.DerivativeOscillator:
        """
        Creates a new DerivativeOscillator indicator.
        
        :param symbol: The symbol whose DO we want
        :param rsi_period: The period over which to compute the RSI
        :param smoothing_rsi_period: The period over which to compute the smoothing RSI
        :param double_smoothing_rsi_period: The period over which to compute the double smoothing RSI
        :param signal_line_period: The period over which to compute the signal line
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The DerivativeOscillator indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def download(self, address: str) -> str:
        """
        Downloads the requested resource as a string.
        The resource to download is specified as a string containing the URI.
        
        :param address: A string containing the URI to download
        :returns: The requested resource as a string.
        """
        ...

    @overload
    def download(self, address: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]]) -> str:
        """
        Downloads the requested resource as a string.
        The resource to download is specified as a string containing the URI.
        
        :param address: A string containing the URI to download
        :param headers: Defines header values to add to the request
        :returns: The requested resource as a string.
        """
        ...

    @overload
    def download(self, address: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]], user_name: str, password: str) -> str:
        """
        Downloads the requested resource as a string.
        The resource to download is specified as a string containing the URI.
        
        :param address: A string containing the URI to download
        :param headers: Defines header values to add to the request
        :param user_name: The user name associated with the credentials
        :param password: The password for the user name associated with the credentials
        :returns: The requested resource as a string.
        """
        ...

    def dpo(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.DetrendedPriceOscillator:
        """
        Creates a new DetrendedPriceOscillator indicator.
        
        :param symbol: The symbol whose DPO we want
        :param period: The period over which to compute the DPO
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: A new registered DetrendedPriceOscillator indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def ema(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.ExponentialMovingAverage:
        """
        Creates an ExponentialMovingAverage indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose EMA we want
        :param period: The period of the EMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The ExponentialMovingAverage for the given parameters.
        """
        ...

    @overload
    def ema(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, smoothing_factor: float, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.ExponentialMovingAverage:
        """
        Creates an ExponentialMovingAverage indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose EMA we want
        :param period: The period of the EMA
        :param smoothing_factor: The percentage of data from the previous value to be carried into the next value
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The ExponentialMovingAverage for the given parameters.
        """
        ...

    @overload
    def emit_insights(self, *insights: QuantConnect.Algorithm.Framework.Alphas.Insight) -> None:
        """
        Manually emit insights from an algorithm.
        This is typically invoked before calls to submit orders in algorithms written against
        QCAlgorithm that have been ported into the algorithm framework.
        
        :param insights: The array of insights to be emitted
        """
        ...

    @overload
    def emit_insights(self, insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> None:
        """
        Manually emit insights from an algorithm.
        This is typically invoked before calls to submit orders in algorithms written against
        QCAlgorithm that have been ported into the algorithm framework.
        
        :param insight: The insight to be emitted
        """
        ...

    def emv(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int = 1, scale: int = 10000, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.EaseOfMovementValue:
        """
        Creates an EaseOfMovementValue indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose EMV we want
        :param period: The period of the EMV
        :param scale: The length of the outputed value
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The EaseOfMovementValue indicator for the given parameters.
        """
        ...

    @overload
    def error(self, message: typing.Any) -> None:
        """
        Send a string error message to the Console.
        
        :param message: Message to display in errors grid
        """
        ...

    @overload
    def error(self, message: str) -> None:
        """
        Send a string error message to the Console.
        
        :param message: Message to display in errors grid
        """
        ...

    @overload
    def error(self, message: int) -> None:
        """
        Send a int error message to the Console.
        
        :param message: Message to display in errors grid
        """
        ...

    @overload
    def error(self, message: float) -> None:
        """
        Send a double error message to the Console.
        
        :param message: Message to display in errors grid
        """
        ...

    @overload
    def error(self, message: float) -> None:
        """
        Send a decimal error message to the Console.
        
        :param message: Message to display in errors grid
        """
        ...

    @overload
    def error(self, error: System.Exception) -> None:
        """
        Send a string error message to the Console.
        
        :param error: Exception object captured from a try catch loop
        """
        ...

    def exercise_option(self, option_symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send an exercise order to the transaction handler
        
        :param option_symbol: String symbol for the option position
        :param quantity: Quantity of options contracts
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    def fi(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.ForceIndex:
        """
        Creates a new ForceIndex indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose ForceIndex we want
        :param period: The smoothing period used to smooth the computed ForceIndex values
        :param type: The type of smoothing to use
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new ForceIndex indicator with the specified smoothing type and period.
        """
        ...

    @overload
    def filtered_identity(self, symbol: typing.Union[QuantConnect.Symbol, str], selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None, filter: typing.Callable[[QuantConnect.Data.IBaseData], bool] = None, field_name: str = None) -> QuantConnect.Indicators.FilteredIdentity:
        """
        Creates a new FilteredIdentity indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The symbol whose values we want as an indicator
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :param filter: Filters the IBaseData send into the indicator, if null defaults to true (x => true) which means no filter
        :param field_name: The name of the field being selected
        :returns: A new FilteredIdentity indicator for the specified symbol and selector.
        """
        ...

    @overload
    def filtered_identity(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None, filter: typing.Callable[[QuantConnect.Data.IBaseData], bool] = None, field_name: str = None) -> QuantConnect.Indicators.FilteredIdentity:
        """
        Creates a new FilteredIdentity indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The symbol whose values we want as an indicator
        :param resolution: The desired resolution of the data
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :param filter: Filters the IBaseData send into the indicator, if null defaults to true (x => true) which means no filter
        :param field_name: The name of the field being selected
        :returns: A new FilteredIdentity indicator for the specified symbol and selector.
        """
        ...

    @overload
    def filtered_identity(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: datetime.timedelta, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None, filter: typing.Callable[[QuantConnect.Data.IBaseData], bool] = None, field_name: str = None) -> QuantConnect.Indicators.FilteredIdentity:
        """
        Creates a new FilteredIdentity indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The symbol whose values we want as an indicator
        :param resolution: The desired resolution of the data
        :param selector: Selects a value from the BaseData, if null defaults to the .Value property (x => x.Value)
        :param filter: Filters the IBaseData send into the indicator, if null defaults to true (x => true) which means no filter
        :param field_name: The name of the field being selected
        :returns: A new FilteredIdentity indicator for the specified symbol and selector.
        """
        ...

    def fish(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.FisherTransform:
        """
        Creates an FisherTransform indicator for the symbol.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose FisherTransform we want
        :param period: The period of the FisherTransform
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The FisherTransform for the given parameters.
        """
        ...

    def frama(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, long_period: int = 198, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.FractalAdaptiveMovingAverage:
        """
        Creates an FractalAdaptiveMovingAverage (FRAMA) indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose FRAMA we want
        :param period: The period of the FRAMA
        :param long_period: The long period of the FRAMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The FRAMA for the given parameters.
        """
        ...

    def framework_post_initialize(self) -> None:
        """
        Called by setup handlers after Initialize and allows the algorithm a chance to organize
        the data gather in the Initialize method
        """
        ...

    @overload
    def fundamentals(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Fundamental.Fundamental:
        """
        Get the fundamental data for the requested symbol at the current time
        
        :param symbol: The Symbol
        :returns: The fundamental data for the Symbol.
        """
        ...

    @overload
    def fundamentals(self, symbols: System.Collections.Generic.List[QuantConnect.Symbol]) -> System.Collections.Generic.List[QuantConnect.Data.Fundamental.Fundamental]:
        """
        Get the fundamental data for the requested symbols at the current time
        
        :param symbols: The Symbol
        :returns: The fundamental data for the symbols.
        """
        ...

    def g(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Gamma:
        """
        Creates a new Gamma indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Gamma
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Gamma indicator for the specified symbol.
        """
        ...

    def get_chart_updates(self, clear_chart_data: bool = False) -> System.Collections.Generic.IEnumerable[QuantConnect.Chart]:
        """
        Get the chart updates by fetch the recent points added and return for dynamic Charting.
        
        :returns: List of chart updates since the last request.
        """
        ...

    def get_data_typed_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect_Algorithm_QCAlgorithm_GetDataTypedHistory_T]]:
        """
        Centralized logic to get data typed history for a given list of requests.
        
        This method is protected.
        """
        ...

    def get_last_known_price(self, security: QuantConnect.Securities.Security) -> QuantConnect.Data.BaseData:
        """
        Get the last known price using the history provider.
        Useful for seeding securities with the correct price
        
        This method is obsolete please use 'GetLastKnownPrices' which will return the last data point" +
                    " for each type associated with the requested security
        
        :param security: Security object for which to retrieve historical data
        :returns: A single BaseData object with the last known price.
        """
        warnings.warn("This method is obsolete please use 'GetLastKnownPrices' which will return the last data point" +
                    " for each type associated with the requested security", DeprecationWarning)

    @overload
    def get_last_known_prices(self, security: QuantConnect.Securities.Security) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Yields data to warmup a security for all it's subscribed data types
        
        :param security: Security object for which to retrieve historical data
        :returns: Securities historical data.
        """
        ...

    @overload
    def get_last_known_prices(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Yields data to warmup a security for all it's subscribed data types
        
        :param symbol: The symbol we want to get seed data for
        :returns: Securities historical data.
        """
        ...

    def get_locked(self) -> bool:
        """Gets whether or not this algorithm has been locked and fully initialized"""
        ...

    @overload
    def get_parameter(self, name: str, default_value: str = None) -> str:
        """
        Gets the parameter with the specified name. If a parameter with the specified name does not exist,
        the given default value is returned if any, else null
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    @overload
    def get_parameter(self, name: str, default_value: int) -> int:
        """
        Gets the parameter with the specified name parsed as an integer. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    @overload
    def get_parameter(self, name: str, default_value: float) -> float:
        """
        Gets the parameter with the specified name parsed as a double. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    @overload
    def get_parameter(self, name: str, default_value: float) -> float:
        """
        Gets the parameter with the specified name parsed as a decimal. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param default_value: The default value to return
        :returns: The value of the specified parameter, or default_value if not found or null if there's no default value.
        """
        ...

    def get_parameters(self) -> System.Collections.Generic.IReadOnlyDictionary[str, str]:
        """Gets a read-only dictionary with all current parameters"""
        ...

    def he(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, max_lag: int = 20, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.HurstExponent:
        """
        Creates a new Hurst Exponent indicator for the specified symbol.
        The Hurst Exponent measures the long-term memory or self-similarity in a time series.
        The default max_lag value of 20 is chosen for reliable and accurate results, but using a higher lag may reduce precision.
        
        :param symbol: The symbol for which the Hurst Exponent is calculated.
        :param period: The number of data points used to calculate the indicator at each step.
        :param max_lag: The maximum time lag used to compute the tau values for the Hurst Exponent calculation.
        :param resolution: The resolution
        :param selector: Function to select a value from the BaseData to input into the indicator. Defaults to using the 'Value' property of BaseData if null.
        :returns: The Hurst Exponent indicator for the specified symbol.
        """
        ...

    def heikin_ashi(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.HeikinAshi:
        """
        Creates a new Heikin-Ashi indicator.
        
        :param symbol: The symbol whose Heikin-Ashi we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Heikin-Ashi indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def history(self, span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Get the history for all configured securities over the requested span.
        This will use the resolution and other subscription settings for each security.
        The symbols must exist in the Securities collection.
        
        :param span: The span over which to request data. This is a calendar span, so take into consideration weekends and such
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing data over the most recent span for all configured securities.
        """
        ...

    @overload
    def history(self, periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Get the history for all configured securities over the requested span.
        This will use the resolution and other subscription settings for each security.
        The symbols must exist in the Securities collection.
        
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing data over the most recent span for all configured securities.
        """
        ...

    @overload
    def history(self, universe: QuantConnect.Data.UniverseSelection.Universe, periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Get the history for all configured securities over the requested span.
        This will use the resolution and other subscription settings for each security.
        The symbols must exist in the Securities collection.
        
        :param universe: The universe to fetch the data for
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing data over the most recent span for all configured securities.
        """
        ...

    @overload
    def history(self, universe: QuantConnect.Data.UniverseSelection.Universe, span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for all symbols of the requested type over the requested span.
        The symbol's configured values for resolution and fill forward behavior will be used
        The symbols must exist in the Securities collection.
        
        :param universe: The universe to fetch the data for
        :param span: The span over which to request data. This is a calendar span, so take into consideration weekends and such
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, universe: QuantConnect.Data.UniverseSelection.Universe, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols between the specified dates. The symbols must exist in the Securities collection.
        
        :param universe: The universe to fetch the data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for all symbols of the requested type over the requested span.
        The symbol's configured values for resolution and fill forward behavior will be used
        The symbols must exist in the Securities collection.
        
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols over the requested span.
        The symbols must exist in the Securities collection.
        
        :param symbols: The symbols to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols. The exact number of bars will be returned for
        each symbol. This may result in some data start earlier/later than others due to when various
        exchanges are open. The symbols must exist in the Securities collection.
        
        :param symbols: The symbols to retrieve historical data for
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols between the specified dates. The symbols must exist in the Securities collection.
        
        :param symbols: The symbols to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbol: typing.Union[QuantConnect.Symbol, str], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbol over the request span. The symbol must exist in the Securities collection.
        
        :param symbol: The symbol to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbol: typing.Union[QuantConnect.Symbol, str], periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param symbol: The symbol to retrieve historical data for
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbol: typing.Union[QuantConnect.Symbol, str], periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param symbol: The symbol to retrieve historical data for
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbol between the specified dates. The symbol must exist in the Securities collection.
        
        :param symbol: The symbol to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbol: typing.Union[QuantConnect.Symbol, str], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbol over the request span. The symbol must exist in the Securities collection.
        
        :param symbol: The symbol to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbol over the request span. The symbol must exist in the Securities collection.
        
        :param symbol: The symbol to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols over the requested span.
        The symbol's configured values for resolution and fill forward behavior will be used
        The symbols must exist in the Securities collection.
        
        :param symbols: The symbols to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols. The exact number of bars will be returned for
        each symbol. This may result in some data start earlier/later than others due to when various
        exchanges are open. The symbols must exist in the Securities collection.
        
        :param symbols: The symbols to retrieve historical data for
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols between the specified dates. The symbols must exist in the Securities collection.
        
        :param symbols: The symbols to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :returns: An enumerable of slice containing the requested historical data.
        """
        ...

    @overload
    def history(self, request: QuantConnect.Data.HistoryRequest) -> pandas.DataFrame:
        """
        Executes the specified history request
        
        :param request: the history request to execute
        :returns: An enumerable of slice satisfying the specified history request.
        """
        ...

    @overload
    def history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]) -> pandas.DataFrame:
        """
        Executes the specified history requests
        
        :param requests: the history requests to execute
        :returns: An enumerable of slice satisfying the specified history request.
        """
        ...

    @overload
    def history(self, type: typing.Type, tickers: typing.Any, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None, flatten: bool = False) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols between the specified dates. The symbols must exist in the Securities collection.
        
        :param type: The data type of the symbols
        :param tickers: The symbols to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :param flatten: Whether to flatten the resulting data frame. e.g. for universe requests, the each row represents a day of data, and the data is stored in a list in a cell of the data frame. If flatten is true, the resulting data frame will contain one row per universe constituent, and each property of the constituent will be a column in the data frame.
        :returns: pandas.DataFrame containing the requested historical data.
        """
        ...

    @overload
    def history(self, type: typing.Type, tickers: typing.Any, periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None, flatten: bool = False) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols. The exact number of bars will be returned for
        each symbol. This may result in some data start earlier/later than others due to when various
        exchanges are open. The symbols must exist in the Securities collection.
        
        :param type: The data type of the symbols
        :param tickers: The symbols to retrieve historical data for
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :param flatten: Whether to flatten the resulting data frame. e.g. for universe requests, the each row represents a day of data, and the data is stored in a list in a cell of the data frame. If flatten is true, the resulting data frame will contain one row per universe constituent, and each property of the constituent will be a column in the data frame.
        :returns: pandas.DataFrame containing the requested historical data.
        """
        ...

    @overload
    def history(self, type: typing.Type, tickers: typing.Any, span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None, flatten: bool = False) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols over the requested span.
        The symbols must exist in the Securities collection.
        
        :param type: The data type of the symbols
        :param tickers: The symbols to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :param flatten: Whether to flatten the resulting data frame. e.g. for universe requests, the each row represents a day of data, and the data is stored in a list in a cell of the data frame. If flatten is true, the resulting data frame will contain one row per universe constituent, and each property of the constituent will be a column in the data frame.
        :returns: pandas.DataFrame containing the requested historical data.
        """
        ...

    @overload
    def history(self, type: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None, flatten: bool = False) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols between the specified dates. The symbols must exist in the Securities collection.
        
        :param type: The data type of the symbols
        :param symbol: The symbol to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :param flatten: Whether to flatten the resulting data frame. e.g. for universe requests, the each row represents a day of data, and the data is stored in a list in a cell of the data frame. If flatten is true, the resulting data frame will contain one row per universe constituent, and each property of the constituent will be a column in the data frame.
        :returns: pandas.DataFrame containing the requested historical data.
        """
        ...

    @overload
    def history(self, type: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], periods: int, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None, flatten: bool = False) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols. The exact number of bars will be returned for
        each symbol. This may result in some data start earlier/later than others due to when various
        exchanges are open. The symbols must exist in the Securities collection.
        
        :param type: The data type of the symbols
        :param symbol: The symbol to retrieve historical data for
        :param periods: The number of bars to request
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :param flatten: Whether to flatten the resulting data frame. e.g. for universe requests, the each row represents a day of data, and the data is stored in a list in a cell of the data frame. If flatten is true, the resulting data frame will contain one row per universe constituent, and each property of the constituent will be a column in the data frame.
        :returns: pandas.DataFrame containing the requested historical data.
        """
        ...

    @overload
    def history(self, type: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: typing.Optional[bool] = None, extended_market_hours: typing.Optional[bool] = None, data_mapping_mode: typing.Optional[QuantConnect.DataMappingMode] = None, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contract_depth_offset: typing.Optional[int] = None, flatten: bool = False) -> pandas.DataFrame:
        """
        Gets the historical data for the specified symbols over the requested span.
        The symbols must exist in the Securities collection.
        
        :param type: The data type of the symbols
        :param symbol: The symbol to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param fill_forward: True to fill forward missing data, false otherwise
        :param extended_market_hours: True to include extended market hours data, false otherwise
        :param data_mapping_mode: The contract mapping mode to use for the security history request
        :param data_normalization_mode: The price scaling mode to use for the securities history
        :param contract_depth_offset: The continuous contract desired offset from the current front month. For example, 0 will use the front month, 1 will use the back month contract
        :param flatten: Whether to flatten the resulting data frame. e.g. for universe requests, the each row represents a day of data, and the data is stored in a list in a cell of the data frame. If flatten is true, the resulting data frame will contain one row per universe constituent, and each property of the constituent will be a column in the data frame.
        :returns: pandas.DataFrame containing the requested historical data.
        """
        ...

    def hma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.HullMovingAverage:
        """
        Creates a new HullMovingAverage indicator. The Hull moving average is a series of nested weighted moving averages, is fast and smooth.
        
        :param symbol: The symbol whose Hull moving average we want
        :param period: The period over which to compute the Hull moving average
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    def ht(self, symbol: typing.Union[QuantConnect.Symbol, str], length: int, in_phase_multiplication_factor: float, quadrature_multiplication_factor: float, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.HilbertTransform:
        """
        Creates a new Hilbert Transform indicator
        
        :param symbol: The symbol whose Hilbert transform we want
        :param length: The length of the FIR filter used in the calculation of the Hilbert Transform. This parameter determines the number of filter coefficients in the FIR filter.
        :param in_phase_multiplication_factor: The multiplication factor used in the calculation of the in-phase component of the Hilbert Transform. This parameter adjusts the sensitivity and responsiveness of the transform to changes in the input signal.
        :param quadrature_multiplication_factor: The multiplication factor used in the calculation of the quadrature component of the Hilbert Transform. This parameter also adjusts the sensitivity and responsiveness of the transform to changes in the input signal.
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    def ibs(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.InternalBarStrength:
        """
        Creates a new InternalBarStrength indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose IBS we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new InternalBarStrength indicator.
        """
        ...

    def ichimoku(self, symbol: typing.Union[QuantConnect.Symbol, str], tenkan_period: int, kijun_period: int, senkou_a_period: int, senkou_b_period: int, senkou_a_delay_period: int, senkou_b_delay_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.IchimokuKinkoHyo:
        """
        Creates a new IchimokuKinkoHyo indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose ICHIMOKU we want
        :param tenkan_period: The period to calculate the Tenkan-sen period
        :param kijun_period: The period to calculate the Kijun-sen period
        :param senkou_a_period: The period to calculate the Tenkan-sen period
        :param senkou_b_period: The period to calculate the Tenkan-sen period
        :param senkou_a_delay_period: The period to calculate the Tenkan-sen period
        :param senkou_b_delay_period: The period to calculate the Tenkan-sen period
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new IchimokuKinkoHyo indicator with the specified periods and delays.
        """
        ...

    @overload
    def identity(self, symbol: typing.Union[QuantConnect.Symbol, str], selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, field_name: str = None) -> QuantConnect.Indicators.Identity:
        """
        Creates a new Identity indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The symbol whose values we want as an indicator
        :param selector: Selects a value from the BaseData, if null defaults to the .Value property (x => x.Value)
        :param field_name: The name of the field being selected
        :returns: A new Identity indicator for the specified symbol and selector.
        """
        ...

    @overload
    def identity(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, field_name: str = None) -> QuantConnect.Indicators.Identity:
        """
        Creates a new Identity indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The symbol whose values we want as an indicator
        :param resolution: The desired resolution of the data
        :param selector: Selects a value from the BaseData, if null defaults to the .Value property (x => x.Value)
        :param field_name: The name of the field being selected
        :returns: A new Identity indicator for the specified symbol and selector.
        """
        ...

    @overload
    def identity(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: datetime.timedelta, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, field_name: str = None) -> QuantConnect.Indicators.Identity:
        """
        Creates a new Identity indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The symbol whose values we want as an indicator
        :param resolution: The desired resolution of the data
        :param selector: Selects a value from the BaseData, if null defaults to the .Value property (x => x.Value)
        :param field_name: The name of the field being selected
        :returns: A new Identity indicator for the specified symbol and selector.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbol: The symbol to retrieve historical data for
        :param period: The number of bars to request
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of an indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an indicator for the specified symbols. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbols: The symbols to retrieve historical data for
        :param period: The number of bars to request
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of an indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T], symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T] = None) -> pandas.DataFrame:
        """
        Gets the historical data of a bar indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbol: The symbol to retrieve historical data for
        :param period: The number of bars to request
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of a bar indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T], symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T] = None) -> pandas.DataFrame:
        """
        Gets the historical data of a bar indicator for the specified symbols. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbols: The symbols to retrieve historical data for
        :param period: The number of bars to request
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of a bar indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], symbol: typing.Union[QuantConnect.Symbol, str], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbol: The symbol to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of an indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbols: The symbols to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of an indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T], symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T] = None) -> pandas.DataFrame:
        """
        Gets the historical data of a bar indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbols: The symbols to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of a bar indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T], symbol: typing.Union[QuantConnect.Symbol, str], span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T] = None) -> pandas.DataFrame:
        """
        Gets the historical data of a bar indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbol: The symbol to retrieve historical data for
        :param span: The span over which to retrieve recent historical data
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of a bar indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an indicator for the specified symbols. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbols: The symbols to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of an indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbol: The symbol to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of an indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T], symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T] = None) -> pandas.DataFrame:
        """
        Gets the historical data of a bar indicator for the specified symbol. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbol: The symbol to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of a bar indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T], symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T] = None) -> pandas.DataFrame:
        """
        Gets the historical data of a bar indicator for the specified symbols. The exact number of bars will be returned.
        The symbol must exist in the Securities collection.
        
        :param indicator: The target indicator
        :param symbols: The symbols to retrieve historical data for
        :param start: The start time in the algorithm's time zone
        :param end: The end time in the algorithm's time zone
        :param resolution: The resolution to request
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame of historical data of a bar indicator.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], history: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an indicator and convert it into pandas.DataFrame
        
        :param indicator: The target indicator
        :param history: Historical data used to calculate the indicator
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame containing the historical data of.
        """
        ...

    @overload
    def indicator_history(self, indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T], history: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_IndicatorHistory_T] = None) -> pandas.DataFrame:
        """
        Gets the historical data of an bar indicator and convert it into pandas.DataFrame
        
        :param indicator: Bar indicator
        :param history: Historical data used to calculate the indicator
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: pandas.DataFrame containing the historical data of.
        """
        ...

    def initialize(self) -> None:
        """Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized."""
        ...

    @overload
    def isin(self, isin: str, trading_date: typing.Optional[datetime.datetime] = None) -> QuantConnect.Symbol:
        """
        Converts an ISIN identifier into a Symbol
        
        :param isin: The International Securities Identification Number (ISIN) of an asset
        :param trading_date: The date that the stock being looked up is/was traded at. The date is used to create a Symbol with the ticker set to the ticker the asset traded under on the trading date.
        :returns: Symbol corresponding to the ISIN. If no Symbol with a matching ISIN was found, returns null.
        """
        ...

    @overload
    def isin(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Symbol into an ISIN identifier
        
        :param symbol: The Symbol
        :returns: ISIN corresponding to the Symbol. If no matching ISIN is found, returns null.
        """
        ...

    def is_market_open(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines if the exchange for the specified symbol is open at the current time.
        
        :param symbol: The symbol
        :returns: True if the exchange is considered open at the current time, false otherwise.
        """
        ...

    def iv(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.ImpliedVolatility:
        """
        Creates a new ImpliedVolatility indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option contract used for parity type calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new ImpliedVolatility indicator for the specified symbol.
        """
        ...

    @overload
    def kama(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.KaufmanAdaptiveMovingAverage:
        """
        Creates a new KaufmanAdaptiveMovingAverage indicator.
        
        :param symbol: The symbol whose KAMA we want
        :param period: The period of the Efficiency Ratio (ER) of KAMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The KaufmanAdaptiveMovingAverage indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def kama(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, fast_ema_period: int, slow_ema_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.KaufmanAdaptiveMovingAverage:
        """
        Creates a new KaufmanAdaptiveMovingAverage indicator.
        
        :param symbol: The symbol whose KAMA we want
        :param period: The period of the Efficiency Ratio (ER)
        :param fast_ema_period: The period of the fast EMA used to calculate the Smoothing Constant (SC)
        :param slow_ema_period: The period of the slow EMA used to calculate the Smoothing Constant (SC)
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The KaufmanAdaptiveMovingAverage indicator for the requested symbol over the specified period.
        """
        ...

    def kch(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, k: float, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.KeltnerChannels:
        """
        Creates a new Keltner Channels indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose Keltner Channel we seek
        :param period: The period over which to compute the Keltner Channels
        :param k: The number of multiples of the AverageTrueRange from the middle band of the Keltner Channels
        :param moving_average_type: Specifies the type of moving average to be used as the middle line of the Keltner Channel
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Keltner Channel indicator for the requested symbol.
        """
        ...

    def ker(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int = 2, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.KaufmanEfficiencyRatio:
        """
        Creates an KaufmanEfficiencyRatio indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose EF we want
        :param period: The period of the EF
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The KaufmanEfficiencyRatio indicator for the given parameters.
        """
        ...

    @overload
    def limit_if_touched_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, trigger_price: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a limit if touched order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param trigger_price: Trigger price for this order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def limit_if_touched_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, trigger_price: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a limit if touched order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param trigger_price: Trigger price for this order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def limit_if_touched_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, trigger_price: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a limit if touched order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param trigger_price: Trigger price for this order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def limit_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a limit order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def limit_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a limit order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def limit_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a limit order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    def link(self, command: typing.Any) -> str:
        """
        Get an authenticated link to execute the given command instance
        
        :param command: The target command
        :returns: The authenticated link.
        """
        ...

    @overload
    def liquidate(self, symbol: typing.Union[QuantConnect.Symbol, str] = None, asynchronous: bool = False, tag: str = None, order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Liquidate your portfolio holdings
        
        :param symbol: Specific asset to liquidate, defaults to all
        :param asynchronous: Flag to indicate if the symbols should be liquidated asynchronously
        :param tag: Custom tag to know who is calling this
        :param order_properties: Order properties to use
        """
        ...

    @overload
    def liquidate(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], asynchronous: bool = False, tag: str = None, order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Liquidate your portfolio holdings
        
        :param symbols: List of symbols to liquidate, defaults to all
        :param asynchronous: Flag to indicate if the symbols should be liquidated asynchronously
        :param tag: Custom tag to know who is calling this
        :param order_properties: Order properties to use
        """
        ...

    @overload
    def liquidate(self, symbol_to_liquidate: typing.Union[QuantConnect.Symbol, str], tag: str) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Liquidate all holdings and cancel open orders. Called at the end of day for tick-strategies.
        
        $"This method is obsolete, please use Liquidate(symbol: symbol_to_liquidate, tag: tag) method
        
        :param symbol_to_liquidate: Symbol we wish to liquidate
        :param tag: Custom tag to know who is calling this.
        :returns: Array of order ids for liquidated symbols.
        """
        ...

    @overload
    def log(self, message: typing.Any) -> None:
        """
        Added another method for logging if user guessed.
        
        :param message: String message to log.
        """
        ...

    @overload
    def log(self, message: str) -> None:
        """
        Added another method for logging if user guessed.
        
        :param message: String message to log.
        """
        ...

    @overload
    def log(self, message: int) -> None:
        """
        Added another method for logging if user guessed.
        
        :param message: Int message to log.
        """
        ...

    @overload
    def log(self, message: float) -> None:
        """
        Added another method for logging if user guessed.
        
        :param message: Double message to log.
        """
        ...

    @overload
    def log(self, message: float) -> None:
        """
        Added another method for logging if user guessed.
        
        :param message: Decimal message to log.
        """
        ...

    def logr(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.LogReturn:
        """
        Creates a new LogReturn indicator.
        
        :param symbol: The symbol whose log return we seek
        :param period: The period of the log return.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar.
        :returns: log return indicator for the requested symbol.
        """
        ...

    def lsma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.LeastSquaresMovingAverage:
        """
        Creates and registers a new Least Squares Moving Average instance.
        
        :param symbol: The symbol whose LSMA we seek.
        :param period: The LSMA period. Normally 14.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar.
        :returns: A LeastSquaredMovingAverage configured with the specified period.
        """
        ...

    def lwma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.LinearWeightedMovingAverage:
        """
        Creates a new LinearWeightedMovingAverage indicator.  This indicator will linearly distribute
        the weights across the periods.
        
        :param symbol: The symbol whose LWMA we want
        :param period: The period over which to compute the LWMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    def macd(self, symbol: typing.Union[QuantConnect.Symbol, str], fast_period: int, slow_period: int, signal_period: int, type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.MovingAverageConvergenceDivergence:
        """
        Creates a MACD indicator for the symbol. The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose MACD we want
        :param fast_period: The period for the fast moving average
        :param slow_period: The period for the slow moving average
        :param signal_period: The period for the signal moving average
        :param type: The type of moving average to use for the MACD
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The moving average convergence divergence between the fast and slow averages.
        """
        ...

    def mad(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.MeanAbsoluteDeviation:
        """
        Creates a new MeanAbsoluteDeviation indicator.
        
        :param symbol: The symbol whose MeanAbsoluteDeviation we want
        :param period: The period over which to compute the MeanAbsoluteDeviation
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The MeanAbsoluteDeviation indicator for the requested symbol over the specified period.
        """
        ...

    def mama(self, symbol: typing.Union[QuantConnect.Symbol, str], fast_limit: float = 0.5, slow_limit: float = 0.05, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.MesaAdaptiveMovingAverage:
        """
        Creates a new Mesa Adaptive Moving Average (MAMA) indicator.
        The MAMA adjusts its smoothing factor based on the market's volatility, making it more adaptive than a simple moving average.
        
        :param symbol: The symbol for which the MAMA indicator is being created.
        :param fast_limit: The fast limit for the adaptive moving average.
        :param slow_limit: The slow limit for the adaptive moving average.
        :param resolution: The resolution
        :param selector: Optional function to select a value from the BaseData. Defaults to casting the input to a TradeBar.
        :returns: The Mesa Adaptive Moving Average (MAMA) indicator for the requested symbol with the specified limits.
        """
        ...

    @overload
    def market_on_close_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market on close order implementation: Send a market order when the exchange closes
        
        :param symbol: The symbol to be ordered
        :param quantity: The number of shares to required
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_on_close_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market on close order implementation: Send a market order when the exchange closes
        
        :param symbol: The symbol to be ordered
        :param quantity: The number of shares to required
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_on_close_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market on close order implementation: Send a market order when the exchange closes
        
        :param symbol: The symbol to be ordered
        :param quantity: The number of shares to required
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_on_open_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market on open order implementation: Send a market order when the exchange opens
        
        :param symbol: The symbol to be ordered
        :param quantity: The number of shares to required
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_on_open_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market on open order implementation: Send a market order when the exchange opens
        
        :param symbol: The symbol to be ordered
        :param quantity: The number of shares to required
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_on_open_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market on open order implementation: Send a market order when the exchange opens
        
        :param symbol: The symbol to be ordered
        :param quantity: The number of shares to required
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market order implementation: Send a market order and wait for it to be filled.
        
        :param symbol: Symbol of the MarketType Required.
        :param quantity: Number of shares to request.
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market order implementation: Send a market order and wait for it to be filled.
        
        :param symbol: Symbol of the MarketType Required.
        :param quantity: Number of shares to request.
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market order implementation: Send a market order and wait for it to be filled.
        
        :param symbol: Symbol of the MarketType Required.
        :param quantity: Number of shares to request.
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def market_order(self, security: QuantConnect.Securities.Security, quantity: float, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Market order implementation: Send a market order and wait for it to be filled.
        
        :param security: Symbol of the MarketType Required.
        :param quantity: Number of shares to request.
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    def mass(self, symbol: typing.Union[QuantConnect.Symbol, str], ema_period: int = 9, sum_period: int = 25, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.MassIndex:
        """
        Creates a new Mass Index indicator. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose Mass Index we want.
        :param ema_period: The period used by both EMA.
        :param sum_period: The sum period.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Mass Index indicator for the requested symbol over the specified period.
        """
        ...

    def max(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.Maximum:
        """
        Creates a new Maximum indicator to compute the maximum value
        
        :param symbol: The symbol whose max we want
        :param period: The look back period over which to compute the max value
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null and the symbol is of type TradeBar defaults to the High property, otherwise it defaults to Value property of BaseData (x => x.Value)
        :returns: A Maximum indicator that compute the max value and the periods since the max value.
        """
        ...

    def mfi(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.MoneyFlowIndex:
        """
        Creates a new MoneyFlowIndex indicator. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose MFI we want
        :param period: The period over which to compute the MFI
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The MoneyFlowIndex indicator for the requested symbol over the specified period.
        """
        ...

    def mgd(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.McGinleyDynamic:
        """
        Creates a new McGinley Dynamic indicator
        
        :param symbol: The symbol whose McGinley Dynamic indicator value we want
        :param period: The period of the McGinley Dynamic indicator
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The McGinley Dynamic indicator for the requested symbol over the specified period.
        """
        ...

    def midpoint(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.MidPoint:
        """
        Creates a new MidPoint indicator.
        
        :param symbol: The symbol whose MIDPOINT we want
        :param period: The period over which to compute the MIDPOINT
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The MidPoint indicator for the requested symbol over the specified period.
        """
        ...

    def midprice(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.MidPrice:
        """
        Creates a new MidPrice indicator.
        
        :param symbol: The symbol whose MIDPRICE we want
        :param period: The period over which to compute the MIDPRICE
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The MidPrice indicator for the requested symbol over the specified period.
        """
        ...

    def min(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.Minimum:
        """
        Creates a new Minimum indicator to compute the minimum value
        
        :param symbol: The symbol whose min we want
        :param period: The look back period over which to compute the min value
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null and the symbol is of type TradeBar defaults to the Low property, otherwise it defaults to Value property of BaseData (x => x.Value)
        :returns: A Minimum indicator that compute the in value and the periods since the min value.
        """
        ...

    def mom(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.Momentum:
        """
        Creates a new Momentum indicator. This will compute the absolute n-period change in the security.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose momentum we want
        :param period: The period over which to compute the momentum
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The momentum indicator for the requested symbol over the specified period.
        """
        ...

    def momersion(self, symbol: typing.Union[QuantConnect.Symbol, str], min_period: typing.Optional[int], full_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.MomersionIndicator:
        """
        Creates a new Momersion indicator.
        
        :param symbol: The symbol whose Momersion we want
        :param min_period: The minimum period over which to compute the Momersion. Must be greater than 3. If null, only full period will be used in computations.
        :param full_period: The full period over which to compute the Momersion
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The Momersion indicator for the requested symbol over the specified period.
        """
        ...

    def momp(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.MomentumPercent:
        """
        Creates a new MomentumPercent indicator. This will compute the n-period percent change in the security.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose momentum we want
        :param period: The period over which to compute the momentum
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The momentum indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def mosc(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], fast_period: int = 19, slow_period: int = 39, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.McClellanOscillator:
        """
        Creates a new McClellan Oscillator indicator
        
        :param symbols: The symbols whose McClellan Oscillator we want
        :param fast_period: Fast period EMA of advance decline difference
        :param slow_period: Slow period EMA of advance decline difference
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The McClellan Oscillator indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def mosc(self, symbols: typing.List[QuantConnect.Symbol], fast_period: int = 19, slow_period: int = 39, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.McClellanOscillator:
        """
        Creates a new McClellan Oscillator indicator
        
        :param symbols: The symbols whose McClellan Oscillator we want
        :param fast_period: Fast period EMA of advance decline difference
        :param slow_period: Slow period EMA of advance decline difference
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The McClellan Oscillator indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def msi(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], fast_period: int = 19, slow_period: int = 39, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.McClellanSummationIndex:
        """
        Creates a new McClellan Summation Index indicator
        
        :param symbols: The symbols whose McClellan Summation Index we want
        :param fast_period: Fast period EMA of advance decline difference
        :param slow_period: Slow period EMA of advance decline difference
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The McClellan Summation Index indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def msi(self, symbols: typing.List[QuantConnect.Symbol], fast_period: int = 19, slow_period: int = 39, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.McClellanSummationIndex:
        """
        Creates a new McClellan Summation Index indicator
        
        :param symbols: The symbols whose McClellan Summation Index we want
        :param fast_period: Fast period EMA of advance decline difference
        :param slow_period: Slow period EMA of advance decline difference
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The McClellan Summation Index indicator for the requested symbol over the specified period.
        """
        ...

    def natr(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.NormalizedAverageTrueRange:
        """
        Creates a new NormalizedAverageTrueRange indicator.
        
        :param symbol: The symbol whose NATR we want
        :param period: The period over which to compute the NATR
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The NormalizedAverageTrueRange indicator for the requested symbol over the specified period.
        """
        ...

    def obv(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.OnBalanceVolume:
        """
        Creates a new On Balance Volume indicator. This will compute the cumulative total volume
        based on whether the close price being higher or lower than the previous period.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose On Balance Volume we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The On Balance Volume indicator for the requested symbol.
        """
        ...

    def on_assignment_order_event(self, assignment_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Option assignment event handler. On an option assignment event for short legs the resulting information is passed to this method.
        
        :param assignment_event: Option exercise event details containing details of the assignment
        """
        ...

    def on_brokerage_disconnect(self) -> None:
        """Brokerage disconnected event handler. This method is called when the brokerage connection is lost."""
        ...

    def on_brokerage_message(self, message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """Brokerage message event handler. This method is called for all types of brokerage messages."""
        ...

    def on_brokerage_reconnect(self) -> None:
        """Brokerage reconnected event handler. This method is called when the brokerage connection is restored after a disconnection."""
        ...

    def on_command(self, data: typing.Any) -> typing.Optional[bool]:
        """
        Generic untyped command call handler
        
        :param data: The associated data
        :returns: True if success, false otherwise. Returning null will disable command feedback.
        """
        ...

    def on_data(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Event - v3.0 DATA EVENT HANDLER: (Pattern) Basic template for user to override for receiving all subscription data in a single event
        
        :param slice: The current slice of data keyed by symbol string
        """
        ...

    def on_delistings(self, delistings: QuantConnect.Data.Market.Delistings) -> None:
        """
        Event handler to be called when there's been a delistings event
        
        :param delistings: The current time slice delistings
        """
        ...

    def on_dividends(self, dividends: QuantConnect.Data.Market.Dividends) -> None:
        """
        Event handler to be called when there's been a dividend event
        
        :param dividends: The current time slice dividends
        """
        ...

    def on_end_of_algorithm(self) -> None:
        """End of algorithm run event handler. This method is called at the end of a backtest or live trading operation. Intended for closing out logs."""
        ...

    @overload
    def on_end_of_day(self, symbol: str) -> None:
        """
        End of a trading day event handler. This method is called at the end of the algorithm day (or multiple times if trading multiple assets).
        
        :param symbol: Asset symbol for this end of day event. Forex and equities have different closing hours.
        """
        ...

    @overload
    def on_end_of_day(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        End of a trading day event handler. This method is called at the end of the algorithm day (or multiple times if trading multiple assets).
        
        :param symbol: Asset symbol for this end of day event. Forex and equities have different closing hours.
        """
        ...

    @overload
    def on_end_of_day(self) -> None:
        """
        End of a trading day event handler. This method is called at the end of the algorithm day (or multiple times if trading multiple assets).
        
        This method is deprecated and will be removed after August 2021. Please use this overload: OnEndOfDay(Symbol symbol)
        """
        ...

    def on_end_of_time_step(self) -> None:
        """
        Invoked at the end of every time step. This allows the algorithm
        to process events before advancing to the next time step.
        """
        ...

    def on_framework_data(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Used to send data updates to algorithm framework models
        
        :param slice: The current data slice
        """
        ...

    def on_framework_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Used to send security changes to algorithm framework models
        
        :param changes: Security additions/removals for this time step
        """
        ...

    def on_margin_call(self, requests: System.Collections.Generic.List[QuantConnect.Orders.SubmitOrderRequest]) -> None:
        """
        Margin call event handler. This method is called right before the margin call orders are placed in the market.
        
        :param requests: The orders to be executed to bring this algorithm within margin limits
        """
        ...

    def on_margin_call_warning(self) -> None:
        """Margin call warning event handler. This method is called when Portfolio.MarginRemaining is under 5% of your Portfolio.TotalPortfolioValue"""
        ...

    def on_order_event(self, order_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Order fill event handler. On an order fill update the resulting information is passed to this method.
        
        :param order_event: Order event details containing details of the events
        """
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param changes: Security additions/removals for this time step
        """
        ...

    def on_splits(self, splits: QuantConnect.Data.Market.Splits) -> None:
        """
        Event handler to be called when there's been a split event
        
        :param splits: The current time slice splits
        """
        ...

    def on_symbol_changed_events(self, symbols_changed: QuantConnect.Data.Market.SymbolChangedEvents) -> None:
        """
        Event handler to be called when there's been a symbol changed event
        
        :param symbols_changed: The current time slice symbol changed events
        """
        ...

    def on_warmup_finished(self) -> None:
        """Called when the algorithm has completed initialization and warm up."""
        ...

    def option_chain(self, symbol: typing.Union[QuantConnect.Symbol, str], flatten: bool = False) -> QuantConnect.Data.Market.OptionChain:
        """
        Get the option chain for the specified symbol at the current time (Time)
        
        :param symbol: The symbol for which the option chain is asked for. It can be either the canonical option or the underlying symbol.
        :param flatten: Whether to flatten the resulting data frame. Used from Python when accessing OptionChain.DataFrame. See History(PyObject, int, Resolution?, bool?, bool?, DataMappingMode?, DataNormalizationMode?, int?, bool)
        :returns: The option chain.
        """
        ...

    def option_chains(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], flatten: bool = False) -> QuantConnect.Data.Market.OptionChains:
        """
        Get the option chains for the specified symbols at the current time (Time)
        
        :param symbols: The symbols for which the option chain is asked for. It can be either the canonical options or the underlying symbols.
        :param flatten: Whether to flatten the resulting data frame. Used from Python when accessing OptionChain.DataFrame. See History(PyObject, int, Resolution?, bool?, bool?, DataMappingMode?, DataNormalizationMode?, int?, bool)
        :returns: The option chains.
        """
        ...

    @overload
    def order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Issue an order/trade for asset: Alias wrapper for Order(string, int);
        
        :param symbol: Symbol to order
        :param quantity: Quantity to order
        :returns: The order ticket instance.
        """
        ...

    @overload
    def order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int) -> QuantConnect.Orders.OrderTicket:
        """
        Issue an order/trade for asset
        
        :param symbol: Symbol to order
        :param quantity: Quantity to order
        :returns: The order ticket instance.
        """
        ...

    @overload
    def order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Issue an order/trade for asset
        
        :param symbol: Symbol to order
        :param quantity: Quantity to order
        :returns: The order ticket instance.
        """
        ...

    @overload
    def order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Wrapper for market order method: submit a new order for quantity of symbol using type order.
        
        :param symbol: Symbol of the MarketType Required.
        :param quantity: Number of shares to request.
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: Place a custom order property or tag (e.g. indicator data).
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def order(self, strategy: QuantConnect.Securities.Option.OptionStrategy, quantity: int, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Issue an order/trade for buying/selling an option strategy
        
        :param strategy: Specification of the strategy to trade
        :param quantity: Quantity of the strategy to trade
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: Sequence of order tickets.
        """
        ...

    @overload
    def order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, type: QuantConnect.Orders.OrderType, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Obsolete implementation of Order method accepting a OrderType. This was deprecated since it
        was impossible to generate other orders via this method. Any calls to this method will always default to a Market Order.
        
        This Order method has been made obsolete, use Order(string, int, bool, string) method instead. Calls to the obsolete method will only generate market orders.
        
        :param symbol: Symbol we want to purchase
        :param quantity: Quantity to buy, + is long, - short.
        :param type: Order Type
        :param asynchronous: Don't wait for the response, just submit order and move on.
        :param tag: Custom data for this order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, type: QuantConnect.Orders.OrderType) -> QuantConnect.Orders.OrderTicket:
        """
        Obsolete method for placing orders.
        
        This Order method has been made obsolete, use the specialized Order helper methods instead. Calls to the obsolete method will only generate market orders.
        
        :param symbol: Symbol we want to order
        :param quantity: The quantity to order
        :param type: The order type
        :returns: The order ticket instance.
        """
        ...

    @overload
    def order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, type: QuantConnect.Orders.OrderType) -> QuantConnect.Orders.OrderTicket:
        """
        Obsolete method for placing orders.
        
        This Order method has been made obsolete, use the specialized Order helper methods instead. Calls to the obsolete method will only generate market orders.
        
        :param symbol: Symbol we want to order
        :param quantity: The quantity to order
        :param type: The order type
        :returns: The order ticket instance.
        """
        ...

    @overload
    def plot(self, series: str, value: float) -> None:
        """
        Plot a chart using string series name, with value.
        
        :param series: Name of the plot series
        :param value: Value to plot
        """
        ...

    @overload
    def plot(self, series: str, value: float) -> None:
        """Plot a chart using string series name, with double value."""
        ...

    @overload
    def plot(self, series: str, value: int) -> None:
        """Plot a chart using string series name, with int value."""
        ...

    @overload
    def plot(self, series: str, value: float) -> None:
        """Plot a chart using string series name, with float value."""
        ...

    @overload
    def plot(self, chart: str, series: str, value: float) -> None:
        """Plot a chart to string chart name, using string series name, with double value."""
        ...

    @overload
    def plot(self, chart: str, series: str, value: int) -> None:
        """Plot a chart to string chart name, using string series name, with int value"""
        ...

    @overload
    def plot(self, chart: str, series: str, value: float) -> None:
        """Plot a chart to string chart name, using string series name, with float value"""
        ...

    @overload
    def plot(self, chart: str, series: str, value: float) -> None:
        """
        Plot a value to a chart of string-chart name, with string series name, and decimal value. If chart does not exist, create it.
        
        :param chart: Chart name
        :param series: Series name
        :param value: Value of the point
        """
        ...

    @overload
    def plot(self, series: str, open: float, high: float, low: float, close: float) -> None:
        """
        Plot a candlestick to the default/primary chart series by the given series name.
        
        :param series: Series name
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, series: str, open: float, high: float, low: float, close: float) -> None:
        """
        Plot a candlestick to the default/primary chart series by the given series name.
        
        :param series: Series name
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, series: str, open: int, high: int, low: int, close: int) -> None:
        """
        Plot a candlestick to the default/primary chart series by the given series name.
        
        :param series: Series name
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, series: str, open: float, high: float, low: float, close: float) -> None:
        """
        Plot a candlestick to the default/primary chart series by the given series name.
        
        :param series: Name of the plot series
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, chart: str, series: str, open: float, high: float, low: float, close: float) -> None:
        """
        Plot a candlestick to the given series of the given chart.
        
        :param chart: Chart name
        :param series: Series name
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, chart: str, series: str, open: float, high: float, low: float, close: float) -> None:
        """
        Plot a candlestick to the given series of the given chart.
        
        :param chart: Chart name
        :param series: Series name
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, chart: str, series: str, open: int, high: int, low: int, close: int) -> None:
        """
        Plot a candlestick to the given series of the given chart.
        
        :param chart: Chart name
        :param series: Series name
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, chart: str, series: str, open: float, high: float, low: float, close: float) -> None:
        """
        Plot a candlestick to a chart of string-chart name, with string series name, and decimal value. If chart does not exist, create it.
        
        :param chart: Chart name
        :param series: Series name
        :param open: The candlestick open value
        :param high: The candlestick high value
        :param low: The candlestick low value
        :param close: The candlestick close value
        """
        ...

    @overload
    def plot(self, series: str, bar: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Plot a candlestick to the given series of the given chart.
        
        :param series: Name of the plot series
        :param bar: The trade bar to be plotted to the candlestick series
        """
        ...

    @overload
    def plot(self, chart: str, series: str, bar: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Plot a candlestick to the given series of the given chart.
        
        :param chart: Chart name
        :param series: Name of the plot series
        :param bar: The trade bar to be plotted to the candlestick series
        """
        ...

    @overload
    def plot(self, chart: str, *indicators: QuantConnect.Indicators.IndicatorBase) -> None:
        """
        Plots the value of each indicator on the chart
        
        :param chart: The chart's name
        :param indicators: The indicators to plot
        """
        ...

    @overload
    def plot_indicator(self, chart: str, *indicators: QuantConnect.Indicators.IndicatorBase) -> None:
        """Automatically plots each indicator when a new value is available"""
        ...

    @overload
    def plot_indicator(self, chart: str, wait_for_ready: bool, *indicators: QuantConnect.Indicators.IndicatorBase) -> None:
        """Automatically plots each indicator when a new value is available, optionally waiting for indicator.IsReady to return true"""
        ...

    def post_initialize(self) -> None:
        """
        Called by setup handlers after Initialize and allows the algorithm a chance to organize
        the data gather in the Initialize method
        """
        ...

    def pphl(self, symbol: typing.Union[QuantConnect.Symbol, str], length_high: int, length_low: int, last_stored_values: int = 100, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.PivotPointsHighLow:
        """
        Creates a new PivotPointsHighLow indicator
        
        :param symbol: The symbol whose PPHL we seek
        :param length_high: The number of surrounding bars whose high values should be less than the current bar's for the bar high to be marked as high pivot point
        :param length_low: The number of surrounding bars whose low values should be more than the current bar's for the bar low to be marked as low pivot point
        :param last_stored_values: The number of last stored indicator values
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The PivotPointsHighLow indicator for the requested symbol.
        """
        ...

    def ppo(self, symbol: typing.Union[QuantConnect.Symbol, str], fast_period: int, slow_period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.PercentagePriceOscillator:
        """
        Creates a new PercentagePriceOscillator indicator.
        
        :param symbol: The symbol whose PPO we want
        :param fast_period: The fast moving average period
        :param slow_period: The slow moving average period
        :param moving_average_type: The type of moving average to use
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The PercentagePriceOscillator indicator for the requested symbol over the specified period.
        """
        ...

    def psar(self, symbol: typing.Union[QuantConnect.Symbol, str], af_start: float = 0.02, af_increment: float = 0.02, af_max: float = 0.2, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.ParabolicStopAndReverse:
        """
        Creates a new Parabolic SAR indicator
        
        :param symbol: The symbol whose PSAR we seek
        :param af_start: Acceleration factor start value. Normally 0.02
        :param af_increment: Acceleration factor increment value. Normally 0.02
        :param af_max: Acceleration factor max value. Normally 0.2
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A ParabolicStopAndReverse configured with the specified periods.
        """
        ...

    def pso(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, ema_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.PremierStochasticOscillator:
        """
        Creates a new instance of the Premier Stochastic Oscillator for the specified symbol.
        
        :param symbol: The symbol for which the stochastic indicator is being calculated.
        :param period: The period for calculating the Stochastic K value.
        :param ema_period: The period for the Exponential Moving Average (EMA) used to smooth the Stochastic K.
        :param resolution: The data resolution (e.g., daily, hourly) for the indicator
        :param selector: Optional function to select a value from the BaseData. Defaults to casting the input to a TradeBar.
        :returns: A PremierStochasticOscillator instance for the specified symbol.
        """
        ...

    @overload
    def quit(self, message: typing.Any) -> None:
        """
        Terminate the algorithm after processing the current event handler.
        
        :param message: Exit message to display on quitting
        """
        ...

    @overload
    def quit(self, message: str = ...) -> None:
        """
        Terminate the algorithm after processing the current event handler.
        
        :param message: Exit message to display on quitting
        """
        ...

    def r(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Rho:
        """
        Creates a new Rho indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Rho
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Rho indicator for the specified symbol.
        """
        ...

    def rc(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, k: float, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.RegressionChannel:
        """
        Creates a new RegressionChannel indicator which will compute the LinearRegression, UpperChannel and LowerChannel lines, the intercept and slope
        
        :param symbol: The symbol whose RegressionChannel we seek
        :param period: The period of the standard deviation and least square moving average (linear regression line)
        :param k: The number of standard deviations specifying the distance between the linear regression and upper or lower channel lines
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: A Regression Channel configured with the specified period and number of standard deviation.
        """
        ...

    def rdv(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int = 2, resolution: QuantConnect.Resolution = ..., selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.RelativeDailyVolume:
        """
        Creates an RelativeDailyVolume indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose RDV we want
        :param period: The period of the RDV
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Relative Volume indicator for the given parameters.
        """
        ...

    @overload
    def record(self, series: str, value: int) -> None:
        """Plot a chart using string series name, with int value. Alias of Plot();"""
        ...

    @overload
    def record(self, series: str, value: float) -> None:
        """Plot a chart using string series name, with double value. Alias of Plot();"""
        ...

    @overload
    def record(self, series: str, value: float) -> None:
        """Plot a chart using string series name, with decimal value. Alias of Plot();"""
        ...

    @overload
    def register_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Creates and registers a new consolidator to receive automatic updates at the specified resolution as well as configures
        the indicator to receive updates from the consolidator.
        
        :param symbol: The symbol to register against
        :param indicator: The indicator to receive data from the consolidator
        :param resolution: The resolution at which to send data to the indicator, null to use the same resolution as the subscription
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def register_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], resolution: typing.Optional[datetime.timedelta] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Creates and registers a new consolidator to receive automatic updates at the specified resolution as well as configures
        the indicator to receive updates from the consolidator.
        
        :param symbol: The symbol to register against
        :param indicator: The indicator to receive data from the consolidator
        :param resolution: The resolution at which to send data to the indicator, null to use the same resolution as the subscription
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def register_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta], selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Registers the consolidator to receive automatic updates as well as configures the indicator to receive updates
        from the consolidator.
        
        :param symbol: The symbol to register against
        :param indicator: The indicator to receive data from the consolidator
        :param consolidator: The consolidator to receive raw subscription data
        :param selector: Selects a value from the BaseData send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def register_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T], resolution: typing.Optional[QuantConnect.Resolution] = None) -> None:
        """
        Registers the consolidator to receive automatic updates as well as configures the indicator to receive updates
        from the consolidator.
        
        :param symbol: The symbol to register against
        :param indicator: The indicator to receive data from the consolidator
        :param resolution: The resolution at which to send data to the indicator, null to use the same resolution as the subscription
        """
        ...

    @overload
    def register_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T], resolution: typing.Optional[QuantConnect.Resolution], selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T]) -> None:
        """
        Registers the consolidator to receive automatic updates as well as configures the indicator to receive updates
        from the consolidator.
        
        :param symbol: The symbol to register against
        :param indicator: The indicator to receive data from the consolidator
        :param resolution: The resolution at which to send data to the indicator, null to use the same resolution as the subscription
        :param selector: Selects a value from the BaseData send into the indicator, if null defaults to a cast (x => (T)x)
        """
        ...

    @overload
    def register_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T], resolution: typing.Optional[datetime.timedelta], selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T] = None) -> None:
        """
        Registers the consolidator to receive automatic updates as well as configures the indicator to receive updates
        from the consolidator.
        
        :param symbol: The symbol to register against
        :param indicator: The indicator to receive data from the consolidator
        :param resolution: The resolution at which to send data to the indicator, null to use the same resolution as the subscription
        :param selector: Selects a value from the BaseData send into the indicator, if null defaults to a cast (x => (T)x)
        """
        ...

    @overload
    def register_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T], consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta], selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_RegisterIndicator_T] = None) -> None:
        """
        Registers the consolidator to receive automatic updates as well as configures the indicator to receive updates
        from the consolidator.
        
        :param symbol: The symbol to register against
        :param indicator: The indicator to receive data from the consolidator
        :param consolidator: The consolidator to receive raw subscription data
        :param selector: Selects a value from the BaseData send into the indicator, if null defaults to a cast (x => (T)x)
        """
        ...

    def remove_option_contract(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Removes the security with the specified symbol. This will cancel all
        open orders and then liquidate any existing holdings
        
        :param symbol: The symbol of the security to be removed
        """
        ...

    def remove_security(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Removes the security with the specified symbol. This will cancel all
        open orders and then liquidate any existing holdings
        
        :param symbol: The symbol of the security to be removed
        """
        ...

    @overload
    def resolve_consolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution], data_type: typing.Type = None) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Gets the default consolidator for the specified symbol and resolution
        
        :param symbol: The symbol whose data is to be consolidated
        :param resolution: The resolution for the consolidator, if null, uses the resolution from subscription
        :param data_type: The data type for this consolidator, if null, uses TradeBar over QuoteBar if present
        :returns: The new default consolidator.
        """
        ...

    @overload
    def resolve_consolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], time_span: typing.Optional[datetime.timedelta], data_type: typing.Type = None) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Gets the default consolidator for the specified symbol and resolution
        
        :param symbol: The symbol whose data is to be consolidated
        :param time_span: The requested time span for the consolidator, if null, uses the resolution from subscription
        :param data_type: The data type for this consolidator, if null, uses TradeBar over QuoteBar if present
        :returns: The new default consolidator.
        """
        ...

    def rma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.RelativeMovingAverage:
        """
        Creates a new Relative Moving Average indicator for the symbol. The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose relative moving average we seek
        :param period: The period of the relative moving average
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: A relative moving average configured with the specified period and number of standard deviation.
        """
        ...

    def roc(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.RateOfChange:
        """
        Creates a new RateOfChange indicator. This will compute the n-period rate of change in the security.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose RateOfChange we want
        :param period: The period over which to compute the RateOfChange
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The RateOfChange indicator for the requested symbol over the specified period.
        """
        ...

    def rocp(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.RateOfChangePercent:
        """
        Creates a new RateOfChangePercent indicator. This will compute the n-period percentage rate of change in the security.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose RateOfChangePercent we want
        :param period: The period over which to compute the RateOfChangePercent
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The RateOfChangePercent indicator for the requested symbol over the specified period.
        """
        ...

    def rocr(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.RateOfChangeRatio:
        """
        Creates a new RateOfChangeRatio indicator.
        
        :param symbol: The symbol whose ROCR we want
        :param period: The period over which to compute the ROCR
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The RateOfChangeRatio indicator for the requested symbol over the specified period.
        """
        ...

    def rsi(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.RelativeStrengthIndex:
        """
        Creates a new RelativeStrengthIndex indicator. This will produce an oscillator that ranges from 0 to 100 based
        on the ratio of average gains to average losses over the specified period.
        
        :param symbol: The symbol whose RSI we want
        :param period: The period over which to compute the RSI
        :param moving_average_type: The type of moving average to use in computing the average gain/loss values
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The RelativeStrengthIndex indicator for the requested symbol over the specified period.
        """
        ...

    def rsv(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.RogersSatchellVolatility:
        """
        Creates a new RogersSatchellVolatility indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose RogersSatchellVolatility we want
        :param period: The period of the rolling window used to compute volatility
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new RogersSatchellVolatility indicator with the specified smoothing type and period.
        """
        ...

    def run_command(self, command: QuantConnect.Commands.CallbackCommand) -> QuantConnect.Commands.CommandResultPacket:
        """
        Run a callback command instance
        
        :param command: The callback command instance
        :returns: The command result.
        """
        ...

    def rvi(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.RelativeVigorIndex:
        """
        Creates a new RelativeVigorIndex indicator.
        
        :param symbol: The symbol whose RVI we want
        :param period: The period over which to compute the RVI
        :param moving_average_type: The type of moving average to use
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The RelativeVigorIndex indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def sedol(self, sedol: str, trading_date: typing.Optional[datetime.datetime] = None) -> QuantConnect.Symbol:
        """
        Converts a SEDOL identifier into a Symbol
        
        :param sedol: The SEDOL identifier of an asset
        :param trading_date: The date that the stock being looked up is/was traded at. The date is used to create a Symbol with the ticker set to the ticker the asset traded under on the trading date.
        :returns: Symbol corresponding to the SEDOL. If no Symbol with a matching SEDOL was found, returns null.
        """
        ...

    @overload
    def sedol(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Symbol into a SEDOL identifier
        
        :param symbol: The Symbol
        :returns: SEDOL corresponding to the Symbol. If no matching SEDOL is found, returns null.
        """
        ...

    @overload
    def sell(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int) -> QuantConnect.Orders.OrderTicket:
        """
        Sell stock (alias of Order)
        
        :param symbol: string Symbol of the asset to trade
        :param quantity: int Quantity of the asset to trade
        :returns: The order ticket instance.
        """
        ...

    @overload
    def sell(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Sell stock (alias of Order)
        
        :param symbol: String symbol to sell
        :param quantity: Quantity to order
        :returns: The order ticket instance.
        """
        ...

    @overload
    def sell(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Sell stock (alias of Order)
        
        :param symbol: String symbol
        :param quantity: Quantity to sell
        :returns: The order ticket instance.
        """
        ...

    @overload
    def sell(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> QuantConnect.Orders.OrderTicket:
        """
        Sell stock (alias of Order)
        
        :param symbol: String symbol to sell
        :param quantity: Quantity to sell
        :returns: The order ticket instance.
        """
        ...

    @overload
    def sell(self, strategy: QuantConnect.Securities.Option.OptionStrategy, quantity: int, asynchronous: bool = False, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Sell Option Strategy (alias of Order)
        
        :param strategy: Specification of the strategy to trade
        :param quantity: Quantity of the strategy to trade
        :param asynchronous: Send the order asynchronously (false). Otherwise we'll block until it fills
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: Sequence of order tickets.
        """
        ...

    def set_account_currency(self, account_currency: str, starting_cash: typing.Optional[float] = None) -> None:
        """
        Sets the account currency cash symbol this algorithm is to manage, as well as
        the starting cash in this currency if given
        
        :param account_currency: The account currency cash symbol to set
        :param starting_cash: The account currency starting cash to set
        """
        ...

    def set_algorithm_id(self, algorithm_id: str) -> None:
        """
        Set the algorithm id (backtestId or live deployId for the algorithm).
        
        :param algorithm_id: String Algorithm Id
        """
        ...

    def set_algorithm_mode(self, algorithm_mode: QuantConnect.AlgorithmMode) -> None:
        """
        Sets the algorithm running mode
        
        :param algorithm_mode: Algorithm mode
        """
        ...

    def set_alpha(self, alpha: QuantConnect.Algorithm.Framework.Alphas.IAlphaModel) -> None:
        """
        Sets the alpha model
        
        :param alpha: Model that generates alpha
        """
        ...

    def set_api(self, api: QuantConnect.Interfaces.IApi) -> None:
        """
        Provide the API for the algorithm.
        
        :param api: Initiated API
        """
        ...

    def set_available_data_types(self, available_data_types: System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]) -> None:
        """
        Set the available data feeds in the SecurityManager
        
        :param available_data_types: The different TickType each Security supports
        """
        ...

    @overload
    def set_benchmark(self, security_type: QuantConnect.SecurityType, symbol: str) -> None:
        """
        Sets the benchmark used for computing statistics of the algorithm to the specified symbol
        
        :param security_type: Is the symbol an equity, forex, base, etc. Default SecurityType.Equity
        :param symbol: symbol to use as the benchmark
        """
        ...

    @overload
    def set_benchmark(self, ticker: str) -> None:
        """
        Sets the benchmark used for computing statistics of the algorithm to the specified ticker, defaulting to SecurityType.Equity
        if the ticker doesn't exist in the algorithm
        
        :param ticker: Ticker to use as the benchmark
        """
        ...

    @overload
    def set_benchmark(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Sets the benchmark used for computing statistics of the algorithm to the specified symbol
        
        :param symbol: symbol to use as the benchmark
        """
        ...

    @overload
    def set_benchmark(self, benchmark: typing.Callable[[datetime.datetime], float]) -> None:
        """
        Sets the specified function as the benchmark, this function provides the value of
        the benchmark at each date/time requested
        
        :param benchmark: The benchmark producing function
        """
        ...

    def set_brokerage_message_handler(self, handler: QuantConnect.Brokerages.IBrokerageMessageHandler) -> None:
        """
        Sets the implementation used to handle messages from the brokerage.
        The default implementation will forward messages to debug or error
        and when a BrokerageMessageType.Error occurs, the algorithm
        is stopped.
        
        :param handler: The message handler to use
        """
        ...

    @overload
    def set_brokerage_model(self, brokerage: QuantConnect.Brokerages.BrokerageName, account_type: QuantConnect.AccountType = ...) -> None:
        """
        Sets the brokerage to emulate in backtesting or paper trading.
        This can be used for brokerages that have been implemented in LEAN
        
        :param brokerage: The brokerage to emulate
        :param account_type: The account type (Cash or Margin)
        """
        ...

    @overload
    def set_brokerage_model(self, model: QuantConnect.Brokerages.IBrokerageModel) -> None:
        """
        Sets the brokerage to emulate in backtesting or paper trading.
        This can be used to set a custom brokerage model.
        
        :param model: The brokerage model to use
        """
        ...

    @overload
    def set_cash(self, starting_cash: float) -> None:
        """
        Set initial cash for the strategy while backtesting. During live mode this value is ignored
        and replaced with the actual cash of your brokerage account.
        
        :param starting_cash: Starting cash for the strategy backtest
        """
        ...

    @overload
    def set_cash(self, starting_cash: int) -> None:
        """
        Set initial cash for the strategy while backtesting. During live mode this value is ignored
        and replaced with the actual cash of your brokerage account.
        
        :param starting_cash: Starting cash for the strategy backtest
        """
        ...

    @overload
    def set_cash(self, starting_cash: float) -> None:
        """
        Set initial cash for the strategy while backtesting. During live mode this value is ignored
        and replaced with the actual cash of your brokerage account.
        
        :param starting_cash: Starting cash for the strategy backtest
        """
        ...

    @overload
    def set_cash(self, symbol: str, starting_cash: float, conversion_rate: float = 0) -> None:
        """
        Set the cash for the specified symbol
        
        :param symbol: The cash symbol to set
        :param starting_cash: Decimal cash value of portfolio
        :param conversion_rate: The current conversion rate for the
        """
        ...

    def set_current_slice(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Sets the current slice
        
        :param slice: The Slice object
        """
        ...

    def set_date_time(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Update the internal algorithm time frontier.
        
        :param frontier: Current utc datetime.
        """
        ...

    def set_deployment_target(self, deployment_target: QuantConnect.DeploymentTarget) -> None:
        """
        Sets the algorithm deployment target
        
        :param deployment_target: Deployment target
        """
        ...

    @overload
    def set_end_date(self, year: int, month: int, day: int) -> None:
        """
        Set the end date for a backtest run
        
        :param year: Int year end date
        :param month: Int month end date
        :param day: Int end date 1-30
        """
        ...

    @overload
    def set_end_date(self, end: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the end date for a backtest.
        
        :param end: Datetime value for end date
        """
        ...

    def set_execution(self, execution: QuantConnect.Algorithm.Framework.Execution.IExecutionModel) -> None:
        """
        Sets the execution model
        
        :param execution: Model defining how to execute trades to reach a portfolio target
        """
        ...

    def set_finished_warming_up(self) -> None:
        """Sets IAlgorithm.IsWarmingUp to false to indicate this algorithm has finished its warm up"""
        ...

    def set_future_chain_provider(self, future_chain_provider: QuantConnect.Interfaces.IFutureChainProvider) -> None:
        """
        Sets the future chain provider, used to get the list of future contracts for an underlying symbol
        
        :param future_chain_provider: The future chain provider
        """
        ...

    def set_history_provider(self, history_provider: QuantConnect.Interfaces.IHistoryProvider) -> None:
        """
        Set the historical data provider
        
        :param history_provider: Historical data provider
        """
        ...

    @overload
    def set_holdings(self, targets: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget], liquidate_existing_holdings: bool = False, tag: str = None, order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Sets holdings for a collection of targets.
        The implementation will order the provided targets executing first those that
        reduce a position, freeing margin.
        
        :param targets: The portfolio desired quantities as percentages
        :param liquidate_existing_holdings: True will liquidate existing holdings
        :param tag: Tag the order with a short string.
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: A list of order tickets.
        """
        ...

    @overload
    def set_holdings(self, symbol: typing.Union[QuantConnect.Symbol, str], percentage: float, liquidate_existing_holdings: bool = False, tag: str = None, order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Alias for SetHoldings to avoid the M-decimal errors.
        
        :param symbol: string symbol we wish to hold
        :param percentage: double percentage of holdings desired
        :param liquidate_existing_holdings: liquidate existing holdings if necessary to hold this stock
        :param tag: Tag the order with a short string.
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: A list of order tickets.
        """
        ...

    @overload
    def set_holdings(self, symbol: typing.Union[QuantConnect.Symbol, str], percentage: float, liquidate_existing_holdings: bool = False, tag: str = None, order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Alias for SetHoldings to avoid the M-decimal errors.
        
        :param symbol: string symbol we wish to hold
        :param percentage: float percentage of holdings desired
        :param liquidate_existing_holdings: bool liquidate existing holdings if necessary to hold this stock
        :param tag: Tag the order with a short string.
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: A list of order tickets.
        """
        ...

    @overload
    def set_holdings(self, symbol: typing.Union[QuantConnect.Symbol, str], percentage: int, liquidate_existing_holdings: bool = False, tag: str = None, order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Alias for SetHoldings to avoid the M-decimal errors.
        
        :param symbol: string symbol we wish to hold
        :param percentage: float percentage of holdings desired
        :param liquidate_existing_holdings: bool liquidate existing holdings if necessary to hold this stock
        :param tag: Tag the order with a short string.
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: A list of order tickets.
        """
        ...

    @overload
    def set_holdings(self, symbol: typing.Union[QuantConnect.Symbol, str], percentage: float, liquidate_existing_holdings: bool = False, tag: str = None, order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Automatically place a market order which will set the holdings to between 100% or -100% of *PORTFOLIO VALUE*.
        E.g. SetHoldings("AAPL", 0.1); SetHoldings("IBM", -0.2); -> Sets portfolio as long 10% APPL and short 20% IBM
        E.g. SetHoldings("AAPL", 2); -> Sets apple to 2x leveraged with all our cash.
        If the market is closed, place a market on open order.
        
        :param symbol: Symbol indexer
        :param percentage: decimal fraction of portfolio to set stock
        :param liquidate_existing_holdings: bool flag to clean all existing holdings before setting new faction.
        :param tag: Tag the order with a short string.
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: A list of order tickets.
        """
        ...

    def set_live_mode(self, live: bool) -> None:
        """Set live mode state of the algorithm run: Public setter for the algorithm property LiveMode."""
        ...

    def set_locked(self) -> None:
        """Lock the algorithm initialization to avoid user modifiying cash and data stream subscriptions"""
        ...

    def set_maximum_orders(self, max: int) -> None:
        """Maximum number of orders for the algorithm"""
        ...

    def set_name(self, name: str) -> None:
        """
        Sets name to the currently running backtest
        
        :param name: The name for the backtest
        """
        ...

    def set_object_store(self, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Sets the object store
        
        :param object_store: The object store
        """
        ...

    def set_option_chain_provider(self, option_chain_provider: QuantConnect.Interfaces.IOptionChainProvider) -> None:
        """
        Sets the option chain provider, used to get the list of option contracts for an underlying symbol
        
        :param option_chain_provider: The option chain provider
        """
        ...

    def set_parameters(self, parameters: System.Collections.Generic.Dictionary[str, str]) -> None:
        """
        Sets the parameters from the dictionary
        
        :param parameters: Dictionary containing the parameter names to values
        """
        ...

    def set_portfolio_construction(self, portfolio_construction: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel) -> None:
        """
        Sets the portfolio construction model
        
        :param portfolio_construction: Model defining how to build a portfolio from insights
        """
        ...

    def set_quit(self, quit: bool) -> None:
        """
        Set the Quit flag property of the algorithm.
        
        :param quit: Boolean quit state
        """
        ...

    def set_risk_free_interest_rate_model(self, model: QuantConnect.Data.IRiskFreeInterestRateModel) -> None:
        """
        Sets the risk free interest rate model to be used in the algorithm
        
        :param model: The risk free interest rate model to use
        """
        ...

    def set_risk_management(self, risk_management: QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel) -> None:
        """
        Sets the risk management model
        
        :param risk_management: Model defining how risk is managed
        """
        ...

    def set_run_time_error(self, exception: System.Exception) -> None:
        """
        Set the runtime error
        
        :param exception: Represents error that occur during execution
        """
        ...

    @overload
    def set_runtime_statistic(self, name: str, value: str) -> None:
        """
        Set a runtime statistic for the algorithm. Runtime statistics are shown in the top banner of a live algorithm GUI.
        
        :param name: Name of your runtime statistic
        :param value: String value of your runtime statistic
        """
        ...

    @overload
    def set_runtime_statistic(self, name: str, value: float) -> None:
        """
        Set a runtime statistic for the algorithm. Runtime statistics are shown in the top banner of a live algorithm GUI.
        
        :param name: Name of your runtime statistic
        :param value: Decimal value of your runtime statistic
        """
        ...

    @overload
    def set_runtime_statistic(self, name: str, value: int) -> None:
        """
        Set a runtime statistic for the algorithm. Runtime statistics are shown in the top banner of a live algorithm GUI.
        
        :param name: Name of your runtime statistic
        :param value: Int value of your runtime statistic
        """
        ...

    @overload
    def set_runtime_statistic(self, name: str, value: float) -> None:
        """
        Set a runtime statistic for the algorithm. Runtime statistics are shown in the top banner of a live algorithm GUI.
        
        :param name: Name of your runtime statistic
        :param value: Double value of your runtime statistic
        """
        ...

    @overload
    def set_security_initializer(self, security_initializer: QuantConnect.Securities.ISecurityInitializer) -> None:
        """
        Sets the security initializer, used to initialize/configure securities after creation.
        The initializer will be applied to all universes and manually added securities.
        
        :param security_initializer: The security initializer
        """
        ...

    @overload
    def set_security_initializer(self, security_initializer: typing.Callable[[QuantConnect.Securities.Security], None]) -> None:
        """
        Sets the security initializer function, used to initialize/configure securities after creation.
        The initializer will be applied to all universes and manually added securities.
        
        :param security_initializer: The security initializer function
        """
        ...

    @overload
    def set_security_initializer(self, security_initializer: typing.Callable[[QuantConnect.Securities.Security, bool], None]) -> None:
        """
        Sets the security initializer function, used to initialize/configure securities after creation.
        The initializer will be applied to all universes and manually added securities.
        
        This method is deprecated. Please use this overload: SetSecurityInitializer(Action<Security> security_initializer)
        
        :param security_initializer: The security initializer function
        """
        ...

    @overload
    def set_start_date(self, year: int, month: int, day: int) -> None:
        """
        Set the start date for backtest.
        
        :param year: Int year starting date
        :param month: Int month starting date
        :param day: Int starting date 1-30
        """
        ...

    @overload
    def set_start_date(self, start: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the start date for the backtest
        
        :param start: Datetime Start date for backtest
        """
        ...

    def set_statistics_service(self, statistics_service: QuantConnect.Statistics.IStatisticsService) -> None:
        """
        Sets the statistics service instance to be used by the algorithm
        
        :param statistics_service: The statistics service instance
        """
        ...

    def set_status(self, status: QuantConnect.AlgorithmStatus) -> None:
        """
        Set the state of a live deployment
        
        :param status: Live deployment status
        """
        ...

    @overload
    def set_summary_statistic(self, name: str, value: str) -> None:
        """
        Set a custom summary statistic for the algorithm.
        
        :param name: Name of the custom summary statistic
        :param value: Value of the custom summary statistic
        """
        ...

    @overload
    def set_summary_statistic(self, name: str, value: int) -> None:
        """
        Set a custom summary statistic for the algorithm.
        
        :param name: Name of the custom summary statistic
        :param value: Value of the custom summary statistic
        """
        ...

    @overload
    def set_summary_statistic(self, name: str, value: float) -> None:
        """
        Set a custom summary statistic for the algorithm.
        
        :param name: Name of the custom summary statistic
        :param value: Value of the custom summary statistic
        """
        ...

    @overload
    def set_summary_statistic(self, name: str, value: float) -> None:
        """
        Set a custom summary statistic for the algorithm.
        
        :param name: Name of the custom summary statistic
        :param value: Value of the custom summary statistic
        """
        ...

    def set_tags(self, tags: System.Collections.Generic.HashSet[str]) -> None:
        """
        Sets the tags for the algorithm
        
        :param tags: The tags
        """
        ...

    @overload
    def set_time_zone(self, time_zone: str) -> None:
        """
        Sets the time zone of the Time property in the algorithm
        
        :param time_zone: The desired time zone
        """
        ...

    @overload
    def set_time_zone(self, time_zone: typing.Any) -> None:
        """
        Sets the time zone of the Time property in the algorithm
        
        :param time_zone: The desired time zone
        """
        ...

    def set_trade_builder(self, trade_builder: QuantConnect.Interfaces.ITradeBuilder) -> None:
        """Set the ITradeBuilder implementation to generate trades from executions and market price updates"""
        ...

    def set_universe_selection(self, universe_selection: QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel) -> None:
        """
        Sets the universe selection model
        
        :param universe_selection: Model defining universes for the algorithm
        """
        ...

    @overload
    def set_warmup(self, time_span: datetime.timedelta) -> None:
        """
        Sets the warm up period to the specified value
        
        :param time_span: The amount of time to warm up, this does not take into account market hours/weekends
        """
        ...

    @overload
    def set_warmup(self, time_span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution]) -> None:
        """
        Sets the warm up period to the specified value
        
        :param time_span: The amount of time to warm up, this does not take into account market hours/weekends
        :param resolution: The resolution to request
        """
        ...

    @overload
    def set_warmup(self, bar_count: int) -> None:
        """
        Sets the warm up period by resolving a start date that would send that amount of data into
        the algorithm. The highest (smallest) resolution in the securities collection will be used.
        For example, if an algorithm has minute and daily data and 200 bars are requested, that would
        use 200 minute bars.
        
        :param bar_count: The number of data points requested for warm up
        """
        ...

    @overload
    def set_warmup(self, bar_count: int, resolution: typing.Optional[QuantConnect.Resolution]) -> None:
        """
        Sets the warm up period by resolving a start date that would send that amount of data into
        the algorithm.
        
        :param bar_count: The number of data points requested for warm up
        :param resolution: The resolution to request
        """
        ...

    @overload
    def set_warm_up(self, time_span: datetime.timedelta) -> None:
        """
        Sets the warm up period to the specified value
        
        :param time_span: The amount of time to warm up, this does not take into account market hours/weekends
        """
        ...

    @overload
    def set_warm_up(self, time_span: datetime.timedelta, resolution: typing.Optional[QuantConnect.Resolution]) -> None:
        """
        Sets the warm up period to the specified value
        
        :param time_span: The amount of time to warm up, this does not take into account market hours/weekends
        :param resolution: The resolution to request
        """
        ...

    @overload
    def set_warm_up(self, bar_count: int) -> None:
        """
        Sets the warm up period by resolving a start date that would send that amount of data into
        the algorithm. The highest (smallest) resolution in the securities collection will be used.
        For example, if an algorithm has minute and daily data and 200 bars are requested, that would
        use 200 minute bars.
        
        :param bar_count: The number of data points requested for warm up
        """
        ...

    @overload
    def set_warm_up(self, bar_count: int, resolution: typing.Optional[QuantConnect.Resolution]) -> None:
        """
        Sets the warm up period by resolving a start date that would send that amount of data into
        the algorithm.
        
        :param bar_count: The number of data points requested for warm up
        :param resolution: The resolution to request
        """
        ...

    @overload
    def shortable(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines if the Symbol is shortable at the brokerage
        
        :param symbol: Symbol to check if shortable
        :returns: True if shortable.
        """
        ...

    @overload
    def shortable(self, symbol: typing.Union[QuantConnect.Symbol, str], short_quantity: float, update_order_id: typing.Optional[int] = None) -> bool:
        """
        Determines if the Symbol is shortable at the brokerage
        
        :param symbol: Symbol to check if shortable
        :param short_quantity: Order's quantity to check if it is currently shortable, taking into account current holdings and open orders
        :param update_order_id: Optionally the id of the order being updated. When updating an order we want to ignore it's submitted short quantity and use the new provided quantity to determine if we can perform the update
        :returns: True if the symbol can be shorted by the requested quantity.
        """
        ...

    def shortable_quantity(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> int:
        """
        Gets the quantity shortable for the given asset
        
        :returns: Quantity shortable for the given asset. Zero if not shortable, or a number greater than zero if shortable.
        """
        ...

    def si(self, symbol: typing.Union[QuantConnect.Symbol, str], limit_move: float, resolution: typing.Optional[QuantConnect.Resolution] = ..., selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.WilderSwingIndex:
        """
        Creates a Wilder Swing Index (SI) indicator for the symbol.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose SI we want
        :param limit_move: The maximum daily change in price for the SI
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The WilderSwingIndex for the given parameters.
        """
        ...

    def sm(self, symbol: typing.Union[QuantConnect.Symbol, str], bollinger_period: int = 20, bollinger_multiplier: float = 2, keltner_period: int = 20, keltner_multiplier: float = 1.5, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.SqueezeMomentum:
        """
        Creates a Squeeze Momentum indicator to identify market squeezes and potential breakouts.
        Compares Bollinger Bands and Keltner Channels to signal low or high volatility periods.
        
        :param symbol: The symbol for which the indicator is calculated.
        :param bollinger_period: The period for Bollinger Bands.
        :param bollinger_multiplier: The multiplier for the Bollinger Bands' standard deviation.
        :param keltner_period: The period for Keltner Channels.
        :param keltner_multiplier: The multiplier for the Average True Range in Keltner Channels.
        :param resolution: The resolution of the data.
        :param selector: Selects a value from the BaseData to send into the indicator. If null, defaults to the Value property of BaseData (x => x.Value).
        :returns: The configured Squeeze Momentum indicator.
        """
        ...

    def sma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.SimpleMovingAverage:
        """
        Creates an SimpleMovingAverage indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose SMA we want
        :param period: The period of the SMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The SimpleMovingAverage for the given parameters.
        """
        ...

    def sobv(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.SmoothedOnBalanceVolume:
        """
        Creates a new SmoothedOnBalanceVolume indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose SmoothedOnBalanceVolume we want
        :param period: The smoothing period used to smooth the computed OnBalanceVolume values
        :param type: The type of smoothing to use
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new SmoothedOnBalanceVolume indicator with the specified smoothing type and period.
        """
        ...

    def sortino(self, symbol: typing.Union[QuantConnect.Symbol, str], sortino_period: int, minimum_acceptable_return: float = 0.0, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.SortinoRatio:
        """
        Creates a new Sortino indicator.
        
        :param symbol: The symbol whose Sortino we want
        :param sortino_period: Period of historical observation for Sortino ratio calculation
        :param minimum_acceptable_return: Minimum acceptable return (eg risk-free rate) for the Sortino ratio calculation
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The SortinoRatio indicator for the requested symbol over the specified period.
        """
        ...

    def sr(self, symbol: typing.Union[QuantConnect.Symbol, str], sharpe_period: int, risk_free_rate: typing.Optional[float] = None, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.SharpeRatio:
        """
        Creates a new SharpeRatio indicator.
        
        :param symbol: The symbol whose RSR we want
        :param sharpe_period: Period of historical observation for sharpe ratio calculation
        :param risk_free_rate: Risk-free rate for sharpe ratio calculation. If not specified, it will use the algorithms' RiskFreeInterestRateModel
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The SharpeRatio indicator for the requested symbol over the specified period.
        """
        ...

    def srsi(self, symbol: typing.Union[QuantConnect.Symbol, str], rsi_period: int, stoch_period: int, k_smoothing_period: int, d_smoothing_period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.StochasticRelativeStrengthIndex:
        """
        Creates a new Stochastic RSI indicator which will compute the %K and %D
        
        :param symbol: The symbol whose Stochastic RSI we seek
        :param rsi_period: The period of the relative strength index
        :param stoch_period: The period of the stochastic indicator
        :param k_smoothing_period: The smoothing period of K output
        :param d_smoothing_period: The smoothing period of D output
        :param moving_average_type: The type of moving average to be used
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: A StochasticRelativeStrengthIndex configured with the specified periods and moving average type.
        """
        ...

    def stc(self, symbol: typing.Union[QuantConnect.Symbol, str], cycle_period: int, fast_period: int, slow_period: int, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.SchaffTrendCycle:
        """
        Creates a new Schaff Trend Cycle indicator
        
        :param symbol: The symbol for the indicator to track
        :param cycle_period: The signal period
        :param fast_period: The fast moving average period
        :param slow_period: The slow moving average period
        :param moving_average_type: The type of moving average to use
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The SchaffTrendCycle indicator for the requested symbol over the specified period.
        """
        ...

    def std(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.StandardDeviation:
        """
        Creates a new StandardDeviation indicator. This will return the population standard deviation of samples over the specified period.
        
        :param symbol: The symbol whose STD we want
        :param period: The period over which to compute the STD
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The StandardDeviation indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def sto(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, k_period: int, d_period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.Stochastic:
        """
        Creates a new Stochastic indicator.
        
        :param symbol: The symbol whose stochastic we seek
        :param period: The period of the stochastic. Normally 14
        :param k_period: The sum period of the stochastic. Normally 14
        :param d_period: The sum period of the stochastic. Normally 3
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: Stochastic indicator for the requested symbol.
        """
        ...

    @overload
    def sto(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.Stochastic:
        """
        Overload short hand to create a new Stochastic indicator; defaulting to the 3 period for dStoch
        
        :param symbol: The symbol whose stochastic we seek
        :param period: The period of the stochastic. Normally 14
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: Stochastic indicator for the requested symbol.
        """
        ...

    @overload
    def stop_limit_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, stop_price: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a stop limit order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param stop_price: Stop price for this order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def stop_limit_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stop_price: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a stop limit order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param stop_price: Stop price for this order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def stop_limit_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stop_price: float, limit_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Send a stop limit order to the transaction handler:
        
        :param symbol: String symbol for the asset
        :param quantity: Quantity of shares for limit order
        :param stop_price: Stop price for this order
        :param limit_price: Limit price to fill this order
        :param tag: String tag for the order (optional)
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def stop_market_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, stop_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a stop market order and return the newly created order id; or negative if the order is invalid
        
        :param symbol: String symbol for the asset we're trading
        :param quantity: Quantity to be traded
        :param stop_price: Price to fill the stop order
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def stop_market_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stop_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a stop market order and return the newly created order id; or negative if the order is invalid
        
        :param symbol: String symbol for the asset we're trading
        :param quantity: Quantity to be traded
        :param stop_price: Price to fill the stop order
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def stop_market_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stop_price: float, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a stop market order and return the newly created order id; or negative if the order is invalid
        
        :param symbol: String symbol for the asset we're trading
        :param quantity: Quantity to be traded
        :param stop_price: Price to fill the stop order
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    def str(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, multiplier: float, moving_average_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.SuperTrend:
        """
        Creates a new SuperTrend indicator.
        
        :param symbol: The symbol whose SuperTrend indicator we want.
        :param period: The smoothing period for average true range.
        :param multiplier: Multiplier to calculate basic upper and lower bands width.
        :param moving_average_type: Smoother type for average true range, defaults to Wilders.
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        """
        ...

    def submit_order_request(self, request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Will submit an order request to the algorithm
        
        :param request: The request to submit
        :returns: The order ticket.
        """
        ...

    def sum(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.Sum:
        """
        Creates a new Sum indicator.
        
        :param symbol: The symbol whose Sum we want
        :param period: The period over which to compute the Sum
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The Sum indicator for the requested symbol over the specified period.
        """
        ...

    def swiss(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, delta: float, tool: QuantConnect.Indicators.SwissArmyKnifeTool, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.SwissArmyKnife:
        """
        Creates Swiss Army Knife transformation for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol to use for calculations
        :param period: The period of the calculation
        :param delta: The delta scale of the BandStop or BandPass
        :param tool: The tool os the Swiss Army Knife
        :param resolution: The resolution
        :param selector: elects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The calculation using the given tool.
        """
        ...

    def symbol(self, ticker: str) -> QuantConnect.Symbol:
        """
        Converts the string 'ticker' symbol into a full Symbol object
        This requires that the string 'ticker' has been added to the algorithm
        
        :param ticker: The ticker symbol. This should be the ticker symbol as it was added to the algorithm
        :returns: The symbol object mapped to the specified ticker.
        """
        ...

    def t(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Theta:
        """
        Creates a new Theta indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Theta
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Theta indicator for the specified symbol.
        """
        ...

    def t_3(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, volume_factor: float = 0.7, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.T3MovingAverage:
        """
        Creates a new T3MovingAverage indicator.
        
        :param symbol: The symbol whose T3 we want
        :param period: The period over which to compute the T3
        :param volume_factor: The volume factor to be used for the T3 (value must be in the [0,1] range, defaults to 0.7)
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The T3MovingAverage indicator for the requested symbol over the specified period.
        """
        ...

    def tdd(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, minimum_acceptable_return: float = 0, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.TargetDownsideDeviation:
        """
        Creates a new TargetDownsideDeviation indicator. The target downside deviation is defined as the root-mean-square, or RMS, of the deviations of the
        realized return’s underperformance from the target return where all returns above the target return are treated as underperformance of 0.
        
        :param symbol: The symbol whose TDD we want
        :param period: The period over which to compute the TDD
        :param minimum_acceptable_return: Minimum acceptable return (MAR) for the target downside deviation calculation
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The TargetDownsideDeviation indicator for the requested symbol over the specified period.
        """
        ...

    def tema(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.TripleExponentialMovingAverage:
        """
        Creates a new TripleExponentialMovingAverage indicator.
        
        :param symbol: The symbol whose TEMA we want
        :param period: The period over which to compute the TEMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The TripleExponentialMovingAverage indicator for the requested symbol over the specified period.
        """
        ...

    def ticker(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        For the given symbol will resolve the ticker it used at the current algorithm date
        
        :param symbol: The symbol to get the ticker for
        :returns: The mapped ticker for a symbol.
        """
        ...

    def tp(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int = 2, value_area_volume_percentage: float = 0.70, price_range_round_off: float = 0.05, resolution: QuantConnect.Resolution = ..., selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.TimeProfile:
        """
        Creates an Market Profile indicator for the symbol with Time Price Opportunity (TPO) mode. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose TP we want
        :param period: The period of the TP
        :param value_area_volume_percentage: The percentage of volume contained in the value area
        :param price_range_round_off: How many digits you want to round and the precision. i.e 0.01 round to two digits exactly.
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Time Profile indicator for the given parameters.
        """
        ...

    def tr(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.TrueRange:
        """
        Creates a new TrueRange indicator.
        
        :param symbol: The symbol whose TR we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The TrueRange indicator for the requested symbol.
        """
        ...

    @overload
    def trailing_stop_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, trailing_amount: float, trailing_as_percentage: bool, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a trailing stop order and return the newly created order id; or negative if the order is invalid.
        It will calculate the stop price using the trailing amount and the current market price.
        
        :param symbol: Trading asset symbol
        :param quantity: Quantity to be traded
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def trailing_stop_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, trailing_amount: float, trailing_as_percentage: bool, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a trailing stop order and return the newly created order id; or negative if the order is invalid.
        It will calculate the stop price using the trailing amount and the current market price.
        
        :param symbol: Trading asset symbol
        :param quantity: Quantity to be traded
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def trailing_stop_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, trailing_amount: float, trailing_as_percentage: bool, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a trailing stop order and return the newly created order id; or negative if the order is invalid.
        It will calculate the stop price using the trailing amount and the current market price.
        
        :param symbol: Trading asset symbol
        :param quantity: Quantity to be traded
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def trailing_stop_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, stop_price: float, trailing_amount: float, trailing_as_percentage: bool, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a trailing stop order and return the newly created order id; or negative if the order is invalid
        
        :param symbol: Trading asset symbol
        :param quantity: Quantity to be traded
        :param stop_price: Initial stop price at which the order should be triggered
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def trailing_stop_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stop_price: float, trailing_amount: float, trailing_as_percentage: bool, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a trailing stop order and return the newly created order id; or negative if the order is invalid
        
        :param symbol: Trading asset symbol
        :param quantity: Quantity to be traded
        :param stop_price: Initial stop price at which the order should be triggered
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def trailing_stop_order(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stop_price: float, trailing_amount: float, trailing_as_percentage: bool, tag: str = ..., order_properties: QuantConnect.Interfaces.IOrderProperties = None) -> QuantConnect.Orders.OrderTicket:
        """
        Create a trailing stop order and return the newly created order id; or negative if the order is invalid
        
        :param symbol: Trading asset symbol
        :param quantity: Quantity to be traded
        :param stop_price: Initial stop price at which the order should be triggered
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param tag: Optional string data tag for the order
        :param order_properties: The order properties to use. Defaults to DefaultOrderProperties
        :returns: The order ticket instance.
        """
        ...

    @overload
    def train(self, training_code: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the provided training code to execute immediately
        
        :param training_code: The training code to be invoked
        """
        ...

    @overload
    def train(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, training_code: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the training code to run using the specified date and time rules
        
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param training_code: The training code to be invoked
        """
        ...

    def trima(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.TriangularMovingAverage:
        """
        Creates a new TriangularMovingAverage indicator.
        
        :param symbol: The symbol whose TRIMA we want
        :param period: The period over which to compute the TRIMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The TriangularMovingAverage indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def trin(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.ArmsIndex:
        """
        Creates a new Arms Index indicator
        
        :param symbols: The symbols whose Arms Index we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Arms Index indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def trin(self, symbols: typing.List[QuantConnect.Symbol], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.ArmsIndex:
        """
        Creates a new Arms Index indicator
        
        :param symbols: The symbols whose Arms Index we want
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Arms Index indicator for the requested symbol over the specified period.
        """
        ...

    def trix(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.Trix:
        """
        Creates a new Trix indicator.
        
        :param symbol: The symbol whose TRIX we want
        :param period: The period over which to compute the TRIX
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The Trix indicator for the requested symbol over the specified period.
        """
        ...

    def tsf(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.TimeSeriesForecast:
        """
        Creates a new Time Series Forecast indicator
        
        :param symbol: The symbol whose TSF we want
        :param period: The period of the TSF
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to Value property of BaseData (x => x.Value)
        :returns: The TimeSeriesForecast indicator for the requested symbol over the specified period.
        """
        ...

    def tsi(self, symbol: typing.Union[QuantConnect.Symbol, str], long_term_period: int = 25, short_term_period: int = 13, signal_period: int = 7, signal_type: QuantConnect.Indicators.MovingAverageType = ..., resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.TrueStrengthIndex:
        """
        Creates a TrueStrengthIndex indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose TSI we want
        :param long_term_period: Period used for the second (double) price change smoothing
        :param short_term_period: Period used for the first price change smoothing
        :param signal_period: The signal period
        :param signal_type: The type of moving average to use for the signal
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The TrueStrengthIndex indicator for the given parameters.
        """
        ...

    def ultosc(self, symbol: typing.Union[QuantConnect.Symbol, str], period_1: int, period_2: int, period_3: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.UltimateOscillator:
        """
        Creates a new UltimateOscillator indicator.
        
        :param symbol: The symbol whose ULTOSC we want
        :param period_1: The first period over which to compute the ULTOSC
        :param period_2: The second period over which to compute the ULTOSC
        :param period_3: The third period over which to compute the ULTOSC
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The UltimateOscillator indicator for the requested symbol over the specified period.
        """
        ...

    def unregister_indicator(self, indicator: QuantConnect.Indicators.IndicatorBase) -> None:
        """
        Will unregister an indicator and it's associated consolidator instance so they stop receiving data updates
        
        :param indicator: The indicator instance to unregister
        """
        ...

    @overload
    def v(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Vega:
        """
        Creates a new Vega indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Vega
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Vega indicator for the specified symbol.
        """
        ...

    @overload
    def v(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.Variance:
        """
        Creates a new Variance indicator. This will return the population variance of samples over the specified period.
        
        :param symbol: The symbol whose variance we want
        :param period: The period over which to compute the variance
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The Variance indicator for the requested symbol over the specified period.
        """
        ...

    @overload
    def var(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, confidence_level: float, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.ValueAtRisk:
        """
        Creates a new ValueAtRisk indicator.
        
        :param symbol: The symbol whose VAR we want
        :param period: The period over which to compute the VAR
        :param confidence_level: The confidence level for Value at risk calculation
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The ValueAtRisk indicator for the requested Symbol, lookback period, and confidence level.
        """
        ...

    @overload
    def var(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.Variance:
        """
        Creates a new Variance indicator. This will return the population variance of samples over the specified period.
        
        'VAR' is obsolete please use 'V' instead
        
        :param symbol: The symbol whose VAR we want
        :param period: The period over which to compute the VAR
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The Variance indicator for the requested symbol over the specified period.
        """
        ...

    def vidya(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.VariableIndexDynamicAverage:
        """
        Creates a new Chande's Variable Index Dynamic Average indicator.
        
        :param symbol: The symbol whose VIDYA we want
        :param period: The period over which to compute the VIDYA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The VariableIndexDynamicAverage indicator for the requested symbol over the specified period.
        """
        ...

    def vp(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int = 2, value_area_volume_percentage: float = 0.70, price_range_round_off: float = 0.05, resolution: QuantConnect.Resolution = ..., selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.VolumeProfile:
        """
        Creates an Market Profile indicator for the symbol with Volume Profile (VOL) mode. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose VP we want
        :param period: The period of the VP
        :param value_area_volume_percentage: The percentage of volume contained in the value area
        :param price_range_round_off: How many digits you want to round and the precision. i.e 0.01 round to two digits exactly.
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Volume Profile indicator for the given parameters.
        """
        ...

    def vtx(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.Vortex:
        """
        Creates a new Vortex indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose VWMA we want
        :param period: The smoothing period used to smooth the computed VWMA values
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new Vortex indicator with the specified smoothing period.
        """
        ...

    @overload
    def vwap(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.VolumeWeightedAveragePriceIndicator:
        """
        Creates an VolumeWeightedAveragePrice (VWAP) indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose VWAP we want
        :param period: The period of the VWAP
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The VolumeWeightedAveragePrice for the given parameters.
        """
        ...

    @overload
    def vwap(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Indicators.IntradayVwap:
        """
        Creates the canonical VWAP indicator that resets each day. The indicator will be automatically
        updated on the security's configured resolution.
        
        :param symbol: The symbol whose VWAP we want
        :returns: The IntradayVWAP for the specified symbol.
        """
        ...

    def vwma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.TradeBar] = None) -> QuantConnect.Indicators.VolumeWeightedMovingAverage:
        """
        Creates a new VolumeWeightedMovingAverage indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose VWMA we want
        :param period: The smoothing period used to smooth the computed VWMA values
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: A new VolumeWeightedMovingAverage indicator with the specified smoothing period.
        """
        ...

    @overload
    def warm_up_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Warms up a given indicator with historical data
        
        :param symbol: The symbol whose indicator we want
        :param indicator: The indicator we want to warm up
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def warm_up_indicator(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Warms up a given indicator with historical data
        
        :param symbols: The symbols whose indicator we want
        :param indicator: The indicator we want to warm up
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def warm_up_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect.Indicators.IndicatorDataPoint], period: datetime.timedelta, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Warms up a given indicator with historical data
        
        :param symbol: The symbol whose indicator we want
        :param indicator: The indicator we want to warm up
        :param period: The necessary period to warm up the indicator
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def warm_up_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T] = None) -> None:
        """
        Warms up a given indicator with historical data
        
        :param symbol: The symbol whose indicator we want
        :param indicator: The indicator we want to warm up
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def warm_up_indicator(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T] = None) -> None:
        """
        Warms up a given indicator with historical data
        
        :param symbols: The symbols whose indicator we want
        :param indicator: The indicator we want to warm up
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        """
        ...

    @overload
    def warm_up_indicator(self, symbol: typing.Union[QuantConnect.Symbol, str], indicator: QuantConnect.Indicators.IndicatorBase[QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T], period: datetime.timedelta, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect_Algorithm_QCAlgorithm_WarmUpIndicator_T] = None) -> None:
        """
        Warms up a given indicator with historical data
        
        :param symbol: The symbol whose indicator we want
        :param indicator: The indicator we want to warm up
        :param period: The necessary period to warm up the indicator
        :param selector: Selects a value from the BaseData send into the indicator, if null defaults to a cast (x => (T)x)
        """
        ...

    def wilr(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.WilliamsPercentR:
        """
        Creates a new Williams %R indicator. This will compute the percentage change of
        the current closing price in relation to the high and low of the past N periods.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose Williams %R we want
        :param period: The period over which to compute the Williams %R
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The Williams %R indicator for the requested symbol over the specified period.
        """
        ...

    def wwma(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.WilderMovingAverage:
        """
        Creates a WilderMovingAverage indicator for the symbol.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose WMA we want
        :param period: The period of the WMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The WilderMovingAverage for the given parameters.
        """
        ...

    def zlema(self, symbol: typing.Union[QuantConnect.Symbol, str], period: int, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> QuantConnect.Indicators.ZeroLagExponentialMovingAverage:
        """
        Creates a ZeroLagExponentialMovingAverage indicator for the symbol. The indicator will be automatically
        updated on the given resolution.
        
        :param symbol: The symbol whose ZLEMA we want
        :param period: The period of the ZLEMA
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The ZeroLagExponentialMovingAverage for the given parameters.
        """
        ...

    def zz(self, symbol: typing.Union[QuantConnect.Symbol, str], sensitivity: float = 0.05, min_trend_length: int = 1, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.ZigZag:
        """
        Creates a ZigZag indicator for the specified symbol, with adjustable sensitivity and minimum trend length.
        
        :param symbol: The symbol for which to create the ZigZag indicator.
        :param sensitivity: The sensitivity for detecting pivots.
        :param min_trend_length: The minimum number of bars required for a trend before a pivot is confirmed.
        :param resolution: The resolution
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)
        :returns: The configured ZigZag indicator.
        """
        ...

    def γ(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: QuantConnect.Indicators.OptionPricingModelType = ..., iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Gamma:
        """
        Creates a new Gamma indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Gamma
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Gamma indicator for the specified symbol.
        """
        ...

    def δ(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: QuantConnect.Indicators.OptionPricingModelType = ..., iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Delta:
        """
        Creates a new Delta indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Delta
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Delta indicator for the specified symbol.
        """
        ...

    def θ(self, symbol: typing.Union[QuantConnect.Symbol, str], mirror_option: typing.Union[QuantConnect.Symbol, str] = None, risk_free_rate: typing.Optional[float] = None, dividend_yield: typing.Optional[float] = None, option_model: QuantConnect.Indicators.OptionPricingModelType = ..., iv_model: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Theta:
        """
        Creates a new Theta indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirror_option: The mirror option for parity calculation
        :param risk_free_rate: The risk free rate
        :param dividend_yield: The dividend yield
        :param option_model: The option pricing model used to estimate Theta
        :param iv_model: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Theta indicator for the specified symbol.
        """
        ...

    def ρ(self, symbol: typing.Union[QuantConnect.Symbol, str], mirrorOption: typing.Union[QuantConnect.Symbol, str] = None, riskFreeRate: typing.Optional[float] = None, dividendYield: typing.Optional[float] = None, optionModel: QuantConnect.Indicators.OptionPricingModelType = ..., ivModel: typing.Optional[QuantConnect.Indicators.OptionPricingModelType] = None, resolution: typing.Optional[QuantConnect.Resolution] = None) -> QuantConnect.Indicators.Rho:
        """
        Creates a new Rho indicator for the symbol The indicator will be automatically
        updated on the symbol's subscription resolution
        
        :param symbol: The option symbol whose values we want as an indicator
        :param mirrorOption: The mirror option for parity calculation
        :param riskFreeRate: The risk free rate
        :param dividendYield: The dividend yield
        :param optionModel: The option pricing model used to estimate Rho
        :param ivModel: The option pricing model used to estimate IV
        :param resolution: The desired resolution of the data
        :returns: A new Rho indicator for the specified symbol.
        """
        ...


class CandlestickPatterns(System.Object):
    """Provides helpers for using candlestick patterns"""

    def __init__(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> None:
        """
        Initializes a new instance of the CandlestickPatterns class
        
        :param algorithm: The algorithm instance
        """
        ...

    def abandoned_baby(self, symbol: typing.Union[QuantConnect.Symbol, str], penetration: float = 0.3, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.AbandonedBaby:
        """
        Creates a new Indicators.CandlestickPatterns.AbandonedBaby pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param penetration: Percentage of penetration of a candle within another candle
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def advance_block(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.AdvanceBlock:
        """
        Creates a new Indicators.CandlestickPatterns.AdvanceBlock pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def belt_hold(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.BeltHold:
        """
        Creates a new Indicators.CandlestickPatterns.BeltHold pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def breakaway(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Breakaway:
        """
        Creates a new Indicators.CandlestickPatterns.Breakaway pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def closing_marubozu(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ClosingMarubozu:
        """
        Creates a new Indicators.CandlestickPatterns.ClosingMarubozu pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def concealed_baby_swallow(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ConcealedBabySwallow:
        """
        Creates a new Indicators.CandlestickPatterns.ConcealedBabySwallow pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def counterattack(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Counterattack:
        """
        Creates a new Indicators.CandlestickPatterns.Counterattack pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def dark_cloud_cover(self, symbol: typing.Union[QuantConnect.Symbol, str], penetration: float = 0.5, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.DarkCloudCover:
        """
        Creates a new Indicators.CandlestickPatterns.DarkCloudCover pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param penetration: Percentage of penetration of a candle within another candle
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def doji(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Doji:
        """
        Creates a new Indicators.CandlestickPatterns.Doji pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def doji_star(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.DojiStar:
        """
        Creates a new Indicators.CandlestickPatterns.DojiStar pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def dragonfly_doji(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.DragonflyDoji:
        """
        Creates a new Indicators.CandlestickPatterns.DragonflyDoji pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def engulfing(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Engulfing:
        """
        Creates a new Indicators.CandlestickPatterns.Engulfing pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def evening_doji_star(self, symbol: typing.Union[QuantConnect.Symbol, str], penetration: float = 0.3, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.EveningDojiStar:
        """
        Creates a new Indicators.CandlestickPatterns.EveningDojiStar pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param penetration: Percentage of penetration of a candle within another candle
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def evening_star(self, symbol: typing.Union[QuantConnect.Symbol, str], penetration: float = 0.3, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.EveningStar:
        """
        Creates a new Indicators.CandlestickPatterns.EveningStar pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param penetration: Percentage of penetration of a candle within another candle
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def gap_side_by_side_white(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.GapSideBySideWhite:
        """
        Creates a new Indicators.CandlestickPatterns.GapSideBySideWhite pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def gravestone_doji(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.GravestoneDoji:
        """
        Creates a new Indicators.CandlestickPatterns.GravestoneDoji pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def hammer(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Hammer:
        """
        Creates a new Indicators.CandlestickPatterns.Hammer pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def hanging_man(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.HangingMan:
        """
        Creates a new Indicators.CandlestickPatterns.HangingMan pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def harami(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Harami:
        """
        Creates a new Indicators.CandlestickPatterns.Harami pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def harami_cross(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.HaramiCross:
        """
        Creates a new Indicators.CandlestickPatterns.HaramiCross pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def high_wave_candle(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.HighWaveCandle:
        """
        Creates a new Indicators.CandlestickPatterns.HighWaveCandle pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def hikkake(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Hikkake:
        """
        Creates a new Indicators.CandlestickPatterns.Hikkake pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def hikkake_modified(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.HikkakeModified:
        """
        Creates a new Indicators.CandlestickPatterns.HikkakeModified pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def homing_pigeon(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.HomingPigeon:
        """
        Creates a new Indicators.CandlestickPatterns.HomingPigeon pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def identical_three_crows(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.IdenticalThreeCrows:
        """
        Creates a new Indicators.CandlestickPatterns.IdenticalThreeCrows pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def in_neck(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.InNeck:
        """
        Creates a new Indicators.CandlestickPatterns.InNeck pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def inverted_hammer(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.InvertedHammer:
        """
        Creates a new Indicators.CandlestickPatterns.InvertedHammer pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def kicking(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Kicking:
        """
        Creates a new Indicators.CandlestickPatterns.Kicking pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def kicking_by_length(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.KickingByLength:
        """
        Creates a new Indicators.CandlestickPatterns.KickingByLength pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def ladder_bottom(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.LadderBottom:
        """
        Creates a new Indicators.CandlestickPatterns.LadderBottom pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def long_legged_doji(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.LongLeggedDoji:
        """
        Creates a new Indicators.CandlestickPatterns.LongLeggedDoji pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def long_line_candle(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.LongLineCandle:
        """
        Creates a new Indicators.CandlestickPatterns.LongLineCandle pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def marubozu(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Marubozu:
        """
        Creates a new Indicators.CandlestickPatterns.Marubozu pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def matching_low(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.MatchingLow:
        """
        Creates a new Indicators.CandlestickPatterns.MatchingLow pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def mat_hold(self, symbol: typing.Union[QuantConnect.Symbol, str], penetration: float = 0.5, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.MatHold:
        """
        Creates a new Indicators.CandlestickPatterns.MatHold pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param penetration: Percentage of penetration of a candle within another candle
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def morning_doji_star(self, symbol: typing.Union[QuantConnect.Symbol, str], penetration: float = 0.3, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.MorningDojiStar:
        """
        Creates a new Indicators.CandlestickPatterns.MorningDojiStar pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param penetration: Percentage of penetration of a candle within another candle
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def morning_star(self, symbol: typing.Union[QuantConnect.Symbol, str], penetration: float = 0.3, resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.MorningStar:
        """
        Creates a new Indicators.CandlestickPatterns.MorningStar pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param penetration: Percentage of penetration of a candle within another candle
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def on_neck(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.OnNeck:
        """
        Creates a new Indicators.CandlestickPatterns.OnNeck pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def piercing(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Piercing:
        """
        Creates a new Indicators.CandlestickPatterns.Piercing pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def rickshaw_man(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.RickshawMan:
        """
        Creates a new Indicators.CandlestickPatterns.RickshawMan pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def rise_fall_three_methods(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.RiseFallThreeMethods:
        """
        Creates a new Indicators.CandlestickPatterns.RiseFallThreeMethods pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def separating_lines(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.SeparatingLines:
        """
        Creates a new Indicators.CandlestickPatterns.SeparatingLines pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def shooting_star(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ShootingStar:
        """
        Creates a new Indicators.CandlestickPatterns.ShootingStar pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def short_line_candle(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ShortLineCandle:
        """
        Creates a new Indicators.CandlestickPatterns.ShortLineCandle pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def spinning_top(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.SpinningTop:
        """
        Creates a new Indicators.CandlestickPatterns.SpinningTop pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def stalled_pattern(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.StalledPattern:
        """
        Creates a new Indicators.CandlestickPatterns.StalledPattern pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def stick_sandwich(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.StickSandwich:
        """
        Creates a new Indicators.CandlestickPatterns.StickSandwich pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def takuri(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Takuri:
        """
        Creates a new Indicators.CandlestickPatterns.Takuri pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def tasuki_gap(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.TasukiGap:
        """
        Creates a new Indicators.CandlestickPatterns.TasukiGap pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def three_black_crows(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ThreeBlackCrows:
        """
        Creates a new Indicators.CandlestickPatterns.ThreeBlackCrows pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def three_inside(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ThreeInside:
        """
        Creates a new Indicators.CandlestickPatterns.ThreeInside pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def three_line_strike(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ThreeLineStrike:
        """
        Creates a new Indicators.CandlestickPatterns.ThreeLineStrike pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def three_outside(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ThreeOutside:
        """
        Creates a new Indicators.CandlestickPatterns.ThreeOutside pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def three_stars_in_south(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ThreeStarsInSouth:
        """
        Creates a new Indicators.CandlestickPatterns.ThreeStarsInSouth pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def three_white_soldiers(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.ThreeWhiteSoldiers:
        """
        Creates a new Indicators.CandlestickPatterns.ThreeWhiteSoldiers pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def thrusting(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Thrusting:
        """
        Creates a new Indicators.CandlestickPatterns.Thrusting pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def tristar(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.Tristar:
        """
        Creates a new Indicators.CandlestickPatterns.Tristar pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def two_crows(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.TwoCrows:
        """
        Creates a new Indicators.CandlestickPatterns.TwoCrows pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def unique_three_river(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.UniqueThreeRiver:
        """
        Creates a new Indicators.CandlestickPatterns.UniqueThreeRiver pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def up_down_gap_three_methods(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.UpDownGapThreeMethods:
        """
        Creates a new Indicators.CandlestickPatterns.UpDownGapThreeMethods pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...

    def upside_gap_two_crows(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, selector: typing.Callable[[QuantConnect.Data.IBaseData], QuantConnect.Data.Market.IBaseDataBar] = None) -> QuantConnect.Indicators.CandlestickPatterns.UpsideGapTwoCrows:
        """
        Creates a new Indicators.CandlestickPatterns.UpsideGapTwoCrows pattern indicator.
        The indicator will be automatically updated on the given resolution.
        
        :param symbol: The symbol whose pattern we seek
        :param resolution: The resolution.
        :param selector: Selects a value from the BaseData to send into the indicator, if null defaults to casting the input value to a TradeBar
        :returns: The pattern indicator for the requested symbol.
        """
        ...


class DollarVolumeUniverseDefinitions(System.Object):
    """Provides helpers for defining universes based on the daily dollar volume"""

    def __init__(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> None:
        """
        Initializes a new instance of the DollarVolumeUniverseDefinitions class
        
        :param algorithm: The algorithm instance, used for obtaining the default UniverseSettings
        """
        ...

    def top(self, count: int, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new coarse universe that contains the top count of stocks
        by daily dollar volume
        
        This method is deprecated. Use method `Universe.DollarVolume.Top(...)` instead
        
        :param count: The number of stock to select
        :param universe_settings: The settings for stocks added by this universe. Defaults to QCAlgorithm.UniverseSettings
        :returns: A new coarse universe for the top count of stocks by dollar volume.
        """
        warnings.warn("This method is deprecated. Use method `Universe.DollarVolume.Top(...)` instead", DeprecationWarning)


class _EventContainer(typing.Generic[QuantConnect_Algorithm__EventContainer_Callable, QuantConnect_Algorithm__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Algorithm__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Algorithm__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Algorithm__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


