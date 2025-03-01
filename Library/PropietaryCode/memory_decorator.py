# memory_decorators.py

import os
import psutil
import functools

def measure_memory_usage(func):
    """
    Decorator to measure memory usage before/after a function call
    and log the consumption delta.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss  # in bytes
        result = func(*args, **kwargs)
        mem_after = process.memory_info().rss
        mem_diff_mb = (mem_after - mem_before) / (1024.0 * 1024.0)
        print(f"[MEMORY] Function {func.__name__} used {mem_diff_mb:.2f} MB additional memory")
        return result
    return wrapper
