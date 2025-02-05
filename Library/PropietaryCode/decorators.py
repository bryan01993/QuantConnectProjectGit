import time
import tracemalloc
from functools import wraps

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

        # Ensure self has Log method (it should be an instance of QCAlgorithm)
        if hasattr(self, "Log"):
            log_entry = {
                "execution_order": execution_order,
                "function": func.__name__,
                "execution_time": f"{execution_time:.6f} sec",
                "memory_usage": f"{current / 1024:.2f} KB",
                "peak_memory": f"{peak / 1024:.2f} KB",
                "args": args,
                "kwargs": kwargs,
                "result": result
            }
            self.Log(str(log_entry))
        else:
            raise TypeError(f"{self} does not have a 'Log' method. Ensure this is used inside a QCAlgorithm class.")

        return result

    return wrapper
