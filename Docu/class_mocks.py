from typing import Dict, Any, List
from datetime import datetime, timedelta


class MockSymbol:
    def __init__(self, ticker: str):
        self.Value = ticker
        self.ID = type("ID", (), {"Date": datetime.now().date()})


class MockSecurity:
    def __init__(self):
        self.Invested = False


class MockPortfolio:
    def __init__(self):
        self._securities = {}

    def __getitem__(self, symbol: MockSymbol) -> MockSecurity:
        if symbol not in self._securities:
            self._securities[symbol] = MockSecurity()
        return self._securities[symbol]

    def __contains__(self, symbol: MockSymbol) -> bool:
        return symbol in self._securities

    @property
    def TotalPortfolioValue(self) -> float:
        return 100000.0


class MockSlice:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.OptionChains = {}

    def __getitem__(self, symbol: MockSymbol):
        return self.data.get(symbol.Value, None)

    def __contains__(self, symbol: MockSymbol):
        return symbol.Value in self.data


class MockOptionContract:
    def __init__(self, expiry: datetime):
        self.Expiry = expiry
        self.Symbol = MockSymbol("SPY")


class MockOptionFilterUniverse:
    def Strikes(self, min_strike: int, max_strike: int):
        return self

    def Expiration(self, min_days: int, max_days: int):
        return self

    def CallsOnly(self):
        return self


class MockQCAlgorithm:
    def __init__(self):
        self.Time = datetime.now()
        self.Portfolio = MockPortfolio()
        self.CurrentSlice = MockSlice({})
        self.DebugMessages = []
        self.LogMessages = []

    def SetStartDate(self, year: int, month: int, day: int):
        pass

    def SetEndDate(self, year: int, month: int, day: int):
        pass

    def SetCash(self, amount: float):
        pass

    def AddEquity(self, ticker: str, resolution: Any):
        return type("Equity", (), {"Symbol": MockSymbol(ticker)})()

    def AddOption(self, ticker: str, resolution: Any):
        return type("Option", (), {
            "SetFilter": lambda self, f: None,
            "Symbol": MockSymbol(ticker)
        })()

    def SetBenchmark(self, ticker: str):
        pass

    def AddChart(self, chart: Any):
        pass

    def Plot(self, chart_name: str, series_name: str, value: float):
        pass

    def MarketOrder(self, symbol: MockSymbol, quantity: int):
        pass

    def Liquidate(self, symbol: MockSymbol):
        pass

    class Schedule:
        @staticmethod
        def On(*args, **kwargs):
            pass

    class DateRules:
        @staticmethod
        def EveryDay(symbol: MockSymbol):
            return "EveryDayRule"

    class TimeRules:
        @staticmethod
        def At(hour: int, minute: int):
            return "TimeRule"

    def GetParameter(self, name: str) -> str:
        # Mock different return values
        if "start_date" in name:
            return "2022-01-01"
        elif "end_date" in name:
            return "2022-12-31"
        elif "initial_amount" in name:
            return "100000"
        elif "univ.coarse.size" in name:
            return "50"
        else:
            return "mock_value"

    def Debug(self, message: str):
        self.DebugMessages.append(message)

    def Log(self, message: str):
        self.LogMessages.append(message)
