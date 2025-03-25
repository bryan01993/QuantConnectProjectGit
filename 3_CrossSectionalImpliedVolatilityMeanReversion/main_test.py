import unittest
from collections import namedtuple

class TestComputeIVRankings(unittest.TestCase):

    def setUp(self):
        # Mock OptionContract object
        self.MockOption = namedtuple("MockOption", ["Symbol", "ImpliedVolatility"])

        # Mock algorithm instance
        class MockAlgorithm:
            def __init__(self):
                self.iv_history = {}

            def ComputeIVRankings(self, candidateOptions):
                iv_ranks = []
                for contract in candidateOptions:
                    option_symbol = contract.Symbol
                    current_iv = contract.ImpliedVolatility

                    if current_iv is None or current_iv == 0:
                        continue

                    if option_symbol not in self.iv_history:
                        self.iv_history[option_symbol] = []

                    self.iv_history[option_symbol].append(current_iv)

                    window_size = 30
                    history = self.iv_history[option_symbol][-window_size:]

                    if len(history) < 5:
                        continue

                    rank = sum(1 for v in history if v < current_iv) / len(history)
                    iv_ranks.append((option_symbol, rank))
                return iv_ranks

        self.algo = MockAlgorithm()

    def test_iv_percentile_ranking(self):
        symbol = "OPT123"
        # Feed increasing IVs so last IV is max
        options = [
            self.MockOption(Symbol=symbol, ImpliedVolatility=iv)
            for iv in [0.2, 0.21, 0.22, 0.23, 0.25, 0.3]
        ]

        for i in range(5):  # Preload 5 IV values
            self.algo.ComputeIVRankings([options[i]])

        rankings = self.algo.ComputeIVRankings([options[-1]])  # Test the last one
        self.assertEqual(len(rankings), 1)
        symbol_out, percentile = rankings[0]
        self.assertEqual(symbol_out, symbol)
        self.assertAlmostEqual(percentile, 1.0, delta=0.01)

    def test_insufficient_history(self):
        symbol = "OPT456"
        options = [
            self.MockOption(Symbol=symbol, ImpliedVolatility=0.2 + i * 0.01)
            for i in range(3)
        ]
        rankings = []
        for opt in options:
            rankings = self.algo.ComputeIVRankings([opt])
        self.assertEqual(rankings, [])  # Not enough history yet

if __name__ == '__main__':
    unittest.main()
