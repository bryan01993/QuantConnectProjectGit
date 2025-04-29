from typing import overload
from enum import Enum
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import QuantConnect.Securities.Crypto


class CryptoExchange(QuantConnect.Securities.SecurityExchange):
    """Crypto exchange class - information and helper tools for Crypto exchange properties"""

    @overload
    def __init__(self, market: str) -> None:
        """
        Initializes a new instance of the CryptoExchange class using market hours
        derived from the market-hours-database for the Crypto market
        """
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the CryptoExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...


class Crypto(QuantConnect.Securities.Security, QuantConnect.Securities.IBaseCurrencySymbol):
    """Crypto Security Object Implementation for Crypto Assets"""

    @property
    def base_currency(self) -> QuantConnect.Securities.Cash:
        """Gets the currency acquired by going long this currency pair"""
        ...

    @property
    def price(self) -> float:
        """Get the current value of the security."""
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, baseCurrency: QuantConnect.Securities.Cash, config: QuantConnect.Data.SubscriptionDataConfig, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the Crypto security
        
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param baseCurrency: The cash object that represent the base currency
        :param config: The subscription configuration for this security
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, baseCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache) -> None:
        """
        Constructor for the Crypto security
        
        :param symbol: The security's symbol
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param baseCurrency: The cash object that represent the base currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        :param securityCache: Cache to store Security data
        """
        ...

    @staticmethod
    def decompose_currency_pair(symbol: typing.Union[QuantConnect.Symbol, str], symbol_properties: QuantConnect.Securities.SymbolProperties, base_currency: typing.Optional[str], quote_currency: typing.Optional[str]) -> typing.Union[None, str, str]:
        """
        Decomposes the specified currency pair into a base and quote currency provided as out parameters
        
        :param symbol: The input symbol to be decomposed
        :param symbol_properties: The symbol properties for this security
        :param base_currency: The output base currency
        :param quote_currency: The output quote currency
        """
        ...


class CryptoHolding(QuantConnect.Securities.SecurityHolding):
    """Crypto holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Crypto.Crypto, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Crypto Holding Class
        
        :param security: The Crypto security being held
        :param currencyConverter: A currency converter instance
        """
        ...


