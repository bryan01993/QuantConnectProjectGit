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

    def log(self, func):
        """
        Method to act as the decorator itself. It logs information about the decorated function's execution.

        :param func: The function being decorated
        """

        def wrapper(*args, **kwargs):
            start_time = time.time()
            FunctionLogger.order += 1  # Increment the order of execution
            func_name = func.__name__

            # Log function arguments with their types --> Commented out for clarity and brevity
            # signature = inspect.signature(func)
            # bound_args = signature.bind(*args, **kwargs)
            # bound_args.apply_defaults()
            # arg_info = {k: (v, type(v).__name__) for k, v in bound_args.arguments.items()}

            try:
                result = func(*args, **kwargs)
                duration = round(time.time() - start_time, 4)  # Duration in seconds

                # Access QCAlgorithm's Debug method
                self.qc.Debug(f"ALGO_ORDER: {FunctionLogger.order}, "
                              f"FUNCTION_ID: {id(func)}, "
                              f"FUNCTION_NAME: {func_name}, "
                              # f"PARAMETERS: {arg_info}, "
                              f"DURATION: {duration}s")

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
