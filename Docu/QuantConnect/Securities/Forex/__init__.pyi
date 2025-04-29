from typing import overload
from enum import Enum
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import QuantConnect.Securities.Forex


class Forex(QuantConnect.Securities.Security, QuantConnect.Securities.IBaseCurrencySymbol):
    """FOREX Security Object Implementation for FOREX Assets"""

    @property
    def base_currency(self) -> QuantConnect.Securities.Cash:
        """Gets the currency acquired by going long this currency pair"""
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, baseCurrency: QuantConnect.Securities.Cash, config: QuantConnect.Data.SubscriptionDataConfig, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the forex security
        
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
        Constructor for the forex security
        
        :param symbol: The security's symbol
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param baseCurrency: The cash object that represent the base currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        :param securityCache: Cache for storing Security data
        """
        ...

    @staticmethod
    def decompose_currency_pair(currency_pair: str, base_currency: typing.Optional[str], quote_currency: typing.Optional[str]) -> typing.Union[None, str, str]:
        """
        Decomposes the specified currency pair into a base and quote currency provided as out parameters
        
        :param currency_pair: The input currency pair to be decomposed, for example, "EURUSD"
        :param base_currency: The output base currency
        :param quote_currency: The output quote currency
        """
        ...


class ForexHolding(QuantConnect.Securities.SecurityHolding):
    """FOREX holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Forex.Forex, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Forex Holding Class
        
        :param security: The forex security being held
        :param currencyConverter: A currency converter instance
        """
        ...

    def total_close_profit_pips(self) -> float:
        """Profit in pips if we closed the holdings right now including the approximate fees"""
        ...


class ForexDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """Forex packet by packet data filtering mechanism for dynamically detecting bad ticks."""

    def __init__(self) -> None:
        """Initialize forex data filter class:"""
        ...

    def filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Forex data filter: a true value means accept the packet, a false means fail.
        
        :param vehicle: Security asset
        :param data: Data object we're scanning to filter
        """
        ...


class ForexExchange(QuantConnect.Securities.SecurityExchange):
    """Forex exchange class - information and helper tools for forex exchange properties"""

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days per year for this security, used for performance statistics."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the ForexExchange class using market hours
        derived from the market-hours-database for the FXCM Forex market
        """
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the ForexExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...


class ForexCache(QuantConnect.Securities.SecurityCache):
    """Forex specific caching support"""

    def __init__(self) -> None:
        """Initialize forex cache"""
        ...


