"""
Library.PropietaryCode
======================
Shared proprietary library code for QuantConnect algorithms.

Subpackages:
  - decorators: Logging and execution monitoring decorators (@log_trade_entry, @log_trade_exit, @monitor_execution)
  - calculation_utils: Shared math, option pricing, and statistical utilities
  - research_utils: Introspection, class visualization, and notebook research tools
"""

from .decorators.trade_logger import (
    log_trade_entry,
    log_trade_exit,
    normalize_exit_reason,
    save_trade_buffer_to_object_store,
)
from .decorators.perf_monitor import monitor_execution, measure_memory_usage
from .calculation_utils.BSMModel import (
    fast_norm_cdf,
    fast_norm_pdf,
    fast_bs_price,
    fast_vega,
    fast_implied_volatility_newton,
)
from .models.alpha_model import CalendarSpreadOpportunity, CalendarSpreadAlphaModel
from .models.execution_manager import CalendarSpreadExecutionManager
from . import decorators
from . import calculation_utils
from . import research_utils
from . import models

__all__ = [
    "log_trade_entry",
    "log_trade_exit",
    "normalize_exit_reason",
    "save_trade_buffer_to_object_store",
    "monitor_execution",
    "measure_memory_usage",
    "fast_norm_cdf",
    "fast_norm_pdf",
    "fast_bs_price",
    "fast_vega",
    "fast_implied_volatility_newton",
    "CalendarSpreadOpportunity",
    "CalendarSpreadAlphaModel",
    "CalendarSpreadExecutionManager",
    "decorators",
    "calculation_utils",
    "research_utils",
    "models",
]
