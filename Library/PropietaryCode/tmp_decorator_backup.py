import logging
import time
from functools import wraps
from inspect import signature
from datetime import datetime

def timeit(func):
    """
    A decorator that measures the execution time of a function.
    The function to be decorated should be a method of a class that has a 'Debug' method.
    """

    def wrapper(self, *args, **kwargs):
        try:
            start_time = time.time()
            result = func(self, *args, **kwargs)
            end_time = time.time()
            self.Log(f"Function {func.__name__!r} executed in {(end_time - start_time):.3f}s")
            return result
        except Exception as e:
            self.Log(f"Function {func.__name__!r} could not be timed because of {e}")

    return wrapper



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class FunctionLogger:
    function_counter = 0
    function_indices = {}

    def __init__(self, func):
        self.func = func
        self.index = FunctionLogger.function_counter
        FunctionLogger.function_counter += 1
        wraps(self.func)(self)

    def __get__(self, instance, owner):
        # Support instance methods
        return self.__class__(self.func.__get__(instance, owner))

    def __call__(self, *args, **kwargs):
        # Log start time
        start_time = datetime.now()
        instance = self._get_instance(args)  # Get the instance (self) from args
        self._log(instance, f"Function {self.func.__name__} (Index: {self.index}) started at {start_time}")

        # Log arguments with their types and values
        arg_info = self._log_arguments(args, kwargs)
        self._log(instance, f"Arguments: {arg_info}")

        try:
            # Execute the function
            result = self.func(*args, **kwargs)
            return result
        except Exception as e:
            # Log exception if occurs using Error() method
            self._log(instance, f"Function {self.func.__name__} (Index: {self.index}) raised an error: {e}", is_error=True)
            raise e
        finally:
            # Log end time and execution duration
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            self._log(instance, f"Function {self.func.__name__} (Index: {self.index}) finished at {end_time}, duration: {round(duration, 5)} seconds")

    def _get_instance(self, args):
        # Assumes first argument is 'self' (i.e., the instance of the class)
        return args[0] if args else None

    def _log(self, instance, message, is_error=False):
        # If instance has Debug or Error, log the message accordingly
        if instance and hasattr(instance, 'Debug'):
            if is_error:
                instance.Error(message)
            else:
                instance.Debug(message)
        else:
            print(message)  # Fallback in case no logging methods are found

    def _log_arguments(self, args, kwargs):
        arg_list = []
        for arg in args:
            arg_list.append(f'"{arg}", {type(arg).__name__}, "{arg}"')
        for key, value in kwargs.items():
            arg_list.append(f'{key}="{value}", {type(value).__name__}, "{value}"')

        # Retrieve function argument names and default values
        arg_names = self.func.__code__.co_varnames[:self.func.__code__.co_argcount]
        defaults = self.func.__defaults__ or []
        defaults_dict = dict(zip(arg_names[-len(defaults):], defaults))

        # Add default arguments if not provided
        for key, value in defaults_dict.items():
            if key not in kwargs and key not in arg_names[:len(args)]:
                arg_list.append(f'{key}="{value}", {type(value).__name__}, "{value}"')

        return ', '.join(arg_list)


# class MyAlgorithm:
#     @FunctionLogger
#     def example_method(self, a, b, c=5):
#         time.sleep(1)
#         return a + b + c
#
# if __name__ == "__main__":
#     algo = MyAlgorithm()
#     try:
#         algo.example_method(1, 2, c=3)
#         algo.example_method("x", "y", "z")
#     except Exception as e:
#         print(f"An error occurred: {e}")