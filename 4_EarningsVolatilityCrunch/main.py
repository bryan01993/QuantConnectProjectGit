# region imports
from AlgorithmImports import *
from math import sqrt
from datetime import timedelta
from QuantConnect.Algorithm.Selection import OptionChainedUniverseSelectionModel
from QuantConnect.Securities.Option import OptionStrategies, OptionDataFilter
from QuantConnect.Orders.Fees import InteractiveBrokersFeeModel
from PropietaryCode.decorators import monitor_execution, measure_memory_usage
# Import alt-data for upcoming earnings
from QuantConnect import Securities
from QuantConnect.DataSource import EODHDUpcomingEarnings


# endregion

class EarningsVolatilityCrunch(QCAlgorithm):
    def Initialize(self):
        # ------------------
        # 1) Basic Algo Settings
        # ------------------
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        self.SetCash(self.GetParameter("exec.initial_amount"))

        # Use a daily resolution in this example
        # self.SetSecurityInitializer(self.CustomSecurityInitializer)
        self.OptionFilterUniverse()
        self.add_universe_options()
        # We will add a coarse universe that picks up stocks with
        # (1) Price below 100
        # (2) Next earnings date within the next 5 days
        # Then we'll dynamically add Options for them.
        # Simple risk management (placeholder):
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.05))

        # Remove references to coarse/fine Universe,
        # and instead use EODHDUpcomingEarnings alt-data.
        self.AddUniverse(EODHDUpcomingEarnings, self.EODUpcomingFilter)

    @monitor_execution
    def EODUpcomingFilter(self, data):
        """
        data is a list of EODHDUpcomingEarnings objects.
        We'll pick those with upcoming earnings date in the next 5 days.
        We'll do the Price < 100 check in OnSecuritiesChanged.
        """
        symbols = []
        for d in data:
            if d.ReportDate is None:
                continue
            days_to_announcement = (d.ReportDate.date() - self.Time.date()).days
            if 0 <= days_to_announcement <= 5:
                symbols.append(d.Symbol)
        return symbols

    @monitor_execution
    def OnData(self, slice):
        """
        Called each data slice. We'll gather each OptionChain in slice.OptionChains
        and pass it to create_calendar_spread.
        """
        if not slice.OptionChains:
            return

        for symbol, chain in slice.OptionChains.items():
            if chain and chain.Contracts.Count > 0:
                contracts_list = list(chain.Contracts.Values)
                self.create_calendar_spread(contracts_list)

    @monitor_execution
    def OnSecuritiesChanged(self, changes):
        """
        Called each time our universe changes (some stocks are added or removed).
        We'll add the Options for the new stocks here, ignoring weeklies,
        and filter for the chain that expires after the earnings date
        plus the following chain.
        This logic is somewhat simplified for demonstration.
        """
        for security in changes.AddedSecurities:
            # Add an Option chain for each new stock
            if security.Symbol.SecurityType == SecurityType.EQUITY:
                option = self.AddOption(security.Symbol.Value,resolution=Resolution.DAILY)
                # By default it returns a Security object for the option, we can further configure
                option.SetFilter(self.OptionChainFilter)

        for security in changes.RemovedSecurities:
            # If an equity is removed from the universe, we can remove the corresponding option
            if security.Symbol.SecurityType == SecurityType.Equity:
                # Clean up any positions or remove the Option from the algo
                # if no longer needed.
                pass

    @monitor_execution
    def OptionChainFilter(self, universe):
        """
        We want:
        - No weekly expirations
        - Only the first two expiration dates
        - 2 strikes up and down from the current ATM
        The idea is to keep the minimum amount of contracts so we don't overload memory.
        """
        # Exclude weekly expirations
        # universe = universe.ExcludeWeeklys()
        OptionChainedUniverseSelectionModel()
        # Keep only the earliest 2 monthly expirations.
        # We can do so by using a lambda that sorts the available expiry dates and picks the first 2.
        universe.Expiration(timedelta(0), timedelta(30))

        # Then filter to only ±2 strikes from the current ATM strike.
        # We'll use Strikes(-2, 2) for that purpose.
        universe = universe.Strikes(-2, 2)

        return universe

    @monitor_execution
    def CustomSecurityInitializer(self, security):
        """
        We can set some custom properties on the newly added securities,
        e.g. leverage or fee model, if we want.
        """
        # Example: security.SetLeverage(2.0)
        pass

    # -----------------------------------
    #  Empty function placeholders
    # -----------------------------------
    @monitor_execution
    def calculate_iv_slope(self, near_contract, far_contract):
        """
        Computes an implied-volatility slope between two option contracts
        with the same strike but different expirations.

        The 'slope' is treated as the hypotenuse of:
           ( horizontal difference ) = daysBetweenExpirations
           ( vertical difference   ) = diff in implied vol

        Returns a tuple or dict with:
            {
              'near_contract': near_contract,
              'far_contract': far_contract,
              'slope': <float>
            }
        """

        # We assume near_contract.Expiry < far_contract.Expiry
        diff_days = (far_contract.Expiry.date() - near_contract.Expiry.date()).days
        diff_iv = far_contract.ImpliedVolatility - near_contract.ImpliedVolatility

        # Hypotenuse
        slope = sqrt(diff_days ** 2 + diff_iv ** 2)

        return {
            "near_contract": near_contract,
            "far_contract": far_contract,
            "slope": slope
        }

    @monitor_execution
    def create_calendar_spread(self, option_chain):
        """
        Identify the top 10 contract pairs with the most negative IV slope.
        A negative slope means near-term IV is higher than far-term IV.

        1. For each strike, find near-expiry vs. far-expiry contracts of the same type.
        2. Compute slope using 'calculate_iv_slope'.
        3. Sort by slope ascending (most negative slope first).
        4. Take top 10.
        5. For each pair, place orders: Sell near, Buy far.
        """
        if not option_chain:
            return

        # 1) Collect all calls/puts grouped by strike.
        calls_by_strike = {}
        puts_by_strike = {}
        for contract in option_chain:
            if contract.Right == OptionRight.CALL:
                if contract.Strike not in calls_by_strike:
                    calls_by_strike[contract.Strike] = []
                calls_by_strike[contract.Strike].append(contract)
            else:  # Put
                if contract.Strike not in puts_by_strike:
                    puts_by_strike[contract.Strike] = []
                puts_by_strike[contract.Strike].append(contract)

        # 2) We'll define a small helper to find pairs of near/far for a list of contracts of same strike.
        def find_slope_pairs(contracts):
            # sort by expiration ascending
            c_sorted = sorted(contracts, key=lambda x: x.Expiry)
            pairs = []
            # compare each possible pair (near, far)
            for i in range(len(c_sorted)):
                for j in range(i + 1, len(c_sorted)):
                    near_c = c_sorted[i]
                    far_c = c_sorted[j]
                    # compute slope
                    slope_info = self.calculate_iv_slope(near_c, far_c)
                    pairs.append(slope_info)
            return pairs

        # 3) We'll gather all slope pairs across calls and puts.
        slope_pairs = []
        # calls:
        for strike, c_list in calls_by_strike.items():
            if len(c_list) < 2:
                continue
            slope_pairs.extend(find_slope_pairs(c_list))
        # puts:
        for strike, p_list in puts_by_strike.items():
            if len(p_list) < 2:
                continue
            slope_pairs.extend(find_slope_pairs(p_list))

        if len(slope_pairs) == 0:
            return

        # 4) Sort by slope ascending (the more negative, the better)
        slope_pairs.sort(key=lambda x: x["slope"])

        # 5) Take top 10
        best_10 = slope_pairs[:10]

        # 6) Place trades: Sell near, Buy far
        for sp in best_10:
            near_c = sp["near_contract"]
            far_c = sp["far_contract"]
            slope_val = sp["slope"]

            # sanity check: if near_c or far_c is None, skip
            if not near_c or not far_c:
                continue

            # We'll do 1-lot, but you might want to do more.
            self.Debug(
                f"Creating calendar spread on {near_c.Underlying.Symbol} Strike={near_c.Strike}, Slope={slope_val}")

            # Sell near
            self.MarketOrder(near_c.Symbol, -1)
            # Buy far
            self.MarketOrder(far_c.Symbol, +1)

        return
