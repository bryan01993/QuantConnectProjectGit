from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Interfaces
import System.Collections.Generic


class InsightManager(QuantConnect.Algorithm.Framework.Alphas.InsightCollection):
    """Encapsulates the storage of insights."""

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Creates a new instance
        
        :param algorithm: The associated algorithm instance
        """
        ...

    @overload
    def cancel(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> None:
        """
        Cancel the insights of the given symbols
        
        :param symbols: Symbol we want to cancel insights for
        """
        ...

    @overload
    def cancel(self, insights: System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> None:
        """
        Cancel the given insights
        
        :param insights: Insights to cancel
        """
        ...

    @overload
    def expire(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> None:
        """
        Expire the insights of the given symbols
        
        :param symbols: Symbol we want to expire insights for
        """
        ...

    @overload
    def expire(self, insights: System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> None:
        """
        Expire the given insights
        
        :param insights: Insights to expire
        """
        ...

    @overload
    def set_insight_score_function(self, insight_score_function: QuantConnect.Algorithm.Framework.Alphas.IInsightScoreFunction) -> None:
        """
        Sets the insight score function to use
        
        :param insight_score_function: Model that scores insights
        """
        ...

    @overload
    def set_insight_score_function(self, insight_score_function: typing.Any) -> None:
        """
        Sets the insight score function to use
        
        :param insight_score_function: Model that scores insights
        """
        ...

    def step(self, utc_now: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Process a new time step handling insights scoring
        
        :param utc_now: The current utc time
        """
        ...


