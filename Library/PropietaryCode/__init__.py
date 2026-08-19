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
from . import decorators
from . import calculation_utils
from . import research_utils

__all__ = [
    "log_trade_entry",
    "log_trade_exit",
    "normalize_exit_reason",
    "save_trade_buffer_to_object_store",
    "monitor_execution",
    "measure_memory_usage",
    "decorators",
    "calculation_utils",
    "research_utils",
]
