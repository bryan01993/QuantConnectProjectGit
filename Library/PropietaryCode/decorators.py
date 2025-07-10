# from QuantConnect.Algorithm import QCAlgorithm
import time
import inspect


class FunctionLogger:
    """
    A class to log function execution details in QuantConnect algorithms.
    It logs the order of execution, function name, start time, parameters, duration,
    and raises any exceptions if occurred.

    This class is callable as a decorator and logs using QuantConnect's native logging system.
    """
    order = 0  # Nominal order of execution

    def __init__(self, qc_algorithm_instance):
        """
        Initialize the FunctionLogger with an instance of the QCAlgorithm class.
        :param qc_algorithm_instance: Instance of QCAlgorithm (or inherited class)
        """
        self.qc = qc_algorithm_instance

    def _truncate(self, value, limit=10):
        """Return a truncated representation for large iterables."""
        try:
            if isinstance(value, dict):
                truncated = {k: value[k] for k in list(value)[:limit]}
                if len(value) > limit:
                    truncated['...'] = f"{len(value) - limit} more items"
                return truncated
            elif isinstance(value, (list, tuple, set)):
                seq = list(value)[:limit]
                if len(value) > limit:
                    seq.append(f"... {len(value) - limit} more")
                return seq
        except Exception:
            pass
        return value

    def log(self, func):
        """
        Method to act as the decorator itself. It logs information about the decorated function's execution.

        :param func: The function being decorated
        """

        def wrapper(*args, **kwargs):
            start_time = time.time()
            FunctionLogger.order += 1  # Increment the order of execution
            func_name = func.__name__

            signature = inspect.signature(func)
            bound_args = signature.bind_partial(*args, **kwargs)
            bound_args.apply_defaults()
            arg_info = {}
            for k, v in bound_args.arguments.items():
                if k == 'self':
                    continue
                arg_info[k] = self._truncate(v)

            try:
                result = func(*args, **kwargs)
                duration = round(time.time() - start_time, 4)  # Duration in seconds

                log_data = {
                    'execution_order': FunctionLogger.order,
                    'function': func_name,
                    'execution_time': f"{duration} sec",
                    'args': arg_info,
                    'result': self._truncate(result)
                }

                self.qc.Debug(str(log_data))

                return result

            except Exception as e:
                # Access QCAlgorithm's Error method and re-raise the exception
                self.qc.Error(f"Exception in {func_name}: {str(e)}")
                raise e

        return wrapper


# Example usage within a QuantConnect Algorithm
# class MyAlgorithm(QCAlgorithm):
#     def Initialize(self):
#         self.SetStartDate(2022, 1, 1)
#         self.SetEndDate(2022, 12, 31)
#         self.SetCash(100000)
#
#         # Instantiate FunctionLogger with the algorithm instance
#         self.function_logger = FunctionLogger(self)
#
#     @FunctionLogger.log
#     def OnData(self, data):
#         # Example function that will be logged
#         self.Debug("Processing new data...")
#         pass
