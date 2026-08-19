# region imports
import sys
import os
import random
import datetime as dt

# Ensure Library/PropietaryCode is resolvable in local LEAN Docker container environments
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_WORKSPACE_DIR = os.path.abspath(os.path.join(_THIS_DIR, ".."))
_LIBRARY_DIR = os.path.join(_WORKSPACE_DIR, "Library")

for path_dir in [_WORKSPACE_DIR, _LIBRARY_DIR, _THIS_DIR]:
    if path_dir not in sys.path:
        sys.path.insert(0, path_dir)

from AlgorithmImports import *
from PropietaryCode import (
    log_trade_entry,
    log_trade_exit,
    monitor_execution,
    measure_memory_usage
)
# endregion


class AlgoTester(QCAlgorithm):
    """
    0AT — Fire-Ring Decorator & Logging Stress Test Algorithm
    
    Purpose:
      Simulates randomized trading strategies with arbitrary dynamic indicators
      (RSI, Z-Score, Momentum, Volatility, Moving Avg Ratio) to stress-test:
        1. @log_trade_entry and @log_trade_exit decorators across multiple exit reasons.
        2. @monitor_execution timing and process memory tracking without backtest failures.
        3. Standardized [BIGQUERY_TRADE_RECORD] emission with low/zero 'Other' categories.
    """

    def Initialize(self):
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        
        initial_amount = self.GetParameter("exec.initial_amount")
        initial_cash = float(initial_amount) if initial_amount else 100000.0
        self.SetCash(initial_cash)

        # Standard algorithm metadata required by logging decorators
        self.algo_code = "0AT"
        self.backtest_run_id = f"0AT_{self.Time.strftime('%Y%m%d_%H%M%S')}_FIRERING"

        # Asset subscriptions
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.qqq = self.AddEquity("QQQ", Resolution.Daily).Symbol
        self.symbols = [self.spy, self.qqq]

        self.SetBenchmark("SPY")

        # Track active positions & custom indicators
        self.active_test_positions = {}

        # Schedule periodic trade evaluations every trading day at 10:00 AM
        self.Schedule.On(
            self.DateRules.EveryDay("SPY"),
            self.TimeRules.AfterMarketOpen("SPY", 30),
            self.RunFireRingCycle
        )

        self.Log(f"[{self.Time}] 0AT Fire-Ring Test Algorithm Initialized. RunID={self.backtest_run_id}")

    @monitor_execution
    def OnData(self, data: Slice):
        """Monitors daily data slice and logs execution stats."""
        # Plot portfolio value safely
        self.Plot("Portfolio Value", "Equity", self.Portfolio.TotalPortfolioValue)

    @monitor_execution
    def RunFireRingCycle(self):
        """
        Daily execution engine:
          1. Evaluates random dynamic indicators against dynamic thresholds.
          2. Opens positions for uninvested assets via @log_trade_entry.
          3. Evaluates open positions and liquidates via @log_trade_exit with explicit exit tags.
        """
        for symbol in self.symbols:
            symbol_str = symbol.Value

            # If already invested, evaluate for random exit condition
            if self.Portfolio[symbol].Invested and symbol_str in self.active_test_positions:
                self.EvaluateAndExitPosition(symbol)
            elif not self.Portfolio[symbol].Invested:
                # Evaluate entry condition with random dynamic indicators
                self.EvaluateAndEnterPosition(symbol)

    @monitor_execution
    def GenerateRandomIndicators(self) -> dict:
        """
        Generates arbitrary dynamic indicators and random thresholds.
        Does NOT rely on 4EVC-specific metrics (vol_ratio, slope, ivrv_ratio).
        """
        return {
            "rsi": round(random.uniform(20.0, 80.0), 2),
            "zscore": round(random.uniform(-3.0, 3.0), 3),
            "momentum_pct": round(random.uniform(-0.08, 0.08), 4),
            "moving_avg_ratio": round(random.uniform(0.92, 1.08), 4),
            "signal_strength": round(random.uniform(0.1, 1.0), 3),
            "volatility_ann": round(random.uniform(0.10, 0.45), 3),
            "random_threshold": round(random.uniform(0.40, 0.70), 3)
        }

    @monitor_execution
    @log_trade_entry
    def ExecuteTradeEntry(self, underlying: Symbol, front: Symbol, back: Symbol, qty: int, metrics: dict):
        """
        Decorated trade entry handler.
        Submits market order and logs [BIGQUERY_TRADE_RECORD] OPEN record.
        """
        price = self.Securities[underlying].Price
        if price <= 0:
            price = 100.0
            
        self.last_entry_price = float(price)
        
        # Save position tracking details
        self.active_test_positions[underlying.Value] = {
            "entry_time": self.Time,
            "entry_price": self.last_entry_price,
            "metrics": metrics,
            "qty": qty
        }
        
        self.MarketOrder(underlying, qty)
        self.Log(f"[{self.Time}] 0AT OPEN trade on {underlying.Value} at ${self.last_entry_price:.2f}. Metrics={metrics}")

    @monitor_execution
    @log_trade_exit
    def LiquidateTestPosition(self, underlying: Symbol, tag: str):
        """
        Decorated trade liquidation handler.
        Offsetting order that liquidates position with explicit exit tags.
        """
        price = self.Securities[underlying].Price
        pos_data = self.active_test_positions.get(underlying.Value, {})
        entry_price = pos_data.get("entry_price", price)

        self.last_exit_price = float(price)
        if entry_price > 0:
            self.last_pnl = (self.last_exit_price - entry_price) / entry_price
        else:
            self.last_pnl = 0.0

        self.Liquidate(underlying, tag=tag)
        
        if underlying.Value in self.active_test_positions:
            del self.active_test_positions[underlying.Value]
            
        self.Log(f"[{self.Time}] 0AT CLOSE trade on {underlying.Value} at ${self.last_exit_price:.2f}. Tag='{tag}' | PnL={self.last_pnl*100:.2f}%")

    def EvaluateAndEnterPosition(self, symbol: Symbol):
        """Evaluates random dynamic indicators against thresholds to open position."""
        indicators = self.GenerateRandomIndicators()
        threshold = indicators["random_threshold"]

        # Signal trigger condition
        if indicators["signal_strength"] > (threshold * 0.5):
            qty = random.randint(10, 50)
            self.ExecuteTradeEntry(symbol, symbol, None, qty, indicators)

    def EvaluateAndExitPosition(self, symbol: Symbol):
        """
        Evaluates position and liquidates under explicit, descriptive exit reasons
        to guarantee low/zero 'Other' classification in BigQuery.
        """
        pos_data = self.active_test_positions.get(symbol.Value, {})
        entry_time = pos_data.get("entry_time", self.Time)
        holding_days = (self.Time - entry_time).days

        current_price = self.Securities[symbol].Price
        entry_price = pos_data.get("entry_price", current_price)
        
        if entry_price > 0:
            unrealized_return = (current_price - entry_price) / entry_price
        else:
            unrealized_return = 0.0

        # Deterministic exit scenario selection to test all categories
        rand_roll = random.random()

        if unrealized_return <= -0.03 or rand_roll < 0.15:
            tag = f"Stop Loss Triggered ({unrealized_return*100:.2f}% loss threshold crossed)"
            self.LiquidateTestPosition(symbol, tag)
            
        elif unrealized_return >= 0.05 or rand_roll < 0.30:
            tag = f"Take Profit Target Achieved ({unrealized_return*100:.2f}% profit gain reached)"
            self.LiquidateTestPosition(symbol, tag)
            
        elif holding_days >= 14 or rand_roll < 0.45:
            tag = f"Time-Based Exit (Holding period limit of {holding_days} days reached)"
            self.LiquidateTestPosition(symbol, tag)
            
        elif rand_roll < 0.70:
            tag = f"Signal Reversion (Dynamic indicator crossed threshold {rand_roll:.2f})"
            self.LiquidateTestPosition(symbol, tag)
            
        elif rand_roll < 0.80:
            tag = f"Risk Margin Reduction (Portfolio risk allocation cap)"
            self.LiquidateTestPosition(symbol, tag)
            
        elif rand_roll < 0.88:
            tag = f"DTE Safety Expiry Close"
            self.LiquidateTestPosition(symbol, tag)

        elif rand_roll < 0.94:
            tag = f"Option Assignment (Assigned stock liquidation post-ITM exercise)"
            self.LiquidateTestPosition(symbol, tag)

        elif rand_roll < 1.00:
            tag = f"Margin Call Warning: Force Liquidation Order"
            self.LiquidateTestPosition(symbol, tag)

    def OnAssignment(self, assignmentEvent: Any) -> None:
        """
        QuantConnect event triggered upon ITM option assignment.
        Liquidates assigned underlying stock immediately to prevent unwanted equity exposure.
        """
        symbol = getattr(assignmentEvent, "Symbol", None)
        if symbol:
            underlying = getattr(symbol, "Underlying", symbol)
            self.Log(f"[{self.Time}] OPTION ASSIGNED on {symbol.Value}. Liquidating assigned stock...")
            if hasattr(self, "LiquidateTestPosition"):
                self.LiquidateTestPosition(underlying, f"Option Assignment (Post-ITM Exercise of {symbol.Value})")

    def OnFrameworkEnd(self) -> None:
        """
        QuantConnect event triggered when backtest execution completes.
        Saves all accumulated trade records into self.ObjectStore.
        """
        save_trade_buffer_to_object_store(self)
