import numpy as np

class KellyCriterion:
    """
    A simple Kelly criterion calculator:
    1) We store trade/return samples up to 'period' in length.
    2) Each call to Update(...) appends new returns.
    3) GetFraction() returns the fraction of your capital to bet,
       scaled by self._factor (Half-Kelly or otherwise).
    """

    def __init__(self, factor, period):
        # factor: scale Kelly bet fraction
        # period: number of trades or returns we keep
        self._factor = factor if factor else 0.5 # Default values
        self._period = period if period else 30  # Default values
        self._returns = np.array([])  # store recent trade/daily returns

    def Update(self, dailyReturns):
        """
        Incorporate new daily returns into our Kelly calculation.
        'dailyReturns' can be a list or array of floats representing
        PnL or percentage returns.
        """
        # Append new returns to our array
        newData = np.array(dailyReturns)
        self._returns = np.append(self._returns, newData)

        # Trim to self._period
        if len(self._returns) > self._period:
            self._returns = self._returns[-self._period:]

    def GetFraction(self):
        """
        Returns the fraction of capital to allocate, as per Kelly formula,
        scaled by 'factor'.

        We'll treat returns > 0 as 'wins' and < 0 as 'losses', and compute
        a win/loss ratio + probability of winning. Because we are using
        daily returns, this is not classical single-trade Kelly, but it
        demonstrates the concept.
        """
        # We need at least some data to compute
        if not self.IsReady:
            return 0.0  # or None—no fraction available yet

        # Separate positive from negative returns
        wins   = self._returns[self._returns > 0]
        losses = self._returns[self._returns < 0]

        # If no losses, bet full factor
        if len(losses) == 0:
            return self._factor
        # If no wins, bet 0
        if len(wins) == 0:
            return 0.0

        # Average sizes
        avgWin   = np.mean(wins)
        avgLoss  = abs(np.mean(losses))  # mean of negative
        winProb  = len(wins) / float(len(self._returns))
        lossProb = 1 - winProb

        # Kelly formula: K% = P - Q / (R)
        #   where P=winProb, Q=lossProb, R=avgWin/abs(avgLoss)
        winLossRatio = avgWin / avgLoss
        rawKelly = winProb - (lossProb / winLossRatio)

        # Multiply by scaling factor (like 0.5 for half Kelly)
        kellyFraction = self._factor * rawKelly

        # clamp to 0-1 if you prefer
        if kellyFraction < 0:
            kellyFraction = 0
        if kellyFraction > 1:
            kellyFraction = 1

        return kellyFraction

    @property
    def IsReady(self):
        """
        We consider the Kelly Criterion 'ready' if we have
        'period' number of returns stored.
        """
        return len(self._returns) >= self._period
