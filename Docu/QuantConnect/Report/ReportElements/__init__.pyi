from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect
import QuantConnect.Packets
import QuantConnect.Report.ReportElements
import System
import System.Collections.Generic


class ReportElement(System.Object, QuantConnect.Report.ReportElements.IReportElement, metaclass=abc.ABCMeta):
    """Common interface for template elements of the report"""

    @property
    def name(self) -> str:
        """Name of this report element"""
        ...

    @property
    def key(self) -> str:
        """Template key code."""
        ...

    @property
    def json_key(self) -> str:
        """Normalizes the key into a JSON-friendly key"""
        ...

    @property
    def result(self) -> System.Object:
        """Result of the render as an object for serialization to JSON"""
        ...

    def render(self) -> str:
        """The generated output string to be injected"""
        ...


class ParametersReportElement(QuantConnect.Report.ReportElements.ReportElement):
    """Class for creating a two column table for the Algorithm's Parameters in a report"""

    def __init__(self, name: str, key: str, backtestConfiguration: QuantConnect.AlgorithmConfiguration, liveConfiguration: QuantConnect.AlgorithmConfiguration, template: str) -> None:
        """
        Creates a two column table for the Algorithm's Parameters
        
        :param name: Name of the widget
        :param key: Location of injection
        :param backtestConfiguration: The configuration of the backtest algorithm
        :param liveConfiguration: The configuration of the live algorithm
        :param template: HTML template to use
        """
        ...

    def render(self) -> str:
        """
        Generates a HTML two column table for the Algorithm's Parameters
        
        :returns: Returns a string representing a HTML two column table.
        """
        ...


class EstimatedCapacityReportElement(QuantConnect.Report.ReportElements.ReportElement):
    """Capacity Estimation Report Element"""

    def __init__(self, name: str, key: str, backtest: QuantConnect.Packets.BacktestResult, live: QuantConnect.Packets.LiveResult) -> None:
        """
        Create a new capacity estimate
        
        :param name: Name of the widget
        :param key: Location of injection
        :param backtest: Backtest result object
        :param live: Live result object
        """
        ...

    def render(self) -> str:
        """Render element"""
        ...


class SharpeRatioReportElement(QuantConnect.Report.ReportElements.ReportElement):
    """Class for render the Sharpe Ratio statistic for a report"""

    @property
    def live_result(self) -> QuantConnect.Packets.LiveResult:
        """
        Live result object
        
        This property is protected.
        """
        ...

    @property
    def backtest_result(self) -> QuantConnect.Packets.BacktestResult:
        """
        Backtest result object
        
        This property is protected.
        """
        ...

    @property
    def backtest_result_value(self) -> typing.Optional[float]:
        """Sharpe Ratio from a backtest"""
        ...

    def __init__(self, name: str, key: str, backtest: QuantConnect.Packets.BacktestResult, live: QuantConnect.Packets.LiveResult, tradingDaysPerYear: int) -> None:
        """
        Estimate the sharpe ratio of the strategy.
        
        :param name: Name of the widget
        :param key: Location of injection
        :param backtest: Backtest result object
        :param live: Live result object
        :param tradingDaysPerYear: The number of trading days per year to get better result of statistics
        """
        ...

    def get_annual_standard_deviation(self, trailing_performance: System.Collections.Generic.List[float], trading_days_per_year: float) -> float:
        """
        Get annual standard deviation
        
        :param trailing_performance: The performance for the last period
        :param trading_days_per_year: The number of trading days per year to get better result of statistics
        :returns: Annual standard deviation.
        """
        ...

    def render(self) -> str:
        """The generated output string to be injected"""
        ...


