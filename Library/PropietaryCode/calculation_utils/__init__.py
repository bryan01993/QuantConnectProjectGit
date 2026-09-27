"""
PropietaryCode.calculation_utils
================================
Quantitative calculation utilities including option pricing, statistics, and risk management.
"""

from .BSMModel import (
    BsmModel,
    BSMModel,
    fast_norm_cdf,
    fast_norm_pdf,
    fast_bs_price,
    fast_vega,
    fast_implied_volatility_newton,
)
from .stats_utils import calculate_mean_and_stdev, calculate_zscore
from .risk_management import KellyCriterion

__all__ = [
    "BsmModel",
    "BSMModel",
    "fast_norm_cdf",
    "fast_norm_pdf",
    "fast_bs_price",
    "fast_vega",
    "fast_implied_volatility_newton",
    "calculate_mean_and_stdev",
    "calculate_zscore",
    "KellyCriterion",
]
