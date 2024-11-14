dict_of_classes = {
    "AddEquity": "<QuantConnect.Securities.Equity.Equity object at 0x7f9417158180>",
    "AddOption": "<QuantConnect.Securities.Option.Option object at 0x7f942121ab40>",
    "slice": "<QuantConnect.Python.PythonSlice object at 0x7f945f30f780>",
    "universe": "<QuantConnect.Securities.OptionFilterUniverse object at 0x7f941c6a8cc0>",
    "contract": "<QuantConnect.Data.Market.OptionContract object at 0x7efa207da680>"}
"""Apparently 

Option: At the top level, you interact with an Option object. This represents the option contract you're trading and is created by calling AddOption in your algorithm. It allows you to set global properties like the underlying symbol.

OptionChain: For each time step in your algorithm, you receive an OptionChain object through the Slice data structure in the OnData method. An OptionChain holds all the option contracts (calls and puts) available for a particular underlying symbol at a snapshot in time.

OptionContract: Within an OptionChain, you have multiple OptionContract objects. Each OptionContract represents a specific option contract and contains details such as the strike price, expiration date, option type (call or put), bid/ask prices, open interest, and the Greeks (Delta, Gamma, Vega, Theta, Rho).

OptionSymbol: Every OptionContract has a Symbol property, an OptionSymbol object encoding the option's underlying symbol, expiration date, strike price, and whether it's a call or put. This symbol is used to uniquely identify the option contract in the market.

OptionExerciseModel and OptionPricingModel: These objects define how the option can be exercised (American, European) and how its price is theoretically calculated, respectively. You can set these on the Option object to control the behavior of your options."""
