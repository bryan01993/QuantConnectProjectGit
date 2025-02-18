import numpy as np
class KellyCriterion:

    def __init__(self, factor, period):
        self._factor = factor
        self._period = period
        self._trades = np.array([])

    def update_signal(self, signal, price):
        if signal:  # Enter
            self._entry_price = price
        else:  # Exit
            self._trades = np.append(self._trades, [price - self._entry_price])[-self._period:]

    def weight(self):
        # Wait until there are enough trade samples.
        if not self.is_ready:
            return None
        # Calculate the Kelly %.
        wins = self._trades[self._trades > 0]
        losses = self._trades[self._trades < 0]
        if not losses.sum():
            return self._factor
        if not wins.sum():
            return 0
        win_loss_ratio = wins.mean() / losses.mean()
        winning_probability = len(wins) / self._period
        return self._factor * (winning_probability - (1 - winning_probability) / win_loss_ratio)

    @property
    def is_ready(self):
        return len(self._trades) == self._period