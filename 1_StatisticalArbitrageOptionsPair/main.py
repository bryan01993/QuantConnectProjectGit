from AlgorithmImports import *
import math
import numpy as np
from datetime import timedelta


class IronCondorAlgorithm(QCAlgorithm):

    def Initialize(self):
        """
        Initialize the algorithm settings, universe, and any helper structures.
        """
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2024, 12, 31)
        self.SetCash(10000)

        # 1. Universe Selection: We'll pick SPY for demonstration
        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.option = self.AddOption("SPY", Resolution.Daily)

        # Set the option's filter for strikes and expirations
        # e.g., filter for expirations up to 60 days out and strikes +/- 30 from ATM
        self.option.SetFilter(-30, +30, timedelta(0), timedelta(days=60))

        # 2. Rolling window for Realized Volatility (30 days)
        self.lookback = 30
        self.priceWindow = RollingWindow[float](self.lookback)

        # Keep track of whether we have an open Iron Condor
        self.ironCondorPositionOpen = False

        # Threshold for (IV - RV) to enter Iron Condor
        self.volThreshold = 0.05  # 5 percentage points for demonstration

        # This is how frequently OnData() or OnData(slice) will run
        self.SetWarmUp(self.lookback)
        self.SetBenchmark(self.symbol)

        # For demonstration: we'll store an ID or reference for the opened Iron Condor
        self.currentIronCondor = None

    def OnData(self, slice):
        """
        Main event handler. Runs on every data 'slice'. We'll do:
          - Update Realized Vol
          - Estimate Implied Vol
          - Compare IV vs. RV
          - If signal, open Iron Condor
          - Risk management checks
        """
        # ----- Update Realized Vol Rolling Window -----
        bar = slice.Bars.get(self.symbol, None)
        if bar is not None:
            self.priceWindow.Add(bar.Close)

        # We need enough history to compute realized vol
        if not self.priceWindow.IsReady:
            return

        # ----- Compute Realized Volatility (RV) -----
        realized_vol = self.ComputeRealizedVolatility()

        # ----- Get Option Chain and Implied Vol (IV) -----
        # Use .get() instead of .GetValue() to avoid TypeError
        chain = slice.OptionChains.get(self.option.Symbol, None)
        if chain is None:
            return

        # Estimate near-term ATM IV from the chain
        # (This is a placeholder function. In practice, you'll find near-ATM strikes
        #  and invert Black-Scholes or use a custom data feed for IV.)
        implied_vol = self.ComputeImpliedVolatility(chain)

        if implied_vol is None or implied_vol <= 0:
            return

        # ----- Alpha Logic: Check IV - RV -----
        diff = implied_vol - realized_vol

        # If we do NOT have an open Iron Condor, check if we should enter
        if not self.ironCondorPositionOpen and diff > self.volThreshold:
            # Signal = ShortVol -> create Iron Condor
            self.Debug(f"ShortVol Signal: IV({implied_vol:.2f}) - RV({realized_vol:.2f}) = {diff:.2f}")
            self.OpenIronCondor(chain)

        # ----- Risk Management & Profit-Taking -----
        if self.ironCondorPositionOpen:
            self.ManageIronCondorPosition()

    def ComputeRealizedVolatility(self):
        """
        Compute a simple 30-day realized volatility from the RollingWindow of prices.
        Using daily log returns, annualized by sqrt(252).
        """
        log_returns = []
        # Build daily log returns from rolling window data
        for i in range(1, self.priceWindow.Count):
            p0 = self.priceWindow[i - 1]
            p1 = self.priceWindow[i]
            if p0 > 0 and p1 > 0:
                lr = math.log(p1 / p0)
                log_returns.append(lr)

        if len(log_returns) < 2:
            return 0

        # Standard deviation of daily log returns
        std_dev = np.std(log_returns)
        # Annualize (assuming ~252 trading days)
        realized_vol = std_dev * math.sqrt(252)

        return realized_vol

    def ComputeImpliedVolatility(self, chain):
        """
        Placeholder function to estimate near-ATM implied volatility from the option chain.
        In a real scenario, you might:
          1) Filter for near expiration (e.g. 20-40 days).
          2) Pick near-ATM calls/puts.
          3) Use a numerical solver or a custom data feed for IV.
        Here, we just pick an arbitrary near-ATM contract for demonstration.
        """
        # Filter chain for near expiration (e.g. ~30 days)
        near_expiry = sorted(chain, key=lambda x: x.Expiry)
        if len(near_expiry) == 0:
            return None

        # We'll pick the first expiry for demonstration
        expiry_group = [x for x in chain if (x.Expiry - self.Time).days > 20 and (x.Expiry - self.Time).days < 40]
        if len(expiry_group) == 0:
            return None

        # Sort by strike distance from current underlying price
        underlying_price = chain.Underlying.Price
        near_atm = sorted(expiry_group, key=lambda x: abs(x.Strike - underlying_price))

        if len(near_atm) == 0:
            return None

        # Just pick the first near-ATM contract
        candidate_contract = near_atm[0]

        # If you're using custom data or a built-in solver, you'd compute IV here:
        # e.g. implied_vol = self.OptionPriceModel.EstimateImpliedVolatility(candidate_contract)
        # For now, we’ll do a naive approach:
        if candidate_contract.ImpliedVolatility is not None:
            return candidate_contract.ImpliedVolatility
        else:
            return None

    def OpenIronCondor(self, chain):
        """
        Portfolio Construction & Execution:
        Pick strikes, place the four legs (ShortCall, LongCall, ShortPut, LongPut).
        """
        # Basic approach: pick an expiry ~30 days out
        expiry = None
        expiries = sorted(set([x.Expiry for x in chain]))
        for e in expiries:
            days_to_expiry = (e - self.Time).days
            if days_to_expiry >= 25 and days_to_expiry <= 35:
                expiry = e
                break
        if not expiry:
            self.Debug("No suitable expiration found for Iron Condor.")
            return

        # We'll define a 1 StdDev range around the current price for short strikes
        underlying_price = chain.Underlying.Price
        # For simplicity, let's assume 1 std dev in 30 days ~ underlying_price * (implied_vol * sqrt(30/252))
        # But we don’t have a direct implied_vol here. We'll just pick a % range for demonstration:
        width_percent = 0.03  # 3% OTM
        shortCallStrike = underlying_price * (1 + width_percent)
        shortPutStrike = underlying_price * (1 - width_percent)

        # Further OTM for the long legs
        longCallStrike = underlying_price * (1 + width_percent * 1.2)
        longPutStrike = underlying_price * (1 - width_percent * 1.2)

        # Gather the contracts
        shortCall = self.SelectContract(chain, expiry, shortCallStrike, OptionRight.Call)
        longCall = self.SelectContract(chain, expiry, longCallStrike, OptionRight.Call)
        shortPut = self.SelectContract(chain, expiry, shortPutStrike, OptionRight.Put)
        longPut = self.SelectContract(chain, expiry, longPutStrike, OptionRight.Put)

        if not shortCall or not longCall or not shortPut or not longPut:
            self.Debug("Could not find required option contracts for Iron Condor.")
            return

        # Position sizing: e.g., 1 contract for demonstration
        quantity = 1

        # Place orders (market orders for simplicity)
        self.MarketOrder(shortCall.Symbol, -quantity)  # Short Call
        self.MarketOrder(longCall.Symbol, quantity)  # Long Call
        self.MarketOrder(shortPut.Symbol, -quantity)  # Short Put
        self.MarketOrder(longPut.Symbol, quantity)  # Long Put

        self.ironCondorPositionOpen = True

        # Store a reference to manage or close later
        self.currentIronCondor = {
            "ShortCall": shortCall.Symbol,
            "LongCall": longCall.Symbol,
            "ShortPut": shortPut.Symbol,
            "LongPut": longPut.Symbol,
            "OpenTime": self.Time
        }

        self.Debug(f"Opened Iron Condor on {self.Time.date()} with expiry {expiry}")

    def SelectContract(self, chain, expiry, targetStrike, right):
        """
        Selects the nearest strike to 'targetStrike' with the given right (Put/Call) and expiry.
        """
        contracts = [x for x in chain if x.Expiry == expiry and x.Right == right]
        # Sort by absolute distance to targetStrike
        sortedByStrike = sorted(contracts, key=lambda c: abs(c.Strike - targetStrike))
        if len(sortedByStrike) > 0:
            return sortedByStrike[0]
        return None

    def ManageIronCondorPosition(self):
        """
        Basic risk management:
         - Check profit/loss on the open condor
         - Close early if we've captured ~50% of max profit (pseudo approach)
         - Check max loss condition
         - Or close near expiry
        """
        if not self.currentIronCondor:
            return

        # Example logic:
        # 1) Calculate current value vs. initial credit (we don't have that stored,
        #    so this is pseudocode).
        # 2) If near 50-75% profit, close.

        # We'll do a simple time-based exit for demonstration: exit after 2 weeks.
        openTime = self.currentIronCondor["OpenTime"]
        if (self.Time - openTime).days >= 14:
            self.Debug("Closing Iron Condor after 14 days.")
            self.CloseIronCondor()

        # You would also check if the short strikes are threatened, or if the cost
        # to close has doubled, etc. (Max loss stop logic).

    def CloseIronCondor(self):
        """
        Liquidate the existing Iron Condor position.
        """
        if not self.currentIronCondor:
            return

        for leg in self.currentIronCondor.values():
            if isinstance(leg, Symbol):
                self.Liquidate(leg)

        self.ironCondorPositionOpen = False
        self.currentIronCondor = None
        self.Debug(f"Iron Condor closed at {self.Time.date()}")
