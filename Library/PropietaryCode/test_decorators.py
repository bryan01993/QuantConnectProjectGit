import unittest
from unittest.mock import patch, call
import logging
from datetime import datetime, timedelta
from decorators import FunctionLogger  # Replace `mymodule` with the actual module name where the FunctionLogger class is defined

class TestFunctionLogger(unittest.TestCase):
    def setUp(self):
        # Reset the function counter before each test
        FunctionLogger.function_counter = 0

    @patch('decorators.datetime')  # Patch datetime in the module where FunctionLogger is defined
    @patch('logging.info')
    def test_simple_function(self, mock_logger_info, mock_datetime):
        mock_datetime.now.side_effect = [
            datetime(2023, 7, 29, 12, 0, 0),
            datetime(2023, 7, 29, 12, 0, 1)
        ]

        @FunctionLogger
        def add(a, b):
            return a + b

        add(2, 3)

        expected_calls = [
            call('Function add (Index: 0) started at 2023-07-29 12:00:00'),
            call('Arguments: "2", int, "2", "3", int, "3"'),
            call('Function add (Index: 0) finished at 2023-07-29 12:00:01, duration: 1.0 seconds')
        ]
        mock_logger_info.assert_has_calls(expected_calls, any_order=False)

    @patch('decorators.datetime')  # Patch datetime in the module where FunctionLogger is defined
    @patch('logging.info')
    def test_function_with_kwargs(self, mock_logger_info, mock_datetime):
        mock_datetime.now.side_effect = [
            datetime(2023, 7, 29, 12, 0, 0),
            datetime(2023, 7, 29, 12, 0, 1)
        ]

        @FunctionLogger
        def greet(greeting, name="World"):
            return f"{greeting}, {name}!"

        greet(greeting="Hello", name="Alice")

        expected_calls = [
            call('Function greet (Index: 0) started at 2023-07-29 12:00:00'),
            call('Arguments: greeting="Hello", str, "Hello", name="Alice", str, "Alice"'),
            call('Function greet (Index: 0) finished at 2023-07-29 12:00:01, duration: 1.0 seconds')
        ]
        mock_logger_info.assert_has_calls(expected_calls, any_order=False)

    @patch('decorators.datetime')  # Patch datetime in the module where FunctionLogger is defined
    @patch('logging.info')
    def test_function_with_default_args(self, mock_logger_info, mock_datetime):
        mock_datetime.now.side_effect = [
            datetime(2023, 7, 29, 12, 0, 0),
            datetime(2023, 7, 29, 12, 0, 1)
        ]

        @FunctionLogger
        def greet(greeting, name="World"):
            return f"{greeting}, {name}!"

        greet("Hi")

        expected_calls = [
            call('Function greet (Index: 0) started at 2023-07-29 12:00:00'),
            call('Arguments: "Hi", str, "Hi", name="World", str, "World"'),
            call('Function greet (Index: 0) finished at 2023-07-29 12:00:01, duration: 1.0 seconds')
        ]
        mock_logger_info.assert_has_calls(expected_calls, any_order=False)

    @patch('decorators.datetime')  # Patch datetime in the module where FunctionLogger is defined
    @patch('logging.info')
    def test_multiple_function_calls(self, mock_logger_info, mock_datetime):
        mock_datetime.now.side_effect = [
            datetime(2023, 7, 29, 12, 0, 0),
            datetime(2023, 7, 29, 12, 0, 1),
            datetime(2023, 7, 29, 12, 0, 2),
            datetime(2023, 7, 29, 12, 0, 3),
            datetime(2023, 7, 29, 12, 0, 4),
            datetime(2023, 7, 29, 12, 0, 5),
        ]

        @FunctionLogger
        def add(a, b):
            return a + b

        @FunctionLogger
        def multiply(a, b):
            return a * b

        add(2, 3)
        multiply(4, 5)
        add(5, 7)

        expected_calls = [
            call('Function add (Index: 0) started at 2023-07-29 12:00:00'),
            call('Arguments: "2", int, "2", "3", int, "3"'),
            call('Function add (Index: 0) finished at 2023-07-29 12:00:01, duration: 1.0 seconds'),
            call('Function multiply (Index: 1) started at 2023-07-29 12:00:02'),
            call('Arguments: "4", int, "4", "5", int, "5"'),
            call('Function multiply (Index: 1) finished at 2023-07-29 12:00:03, duration: 1.0 seconds'),
            call('Function add (Index: 0) started at 2023-07-29 12:00:04'),
            call('Arguments: "5", int, "5", "7", int, "7"'),
            call('Function add (Index: 0) finished at 2023-07-29 12:00:05, duration: 1.0 seconds')
        ]
        mock_logger_info.assert_has_calls(expected_calls, any_order=False)

    @patch('decorators.datetime')  # Patch datetime in the module where FunctionLogger is defined
    @patch('logging.info')
    @patch('logging.error')
    def test_function_raises_exception(self, mock_logger_error, mock_logger_info, mock_datetime):
        mock_datetime.now.side_effect = [
            datetime(2023, 7, 29, 12, 0, 0),
            datetime(2023, 7, 29, 12, 0, 1)
        ]

        @FunctionLogger
        def divide(a, b):
            return a / b

        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

        expected_info_calls = [
            call('Function divide (Index: 0) started at 2023-07-29 12:00:00'),
            call('Arguments: "1", int, "1", "0", int, "0"')
        ]
        mock_logger_info.assert_has_calls(expected_info_calls, any_order=False)

        mock_logger_error.assert_called_once_with('Function divide (Index: 0) raised an error: division by zero')

if __name__ == '__main__':
    unittest.main()
