"""
models
======
Modular strategy components for QuantConnect algorithm architectures.
"""

from .alpha_model import CalendarSpreadOpportunity, CalendarSpreadAlphaModel
from .execution_manager import CalendarSpreadExecutionManager

__all__ = [
    "CalendarSpreadOpportunity",
    "CalendarSpreadAlphaModel",
    "CalendarSpreadExecutionManager",
]
