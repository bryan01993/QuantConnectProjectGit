import time
import tracemalloc
from functools import wraps
from collections.abc import Iterator
import itertools

execution_order = 0  # Global counter for function order

def monitor_execution(func):
    """
    Decorator to log execution time, arguments, return values, and memory usage of selected functions
    using QuantConnect's .Log() method. Also maintains nominal execution order.
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        global execution_order
        execution_order += 1
        start_time = time.time()
        tracemalloc.start()  # Start memory tracking

        result = func(self, *args, **kwargs)  # Execute the function

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()  # Get memory usage
        tracemalloc.stop()
        execution_time = end_time - start_time

        # Handle cases where args or kwargs are empty
        args_display = args if args else None
        kwargs_display = kwargs if kwargs else None

        # Limit result size if it's a list or iterator
        try:
            if result is None:
                result_display = "No return value"
            elif isinstance(result, list):
                if len(result) > 5:
                    result_display = result[:5] + ["..."]  # Keep first 5 elements and indicate truncation
                elif len(result) == 0:
                    result_display = "Empty list"
                else:
                    result_display = result
            elif isinstance(result, Iterator):
                result_display = list(itertools.islice(result, 5))  # Take the first 5 elements from iterator
                if result_display:
                    result_display.append("...")
                else:
                    result_display = "Empty iterator"
            else:
                result_display = result
        except MemoryError:
            result_display = "MemoryError encountered while processing result"

        # Ensure self has Log method (it should be an instance of QCAlgorithm)
        if hasattr(self, "Log"):
            log_entry = {
                "execution_order": execution_order,
                "function": func.__name__,
                "execution_time": f"{execution_time:.6f} sec",
                "memory_usage": f"{current / 1024:.2f} KB",
                "peak_memory": f"{peak / 1024:.2f} KB",
                "args": args_display,
                "kwargs": kwargs_display,
                "result": result_display
            }
            self.Log(str(log_entry))
        else:
            raise TypeError(f"{self} does not have a 'Log' method. Ensure this is used inside a QCAlgorithm class.")

        return result
    return wrapper
