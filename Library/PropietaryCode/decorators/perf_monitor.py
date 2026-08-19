"""
PropietaryCode.decorators.perf_monitor
======================================
Performance and memory monitoring decorators for QuantConnect algorithms.

  - @monitor_execution: Measures function execution time, process-level RSS memory
                        delta, and logs formatted execution metrics via self.Log().
  - @measure_memory_usage: Measures RSS memory consumption before/after function call.

Zero-Failure Invariant:
  Under NO circumstances will logging, memory measurement, or string formatting
  raise an exception that interrupts algorithm execution.
"""

from __future__ import annotations

import functools
import sys
import time
from typing import Any, Callable, Tuple
import psutil

__all__ = [
    "monitor_execution",
    "measure_memory_usage",
]


def _get_process_rss_mb() -> float:
    """Returns current process Resident Set Size (RSS) memory in Megabytes."""
    try:
        process = psutil.Process()
        return process.memory_info().rss / (1024 * 1024)
    except Exception:
        return 0.0


def _safe_format_args(args: Tuple[Any, ...], kwargs: dict) -> str:
    """Safely formats function arguments without consuming iterators or raising errors."""
    formatted = []

    # Format positional args (skipping self/cls if present)
    for i, arg in enumerate(args):
        if i == 0 and hasattr(arg, "__class__") and not isinstance(arg, (int, float, str, dict, list, tuple, set)):
            continue
        try:
            if hasattr(arg, "__next__") or hasattr(arg, "__iter__") and not isinstance(arg, (str, dict, list, tuple, set)):
                formatted.append(f"<{type(arg).__name__} iterator>")
            else:
                formatted.append(repr(arg))
        except Exception:
            formatted.append("<unrepresentable>")

    # Format keyword args
    for k, v in kwargs.items():
        try:
            if hasattr(v, "__next__") or hasattr(v, "__iter__") and not isinstance(v, (str, dict, list, tuple, set)):
                formatted.append(f"{k}=<{type(v).__name__} iterator>")
            else:
                formatted.append(f"{k}={repr(v)}")
        except Exception:
            formatted.append(f"{k}=<unrepresentable>")

    res = ", ".join(formatted)
    return res[:150] + "..." if len(res) > 150 else res


def _safe_format_result(result: Any) -> str:
    """Safely formats function result without consuming generators/iterators."""
    if result is None:
        return "No return value"
    try:
        if hasattr(result, "__next__") or (hasattr(result, "__iter__") and not isinstance(result, (str, dict, list, tuple, set))):
            return f"<{type(result).__name__} generator/iterator>"
        res_str = repr(result)
        return res_str[:150] + "..." if len(res_str) > 150 else res_str
    except Exception as err:
        return f"<unrepresentable result: {err}>"


def monitor_execution(func: Callable) -> Callable:
    """
    Decorator that monitors function execution duration and process RSS memory.
    Logs metrics via self.Log(...) if available. Guaranteed never to interrupt execution.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        mem_before = _get_process_rss_mb()
        order_counter = 0

        # Execute target function
        result = func(*args, **kwargs)

        exec_time = time.perf_counter() - start_time
        mem_after = _get_process_rss_mb()
        mem_delta = max(0.0, mem_after - mem_before)

        # Resilient logging logic
        try:
            self_obj = args[0] if len(args) > 0 else None
            
            if self_obj is not None:
                order_counter = getattr(self_obj, "_exec_order_counter", 0) + 1
                setattr(self_obj, "_exec_order_counter", order_counter)

            formatted_result = _safe_format_result(result)

            log_dict = {
                "execution_order": order_counter,
                "function": func.__name__,
                "execution_time": f"{exec_time:.6f} sec",
                "memory_delta_mb": f"{mem_delta:.2f} MB",
                "current_memory_mb": f"{mem_after:.2f} MB",
                "result": formatted_result,
            }

            log_msg = f"{log_dict}"

            if self_obj is not None and hasattr(self_obj, "Log") and callable(getattr(self_obj, "Log")):
                self_obj.Log(log_msg)

        except Exception as log_err:
            sys.stderr.write(f"[monitor_execution WARNING] Failed to format or emit execution log: {log_err}\n")

        return result

    return wrapper


def measure_memory_usage(func: Callable) -> Callable:
    """
    Decorator to measure and return process RSS memory consumption along with function output.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, float]:
        mem_before = _get_process_rss_mb()
        result = func(*args, **kwargs)
        mem_after = _get_process_rss_mb()
        return result, mem_after - mem_before

    return wrapper
