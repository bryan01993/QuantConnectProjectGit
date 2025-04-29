from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect
import QuantConnect.Securities
import QuantConnect.Securities.CurrencyConversion
import System
import System.Collections.Generic

QuantConnect_Securities_CurrencyConversion__EventContainer_Callable = typing.TypeVar("QuantConnect_Securities_CurrencyConversion__EventContainer_Callable")
QuantConnect_Securities_CurrencyConversion__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Securities_CurrencyConversion__EventContainer_ReturnType")


class ICurrencyConversion(metaclass=abc.ABCMeta):
    """Represents a type capable of calculating the conversion rate between two currencies"""

    @property
    @abc.abstractmethod
    def conversion_rate_updated(self) -> _EventContainer[typing.Callable[[System.Object, float], None], None]:
        """Event fired when the conversion rate is updated"""
        ...

    @property
    @abc.abstractmethod
    def source_currency(self) -> str:
        """The currency this conversion converts from"""
        ...

    @property
    @abc.abstractmethod
    def destination_currency(self) -> str:
        """The currency this conversion converts to"""
        ...

    @property
    @abc.abstractmethod
    def conversion_rate(self) -> float:
        """The current conversion rate between SourceCurrency and DestinationCurrency"""
        ...

    @property.setter
    def conversion_rate(self, value: float) -> None:
        ...

    @property
    @abc.abstractmethod
    def conversion_rate_securities(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security]:
        """The securities which the conversion rate is based on"""
        ...

    def update(self) -> None:
        """
        Updates the internal conversion rate based on the latest data, and returns the new conversion rate
        
        :returns: The new conversion rate.
        """
        ...


class ConstantCurrencyConversion(System.Object, QuantConnect.Securities.CurrencyConversion.ICurrencyConversion):
    """Provides an implementation of ICurrencyConversion with a fixed conversion rate"""

    @property
    def conversion_rate_updated(self) -> _EventContainer[typing.Callable[[System.Object, float], None], None]:
        """Event fired when the conversion rate is updated"""
        ...

    @property
    def source_currency(self) -> str:
        """The currency this conversion converts from"""
        ...

    @property
    def destination_currency(self) -> str:
        """The currency this conversion converts to"""
        ...

    @property
    def conversion_rate(self) -> float:
        """The current conversion rate"""
        ...

    @property.setter
    def conversion_rate(self, value: float) -> None:
        ...

    @property
    def conversion_rate_securities(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security]:
        """The securities which the conversion rate is based on"""
        ...

    def __init__(self, sourceCurrency: str, destinationCurrency: str, conversionRate: float = 1) -> None:
        """
        Initializes a new instance of the ConstantCurrencyConversion class.
        
        :param sourceCurrency: The currency this conversion converts from
        :param destinationCurrency: The currency this conversion converts to
        :param conversionRate: The conversion rate between the currencies
        """
        ...

    @staticmethod
    def identity(source_currency: str, destination_currency: str = None) -> QuantConnect.Securities.CurrencyConversion.ConstantCurrencyConversion:
        """
        Creates a new identity conversion, where the conversion rate is set to 1 and the source and destination currencies might the same
        
        :param source_currency: The currency this conversion converts from
        :param destination_currency: The currency this conversion converts to. If null, the destination and source currencies are the same
        :returns: The identity currency conversion.
        """
        ...

    @staticmethod
    def null(source_currency: str, destination_currency: str) -> QuantConnect.Securities.CurrencyConversion.ConstantCurrencyConversion:
        """Returns an instance of ConstantCurrencyConversion that represents a null conversion"""
        ...

    def update(self) -> None:
        """Marks the conversion rate as potentially outdated, needing an update based on the latest data"""
        ...


class SecurityCurrencyConversion(System.Object, QuantConnect.Securities.CurrencyConversion.ICurrencyConversion):
    """Provides an implementation of ICurrencyConversion to find and use multi-leg currency conversions"""

    @property
    def conversion_rate_updated(self) -> _EventContainer[typing.Callable[[System.Object, float], None], None]:
        """Event fired when the conversion rate is updated"""
        ...

    @property
    def source_currency(self) -> str:
        """The currency this conversion converts from"""
        ...

    @property
    def destination_currency(self) -> str:
        """The currency this conversion converts to"""
        ...

    @property
    def conversion_rate(self) -> float:
        """The current conversion rate"""
        ...

    @property.setter
    def conversion_rate(self, value: float) -> None:
        ...

    @property
    def conversion_rate_securities(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security]:
        """The securities which the conversion rate is based on"""
        ...

    @staticmethod
    def linear_search(source_currency: str, destination_currency: str, existing_securities: System.Collections.Generic.IList[QuantConnect.Securities.Security], potential_symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], make_new_security: typing.Callable[[QuantConnect.Symbol], QuantConnect.Securities.Security]) -> QuantConnect.Securities.CurrencyConversion.SecurityCurrencyConversion:
        """
        Finds a conversion between two currencies by looking through all available 1 and 2-leg options
        
        :param source_currency: The currency to convert from
        :param destination_currency: The currency to convert to
        :param existing_securities: The securities which are already added to the algorithm
        :param potential_symbols: The symbols to consider, may overlap with existing_securities
        :param make_new_security: The function to call when a symbol becomes part of the conversion, must return the security that will provide price data about the symbol
        :returns: A new SecurityCurrencyConversion instance representing the conversion from source_currency to destination_currency.
        """
        ...

    def update(self) -> None:
        """
        Signals an updates to the internal conversion rate based on the latest data.
        It will set the conversion rate as potentially outdated so it gets re-calculated.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Securities_CurrencyConversion__EventContainer_Callable, QuantConnect_Securities_CurrencyConversion__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Securities_CurrencyConversion__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Securities_CurrencyConversion__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Securities_CurrencyConversion__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


