from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Api
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Serialization
import QuantConnect.Securities
import QuantConnect.Securities.Positions
import System
import System.Collections.Generic
import System.Threading

JsonConverter = typing.Any

QuantConnect_Orders_OrderTicket_Get_T = typing.TypeVar("QuantConnect_Orders_OrderTicket_Get_T")


class OrderDirection(Enum):
    """Direction of the order"""

    BUY = 0
    """Buy Order (0)"""

    SELL = 1
    """Sell Order (1)"""

    HOLD = 2
    """Default Value - No Order Direction (2)"""


class GroupOrderManager(System.Object):
    """Manager of a group of orders"""

    @property
    def id(self) -> int:
        """The unique order group Id"""
        ...

    @property
    def quantity(self) -> float:
        """The group order quantity"""
        ...

    @property
    def count(self) -> int:
        """The total order count associated with this order group"""
        ...

    @property
    def limit_price(self) -> float:
        """The limit price associated with this order group if any"""
        ...

    @property.setter
    def limit_price(self, value: float) -> None:
        ...

    @property
    def order_ids(self) -> System.Collections.Generic.HashSet[int]:
        """The order Ids in this group"""
        ...

    @property
    def direction(self) -> QuantConnect.Orders.OrderDirection:
        """Order Direction Property based off Quantity."""
        ...

    @property
    def absolute_quantity(self) -> float:
        """Get the absolute quantity for this combo order"""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new empty instance"""
        ...

    @overload
    def __init__(self, id: int, legCount: int, quantity: float, limitPrice: float = 0) -> None:
        """
        Creates a new instance of GroupOrderManager
        
        :param id: This order group unique Id
        :param legCount: The order leg count
        :param quantity: The group order quantity
        :param limitPrice: The limit price associated with this order group if any
        """
        ...

    @overload
    def __init__(self, legCount: int, quantity: float, limitPrice: float = 0) -> None:
        """
        Creates a new instance of GroupOrderManager
        
        :param legCount: The order leg count
        :param quantity: The group order quantity
        :param limitPrice: The limit price associated with this order group if any
        """
        ...


class OrderStatus(Enum):
    """Fill status of the order class."""

    NEW = 0
    """New order pre-submission to the order processor (0)"""

    SUBMITTED = 1
    """Order submitted to the market (1)"""

    PARTIALLY_FILLED = 2
    """Partially filled, In Market Order (2)"""

    FILLED = 3
    """Completed, Filled, In Market Order (3)"""

    CANCELED = 5
    """Order cancelled before it was filled (5)"""

    NONE = 6
    """No Order State Yet (6)"""

    INVALID = 7
    """Order invalidated before it hit the market (e.g. insufficient capital) (7)"""

    CANCEL_PENDING = 8
    """Order waiting for confirmation of cancellation (8)"""

    UPDATE_SUBMITTED = 9
    """Order update submitted to the market (9)"""


class OrderEvent(System.Object):
    """Order Event - Messaging class signifying a change in an order state and record the change in the user's algorithm portfolio"""

    @property
    def order_id(self) -> int:
        """Id of the order this event comes from."""
        ...

    @property.setter
    def order_id(self, value: int) -> None:
        ...

    @property
    def id(self) -> int:
        """The unique order event id for each order"""
        ...

    @property.setter
    def id(self, value: int) -> None:
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Easy access to the order symbol associated with this event."""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def utc_time(self) -> datetime.datetime:
        """The date and time of this event (UTC)."""
        ...

    @property.setter
    def utc_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def status(self) -> QuantConnect.Orders.OrderStatus:
        """Status message of the order."""
        ...

    @property.setter
    def status(self, value: QuantConnect.Orders.OrderStatus) -> None:
        ...

    @property
    def order_fee(self) -> QuantConnect.Orders.Fees.OrderFee:
        """The fee associated with the order"""
        ...

    @property.setter
    def order_fee(self, value: QuantConnect.Orders.Fees.OrderFee) -> None:
        ...

    @property
    def fill_price(self) -> float:
        """Fill price information about the order"""
        ...

    @property.setter
    def fill_price(self, value: float) -> None:
        ...

    @property
    def fill_price_currency(self) -> str:
        """Currency for the fill price"""
        ...

    @property.setter
    def fill_price_currency(self, value: str) -> None:
        ...

    @property
    def fill_quantity(self) -> float:
        """Number of shares of the order that was filled in this event."""
        ...

    @property.setter
    def fill_quantity(self, value: float) -> None:
        ...

    @property
    def absolute_fill_quantity(self) -> float:
        """Public Property Absolute Getter of Quantity -Filled"""
        ...

    @property
    def direction(self) -> QuantConnect.Orders.OrderDirection:
        """Order direction."""
        ...

    @property.setter
    def direction(self, value: QuantConnect.Orders.OrderDirection) -> None:
        ...

    @property
    def message(self) -> str:
        """Any message from the exchange."""
        ...

    @property.setter
    def message(self, value: str) -> None:
        ...

    @property
    def is_assignment(self) -> bool:
        """True if the order event is an assignment"""
        ...

    @property.setter
    def is_assignment(self, value: bool) -> None:
        ...

    @property
    def stop_price(self) -> typing.Optional[float]:
        """The current stop price"""
        ...

    @property.setter
    def stop_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trigger_price(self) -> typing.Optional[float]:
        """The current trigger price"""
        ...

    @property.setter
    def trigger_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def limit_price(self) -> typing.Optional[float]:
        """The current limit price"""
        ...

    @property.setter
    def limit_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def quantity(self) -> float:
        """The current order quantity"""
        ...

    @property.setter
    def quantity(self, value: float) -> None:
        ...

    @property
    def is_in_the_money(self) -> bool:
        """True if the order event's option is In-The-Money (ITM)"""
        ...

    @property.setter
    def is_in_the_money(self, value: bool) -> None:
        ...

    @property
    def trailing_amount(self) -> typing.Optional[float]:
        """The trailing stop amount"""
        ...

    @property.setter
    def trailing_amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trailing_as_percentage(self) -> typing.Optional[bool]:
        """Whether the TrailingAmount is a percentage or an absolute currency value"""
        ...

    @property.setter
    def trailing_as_percentage(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    def ticket(self) -> QuantConnect.Orders.OrderTicket:
        """The order ticket associated to the order"""
        ...

    @property.setter
    def ticket(self, value: QuantConnect.Orders.OrderTicket) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Order Event empty constructor required for json converter"""
        ...

    @overload
    def __init__(self, orderId: int, symbol: typing.Union[QuantConnect.Symbol, str], utcTime: typing.Union[datetime.datetime, datetime.date], status: QuantConnect.Orders.OrderStatus, direction: QuantConnect.Orders.OrderDirection, fillPrice: float, fillQuantity: float, orderFee: QuantConnect.Orders.Fees.OrderFee, message: str = ...) -> None:
        """
        Order Event Constructor.
        
        :param orderId: Id of the parent order
        :param symbol: Asset Symbol
        :param utcTime: Date/time of this event
        :param status: Status of the order
        :param direction: The direction of the order this event belongs to
        :param fillPrice: Fill price information if applicable.
        :param fillQuantity: Fill quantity
        :param orderFee: The order fee
        :param message: Message from the exchange
        """
        ...

    @overload
    def __init__(self, order: QuantConnect.Orders.Order, utcTime: typing.Union[datetime.datetime, datetime.date], orderFee: QuantConnect.Orders.Fees.OrderFee, message: str = ...) -> None:
        """
        Helper Constructor using Order to Initialize.
        
        :param order: Order for this order status
        :param utcTime: Date/time of this event
        :param orderFee: The order fee
        :param message: Message from exchange or QC.
        """
        ...

    def clone(self) -> QuantConnect.Orders.OrderEvent:
        """
        Returns a clone of the current object.
        
        :returns: The new clone object.
        """
        ...

    @staticmethod
    def from_serialized(serialized_order_event: QuantConnect.Orders.Serialization.SerializedOrderEvent) -> QuantConnect.Orders.OrderEvent:
        """Creates a new instance based on the provided serialized order event"""
        ...

    def short_to_string(self) -> str:
        """Returns a short string that represents the current object."""
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class TimeInForce(System.Object, QuantConnect.Interfaces.ITimeInForceHandler, metaclass=abc.ABCMeta):
    """Time In Force - defines the length of time over which an order will continue working before it is canceled"""

    GOOD_TIL_CANCELED: QuantConnect.Orders.TimeInForce = ...
    """Gets a GoodTilCanceledTimeInForce instance"""

    DAY: QuantConnect.Orders.TimeInForce = ...
    """Gets a DayTimeInForce instance"""

    GOOD_TIL_DATE: typing.Callable[[datetime.datetime], QuantConnect.Orders.TimeInForce]
    """Gets a GoodTilDateTimeInForce instance"""

    def is_fill_valid(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> bool:
        """
        Checks if an order fill is valid
        
        :param security: The security matching the order
        :param order: The order to be checked
        :param fill: The order fill to be checked
        :returns: Returns true if the order fill can be emitted, false otherwise.
        """
        ...

    def is_order_expired(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Checks if an order is expired
        
        :param security: The security matching the order
        :param order: The order to be checked
        :returns: Returns true if the order has expired, false otherwise.
        """
        ...


class OrderProperties(System.Object, QuantConnect.Interfaces.IOrderProperties):
    """Contains additional properties and settings for an order"""

    @property
    def time_in_force(self) -> QuantConnect.Orders.TimeInForce:
        """Defines the length of time over which an order will continue working before it is cancelled"""
        ...

    @property.setter
    def time_in_force(self, value: QuantConnect.Orders.TimeInForce) -> None:
        ...

    @property
    def exchange(self) -> QuantConnect.Exchange:
        """Defines the exchange name for a particular market"""
        ...

    @property.setter
    def exchange(self, value: QuantConnect.Exchange) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the OrderProperties class"""
        ...

    @overload
    def __init__(self, exchange: QuantConnect.Exchange) -> None:
        """
        Initializes a new instance of the OrderProperties class, with exchange param
        Exchange name for market
        
        :param exchange: Exchange name for market
        """
        ...

    def clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Returns a new instance clone of this object"""
        ...


class EzeOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to EZE brokerage"""

    @property
    def route(self) -> str:
        """Route name as shown in Eze EMS."""
        ...

    @property.setter
    def route(self, value: str) -> None:
        ...

    @property
    def account(self) -> str:
        """
        Semi-colon separated values that represent either Trade or Neutral accounts the user has permission
        e.g.,TAL;TEST;USER1;TRADE or TAL;TEST;USER2;NEUTRAL
        """
        ...

    @property.setter
    def account(self, value: str) -> None:
        ...

    @property
    def notes(self) -> str:
        """User message/notes"""
        ...

    @property.setter
    def notes(self, value: str) -> None:
        ...

    def __init__(self, route: str, account: str, exchange: QuantConnect.Exchange, notes: str = ...) -> None:
        """
        Initializes a new instance of the EzeOrderProperties class
        
        :param route: Trading route name
        :param account: Trading account with specific permission
        :param exchange: Exchange name
        :param notes: Some notes about order
        """
        ...


class OrderType(Enum):
    """Type of the order: market, limit or stop"""

    MARKET = 0
    """Market Order Type (0)"""

    LIMIT = 1
    """Limit Order Type (1)"""

    STOP_MARKET = 2
    """Stop Market Order Type - Fill at market price when break target price (2)"""

    STOP_LIMIT = 3
    """Stop limit order type - trigger fill once pass the stop price; but limit fill to limit price (3)"""

    MARKET_ON_OPEN = 4
    """Market on open type - executed on exchange open (4)"""

    MARKET_ON_CLOSE = 5
    """Market on close type - executed on exchange close (5)"""

    OPTION_EXERCISE = 6
    """Option Exercise Order Type (6)"""

    LIMIT_IF_TOUCHED = 7
    """Limit if Touched Order Type - a limit order to be placed after first reaching a trigger value (7)"""

    COMBO_MARKET = 8
    """Combo Market Order Type - (8)"""

    COMBO_LIMIT = 9
    """Combo Limit Order Type - (9)"""

    COMBO_LEG_LIMIT = 10
    """Combo Leg Limit Order Type - (10)"""

    TRAILING_STOP = 11
    """Trailing Stop Order Type - (11)"""


class OrderSubmissionData(System.Object):
    """
    The purpose of this class is to store time and price information
    available at the time an order was submitted.
    """

    @property
    def bid_price(self) -> float:
        """The bid price at order submission time"""
        ...

    @property
    def ask_price(self) -> float:
        """The ask price at order submission time"""
        ...

    @property
    def last_price(self) -> float:
        """The current price at order submission time"""
        ...

    def __init__(self, bidPrice: float, askPrice: float, lastPrice: float) -> None:
        """Initializes a new instance of the OrderSubmissionData class"""
        ...

    def clone(self) -> QuantConnect.Orders.OrderSubmissionData:
        """Return a new instance clone of this object"""
        ...


class OrderRequestType(Enum):
    """Specifies the type of OrderRequest"""

    SUBMIT = 0
    """The request is a SubmitOrderRequest (0)"""

    UPDATE = 1
    """The request is a UpdateOrderRequest (1)"""

    CANCEL = 2
    """The request is a CancelOrderRequest (2)"""


class OrderRequestStatus(Enum):
    """Specifies the status of a request"""

    UNPROCESSED = 0
    """This is an unprocessed request (0)"""

    PROCESSING = 1
    """This request is partially processed (1)"""

    PROCESSED = 2
    """This request has been completely processed (2)"""

    ERROR = 3
    """This request encountered an error (3)"""


class OrderResponseErrorCode(Enum):
    """Error detail code"""

    NONE = 0
    """No error (0)"""

    PROCESSING_ERROR = -1
    """Unknown error (-1)"""

    ORDER_ALREADY_EXISTS = -2
    """Cannot submit because order already exists (-2)"""

    INSUFFICIENT_BUYING_POWER = -3
    """Not enough money to to submit order (-3)"""

    BROKERAGE_MODEL_REFUSED_TO_SUBMIT_ORDER = -4
    """Internal logic invalidated submit order (-4)"""

    BROKERAGE_FAILED_TO_SUBMIT_ORDER = -5
    """Brokerage submit error (-5)"""

    BROKERAGE_FAILED_TO_UPDATE_ORDER = -6
    """Brokerage update error (-6)"""

    BROKERAGE_HANDLER_REFUSED_TO_UPDATE_ORDER = -7
    """Internal logic invalidated update order (-7)"""

    BROKERAGE_FAILED_TO_CANCEL_ORDER = -8
    """Brokerage cancel error (-8)"""

    INVALID_ORDER_STATUS = -9
    """Only pending orders can be canceled (-9)"""

    UNABLE_TO_FIND_ORDER = -10
    """Missing order (-10)"""

    ORDER_QUANTITY_ZERO = -11
    """Cannot submit or update orders with zero quantity (-11)"""

    UNSUPPORTED_REQUEST_TYPE = -12
    """This type of request is unsupported (-12)"""

    PRE_ORDER_CHECKS_ERROR = -13
    """Unknown error during pre order request validation (-13)"""

    MISSING_SECURITY = -14
    """Security is missing. Probably did not subscribe (-14)"""

    EXCHANGE_NOT_OPEN = -15
    """Some order types require open exchange (-15)"""

    SECURITY_PRICE_ZERO = -16
    """Zero security price is probably due to bad data (-16)"""

    FOREX_BASE_AND_QUOTE_CURRENCIES_REQUIRED = -17
    """Need both currencies in cashbook to trade a pair (-17)"""

    FOREX_CONVERSION_RATE_ZERO = -18
    """Need conversion rate to account currency (-18)"""

    SECURITY_HAS_NO_DATA = -19
    """Should not attempt trading without at least one data point (-19)"""

    EXCEEDED_MAXIMUM_ORDERS = -20
    """Transaction manager's cache is full (-20)"""

    MARKET_ON_CLOSE_ORDER_TOO_LATE = -21
    """Below buffer time for MOC order to be placed before exchange closes. 15.5 minutes by default (-21)"""

    INVALID_REQUEST = -22
    """Request is invalid or null (-22)"""

    REQUEST_CANCELED = -23
    """Request was canceled by user (-23)"""

    ALGORITHM_WARMING_UP = -24
    """All orders are invalidated while algorithm is warming up (-24)"""

    BROKERAGE_MODEL_REFUSED_TO_UPDATE_ORDER = -25
    """Internal logic invalidated update order (-25)"""

    QUOTE_CURRENCY_REQUIRED = -26
    """Need quote currency in cashbook to trade (-26)"""

    CONVERSION_RATE_ZERO = -27
    """Need conversion rate to account currency (-27)"""

    NON_TRADABLE_SECURITY = -28
    """The order's symbol references a non-tradable security (-28)"""

    NON_EXERCISABLE_SECURITY = -29
    """The order's symbol references a non-exercisable security (-29)"""

    ORDER_QUANTITY_LESS_THAN_LOT_SIZE = -30
    """Cannot submit or update orders with quantity that is less than lot size (-30)"""

    EXCEEDS_SHORTABLE_QUANTITY = -31
    """The order's quantity exceeds the max shortable quantity set by the brokerage (-31)"""

    INVALID_NEW_ORDER_STATUS = -32
    """Cannot update/cancel orders with OrderStatus.New (-32)"""

    EUROPEAN_OPTION_NOT_EXPIRED_ON_EXERCISE = -33
    """Exercise time before expiry for European options (-33)"""

    OPTION_ORDER_ON_STOCK_SPLIT = -34
    """Option order is invalid due to underlying stock split (-34)"""


class OrderResponse(System.Object):
    """
    Represents a response to an OrderRequest. See OrderRequest.Response property for
    a specific request's response value
    """

    @property
    def order_id(self) -> int:
        """Gets the order id"""
        ...

    @property
    def error_message(self) -> str:
        """
        Gets the error message if the ErrorCode does not equal OrderResponseErrorCode.None, otherwise
        gets string.Empty
        """
        ...

    @property
    def error_code(self) -> QuantConnect.Orders.OrderResponseErrorCode:
        """Gets the error code for this response."""
        ...

    @property
    def is_success(self) -> bool:
        """
        Gets true if this response represents a successful request, false otherwise
        If this is an unprocessed response, IsSuccess will return false.
        """
        ...

    @property
    def is_error(self) -> bool:
        """Gets true if this response represents an error, false otherwise"""
        ...

    @property
    def is_processed(self) -> bool:
        """Gets true if this response has been processed, false otherwise"""
        ...

    UNPROCESSED: QuantConnect.Orders.OrderResponse = ...
    """Gets an OrderResponse for a request that has not yet been processed"""

    @staticmethod
    def error(request: QuantConnect.Orders.OrderRequest, error_code: QuantConnect.Orders.OrderResponseErrorCode, error_message: str) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create an error response from a request"""
        ...

    @staticmethod
    def invalid_new_status(request: QuantConnect.Orders.OrderRequest, order: QuantConnect.Orders.Order) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create an error response due to the "New" order status"""
        ...

    @staticmethod
    def invalid_status(request: QuantConnect.Orders.OrderRequest, order: QuantConnect.Orders.Order) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create an error response due to an invalid order status"""
        ...

    @staticmethod
    def missing_security(request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create an error response due to a missing security"""
        ...

    @staticmethod
    def success(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create a successful response from a request"""
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    @staticmethod
    def unable_to_find_order(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create an error response due to a bad order id"""
        ...

    @staticmethod
    def warming_up(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create an error response due to algorithm still in warmup mode"""
        ...

    @staticmethod
    def zero_quantity(request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderResponse:
        """Helper method to create an error response due to a zero order quantity"""
        ...


class OrderRequest(System.Object, metaclass=abc.ABCMeta):
    """Represents a request to submit, update, or cancel an order"""

    @property
    @abc.abstractmethod
    def order_request_type(self) -> QuantConnect.Orders.OrderRequestType:
        """Gets the type of this order request"""
        ...

    @property
    def status(self) -> QuantConnect.Orders.OrderRequestStatus:
        """Gets the status of this request"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Gets the UTC time the request was created"""
        ...

    @property
    def order_id(self) -> int:
        """Gets the order id the request acts on"""
        ...

    @property
    def tag(self) -> str:
        """Gets a tag for this request"""
        ...

    @property
    def response(self) -> QuantConnect.Orders.OrderResponse:
        """
        Gets the response for this request. If this request was never processed then this
        will equal OrderResponse.Unprocessed. This value is never equal to null.
        """
        ...

    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], orderId: int, tag: str) -> None:
        """
        Initializes a new instance of the OrderRequest class
        
        This method is protected.
        
        :param time: The time this request was created
        :param orderId: The order id this request acts on, specify zero for SubmitOrderRequest
        :param tag: A custom tag for the request
        """
        ...

    def set_response(self, response: QuantConnect.Orders.OrderResponse, status: QuantConnect.Orders.OrderRequestStatus = ...) -> None:
        """
        Sets the Response for this request
        
        :param response: The response to this request
        :param status: The current status of this request
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class UpdateOrderFields(System.Object):
    """Specifies the data in an order to be updated"""

    @property
    def quantity(self) -> typing.Optional[float]:
        """Specify to update the quantity of the order"""
        ...

    @property.setter
    def quantity(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def limit_price(self) -> typing.Optional[float]:
        """Specify to update the limit price of the order"""
        ...

    @property.setter
    def limit_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def stop_price(self) -> typing.Optional[float]:
        """Specify to update the stop price of the order"""
        ...

    @property.setter
    def stop_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trigger_price(self) -> typing.Optional[float]:
        """Specify to update the trigger price of the order"""
        ...

    @property.setter
    def trigger_price(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trailing_amount(self) -> typing.Optional[float]:
        """The trailing stop order trailing amount"""
        ...

    @property.setter
    def trailing_amount(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def tag(self) -> str:
        """Specify to update the order's tag"""
        ...

    @property.setter
    def tag(self, value: str) -> None:
        ...


class UpdateOrderRequest(QuantConnect.Orders.OrderRequest):
    """Defines a request to update an order's values"""

    @property
    def order_request_type(self) -> QuantConnect.Orders.OrderRequestType:
        """Gets Orders.OrderRequestType.Update"""
        ...

    @property
    def quantity(self) -> typing.Optional[float]:
        """Gets the new quantity of the order, null to not change the quantity"""
        ...

    @property
    def limit_price(self) -> typing.Optional[float]:
        """Gets the new limit price of the order, null to not change the limit price"""
        ...

    @property
    def stop_price(self) -> typing.Optional[float]:
        """Gets the new stop price of the order, null to not change the stop price"""
        ...

    @property
    def trigger_price(self) -> typing.Optional[float]:
        """Gets the new trigger price of the order, null to not change the trigger price"""
        ...

    @property
    def trailing_amount(self) -> typing.Optional[float]:
        """The trailing stop order trailing amount"""
        ...

    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], orderId: int, fields: QuantConnect.Orders.UpdateOrderFields) -> None:
        """
        Initializes a new instance of the UpdateOrderRequest class
        
        :param time: The time the request was submitted
        :param orderId: The order id to be updated
        :param fields: The fields defining what should be updated
        """
        ...

    def is_allowed_for_closed_order(self) -> bool:
        """
        Checks whether the update request is allowed for a closed order.
        Only tag updates are allowed on closed orders.
        
        :returns: True if the update request is allowed for a closed order.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class SubmitOrderRequest(QuantConnect.Orders.OrderRequest):
    """Defines a request to submit a new order"""

    @property
    def order_request_type(self) -> QuantConnect.Orders.OrderRequestType:
        """Gets Orders.OrderRequestType.Submit"""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets the security type of the symbol"""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol to be traded"""
        ...

    @property
    def order_type(self) -> QuantConnect.Orders.OrderType:
        """Gets the order type od the order"""
        ...

    @property
    def quantity(self) -> float:
        """Gets the quantity of the order"""
        ...

    @property
    def limit_price(self) -> float:
        """Gets the limit price of the order, zero if not a limit order"""
        ...

    @property
    def stop_price(self) -> float:
        """Gets the stop price of the order, zero if not a stop order"""
        ...

    @property
    def trigger_price(self) -> float:
        """Price which must first be reached before a limit order can be submitted."""
        ...

    @property
    def trailing_amount(self) -> float:
        """Trailing amount for a trailing stop order"""
        ...

    @property
    def trailing_as_percentage(self) -> bool:
        """Determines whether the TrailingAmount is a percentage or an absolute currency value"""
        ...

    @property
    def order_properties(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Gets the order properties for this request"""
        ...

    @property
    def group_order_manager(self) -> QuantConnect.Orders.GroupOrderManager:
        """Gets the manager for the combo order. If null, the order is not a combo order."""
        ...

    @overload
    def __init__(self, orderType: QuantConnect.Orders.OrderType, securityType: QuantConnect.SecurityType, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stopPrice: float, limitPrice: float, triggerPrice: float, trailingAmount: float, trailingAsPercentage: bool, time: typing.Union[datetime.datetime, datetime.date], tag: str, properties: QuantConnect.Interfaces.IOrderProperties = None, groupOrderManager: QuantConnect.Orders.GroupOrderManager = None) -> None:
        """
        Initializes a new instance of the SubmitOrderRequest class.
        The OrderRequest.OrderId will default to OrderResponseErrorCode.UnableToFindOrder
        
        :param orderType: The order type to be submitted
        :param securityType: The symbol's SecurityType
        :param symbol: The symbol to be traded
        :param quantity: The number of units to be ordered
        :param stopPrice: The stop price for stop orders, non-stop orders this value is ignored
        :param limitPrice: The limit price for limit orders, non-limit orders this value is ignored
        :param triggerPrice: The trigger price for limit if touched orders, for non-limit if touched orders this value is ignored
        :param trailingAmount: The trailing amount to be used to update the stop price
        :param trailingAsPercentage: Whether the  is a percentage or an absolute currency value
        :param time: The time this request was created
        :param tag: A custom tag for this request
        :param properties: The order properties for this request
        :param groupOrderManager: The manager for this combo order
        """
        ...

    @overload
    def __init__(self, orderType: QuantConnect.Orders.OrderType, securityType: QuantConnect.SecurityType, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stopPrice: float, limitPrice: float, triggerPrice: float, time: typing.Union[datetime.datetime, datetime.date], tag: str, properties: QuantConnect.Interfaces.IOrderProperties = None, groupOrderManager: QuantConnect.Orders.GroupOrderManager = None) -> None:
        """
        Initializes a new instance of the SubmitOrderRequest class.
        The OrderRequest.OrderId will default to OrderResponseErrorCode.UnableToFindOrder
        
        :param orderType: The order type to be submitted
        :param securityType: The symbol's SecurityType
        :param symbol: The symbol to be traded
        :param quantity: The number of units to be ordered
        :param stopPrice: The stop price for stop orders, non-stop orders this value is ignored
        :param limitPrice: The limit price for limit orders, non-limit orders this value is ignored
        :param triggerPrice: The trigger price for limit if touched orders, for non-limit if touched orders this value is ignored
        :param time: The time this request was created
        :param tag: A custom tag for this request
        :param properties: The order properties for this request
        :param groupOrderManager: The manager for this combo order
        """
        ...

    @overload
    def __init__(self, orderType: QuantConnect.Orders.OrderType, securityType: QuantConnect.SecurityType, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stopPrice: float, limitPrice: float, time: typing.Union[datetime.datetime, datetime.date], tag: str, properties: QuantConnect.Interfaces.IOrderProperties = None, groupOrderManager: QuantConnect.Orders.GroupOrderManager = None) -> None:
        """
        Initializes a new instance of the SubmitOrderRequest class.
        The OrderRequest.OrderId will default to OrderResponseErrorCode.UnableToFindOrder
        
        :param orderType: The order type to be submitted
        :param securityType: The symbol's SecurityType
        :param symbol: The symbol to be traded
        :param quantity: The number of units to be ordered
        :param stopPrice: The stop price for stop orders, non-stop orders this value is ignored
        :param limitPrice: The limit price for limit orders, non-limit orders this value is ignored
        :param time: The time this request was created
        :param tag: A custom tag for this request
        :param properties: The order properties for this request
        :param groupOrderManager: The manager for this combo order
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class Order(System.Object, metaclass=abc.ABCMeta):
    """Order struct for placing new trade"""

    @property
    def id(self) -> int:
        """Order ID."""
        ...

    @property
    def contingent_id(self) -> int:
        """Order id to process before processing this order."""
        ...

    @property
    def broker_id(self) -> System.Collections.Generic.List[str]:
        """Brokerage Id for this order for when the brokerage splits orders into multiple pieces"""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol of the Asset"""
        ...

    @property
    def price(self) -> float:
        """Price of the Order."""
        ...

    @property
    def price_currency(self) -> str:
        """Currency for the order price"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Gets the utc time the order was created."""
        ...

    @property
    def created_time(self) -> datetime.datetime:
        """Gets the utc time this order was created. Alias for Time"""
        ...

    @property
    def last_fill_time(self) -> typing.Optional[datetime.datetime]:
        """Gets the utc time the last fill was received, or null if no fills have been received"""
        ...

    @property
    def last_update_time(self) -> typing.Optional[datetime.datetime]:
        """Gets the utc time this order was last updated, or null if the order has not been updated."""
        ...

    @property
    def canceled_time(self) -> typing.Optional[datetime.datetime]:
        """Gets the utc time this order was canceled, or null if the order was not canceled."""
        ...

    @property
    def quantity(self) -> float:
        """Number of shares to execute."""
        ...

    @property
    @abc.abstractmethod
    def type(self) -> QuantConnect.Orders.OrderType:
        """Order Type"""
        ...

    @property
    def status(self) -> QuantConnect.Orders.OrderStatus:
        """Status of the Order"""
        ...

    @property.setter
    def status(self, value: QuantConnect.Orders.OrderStatus) -> None:
        ...

    @property
    def time_in_force(self) -> QuantConnect.Orders.TimeInForce:
        """Order Time In Force"""
        ...

    @property
    def tag(self) -> str:
        """Tag the order with some custom data"""
        ...

    @property
    def properties(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Additional properties of the order"""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """The symbol's security type"""
        ...

    @property
    def direction(self) -> QuantConnect.Orders.OrderDirection:
        """Order Direction Property based off Quantity."""
        ...

    @property
    def absolute_quantity(self) -> float:
        """Get the absolute quantity for this order"""
        ...

    @property
    def value(self) -> float:
        """
        Deprecated
        
        Please use Order.GetValue(security) or security.Holdings.HoldingsValue
        """
        warnings.warn("Please use Order.GetValue(security) or security.Holdings.HoldingsValue", DeprecationWarning)

    @property
    def order_submission_data(self) -> QuantConnect.Orders.OrderSubmissionData:
        """Gets the price data at the time the order was submitted"""
        ...

    @property
    def is_marketable(self) -> bool:
        """Returns true if the order is a marketable order."""
        ...

    @property
    def group_order_manager(self) -> QuantConnect.Orders.GroupOrderManager:
        """Manager for the orders in the group if this is a combo order"""
        ...

    @property.setter
    def group_order_manager(self, value: QuantConnect.Orders.GroupOrderManager) -> None:
        ...

    @property
    def price_adjustment_mode(self) -> QuantConnect.DataNormalizationMode:
        """The adjustment mode used on the order fill price"""
        ...

    @property.setter
    def price_adjustment_mode(self, value: QuantConnect.DataNormalizationMode) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Added a default constructor for JSON Deserialization:
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], groupOrderManager: QuantConnect.Orders.GroupOrderManager, tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New order constructor
        
        This method is protected.
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param time: Time the order was placed
        :param groupOrderManager: Manager for the orders in the group if this is a combo order
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New order constructor
        
        This method is protected.
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def copy_to(self, order: QuantConnect.Orders.Order) -> None:
        """
        Copies base Order properties to the specified order
        
        This method is protected.
        
        :param order: The target of the copy
        """
        ...

    @staticmethod
    def create_order(request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.Order:
        """
        Creates an Order to match the specified
        
        :param request: The SubmitOrderRequest to create an order for
        :returns: The Order that matches the request.
        """
        ...

    def create_positions(self, securities: QuantConnect.Securities.SecurityManager) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]:
        """
        Creates an enumerable containing each position resulting from executing this order.
        
        :returns: An enumerable of positions matching the results of executing this order.
        """
        ...

    def get_default_tag(self) -> str:
        """
        Gets the default tag for this order
        
        :returns: The default tag.
        """
        ...

    def get_value(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the value of this order at the given market price in units of the account currency
        NOTE: Some order types derive value from other parameters, such as limit prices
        
        :param security: The security matching this order's symbol
        :returns: The value of this order given the current market price.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency for a single unit.
        A single unit here is a single share of stock, or a single barrel of oil, or the
        cost of a single share in an option contract.
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class ComboOrder(QuantConnect.Orders.Order, metaclass=abc.ABCMeta):
    """Combo order type"""

    @property
    def quantity(self) -> float:
        """
        Number of shares to execute.
        For combo orders, we store the ratio of each leg instead of the quantity,
        and the actual quantity is calculated when requested using the group order manager quantity.
        This allows for a single quantity update to be applied to all the legs of the combo.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Added a default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], groupOrderManager: QuantConnect.Orders.GroupOrderManager, tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New market order constructor
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param time: Time the order was placed
        :param groupOrderManager: Manager for the orders in the group
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...


class ComboLimitOrder(QuantConnect.Orders.ComboOrder):
    """Combo limit order type"""

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """Combo Limit Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Added a default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, limitPrice: float, time: typing.Union[datetime.datetime, datetime.date], groupOrderManager: QuantConnect.Orders.GroupOrderManager, tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New limit order constructor
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param limitPrice: Price the order should be filled at if a limit order
        :param time: Time the order was placed
        :param groupOrderManager: Manager for the orders in the group
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...


class StopMarketOrder(QuantConnect.Orders.Order):
    """Stop Market Order Type Definition"""

    @property
    def stop_price(self) -> float:
        """Stop price for this stop market order."""
        ...

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """StopMarket Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stopPrice: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New Stop Market Order constructor -
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param stopPrice: Price the order should be filled at if a limit order
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_default_tag(self) -> str:
        """
        Gets the default tag for this order
        
        :returns: The default tag.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class TrailingStopOrder(QuantConnect.Orders.StopMarketOrder):
    """Trailing Stop Order Type Definition"""

    @property
    def trailing_amount(self) -> float:
        """Trailing amount for this trailing stop order"""
        ...

    @property
    def trailing_as_percentage(self) -> bool:
        """Determines whether the TrailingAmount is a percentage or an absolute currency value"""
        ...

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """StopLimit Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stopPrice: float, trailingAmount: float, trailingAsPercentage: bool, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New Trailing Stop Market Order constructor
        
        :param symbol: Symbol asset being traded
        :param quantity: Quantity of the asset to be traded
        :param stopPrice: Initial stop price at which the order should be triggered
        :param trailingAmount: The trailing amount to be used to update the stop price
        :param trailingAsPercentage: Whether the  is a percentage or an absolute currency value
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The properties for this order
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, trailingAmount: float, trailingAsPercentage: bool, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New Trailing Stop Market Order constructor.
        It creates a new Trailing Stop Market Order with an initial stop price calculated by subtracting (for a sell) or adding (for a buy) the
        trailing amount to the current market price.
        
        :param symbol: Symbol asset being traded
        :param quantity: Quantity of the asset to be traded
        :param trailingAmount: The trailing amount to be used to update the stop price
        :param trailingAsPercentage: Whether the  is a percentage or an absolute currency value
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    @staticmethod
    def calculate_stop_price(current_market_price: float, trailing_amount: float, trailing_as_percentage: bool, direction: QuantConnect.Orders.OrderDirection) -> float:
        """
        Calculates the stop price for a trailing stop order given the current market price
        
        :param current_market_price: The current market price
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param direction: The order direction
        :returns: The stop price for the order given the current market price.
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_default_tag(self) -> str:
        """
        Gets the default tag for this order
        
        :returns: The default tag.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    @staticmethod
    def try_update_stop_price(current_market_price: float, current_stop_price: float, trailing_amount: float, trailing_as_percentage: bool, direction: QuantConnect.Orders.OrderDirection, updated_stop_price: typing.Optional[float]) -> typing.Union[bool, float]:
        """
        Tries to update the stop price for a trailing stop order given the current market price
        
        :param current_market_price: The current market price
        :param current_stop_price: The current trailing stop order stop price
        :param trailing_amount: The trailing amount to be used to update the stop price
        :param trailing_as_percentage: Whether the  is a percentage or an absolute currency value
        :param direction: The order direction
        :param updated_stop_price: The updated stop price
        :returns: Whether the stop price was updated. This only happens when the distance between the current stop price and the current market price is greater than the trailing amount, which will happen when the market price raises/falls for sell/buy orders respectively.
        """
        ...


class OrderError(Enum):
    """Specifies the possible error states during presubmission checks"""

    CAN_NOT_UPDATE_FILLED_ORDER = -8
    """Order has already been filled and cannot be modified (-8)"""

    GENERAL_ERROR = -7
    """General error in order (-7)"""

    TIMESTAMP_ERROR = -6
    """Order timestamp error. Order appears to be executing in the future (-6)"""

    MAX_ORDERS_EXCEEDED = -5
    """Exceeded maximum allowed orders for one analysis period (-5)"""

    INSUFFICIENT_CAPITAL = -4
    """Insufficient capital to execute order (-4)"""

    MARKET_CLOSED = -3
    """Attempting market order outside of market hours (-3)"""

    NO_DATA = -2
    """There is no data yet for this security - please wait for data (market order price not available yet) (-2)"""

    ZERO_QUANTITY = -1
    """Order quantity must not be zero (-1)"""

    NONE = 0
    """The order is OK (0)"""


class BybitOrderProperties(QuantConnect.Orders.OrderProperties):
    """Class containing Bybit OrderProperties"""

    @property
    def post_only(self) -> bool:
        """
        This flag will ensure the order executes only as a maker (no fee) order.
        If part of the order results in taking liquidity rather than providing,
        it will be rejected and no part of the order will execute.
        Note: this flag is only applied to Limit orders.
        """
        ...

    @property.setter
    def post_only(self, value: bool) -> None:
        ...

    @property
    def reduce_only(self) -> typing.Optional[bool]:
        """This flag will ensure your position can only reduce in size if the order is triggered."""
        ...

    @property.setter
    def reduce_only(self, value: typing.Optional[bool]) -> None:
        ...


class StopLimitOrder(QuantConnect.Orders.Order):
    """Stop Market Order Type Definition"""

    @property
    def stop_price(self) -> float:
        """Stop price for this stop market order."""
        ...

    @property
    def stop_triggered(self) -> bool:
        """Signal showing the "StopLimitOrder" has been converted into a Limit Order"""
        ...

    @property
    def limit_price(self) -> float:
        """Limit price for the stop limit order"""
        ...

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """StopLimit Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, stopPrice: float, limitPrice: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New Stop Market Order constructor -
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param stopPrice: Price the order should be filled at if a limit order
        :param limitPrice: Maximum price to fill the order
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_default_tag(self) -> str:
        """
        Gets the default tag for this order
        
        :returns: The default tag.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class WolverineOrderProperties(QuantConnect.Orders.OrderProperties):
    """Wolverine order properties"""

    @property
    def exchange_post_fix(self) -> str:
        """The exchange post fix to apply if any"""
        ...

    @property.setter
    def exchange_post_fix(self, value: str) -> None:
        ...


class MarketOrder(QuantConnect.Orders.Order):
    """Market order type definition"""

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """Market Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Added a default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], price: float, tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New market order constructor
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param time: Time the order was placed
        :param price: Price of the order
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New market order constructor
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...


class FixOrderProperites(QuantConnect.Orders.OrderProperties):
    """FIX (Financial Information Exchange) order properties"""

    @property
    def handle_instruction(self) -> typing.Optional[str]:
        """Instruction for order handling on Broker floor"""
        ...

    @property.setter
    def handle_instruction(self, value: typing.Optional[str]) -> None:
        ...

    @property
    def notes(self) -> str:
        """Free format text string"""
        ...

    @property.setter
    def notes(self, value: str) -> None:
        ...

    AUTOMATED_EXECUTION_ORDER_PRIVATE: str = ...
    """Automated execution order, private, no broker intervention"""

    AUTOMATED_EXECUTION_ORDER_PUBLIC: str = ...
    """Automated execution order, public, broker, intervention OK"""

    MANUAL_ORDER: str = ...
    """Staged order, broker intervention required"""


class TradingTechnologiesOrderProperties(QuantConnect.Orders.FixOrderProperites):
    """Trading Technologies order properties"""


class CancelOrderRequest(QuantConnect.Orders.OrderRequest):
    """Defines a request to cancel an order"""

    @property
    def order_request_type(self) -> QuantConnect.Orders.OrderRequestType:
        """Gets Orders.OrderRequestType.Cancel"""
        ...

    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], orderId: int, tag: str) -> None:
        """
        Initializes a new instance of the CancelOrderRequest class
        
        :param time: The time this cancelation was requested
        :param orderId: The order id to be canceled
        :param tag: A new tag for the order
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class TDAmeritradeOrderProperties(QuantConnect.Orders.OrderProperties):
    """TDAmeritrade order properties"""


class OrderJsonConverter(JsonConverter):
    """Provides an implementation of JsonConverter that can deserialize Orders"""

    @property
    def can_write(self) -> bool:
        """Gets a value indicating whether this Newtonsoft.Json.JsonConverter can write JSON."""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    @staticmethod
    def create_order_from_j_object(j_object: typing.Any) -> QuantConnect.Orders.Order:
        """
        Create an order from a simple JObject
        
        :returns: Order Object.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class ReadOrdersResponseJsonConverter(JsonConverter):
    """Api orders read response json converter"""

    def can_convert(self, object_type: typing.Type) -> bool:
        """Determines if can convert the given open type"""
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """Deserialize the given api order response"""
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Serialize the given api order response"""
        ...


class IndiaOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to Indian Brokerages"""

    class IndiaProductType(Enum):
        """Define the India Order type that we are targeting (MIS/CNC/NRML)."""

        MIS = 0
        """Margin Intraday Square Off (0)"""

        CNC = 1
        """Cash and Carry (1)"""

        NRML = 2
        """Normal (2)"""

    @property
    def product_type(self) -> str:
        """India product type"""
        ...

    @overload
    def __init__(self, exchange: QuantConnect.Exchange) -> None:
        """
        Initialize a new OrderProperties for IndiaOrderProperties
        
        :param exchange: Exchange value, nse/bse etc
        """
        ...

    @overload
    def __init__(self, exchange: QuantConnect.Exchange, productType: QuantConnect.Orders.IndiaOrderProperties.IndiaProductType) -> None:
        """
        Initialize a new OrderProperties for IndiaOrderProperties
        
        :param exchange: Exchange value, nse/bse etc
        :param productType: ProductType value, MIS/CNC/NRML etc
        """
        ...

    def clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Returns a new instance clone of this object"""
        ...


class ComboMarketOrder(QuantConnect.Orders.ComboOrder):
    """Combo market order type"""

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """Combo Market Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Added a default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], groupOrderManager: QuantConnect.Orders.GroupOrderManager, tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New market order constructor
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param time: Time the order was placed
        :param groupOrderManager: Manager for the orders in the group
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...


class OrderUpdateEvent(System.Object):
    """
    Event that fires each time an order is updated in the brokerage side.
    These are not status changes but mainly price changes, like the stop price of a trailing stop order.
    """

    @property
    def order_id(self) -> int:
        """The order ID."""
        ...

    @property.setter
    def order_id(self, value: int) -> None:
        ...

    @property
    def trailing_stop_price(self) -> float:
        """The updated stop price for a TrailingStopOrder"""
        ...

    @property.setter
    def trailing_stop_price(self, value: float) -> None:
        ...

    @property
    def stop_triggered(self) -> bool:
        """Flag indicating whether stop has been triggered for a StopLimitOrder"""
        ...

    @property.setter
    def stop_triggered(self, value: bool) -> None:
        ...


class OrderPosition(Enum):
    """Position of the order"""

    BUY_TO_OPEN = 0
    """Indicates the buy order will result in a long position, starting either from zero or an existing long position (0)"""

    BUY_TO_CLOSE = 1
    """Indicates the buy order is starting from an existing short position, resulting in a closed or long position (1)"""

    SELL_TO_OPEN = 2
    """Indicates the sell order will result in a short position, starting either from zero or an existing short position (2)"""

    SELL_TO_CLOSE = 3
    """Indicates the sell order is starting from an existing long position, resulting in a closed or short position (3)"""


class BitfinexOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to Bitfinex brokerage"""

    @property
    def post_only(self) -> bool:
        """
        This flag will ensure the order executes only as a maker (no fee) order.
        If part of the order results in taking liquidity rather than providing,
        it will be rejected and no part of the order will execute.
        Note: this flag is only applied to Limit orders.
        """
        ...

    @property.setter
    def post_only(self, value: bool) -> None:
        ...

    @property
    def hidden(self) -> bool:
        """
        The hidden order option ensures an order does not appear in the order book; thus does not influence other market participants.
        If you place a hidden order, you will always pay the taker fee. If you place a limit order that hits a hidden order, you will always pay the maker fee.
        """
        ...

    @property.setter
    def hidden(self, value: bool) -> None:
        ...

    def clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Returns a new instance clone of this object"""
        ...


class FTXOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to FTX brokerage"""

    @property
    def post_only(self) -> bool:
        """
        This flag will ensure the order executes only as a maker (maker fee) order.
        If part of the order results in taking liquidity rather than providing,
        it will be rejected and no part of the order will execute.
        Note: this flag is only applied to Limit orders.
        """
        ...

    @property.setter
    def post_only(self, value: bool) -> None:
        ...

    @property
    def reduce_only(self) -> bool:
        """If you send a reduce only order, it will only trade if it would decrease your position size."""
        ...

    @property.setter
    def reduce_only(self, value: bool) -> None:
        ...

    def clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Returns a new instance clone of this object"""
        ...


class GroupOrderExtensions(System.Object):
    """Group (combo) orders extension methods for easiest combo order manipulation"""

    @staticmethod
    def get_error_message(securities: System.Collections.Generic.Dictionary[QuantConnect.Orders.Order, QuantConnect.Securities.Security], has_sufficient_buying_power_result: QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult) -> str:
        """
        Returns an error string message saying there is insufficient buying power for the given orders associated with their respective
        securities
        """
        ...

    @staticmethod
    def get_order_leg_group_quantity(leg_ratio: float, group_order_manager: QuantConnect.Orders.GroupOrderManager) -> float:
        """
        Gets the combo order leg group quantity, that is, the total number of shares to be bought/sold from this leg,
        from its ratio and the group order quantity
        
        :param leg_ratio: The leg ratio
        :param group_order_manager: The group order manager
        :returns: The total number of shares to be bought/sold from this leg.
        """
        ...

    @staticmethod
    def get_order_leg_ratio(leg_group_quantity: float, group_order_manager: QuantConnect.Orders.GroupOrderManager) -> float:
        """
        Gets the combo order leg ratio from its group quantity and the group order quantity
        
        :param leg_group_quantity: The total number of shares to be bought/sold from this leg, that is, the result of the let ratio times the group quantity
        :param group_order_manager: The group order manager
        :returns: The ratio of this combo order leg.
        """
        ...

    @staticmethod
    def try_get_group_orders(order: QuantConnect.Orders.Order, order_provider: typing.Callable[[int], QuantConnect.Orders.Order], orders: typing.Optional[System.Collections.Generic.List[QuantConnect.Orders.Order]]) -> typing.Union[bool, System.Collections.Generic.List[QuantConnect.Orders.Order]]:
        """
        Gets the grouped orders (legs) of a group order
        
        :param order: Target order, which can be any of the legs of the combo
        :param order_provider: Order provider to use to access the existing orders
        :param orders: List of orders in the combo
        :returns: False if any of the orders in the combo is not yet found in the order provider. True otherwise.
        """
        ...

    @staticmethod
    def try_get_group_orders_securities(orders: System.Collections.Generic.List[QuantConnect.Orders.Order], security_provider: QuantConnect.Securities.ISecurityProvider, securities: typing.Optional[System.Collections.Generic.Dictionary[QuantConnect.Orders.Order, QuantConnect.Securities.Security]]) -> typing.Union[bool, System.Collections.Generic.Dictionary[QuantConnect.Orders.Order, QuantConnect.Securities.Security]]:
        """
        Gets the securities corresponding to each order in the group
        
        :param orders: List of orders to map
        :param security_provider: The security provider to use
        :param securities: The resulting map of order to security
        :returns: True if the mapping is successful, false otherwise.
        """
        ...


class RBIOrderProperties(QuantConnect.Orders.OrderProperties):
    """RBI order properties"""


class LimitOrder(QuantConnect.Orders.Order):
    """Limit order type definition"""

    @property
    def limit_price(self) -> float:
        """Limit price for this order."""
        ...

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """Limit Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Added a default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, limitPrice: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New limit order constructor
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param limitPrice: Price the order should be filled at if a limit order
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_default_tag(self) -> str:
        """
        Gets the default tag for this order
        
        :returns: The default tag.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class CoinbaseOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to Coinbase brokerage"""

    @property
    def post_only(self) -> bool:
        """
        This flag will ensure the order executes only as a maker (no fee) order.
        If part of the order results in taking liquidity rather than providing,
        it will be rejected and no part of the order will execute.
        Note: this flag is only applied to Limit orders.
        """
        ...

    @property.setter
    def post_only(self, value: bool) -> None:
        ...

    @property
    def self_trade_prevention_id(self) -> bool:
        """
        Gets or sets a value indicating whether self-trade prevention is enabled for this order.
        Self-trade prevention helps prevent an order from crossing against the same user,
        reducing the risk of unintentional trades within the same account.
        """
        ...

    @property.setter
    def self_trade_prevention_id(self, value: bool) -> None:
        ...


class ApiOrderResponse(QuantConnect.Api.StringRepresentation):
    """Api order and order events reponse"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """The symbol associated with this order"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """The order"""
        ...

    @property.setter
    def order(self, value: QuantConnect.Orders.Order) -> None:
        ...

    @property
    def events(self) -> System.Collections.Generic.List[QuantConnect.Orders.Serialization.SerializedOrderEvent]:
        """The order events"""
        ...

    @property.setter
    def events(self, value: System.Collections.Generic.List[QuantConnect.Orders.Serialization.SerializedOrderEvent]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """ApiOrderResponse empty constructor"""
        ...

    @overload
    def __init__(self, order: QuantConnect.Orders.Order, events: System.Collections.Generic.List[QuantConnect.Orders.Serialization.SerializedOrderEvent], symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """Creates an instance of an ApiOrderResponse class using the given arguments"""
        ...


class OrdersResponseWrapper(QuantConnect.Api.RestResponse):
    """Collection container for a list of orders for a project"""

    @property
    def length(self) -> int:
        """Returns the total order collection length, not only the amount we are sending here"""
        ...

    @property.setter
    def length(self, value: int) -> None:
        ...

    @property
    def orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.ApiOrderResponse]:
        """Collection of summarized Orders objects"""
        ...

    @property.setter
    def orders(self, value: System.Collections.Generic.List[QuantConnect.Orders.ApiOrderResponse]) -> None:
        ...


class OrderSizing(System.Object):
    """Provides methods for computing a maximum order size."""

    @staticmethod
    def adjust_by_lot_size(security: QuantConnect.Securities.Security, quantity: float) -> float:
        """
        Adjusts the provided order quantity to respect the securities lot size.
        If the quantity is missing 1M part of the lot size it will be rounded up
        since we suppose it's due to floating point error, this is required to avoid diff
        between Py and C#
        
        :param security: The security instance
        :param quantity: The desired quantity to adjust, can be signed
        :returns: The signed adjusted quantity.
        """
        ...

    @staticmethod
    def get_order_size_for_maximum_value(security: QuantConnect.Securities.Security, maximum_order_value_in_account_currency: float, desired_order_size: float) -> float:
        """
        Adjust the provided order size to respect the maximum total order value
        
        :param security: The security object
        :param maximum_order_value_in_account_currency: The maximum order value in units of the account currency
        :param desired_order_size: The desired order size to adjust
        :returns: The signed adjusted order size.
        """
        ...

    @staticmethod
    def get_order_size_for_percent_volume(security: QuantConnect.Securities.Security, maximum_percent_current_volume: float, desired_order_size: float) -> float:
        """
        Adjust the provided order size to respect maximum order size based on a percentage of current volume.
        
        :param security: The security object
        :param maximum_percent_current_volume: The maximum percentage of the current bar's volume
        :param desired_order_size: The desired order size to adjust
        :returns: The signed adjusted order size.
        """
        ...

    @staticmethod
    @overload
    def get_unordered_quantity(algorithm: QuantConnect.Interfaces.IAlgorithm, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget) -> float:
        """
        Gets the remaining quantity to be ordered to reach the specified target quantity.
        
        :param algorithm: The algorithm instance
        :param target: The portfolio target
        :returns: The signed remaining quantity to be ordered.
        """
        ...

    @staticmethod
    @overload
    def get_unordered_quantity(algorithm: QuantConnect.Interfaces.IAlgorithm, target: QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget, security: QuantConnect.Securities.Security, account_for_fees: bool = False) -> float:
        """
        Gets the remaining quantity to be ordered to reach the specified target quantity.
        
        :param algorithm: The algorithm instance
        :param target: The portfolio target
        :param security: The target security
        :param account_for_fees: True for taking into account the fee's in the order quantity. False, otherwise.
        :returns: The signed remaining quantity to be ordered.
        """
        ...


class MarketOnOpenOrder(QuantConnect.Orders.Order):
    """Market on Open order type, submits a market order when the exchange opens"""

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """MarketOnOpen Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Intiializes a new instance of the MarketOnOpenOrder class."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        Intiializes a new instance of the MarketOnOpenOrder class.
        
        :param symbol: The security's symbol being ordered
        :param quantity: The number of units to order
        :param time: The current time
        :param tag: A user defined tag for the order
        :param properties: The order properties for this order
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...


class KrakenOrderProperties(QuantConnect.Orders.OrderProperties):
    """Kraken order properties"""

    @property
    def post_only(self) -> bool:
        """Post-only order (available when ordertype = limit)"""
        ...

    @property.setter
    def post_only(self, value: bool) -> None:
        ...

    @property
    def fee_in_base(self) -> bool:
        """If true or by default when selling, fees will be charged in base currency. If false will be ignored. Mutually exclusive with FeeInQuote."""
        ...

    @property.setter
    def fee_in_base(self, value: bool) -> None:
        ...

    @property
    def fee_in_quote(self) -> bool:
        """If true or by default when buying, fees will be charged in quote currency. If false will be ignored. Mutually exclusive with FeeInBase."""
        ...

    @property.setter
    def fee_in_quote(self, value: bool) -> None:
        ...

    @property
    def no_market_price_protection(self) -> bool:
        """https://support.kraken.com/hc/en-us/articles/201648183-Market-Price-Protection"""
        ...

    @property.setter
    def no_market_price_protection(self, value: bool) -> None:
        ...

    @property
    def conditional_order(self) -> QuantConnect.Orders.Order:
        """Conditional close orders are triggered by execution of the primary order in the same quantity and opposite direction. Ordertypes can be the same with primary order."""
        ...

    @property.setter
    def conditional_order(self, value: QuantConnect.Orders.Order) -> None:
        ...


class TradeStationOrderProperties(QuantConnect.Orders.OrderProperties):
    """Represents the properties of an order in TradeStation."""

    @property
    def all_or_none(self) -> bool:
        """
        Enables the "All or None" feature for your order, ensuring it will only be filled completely or not at all.
        Set to true to activate this feature, or false to allow partial fills.
        """
        ...

    @property.setter
    def all_or_none(self, value: bool) -> None:
        ...


class GroupOrderCacheManager(System.Object):
    """Provides a thread-safe service for caching and managing original orders when they are part of a group."""

    def try_get_group_cached_orders(self, order: QuantConnect.Orders.Order, orders: typing.Optional[System.Collections.Generic.List[QuantConnect.Orders.Order]]) -> typing.Union[bool, System.Collections.Generic.List[QuantConnect.Orders.Order]]:
        """
        Attempts to retrieve all the orders in the combo group from the cache.
        
        :param order: Target order, which can be any of the legs of the combo
        :param orders: List of orders in the combo
        :returns: true if all the orders in the combo group were successfully retrieved from the cache; otherwise, false. If the retrieval fails, the target order is cached for future retrieval.
        """
        ...


class BinanceOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to Binance brokerage"""

    @property
    def post_only(self) -> bool:
        """
        This flag will ensure the order executes only as a maker (no fee) order.
        If part of the order results in taking liquidity rather than providing,
        it will be rejected and no part of the order will execute.
        Note: this flag is only applied to Limit orders.
        """
        ...

    @property.setter
    def post_only(self, value: bool) -> None:
        ...

    def clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Returns a new instance clone of this object"""
        ...


class TimeInForceJsonConverter(JsonConverter):
    """Provides an implementation of JsonConverter that can deserialize TimeInForce objects"""

    @property
    def can_write(self) -> bool:
        """Gets a value indicating whether this Newtonsoft.Json.JsonConverter can write JSON."""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class OrderField(Enum):
    """Specifies an order field that does not apply to all order types"""

    LIMIT_PRICE = 0
    """The limit price for a LimitOrder, StopLimitOrder or LimitIfTouchedOrder (0)"""

    STOP_PRICE = 1
    """The stop price for stop orders (StopMarketOrder, StopLimitOrder) (1)"""

    TRIGGER_PRICE = 2
    """The trigger price for a LimitIfTouchedOrder (2)"""

    TRAILING_AMOUNT = 3
    """The trailing amount for a TrailingStopOrder (3)"""

    TRAILING_AS_PERCENTAGE = 4
    """Whether the trailing amount for a TrailingStopOrder is a percentage or an absolute currency value (4)"""


class OrderTicket(System.Object):
    """
    Provides a single reference to an order for the algorithm to maintain. As the order gets
    updated this ticket will also get updated
    """

    @property
    def order_id(self) -> int:
        """Gets the order id of this ticket"""
        ...

    @property
    def status(self) -> QuantConnect.Orders.OrderStatus:
        """Gets the current status of this order ticket"""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol being ordered"""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets the Symbol's SecurityType"""
        ...

    @property
    def quantity(self) -> float:
        """Gets the number of units ordered"""
        ...

    @property
    def average_fill_price(self) -> float:
        """
        Gets the average fill price for this ticket. If no fills have been processed
        then this will return a value of zero.
        """
        ...

    @property
    def quantity_filled(self) -> float:
        """
        Gets the total qantity filled for this ticket. If no fills have been processed
        then this will return a value of zero.
        """
        ...

    @property
    def time(self) -> datetime.datetime:
        """Gets the time this order was last updated"""
        ...

    @property
    def order_type(self) -> QuantConnect.Orders.OrderType:
        """Gets the type of order"""
        ...

    @property
    def tag(self) -> str:
        """Gets the order's current tag"""
        ...

    @property
    def submit_request(self) -> QuantConnect.Orders.SubmitOrderRequest:
        """Gets the SubmitOrderRequest that initiated this order"""
        ...

    @property
    def update_requests(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Orders.UpdateOrderRequest]:
        """
        Gets a list of UpdateOrderRequest containing an item for each
        UpdateOrderRequest that was sent for this order id
        """
        ...

    @property
    def cancel_request(self) -> QuantConnect.Orders.CancelOrderRequest:
        """
        Gets the CancelOrderRequest if this order was canceled. If this order
        was not canceled, this will return null
        """
        ...

    @property
    def order_events(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Orders.OrderEvent]:
        """Gets a list of all order events for this ticket"""
        ...

    @property
    def order_closed(self) -> System.Threading.WaitHandle:
        """Gets a wait handle that can be used to wait until this order has filled"""
        ...

    @property
    def has_order(self) -> bool:
        """Returns true if the order has been set for this ticket"""
        ...

    @property
    def order_set(self) -> System.Threading.WaitHandle:
        """Gets a wait handle that can be used to wait until the order has been set"""
        ...

    def __init__(self, transactionManager: QuantConnect.Securities.SecurityTransactionManager, submitRequest: QuantConnect.Orders.SubmitOrderRequest) -> None:
        """
        Initializes a new instance of the OrderTicket class
        
        :param transactionManager: The transaction manager used for submitting updates and cancels for this ticket
        :param submitRequest: The order request that initiated this order ticket
        """
        ...

    def cancel(self, tag: str = None) -> QuantConnect.Orders.OrderResponse:
        """Submits a new request to cancel this order"""
        ...

    @overload
    def get(self, field: QuantConnect.Orders.OrderField) -> float:
        """
        Gets the specified field from the ticket
        
        :param field: The order field to get
        :returns: The value of the field.
        """
        ...

    @overload
    def get(self, field: QuantConnect.Orders.OrderField) -> QuantConnect_Orders_OrderTicket_Get_T:
        """
        Gets the specified field from the ticket and tries to convert it to the specified type
        
        :param field: The order field to get
        :returns: The value of the field.
        """
        ...

    def get_most_recent_order_request(self) -> QuantConnect.Orders.OrderRequest:
        """
        Gets the most recent OrderRequest for this ticket
        
        :returns: The most recent OrderRequest for this ticket.
        """
        ...

    def get_most_recent_order_response(self) -> QuantConnect.Orders.OrderResponse:
        """
        Gets the most recent OrderResponse for this ticket
        
        :returns: The most recent OrderResponse for this ticket.
        """
        ...

    @staticmethod
    def invalid_cancel_order_id(transaction_manager: QuantConnect.Securities.SecurityTransactionManager, request: QuantConnect.Orders.CancelOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """Creates a new OrderTicket that represents trying to cancel an order for which no ticket exists"""
        ...

    @staticmethod
    def invalid_submit_request(transaction_manager: QuantConnect.Securities.SecurityTransactionManager, request: QuantConnect.Orders.SubmitOrderRequest, response: QuantConnect.Orders.OrderResponse) -> QuantConnect.Orders.OrderTicket:
        """Creates a new OrderTicket that represents trying to submit a new order that had errors embodied in the"""
        ...

    @staticmethod
    def invalid_update_order_id(transaction_manager: QuantConnect.Securities.SecurityTransactionManager, request: QuantConnect.Orders.UpdateOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """Creates a new OrderTicket that represents trying to update an order for which no ticket exists"""
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def update(self, fields: QuantConnect.Orders.UpdateOrderFields) -> QuantConnect.Orders.OrderResponse:
        """
        Submits an UpdateOrderRequest with the SecurityTransactionManager to update
        the ticket with data specified in
        
        :param fields: Defines what properties of the order should be updated
        :returns: The OrderResponse from updating the order.
        """
        ...

    def update_limit_price(self, limit_price: float, tag: str = None) -> QuantConnect.Orders.OrderResponse:
        """
        Submits an UpdateOrderRequest with the SecurityTransactionManager to update
        the ticker with limit price specified in  and with tag specified in
        
        :param limit_price: The new limit price for this order ticket
        :param tag: The new tag for this order ticket
        :returns: OrderResponse from updating the order.
        """
        ...

    def update_quantity(self, quantity: float, tag: str = None) -> QuantConnect.Orders.OrderResponse:
        """
        Submits an UpdateOrderRequest with the SecurityTransactionManager to update
        the ticket with quantity specified in  and with tag specified in
        
        :param quantity: The new quantity for this order ticket
        :param tag: The new tag for this order ticket
        :returns: OrderResponse from updating the order.
        """
        ...

    def update_stop_price(self, stop_price: float, tag: str = None) -> QuantConnect.Orders.OrderResponse:
        """
        Submits an UpdateOrderRequest with the SecurityTransactionManager to update
        the ticker with stop price specified in  and with tag specified in
        
        :param stop_price: The new stop price  for this order ticket
        :param tag: The new tag for this order ticket
        :returns: OrderResponse from updating the order.
        """
        ...

    def update_stop_trailing_amount(self, trailing_amount: float, tag: str = None) -> QuantConnect.Orders.OrderResponse:
        """
        Submits an UpdateOrderRequest with the SecurityTransactionManager to update
        the ticker with stop trailing amount specified in  and with tag specified in
        
        :param trailing_amount: The new trailing amount for this order ticket
        :param tag: The new tag for this order ticket
        :returns: OrderResponse from updating the order.
        """
        ...

    def update_tag(self, tag: str) -> QuantConnect.Orders.OrderResponse:
        """
        Submits an UpdateOrderRequest with the SecurityTransactionManager to update
        the ticket with tag specified in
        
        :param tag: The new tag for this order ticket
        :returns: OrderResponse from updating the order.
        """
        ...

    def update_trigger_price(self, trigger_price: float, tag: str = None) -> QuantConnect.Orders.OrderResponse:
        """
        Submits an UpdateOrderRequest with the SecurityTransactionManager to update
        the ticker with trigger price specified in  and with tag specified in
        
        :param trigger_price: The new price which, when touched, will trigger the setting of a limit order.
        :param tag: The new tag for this order ticket
        :returns: OrderResponse from updating the order.
        """
        ...


class MarketOnCloseOrder(QuantConnect.Orders.Order):
    """Market on close order type - submits a market order on exchange close"""

    DEFAULT_SUBMISSION_TIME_BUFFER: datetime.timedelta = ...
    """
    Gets the default interval before market close that an MOC order may be submitted.
    For example, US equity exchanges typically require MOC orders to be placed no later
    than 15 minutes before market close, which yields a nominal time of 3:45PM.
    This buffer value takes into account the 15 minutes and adds an additional 30 seconds
    to account for other potential delays, such as LEAN order processing and placement of
    the order to the exchange.
    """

    submission_time_buffer: datetime.timedelta = ...
    """The interval before market close that an MOC order may be submitted."""

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """MarketOnClose Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Intiializes a new instance of the MarketOnCloseOrder class."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        Intiializes a new instance of the MarketOnCloseOrder class.
        
        :param symbol: The security's symbol being ordered
        :param quantity: The number of units to order
        :param time: The current time
        :param tag: A user defined tag for the order
        :param properties: The order properties for this order
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...


class AlpacaOrderProperties(QuantConnect.Orders.OrderProperties):
    """Provides an implementation of the OrderProperties specific to Alpaca order."""


class ComboLegLimitOrder(QuantConnect.Orders.ComboOrder):
    """Combo leg limit order type"""

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """Combo Limit Leg Order Type"""
        ...

    @property
    def limit_price(self) -> float:
        """Limit price for this order."""
        ...

    @overload
    def __init__(self) -> None:
        """Added a default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, limitPrice: float, time: typing.Union[datetime.datetime, datetime.date], groupOrderManager: QuantConnect.Orders.GroupOrderManager, tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New limit order constructor
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param limitPrice: Price the order should be filled at if a limit order
        :param time: Time the order was placed
        :param groupOrderManager: Manager for the orders in the group
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...


class TerminalLinkOrderProperties(QuantConnect.Orders.OrderProperties):
    """The terminal link order properties"""

    class StrategyParameters(System.Object):
        """Models an EMSX order strategy parameter"""

        @property
        def name(self) -> str:
            """The strategy name"""
            ...

        @property.setter
        def name(self, value: str) -> None:
            ...

        @property
        def fields(self) -> System.Collections.Generic.List[QuantConnect.Orders.TerminalLinkOrderProperties.StrategyField]:
            """The strategy fields"""
            ...

        @property.setter
        def fields(self, value: System.Collections.Generic.List[QuantConnect.Orders.TerminalLinkOrderProperties.StrategyField]) -> None:
            ...

        def __init__(self, name: str, fields: System.Collections.Generic.List[QuantConnect.Orders.TerminalLinkOrderProperties.StrategyField]) -> None:
            """
            Creates a new TerminalLink order strategy instance
            
            :param name: The strategy name
            :param fields: The strategy fields
            """
            ...

    class StrategyField(System.Object):
        """Models an EMSX order strategy field"""

        @property
        def value(self) -> str:
            """The strategy field value"""
            ...

        @property.setter
        def value(self, value: str) -> None:
            ...

        @property
        def has_value(self) -> bool:
            """Whether the strategy field carries a value"""
            ...

        @property.setter
        def has_value(self, value: bool) -> None:
            ...

        @overload
        def __init__(self, value: str) -> None:
            """
            Creates a new TerminalLink order strategy field carrying a value.
            
            :param value: The strategy field value
            """
            ...

        @overload
        def __init__(self) -> None:
            """Creates a new TerminalLink order strategy field without a value."""
            ...

    @property
    def notes(self) -> str:
        """The EMSX Instructions is the free form instructions that may be sent to the broker"""
        ...

    @property.setter
    def notes(self, value: str) -> None:
        ...

    @property
    def handling_instruction(self) -> str:
        """
        The EMSX Handling Instruction is the instructions for handling the order or route.The values can be
        preconfigured or a value customized by the broker.
        """
        ...

    @property.setter
    def handling_instruction(self, value: str) -> None:
        ...

    @property
    def execution_instruction(self) -> str:
        """The execution instruction field"""
        ...

    @property.setter
    def execution_instruction(self, value: str) -> None:
        ...

    @property
    def custom_notes_1(self) -> str:
        """Custom user order notes 1"""
        ...

    @property.setter
    def custom_notes_1(self, value: str) -> None:
        ...

    @property
    def custom_notes_2(self) -> str:
        """Custom user order notes 2"""
        ...

    @property.setter
    def custom_notes_2(self, value: str) -> None:
        ...

    @property
    def custom_notes_3(self) -> str:
        """Custom user order notes 3"""
        ...

    @property.setter
    def custom_notes_3(self, value: str) -> None:
        ...

    @property
    def custom_notes_4(self) -> str:
        """Custom user order notes 4"""
        ...

    @property.setter
    def custom_notes_4(self, value: str) -> None:
        ...

    @property
    def custom_notes_5(self) -> str:
        """Custom user order notes 5"""
        ...

    @property.setter
    def custom_notes_5(self, value: str) -> None:
        ...

    @property
    def account(self) -> str:
        """The EMSX account"""
        ...

    @property.setter
    def account(self, value: str) -> None:
        ...

    @property
    def broker(self) -> str:
        """The EMSX broker code"""
        ...

    @property.setter
    def broker(self, value: str) -> None:
        ...

    @property
    def strategy(self) -> QuantConnect.Orders.TerminalLinkOrderProperties.StrategyParameters:
        """
        The EMSX order strategy details.
        Strategy parameters must be appended in the correct order as expected by EMSX.
        """
        ...

    @property.setter
    def strategy(self, value: QuantConnect.Orders.TerminalLinkOrderProperties.StrategyParameters) -> None:
        ...

    @property
    def automatic_position_sides(self) -> bool:
        """Whether to automatically include the position side in the order direction (buy-to-open, sell-to-close, etc.) instead of the default (buy, sell)"""
        ...

    @property.setter
    def automatic_position_sides(self, value: bool) -> None:
        ...

    @property
    def position_side(self) -> typing.Optional[QuantConnect.Orders.OrderPosition]:
        """Can optionally specify the position side in the order direction (buy-to-open, sell-to-close, etc.) instead of the default (buy, sell)"""
        ...

    @property.setter
    def position_side(self, value: typing.Optional[QuantConnect.Orders.OrderPosition]) -> None:
        ...


class BrokerageOrderIdChangedEvent(System.Object):
    """Event used when the brokerage order id has changed"""

    @property
    def order_id(self) -> int:
        """The lean order ID."""
        ...

    @property.setter
    def order_id(self, value: int) -> None:
        ...

    @property
    def broker_id(self) -> System.Collections.Generic.List[str]:
        """Brokerage Id for this order"""
        ...

    @property.setter
    def broker_id(self, value: System.Collections.Generic.List[str]) -> None:
        ...


class GDAXOrderProperties(QuantConnect.Orders.CoinbaseOrderProperties):
    """
    Contains additional properties and settings for an order submitted to GDAX brokerage
    
    GDAXOrderProperties is deprecated. Use CoinbaseOrderProperties instead.
    """


class InteractiveBrokersOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to Interactive Brokers"""

    @property
    def account(self) -> str:
        """The linked account for which to submit the order (only used by Financial Advisors)"""
        ...

    @property.setter
    def account(self, value: str) -> None:
        ...

    @property
    def fa_group(self) -> str:
        """The account group for the order (only used by Financial Advisors)"""
        ...

    @property.setter
    def fa_group(self, value: str) -> None:
        ...

    @property
    def fa_method(self) -> str:
        """
        The allocation method for the account group order (only used by Financial Advisors)
        Supported allocation methods are: EqualQuantity, NetLiq, AvailableEquity, PctChange
        """
        ...

    @property.setter
    def fa_method(self, value: str) -> None:
        ...

    @property
    def fa_percentage(self) -> int:
        """The percentage for the percent change method (only used by Financial Advisors)"""
        ...

    @property.setter
    def fa_percentage(self, value: int) -> None:
        ...

    @property
    def fa_profile(self) -> str:
        """The allocation profile to be used for the order (only used by Financial Advisors)"""
        ...

    @property.setter
    def fa_profile(self, value: str) -> None:
        ...

    @property
    def outside_regular_trading_hours(self) -> bool:
        """If set to true, allows orders to also trigger or fill outside of regular trading hours."""
        ...

    @property.setter
    def outside_regular_trading_hours(self, value: bool) -> None:
        ...

    def clone(self) -> QuantConnect.Interfaces.IOrderProperties:
        """Returns a new instance clone of this object"""
        ...


class OptionExerciseOrder(QuantConnect.Orders.Order):
    """Option exercise order type definition"""

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """Option Exercise Order Type"""
        ...

    @overload
    def __init__(self) -> None:
        """Added a default constructor for JSON Deserialization:"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New option exercise order constructor. We model option exercising as an underlying asset long/short order with strike equal to limit price.
        This means that by exercising a call we get into long asset position, by exercising a put we get into short asset position.
        
        :param symbol: Option symbol we're seeking to exercise
        :param quantity: Quantity of the option we're seeking to exercise. Must be a positive value.
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in option contracts quoted in options's currency
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...


class LimitIfTouchedOrder(QuantConnect.Orders.Order):
    """
    In effect, a LimitIfTouchedOrder behaves opposite to the StopLimitOrder;
    after a trigger price is touched, a limit order is set for some user-defined value above (below)
    the trigger when selling (buying).
    https://www.interactivebrokers.ca/en/index.php?f=45318
    """

    @property
    def type(self) -> QuantConnect.Orders.OrderType:
        """Order Type"""
        ...

    @property
    def trigger_price(self) -> float:
        """The price which, when touched, will trigger the setting of a limit order at LimitPrice."""
        ...

    @property
    def limit_price(self) -> float:
        """The price at which to set the limit order following TriggerPrice being touched."""
        ...

    @property
    def trigger_touched(self) -> bool:
        """Whether or not the TriggerPrice has been touched."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, triggerPrice: typing.Optional[float], limitPrice: float, time: typing.Union[datetime.datetime, datetime.date], tag: str = ..., properties: QuantConnect.Interfaces.IOrderProperties = None) -> None:
        """
        New LimitIfTouchedOrder constructor.
        
        :param symbol: Symbol asset we're seeking to trade
        :param quantity: Quantity of the asset we're seeking to trade
        :param triggerPrice: Price which must be touched in order to then set a limit order
        :param limitPrice: Maximum price to fill the order
        :param time: Time the order was placed
        :param tag: User defined data tag for this order
        :param properties: The order properties for this order
        """
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Deserialization:"""
        ...

    def apply_update_order_request(self, request: QuantConnect.Orders.UpdateOrderRequest) -> None:
        """
        Modifies the state of this order to match the update request
        
        :param request: The request to update this order object
        """
        ...

    def clone(self) -> QuantConnect.Orders.Order:
        """
        Creates a deep-copy clone of this order
        
        :returns: A copy of this order.
        """
        ...

    def get_default_tag(self) -> str:
        """
        Gets the default tag for this order
        
        :returns: The default tag.
        """
        ...

    def get_value_impl(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the order value in units of the security's quote currency for a single unit.
        A single unit here is a single share of stock, or a single barrel of oil, or the
        cost of a single share in an option contract.
        
        This method is protected.
        
        :param security: The security matching this order's symbol
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class CharlesSchwabOrderProperties(QuantConnect.Orders.OrderProperties):
    """Contains additional properties and settings for an order submitted to Charles Schwab brokerage"""

    @property
    def extended_regular_trading_hours(self) -> bool:
        """If set to true, allows orders to also trigger or fill outside of regular trading hours."""
        ...

    @property.setter
    def extended_regular_trading_hours(self, value: bool) -> None:
        ...


class Leg(System.Object):
    """Basic order leg"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """The legs symbol"""
        ...

    @property.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def quantity(self) -> int:
        """Quantity multiplier used to specify proper scale (and direction) of the leg within the strategy"""
        ...

    @property.setter
    def quantity(self, value: int) -> None:
        ...

    @property
    def order_price(self) -> typing.Optional[float]:
        """Order limit price of the leg in case limit order is sent to the market on strategy execution"""
        ...

    @property.setter
    def order_price(self, value: typing.Optional[float]) -> None:
        ...

    @staticmethod
    def create(symbol: typing.Union[QuantConnect.Symbol, str], quantity: int, limit_price: typing.Optional[float] = None) -> QuantConnect.Orders.Leg:
        """
        Creates a new instance
        
        :param symbol: The symbol
        :param quantity: The quantity
        :param limit_price: Associated limit price if any
        """
        ...


class OrderExtensions(System.Object):
    """Provides extension methods for the Order class and for the OrderStatus enumeration"""

    @staticmethod
    def is_closed(status: QuantConnect.Orders.OrderStatus) -> bool:
        """
        Determines if the specified status is in a closed state.
        
        :param status: The status to check
        :returns: True if the status is OrderStatus.Filled, OrderStatus.Canceled, or OrderStatus.Invalid.
        """
        ...

    @staticmethod
    def is_fill(status: QuantConnect.Orders.OrderStatus) -> bool:
        """
        Determines if the specified status is a fill, that is, OrderStatus.Filled
        order OrderStatus.PartiallyFilled
        
        :param status: The status to check
        :returns: True if the status is OrderStatus.Filled or OrderStatus.PartiallyFilled, false otherwise.
        """
        ...

    @staticmethod
    def is_limit_order(order_type: QuantConnect.Orders.OrderType) -> bool:
        """
        Determines whether or not the specified order is a limit order
        
        :param order_type: The order to check
        :returns: True if the order is a limit order, false otherwise.
        """
        ...

    @staticmethod
    def is_open(status: QuantConnect.Orders.OrderStatus) -> bool:
        """
        Determines if the specified status is in an open state.
        
        :param status: The status to check
        :returns: True if the status is not OrderStatus.Filled, OrderStatus.Canceled, or OrderStatus.Invalid.
        """
        ...

    @staticmethod
    def is_stop_order(order_type: QuantConnect.Orders.OrderType) -> bool:
        """
        Determines whether or not the specified order is a stop order
        
        :param order_type: The order to check
        :returns: True if the order is a stop order, false otherwise.
        """
        ...


