from typing import overload
from enum import Enum
import typing

import QuantConnect
import QuantConnect.Orders
import QuantConnect.Securities
import QuantConnect.Securities.CryptoFuture
import System


class CryptoFutureMarginModel(QuantConnect.Securities.SecurityMarginModel):
    """The crypto future margin model which supports both Coin and USDT futures"""

    def __init__(self, leverage: float = 25, maintenanceMarginRate: float = 0.05, maintenanceAmount: float = 0) -> None:
        """
        Creates a new instance
        
        :param leverage: The leverage to use, used on initial margin requirements, default 25x
        :param maintenanceMarginRate: The maintenance margin rate, default 5%
        :param maintenanceAmount: The maintenance amount which will reduce maintenance margin requirements, default 0
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity of shares
        :returns: The initial margin required for the option (i.e. the equity required to enter a position for this option).
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently alloted to the specified holding.
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the option.
        """
        ...

    def get_margin_remaining(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> float:
        """
        Gets the margin cash available for a trade
        
        This method is protected.
        
        :param portfolio: The algorithm's portfolio
        :param security: The security to be traded
        :param direction: The direction of the trade
        :returns: The margin available for the trade.
        """
        ...


class BinanceFutureMarginInterestRateModel(System.Object, QuantConnect.Securities.IMarginInterestRateModel):
    """The responsability of this model is to apply future funding rate cash flows to the portfolio based on open positions"""

    def apply_margin_interest_rate(self, margin_interest_rate_parameters: QuantConnect.Securities.MarginInterestRateParameters) -> None:
        """
        Apply margin interest rates to the portfolio
        
        :param margin_interest_rate_parameters: The parameters to use
        """
        ...


class BybitFutureMarginInterestRateModel(QuantConnect.Securities.CryptoFuture.BinanceFutureMarginInterestRateModel):
    """The responsibility of this model is to apply future funding rate cash flows to the portfolio based on open positions"""


class CryptoFutureExchange(QuantConnect.Securities.SecurityExchange):
    """Crypto future exchange class - information and helper tools for Crypto future exchange properties"""

    @overload
    def __init__(self, market: str) -> None:
        """
        Initializes a new instance of the CryptoFutureExchange class using market hours
        derived from the market-hours-database for the Crypto future market
        """
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the CryptoFutureExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...


class CryptoFutureHolding(QuantConnect.Securities.SecurityHolding):
    """Crypto Future holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Security, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Crypto Future Holding Class constructor
        
        :param security: The crypto future security being held
        :param currencyConverter: A currency converter instance
        """
        ...

    def get_quantity_value(self, quantity: float, price: float) -> QuantConnect.Securities.ConvertibleCashAmount:
        """
        Gets the total value of the specified  of shares of this security
        in the account currency
        
        :param quantity: The quantity of shares
        :param price: The current price
        :returns: The value of the quantity of shares in the account currency.
        """
        ...


class CryptoFuture(QuantConnect.Securities.Security, QuantConnect.Securities.IBaseCurrencySymbol):
    """Crypto Future Security Object Implementation for Crypto Future Assets"""

    @property
    def base_currency(self) -> QuantConnect.Securities.Cash:
        """Gets the currency acquired by going long this currency pair"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, baseCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, cache: QuantConnect.Securities.SecurityCache) -> None:
        """
        Constructor for the Crypto Future security
        
        :param symbol: The symbol
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param baseCurrency: The cash object that represent the base currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        :param cache: The security cache
        """
        ...

    def is_crypto_coin_future(self) -> bool:
        """
        Checks whether the security is a crypto coin future
        
        :returns: True if the security is a crypto coin future.
        """
        ...


