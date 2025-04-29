from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Generic


class TradeDirection(Enum):
    """Direction of a trade"""

    LONG = 0
    """Long direction (0)"""

    SHORT = 1
    """Short direction (1)"""


class Trade(System.Object):
    """Represents a closed trade"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """The symbol of the traded instrument"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def entry_time(self) -> datetime.datetime:
        """The date and time the trade was opened"""
        ...

    @property.setter
    def entry_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def entry_price(self) -> float:
        """The price at which the trade was opened (or the average price if multiple entries)"""
        ...

    @property.setter
    def entry_price(self, value: float) -> None:
        ...

    @property
    def direction(self) -> QuantConnect.Statistics.TradeDirection:
        """The direction of the trade (Long or Short)"""
        ...

    @property.setter
    def direction(self, value: QuantConnect.Statistics.TradeDirection) -> None:
        ...

    @property
    def quantity(self) -> float:
        """The total unsigned quantity of the trade"""
        ...

    @property.setter
    def quantity(self, value: float) -> None:
        ...

    @property
    def exit_time(self) -> datetime.datetime:
        """The date and time the trade was closed"""
        ...

    @property.setter
    def exit_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def exit_price(self) -> float:
        """The price at which the trade was closed (or the average price if multiple exits)"""
        ...

    @property.setter
    def exit_price(self, value: float) -> None:
        ...

    @property
    def profit_loss(self) -> float:
        """The gross profit/loss of the trade (as account currency)"""
        ...

    @property.setter
    def profit_loss(self, value: float) -> None:
        ...

    @property
    def total_fees(self) -> float:
        """The total fees associated with the trade (always positive value) (as account currency)"""
        ...

    @property.setter
    def total_fees(self, value: float) -> None:
        ...

    @property
    def mae(self) -> float:
        """The Maximum Adverse Excursion (as account currency)"""
        ...

    @property.setter
    def mae(self, value: float) -> None:
        ...

    @property
    def mfe(self) -> float:
        """The Maximum Favorable Excursion (as account currency)"""
        ...

    @property.setter
    def mfe(self, value: float) -> None:
        ...

    @property
    def duration(self) -> datetime.timedelta:
        """Returns the duration of the trade"""
        ...

    @property
    def end_trade_drawdown(self) -> float:
        """Returns the amount of profit given back before the trade was closed"""
        ...

    @property
    def is_win(self) -> bool:
        """Returns whether the trade was profitable (is a win) or not (a loss)"""
        ...

    @property.setter
    def is_win(self, value: bool) -> None:
        ...


class TradeStatistics(System.Object):
    """The TradeStatistics class represents a set of statistics calculated from a list of closed trades"""

    @property
    def start_date_time(self) -> typing.Optional[datetime.datetime]:
        """The entry date/time of the first trade"""
        ...

    @property.setter
    def start_date_time(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def end_date_time(self) -> typing.Optional[datetime.datetime]:
        """The exit date/time of the last trade"""
        ...

    @property.setter
    def end_date_time(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def total_number_of_trades(self) -> int:
        """The total number of trades"""
        ...

    @property.setter
    def total_number_of_trades(self, value: int) -> None:
        ...

    @property
    def number_of_winning_trades(self) -> int:
        """The total number of winning trades"""
        ...

    @property.setter
    def number_of_winning_trades(self, value: int) -> None:
        ...

    @property
    def number_of_losing_trades(self) -> int:
        """The total number of losing trades"""
        ...

    @property.setter
    def number_of_losing_trades(self, value: int) -> None:
        ...

    @property
    def total_profit_loss(self) -> float:
        """The total profit/loss for all trades (as symbol currency)"""
        ...

    @property.setter
    def total_profit_loss(self, value: float) -> None:
        ...

    @property
    def total_profit(self) -> float:
        """The total profit for all winning trades (as symbol currency)"""
        ...

    @property.setter
    def total_profit(self, value: float) -> None:
        ...

    @property
    def total_loss(self) -> float:
        """The total loss for all losing trades (as symbol currency)"""
        ...

    @property.setter
    def total_loss(self, value: float) -> None:
        ...

    @property
    def largest_profit(self) -> float:
        """The largest profit in a single trade (as symbol currency)"""
        ...

    @property.setter
    def largest_profit(self, value: float) -> None:
        ...

    @property
    def largest_loss(self) -> float:
        """The largest loss in a single trade (as symbol currency)"""
        ...

    @property.setter
    def largest_loss(self, value: float) -> None:
        ...

    @property
    def average_profit_loss(self) -> float:
        """The average profit/loss (a.k.a. Expectancy or Average Trade) for all trades (as symbol currency)"""
        ...

    @property.setter
    def average_profit_loss(self, value: float) -> None:
        ...

    @property
    def average_profit(self) -> float:
        """The average profit for all winning trades (as symbol currency)"""
        ...

    @property.setter
    def average_profit(self, value: float) -> None:
        ...

    @property
    def average_loss(self) -> float:
        """The average loss for all winning trades (as symbol currency)"""
        ...

    @property.setter
    def average_loss(self, value: float) -> None:
        ...

    @property
    def average_trade_duration(self) -> datetime.timedelta:
        """The average duration for all trades"""
        ...

    @property.setter
    def average_trade_duration(self, value: datetime.timedelta) -> None:
        ...

    @property
    def average_winning_trade_duration(self) -> datetime.timedelta:
        """The average duration for all winning trades"""
        ...

    @property.setter
    def average_winning_trade_duration(self, value: datetime.timedelta) -> None:
        ...

    @property
    def average_losing_trade_duration(self) -> datetime.timedelta:
        """The average duration for all losing trades"""
        ...

    @property.setter
    def average_losing_trade_duration(self, value: datetime.timedelta) -> None:
        ...

    @property
    def median_trade_duration(self) -> datetime.timedelta:
        """The median duration for all trades"""
        ...

    @property.setter
    def median_trade_duration(self, value: datetime.timedelta) -> None:
        ...

    @property
    def median_winning_trade_duration(self) -> datetime.timedelta:
        """The median duration for all winning trades"""
        ...

    @property.setter
    def median_winning_trade_duration(self, value: datetime.timedelta) -> None:
        ...

    @property
    def median_losing_trade_duration(self) -> datetime.timedelta:
        """The median duration for all losing trades"""
        ...

    @property.setter
    def median_losing_trade_duration(self, value: datetime.timedelta) -> None:
        ...

    @property
    def max_consecutive_winning_trades(self) -> int:
        """The maximum number of consecutive winning trades"""
        ...

    @property.setter
    def max_consecutive_winning_trades(self, value: int) -> None:
        ...

    @property
    def max_consecutive_losing_trades(self) -> int:
        """The maximum number of consecutive losing trades"""
        ...

    @property.setter
    def max_consecutive_losing_trades(self, value: int) -> None:
        ...

    @property
    def profit_loss_ratio(self) -> float:
        """The ratio of the average profit per trade to the average loss per trade"""
        ...

    @property.setter
    def profit_loss_ratio(self, value: float) -> None:
        ...

    @property
    def win_loss_ratio(self) -> float:
        """The ratio of the number of winning trades to the number of losing trades"""
        ...

    @property.setter
    def win_loss_ratio(self, value: float) -> None:
        ...

    @property
    def win_rate(self) -> float:
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @property.setter
    def win_rate(self, value: float) -> None:
        ...

    @property
    def loss_rate(self) -> float:
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @property.setter
    def loss_rate(self, value: float) -> None:
        ...

    @property
    def average_mae(self) -> float:
        """The average Maximum Adverse Excursion for all trades"""
        ...

    @property.setter
    def average_mae(self, value: float) -> None:
        ...

    @property
    def average_mfe(self) -> float:
        """The average Maximum Favorable Excursion for all trades"""
        ...

    @property.setter
    def average_mfe(self, value: float) -> None:
        ...

    @property
    def largest_mae(self) -> float:
        """The largest Maximum Adverse Excursion in a single trade (as symbol currency)"""
        ...

    @property.setter
    def largest_mae(self, value: float) -> None:
        ...

    @property
    def largest_mfe(self) -> float:
        """The largest Maximum Favorable Excursion in a single trade (as symbol currency)"""
        ...

    @property.setter
    def largest_mfe(self, value: float) -> None:
        ...

    @property
    def maximum_closed_trade_drawdown(self) -> float:
        """The maximum closed-trade drawdown for all trades (as symbol currency)"""
        ...

    @property.setter
    def maximum_closed_trade_drawdown(self, value: float) -> None:
        ...

    @property
    def maximum_intra_trade_drawdown(self) -> float:
        """The maximum intra-trade drawdown for all trades (as symbol currency)"""
        ...

    @property.setter
    def maximum_intra_trade_drawdown(self, value: float) -> None:
        ...

    @property
    def profit_loss_standard_deviation(self) -> float:
        """The standard deviation of the profits/losses for all trades (as symbol currency)"""
        ...

    @property.setter
    def profit_loss_standard_deviation(self, value: float) -> None:
        ...

    @property
    def profit_loss_downside_deviation(self) -> float:
        """The downside deviation of the profits/losses for all trades (as symbol currency)"""
        ...

    @property.setter
    def profit_loss_downside_deviation(self, value: float) -> None:
        ...

    @property
    def profit_factor(self) -> float:
        """The ratio of the total profit to the total loss"""
        ...

    @property.setter
    def profit_factor(self, value: float) -> None:
        ...

    @property
    def sharpe_ratio(self) -> float:
        """The ratio of the average profit/loss to the standard deviation"""
        ...

    @property.setter
    def sharpe_ratio(self, value: float) -> None:
        ...

    @property
    def sortino_ratio(self) -> float:
        """The ratio of the average profit/loss to the downside deviation"""
        ...

    @property.setter
    def sortino_ratio(self, value: float) -> None:
        ...

    @property
    def profit_to_max_drawdown_ratio(self) -> float:
        """The ratio of the total profit/loss to the maximum closed trade drawdown"""
        ...

    @property.setter
    def profit_to_max_drawdown_ratio(self, value: float) -> None:
        ...

    @property
    def maximum_end_trade_drawdown(self) -> float:
        """The maximum amount of profit given back by a single trade before exit (as symbol currency)"""
        ...

    @property.setter
    def maximum_end_trade_drawdown(self, value: float) -> None:
        ...

    @property
    def average_end_trade_drawdown(self) -> float:
        """The average amount of profit given back by all trades before exit (as symbol currency)"""
        ...

    @property.setter
    def average_end_trade_drawdown(self, value: float) -> None:
        ...

    @property
    def maximum_drawdown_duration(self) -> datetime.timedelta:
        """The maximum amount of time to recover from a drawdown (longest time between new equity highs or peaks)"""
        ...

    @property.setter
    def maximum_drawdown_duration(self, value: datetime.timedelta) -> None:
        ...

    @property
    def total_fees(self) -> float:
        """The sum of fees for all trades"""
        ...

    @property.setter
    def total_fees(self, value: float) -> None:
        ...

    @overload
    def __init__(self, trades: System.Collections.Generic.IEnumerable[QuantConnect.Statistics.Trade]) -> None:
        """
        Initializes a new instance of the TradeStatistics class
        
        :param trades: The list of closed trades
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the TradeStatistics class"""
        ...


class PortfolioStatistics(System.Object):
    """The PortfolioStatistics class represents a set of statistics calculated from equity and benchmark samples"""

    @property
    def average_win_rate(self) -> float:
        """The average rate of return for winning trades"""
        ...

    @property.setter
    def average_win_rate(self, value: float) -> None:
        ...

    @property
    def average_loss_rate(self) -> float:
        """The average rate of return for losing trades"""
        ...

    @property.setter
    def average_loss_rate(self, value: float) -> None:
        ...

    @property
    def profit_loss_ratio(self) -> float:
        """The ratio of the average win rate to the average loss rate"""
        ...

    @property.setter
    def profit_loss_ratio(self, value: float) -> None:
        ...

    @property
    def win_rate(self) -> float:
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @property.setter
    def win_rate(self, value: float) -> None:
        ...

    @property
    def loss_rate(self) -> float:
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @property.setter
    def loss_rate(self, value: float) -> None:
        ...

    @property
    def expectancy(self) -> float:
        """The expected value of the rate of return"""
        ...

    @property.setter
    def expectancy(self, value: float) -> None:
        ...

    @property
    def start_equity(self) -> float:
        """Initial Equity Total Value"""
        ...

    @property.setter
    def start_equity(self, value: float) -> None:
        ...

    @property
    def end_equity(self) -> float:
        """Final Equity Total Value"""
        ...

    @property.setter
    def end_equity(self, value: float) -> None:
        ...

    @property
    def compounding_annual_return(self) -> float:
        """Annual compounded returns statistic based on the final-starting capital and years."""
        ...

    @property.setter
    def compounding_annual_return(self, value: float) -> None:
        ...

    @property
    def drawdown(self) -> float:
        """Drawdown maximum percentage."""
        ...

    @property.setter
    def drawdown(self, value: float) -> None:
        ...

    @property
    def total_net_profit(self) -> float:
        """The total net profit percentage."""
        ...

    @property.setter
    def total_net_profit(self, value: float) -> None:
        ...

    @property
    def sharpe_ratio(self) -> float:
        """Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk."""
        ...

    @property.setter
    def sharpe_ratio(self, value: float) -> None:
        ...

    @property
    def probabilistic_sharpe_ratio(self) -> float:
        """
        Probabilistic Sharpe Ratio is a probability measure associated with the Sharpe ratio.
        It informs us of the probability that the estimated Sharpe ratio is greater than a chosen benchmark
        """
        ...

    @property.setter
    def probabilistic_sharpe_ratio(self, value: float) -> None:
        ...

    @property
    def sortino_ratio(self) -> float:
        """Sortino ratio with respect to risk free rate: measures excess of return per unit of downside risk."""
        ...

    @property.setter
    def sortino_ratio(self, value: float) -> None:
        ...

    @property
    def alpha(self) -> float:
        """Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns."""
        ...

    @property.setter
    def alpha(self, value: float) -> None:
        ...

    @property
    def beta(self) -> float:
        """Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance"""
        ...

    @property.setter
    def beta(self, value: float) -> None:
        ...

    @property
    def annual_standard_deviation(self) -> float:
        """Annualized standard deviation"""
        ...

    @property.setter
    def annual_standard_deviation(self, value: float) -> None:
        ...

    @property
    def annual_variance(self) -> float:
        """Annualized variance statistic calculation using the daily performance variance and trading days per year."""
        ...

    @property.setter
    def annual_variance(self, value: float) -> None:
        ...

    @property
    def information_ratio(self) -> float:
        """Information ratio - risk adjusted return"""
        ...

    @property.setter
    def information_ratio(self, value: float) -> None:
        ...

    @property
    def tracking_error(self) -> float:
        """Tracking error volatility (TEV) statistic - a measure of how closely a portfolio follows the index to which it is benchmarked"""
        ...

    @property.setter
    def tracking_error(self, value: float) -> None:
        ...

    @property
    def treynor_ratio(self) -> float:
        """Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk"""
        ...

    @property.setter
    def treynor_ratio(self, value: float) -> None:
        ...

    @property
    def portfolio_turnover(self) -> float:
        """The average Portfolio Turnover"""
        ...

    @property.setter
    def portfolio_turnover(self, value: float) -> None:
        ...

    @property
    def value_at_risk_99(self) -> float:
        """
        The 1-day VaR for the portfolio, using the Variance-covariance approach.
        Assumes a 99% confidence level, 1 year lookback period, and that the returns are normally distributed.
        """
        ...

    @property.setter
    def value_at_risk_99(self, value: float) -> None:
        ...

    @property
    def value_at_risk_95(self) -> float:
        """
        The 1-day VaR for the portfolio, using the Variance-covariance approach.
        Assumes a 95% confidence level, 1 year lookback period, and that the returns are normally distributed.
        """
        ...

    @property.setter
    def value_at_risk_95(self, value: float) -> None:
        ...

    @overload
    def __init__(self, profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], equity: System.Collections.Generic.SortedDictionary[datetime.datetime, float], portfolioTurnover: System.Collections.Generic.SortedDictionary[datetime.datetime, float], listPerformance: System.Collections.Generic.List[float], listBenchmark: System.Collections.Generic.List[float], startingCapital: float, riskFreeInterestRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, tradingDaysPerYear: int, winCount: typing.Optional[int] = None, lossCount: typing.Optional[int] = None) -> None:
        """
        Initializes a new instance of the PortfolioStatistics class
        
        :param profitLoss: Trade record of profits and losses
        :param equity: The list of daily equity values
        :param portfolioTurnover: The algorithm portfolio turnover
        :param listPerformance: The list of algorithm performance values
        :param listBenchmark: The list of benchmark values
        :param startingCapital: The algorithm starting capital
        :param riskFreeInterestRateModel: The risk free interest rate model to use
        :param tradingDaysPerYear: The number of trading days per year
        :param winCount: The number of wins, including ITM options with profitLoss less than 0. If this and  are null, they will be calculated from
        :param lossCount: The number of losses
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the PortfolioStatistics class"""
        ...


class AlgorithmPerformance(System.Object):
    """The AlgorithmPerformance class is a wrapper for TradeStatistics and PortfolioStatistics"""

    @property
    def trade_statistics(self) -> QuantConnect.Statistics.TradeStatistics:
        """The algorithm statistics on closed trades"""
        ...

    @property.setter
    def trade_statistics(self, value: QuantConnect.Statistics.TradeStatistics) -> None:
        ...

    @property
    def portfolio_statistics(self) -> QuantConnect.Statistics.PortfolioStatistics:
        """The algorithm statistics on portfolio"""
        ...

    @property.setter
    def portfolio_statistics(self, value: QuantConnect.Statistics.PortfolioStatistics) -> None:
        ...

    @property
    def closed_trades(self) -> System.Collections.Generic.List[QuantConnect.Statistics.Trade]:
        """The list of closed trades"""
        ...

    @property.setter
    def closed_trades(self, value: System.Collections.Generic.List[QuantConnect.Statistics.Trade]) -> None:
        ...

    @overload
    def __init__(self, trades: System.Collections.Generic.List[QuantConnect.Statistics.Trade], profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], equity: System.Collections.Generic.SortedDictionary[datetime.datetime, float], portfolioTurnover: System.Collections.Generic.SortedDictionary[datetime.datetime, float], listPerformance: System.Collections.Generic.List[float], listBenchmark: System.Collections.Generic.List[float], startingCapital: float, winningTransactions: int, losingTransactions: int, riskFreeInterestRateModel: QuantConnect.Data.IRiskFreeInterestRateModel, tradingDaysPerYear: int) -> None:
        """
        Initializes a new instance of the AlgorithmPerformance class
        
        :param trades: The list of closed trades
        :param profitLoss: Trade record of profits and losses
        :param equity: The list of daily equity values
        :param portfolioTurnover: The algorithm portfolio turnover
        :param listPerformance: The list of algorithm performance values
        :param listBenchmark: The list of benchmark values
        :param startingCapital: The algorithm starting capital
        :param winningTransactions: Number of winning transactions
        :param losingTransactions: Number of losing transactions
        :param riskFreeInterestRateModel: The risk free interest rate model to use
        :param tradingDaysPerYear: The number of trading days per year
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AlgorithmPerformance class"""
        ...


class StatisticsResults(System.Object):
    """The StatisticsResults class represents total and rolling statistics for an algorithm"""

    @property
    def total_performance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """The performance of the algorithm over the whole period"""
        ...

    @property
    def rolling_performances(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """The rolling performance of the algorithm over 1, 3, 6, 12 month periods"""
        ...

    @property
    def summary(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Returns a summary of the algorithm performance as a dictionary"""
        ...

    @overload
    def __init__(self, totalPerformance: QuantConnect.Statistics.AlgorithmPerformance, rollingPerformances: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance], summary: System.Collections.Generic.Dictionary[str, str]) -> None:
        """
        Initializes a new instance of the StatisticsResults class
        
        :param totalPerformance: The algorithm total performance
        :param rollingPerformances: The algorithm rolling performances
        :param summary: The summary performance dictionary
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the StatisticsResults class"""
        ...


class IStatisticsService(metaclass=abc.ABCMeta):
    """This interface exposes methods for accessing algorithm statistics results at runtime."""

    def set_summary_statistic(self, name: str, value: str) -> None:
        """
        Sets or updates a custom summary statistic
        
        :param name: The statistic name
        :param value: The statistic value
        """
        ...

    def statistics_results(self) -> QuantConnect.Statistics.StatisticsResults:
        """
        Calculates and gets the current statistics for the algorithm
        
        :returns: The current statistics.
        """
        ...


class Statistics(System.Object):
    """Calculate all the statistics required from the backtest, based on the equity curve and the profit loss statement."""

    @staticmethod
    def annual_downside_standard_deviation(performance: System.Collections.Generic.List[float], trading_days_per_year: float, minimum_acceptable_return: float = 0) -> float:
        """
        Annualized downside standard deviation
        
        :param performance: Collection of double values for daily performance
        :param trading_days_per_year: Number of trading days for the assets in portfolio to get annualize standard deviation.
        :param minimum_acceptable_return: Minimum acceptable return
        :returns: Value for annual downside standard deviation.
        """
        ...

    @staticmethod
    def annual_downside_variance(performance: System.Collections.Generic.List[float], trading_days_per_year: float, minimum_acceptable_return: float = 0) -> float:
        """
        Annualized variance statistic calculation using the daily performance variance and trading days per year.
        
        :param minimum_acceptable_return: Minimum acceptable return
        :returns: Annual variance value.
        """
        ...

    @staticmethod
    def annual_performance(performance: System.Collections.Generic.List[float], trading_days_per_year: float) -> float:
        """
        Annualized return statistic calculated as an average of daily trading performance multiplied by the number of trading days per year.
        
        :param performance: Dictionary collection of double performance values
        :param trading_days_per_year: Trading days per year for the assets in portfolio
        :returns: Double annual performance percentage.
        """
        ...

    @staticmethod
    def annual_standard_deviation(performance: System.Collections.Generic.List[float], trading_days_per_year: float) -> float:
        """
        Annualized standard deviation
        
        :param performance: Collection of double values for daily performance
        :param trading_days_per_year: Number of trading days for the assets in portfolio to get annualize standard deviation.
        :returns: Value for annual standard deviation.
        """
        ...

    @staticmethod
    def annual_variance(performance: System.Collections.Generic.List[float], trading_days_per_year: float) -> float:
        """
        Annualized variance statistic calculation using the daily performance variance and trading days per year.
        
        :returns: Annual variance value.
        """
        ...

    @staticmethod
    def compounding_annual_performance(starting_capital: float, final_capital: float, years: float) -> float:
        """
        Annual compounded returns statistic based on the final-starting capital and years.
        
        :param starting_capital: Algorithm starting capital
        :param final_capital: Algorithm final capital
        :param years: Years trading
        :returns: Decimal fraction for annual compounding performance.
        """
        ...

    @staticmethod
    @overload
    def drawdown_percent(equity_over_time: System.Collections.Generic.SortedDictionary[datetime.datetime, float], rounding: int = 2) -> float:
        """Drawdown maximum percentage."""
        ...

    @staticmethod
    @overload
    def drawdown_percent(current: float, high: float, rounding_decimals: int = 2) -> float:
        """
        Calculate the drawdown between a high and current value
        
        :param current: Current value
        :param high: Latest maximum
        :param rounding_decimals: Digits to round the result too
        :returns: Drawdown percentage.
        """
        ...

    @staticmethod
    def observed_sharpe_ratio(list_performance: System.Collections.Generic.List[float]) -> float:
        """
        Calculates the observed sharpe ratio
        
        :param list_performance: The performance samples to use
        :returns: The observed sharpe ratio.
        """
        ...

    @staticmethod
    def probabilistic_sharpe_ratio(list_performance: System.Collections.Generic.List[float], benchmark_sharpe_ratio: float) -> float:
        """
        Helper method to calculate the probabilistic sharpe ratio
        
        :param list_performance: The list of algorithm performance values
        :param benchmark_sharpe_ratio: The benchmark sharpe ratio to use
        :returns: Probabilistic Sharpe Ratio.
        """
        ...

    @staticmethod
    @overload
    def sharpe_ratio(average_performance: float, standard_deviation: float, risk_free_rate: float) -> float:
        """
        Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk.
        
        :param average_performance: Average daily performance
        :param standard_deviation: Standard deviation of the daily performance
        :param risk_free_rate: The risk free rate
        :returns: Value for sharpe ratio.
        """
        ...

    @staticmethod
    @overload
    def sharpe_ratio(average_performance: float, standard_deviation: float, risk_free_rate: float) -> float:
        """
        Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk.
        
        :param average_performance: Average daily performance
        :param standard_deviation: Standard deviation of the daily performance
        :param risk_free_rate: The risk free rate
        :returns: Value for sharpe ratio.
        """
        ...

    @staticmethod
    @overload
    def sharpe_ratio(algo_performance: System.Collections.Generic.List[float], risk_free_rate: float, trading_days_per_year: float) -> float:
        """
        Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk.
        
        :param algo_performance: Collection of double values for the algorithm daily performance
        :param risk_free_rate: The risk free rate
        :param trading_days_per_year: Trading days per year for the assets in portfolio
        :returns: Value for sharpe ratio.
        """
        ...

    @staticmethod
    def sortino_ratio(algo_performance: System.Collections.Generic.List[float], risk_free_rate: float, trading_days_per_year: float, minimum_acceptable_return: float = 0) -> float:
        """
        Sortino ratio with respect to risk free rate: measures excess of return per unit of downside risk.
        
        :param algo_performance: Collection of double values for the algorithm daily performance
        :param risk_free_rate: The risk free rate
        :param trading_days_per_year: Trading days per year for the assets in portfolio
        :param minimum_acceptable_return: Minimum acceptable return for Sortino ratio calculation
        :returns: Value for Sortino ratio.
        """
        ...

    @staticmethod
    def tracking_error(algo_performance: System.Collections.Generic.List[float], benchmark_performance: System.Collections.Generic.List[float], trading_days_per_year: float) -> float:
        """
        Tracking error volatility (TEV) statistic - a measure of how closely a portfolio follows the index to which it is benchmarked
        
        :param algo_performance: Double collection of algorithm daily performance values
        :param benchmark_performance: Double collection of benchmark daily performance values
        :param trading_days_per_year: Number of trading days per year
        :returns: Value for tracking error.
        """
        ...


class FillGroupingMethod(Enum):
    """The method used to group order fills into trades"""

    FILL_TO_FILL = 0
    """A Trade is defined by a fill that establishes or increases a position and an offsetting fill that reduces the position size (0)"""

    FLAT_TO_FLAT = 1
    """A Trade is defined by a sequence of fills, from a flat position to a non-zero position which may increase or decrease in quantity, and back to a flat position (1)"""

    FLAT_TO_REDUCED = 2
    """A Trade is defined by a sequence of fills, from a flat position to a non-zero position and an offsetting fill that reduces the position size (2)"""


class FillMatchingMethod(Enum):
    """The method used to match offsetting order fills"""

    FIFO = 0
    """First In First Out fill matching method (0)"""

    LIFO = 1
    """Last In Last Out fill matching method (1)"""


class TradeBuilder(System.Object, QuantConnect.Interfaces.ITradeBuilder):
    """The TradeBuilder class generates trades from executions and market price updates"""

    @property
    def closed_trades(self) -> System.Collections.Generic.List[QuantConnect.Statistics.Trade]:
        """The list of closed trades"""
        ...

    def __init__(self, groupingMethod: QuantConnect.Statistics.FillGroupingMethod, matchingMethod: QuantConnect.Statistics.FillMatchingMethod) -> None:
        """Initializes a new instance of the TradeBuilder class"""
        ...

    def apply_split(self, split: QuantConnect.Data.Market.Split, live_mode: bool, data_normalization_mode: QuantConnect.DataNormalizationMode) -> None:
        """
        Applies a split to the trade builder
        
        :param split: The split to be applied
        :param live_mode: True if live mode, false for backtest
        :param data_normalization_mode: The DataNormalizationMode for this security
        """
        ...

    def has_open_position(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Returns true if there is an open position for the symbol
        
        :param symbol: The symbol
        :returns: true if there is an open position for the symbol.
        """
        ...

    def process_fill(self, fill: QuantConnect.Orders.OrderEvent, security_conversion_rate: float, fee_in_account_currency: float, multiplier: float = 1.0) -> None:
        """
        Processes a new fill, eventually creating new trades
        
        :param fill: The new fill order event
        :param security_conversion_rate: The current security market conversion rate into the account currency
        :param fee_in_account_currency: The current order fee in the account currency
        :param multiplier: The contract multiplier
        """
        ...

    def set_live_mode(self, live: bool) -> None:
        """
        Sets the live mode flag
        
        :param live: The live mode flag
        """
        ...

    def set_market_price(self, symbol: typing.Union[QuantConnect.Symbol, str], price: float) -> None:
        """Sets the current market price for the symbol"""
        ...

    def set_security_manager(self, securities: QuantConnect.Securities.SecurityManager) -> None:
        """
        Sets the security manager instance
        
        :param securities: The security manager
        """
        ...


class PerformanceMetrics(System.Object):
    """PerformanceMetrics contains the names of the various performance metrics used for evaluation purposes."""

    ALPHA: str = "Alpha"
    """Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns."""

    ANNUAL_STANDARD_DEVIATION: str = "Annual Standard Deviation"
    """Annualized standard deviation"""

    ANNUAL_VARIANCE: str = "Annual Variance"
    """Annualized variance statistic calculation using the daily performance variance and trading days per year."""

    AVERAGE_LOSS: str = "Average Loss"
    """The average rate of return for losing trades"""

    AVERAGE_WIN: str = "Average Win"
    """The average rate of return for winning trades"""

    BETA: str = "Beta"
    """Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance"""

    COMPOUNDING_ANNUAL_RETURN: str = "Compounding Annual Return"
    """Annual compounded returns statistic based on the final-starting capital and years."""

    DRAWDOWN: str = "Drawdown"
    """Drawdown maximum percentage."""

    ESTIMATED_STRATEGY_CAPACITY: str = "Estimated Strategy Capacity"
    """Total capacity of the algorithm"""

    EXPECTANCY: str = "Expectancy"
    """The expected value of the rate of return"""

    START_EQUITY: str = "Start Equity"
    """Initial Equity Total Value"""

    END_EQUITY: str = "End Equity"
    """Final Equity Total Value"""

    INFORMATION_RATIO: str = "Information Ratio"
    """Information ratio - risk adjusted return"""

    LOSS_RATE: str = "Loss Rate"
    """The ratio of the number of losing trades to the total number of trades"""

    NET_PROFIT: str = "Net Profit"
    """Total net profit percentage"""

    PROBABILISTIC_SHARPE_RATIO: str = "Probabilistic Sharpe Ratio"
    """
    Probabilistic Sharpe Ratio is a probability measure associated with the Sharpe ratio.
    It informs us of the probability that the estimated Sharpe ratio is greater than a chosen benchmark
    """

    PROFIT_LOSS_RATIO: str = "Profit-Loss Ratio"
    """The ratio of the average win rate to the average loss rate"""

    SHARPE_RATIO: str = "Sharpe Ratio"
    """Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk."""

    SORTINO_RATIO: str = "Sortino Ratio"
    """Sortino ratio with respect to risk free rate: measures excess of return per unit of downside risk."""

    TOTAL_FEES: str = "Total Fees"
    """Total amount of fees in the account currency"""

    TOTAL_ORDERS: str = "Total Orders"
    """Total amount of orders in the algorithm"""

    TRACKING_ERROR: str = "Tracking Error"
    """Tracking error volatility (TEV) statistic - a measure of how closely a portfolio follows the index to which it is benchmarked"""

    TREYNOR_RATIO: str = "Treynor Ratio"
    """Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk"""

    WIN_RATE: str = "Win Rate"
    """The ratio of the number of winning trades to the total number of trades"""

    LOWEST_CAPACITY_ASSET: str = "Lowest Capacity Asset"
    """Provide a reference to the lowest capacity symbol used in scaling down the capacity for debugging."""

    PORTFOLIO_TURNOVER: str = "Portfolio Turnover"
    """The average Portfolio Turnover"""


class StatisticsBuilder(System.Object):
    """The StatisticsBuilder class creates summary and rolling statistics from trades, equity and benchmark points"""

    @staticmethod
    def create_benchmark_differences(points: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[datetime.datetime, float]], from_date: typing.Union[datetime.datetime, datetime.date], to_date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[datetime.datetime, float]]:
        """
        Yields pairs of date and percentage change for the period
        
        :param points: The values to calculate percentage change for
        :param from_date: Starting date (inclusive)
        :param to_date: Ending date (inclusive)
        :returns: Pairs of date and percentage change.
        """
        ...

    @staticmethod
    def generate(trades: System.Collections.Generic.List[QuantConnect.Statistics.Trade], profit_loss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], points_equity: System.Collections.Generic.List[QuantConnect.ISeriesPoint], points_performance: System.Collections.Generic.List[QuantConnect.ISeriesPoint], points_benchmark: System.Collections.Generic.List[QuantConnect.ISeriesPoint], points_portfolio_turnover: System.Collections.Generic.List[QuantConnect.ISeriesPoint], starting_capital: float, total_fees: float, total_orders: int, estimated_strategy_capacity: QuantConnect.CapacityEstimate, account_currency_symbol: str, transactions: QuantConnect.Securities.SecurityTransactionManager, risk_free_interest_rate_model: QuantConnect.Data.IRiskFreeInterestRateModel, trading_days_per_year: int) -> QuantConnect.Statistics.StatisticsResults:
        """
        Generates the statistics and returns the results
        
        :param trades: The list of closed trades
        :param profit_loss: Trade record of profits and losses
        :param points_equity: The list of daily equity values
        :param points_performance: The list of algorithm performance values
        :param points_benchmark: The list of benchmark values
        :param points_portfolio_turnover: The list of portfolio turnover daily samples
        :param starting_capital: The algorithm starting capital
        :param total_fees: The total fees
        :param total_orders: The total number of transactions
        :param estimated_strategy_capacity: The estimated capacity of this strategy
        :param account_currency_symbol: The account currency symbol
        :param transactions: The transaction manager to get number of winning and losing transactions
        :param risk_free_interest_rate_model: The risk free interest rate model to use
        :param trading_days_per_year: The number of trading days per year
        :returns: Returns a StatisticsResults object.
        """
        ...

    @staticmethod
    def preprocess_performance_values(points: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[datetime.datetime, float]]) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[datetime.datetime, float]]:
        """
        Skips the first two entries from the given points and divides each entry by 100
        
        :param points: The values to divide by 100
        :returns: Pairs of date and performance value divided by 100.
        """
        ...


