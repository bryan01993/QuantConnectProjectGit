"""
test_trade_logger.py
====================
Unit tests for universal trade logging decorators in Library/PropietaryCode/decorators/trade_logger.py
"""

import unittest
import datetime as dt
from Library.PropietaryCode.decorators.trade_logger import (
    log_trade_entry,
    log_trade_exit,
    normalize_exit_reason,
)


class MockSymbol:
    def __init__(self, value: str):
        self.Value = value


class MockQCAlgorithm:
    algo_code = "TEST_ALGO"

    def __init__(self):
        self.Time = dt.datetime(2026, 7, 23, 12, 0, 0)
        self.logged_messages = []
        self.last_entry_price = 10.50
        self.last_exit_price = 12.00
        self.last_pnl = 0.14286

    def Log(self, message: str):
        self.logged_messages.append(message)


class TestTradeLogger(unittest.TestCase):

    def test_normalize_exit_reason(self):
        self.assertEqual(normalize_exit_reason("Stop Loss Triggered (-12.5% loss)"), "Stop Loss")
        self.assertEqual(normalize_exit_reason("Take Profit Reached (+25% gain)"), "Take Profit")
        self.assertEqual(normalize_exit_reason("Time-Based Exit (Post-Earnings Crush)"), "Time Exit")
        self.assertEqual(normalize_exit_reason("Leg DTE=1 Safety Expiry close"), "DTE Safety")
        self.assertEqual(normalize_exit_reason("Signal Reversion"), "Signal Exit")
        self.assertEqual(normalize_exit_reason("Option Assignment (Stock Delivered)"), "Option Assignment")
        self.assertEqual(normalize_exit_reason("Margin Call Warning: Liquidation Order"), "Margin Call")
        self.assertEqual(normalize_exit_reason("Stock Split / Merger Corporate Action"), "Corporate Action")
        self.assertEqual(normalize_exit_reason("Unrecognized tag"), "Other")

    def test_decorators_flow(self):
        algo = MockQCAlgorithm()

        @log_trade_entry
        def enter(self_inst, underlying, front, back, qty, metrics):
            return "entered"

        @log_trade_exit
        def exit(self_inst, underlying, tag):
            return "exited"

        symbol = MockSymbol("AAPL")
        metrics = {"vol_ratio": 1.25, "slope": 0.015, "ivrv_ratio": 1.10}

        result_entry = enter(algo, symbol, None, None, 5, metrics)
        self.assertEqual(result_entry, "entered")
        self.assertEqual(len(algo.logged_messages), 1)
        self.assertIn("[BIGQUERY_TRADE_RECORD]", algo.logged_messages[0])
        self.assertIn('"action":"OPEN"', algo.logged_messages[0])
        self.assertIn('"algo_code":"TEST_ALGO"', algo.logged_messages[0])

        result_exit = exit(algo, symbol, "Stop Loss Triggered (-10% loss)")
        self.assertEqual(result_exit, "exited")
        self.assertEqual(len(algo.logged_messages), 2)
        self.assertIn("[BIGQUERY_TRADE_RECORD]", algo.logged_messages[1])
        self.assertIn('"action":"CLOSE"', algo.logged_messages[1])
        self.assertIn('"exit_reason":"Stop Loss"', algo.logged_messages[1])

    def test_object_store_buffering_and_save(self):
        from Library.PropietaryCode.decorators.trade_logger import save_trade_buffer_to_object_store

        class MockObjectStore:
            def __init__(self):
                self.saved_data = {}

            def Save(self, key: str, payload: str):
                self.saved_data[key] = payload

        algo = MockQCAlgorithm()
        algo.ObjectStore = MockObjectStore()

        @log_trade_entry
        def enter(self_inst, underlying, front, back, qty, metrics):
            return "entered"

        symbol = MockSymbol("SPY")
        enter(algo, symbol, None, None, 10, {"vol_ratio": 1.5})

        self.assertTrue(hasattr(algo, "_universal_trade_buffer"))
        self.assertEqual(len(algo._universal_trade_buffer), 1)

        save_trade_buffer_to_object_store(algo)

        saved_keys = list(algo.ObjectStore.saved_data.keys())
        self.assertEqual(len(saved_keys), 1)
        self.assertEqual(saved_keys[0], "BTOPTrades_TEST_ALGO_latest.json")
        self.assertIn('"underlying": "SPY"', algo.ObjectStore.saved_data[saved_keys[0]])


if __name__ == "__main__":
    unittest.main()
