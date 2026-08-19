"""
test_decorators_resilience.py
==============================
Resilience and Error-Injection Unit Tests for Library/PropietaryCode/decorators/

Verifies the Zero-Failure Invariant:
Under NO circumstances will logging, memory measuring, string formatting, or metric
calculations interrupt, crash, or alter the execution of a QuantConnect algorithm function.
"""

import unittest
import datetime as dt
import time
from typing import Any
from Library.PropietaryCode.decorators.perf_monitor import (
    monitor_execution,
    measure_memory_usage,
)
from Library.PropietaryCode.decorators.trade_logger import log_trade_entry, log_trade_exit, normalize_exit_reason


class MockSymbol:
    def __init__(self, value: str):
        self.Value = value


class MockQCAlgorithm:
    algo_code = "RESILIENCE_TEST"

    def __init__(self):
        self.Time = dt.datetime(2026, 7, 23, 12, 0, 0)
        self.logged_messages = []
        self.last_entry_price = 15.00
        self.last_exit_price = 18.00
        self.last_pnl = 0.20

    def Log(self, message: str):
        self.logged_messages.append(message)


class UnstringifiableObject:
    """An object whose __str__ and __repr__ explicitly raise exceptions."""
    def __str__(self):
        raise RuntimeError("Forced __str__ exception for testing")

    def __repr__(self):
        raise TypeError("Forced __repr__ exception for testing")


class ObjectWithoutLog:
    """An object that lacks a .Log() method."""
    pass


class TestDecoratorResilience(unittest.TestCase):

    def test_01_normal_execution_monitoring(self):
        """Verify normal timing and memory logging via @monitor_execution."""
        algo = MockQCAlgorithm()

        @monitor_execution
        def calculate(self_inst, x, y):
            time.sleep(0.001)
            return x + y

        result = calculate(algo, 10, 20)
        self.assertEqual(result, 30)
        self.assertEqual(len(algo.logged_messages), 1)
        self.assertIn("execution_time", algo.logged_messages[0])
        self.assertIn("memory_delta_mb", algo.logged_messages[0])

    def test_02_target_function_exception_propagation(self):
        """Verify that when target func raises an exception, the exact exception propagates naturally."""
        algo = MockQCAlgorithm()

        @monitor_execution
        def failing_func(self_inst):
            raise ValueError("Target algorithm exception")

        with self.assertRaises(ValueError) as ctx:
            failing_func(algo)
        
        self.assertEqual(str(ctx.exception), "Target algorithm exception")

    def test_03_missing_log_method_fallback(self):
        """Verify that if self lacks .Log(), no TypeError is raised and target function succeeds."""
        obj_no_log = ObjectWithoutLog()

        @monitor_execution
        def compute(self_inst, a, b):
            return a * b

        # Should execute cleanly without raising TypeError
        result = compute(obj_no_log, 6, 7)
        self.assertEqual(result, 42)

    def test_04_unstringifiable_return_value(self):
        """Verify that if return value raises exception on str/repr, function still returns cleanly."""
        algo = MockQCAlgorithm()
        bad_obj = UnstringifiableObject()

        @monitor_execution
        def get_bad_object(self_inst):
            return bad_obj

        # Should return bad_obj without throwing an exception
        res = get_bad_object(algo)
        self.assertIs(res, bad_obj)
        self.assertEqual(len(algo.logged_messages), 1)
        self.assertIn("unrepresentable result", algo.logged_messages[0])

    def test_05_generator_iterator_protection(self):
        """Verify that returning a single-use generator does NOT consume or mutate generator items."""
        algo = MockQCAlgorithm()

        def sample_generator():
            yield 1
            yield 2
            yield 3

        @monitor_execution
        def get_gen(self_inst):
            return sample_generator()

        gen_result = get_gen(algo)
        # Verify generator is intact and unconsumed
        items = list(gen_result)
        self.assertEqual(items, [1, 2, 3])

    def test_06_stacked_decorators(self):
        """Verify that stacking @log_trade_exit and @monitor_execution on the same method works seamlessly."""
        algo = MockQCAlgorithm()
        symbol = MockSymbol("NVDA")

        @monitor_execution
        @log_trade_exit
        def liquidate(self_inst, underlying, tag):
            return "liquidated"

        res = liquidate(algo, symbol, "Stop Loss Triggered (-5%)")
        self.assertEqual(res, "liquidated")
        self.assertEqual(len(algo.logged_messages), 2)
        
        # Check that both trade record and execution monitor logged messages
        trade_logs = [m for m in algo.logged_messages if "[BIGQUERY_TRADE_RECORD]" in m]
        monitor_logs = [m for m in algo.logged_messages if "execution_time" in m]
        
        self.assertEqual(len(trade_logs), 1)
        self.assertEqual(len(monitor_logs), 1)

    def test_07_high_frequency_stress_test(self):
        """Verify performance and stability across 1,000 rapid invocations."""
        algo = MockQCAlgorithm()

        @monitor_execution
        def fast_calc(self_inst, i):
            return i * 2

        start_t = time.time()
        for i in range(1000):
            fast_calc(algo, i)
        elapsed = time.time() - start_t

        self.assertEqual(len(algo.logged_messages), 1000)
        # 1,000 calls should take less than 1.0 second
        self.assertLess(elapsed, 1.0)


if __name__ == "__main__":
    unittest.main()
