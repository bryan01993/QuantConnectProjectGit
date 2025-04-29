from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.OptionExercise
import QuantConnect.Orders.Slippage
import QuantConnect.Securities
import QuantConnect.Securities.Future
import QuantConnect.Securities.Interfaces
import QuantConnect.Securities.Option
import QuantConnect.Securities.Positions
import System
import System.Collections.Generic

QuantConnect_Securities_Option_OptionStrategy_LegData = typing.Any
GeneralizedBlackScholesProcess = typing.Any
IPricingEngine = typing.Any


class IQLDividendYieldEstimator(metaclass=abc.ABCMeta):
    """
    Defines QuantLib dividend yield estimator for option pricing model. User may define his own estimators,
    including those forward and backward looking ones.
    """

    def estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        """
        Returns current estimate of the stock dividend yield
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: Dividend yield.
        """
        ...


class ConstantQLDividendYieldEstimator(System.Object, QuantConnect.Securities.Option.IQLDividendYieldEstimator):
    """Class implements default flat dividend yield curve estimator, implementing IQLDividendYieldEstimator."""

    def __init__(self, dividendYield: float = 0.00) -> None:
        """Constructor initializes class with constant dividend yield."""
        ...

    def estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        """
        Returns current flat estimate of the dividend yield
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: The estimate.
        """
        ...


class OptionPriceModelResult(System.Object):
    """Result type for IOptionPriceModel.Evaluate"""

    NONE: QuantConnect.Securities.Option.OptionPriceModelResult
    """Represents the zero option price and greeks."""

    @property
    def theoretical_price(self) -> float:
        """Gets the theoretical price as computed by the IOptionPriceModel"""
        ...

    @property
    def implied_volatility(self) -> float:
        """Gets the implied volatility of the option contract"""
        ...

    @property
    def greeks(self) -> QuantConnect.Data.Market.Greeks:
        """Gets the various sensitivities as computed by the IOptionPriceModel"""
        ...

    @overload
    def __init__(self, theoreticalPrice: float, greeks: QuantConnect.Data.Market.Greeks) -> None:
        """
        Initializes a new instance of the OptionPriceModelResult class
        
        :param theoreticalPrice: The theoretical price computed by the price model
        :param greeks: The sensitivities (greeks) computed by the price model
        """
        ...

    @overload
    def __init__(self, theoreticalPrice: float, impliedVolatility: typing.Callable[[], float], greeks: typing.Callable[[], QuantConnect.Data.Market.Greeks]) -> None:
        """
        Initializes a new instance of the OptionPriceModelResult class with lazy calculations of implied volatility and greeks
        
        :param theoreticalPrice: The theoretical price computed by the price model
        :param impliedVolatility: The calculated implied volatility
        :param greeks: The sensitivities (greeks) computed by the price model
        """
        ...


class IOptionPriceModel(metaclass=abc.ABCMeta):
    """Defines a model used to calculate the theoretical price of an option contract."""

    def evaluate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        """
        Evaluates the specified option contract to compute a theoretical price, IV and greeks
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: An instance of OptionPriceModelResult containing the theoretical price of the specified option contract.
        """
        ...


class CurrentPriceOptionPriceModel(System.Object, QuantConnect.Securities.Option.IOptionPriceModel):
    """
    Provides a default implementation of IOptionPriceModel that does not compute any
    greeks and uses the current price for the theoretical price.
    This is a stub implementation until the real models are implemented
    """

    def evaluate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        """
        Creates a new OptionPriceModelResult containing the current Security.Price
        and a default, empty instance of first Order Greeks
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: An instance of OptionPriceModelResult containing the theoretical price of the specified option contract.
        """
        ...


class OptionSymbolProperties(QuantConnect.Securities.SymbolProperties):
    """Represents common properties for a specific option contract"""

    @property
    def contract_multiplier(self) -> float:
        """The contract multiplier for the security"""
        ...

    @property
    def contract_unit_of_trade(self) -> int:
        """
        When the holder of an equity option exercises one contract, or when the writer of an equity option is assigned
        an exercise notice on one contract, this unit of trade, usually 100 shares of the underlying security, changes hands.
        """
        ...

    @overload
    def __init__(self, description: str, quoteCurrency: str, contractMultiplier: float, pipSize: float, lotSize: float) -> None:
        """Creates an instance of the OptionSymbolProperties class"""
        ...

    @overload
    def __init__(self, properties: QuantConnect.Securities.SymbolProperties) -> None:
        """Creates an instance of the OptionSymbolProperties class from SymbolProperties class"""
        ...


class Option(QuantConnect.Securities.Security, QuantConnect.Securities.IDerivativeSecurity, QuantConnect.Interfaces.IOptionPrice):
    """Option Security Object Implementation for Option Assets"""

    DEFAULT_SETTLEMENT_DAYS: int = 1
    """The default number of days required to settle an equity sale"""

    DEFAULT_SETTLEMENT_TIME: datetime.timedelta = ...
    """The default time of day for settlement"""

    @property
    def is_option_chain(self) -> bool:
        """Returns true if this is the option chain security, false if it is a specific option contract"""
        ...

    @property
    def is_option_contract(self) -> bool:
        """Returns true if this is a specific option contract security, false if it is the option chain security"""
        ...

    @property
    def strike_price(self) -> float:
        """Gets the strike price"""
        ...

    @property
    def scaled_strike_price(self) -> float:
        """Gets the strike price multiplied by the strike multiplier"""
        ...

    @property
    def expiry(self) -> datetime.datetime:
        """Gets the expiration date"""
        ...

    @property
    def right(self) -> QuantConnect.OptionRight:
        """Gets the right being purchased (call [right to buy] or put [right to sell])"""
        ...

    @property
    def style(self) -> QuantConnect.OptionStyle:
        """Gets the option style"""
        ...

    @property
    def bid_price(self) -> float:
        """Gets the most recent bid price if available"""
        ...

    @property
    def ask_price(self) -> float:
        """Gets the most recent ask price if available"""
        ...

    @property
    def contract_unit_of_trade(self) -> int:
        """
        When the holder of an equity option exercises one contract, or when the writer of an equity option is assigned
        an exercise notice on one contract, this unit of trade, usually 100 shares of the underlying security, changes hands.
        """
        ...

    @property.setter
    def contract_unit_of_trade(self, value: int) -> None:
        ...

    @property
    def contract_multiplier(self) -> int:
        """The contract multiplier for the option security"""
        ...

    @property.setter
    def contract_multiplier(self, value: int) -> None:
        ...

    @property
    def exercise_settlement(self) -> QuantConnect.SettlementType:
        """Specifies if option contract has physical or cash settlement on exercise"""
        ...

    @property.setter
    def exercise_settlement(self, value: QuantConnect.SettlementType) -> None:
        ...

    @property
    def underlying(self) -> QuantConnect.Securities.Security:
        """Gets or sets the underlying security object."""
        ...

    @property.setter
    def underlying(self, value: QuantConnect.Securities.Security) -> None:
        ...

    @property
    def price_model(self) -> QuantConnect.Securities.Option.IOptionPriceModel:
        """Gets or sets the price model for this option security"""
        ...

    @property.setter
    def price_model(self, value: QuantConnect.Securities.Option.IOptionPriceModel) -> None:
        ...

    @property
    def option_exercise_model(self) -> QuantConnect.Orders.OptionExercise.IOptionExerciseModel:
        """Fill model used to produce fill events for this security"""
        ...

    @property.setter
    def option_exercise_model(self, value: QuantConnect.Orders.OptionExercise.IOptionExerciseModel) -> None:
        ...

    @property
    def option_assignment_model(self) -> QuantConnect.Securities.Option.IOptionAssignmentModel:
        """The automatic option assignment model"""
        ...

    @property.setter
    def option_assignment_model(self, value: QuantConnect.Securities.Option.IOptionAssignmentModel) -> None:
        ...

    @property
    def enable_greek_approximation(self) -> bool:
        """
        When enabled, approximates Greeks if corresponding pricing model didn't calculate exact numbers
        
        This property has been deprecated. Please use QLOptionPriceModel.EnableGreekApproximation instead.
        """
        warnings.warn("This property has been deprecated. Please use QLOptionPriceModel.EnableGreekApproximation instead.", DeprecationWarning)

    @property.setter
    def enable_greek_approximation(self, value: bool) -> None:
        warnings.warn("This property has been deprecated. Please use QLOptionPriceModel.EnableGreekApproximation instead.", DeprecationWarning)

    @property
    def contract_filter(self) -> QuantConnect.Securities.IDerivativeSecurityFilter[QuantConnect.Data.UniverseSelection.OptionUniverse]:
        """Gets or sets the contract filter"""
        ...

    @property.setter
    def contract_filter(self, value: QuantConnect.Securities.IDerivativeSecurityFilter[QuantConnect.Data.UniverseSelection.OptionUniverse]) -> None:
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.Option.OptionSymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the option security
        
        :param exchangeHours: Defines the hours this exchange is open
        :param config: The subscription configuration for this security
        :param quoteCurrency: The cash object that represent the quote currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.Option.OptionSymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache, underlying: QuantConnect.Securities.Security) -> None:
        """
        Constructor for the option security
        
        :param symbol: The symbol of the security
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        :param securityCache: Cache to store security information
        :param underlying: Future underlying security
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, exchange: QuantConnect.Securities.SecurityExchange, cache: QuantConnect.Securities.SecurityCache, portfolioModel: QuantConnect.Securities.ISecurityPortfolioModel, fillModel: QuantConnect.Orders.Fills.IFillModel, feeModel: QuantConnect.Orders.Fees.IFeeModel, slippageModel: QuantConnect.Orders.Slippage.ISlippageModel, settlementModel: QuantConnect.Securities.ISettlementModel, volatilityModel: QuantConnect.Securities.IVolatilityModel, buyingPowerModel: QuantConnect.Securities.IBuyingPowerModel, dataFilter: QuantConnect.Securities.Interfaces.ISecurityDataFilter, priceVariationModel: QuantConnect.Securities.IPriceVariationModel, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, underlying: QuantConnect.Securities.Security) -> None:
        """
        Creates instance of the Option class.
        
        This method is protected.
        """
        ...

    def evaluate_price_model(self, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        """
        For this option security object, evaluates the specified option
        contract to compute a theoretical price, IV and greeks
        
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: An instance of OptionPriceModelResult containing the theoretical price of the specified option contract.
        """
        ...

    def get_aggregate_exercise_amount(self) -> float:
        """
        Aggregate exercise amount or aggregate contract value. It is the total amount of cash one will pay (or receive) for the shares of the
        underlying stock if he/she decides to exercise (or is assigned an exercise notice). This amount is not the premium paid or received for an equity option.
        """
        ...

    @overload
    def get_exercise_quantity(self) -> float:
        """
        Returns the directional quantity of underlying shares that are going to change hands on exercise/assignment of all
        contracts held by this account, taking into account the contract's Right as well as the contract's current
        ContractUnitOfTrade, which may have recently changed due to a split/reverse split in the underlying security.
        """
        ...

    @overload
    def get_exercise_quantity(self, exercise_order_quantity: float) -> float:
        """
        Returns the directional quantity of underlying shares that are going to change hands on exercise/assignment of the
        specified , taking into account the contract's Right as well
        as the contract's current ContractUnitOfTrade, which may have recently changed due to a split/reverse
        split in the underlying security.
        """
        ...

    def get_intrinsic_value(self, underlying_price: float) -> float:
        """Intrinsic value function of the option"""
        ...

    def get_pay_off(self, underlying_price: float) -> float:
        """
        Option payoff function at expiration time
        
        :param underlying_price: The price of the underlying
        """
        ...

    def is_auto_exercised(self, underlying_price: float) -> bool:
        """Checks if option is eligible for automatic exercise on expiration"""
        ...

    def out_of_the_money_amount(self, underlying_price: float) -> float:
        """
        Option out of the money function
        
        :param underlying_price: The price of the underlying
        """
        ...

    def set_data_normalization_mode(self, mode: QuantConnect.DataNormalizationMode) -> None:
        """Sets the data normalization mode to be used by this security"""
        ...

    @overload
    def set_filter(self, min_strike: int, max_strike: int) -> None:
        """
        Sets the ContractFilter to a new instance of the filter
        using the specified min and max strike values. Contracts with expirations further than 35
        days out will also be filtered.
        
        :param min_strike: The min strike rank relative to market price, for example, -1 would put a lower bound of one strike under market price, where a +1 would put a lower bound of one strike over market price
        :param max_strike: The max strike rank relative to market place, for example, -1 would put an upper bound of on strike under market price, where a +1 would be an upper bound of one strike over market price
        """
        ...

    @overload
    def set_filter(self, min_expiry: datetime.timedelta, max_expiry: datetime.timedelta) -> None:
        """
        Sets the ContractFilter to a new instance of the filter
        using the specified min and max strike and expiration range values
        
        :param min_expiry: The minimum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in less than 10 days
        :param max_expiry: The maximum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in more than 10 days
        """
        ...

    @overload
    def set_filter(self, min_strike: int, max_strike: int, min_expiry: datetime.timedelta, max_expiry: datetime.timedelta) -> None:
        """
        Sets the ContractFilter to a new instance of the filter
        using the specified min and max strike and expiration range values
        
        :param min_strike: The min strike rank relative to market price, for example, -1 would put a lower bound of one strike under market price, where a +1 would put a lower bound of one strike over market price
        :param max_strike: The max strike rank relative to market place, for example, -1 would put an upper bound of on strike under market price, where a +1 would be an upper bound of one strike over market price
        :param min_expiry: The minimum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in less than 10 days
        :param max_expiry: The maximum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in more than 10 days
        """
        ...

    @overload
    def set_filter(self, min_strike: int, max_strike: int, min_expiry_days: int, max_expiry_days: int) -> None:
        """
        Sets the ContractFilter to a new instance of the filter
        using the specified min and max strike and expiration range values
        
        :param min_strike: The min strike rank relative to market price, for example, -1 would put a lower bound of one strike under market price, where a +1 would put a lower bound of one strike over market price
        :param max_strike: The max strike rank relative to market place, for example, -1 would put an upper bound of on strike under market price, where a +1 would be an upper bound of one strike over market price
        :param min_expiry_days: The minimum time, expressed in days, until expiry to include, for example, 10 would exclude contracts expiring in less than 10 days
        :param max_expiry_days: The maximum time, expressed in days, until expiry to include, for example, 10 would exclude contracts expiring in more than 10 days
        """
        ...

    @overload
    def set_filter(self, universe_func: typing.Callable[[QuantConnect.Securities.OptionFilterUniverse], QuantConnect.Securities.OptionFilterUniverse]) -> None:
        """
        Sets the ContractFilter to a new universe selection function
        
        :param universe_func: new universe selection function
        """
        ...

    @overload
    def set_filter(self, universe_func: typing.Any) -> None:
        """
        Sets the ContractFilter to a new universe selection function
        
        :param universe_func: new universe selection function
        """
        ...

    @overload
    def set_option_assignment_model(self, py_object: typing.Any) -> None:
        """
        Sets the automatic option assignment model
        
        :param py_object: The option assignment model to use
        """
        ...

    @overload
    def set_option_assignment_model(self, option_assignment_model: QuantConnect.Securities.Option.IOptionAssignmentModel) -> None:
        """
        Sets the automatic option assignment model
        
        :param option_assignment_model: The option assignment model to use
        """
        ...

    @overload
    def set_option_exercise_model(self, py_object: typing.Any) -> None:
        """
        Sets the option exercise model
        
        :param py_object: The option exercise model to use
        """
        ...

    @overload
    def set_option_exercise_model(self, option_exercise_model: QuantConnect.Orders.OptionExercise.IOptionExerciseModel) -> None:
        """
        Sets the option exercise model
        
        :param option_exercise_model: The option exercise model to use
        """
        ...


class OptionAssignmentParameters(System.Object):
    """The option assignment parameters data transfer class"""

    @property
    def option(self) -> QuantConnect.Securities.Option.Option:
        """The option to evaluate option assignments for"""
        ...

    @property.setter
    def option(self, value: QuantConnect.Securities.Option.Option) -> None:
        ...

    def __init__(self, option: QuantConnect.Securities.Option.Option) -> None:
        """
        Creates a new instance
        
        :param option: The target option
        """
        ...


class OptionAssignmentResult(System.Object):
    """Data transfer object class"""

    NULL: QuantConnect.Securities.Option.OptionAssignmentResult
    """No option assignment should take place"""

    @property
    def quantity(self) -> float:
        """The amount of option holdings to trigger the assignment for"""
        ...

    @property.setter
    def quantity(self, value: float) -> None:
        ...

    @property
    def tag(self) -> str:
        """The tag that will be used in the order for the option assignment"""
        ...

    @property.setter
    def tag(self, value: str) -> None:
        ...

    def __init__(self, quantity: float, tag: str) -> None:
        """
        Creates a new instance
        
        :param quantity: The quantity to assign
        :param tag: The order tag to use
        """
        ...


class IOptionAssignmentModel(metaclass=abc.ABCMeta):
    """The option assignment model emulates exercising of short option positions in the portfolio."""

    def get_assignment(self, parameters: QuantConnect.Securities.Option.OptionAssignmentParameters) -> QuantConnect.Securities.Option.OptionAssignmentResult:
        """
        Get's the option assignments to generate if any
        
        :param parameters: The option assignment parameters data transfer class
        :returns: The option assignment result.
        """
        ...


class NullOptionAssignmentModel(System.Object, QuantConnect.Securities.Option.IOptionAssignmentModel):
    """The null option assignment model, that will disable automatic order assignment"""

    def get_assignment(self, parameters: QuantConnect.Securities.Option.OptionAssignmentParameters) -> QuantConnect.Securities.Option.OptionAssignmentResult:
        """
        Get's the option assignments to generate if any
        
        :param parameters: The option assignment parameters data transfer object
        :returns: The option assignment result.
        """
        ...


class OptionStrategy(System.Object):
    """Option strategy specification class. Describes option strategy and its parameters for trading."""

    class LegData(QuantConnect.Orders.Leg, metaclass=abc.ABCMeta):
        """Defines common properties between OptionLegData and UnderlyingLegData"""

        def invoke(self, underlying_handler: typing.Callable[[QuantConnect.Securities.Option.OptionStrategy.UnderlyingLegData], None], option_handler: typing.Callable[[QuantConnect.Securities.Option.OptionStrategy.OptionLegData], None]) -> None:
            """Invokes the correct handler based on the runtime type."""
            ...

    class OptionLegData(QuantConnect_Securities_Option_OptionStrategy_LegData):
        """This class is a POCO containing basic data for the option legs of the strategy"""

        @property
        def right(self) -> QuantConnect.OptionRight:
            """Option right (type) of the option leg"""
            ...

        @property.setter
        def right(self, value: QuantConnect.OptionRight) -> None:
            ...

        @property
        def expiration(self) -> datetime.datetime:
            """Expiration date of the leg"""
            ...

        @property.setter
        def expiration(self, value: datetime.datetime) -> None:
            ...

        @property
        def strike(self) -> float:
            """Strike price of the leg"""
            ...

        @property.setter
        def strike(self, value: float) -> None:
            ...

        @staticmethod
        def create(quantity: int, symbol: typing.Union[QuantConnect.Symbol, str], order_price: typing.Optional[float] = None) -> QuantConnect.Securities.Option.OptionStrategy.OptionLegData:
            """Creates a new instance of OptionLegData from the specified parameters"""
            ...

        def invoke(self, underlying_handler: typing.Callable[[QuantConnect.Securities.Option.OptionStrategy.UnderlyingLegData], None], option_handler: typing.Callable[[QuantConnect.Securities.Option.OptionStrategy.OptionLegData], None]) -> None:
            """Invokes the"""
            ...

    class UnderlyingLegData(QuantConnect_Securities_Option_OptionStrategy_LegData):
        """This class is a POCO containing basic data for the underlying leg of the strategy"""

        @staticmethod
        @overload
        def create(quantity: int, symbol: typing.Union[QuantConnect.Symbol, str], order_price: typing.Optional[float] = None) -> QuantConnect.Securities.Option.OptionStrategy.UnderlyingLegData:
            """Creates a new instance of UnderlyingLegData for the specified  of underlying shares."""
            ...

        @staticmethod
        @overload
        def create(quantity: int, order_price: typing.Optional[float] = None) -> QuantConnect.Securities.Option.OptionStrategy.UnderlyingLegData:
            """Creates a new instance of UnderlyingLegData for the specified  of underlying shares."""
            ...

        def invoke(self, underlying_handler: typing.Callable[[QuantConnect.Securities.Option.OptionStrategy.UnderlyingLegData], None], option_handler: typing.Callable[[QuantConnect.Securities.Option.OptionStrategy.OptionLegData], None]) -> None:
            """Invokes the"""
            ...

    @property
    def name(self) -> str:
        """Option strategy name"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def canonical_option(self) -> QuantConnect.Symbol:
        """The canonical Option symbol of the strategy"""
        ...

    @property.setter
    def canonical_option(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def underlying(self) -> QuantConnect.Symbol:
        """Underlying symbol of the strategy"""
        ...

    @property.setter
    def underlying(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def option_legs(self) -> System.Collections.Generic.List[QuantConnect.Securities.Option.OptionStrategy.OptionLegData]:
        """Option strategy legs"""
        ...

    @property.setter
    def option_legs(self, value: System.Collections.Generic.List[QuantConnect.Securities.Option.OptionStrategy.OptionLegData]) -> None:
        ...

    @property
    def underlying_legs(self) -> System.Collections.Generic.List[QuantConnect.Securities.Option.OptionStrategy.UnderlyingLegData]:
        """Option strategy underlying legs (usually 0 or 1 legs)"""
        ...

    @property.setter
    def underlying_legs(self, value: System.Collections.Generic.List[QuantConnect.Securities.Option.OptionStrategy.UnderlyingLegData]) -> None:
        ...


class IQLRiskFreeRateEstimator(metaclass=abc.ABCMeta):
    """Defines QuantLib risk free rate estimator for option pricing model."""

    def estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        """
        Returns current estimate of the risk free rate
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: Risk free rate.
        """
        ...


class EmptyOptionChainProvider(System.Object, QuantConnect.Interfaces.IOptionChainProvider):
    """An implementation of IOptionChainProvider that always returns an empty list of contracts"""

    def get_option_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of option contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the option chain (only used in backtesting)
        :returns: The list of option contracts.
        """
        ...


class OptionDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """Option packet by packet data filtering mechanism for dynamically detecting bad ticks."""


class IQLUnderlyingVolatilityEstimator(metaclass=abc.ABCMeta):
    """
    Defines QuantLib underlying volatility estimator for option pricing model. User may define his own estimators,
    including those forward and backward looking ones.
    """

    @property
    @abc.abstractmethod
    def is_ready(self) -> bool:
        """Indicates whether volatility model is warmed up or no"""
        ...

    def estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        """
        Returns current estimate of the underlying volatility
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: Volatility.
        """
        ...


class DefaultOptionAssignmentModel(System.Object, QuantConnect.Securities.Option.IOptionAssignmentModel):
    """
    The option assignment model emulates exercising of short option positions in the portfolio.
    Simulator implements basic no-arb argument: when time value of the option contract is close to zero
    it assigns short legs getting profit close to expiration dates in deep ITM positions. User algorithm then receives
    assignment event from LEAN. Simulator randomly scans for arbitrage opportunities every two hours or so.
    """

    def __init__(self, requiredInTheMoneyPercent: float = 0.05, priorExpiration: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Creates a new instance
        
        :param requiredInTheMoneyPercent: The percent in the money the option has to be to trigger the option assignment
        :param priorExpiration: For OptionStyle.American, the time span prior to expiration were we will try to evaluate option assignment
        """
        ...

    def get_assignment(self, parameters: QuantConnect.Securities.Option.OptionAssignmentParameters) -> QuantConnect.Securities.Option.OptionAssignmentResult:
        """
        Get's the option assignments to generate if any
        
        :param parameters: The option assignment parameters data transfer class
        :returns: The option assignment result.
        """
        ...


class OptionExchange(QuantConnect.Securities.SecurityExchange):
    """Option exchange class - information and helper tools for option exchange properties"""

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days per year for this security, 252."""
        ...

    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the OptionExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...


class QLOptionPriceModel(System.Object, QuantConnect.Securities.Option.IOptionPriceModel):
    """Provides QuantLib(QL) implementation of IOptionPriceModel to support major option pricing models, available in QL."""

    @property
    def enable_greek_approximation(self) -> bool:
        """
        When enabled, approximates Greeks if corresponding pricing model didn't calculate exact numbers.
        The default value is true.
        """
        ...

    @property.setter
    def enable_greek_approximation(self, value: bool) -> None:
        ...

    @property
    def volatility_estimator_warmed_up(self) -> bool:
        """True if volatility model is warmed up, i.e. has generated volatility value different from zero, otherwise false."""
        ...

    @property
    def allowed_option_styles(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.OptionStyle]:
        """
        List of option styles supported by the pricing model.
        By default, both American and European option styles are supported.
        """
        ...

    @overload
    def __init__(self, pricingEngineFunc: typing.Callable[[GeneralizedBlackScholesProcess], IPricingEngine], underlyingVolEstimator: QuantConnect.Securities.Option.IQLUnderlyingVolatilityEstimator = None, riskFreeRateEstimator: QuantConnect.Securities.Option.IQLRiskFreeRateEstimator = None, dividendYieldEstimator: QuantConnect.Securities.Option.IQLDividendYieldEstimator = None, allowedOptionStyles: typing.List[QuantConnect.OptionStyle] = None) -> None:
        """
        Method constructs QuantLib option price model with necessary estimators of underlying volatility, risk free rate, and underlying dividend yield
        
        :param pricingEngineFunc: Function modeled stochastic process, and returns new pricing engine to run calculations for that option
        :param underlyingVolEstimator: The underlying volatility estimator
        :param riskFreeRateEstimator: The risk free rate estimator
        :param dividendYieldEstimator: The underlying dividend yield estimator
        :param allowedOptionStyles: List of option styles supported by the pricing model. It defaults to both American and European option styles
        """
        ...

    @overload
    def __init__(self, pricingEngineFunc: typing.Callable[[QuantConnect.Symbol, GeneralizedBlackScholesProcess], IPricingEngine], underlyingVolEstimator: QuantConnect.Securities.Option.IQLUnderlyingVolatilityEstimator = None, riskFreeRateEstimator: QuantConnect.Securities.Option.IQLRiskFreeRateEstimator = None, dividendYieldEstimator: QuantConnect.Securities.Option.IQLDividendYieldEstimator = None, allowedOptionStyles: typing.List[QuantConnect.OptionStyle] = None) -> None:
        """
        Method constructs QuantLib option price model with necessary estimators of underlying volatility, risk free rate, and underlying dividend yield
        
        :param pricingEngineFunc: Function takes option and modeled stochastic process, and returns new pricing engine to run calculations for that option
        :param underlyingVolEstimator: The underlying volatility estimator
        :param riskFreeRateEstimator: The risk free rate estimator
        :param dividendYieldEstimator: The underlying dividend yield estimator
        :param allowedOptionStyles: List of option styles supported by the pricing model. It defaults to both American and European option styles
        """
        ...

    def evaluate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        """
        Evaluates the specified option contract to compute a theoretical price, IV and greeks
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: An instance of OptionPriceModelResult containing the theoretical price of the specified option contract.
        """
        ...

    def implied_volatility_estimation(self, price: float, initial_guess: float, time_till_expiry: float, risk_free_discount: float, forward_price: float, payoff: typing.Any, black: typing.Optional[typing.Any]) -> typing.Union[float, typing.Any]:
        """
        An implied volatility approximation by Newton-Raphson method. Return 0 if result is not converged
        
        This method is protected.
        
        :param price: current price of the option
        :param initial_guess: initial guess of the IV
        :param time_till_expiry: time till option contract expiry
        :param risk_free_discount: risk free rate discount factor
        :param forward_price: future value of underlying price
        :param payoff: payoff structure of the option contract
        :param black: black calculator instance
        :returns: implied volatility estimation.
        """
        ...


class OptionPriceModels(System.Object):
    """Static class contains definitions of major option pricing models that can be used in LEAN"""

    @staticmethod
    def additive_equiprobabilities() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American vanilla options using binomial trees. Additive Equiprobabilities model.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def barone_adesi_whaley() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Barone-Adesi and Whaley pricing engine for American options (1987)
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_barone_adesi_whaley_approximation_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def binomial_cox_ross_rubinstein() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American vanilla options using binomial trees. Cox-Ross-Rubinstein(CRR) model.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def binomial_jarrow_rudd() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American vanilla options using binomial trees. Jarrow-Rudd model.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def binomial_joshi() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American vanilla options using binomial trees. Joshi model.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def binomial_leisen_reimer() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American vanilla options using binomial trees. Leisen-Reimer model.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def binomial_tian() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American vanilla options using binomial trees. Tian model.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def binomial_trigeorgis() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American vanilla options using binomial trees. Trigeorgis model.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def bjerksund_stensland() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Bjerksund and Stensland pricing engine for American options (1993)
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_bjerksund_stensland_approximation_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def black_scholes() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European vanilla options using analytical formula.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_analytic_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def crank_nicolson_fd() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European and American options using finite-differences.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_f_d_european_engine.html
        
        :returns: New option price model instance.
        """
        ...

    @staticmethod
    def create(price_engine_name: str, risk_free: float, allowed_option_styles: typing.List[QuantConnect.OptionStyle] = None) -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Creates pricing engine by engine type name.
        
        :param price_engine_name: QL price engine name
        :param risk_free: The risk free rate
        :param allowed_option_styles: List of option styles supported by the pricing model. It defaults to both American and European option styles
        :returns: New option price model instance of specific engine.
        """
        ...

    @staticmethod
    def integral() -> QuantConnect.Securities.Option.IOptionPriceModel:
        """
        Pricing engine for European vanilla options using integral approach.
        QuantLib reference: http://quantlib.org/reference/class_quant_lib_1_1_integral_engine.html
        
        :returns: New option price model instance.
        """
        ...


class OptionMarginModel(QuantConnect.Securities.SecurityMarginModel):
    """Represents a simple option margin model."""

    def __init__(self, requiredFreeBuyingPowerPercent: float = 0) -> None:
        """
        Initializes a new instance of the OptionMarginModel
        
        :param requiredFreeBuyingPowerPercent: The percentage used to determine the required unused buying power for the account.
        """
        ...

    def get_initial_margin_required_for_order(self, parameters: QuantConnect.Securities.InitialMarginRequiredForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :returns: The initial margin required for the provided security and quantity.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the current leverage of the security
        
        :param security: The security to get leverage for
        :returns: The current leverage in the security.
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently alloted to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the provided holdings quantity/cost/value.
        """
        ...

    def set_leverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, options.
        
        :param leverage: The new leverage
        """
        ...


class OptionCache(QuantConnect.Securities.SecurityCache):
    """Option specific caching support"""


class OptionHolding(QuantConnect.Securities.SecurityHolding):
    """Option holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Option.Option, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Option Holding Class constructor
        
        :param security: The option security being held
        :param currencyConverter: A currency converter instance
        """
        ...


class OptionSymbol(System.Object):
    """Static class contains common utility methods specific to symbols representing the option contracts"""

    @staticmethod
    def get_last_day_of_trading(symbol: typing.Union[QuantConnect.Symbol, str]) -> datetime.datetime:
        """
        Returns the last trading date for the option contract
        
        :param symbol: Option symbol
        """
        ...

    @staticmethod
    def get_settlement_date_time(symbol: typing.Union[QuantConnect.Symbol, str]) -> datetime.datetime:
        """
        Returns the settlement date time of the option contract.
        
        :param symbol: The option contract symbol
        :returns: The settlement date time.
        """
        ...

    @staticmethod
    def is_option_contract_expired(symbol: typing.Union[QuantConnect.Symbol, str], current_time_utc: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Returns true if the option contract is expired at the specified time
        
        :param symbol: The option contract symbol
        :param current_time_utc: The current time (UTC)
        :returns: True if the option contract is expired at the specified time, false otherwise.
        """
        ...

    @staticmethod
    def is_standard(symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Returns true if the option is a standard contract that expires 3rd Friday of the month
        
        :param symbol: Option symbol
        """
        ...

    @staticmethod
    def is_standard_contract(symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Returns true if the option is a standard contract that expires 3rd Friday of the month
        
        :param symbol: Option symbol
        """
        ...

    @staticmethod
    def is_weekly(symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Returns true if the option is a weekly contract that expires on Friday , except 3rd Friday of the month
        
        :param symbol: Option symbol
        """
        ...

    @staticmethod
    def map_to_underlying(option_ticker: str, security_type: QuantConnect.SecurityType) -> str:
        """
        Maps the option ticker to it's underlying
        
        :param option_ticker: The option ticker to map
        :param security_type: The security type of the option or underlying
        :returns: The underlying ticker.
        """
        ...


class OptionPortfolioModel(QuantConnect.Securities.SecurityPortfolioModel):
    """
    Provides an implementation of ISecurityPortfolioModel for options that supports
    default fills as well as option exercising.
    """

    def process_close_trade_profit(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> QuantConnect.Securities.ConvertibleCashAmount:
        """
        Helper method to determine the close trade profit
        
        This method is protected.
        """
        ...

    def process_fill(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Performs application of an OrderEvent to the portfolio
        
        :param portfolio: The algorithm's portfolio
        :param security: Option security
        :param fill: The order event fill object to be applied
        """
        ...


class ConstantQLUnderlyingVolatilityEstimator(System.Object, QuantConnect.Securities.Option.IQLUnderlyingVolatilityEstimator):
    """
    Class implements default underlying constant volatility estimator (IQLUnderlyingVolatilityEstimator.), that projects the underlying own volatility
    model into corresponding option pricing model.
    """

    @property
    def is_ready(self) -> bool:
        """Indicates whether volatility model has been warmed ot not"""
        ...

    def estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        """
        Returns current estimate of the underlying volatility
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: The estimate.
        """
        ...


class OptionStrategies(System.Object):
    """
    Provides methods for creating popular OptionStrategy instances.
    These strategies can be directly bought and sold via:
        QCAlgorithm.Buy(OptionStrategy strategy, int quantity)
        QCAlgorithm.Sell(OptionStrategy strategy, int quantity)
    
    See also OptionStrategyDefinitions
    """

    @staticmethod
    def bear_call_ladder(canonical_option: typing.Union[QuantConnect.Symbol, str], lower_strike: float, middle_strike: float, higher_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bear Call Ladder strategy, that consists of three calls with the same expiration but different strikes.
        The strike price of the short call is below the strikes of the two long calls.
        
        :param canonical_option: Option symbol
        :param lower_strike: The strike price of the short call
        :param middle_strike: The middle strike price of one long call
        :param higher_strike: The strike price of one long call with higher strike price
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def bear_call_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], leg_1_strike: float, leg_2_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bear Call Spread strategy, that consists of two calls with the same expiration but different strikes.
        The strike price of the short call is below the strike of the long call. This is a credit spread.
        
        :param canonical_option: Option symbol
        :param leg_1_strike: The strike price of the short call
        :param leg_2_strike: The strike price of the long call
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def bear_put_ladder(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bear Put Ladder strategy, that consists of three puts with the same expiration but different strikes.
        The strike price of the long put is above the strikes of the two short puts.
        
        :param canonical_option: Option symbol
        :param higher_strike: The strike price of the long put
        :param middle_strike: The middle strike price of one short put
        :param lower_strike: The strike price of one short put with lower strike price
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def bear_put_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], leg_1_strike: float, leg_2_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bear Put Spread strategy, that consists of two puts with the same expiration but different strikes.
        The strike price of the short put is below the strike of the long put. This is a debit spread.
        
        :param canonical_option: Option symbol
        :param leg_1_strike: The strike price of the long put
        :param leg_2_strike: The strike price of the short put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def box_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Box Spread strategy which consists of a long call and a short put (buy side) of the same strikes,
        coupled with a short call and a long put (sell side) of higher but same strikes. All options have the same expiry.
        
        :param canonical_option: Option symbol
        :param higher_strike: The strike price of the sell side legs
        :param lower_strike: The strike price of the buy side legs
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def bull_call_ladder(canonical_option: typing.Union[QuantConnect.Symbol, str], lower_strike: float, middle_strike: float, higher_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bull Call Ladder strategy, that consists of three calls with the same expiration but different strikes.
        The strike price of the long call is below the strikes of the two short calls.
        
        :param canonical_option: Option symbol
        :param lower_strike: The strike price of the long call
        :param middle_strike: The middle strike price of one short call
        :param higher_strike: The strike price of one short call with higher strike price
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def bull_call_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], leg_1_strike: float, leg_2_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bull Call Spread strategy, that consists of two calls with the same expiration but different strikes.
        The strike price of the short call is higher than the strike of the long call. This is a debit spread.
        
        :param canonical_option: Option symbol
        :param leg_1_strike: The strike price of the long call
        :param leg_2_strike: The strike price of the short call
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def bull_put_ladder(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bull Put Ladder strategy, that consists of three puts with the same expiration but different strikes.
        The strike price of the short put is above the strikes of the two long puts.
        
        :param canonical_option: Option symbol
        :param higher_strike: The strike price of the short put
        :param middle_strike: The middle strike price of one long put
        :param lower_strike: The strike price of one long put with lower strike price
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def bull_put_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], leg_1_strike: float, leg_2_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Bull Put Spread strategy, that consists of two puts with the same expiration but different strikes.
        The strike price of the short put is above the strike of the long put. This is a credit spread.
        
        :param canonical_option: Option symbol
        :param leg_1_strike: The strike price of the short put
        :param leg_2_strike: The strike price of the long put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def butterfly_call(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Butterfly Call strategy that consists of two short calls at a middle strike,
        and one long call each at a lower and upper strike.
        The upper and lower strikes must both be equidistant from the middle strike.
        
        :param canonical_option: Option symbol
        :param higher_strike: The upper strike price of the long call
        :param middle_strike: The middle strike price of the two short calls
        :param lower_strike: The lower strike price of the long call
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def butterfly_put(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Butterfly Put strategy that consists of two short puts at a middle strike,
        and one long put each at a lower and upper strike.
        The upper and lower strikes must both be equidistant from the middle strike.
        
        :param canonical_option: Option symbol
        :param higher_strike: The upper strike price of the long put
        :param middle_strike: The middle strike price of the two short puts
        :param lower_strike: The lower strike price of the long put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def call_backspread(canonical_option: typing.Union[QuantConnect.Symbol, str], lower_strike: float, higher_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Long Call Backspread strategy, that consists of two calls with the same expiration but different strikes.
        It involves selling the lower strike call, while buying twice the number of the higher strike call.
        
        :param canonical_option: Option symbol
        :param lower_strike: The strike price of the short call
        :param higher_strike: The strike price of the long call
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def call_butterfly(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Call Butterfly strategy, that consists of two short calls at a middle strike, and one long call each at a lower and upper strike.
        The upper and lower strikes must both be equidistant from the middle strike.
        
        :param canonical_option: Option symbol
        :param higher_strike: The upper strike price of the long call
        :param middle_strike: The middle strike price of the two short calls
        :param lower_strike: The lower strike price of the long call
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def call_calendar_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, near_expiration: typing.Union[datetime.datetime, datetime.date], far_expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates new Call Calendar Spread strategy which consists of a short and a long call
        with the same strikes but with the long call having a further expiration date.
        
        :param canonical_option: Option symbol
        :param strike: The strike price of the both legs
        :param near_expiration: Near expiration date for the short option
        :param far_expiration: Far expiration date for the long option
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def conversion(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Conversion strategy that consists of buying 1 put contract, 1 lot of the underlying and selling 1 call contract.
        Put and call must have the same expiration date, underlying (multiplier), and strike price.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the call and put option contract
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def covered_call(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Covered Call strategy that consists of selling one call contract and buying 1 lot of the underlying.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the call option contract
        :param expiration: The expiration date for the call option contract
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def covered_put(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Covered Put strategy that consists of selling 1 put contract and 1 lot of the underlying.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the put option contract
        :param expiration: The expiration date for the put option contract
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def iron_butterfly(canonical_option: typing.Union[QuantConnect.Symbol, str], otm_put_strike: float, atm_strike: float, otm_call_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Iron Butterfly strategy which consists of a short ATM call, a short ATM put, a long OTM call, and a long OTM put.
        all with the same expiration date and with increasing strikes prices in the mentioned order.
        
        :param canonical_option: Option symbol
        :param otm_put_strike: OTM put option strike price
        :param atm_strike: 2 ATM options strike price
        :param otm_call_strike: OTM call option strike price
        :param expiration: Expiration date for all the options
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def iron_condor(canonical_option: typing.Union[QuantConnect.Symbol, str], long_put_strike: float, short_put_strike: float, short_call_strike: float, long_call_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Iron Condor strategy which consists of a long put, a short put, a short call and a long option,
        all with the same expiration date and with increasing strikes prices in the mentioned order.
        
        :param canonical_option: Option symbol
        :param long_put_strike: Long put option strike price
        :param short_put_strike: Short put option strike price
        :param short_call_strike: Short call option strike price
        :param long_call_strike: Long call option strike price
        :param expiration: Expiration date for all the options
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def jelly_roll(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, near_expiration: typing.Union[datetime.datetime, datetime.date], far_expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates new Jelly Roll strategy which combines a long call calendar spread and a short put calendar spread
        with the same strikes and the same pair of expiration dates.
        
        :param canonical_option: Option symbol
        :param strike: The strike price of the all legs
        :param near_expiration: Near expiration date for the short call and the long put
        :param far_expiration: Far expiration date for the long call and the short put
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def naked_call(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Naked Call strategy that consists of selling 1 call contract.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the call option contract
        :param expiration: The expiration date for the call option contract
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def naked_put(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Naked Put strategy that consists of selling 1 put contract.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the put option contract
        :param expiration: The expiration date for the put option contract
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def protective_call(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Protective Call strategy that consists of buying one call contract and selling 1 lot of the underlying.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the call option contract
        :param expiration: The expiration date for the call option contract
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def protective_collar(canonical_option: typing.Union[QuantConnect.Symbol, str], call_strike: float, put_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Protective Collar strategy that consists of buying 1 put contract and 1 lot of the underlying.
        
        :param canonical_option: Option symbol
        :param call_strike: The strike price for the call option contract
        :param put_strike: The strike price for the put option contract
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def protective_put(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Protective Put strategy that consists of buying 1 put contract and 1 lot of the underlying.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the put option contract
        :param expiration: The expiration date for the put option contract
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def put_backspread(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Long Put Backspread strategy, that consists of two puts with the same expiration but different strikes.
        It involves selling the higher strike put, while buying twice the number of the lower strike put.
        
        :param canonical_option: Option symbol
        :param higher_strike: The strike price of the short put
        :param lower_strike: The strike price of the long put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def put_butterfly(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Put Butterfly strategy, that consists of two short puts at a middle strike, and one long put each at a lower and upper strike.
        The upper and lower strikes must both be equidistant from the middle strike.
        
        :param canonical_option: Option symbol
        :param higher_strike: The upper strike price of the long put
        :param middle_strike: The middle strike price of the two short puts
        :param lower_strike: The lower strike price of the long put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def put_calendar_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, near_expiration: typing.Union[datetime.datetime, datetime.date], far_expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates new Put Calendar Spread strategy which consists of a short and a long put
        with the same strikes but with the long put having a further expiration date.
        
        :param canonical_option: Option symbol
        :param strike: The strike price of the both legs
        :param near_expiration: Near expiration date for the short option
        :param far_expiration: Far expiration date for the long option
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def reverse_conversion(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Reverse Conversion strategy that consists of buying 1 put contract and 1 lot of the underlying.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the put option contract
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_box_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Short Box Spread strategy which consists of a long call and a short put (buy side) of the same strikes,
        coupled with a short call and a long put (sell side) of lower but same strikes. All options have the same expiry.
        
        :param canonical_option: Option symbol
        :param higher_strike: The strike price of the buy side
        :param lower_strike: The strike price of the sell side
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_butterfly_call(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Butterfly Call strategy that consists of two long calls at a middle strike,
        and one short call each at a lower and upper strike.
        The upper and lower strikes must both be equidistant from the middle strike.
        
        :param canonical_option: Option symbol
        :param higher_strike: The upper strike price of the short call
        :param middle_strike: The middle strike price of the two long calls
        :param lower_strike: The lower strike price of the short call
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_butterfly_put(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, middle_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Butterfly Put strategy that consists of two long puts at a middle strike,
        and one short put each at a lower and upper strike.
        The upper and lower strikes must both be equidistant from the middle strike.
        
        :param canonical_option: Option symbol
        :param higher_strike: The upper strike price of the short put
        :param middle_strike: The middle strike price of the two long puts
        :param lower_strike: The lower strike price of the short put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_call_backspread(canonical_option: typing.Union[QuantConnect.Symbol, str], lower_strike: float, higher_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Short Call Backspread strategy, that consists of two calls with the same expiration but different strikes.
        It involves buying the lower strike call, while shorting twice the number of the higher strike call.
        
        :param canonical_option: Option symbol
        :param lower_strike: The strike price of the long call
        :param higher_strike: The strike price of the short call
        :param expiration: Option expiration date
        """
        ...

    @staticmethod
    def short_call_calendar_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, near_expiration: typing.Union[datetime.datetime, datetime.date], far_expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates new Short Call Calendar Spread strategy which consists of a short and a long call
        with the same strikes but with the short call having a further expiration date.
        
        :param canonical_option: Option symbol
        :param strike: The strike price of the both legs
        :param near_expiration: Near expiration date for the long option
        :param far_expiration: Far expiration date for the short option
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_iron_butterfly(canonical_option: typing.Union[QuantConnect.Symbol, str], otm_put_strike: float, atm_strike: float, otm_call_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Short Iron Butterfly strategy which consists of a long ATM call, a long ATM put, a short OTM call, and a short OTM put,
        all with the same expiration date and with increasing strikes prices in the mentioned order.
        It is the inverse of an .
        
        :param canonical_option: Option symbol
        :param otm_put_strike: OTM put option strike price
        :param atm_strike: 2 ATM options strike price
        :param otm_call_strike: OTM call option strike price
        :param expiration: Expiration date for all the options
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_iron_condor(canonical_option: typing.Union[QuantConnect.Symbol, str], short_put_strike: float, long_put_strike: float, long_call_strike: float, short_call_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a new Short Iron Condor strategy which consists of a short put, a long put, a long call and a short call,
        all with the same expiration date and with increasing strikes prices in the mentioned order.
        
        :param canonical_option: Option symbol
        :param short_put_strike: Short put option strike price
        :param long_put_strike: Long put option strike price
        :param long_call_strike: Long call option strike price
        :param short_call_strike: Short call option strike price
        :param expiration: Expiration date for all the options
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_jelly_roll(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, near_expiration: typing.Union[datetime.datetime, datetime.date], far_expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates new Short Jelly Roll strategy which combines a long call calendar spread and a short put calendar spread
        with the same strikes and the same pair of expiration dates.
        
        :param canonical_option: Option symbol
        :param strike: The strike price of the all legs
        :param near_expiration: Near expiration date for the short call and the long put
        :param far_expiration: Far expiration date for the long call and the short put
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_put_backspread(canonical_option: typing.Union[QuantConnect.Symbol, str], higher_strike: float, lower_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Short Put Backspread strategy, that consists of two puts with the same expiration but different strikes.
        It involves buying the higher strike put, while selling twice the number of the lower strike put.
        
        :param canonical_option: Option symbol
        :param higher_strike: The strike price of the long put
        :param lower_strike: The strike price of the short put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_put_calendar_spread(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, near_expiration: typing.Union[datetime.datetime, datetime.date], far_expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates new Short Put Calendar Spread strategy which consists of a short and a long put
        with the same strikes but with the short put having a further expiration date.
        
        :param canonical_option: Option symbol
        :param strike: The strike price of the both legs
        :param near_expiration: Near expiration date for the long option
        :param far_expiration: Far expiration date for the short option
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_straddle(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Short Straddle strategy that consists of selling a call and a put, both with the same strike price and expiration.
        
        :param canonical_option: Option symbol
        :param strike: The strike price for the option contracts
        :param expiration: The expiration date for the option contracts
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def short_strangle(canonical_option: typing.Union[QuantConnect.Symbol, str], call_leg_strike: float, put_leg_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Creates a Short Strangle strategy that consists of selling a call and a put, with the same expiration date and
        the call strike being above the put strike.
        
        :param canonical_option: Option symbol
        :param call_leg_strike: The strike price of the short call
        :param put_leg_strike: The strike price of the short put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def straddle(canonical_option: typing.Union[QuantConnect.Symbol, str], strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Straddle strategy, that is a combination of buying a call and buying a put, both with the same strike price and expiration.
        
        :param canonical_option: Option symbol
        :param strike: The strike price of the both legs
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...

    @staticmethod
    def strangle(canonical_option: typing.Union[QuantConnect.Symbol, str], call_leg_strike: float, put_leg_strike: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.Option.OptionStrategy:
        """
        Method creates new Strangle strategy, that buying a call option and a put option with the same expiration date
        The strike price of the call is above the strike of the put.
        
        :param canonical_option: Option symbol
        :param call_leg_strike: The strike price of the long call
        :param put_leg_strike: The strike price of the long put
        :param expiration: Option expiration date
        :returns: Option strategy specification.
        """
        ...


class OptionStrategyPositionGroupBuyingPowerModel(QuantConnect.Securities.Positions.PositionGroupBuyingPowerModel):
    """Option strategy buying power model"""

    def __init__(self, optionStrategy: QuantConnect.Securities.Option.OptionStrategy) -> None:
        """
        Creates a new instance for a target option strategy
        
        :param optionStrategy: The option strategy to model
        """
        ...

    def get_contemplated_groups_initial_margin(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, contemplated_groups: QuantConnect.Securities.Positions.PositionGroupCollection, orders_positions: System.Collections.Generic.List[QuantConnect.Securities.Positions.IPosition]) -> float:
        """
        Gets the initial margin required for the specified contemplated position group.
        Used by QuantConnect.Securities.Positions.PositionGroupBuyingPowerModel.GetReservedBuyingPowerImpact to get the contemplated groups margin.
        
        This method is protected.
        """
        ...

    def get_initial_margin_required_for_order(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.Positions.PositionGroupMaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class FedRateQLRiskFreeRateEstimator(System.Object, QuantConnect.Securities.Option.IQLRiskFreeRateEstimator):
    """Class implements Fed's US primary credit rate as risk free rate, implementing IQLRiskFreeRateEstimator."""

    def estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        """
        Returns current flat estimate of the risk free rate
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: The estimate.
        """
        ...


class ConstantQLRiskFreeRateEstimator(System.Object, QuantConnect.Securities.Option.IQLRiskFreeRateEstimator):
    """Class implements default flat risk free curve, implementing IQLRiskFreeRateEstimator."""

    def __init__(self, riskFreeRate: float = 0.01) -> None:
        """Constructor initializes class with risk free rate constant"""
        ...

    def estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        """
        Returns current flat estimate of the risk free rate
        
        :param security: The option security object
        :param slice: The current data slice. This can be used to access other information available to the algorithm
        :param contract: The option contract to evaluate
        :returns: The estimate.
        """
        ...


class FuturesOptionsMarginModel(QuantConnect.Securities.Future.FutureMarginModel):
    """
    Defines a margin model for future options (an option with a future as its underlying).
    We re-use the FutureMarginModel implementation and multiply its results
    by 1.5x to simulate the increased margins seen for future options.
    """

    @property
    def initial_overnight_margin_requirement(self) -> float:
        """Initial Overnight margin requirement for the contract effective from the date of change"""
        ...

    @property
    def maintenance_overnight_margin_requirement(self) -> float:
        """Maintenance Overnight margin requirement for the contract effective from the date of change"""
        ...

    @property
    def initial_intraday_margin_requirement(self) -> float:
        """Initial Intraday margin for the contract effective from the date of change"""
        ...

    @property
    def maintenance_intraday_margin_requirement(self) -> float:
        """Maintenance Intraday margin requirement for the contract effective from the date of change"""
        ...

    def __init__(self, requiredFreeBuyingPowerPercent: float = 0, futureOption: QuantConnect.Securities.Option.Option = None) -> None:
        """
        Creates an instance of FutureOptionMarginModel
        
        :param requiredFreeBuyingPowerPercent: The percentage used to determine the required unused buying power for the account.
        :param futureOption: Option Security containing a Future security as the underlying
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

    @staticmethod
    def get_margin_requirement(option: QuantConnect.Securities.Option.Option, underlying_requirement: float, position_side: QuantConnect.PositionSide = ...) -> int:
        """
        Get's the margin requirement for a future option based on the underlying future margin requirement and the position side to trade.
        FOPs margin requirement is an 'S' curve based on the underlying requirement around it's current price, see https://en.wikipedia.org/wiki/Logistic_function
        
        :param option: The future option contract to trade
        :param underlying_requirement: The underlying future associated margin requirement
        :param position_side: The position side to trade, long by default. This is because short positions require higher margin requirements
        """
        ...


