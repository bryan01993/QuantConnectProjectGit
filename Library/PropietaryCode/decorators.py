import time
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
            self.Debug(f"Function {func.__name__!r} executed in {(end_time - start_time):.3f}s")
            return result
        except Exception as e:
            self.Debug(f"Function {func.__name__!r} could not be timed because of {e}")

    return wrapper