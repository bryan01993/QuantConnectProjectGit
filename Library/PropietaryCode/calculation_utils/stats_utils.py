"""
PropietaryCode.calculation_utils.stats_utils
=============================================
Statistical helpers and rolling metric calculations for QuantConnect algorithms.
"""

from __future__ import annotations

import math
from typing import List, Tuple, Optional
import numpy as np


def calculate_mean_and_stdev(data: List[float]) -> Tuple[float, float]:
    """Calculates sample mean and standard deviation for a numeric list."""
    if not data or len(data) < 2:
        return 0.0, 0.0
    arr = np.array(data, dtype=float)
    return float(np.mean(arr)), float(np.std(arr, ddof=1))


def calculate_zscore(current_val: float, history: List[float]) -> float:
    """Calculates Z-score of current_val relative to historical distribution."""
    mean, stdev = calculate_mean_and_stdev(history)
    if stdev == 0.0:
        return 0.0
    return (current_val - mean) / stdev
