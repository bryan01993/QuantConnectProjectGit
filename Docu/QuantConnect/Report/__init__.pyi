from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.Results
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Report
import QuantConnect.Securities
import System
import System.Collections.Generic

JsonConverter = typing.Any

QuantConnect_Report_NullResultValueTypeJsonConverter_T = typing.TypeVar("QuantConnect_Report_NullResultValueTypeJsonConverter_T")


class PointInTimePortfolio(System.Object):
    """Lightweight portfolio at a point in time"""

    class PointInTimeHolding(System.Object):
        """Holding of an asset at a point in time"""

        @property
        def symbol(self) -> QuantConnect.Symbol:
            """Symbol of the holding"""
            ...

        @property
        def holdings_value(self) -> float:
            """Value of the holdings of the asset. Can be negative if shorting an asset"""
            ...

        @property
        def quantity(self) -> float:
            """Quantity of the asset. Can be negative if shorting an asset"""
            ...

        @property
        def absolute_holdings_value(self) -> float:
            """Absolute value of the holdings."""
            ...

        @property
        def absolute_holdings_quantity(self) -> float:
            """Absolute value of the quantity"""
            ...

        def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], holdingsValue: float, holdingsQuantity: float) -> None:
            """
            Creates an instance of PointInTimeHolding, representing a holding at a given point in time
            
            :param symbol: Symbol of the holding
            :param holdingsValue: Value of the holding
            :param holdingsQuantity: Quantity of the holding
            """
            ...

    @property
    def time(self) -> datetime.datetime:
        """Time that this point in time portfolio is for"""
        ...

    @property
    def total_portfolio_value(self) -> float:
        """The total value of the portfolio. This is cash + absolute value of holdings"""
        ...

    @property
    def cash(self) -> float:
        """The cash the portfolio has"""
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """The order we just processed"""
        ...

    @property
    def holdings(self) -> System.Collections.Generic.List[QuantConnect.Report.PointInTimePortfolio.PointInTimeHolding]:
        """A list of holdings at the current moment in time"""
        ...

    @property
    def leverage(self) -> float:
        """Portfolio leverage - provided for convenience"""
        ...

    @overload
    def __init__(self, order: QuantConnect.Orders.Order, portfolio: QuantConnect.Securities.SecurityPortfolioManager) -> None:
        """
        Creates an instance of the PointInTimePortfolio object
        
        :param order: Order applied to the portfolio
        :param portfolio: Algorithm portfolio at a point in time
        """
        ...

    @overload
    def __init__(self, portfolio: QuantConnect.Report.PointInTimePortfolio, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Clones the provided portfolio
        
        :param portfolio: Portfolio
        :param time: Time
        """
        ...

    def no_empty_holdings(self) -> QuantConnect.Report.PointInTimePortfolio:
        """
        Filters out any empty holdings from the current Holdings
        
        :returns: Current object, but without empty holdings.
        """
        ...


class Metrics(System.Object):
    """Strategy metrics collection such as usage of funds and asset allocations"""

    @staticmethod
    @overload
    def asset_allocations(equity_curve: typing.Any, orders: System.Collections.Generic.List[QuantConnect.Orders.Order]) -> typing.Any:
        """
        Calculates the portfolio's asset allocation percentage over time. The series used to call this extension function should
        be the equity curve with the associated Order objects that go along with it.
        
        :param equity_curve: Equity curve series
        :param orders: Orders associated with the equity curve
        """
        ...

    @staticmethod
    @overload
    def asset_allocations(portfolios: System.Collections.Generic.List[QuantConnect.Report.PointInTimePortfolio]) -> typing.Any:
        """
        Calculates the asset allocation percentage over time.
        
        :param portfolios: Point in time portfolios
        :returns: Series keyed by Symbol containing the percentage allocated to that asset over time.
        """
        ...

    @staticmethod
    @overload
    def exposure(equity_curve: typing.Any, orders: System.Collections.Generic.List[QuantConnect.Orders.Order], direction: QuantConnect.Orders.OrderDirection) -> typing.Any:
        """
        Strategy long/short exposure by asset class
        
        :param equity_curve: Equity curve
        :param orders: Orders of the strategy
        :param direction: Long or short
        :returns: Frame keyed by SecurityType and OrderDirection. Returns a Frame of exposure per asset per direction over time.
        """
        ...

    @staticmethod
    @overload
    def exposure(portfolios: System.Collections.Generic.List[QuantConnect.Report.PointInTimePortfolio], direction: QuantConnect.Orders.OrderDirection) -> typing.Any:
        """
        Strategy long/short exposure by asset class
        
        :param portfolios: Point in time portfolios
        :param direction: Long or short
        :returns: Frame keyed by SecurityType and OrderDirection. Returns a Frame of exposure per asset per direction over time.
        """
        ...

    @staticmethod
    @overload
    def leverage_utilization(equity_curve: typing.Any, orders: System.Collections.Generic.List[QuantConnect.Orders.Order]) -> typing.Any:
        """
        Calculates the leverage used from trades. The series used to call this extension function should
        be the equity curve with the associated Order objects that go along with it.
        
        :param equity_curve: Equity curve series
        :param orders: Orders associated with the equity curve
        :returns: Leverage utilization over time.
        """
        ...

    @staticmethod
    @overload
    def leverage_utilization(portfolios: System.Collections.Generic.List[QuantConnect.Report.PointInTimePortfolio]) -> typing.Any:
        """
        Gets the leverage utilization from a list of PointInTimePortfolio
        
        :param portfolios: Point in time portfolios
        :returns: Series of leverage utilization.
        """
        ...


class OrderTypeNormalizingJsonConverter(JsonConverter):
    """
    Normalizes the "Type" field to a value that will allow for
    successful deserialization in the OrderJsonConverter class.
    """

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determine if this Converter can convert a given object type
        
        :param object_type: Object type to convert
        :returns: True if assignable from Order.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Read Json and convert
        
        :returns: Resulting Order.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Write Json; Not implemented"""
        ...


class DeedleUtil(System.Object):
    """Utility extension methods for Deedle series/frames"""

    @staticmethod
    def cumulative_max(input: typing.Any) -> typing.Any:
        """Calculates the cumulative max of the series. This is equal to the python pandas method: `df.cummax()`."""
        ...

    @staticmethod
    def cumulative_product(input: typing.Any) -> typing.Any:
        """
        Calculates the cumulative product of the series. This is equal to the python pandas method: `df.cumprod()`
        
        :param input: Input series
        :returns: Cumulative product.
        """
        ...

    @staticmethod
    def cumulative_returns(input: typing.Any) -> typing.Any:
        """
        Calculates the cumulative returns series of the given input equity curve
        
        :param input: Equity curve series
        :returns: Cumulative returns over time.
        """
        ...

    @staticmethod
    def cumulative_sum(input: typing.Any) -> typing.Any:
        """
        Calculates the cumulative sum for the given series
        
        :param input: Series to calculate cumulative sum for
        :returns: Cumulative sum in series form.
        """
        ...

    @staticmethod
    def drop_sparse_columns_all(frame: typing.Any) -> typing.Any:
        """
        Drops sparse columns only if every value is `missing` in the column
        
        :param frame: Data Frame
        :returns: new Frame with sparse columns dropped.
        """
        ...

    @staticmethod
    def drop_sparse_rows_all(frame: typing.Any) -> typing.Any:
        """
        Drops sparse rows if and only if every value is `missing` in the Frame
        
        :param frame: Data Frame
        :returns: new Frame with sparse rows dropped.
        """
        ...

    @staticmethod
    def percent_change(input: typing.Any) -> typing.Any:
        """
        Calculates the percentage change from the previous value to the current
        
        :param input: Series to calculate percentage change for
        :returns: Percentage change in series form.
        """
        ...

    @staticmethod
    def total_returns(input: typing.Any) -> float:
        """
        Calculates the total returns over a period of time for the given input
        
        :param input: Equity curve series
        :returns: Total returns over time.
        """
        ...


class Rolling(System.Object):
    """Rolling window functions"""

    @staticmethod
    def beta(performance_points: System.Collections.Generic.SortedList[datetime.datetime, float], benchmark_points: System.Collections.Generic.SortedList[datetime.datetime, float], window_size: int = 132) -> typing.Any:
        """
        Calculate the rolling beta with the given window size (in days)
        
        :param performance_points: The performance points you want to measure beta for
        :param benchmark_points: The benchmark/points you want to calculate beta with
        :param window_size: Days/window to lookback
        :returns: Rolling beta.
        """
        ...

    @staticmethod
    def sharpe(equity_curve: typing.Any, months: int, trading_day_per_year: int) -> typing.Any:
        """
        Get the rolling sharpe of the given series with a lookback of . The risk free rate is adjustable
        
        :param equity_curve: Equity curve to calculate rolling sharpe for
        :param months: Number of months to calculate the rolling period for
        :param trading_day_per_year: The number of trading days per year to increase result of Annual statistics
        :returns: Rolling sharpe ratio.
        """
        ...


class CrisisEvent(Enum):
    """Crisis Events"""

    DOT_COM = 0
    """DotCom bubble - https://en.wikipedia.org/wiki/Dot-com_bubble (0)"""

    SEPTEMBER_ELEVENTH = 1
    """September 11, 2001 attacks - https://en.wikipedia.org/wiki/September_11_attacks (1)"""

    US_HOUSING_BUBBLE_2003 = 2
    """United States housing bubble - https://en.wikipedia.org/wiki/United_States_housing_bubble (2)"""

    GLOBAL_FINANCIAL_CRISIS = 3
    """https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308 (3)"""

    FLASH_CRASH = 4
    """The flash crash of 2010 - https://en.wikipedia.org/wiki/2010_Flash_Crash (4)"""

    FUKUSHIMA_MELTDOWN = 5
    """Fukushima nuclear power plant meltdown - https://en.wikipedia.org/wiki/Fukushima_Daiichi_nuclear_disaster (5)"""

    US_DOWNGRADE_EUROPEAN_DEBT = 6
    """
    United States credit rating downgrade - https://en.wikipedia.org/wiki/United_States_federal_government_credit-rating_downgrades
    European debt crisis - https://en.wikipedia.org/wiki/European_debt_crisis (6)
    """

    EUROZONE_SEPTEMBER_2012 = 7
    """European debt crisis - https://en.wikipedia.org/wiki/European_debt_crisis (7)"""

    EUROZONE_OCTOBER_2014 = 8
    """European debt crisis - https://en.wikipedia.org/wiki/European_debt_crisis (8)"""

    MARKET_SELL_OFF_2015 = 9
    """2015-2016 market sell off https://en.wikipedia.org/wiki/2015%E2%80%9316_stock_market_selloff (9)"""

    RECOVERY = 10
    """Crisis recovery (2010 - 2012) (10)"""

    NEW_NORMAL = 11
    """2014 - 2019 market performance (11)"""

    COVID_19 = 12
    """COVID-19 pandemic market crash (12)"""

    POST_COVID_RUN_UP = 13
    """Post COVID-19 recovery (13)"""

    MEME_SEASON = 14
    """Meme-craze era like GME, AMC, and DOGE (14)"""

    RUSSIA_INVADES_UKRAINE = 15
    """Russia invased Ukraine (15)"""

    AI_BOOM = 16
    """Artificial intelligence boom (16)"""


class Crisis(System.Object):
    """Crisis events utility class"""

    EVENTS: System.Collections.Generic.Dictionary[QuantConnect.Report.CrisisEvent, QuantConnect.Report.Crisis] = ...
    """Crisis events and pre-defined values"""

    @property
    def start(self) -> datetime.datetime:
        """Start of the crisis event"""
        ...

    @property
    def end(self) -> datetime.datetime:
        """End of the crisis event"""
        ...

    @property
    def name(self) -> str:
        """Name of the crisis"""
        ...

    def __init__(self, name: str, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Creates a new crisis instance with the given name and start/end date.
        
        :param name: Name of the crisis
        :param start: Start date of the crisis
        :param end: End date of the crisis
        """
        ...

    @staticmethod
    def from_crisis(crisis_event: QuantConnect.Report.CrisisEvent) -> QuantConnect.Report.Crisis:
        """
        Returns a pre-defined crisis event
        
        :param crisis_event: Crisis Event
        :returns: Pre-defined crisis event.
        """
        ...

    @overload
    def to_string(self) -> str:
        """Converts instance to string using the dates in the instance as start/end dates"""
        ...

    @overload
    def to_string(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> str:
        """
        Converts instance to string using the provided dates
        
        :param start: Start date
        :param end: End date
        """
        ...


class ResultsUtil(System.Object):
    """Utility methods for dealing with the Result objects"""

    @staticmethod
    def benchmark_points(result: QuantConnect.Result) -> System.Collections.Generic.SortedList[datetime.datetime, float]:
        """
        Gets the points of the benchmark
        
        :param result: Backtesting or live results
        :returns: Sorted list keyed by date and value.
        """
        ...

    @staticmethod
    def equity_points(result: QuantConnect.Result, series_name: str = None) -> System.Collections.Generic.SortedList[datetime.datetime, float]:
        """
        Get the points, from the Series name given, in Strategy Equity chart
        
        :param result: Result object to extract the chart points
        :param series_name: Series name from which the points will be extracted. By default is Equity series
        """
        ...


class DrawdownPeriod(System.Object):
    """Represents a period of time where the drawdown ranks amongst the top N drawdowns."""

    @property
    def start(self) -> datetime.datetime:
        """Start of the drawdown period"""
        ...

    @property
    def end(self) -> datetime.datetime:
        """End of the drawdown period"""
        ...

    @property
    def peak_to_trough(self) -> float:
        """Loss in percent from peak to trough"""
        ...

    @property
    def drawdown(self) -> float:
        """Loss in percent from peak to trough - Alias for PeakToTrough"""
        ...

    def __init__(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], drawdown: float) -> None:
        """
        Creates an instance with the given start, end, and drawdown
        
        :param start: Start of the drawdown period
        :param end: End of the drawdown period
        :param drawdown: Max drawdown of the period
        """
        ...


class DrawdownCollection(System.Object):
    """Collection of drawdowns for the given period marked by start and end date"""

    @property
    def start(self) -> datetime.datetime:
        """Starting time of the drawdown collection"""
        ...

    @property
    def end(self) -> datetime.datetime:
        """Ending time of the drawdown collection"""
        ...

    @property
    def periods(self) -> int:
        """
        Number of periods to take into consideration for the top N drawdown periods.
        This will be the number of items contained in the Drawdowns collection.
        """
        ...

    @property
    def drawdowns(self) -> System.Collections.Generic.List[QuantConnect.Report.DrawdownPeriod]:
        """Worst drawdowns encountered"""
        ...

    @overload
    def __init__(self, periods: int) -> None:
        """Creates an instance with a default collection (no items) and the top N worst drawdowns"""
        ...

    @overload
    def __init__(self, strategySeries: typing.Any, periods: int) -> None:
        """
        Creates an instance from the given drawdowns and the top N worst drawdowns
        
        :param strategySeries: Equity curve with both live and backtesting merged
        :param periods: Periods this collection contains
        """
        ...

    @staticmethod
    def from_result(backtest_result: QuantConnect.Packets.BacktestResult = None, live_result: QuantConnect.Packets.LiveResult = None, periods: int = 5) -> QuantConnect.Report.DrawdownCollection:
        """
        Generate a new instance of DrawdownCollection from backtest and live Result derived instances
        
        :param backtest_result: Backtest result packet
        :param live_result: Live result packet
        :param periods: Top N drawdown periods to get
        :returns: DrawdownCollection instance.
        """
        ...

    @staticmethod
    def get_drawdown_periods(curve: typing.Any, periods: int = 5) -> System.Collections.Generic.IEnumerable[QuantConnect.Report.DrawdownPeriod]:
        """
        Gets the given drawdown periods from the equity curve and the set periods
        
        :param curve: Equity curve
        :param periods: Top N drawdown periods to get
        :returns: Enumerable of DrawdownPeriod.
        """
        ...

    @staticmethod
    def get_top_worst_drawdowns(curve: typing.Any, periods: int) -> typing.Any:
        """
        Gets the top N worst drawdowns and associated statistics.
        Returns a Frame with the following keys: "duration", "cumulativeMax", "drawdown"
        
        :param curve: Equity curve
        :param periods: Top N worst periods. If this is greater than the results, we retrieve all the items instead
        :returns: Frame with the following keys: "duration", "cumulativeMax", "drawdown".
        """
        ...

    @staticmethod
    def get_underwater(curve: typing.Any) -> typing.Any:
        """
        Gets the underwater plot for the provided curve.
        Data is expected to be the concatenated output of ResultsUtil.EquityPoints.
        
        :param curve: Equity curve
        """
        ...

    @staticmethod
    def get_underwater_frame(curve: typing.Any) -> typing.Any:
        """
        Gets all the data associated with the underwater plot and everything used to generate it.
        Note that you should instead use GetUnderwater(Series{DateTime, double}) if you
        want to just generate an underwater plot. This is internally used to get the top N worst drawdown periods.
        
        :param curve: Equity curve
        :returns: Frame containing the following keys: "returns", "cumulativeMax", "drawdown".
        """
        ...

    @staticmethod
    def normalize_results(backtest_result: QuantConnect.Packets.BacktestResult, live_result: QuantConnect.Packets.LiveResult) -> typing.Any:
        """
        Normalizes the Series used to calculate the drawdown plots and charts
        
        :param backtest_result: Backtest result packet
        :param live_result: Live result packet
        """
        ...


class NullResultValueTypeJsonConverter(typing.Generic[QuantConnect_Report_NullResultValueTypeJsonConverter_T], JsonConverter):
    """
    Removes null values in the Result object's x,y values so that
    deserialization can occur without exceptions.
    """

    def __init__(self) -> None:
        """Initialize a new instance of NullResultValueTypeJsonConverter{T}"""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determine if this converter can convert a given type
        
        :param object_type: Object type to convert
        :returns: Always true.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Read Json for conversion
        
        :returns: Resulting object.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Write Json; Not implemented"""
        ...


class Report(System.Object):
    """Report class"""

    STATISTICS_FILE_NAME: str = "report-statistics.json"
    """File name for statistics"""

    def __init__(self, name: str, description: str, version: str, backtest: QuantConnect.Packets.BacktestResult, live: QuantConnect.Packets.LiveResult, pointInTimePortfolioDestination: str = None, cssOverride: str = None, htmlCustom: str = None) -> None:
        """
        Create beautiful HTML and PDF Reports based on backtest and live data.
        
        :param name: Name of the strategy
        :param description: Description of the strategy
        :param version: Version number of the strategy
        :param backtest: Backtest result object
        :param live: Live result object
        :param pointInTimePortfolioDestination: Point in time portfolio json output base filename
        :param cssOverride: CSS file that overrides some of the default rules defined in report.css
        :param htmlCustom: Custom HTML file to replace the default template
        """
        ...

    def compile(self, html: typing.Optional[str], report_statistics: typing.Optional[str]) -> typing.Union[None, str, str]:
        """Compile the backtest data into a report"""
        ...

    @staticmethod
    def get_regex_in_input(pattern: str, input: str) -> str:
        """
        Gets the regex pattern in the given input string
        
        :param pattern: Regex pattern to be find the input string
        :param input: Input string that may contain the regex pattern
        :returns: The regex pattern in the input string if found. Otherwise, null.
        """
        ...


class PortfolioLooperAlgorithm(QuantConnect.Algorithm.QCAlgorithm):
    """Fake algorithm that initializes portfolio and algorithm securities. Never ran."""

    def __init__(self, startingCash: float, orders: System.Collections.Generic.IEnumerable[QuantConnect.Orders.Order], algorithmConfiguration: QuantConnect.AlgorithmConfiguration = None) -> None:
        """
        Initialize an instance of PortfolioLooperAlgorithm
        
        :param startingCash: Starting algorithm cash
        :param orders: Orders to use
        :param algorithmConfiguration: Optional parameter to override default algorithm configuration
        """
        ...

    def from_orders(self, orders: System.Collections.Generic.IEnumerable[QuantConnect.Orders.Order]) -> None:
        """
        Initializes all the proper Securities from the orders provided by the user
        
        :param orders: Orders to use
        """
        ...

    def initialize(self) -> None:
        """Initialize this algorithm"""
        ...


class PortfolioLooper(System.Object, System.IDisposable):
    """
    Runs LEAN to calculate the portfolio at a given time from Order objects.
    Generates and returns PointInTimePortfolio objects that represents
    the holdings and other miscellaneous metrics at a point in time by reprocessing the orders
    as they were filled.
    """

    @property
    def algorithm(self) -> QuantConnect.Report.PortfolioLooperAlgorithm:
        """
        QCAlgorithm derived class that sets up internal data feeds for
        use with crypto and forex data, as well as managing the SecurityPortfolioManager
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @staticmethod
    def from_orders(equity_curve: typing.Any, orders: System.Collections.Generic.IEnumerable[QuantConnect.Orders.Order], algorithm_configuration: QuantConnect.AlgorithmConfiguration = None, live_series: bool = False) -> System.Collections.Generic.IEnumerable[QuantConnect.Report.PointInTimePortfolio]:
        """
        Gets the point in time portfolio over multiple deployments
        
        :param equity_curve: Equity curve series
        :param orders: Orders
        :param algorithm_configuration: Optional parameter to override default algorithm configuration
        :param live_series: Equity curve series originates from LiveResult
        :returns: Enumerable of PointInTimePortfolio.
        """
        ...

    @staticmethod
    def get_history(symbols: System.Collections.Generic.List[QuantConnect.Symbol], start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the given symbols from the  to the
        
        :param symbols: Symbols to request history for
        :param start: Start date of history request
        :param end: End date of history request
        :param resolution: Resolution of history request
        :returns: Enumerable of slices.
        """
        ...


class MockDataFeed(System.Object, QuantConnect.Lean.Engine.DataFeeds.IDataFeed):
    """Fake IDataFeed"""

    @property
    def is_active(self) -> bool:
        """Bool if the feed is active"""
        ...

    def create_subscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Create Subscription
        
        :param request: Subscription request to use
        :returns: Always null.
        """
        ...

    def exit(self) -> None:
        """DataFeed Exit"""
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider, subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, data_feed_time_provider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, data_channel_provider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        """
        Initialize the data feed
        This implementation does nothing
        """
        ...

    def remove_subscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Remove Subscription; Not implemented
        
        :param subscription: Subscription to remove
        """
        ...


