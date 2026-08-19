"""
PropietaryCode.decorators
=========================
Subpackage containing universal decorators for QuantConnect algorithms:
  - trade_logger: @log_trade_entry and @log_trade_exit for standardized BigQuery logging
  - perf_monitor: @monitor_execution and @measure_memory_usage for performance monitoring
"""

from .trade_logger import (
    log_trade_entry,
    log_trade_exit,
    normalize_exit_reason,
    save_trade_buffer_to_object_store,
)
from .perf_monitor import monitor_execution, measure_memory_usage

__all__ = [
    "log_trade_entry",
    "log_trade_exit",
    "normalize_exit_reason",
    "save_trade_buffer_to_object_store",
    "monitor_execution",
    "measure_memory_usage",
]
