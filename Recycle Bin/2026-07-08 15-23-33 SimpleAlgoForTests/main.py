from QuantConnect import *
from QuantConnect.Algorithm import *
from QuantConnect.Data.Market import OptionChain, Tick
from datetime import timedelta
from decorators import FunctionLogger  # Assuming the FunctionLogger is in the same project folder


class MonthlySPYCallOptionsAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash

        equity = self.AddEquity("SPY", Resolution.Minute)
        self.symbol = equity.Symbol

        # Add the option contract and use its canonical symbol
        option = self.AddOption("SPY")
        self.option_symbol = option.Symbol

        # Set our filter for the option chain
        option.SetFilter(-2, 2, timedelta(days=21), timedelta(days=42))

        self.SetBenchmark("SPY")

        # Schedule the buying of options on the first trading day of each month
        self.Schedule.On(self.DateRules.MonthStart("SPY"), self.TimeRules.AfterMarketOpen("SPY"), self.BuyOptions)

        # Store the expiration of the current option position
        self.current_option_expiry = None

        # Instantiate FunctionLogger with the algorithm instance
        self.function_logger = FunctionLogger(self)

        self.Debug("Algorithm initialized")

    @FunctionLogger.log
    def OnData(self, slice):
        # Log the types of slice we're receiving
        self.Debug(f"Received slice types: {', '.join(slice.Keys)}")

        if self.option_symbol in slice.OptionChains:
            chain = slice.OptionChains[self.option_symbol]
            self.Debug(f"Received option chain with {len(chain)} contracts")

        # Check if we need to close the current option position
        if self.current_option_expiry is not None:
            days_to_expiry = (self.current_option_expiry - self.Time).days
            self.Debug(f"Current option expires in {days_to_expiry} days")
            if days_to_expiry <= 2:  # Close position 2 days before expiration
                self.Liquidate()
                self.Debug(f"Liquidated position {days_to_expiry} days before expiry")
                self.current_option_expiry = None

    @FunctionLogger.log
    def BuyOptions(self):
        self.Debug("BuyOptions method called")

        # Request option chain slice
        chain = self.CurrentSlice.OptionChains.get(self.option_symbol)
        if chain is None or len(chain) == 0:
            self.Debug("No option chain slice available in CurrentSlice")
            return

        self.Debug(f"Option chain contains {len(chain)} contracts")

        # Get ATM strike
        underlying_price = self.Securities[self.symbol].Price
        self.Debug(f"Underlying price: {underlying_price}")
        atm_strike = min(chain, key=lambda x: abs(x.Strike - underlying_price)).Strike
        self.Debug(f"ATM strike selected: {atm_strike}")

        # Find a call option that expires in 3-6 weeks
        expiry_range = (self.Time + timedelta(weeks=3), self.Time + timedelta(weeks=6))
        self.Debug(f"Looking for options expiring between {expiry_range[0]} and {expiry_range[1]}")
        valid_options = [x for x in chain if x.Expiry >= expiry_range[0] and x.Expiry <= expiry_range[1]
                         and x.Strike == atm_strike and x.Right == OptionRight.Call]

        self.Debug(f"Found {len(valid_options)} valid options")
        if not valid_options:
            self.Debug("No valid options found")
            return

        # Select the option with the highest liquidity (open interest)
        selected_option = max(valid_options, key=lambda x: x.OpenInterest)
        self.Debug(
            f"Selected option: {selected_option.Symbol}, Expiry: {selected_option.Expiry}, OpenInterest: {selected_option.OpenInterest}")

        # Calculate the quantity based on 5% of our portfolio value
        option_price = selected_option.LastPrice
        quantity = self.Portfolio.TotalPortfolioValue * 0.05 / (option_price * 100)
        quantity = int(quantity)  # Round down to nearest whole contract
        self.Debug(f"Calculated quantity: {quantity}, Option price: {option_price}")

        if quantity > 0:
            # Place the order and store the expiration
            order = self.MarketOrder(selected_option.Symbol, quantity)
            self.Debug(f"Placed order: {order}")
            self.current_option_expiry = selected_option.Expiry
        else:
            self.Debug("Quantity is 0, no order placed")

    @FunctionLogger.log
    def OnOrderEvent(self, orderEvent):
        self.Debug(f"Order Event: {orderEvent}")

    @FunctionLogger.log
    def OnEndOfAlgorithm(self):
        self.Debug("Algorithm completed")
        self.Debug(f"Final Portfolio Value: {self.Portfolio.TotalPortfolioValue}")
