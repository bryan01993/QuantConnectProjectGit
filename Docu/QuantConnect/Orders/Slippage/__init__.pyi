from typing import overload
from enum import Enum
import abc

import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Slippage
import QuantConnect.Securities
import System


class ISlippageModel(metaclass=abc.ABCMeta):
    """Represents a model that simulates market order slippage"""

    def get_slippage_approximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Slippage Model. Return a decimal cash slippage approximation on the order."""
        ...


class VolumeShareSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """
    Represents a slippage model that is calculated by multiplying the price impact constant
    by the square of the ratio of the order to the total volume.
    """

    def __init__(self, volumeLimit: float = 0.025, priceImpact: float = 0.1) -> None:
        """
        Initializes a new instance of the VolumeShareSlippageModel class
        
        :param priceImpact: Defines how large of an impact the order will have on the price calculation
        """
        ...

    def get_slippage_approximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Slippage Model. Return a decimal cash slippage approximation on the order."""
        ...


class AlphaStreamsSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """Represents a slippage model that uses a constant percentage of slip"""

    def __init__(self) -> None:
        """Initializes a new instance of the AlphaStreamsSlippageModel class"""
        ...

    def get_slippage_approximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Return a decimal cash slippage approximation on the order."""
        ...


class MarketImpactSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """
    Slippage model that mimic the effect brought by market impact,
    i.e. consume the volume listed in the order book
    """

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, nonNegative: bool = True, latency: float = ..., impactTime: float = ..., alpha: float = ..., beta: float = ..., gamma: float = ..., eta: float = ..., delta: float = ..., randomSeed: int = 50) -> None:
        """
        Instantiate a new instance of MarketImpactSlippageModel
        
        :param algorithm: IAlgorithm instance
        :param nonNegative: Indicator whether only non-negative slippage allowed
        :param latency: Time between order submitted and filled, in seconds(s)
        :param impactTime: Time between order filled and new equilibrium established, in second(s)
        :param alpha: Exponent of the permanent impact function
        :param beta: Exponent of the temporary impact function
        :param gamma: Coefficient of the permanent impact function
        :param eta: Coefficient of the temporary impact function
        :param delta: Liquidity scaling factor for permanent impact
        :param randomSeed: Random seed for generating gaussian noise
        """
        ...

    def get_slippage_approximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Slippage Model. Return a decimal cash slippage approximation on the order."""
        ...


class ConstantSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """Represents a slippage model that uses a constant percentage of slip"""

    def __init__(self, slippagePercent: float) -> None:
        """
        Initializes a new instance of the ConstantSlippageModel class
        
        :param slippagePercent: The slippage percent for each order. Percent is ranged 0 to 1.
        """
        ...

    def get_slippage_approximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Slippage Model. Return a decimal cash slippage approximation on the order."""
        ...


class NullSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """Null slippage model, which provider no slippage"""

    INSTANCE: QuantConnect.Orders.Slippage.NullSlippageModel
    """The null slippage model instance"""

    def get_slippage_approximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Will return no slippage"""
        ...


