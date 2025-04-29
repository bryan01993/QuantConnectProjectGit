from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Securities
import System
import System.Collections.Generic


class OrderFee(System.Object):
    """Defines the result for IFeeModel.GetOrderFee"""

    @property
    def value(self) -> QuantConnect.Securities.CashAmount:
        """Gets the order fee"""
        ...

    @property.setter
    def value(self, value: QuantConnect.Securities.CashAmount) -> None:
        ...

    ZERO: QuantConnect.Orders.Fees.OrderFee = ...
    """Gets an instance of OrderFee that represents zero."""

    def __init__(self, orderFee: QuantConnect.Securities.CashAmount) -> None:
        """
        Initializes a new instance of the OrderFee class
        
        :param orderFee: The order fee
        """
        ...

    def apply_to_portfolio(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Applies the order fee to the given portfolio
        
        :param portfolio: The portfolio instance
        :param fill: The order fill event
        """
        ...

    def to_string(self) -> str:
        """This is for backward compatibility with old 'decimal' order fee"""
        ...


class OrderFeeParameters(System.Object):
    """Defines the parameters for IFeeModel.GetOrderFee"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the OrderFeeParameters class
        
        :param security: The security
        :param order: The order
        """
        ...


class IFeeModel(metaclass=abc.ABCMeta):
    """Represents a model the simulates order fees"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class FeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Base class for any order fee model"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class CharlesSchwabFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Represents a fee model specific to Charles Schwab."""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Calculates the order fee based on the security type and order parameters.
        
        :param parameters: The parameters for the order fee calculation, which include security and order details.
        :returns: An OrderFee instance representing the calculated order fee.
        """
        ...


class AlphaStreamsFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models order fees that alpha stream clients pay/receive"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class ConstantFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an order fee model that always returns the same order fee."""

    def __init__(self, fee: float, currency: str = "USD") -> None:
        """
        Initializes a new instance of the ConstantFeeModel class with the specified
        
        :param fee: The constant order fee used by the model
        :param currency: The currency of the order fee
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Returns the constant fee for the model in units of the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class CoinbaseFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Represents a fee model specific to Coinbase.
    This class extends the base fee model.
    """

    MAKER_ADVANCED_1: float = 0.006
    """
    Level Advanced 1 maker fee
    Tab "Fee tiers" on https://www.coinbase.com/advanced-fees
    """

    TAKER_ADVANCED_1: float = 0.008
    """
    Level Advanced 1 taker fee
    Tab "Fee tiers" on https://www.coinbase.com/advanced-fees
    """

    MAKER_STABLE_PAIRS: float = 0
    """
    Stable Pairs maker fee
    Tab "Stable pairs" on https://www.coinbase.com/advanced-fees
    """

    TAKER_STABLE_PARIS: float = 0.00001
    """
    Stable Pairs taker fee
    Tab "Stable pairs" on https://www.coinbase.com/advanced-fees
    """

    def __init__(self, makerFee: float = ..., takerFee: float = ...) -> None:
        """
        Create Coinbase Fee model setting fee values
        
        :param makerFee: Maker fee value
        :param takerFee: Taker fee value
        """
        ...

    @staticmethod
    def get_fee_percentage(utc_time: typing.Union[datetime.datetime, datetime.date], is_maker: bool, is_stable_coin: bool, maker_fee: float, taker_fee: float) -> float:
        """
        Returns the maker/taker fee percentage effective at the requested date.
        
        This method is protected.
        
        :param utc_time: The date/time requested (UTC)
        :param is_maker: true if the maker percentage fee is requested, false otherwise
        :param is_stable_coin: true if the order security symbol is a StableCoin, false otherwise
        :param maker_fee: maker fee amount
        :param taker_fee: taker fee amount
        :returns: The fee percentage.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class IndiaFeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def brokerage_multiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @property.setter
    def brokerage_multiplier(self, value: float) -> None:
        ...

    @property
    def max_brokerage(self) -> float:
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @property.setter
    def max_brokerage(self, value: float) -> None:
        ...

    @property
    def securities_transaction_tax_total_multiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property.setter
    def securities_transaction_tax_total_multiplier(self, value: float) -> None:
        ...

    @property
    def exchange_transaction_charge_multiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @property.setter
    def exchange_transaction_charge_multiplier(self, value: float) -> None:
        ...

    @property
    def state_tax_multiplier(self) -> float:
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property.setter
    def state_tax_multiplier(self, value: float) -> None:
        ...

    @property
    def sebi_charges_multiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property.setter
    def sebi_charges_multiplier(self, value: float) -> None:
        ...

    @property
    def stamp_charges_multiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property.setter
    def stamp_charges_multiplier(self, value: float) -> None:
        ...

    @property
    def is_stamp_charges_from_order_value(self) -> bool:
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        This property is protected.
        """
        ...

    @property.setter
    def is_stamp_charges_from_order_value(self, value: bool) -> None:
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        """
        ...


class ZerodhaFeeModel(QuantConnect.Orders.Fees.IndiaFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def brokerage_multiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def max_brokerage(self) -> float:
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @property
    def securities_transaction_tax_total_multiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def exchange_transaction_charge_multiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def state_tax_multiplier(self) -> float:
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def sebi_charges_multiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def stamp_charges_multiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def is_stamp_charges_from_order_value(self) -> bool:
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        This property is protected.
        """
        ...


class InteractiveBrokersFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides the default implementation of IFeeModel"""

    def __init__(self, monthlyForexTradeAmountInUSDollars: float = 0, monthlyOptionsTradeAmountInContracts: float = 0) -> None:
        """
        Initializes a new instance of the ImmediateFillModel
        
        :param monthlyForexTradeAmountInUSDollars: Monthly FX dollar volume traded
        :param monthlyOptionsTradeAmountInContracts: Monthly options contracts traded
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...

    @staticmethod
    def get_potential_order_price(order: QuantConnect.Orders.Order, security: QuantConnect.Securities.Security) -> float:
        """
        Approximates the order's price based on the order type
        
        This method is protected.
        """
        ...


class EzeFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Eze fee model implementation"""


class AlpacaFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Represents the fee model specific to Alpaca trading platform."""

    MAKER_CRYPTO_FEE: float = 0.0015
    """The fee percentage for a maker transaction in cryptocurrency."""

    TAKER_CRYPTO_FEE: float = 0.0025
    """The fee percentage for a taker transaction in cryptocurrency."""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class AxosFeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Provides an implementation of FeeModel that models Axos order fees"""

    def __init__(self, feesPerShare: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param feesPerShare: The fees per share to apply
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class FeeModelExtensions(System.Object):
    """
    Provide extension method for IFeeModel to enable
    backwards compatibility of invocations.
    """

    @staticmethod
    def get_order_fee(model: QuantConnect.Orders.Fees.IFeeModel, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param model: The fee model
        :param security: The security matching the order
        :param order: The order to compute fees for
        :returns: The cost of the order in units of the account currency.
        """
        ...


class TDAmeritradeFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models TDAmeritrade order fees"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class RBIFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models RBI order fees"""

    def __init__(self, feesPerShare: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param feesPerShare: The fees per share to apply
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class BinanceFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Binance order fees"""

    MAKER_TIER_1_FEE: float = 0.001
    """
    Tier 1 maker fees
    https://www.binance.com/en/fee/schedule
    """

    TAKER_TIER_1_FEE: float = 0.001
    """
    Tier 1 taker fees
    https://www.binance.com/en/fee/schedule
    """

    def __init__(self, mFee: float = ..., tFee: float = ...) -> None:
        """
        Creates Binance fee model setting fees values
        
        :param mFee: Maker fee value
        :param tFee: Taker fee value
        """
        ...

    @overload
    def get_fee(self, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the fee factor for the given order
        
        This method is protected.
        
        :param order: The order to get the fee factor for
        :returns: The fee factor for the given order.
        """
        ...

    @staticmethod
    @overload
    def get_fee(order: QuantConnect.Orders.Order, maker_fee: float, taker_fee: float) -> float:
        """
        Gets the fee factor for the given order taking into account the maker and the taker fee
        
        This method is protected.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class BinanceCoinFuturesFeeModel(QuantConnect.Orders.Fees.BinanceFeeModel):
    """Provides an implementation of FeeModel that models Binance Coin Futures order fees"""

    MAKER_TIER_1_FEE: float = 0.0001
    """
    Tier 1 maker fees
    https://www.binance.com/en/fee/deliveryFee
    """

    TAKER_TIER_1_FEE: float = 0.0005
    """
    Tier 1 taker fees
    https://www.binance.com/en/fee/deliveryFee
    """

    def __init__(self, mFee: float = ..., tFee: float = ...) -> None:
        """
        Creates Binance Coin Futures fee model setting fees values
        
        :param mFee: Maker fee value
        :param tFee: Taker fee value
        """
        ...


class GDAXFeeModel(QuantConnect.Orders.Fees.CoinbaseFeeModel):
    """
    Provides an implementation of FeeModel that models GDAX order fees
    
    GDAXFeeModel is deprecated. Use CoinbaseFeeModel instead.
    """


class FTXFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Provides an implementation of FeeModel that models FTX order fees
    https://help.ftx.com/hc/en-us/articles/360024479432-Fees
    """

    @property
    def maker_fee(self) -> float:
        """Tier 1 maker fees"""
        ...

    @property
    def taker_fee(self) -> float:
        """Tier 1 taker fees"""
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class ExanteFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Provides an implementation of FeeModel that models Exante order fees.
    According to:
    https://support.exante.eu/hc/en-us/articles/115005873143-Fees-overview-exchange-imposed-fees?source=searchhttps://exante.eu/markets/
    """

    MARKET_USA_RATE: float = 0.02
    """Market USA rate"""

    DEFAULT_RATE: float = 0.02
    """Default rate"""

    def __init__(self, forexCommissionRate: float = 0.25) -> None:
        """
        Creates a new instance
        
        :param forexCommissionRate: Commission rate for FX operations
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class BybitFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Bybit fee model implementation"""

    MAKER_NON_VIP_FEE: float = 0.001
    """
    Tier 1 maker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    TAKER_NON_VIP_FEE: float = 0.001
    """
    Tier 1 taker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    def __init__(self, mFee: float = ..., tFee: float = ...) -> None:
        """
        Creates Binance fee model setting fees values
        
        :param mFee: Maker fee value
        :param tFee: Taker fee value
        """
        ...

    def get_fee(self, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the fee factor for the given order
        
        This method is protected.
        
        :param order: The order to get the fee factor for
        :returns: The fee factor for the given order.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class WolverineFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Wolverine order fees"""

    def __init__(self, feesPerShare: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param feesPerShare: The fees per share to apply
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class BybitFuturesFeeModel(QuantConnect.Orders.Fees.BybitFeeModel):
    """Bybit futures fee model implementation"""

    MAKER_NON_VIP_FEE: float = 0.0002
    """
    Tier 1 maker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    TAKER_NON_VIP_FEE: float = 0.00055
    """
    Tier 1 taker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    def __init__(self, makerFee: float = ..., takerFee: float = ...) -> None:
        """
        Initializes a new instance of the BybitFuturesFeeModel class
        
        :param makerFee: The accounts maker fee
        :param takerFee: The accounts taker fee
        """
        ...


class KrakenFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Kraken order fees"""

    MAKER_TIER_1_CRYPTO_FEE: float = 0.0016
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#kraken-pro
    """

    TAKER_TIER_1_CRYPTO_FEE: float = 0.0026
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#kraken-pro
    """

    TIER_1_FX_FEE: float = 0.002
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#stablecoin-fx-pairs
    """

    @property
    def fx_stablecoin_list(self) -> System.Collections.Generic.List[str]:
        """Fiats and stablecoins list that have own fee."""
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order.
        If sell - fees in base currency
        If buy - fees in quote currency
        It can be defined manually in KrakenOrderProperties
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The fee of the order.
        """
        ...


class FTXUSFeeModel(QuantConnect.Orders.Fees.FTXFeeModel):
    """
    Provides an implementation of FeeModel that models FTX order fees
    https://help.ftx.us/hc/en-us/articles/360043579273-Fees
    """

    @property
    def maker_fee(self) -> float:
        """Tier 1 maker fees"""
        ...

    @property
    def taker_fee(self) -> float:
        """Tier 1 taker fees"""
        ...


class BitfinexFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Bitfinex order fees"""

    MAKER_FEE: float = 0.001
    """
    Tier 1 maker fees
    Maker fees are paid when you add liquidity to our order book by placing a limit order under the ticker price for buy and above the ticker price for sell.
    https://www.bitfinex.com/fees
    """

    TAKER_FEE: float = 0.002
    """
    Tier 1 taker fees
    Taker fees are paid when you remove liquidity from our order book by placing any order that is executed against an order of the order book.
    Note: If you place a hidden order, you will always pay the taker fee. If you place a limit order that hits a hidden order, you will always pay the maker fee.
    https://www.bitfinex.com/fees
    """

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class TradeStationFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Represents a fee model specific to TradeStation."""

    @property
    def us_resident(self) -> bool:
        """Gets or sets a value indicating whether the entity or person is a resident of the United States."""
        ...

    @property.setter
    def us_resident(self, value: bool) -> None:
        ...

    def __init__(self, usResident: bool = True) -> None:
        """
        Initializes a new instance of the TradeStationFeeModel class.
        
        :param usResident: A boolean value indicating whether the entity or person is a US resident. Default is true.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Calculates the order fee based on the security type and order parameters.
        
        :param parameters: The parameters for the order fee calculation, which include security and order details.
        :returns: An OrderFee instance representing the calculated order fee.
        """
        ...


class ModifiedFillQuantityOrderFee(QuantConnect.Orders.Fees.OrderFee):
    """
    An order fee where the fee quantity has already been subtracted from the filled quantity so instead we subtracted
    from the quote currency when applied to the portfolio
    """

    def __init__(self, orderFee: QuantConnect.Securities.CashAmount, quoteCurrency: str, contractMultiplier: float) -> None:
        """
        Initializes a new instance of the ModifiedFillQuantityOrderFee class
        
        :param orderFee: The order fee
        :param quoteCurrency: The associated security quote currency
        :param contractMultiplier: The associated security contract multiplier
        """
        ...

    def apply_to_portfolio(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Applies the order fee to the given portfolio
        
        :param portfolio: The portfolio instance
        :param fill: The order fill event
        """
        ...


class FxcmFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models FXCM order fees"""

    def __init__(self, currency: str = "USD") -> None:
        """
        Creates a new instance
        
        :param currency: The currency of the order fee, for FXCM this is the account currency
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in units of the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class SamcoFeeModel(QuantConnect.Orders.Fees.IndiaFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def brokerage_multiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def max_brokerage(self) -> float:
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @property
    def securities_transaction_tax_total_multiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def exchange_transaction_charge_multiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def state_tax_multiplier(self) -> float:
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def sebi_charges_multiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def stamp_charges_multiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...


class BinanceFuturesFeeModel(QuantConnect.Orders.Fees.BinanceFeeModel):
    """Provides an implementation of FeeModel that models Binance Futures order fees"""

    MAKER_TIER_1_USDT_FEE: float = 0.0002
    """
    Tier 1 USDT maker fees
    https://www.binance.com/en/fee/futureFee
    """

    TAKER_TIER_1_USDT_FEE: float = 0.0004
    """
    Tier 1 USDT taker fees
    https://www.binance.com/en/fee/futureFee
    """

    MAKER_TIER_1_BUSD_FEE: float = 0.00012
    """
    Tier 1 BUSD maker fees
    https://www.binance.com/en/fee/futureFee
    """

    TAKER_TIER_1_BUSD_FEE: float = 0.00036
    """
    Tier 1 BUSD taker fees
    https://www.binance.com/en/fee/futureFee
    """

    def __init__(self, mUsdtFee: float = ..., tUsdtFee: float = ..., mBusdFee: float = ..., tBusdFee: float = ...) -> None:
        """
        Creates Binance Futures fee model setting fees values
        
        :param mUsdtFee: Maker fee value for USDT pair contracts
        :param tUsdtFee: Taker fee value for USDT pair contracts
        :param mBusdFee: Maker fee value for BUSD pair contracts
        :param tBusdFee: Taker fee value for BUSD pair contracts
        """
        ...

    def get_fee(self, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the fee for the given order
        
        This method is protected.
        """
        ...


