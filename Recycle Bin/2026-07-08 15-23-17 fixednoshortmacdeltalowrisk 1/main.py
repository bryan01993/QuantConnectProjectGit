from AlgorithmImports import *
from ContinuousMACDSignalGenerator import MACDSignalGenerator
from AssetWeightCalculator import AssetWeightCalculator

class TestMACDInitializationAlgorithm(QCAlgorithm):
    def Initialize(self):
        """
        Things to add:
        1. Warmup period for asset selector
        2. Initialization with warmed up assets
        """
        self.set_start_date(2012, 1, 1)
        self.set_cash(1000000)
        self.set_benchmark("SPY")
        
        # Set maximum leverage to 1 (no leverage)
        self.universe_settings.leverage = 1
        
        self.bond_etf = self.add_equity("BIL", Resolution.HOUR)
        self.spy = self.add_equity("SPY", Resolution.HOUR)   

        # Initialize tracking set for universe changes
        self.current_symbols = set() 
        
        # Initialize the asset weight calculator
        self.asset_calculator = AssetWeightCalculator(self)

        # Add universe for coarse and fine selection
        self.spy = self.add_equity("SPY", Resolution.HOUR)
        self.add_universe(self.asset_calculator.coarse_selection, self.asset_calculator.fine_selection)

        # Universe settings
        self.universe_settings.Resolution = Resolution.HOUR

        # Initialize MACD generator 
        self.macd_generator = MACDSignalGenerator(self, [])

        # Scheduled ranking update
        self.schedule.on(self.date_rules.week_start("SPY"), 
                         self.time_rules.after_market_open("SPY", 1), 
                         self.rank_and_update_symbols
                        )
        
        # Schedule Monday 10:36 rebalancing
        self.schedule.on(
                        self.date_rules.week_start("SPY"),
                        self.time_rules.after_market_open("SPY", 65),
                        self.rebalance_positions
                        )


    def rank_and_update_symbols(self):

        # Skip during warmup
        if self.is_warming_up:
            self.debug("Skipping rank_and_update during warmup")
            return

        # Log current state
        owned_symbols = [symbol for symbol in self.portfolio.keys() if self.portfolio[symbol].quantity > 0]
        self.debug(f"Currently owned symbols: {[s.value for s in owned_symbols]}")

        # Get new universe, excluding tracking symbols and limiting to 20
        excluded_symbols = {"BIL", "SPY"}
        new_symbols = set(s.key for s in self.active_securities 
                        if s.key.value not in excluded_symbols)
        new_symbols = set(list(new_symbols)[:20])
        
        self.debug(f"New universe symbols: {[s.value for s in new_symbols]}")
        
        # Handle removals first
        removed_symbols = self.current_symbols - new_symbols
        if removed_symbols:
            self.debug(f"Removing symbols: {[x.value for x in removed_symbols]}")
            self.macd_generator.remove_symbols(list(removed_symbols))
            # Double-check liquidation
            for symbol in removed_symbols:
                if self.portfolio.contains_key(symbol) and self.portfolio[symbol].invested:
                    self.liquidate(symbol)
        
        # Then handle additions
        added_symbols = new_symbols - self.current_symbols
        if added_symbols:
            self.debug(f"Adding symbols: {[x.value for x in added_symbols]}")
            self.macd_generator.add_symbols(list(added_symbols))
        
        # Update tracking set
        self.current_symbols = new_symbols
        
        # Verify final state
        self.debug(f"Final universe size: {len(self.current_symbols)}")
        self.debug(f"MACD symbols count: {len(self.macd_generator.symbols)}")
        
        # Verify alignment
        if self.current_symbols != self.macd_generator.symbols:
            self.debug("WARNING: Universe and MACD symbols misaligned!")
            self.debug(f"Universe only: {[s.value for s in self.current_symbols - self.macd_generator.symbols]}")
            self.debug(f"MACD only: {[s.value for s in self.macd_generator.symbols - self.current_symbols]}")

    def rebalance_positions(self):
        """Actual position rebalancing 64 mins after re-ranking"""
        if self.is_warming_up:
            return

        # Get current positions that shouldn't be there
        invalid_positions = [symbol for symbol in self.portfolio.keys() 
                            if symbol not in self.macd_generator.symbols 
                            and self.portfolio[symbol].invested
                            and symbol.Value not in ["BIL", "SPY"]] # This could end up being inefficient where liquidation occurs when loading up on size
        
        # Liquidate invalid positions
        for symbol in invalid_positions:
            self.debug(f"Liquidating invalid position: {symbol.value}")
            self.liquidate(symbol)

        # Calculate new positions
        position_sizes = self.macd_generator.calculate_position_sizes()

        # Verify we're only trading valid symbols
        for symbol in list(position_sizes.keys()):
            if symbol not in self.macd_generator.symbols:
                self.debug(f"WARNING: Position calculated for non-MACD symbol: {symbol.value}")
                del position_sizes[symbol]

        # Build target weights for all assets
        target_weights = {}
        total_equity_weight = 0
        for symbol, variants in position_sizes.items():
            security = self.securities[symbol]
            if not security.has_data or not security.is_tradable:
                continue
            total_size = sum(variants.values())
            if abs(total_size) > 0.001:
                target_weights[symbol] = total_size
                total_equity_weight += total_size

        # Set bond weight as the remainder, but never negative
        bond_weight = max(0, 1 - total_equity_weight)
        target_weights[self.bond_etf.symbol] = bond_weight

        # Normalize weights if total > 1.0
        total_weight = sum(target_weights.values())
        if total_weight > 1.0:
            self.debug(f"Total target weight {total_weight} > 1.0, normalizing weights.")
            for symbol in target_weights:
                target_weights[symbol] /= total_weight

        # Set all holdings in one pass
        for symbol, weight in target_weights.items():
            self.set_holdings(symbol, weight)

        # Log the current portfolio
        invested_value = self.portfolio.total_portfolio_value
        self.debug(f"Portfolio value: {invested_value}")
        self.debug(f"Bond weight: {bond_weight}")

        # Final verification
        actual_positions = [s for s in self.portfolio.keys() 
                        if self.portfolio[s].invested 
                        and s.value not in ["BIL", "SPY"]]
        self.debug(f"Positions after rebalance: {len(actual_positions)}")
        self.debug(f"Position symbols: {[s.value for s in actual_positions]}")

        self.debug(f"Bond position set to {self.portfolio[self.bond_etf.symbol].quantity} shares of {self.bond_etf.symbol.value}")
        self.debug(f"Cash remaining: {self.portfolio.cash}")
        self.debug(f"Amount in equities: {self.portfolio.total_portfolio_value - self.portfolio.cash - self.portfolio[self.bond_etf.symbol].quantity * self.bond_etf.price}")
