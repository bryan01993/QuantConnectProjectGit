from AlgorithmImports import *

class MACDSignalGenerator:

    def __init__(self, algorithm: QCAlgorithm, symbols: list, cash_buffer: float = 0.05):
        self.algorithm = algorithm
        self.symbols = set(symbols)
        self.cash_buffer = cash_buffer
        self.macd_indicators = {}  # {symbol: {variant: MACD}}
            
        # Define MACD parameters for different variants
        self.macd_variants = {
            "slow": {"fast": 12, "slow": 26, "signal": 9},
            "slow-med": {"fast": 9, "slow": 19, "signal": 5},
            "med-fast": {"fast": 7, "slow": 15, "signal": 3},
            "fast": {"fast": 5, "slow": 12, "signal": 2},
        }

    def remove_symbols(self, symbols: list):
        """
        Removes MACD indicators for the specified symbols.
        """
        for symbol in symbols:
            if symbol in self.macd_indicators:
                for variant, macd in self.macd_indicators[symbol].items():
                    self.algorithm.unregister_indicator(macd)
                    self.algorithm.debug(f"Unregistering {symbol.value} {variant} MACD indicator")
                del self.macd_indicators[symbol]
            
            # Remove from symbols set
            self.symbols.discard(symbol)
            
            # Liquidate position
            if self.algorithm.portfolio.contains_key(symbol):
                self.algorithm.liquidate(symbol)

    def add_symbols(self, new_symbols):
            """
            Add in the new symbols that are given by AssetWeightCalculator.
            """

            # Convert to set for efficient operations
            new_symbols = set(new_symbols)
            
            # Only process truly new symbols
            actually_new = new_symbols - self.symbols
            
            if not actually_new:
                return

            # Get historical data for new symbols
            history = self.algorithm.history([s for s in new_symbols], 
                                        35,  # Longest MACD period needed
                                        Resolution.HOUR)
            
            for symbol in actually_new:

                # Check if security has data
                if not self.algorithm.securities[symbol].has_data:
                    self.algorithm.debug(f"Waiting for data: {symbol.value}")
                    continue


                self.macd_indicators[symbol] = {}

                # Check if no history
                if symbol not in history.index.get_level_values(0):
                    self.algorithm.log(f"No History for adding")
                    continue
                    
                symbol_history = history.loc[symbol]

                for variant, params in self.macd_variants.items():
                    macd = self.algorithm.macd(
                        symbol=symbol,
                        fast_period=params["fast"], 
                        slow_period=params["slow"], 
                        signal_period=params["signal"], 
                        type=MovingAverageType.EXPONENTIAL,
                        resolution=Resolution.HOUR,
                        selector=Field.CLOSE
                    )

                    # Warm up MACD with historical data
                    for time, row in symbol_history.iterrows():
                        macd.update(time, row['close'])
                        
                    self.macd_indicators[symbol][variant] = macd
                    self.algorithm.log(f"Adding macd: {symbol} and {variant}")

                # Only add symbol after proper setup
                self.symbols.add(symbol)

    def calculate_position_sizes(self):
        position_sizes = {}
        max_position_limit = 0.1

        # Check if we have any symbols to process
        if not self.symbols or not self.macd_indicators:
            self.algorithm.debug("No symbols available for position calculation")
            return position_sizes
        
        # Calculate base position size
        max_position = (1 - self.cash_buffer) / (len(self.symbols) * len(self.macd_variants))

        total_portfolio_allocation = 0  # Track total allocation

        for symbol in self.macd_indicators:
            position_sizes[symbol] = {}
            symbol_total = 0  # Track total for this symbol

            for variant, macd in self.macd_indicators[symbol].items():
                if macd.is_ready:
                    security = self.algorithm.securities[symbol]

                    if not security.has_data or not security.is_tradable:
                        self.algorithm.debug(f"Security not ready: {symbol.value}")
                        continue

                    # Distance between fast and slow
                    distance = macd.fast.current.value - macd.slow.current.value

                    # Calculate initial position size
                    position_size = max_position * (distance / macd.slow.current.value) * 350  # Your scalar
                    
                    # Ensure non-negative and within variant limit
                    position_size = max(0, min(position_size, max_position))
                    
                    position_sizes[symbol][variant] = position_size
                    symbol_total += position_size
                else:
                    position_sizes[symbol][variant] = 0

            # If symbol total exceeds max limit, scale down proportionally
            if symbol_total > max_position_limit:
                scale_factor = max_position_limit / symbol_total
                for variant in position_sizes[symbol]:
                    position_sizes[symbol][variant] *= scale_factor
                symbol_total = max_position_limit

            total_portfolio_allocation += symbol_total

        # If total allocation exceeds 100%, scale everything down proportionally
        if total_portfolio_allocation > 1:
            scale_factor = 1 / total_portfolio_allocation
            for symbol in position_sizes:
                for variant in position_sizes[symbol]:
                    position_sizes[symbol][variant] *= scale_factor

        # Log position sizes for verification
        for symbol in position_sizes:
            total_size = sum(position_sizes[symbol].values())
            if total_size > max_position_limit:
                self.algorithm.debug(f"WARNING: {symbol.value} position size {total_size:.3f} exceeds limit")

        return position_sizes
