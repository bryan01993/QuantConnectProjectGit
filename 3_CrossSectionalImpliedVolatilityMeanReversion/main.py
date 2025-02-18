class CrossSectionalImpliedVolatilityMeanReversion(QCAlgorithm):

    def Initialize(self):
        """
        1) Basic QC Algorithm Setup
        """
        # a) Set Start Date, End Date, and Initial Cash
        # b) Configure Brokerage Model if needed
        # c) Define Rebalancing Frequency (Daily/Weekly)

        pass

    def OnData(self, data):
        """
        2) OnData event is called whenever new data is available
        """
        # NOTE: If using scheduled rebalancing, the main logic might not be
        # here in OnData, but instead in OnSecuritiesChanged or a scheduled event.

        # a) If rebalancing condition is not met, return
        # b) Otherwise, handle rebalancing
        pass

    def OnSecuritiesChanged(self, changes):
        """
        3) Handle additions/removals from the universe
        """
        # a) For newly added securities: warm up data, request option chain
        # b) For removed securities: liquidate or handle open positions, remove from tracking
        pass

    # ------------------------------------------------------------------------
    # 4) Universe Selection and IV Ranking
    # ------------------------------------------------------------------------
    def SelectCoarseUniverse(self, coarse):
        """
        4a) Filter for Liquid Equities:
            - e.g. top by market cap, price, or daily dollar volume
        """
        # a) Filter, sort, and select top N or M from the coarse list
        # b) Return the ticker symbols for the fine universe step
        pass

    def SelectFineUniverse(self, fine):
        """
        4b) Narrow to final set of symbols to trade:
            - e.g. remove low-priced or lightly traded shares
        """
        # a) Possibly further refine the selection
        # b) Return final symbol list
        pass

    def SelectOptionContracts(self, option_chain):
        """
        4c) Pick near-term, at-the-money calls/puts to analyze implied vol
        """
        # a) Filter calls/puts based on contract expiration, OI, IV rank, etc.
        # b) Return final list of OptionContracts to examine or trade
        pass

    def ComputeIVRankings(self):
        """
        4d) For the selected securities, compute or fetch Implied Vol (IV)
            and rank them by how 'high' or 'low' each IV is relative to its history
        """
        # a) Access each Option's Implied Volatility
        # b) Compare against historical average or median
        # c) Produce rank for each asset, store results
        pass

    # ------------------------------------------------------------------------
    # 5) Construct Delta-Neutral Positions
    # ------------------------------------------------------------------------
    def BuildPositions(self):
        """
        5) For high-IV securities:
            - Possibly short calls/puts or straddles
          For low-IV securities:
            - Possibly long calls/puts or straddles
          Hedge deltas with shares to remain near delta-neutral.
        """
        # a) Based on ranking, select top X high IV symbols and short options
        # b) Select top X low IV symbols and buy options
        # c) Hedge net delta by buy/sell underlying shares
        pass

    def RebalancePositions(self):
        """
        6) Rebalance the portfolio frequently, adjusting net delta to near zero
        """
        # a) Periodically recalc total delta
        # b) If net delta exceeds threshold, adjust shares to bring net delta to zero
        pass

    def RiskManagement(self):
        """
        7) Monitor volatility shocks and manage stops or exposure constraints
        """
        # a) Possibly track aggregate vega or net exposure
        # b) If short IV side is too large or volatility spikes too high, reduce short side
        # c) Close or scale positions when max drawdown or stop-loss is hit
        pass
