from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Benchmarks
import QuantConnect.Brokerages
import QuantConnect.Brokerages.CrossZero
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Slippage
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections.Concurrent
import System.Collections.Generic

QuantConnect_Brokerages_WebSocketClientWrapper_MessageData = typing.Any

QuantConnect_Brokerages_BrokerageConcurrentMessageHandler_T = typing.TypeVar("QuantConnect_Brokerages_BrokerageConcurrentMessageHandler_T")
QuantConnect_Brokerages_BrokerageFactory_Read_T = typing.TypeVar("QuantConnect_Brokerages_BrokerageFactory_Read_T")
QuantConnect_Brokerages_IOrderBookUpdater_K = typing.TypeVar("QuantConnect_Brokerages_IOrderBookUpdater_K")
QuantConnect_Brokerages_IOrderBookUpdater_V = typing.TypeVar("QuantConnect_Brokerages_IOrderBookUpdater_V")
QuantConnect_Brokerages__EventContainer_Callable = typing.TypeVar("QuantConnect_Brokerages__EventContainer_Callable")
QuantConnect_Brokerages__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Brokerages__EventContainer_ReturnType")


class WebSocketMessage(System.Object):
    """Defines a message received at a web socket"""

    @property
    def web_socket(self) -> QuantConnect.Brokerages.IWebSocket:
        """Gets the sender websocket instance"""
        ...

    @property
    def data(self) -> QuantConnect.Brokerages.WebSocketClientWrapper.MessageData:
        """Gets the raw message data as text"""
        ...

    def __init__(self, webSocket: QuantConnect.Brokerages.IWebSocket, data: QuantConnect.Brokerages.WebSocketClientWrapper.MessageData) -> None:
        """
        Initializes a new instance of the WebSocketMessage class
        
        :param webSocket: The sender websocket instance
        :param data: The message data
        """
        ...


class WebSocketError(System.Object):
    """Defines data returned from a web socket error"""

    @property
    def message(self) -> str:
        """Gets the message"""
        ...

    @property
    def exception(self) -> System.Exception:
        """Gets the exception raised"""
        ...

    def __init__(self, message: str, exception: System.Exception) -> None:
        """
        Initializes a new instance of the WebSocketError class
        
        :param message: The message
        :param exception: The error
        """
        ...


class WebSocketCloseData(System.Object):
    """Defines data returned from a web socket close event"""

    @property
    def code(self) -> int:
        """Gets the status code for the connection close."""
        ...

    @property
    def reason(self) -> str:
        """Gets the reason for the connection close."""
        ...

    @property
    def was_clean(self) -> bool:
        """Gets a value indicating whether the connection has been closed cleanly."""
        ...

    def __init__(self, code: int, reason: str, wasClean: bool) -> None:
        """
        Initializes a new instance of the WebSocketCloseData class
        
        :param code: The status code for the connection close
        :param reason: The reaspn for the connection close
        :param wasClean: True if the connection has been closed cleanly, false otherwise
        """
        ...


class IWebSocket(metaclass=abc.ABCMeta):
    """Wrapper for WebSocket4Net to enhance testability"""

    @property
    @abc.abstractmethod
    def is_open(self) -> bool:
        """Wraps IsOpen"""
        ...

    @property
    @abc.abstractmethod
    def message(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.WebSocketMessage], None], None]:
        """on message event"""
        ...

    @property
    @abc.abstractmethod
    def error(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.WebSocketError], None], None]:
        """On error event"""
        ...

    @property
    @abc.abstractmethod
    def open(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """On Open event"""
        ...

    @property
    @abc.abstractmethod
    def closed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.WebSocketCloseData], None], None]:
        """On Close event"""
        ...

    def close(self) -> None:
        """Wraps Close method"""
        ...

    def connect(self) -> None:
        """Wraps Connect method"""
        ...

    def initialize(self, url: str, session_token: str = None) -> None:
        """
        Wraps constructor
        
        :param url: The target websocket url
        :param session_token: The websocket session token
        """
        ...

    def send(self, data: str) -> None:
        """Wraps send method"""
        ...


class WebSocketClientWrapper(System.Object, QuantConnect.Brokerages.IWebSocket):
    """Wrapper for System.Net.Websockets.ClientWebSocket to enhance testability"""

    class MessageData(System.Object, metaclass=abc.ABCMeta):
        """Defines a message of websocket data"""

        @property
        def message_type(self) -> typing.Any:
            """Type of message"""
            ...

        @property.setter
        def message_type(self, value: typing.Any) -> None:
            ...

    class TextMessage(QuantConnect_Brokerages_WebSocketClientWrapper_MessageData):
        """Defines a text-Type message of websocket data"""

        @property
        def message(self) -> str:
            """Data contained in message"""
            ...

        @property.setter
        def message(self, value: str) -> None:
            ...

        def __init__(self) -> None:
            """Constructs default instance of the TextMessage"""
            ...

    class BinaryMessage(QuantConnect_Brokerages_WebSocketClientWrapper_MessageData):
        """Defines a byte-Type message of websocket data"""

        @property
        def data(self) -> typing.List[int]:
            """Data contained in message"""
            ...

        @property.setter
        def data(self, value: typing.List[int]) -> None:
            ...

        @property
        def count(self) -> int:
            """Count of message"""
            ...

        @property.setter
        def count(self, value: int) -> None:
            ...

        def __init__(self) -> None:
            """Constructs default instance of the BinaryMessage"""
            ...

    @property
    def is_open(self) -> bool:
        """Wraps IsAlive"""
        ...

    @property
    def message(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.WebSocketMessage], None], None]:
        """Wraps message event"""
        ...

    @property
    def error(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.WebSocketError], None], None]:
        """Wraps error event"""
        ...

    @property
    def open(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Wraps open method"""
        ...

    @property
    def closed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.WebSocketCloseData], None], None]:
        """Wraps close method"""
        ...

    def close(self) -> None:
        """Wraps Close method"""
        ...

    def connect(self) -> None:
        """Wraps Connect method"""
        ...

    def initialize(self, url: str, session_token: str = None) -> None:
        """
        Wraps constructor
        
        :param url: The target websocket url
        :param session_token: The websocket session token
        """
        ...

    def on_close(self, e: QuantConnect.Brokerages.WebSocketCloseData) -> None:
        """
        Event invocator for the Close event
        
        This method is protected.
        """
        ...

    def on_error(self, e: QuantConnect.Brokerages.WebSocketError) -> None:
        """
        Event invocator for the Error event
        
        This method is protected.
        """
        ...

    def on_message(self, e: QuantConnect.Brokerages.WebSocketMessage) -> None:
        """
        Event invocator for the Message event
        
        This method is protected.
        """
        ...

    def on_open(self) -> None:
        """
        Event invocator for the Open event
        
        This method is protected.
        """
        ...

    def send(self, data: str) -> None:
        """Wraps send method"""
        ...


class ISymbolMapper(metaclass=abc.ABCMeta):
    """Provides the mapping between Lean symbols and brokerage specific symbols."""

    def get_brokerage_symbol(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Lean symbol instance to a brokerage symbol
        
        :param symbol: A Lean symbol instance
        :returns: The brokerage symbol.
        """
        ...

    def get_lean_symbol(self, brokerage_symbol: str, security_type: QuantConnect.SecurityType, market: str, expiration_date: typing.Union[datetime.datetime, datetime.date] = ..., strike: float = 0, option_right: QuantConnect.OptionRight = 0) -> QuantConnect.Symbol:
        """
        Converts a brokerage symbol to a Lean symbol instance
        
        :param brokerage_symbol: The brokerage symbol
        :param security_type: The security type
        :param market: The market
        :param expiration_date: Expiration date of the security(if applicable)
        :param strike: The strike of the security (if applicable)
        :param option_right: The option right of the security (if applicable)
        :returns: A new Lean Symbol instance.
        """
        ...


class SymbolPropertiesDatabaseSymbolMapper(System.Object, QuantConnect.Brokerages.ISymbolMapper):
    """Provides the mapping between Lean symbols and brokerage symbols using the symbol properties database"""

    def __init__(self, market: str) -> None:
        """
        Creates a new instance of the SymbolPropertiesDatabaseSymbolMapper class.
        
        :param market: The Lean market
        """
        ...

    def get_brokerage_security_type(self, brokerage_symbol: str) -> QuantConnect.SecurityType:
        """
        Returns the security type for a brokerage symbol
        
        :param brokerage_symbol: The brokerage symbol
        :returns: The security type.
        """
        ...

    def get_brokerage_symbol(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Converts a Lean symbol instance to a brokerage symbol
        
        :param symbol: A Lean symbol instance
        :returns: The brokerage symbol.
        """
        ...

    def get_lean_symbol(self, brokerage_symbol: str, security_type: QuantConnect.SecurityType, market: str, expiration_date: typing.Union[datetime.datetime, datetime.date] = ..., strike: float = 0, option_right: QuantConnect.OptionRight = ...) -> QuantConnect.Symbol:
        """
        Converts a brokerage symbol to a Lean symbol instance
        
        :param brokerage_symbol: The brokerage symbol
        :param security_type: The security type
        :param market: The market
        :param expiration_date: Expiration date of the security(if applicable)
        :param strike: The strike of the security (if applicable)
        :param option_right: The option right of the security (if applicable)
        :returns: A new Lean Symbol instance.
        """
        ...

    def is_known_brokerage_symbol(self, brokerage_symbol: str) -> bool:
        """
        Checks if the symbol is supported by the brokerage
        
        :param brokerage_symbol: The brokerage symbol
        :returns: True if the brokerage supports the symbol.
        """
        ...

    def is_known_lean_symbol(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Checks if the Lean symbol is supported by the brokerage
        
        :param symbol: The Lean symbol
        :returns: True if the brokerage supports the symbol.
        """
        ...


class BrokerageMultiWebSocketEntry(System.Object):
    """Helper class for BrokerageMultiWebSocketSubscriptionManager"""

    @property
    def web_socket(self) -> QuantConnect.Brokerages.IWebSocket:
        """Gets the web socket instance"""
        ...

    @property
    def total_weight(self) -> int:
        """Gets the sum of symbol weights for this web socket"""
        ...

    @property
    def symbol_count(self) -> int:
        """Gets the number of symbols subscribed"""
        ...

    @property
    def symbols(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.Symbol]:
        """Returns the list of subscribed symbols"""
        ...

    @overload
    def __init__(self, symbolWeights: System.Collections.Generic.Dictionary[QuantConnect.Symbol, int], webSocket: QuantConnect.Brokerages.IWebSocket) -> None:
        """
        Initializes a new instance of the BrokerageMultiWebSocketEntry class
        
        :param symbolWeights: A dictionary of symbol weights
        :param webSocket: The web socket instance
        """
        ...

    @overload
    def __init__(self, webSocket: QuantConnect.Brokerages.IWebSocket) -> None:
        """
        Initializes a new instance of the BrokerageMultiWebSocketEntry class
        
        :param webSocket: The web socket instance
        """
        ...

    def add_symbol(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Adds a symbol to the entry
        
        :param symbol: The symbol to add
        """
        ...

    def contains(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """Returns whether the symbol is subscribed"""
        ...

    def remove_symbol(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Removes a symbol from the entry
        
        :param symbol: The symbol to remove
        """
        ...


class OptionNotificationEventArgs(System.EventArgs):
    """Event arguments class for the IBrokerage.OptionNotification event"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the option symbol which has received a notification"""
        ...

    @property
    def position(self) -> float:
        """Gets the new option position (positive for long, zero for flat, negative for short)"""
        ...

    @property
    def tag(self) -> str:
        """The tag that will be used in the order"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], position: float) -> None:
        """
        Initializes a new instance of the OptionNotificationEventArgs class
        
        :param symbol: The symbol
        :param position: The new option position
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], position: float, tag: str) -> None:
        """
        Initializes a new instance of the OptionNotificationEventArgs class
        
        :param symbol: The symbol
        :param position: The new option position
        :param tag: The tag to be used for the order
        """
        ...

    def to_string(self) -> str:
        """Returns the string representation of this event"""
        ...


class NewBrokerageOrderNotificationEventArgs(System.Object):
    """Event arguments class for the IBrokerage.NewBrokerageOrderNotification event"""

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """The new brokerage side generated order"""
        ...

    @property.setter
    def order(self, value: QuantConnect.Orders.Order) -> None:
        ...

    def __init__(self, order: QuantConnect.Orders.Order) -> None:
        """Creates a new instance"""
        ...


class DelistingNotificationEventArgs(System.Object):
    """Event arguments class for the IBrokerage.DelistingNotification event"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the option symbol which has received a notification"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Initializes a new instance of the DelistingNotificationEventArgs class
        
        :param symbol: The symbol
        """
        ...


class BrokerageMessageType(Enum):
    """Specifies the type of message received from an IBrokerage implementation"""

    INFORMATION = 0
    """Informational message (0)"""

    WARNING = 1
    """Warning message (1)"""

    ERROR = 2
    """Fatal error message, the algo will be stopped (2)"""

    RECONNECT = 3
    """Brokerage reconnected with remote server (3)"""

    DISCONNECT = 4
    """Brokerage disconnected from remote server (4)"""


class BrokerageMessageEvent(System.Object):
    """Represents a message received from a brokerage"""

    @property
    def type(self) -> QuantConnect.Brokerages.BrokerageMessageType:
        """Gets the type of brokerage message"""
        ...

    @property
    def code(self) -> str:
        """Gets the brokerage specific code for this message, zero if no code was specified"""
        ...

    @property
    def message(self) -> str:
        """Gets the message text received from the brokerage"""
        ...

    @overload
    def __init__(self, type: QuantConnect.Brokerages.BrokerageMessageType, code: int, message: str) -> None:
        """
        Initializes a new instance of the BrokerageMessageEvent class
        
        :param type: The type of brokerage message
        :param code: The brokerage specific code
        :param message: The message text received from the brokerage
        """
        ...

    @overload
    def __init__(self, type: QuantConnect.Brokerages.BrokerageMessageType, code: str, message: str) -> None:
        """
        Initializes a new instance of the BrokerageMessageEvent class
        
        :param type: The type of brokerage message
        :param code: The brokerage specific code
        :param message: The message text received from the brokerage
        """
        ...

    @staticmethod
    def disconnected(message: str) -> QuantConnect.Brokerages.BrokerageMessageEvent:
        """
        Creates a new BrokerageMessageEvent to represent a disconnect message
        
        :param message: The message from the brokerage
        :returns: A brokerage disconnect message.
        """
        ...

    @staticmethod
    def reconnected(message: str) -> QuantConnect.Brokerages.BrokerageMessageEvent:
        """
        Creates a new BrokerageMessageEvent to represent a reconnect message
        
        :param message: The message from the brokerage
        :returns: A brokerage reconnect message.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class Brokerage(System.Object, QuantConnect.Interfaces.IBrokerage, metaclass=abc.ABCMeta):
    """Represents the base Brokerage implementation. This provides logging on brokerage events."""

    @property
    def order_id_changed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.BrokerageOrderIdChangedEvent], None], None]:
        """Event that fires each time the brokerage order id changes"""
        ...

    @property
    def orders_status_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]], None], None]:
        """Event that fires each time the status for a list of orders change"""
        ...

    @property
    def order_updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.OrderUpdateEvent], None], None]:
        """Event that fires each time an order is updated in the brokerage side"""
        ...

    @property
    def option_position_assigned(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.OrderEvent], None], None]:
        """Event that fires each time a short option position is assigned"""
        ...

    @property
    def option_notification(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.OptionNotificationEventArgs], None], None]:
        """Event that fires each time an option position has changed"""
        ...

    @property
    def new_brokerage_order_notification(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.NewBrokerageOrderNotificationEventArgs], None], None]:
        """Event that fires each time there's a brokerage side generated order"""
        ...

    @property
    def delisting_notification(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.DelistingNotificationEventArgs], None], None]:
        """Event that fires each time a delisting occurs"""
        ...

    @property
    def account_changed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Securities.AccountEvent], None], None]:
        """Event that fires each time a user's brokerage account is changed"""
        ...

    @property
    def message(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.BrokerageMessageEvent], None], None]:
        """Event that fires when an error is encountered in the brokerage"""
        ...

    @property
    def name(self) -> str:
        """Gets the name of the brokerage"""
        ...

    @property
    @abc.abstractmethod
    def is_connected(self) -> bool:
        """Returns true if we're currently connected to the broker"""
        ...

    @property
    def account_instantly_updated(self) -> bool:
        """Specifies whether the brokerage will instantly update account balances"""
        ...

    @property
    def account_base_currency(self) -> str:
        """Returns the brokerage account's base currency"""
        ...

    @property
    def last_sync_date(self) -> datetime.datetime:
        """
        Gets the date of the last sync (New York time zone)
        
        This property is protected.
        """
        ...

    @property
    def last_sync_date_time_utc(self) -> datetime.datetime:
        """Gets the datetime of the last sync (UTC)"""
        ...

    @property
    def lean_order_by_zero_cross_brokerage_order_id(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, QuantConnect.Orders.Order]:
        """
        A thread-safe dictionary that maps brokerage order IDs to their corresponding Order objects.
        
        This property is protected.
        """
        ...

    def __init__(self, name: str) -> None:
        """
        Creates a new Brokerage instance with the specified name
        
        This method is protected.
        
        :param name: The name of the brokerage
        """
        ...

    def cancel_order(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Cancels the order with the specified ID
        
        :param order: The order to cancel
        :returns: True if the request was made for the order to be canceled, false otherwise.
        """
        ...

    def connect(self) -> None:
        """Connects the client to the broker's remote servers"""
        ...

    def disconnect(self) -> None:
        """Disconnects the client from the broker's remote servers"""
        ...

    def dispose(self) -> None:
        """Dispose of the brokerage instance"""
        ...

    @overload
    def get_account_holdings(self, brokerage_data: System.Collections.Generic.Dictionary[str, str], securities: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security]) -> System.Collections.Generic.List[QuantConnect.Holding]:
        """
        Helper method that will try to get the live holdings from the provided brokerage data collection else will default to the algorithm state
        
        This method is protected.
        """
        ...

    @overload
    def get_account_holdings(self) -> System.Collections.Generic.List[QuantConnect.Holding]:
        """
        Gets all holdings for the account
        
        :returns: The current holdings from the account.
        """
        ...

    @overload
    def get_cash_balance(self, brokerage_data: System.Collections.Generic.Dictionary[str, str], cash_book: QuantConnect.Securities.CashBook) -> System.Collections.Generic.List[QuantConnect.Securities.CashAmount]:
        """
        Helper method that will try to get the live cash balance from the provided brokerage data collection else will default to the algorithm state
        
        This method is protected.
        """
        ...

    @overload
    def get_cash_balance(self) -> System.Collections.Generic.List[QuantConnect.Securities.CashAmount]:
        """
        Gets the current cash balance for each currency held in the brokerage account
        
        :returns: The current cash balance for each currency available for trading.
        """
        ...

    def get_history(self, request: QuantConnect.Data.HistoryRequest) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Gets the history for the requested security
        
        :param request: The historical data request
        :returns: An enumerable of bars covering the span specified in the request.
        """
        ...

    def get_open_orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets all open orders on the account.
        NOTE: The order objects returned do not have QC order IDs.
        
        :returns: The open orders returned from IB.
        """
        ...

    @staticmethod
    def get_order_position(order_direction: QuantConnect.Orders.OrderDirection, holdings_quantity: float) -> QuantConnect.Orders.OrderPosition:
        """
        Gets the position that might result given the specified order direction and the current holdings quantity.
        This is useful for brokerages that require more specific direction information than provided by the OrderDirection enum
        (e.g. Tradier differentiates Buy/Sell and BuyToOpen/BuyToCover/SellShort/SellToClose)
        
        This method is protected.
        
        :param order_direction: The order direction
        :param holdings_quantity: The current holdings quantity
        :returns: The order position.
        """
        ...

    def on_account_changed(self, e: QuantConnect.Securities.AccountEvent) -> None:
        """
        Event invocator for the AccountChanged event
        
        This method is protected.
        
        :param e: The AccountEvent
        """
        ...

    def on_delisting_notification(self, e: QuantConnect.Brokerages.DelistingNotificationEventArgs) -> None:
        """
        Event invocator for the DelistingNotification event
        
        This method is protected.
        
        :param e: The DelistingNotification event arguments
        """
        ...

    def on_message(self, e: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Event invocator for the Message event
        
        This method is protected.
        
        :param e: The error
        """
        ...

    def on_new_brokerage_order_notification(self, e: QuantConnect.Brokerages.NewBrokerageOrderNotificationEventArgs) -> None:
        """
        Event invocator for the NewBrokerageOrderNotification event
        
        This method is protected.
        
        :param e: The NewBrokerageOrderNotification event arguments
        """
        ...

    def on_option_notification(self, e: QuantConnect.Brokerages.OptionNotificationEventArgs) -> None:
        """
        Event invocator for the OptionNotification event
        
        This method is protected.
        
        :param e: The OptionNotification event arguments
        """
        ...

    def on_option_position_assigned(self, e: QuantConnect.Orders.OrderEvent) -> None:
        """
        Event invocator for the OptionPositionAssigned event
        
        This method is protected.
        
        :param e: The OrderEvent
        """
        ...

    def on_order_event(self, e: QuantConnect.Orders.OrderEvent) -> None:
        """
        Event invocator for the OrderFilled event
        
        This method is protected.
        
        :param e: The order event
        """
        ...

    def on_order_events(self, order_events: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]) -> None:
        """
        Event invocator for the OrderFilled event
        
        This method is protected.
        
        :param order_events: The list of order events
        """
        ...

    def on_order_id_changed_event(self, e: QuantConnect.Orders.BrokerageOrderIdChangedEvent) -> None:
        """
        Event invocator for the OrderIdChanged event
        
        This method is protected.
        
        :param e: The BrokerageOrderIdChangedEvent
        """
        ...

    def on_order_updated(self, e: QuantConnect.Orders.OrderUpdateEvent) -> None:
        """
        Event invocator for the OrderUpdated event
        
        This method is protected.
        
        :param e: The update event
        """
        ...

    def perform_cash_sync(self, algorithm: QuantConnect.Interfaces.IAlgorithm, current_time_utc: typing.Union[datetime.datetime, datetime.date], get_time_since_last_fill: typing.Callable[[], datetime.timedelta]) -> bool:
        """
        Synchronizes the cashbook with the brokerage account
        
        :param algorithm: The algorithm instance
        :param current_time_utc: The current time (UTC)
        :param get_time_since_last_fill: A function which returns the time elapsed since the last fill
        :returns: True if the cash sync was performed successfully.
        """
        ...

    def place_cross_zero_order(self, cross_zero_order_request: QuantConnect.Brokerages.CrossZero.CrossZeroFirstOrderRequest, is_place_order_with_lean_event: bool = True) -> QuantConnect.Brokerages.CrossZero.CrossZeroOrderResponse:
        """
        Places an order that crosses zero (transitions from a short position to a long position or vice versa) and returns the response.
        This method should be overridden in a derived class to implement brokerage-specific logic for placing such orders.
        
        This method is protected.
        
        :param cross_zero_order_request: The request object containing details of the cross zero order to be placed.
        :param is_place_order_with_lean_event: A boolean indicating whether the order should be placed with triggering a Lean event. Default is true, meaning Lean events will be triggered.
        :returns: A CrossZeroOrderResponse object indicating the result of the order placement.
        """
        ...

    def place_order(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Places a new order and assigns a new broker ID to the order
        
        :param order: The order to be placed
        :returns: True if the request for a new order has been placed, false otherwise.
        """
        ...

    def should_perform_cash_sync(self, current_time_utc: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Returns whether the brokerage should perform the cash synchronization
        
        :param current_time_utc: The current time (UTC)
        :returns: True if the cash sync should be performed.
        """
        ...

    def try_cross_zero_position_order(self, order: QuantConnect.Orders.Order, holding_quantity: float) -> typing.Optional[bool]:
        """
        Attempts to place an order that may cross the zero position.
        If the order needs to be split into two parts due to crossing zero,
        this method handles the split and placement accordingly.
        
        This method is protected.
        
        :param order: The order to be placed. Must not be null.
        :param holding_quantity: The current holding quantity of the order's symbol.
        :returns: true if the order crosses zero and the first part was successfully placed;false if the first part of the order could not be placed;null if the order does not cross zero.
        """
        ...

    def try_get_or_remove_cross_zero_order(self, brokerage_order_id: str, lean_order_status: QuantConnect.Orders.OrderStatus, lean_order: typing.Optional[QuantConnect.Orders.Order]) -> typing.Union[bool, QuantConnect.Orders.Order]:
        """
        Attempts to retrieve or remove a cross-zero order based on the brokerage order ID and its filled status.
        
        This method is protected.
        
        :param brokerage_order_id: The unique identifier of the brokerage order.
        :param lean_order_status: The updated status of the order received from the brokerage
        :param lean_order: When this method returns, contains the Order object associated with the given brokerage order ID, if the operation was successful; otherwise, null. This parameter is passed uninitialized.
        :returns: true if the method successfully retrieves or removes the order; otherwise, false.
        """
        ...

    def try_get_update_cross_zero_order_quantity(self, lean_order: QuantConnect.Orders.Order, quantity: typing.Optional[float]) -> typing.Union[bool, float]:
        """
        Determines whether the given Lean order crosses zero quantity based on the initial order quantity.
        
        This method is protected.
        
        :param lean_order: The Lean order to check.
        :param quantity: The quantity to be updated based on whether the order crosses zero.
        :returns: true if the Lean order does not cross zero quantity; otherwise, false.
        """
        ...

    def try_handle_remaining_cross_zero_order(self, lean_order: QuantConnect.Orders.Order, order_event: QuantConnect.Orders.OrderEvent) -> bool:
        """
        Attempts to handle any remaining orders that cross the zero boundary.
        
        This method is protected.
        
        :param lean_order: The order object that needs to be processed.
        :param order_event: The event object containing order event details.
        """
        ...

    def update_order(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Updates the order with the same id
        
        :param order: The new order information
        :returns: True if the request was made for the order to be updated, false otherwise.
        """
        ...


class BaseWebsocketsBrokerage(QuantConnect.Brokerages.Brokerage, metaclass=abc.ABCMeta):
    """Provides shared brokerage websockets implementation"""

    @property
    def is_initialized(self) -> bool:
        """
        True if the current brokerage is already initialized
        
        This property is protected.
        """
        ...

    @property.setter
    def is_initialized(self, value: bool) -> None:
        ...

    @property
    def web_socket(self) -> QuantConnect.Brokerages.IWebSocket:
        """
        The websockets client instance
        
        This property is protected.
        """
        ...

    @property.setter
    def web_socket(self, value: QuantConnect.Brokerages.IWebSocket) -> None:
        ...

    @property
    def rest_client(self) -> typing.Any:
        """
        The rest client instance
        
        This property is protected.
        """
        ...

    @property.setter
    def rest_client(self, value: typing.Any) -> None:
        ...

    @property
    def json_settings(self) -> typing.Any:
        """
        standard json parsing settings
        
        This property is protected.
        """
        ...

    @property.setter
    def json_settings(self, value: typing.Any) -> None:
        ...

    @property
    def cached_order_i_ds(self) -> System.Collections.Concurrent.ConcurrentDictionary[int, QuantConnect.Orders.Order]:
        """A list of currently active orders"""
        ...

    @property.setter
    def cached_order_i_ds(self, value: System.Collections.Concurrent.ConcurrentDictionary[int, QuantConnect.Orders.Order]) -> None:
        ...

    @property
    def api_secret(self) -> str:
        """
        The api secret
        
        This property is protected.
        """
        ...

    @property.setter
    def api_secret(self, value: str) -> None:
        ...

    @property
    def api_key(self) -> str:
        """
        The api key
        
        This property is protected.
        """
        ...

    @property.setter
    def api_key(self, value: str) -> None:
        ...

    @property
    def subscription_manager(self) -> QuantConnect.Data.DataQueueHandlerSubscriptionManager:
        """
        Count subscribers for each (symbol, tickType) combination
        
        This property is protected.
        """
        ...

    @property.setter
    def subscription_manager(self, value: QuantConnect.Data.DataQueueHandlerSubscriptionManager) -> None:
        ...

    def __init__(self, name: str) -> None:
        """
        Creates an instance of a websockets brokerage
        
        This method is protected.
        
        :param name: Name of brokerage
        """
        ...

    def connect(self) -> None:
        """Creates wss connection, monitors for disconnection and re-connects when necessary"""
        ...

    def connect_sync(self) -> None:
        """
        Start websocket connect
        
        This method is protected.
        """
        ...

    def get_subscribed(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets a list of current subscriptions
        
        This method is protected.
        """
        ...

    def initialize(self, wss_url: str, websocket: QuantConnect.Brokerages.IWebSocket, rest_client: typing.Any, api_key: str, api_secret: str) -> None:
        """
        Initialize the instance of this class
        
        This method is protected.
        
        :param wss_url: The web socket base url
        :param websocket: instance of websockets client
        :param rest_client: instance of rest client
        :param api_key: api key
        :param api_secret: api secret
        """
        ...

    def on_message(self, sender: typing.Any, e: QuantConnect.Brokerages.WebSocketMessage) -> None:
        """
        Handles websocket received messages
        
        This method is protected.
        """
        ...

    def subscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> bool:
        """
        Handles the creation of websocket subscriptions
        
        This method is protected.
        """
        ...


class BrokerageConcurrentMessageHandler(typing.Generic[QuantConnect_Brokerages_BrokerageConcurrentMessageHandler_T], System.Object):
    """Brokerage helper class to lock message stream while executing an action, for example placing an order"""

    def __init__(self, processMessages: typing.Callable[[QuantConnect_Brokerages_BrokerageConcurrentMessageHandler_T], None]) -> None:
        """
        Creates a new instance
        
        :param processMessages: The action to call for each new message
        """
        ...

    def handle_new_message(self, message: QuantConnect_Brokerages_BrokerageConcurrentMessageHandler_T) -> None:
        """
        Will process or enqueue a message for later processing it
        
        :param message: The new message
        """
        ...

    def with_locked_stream(self, code: typing.Callable[[], None]) -> None:
        """Lock the streaming processing while we're sending orders as sometimes they fill before the call returns."""
        ...


class IBrokerageModel(metaclass=abc.ABCMeta):
    """Models brokerage transactions, fees, and order"""

    @property
    @abc.abstractmethod
    def account_type(self) -> QuantConnect.AccountType:
        """Gets the account type used by this model"""
        ...

    @property
    @abc.abstractmethod
    def required_free_buying_power_percent(self) -> float:
        """
        Gets the brokerages model percentage factor used to determine the required unused buying power for the account.
        From 1 to 0. Example: 0 means no unused buying power is required. 0.5 means 50% of the buying power should be left unused.
        """
        ...

    @property
    @abc.abstractmethod
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def apply_split(self, tickets: System.Collections.Generic.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        """
        Applies the split to the specified order ticket
        
        :param tickets: The open tickets matching the split event
        :param split: The split event data
        """
        ...

    def can_execute_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not perform
        executions during extended market hours. This is not intended to be checking whether or not
        the exchange is open, that is handled in the Security.Exchange property.
        
        :param security: The security being ordered
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested updated to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    @overload
    def get_buying_power_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        """
        Gets a new buying power model for the security
        
        :param security: The security to get a buying power model for
        :returns: The buying power model for this brokerage/security.
        """
        ...

    @overload
    def get_buying_power_model(self, security: QuantConnect.Securities.Security, account_type: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        """
        Gets a new buying power model for the security
        
        Flagged deprecated and will remove December 1st 2018
        
        :param security: The security to get a buying power model for
        :param account_type: The account type
        :returns: The buying power model for this brokerage/security.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_fill_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        """
        Gets a new fill model that represents this brokerage's fill behavior
        
        :param security: The security to get fill model for
        :returns: The new fill model for this brokerage.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the brokerage's leverage for the specified security
        
        :param security: The security's whose leverage we seek
        :returns: The leverage for the specified security.
        """
        ...

    def get_margin_interest_rate_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IMarginInterestRateModel:
        """
        Gets a new margin interest rate model for the security
        
        :param security: The security to get a margin interest rate model for
        :returns: The margin interest rate model for this brokerage.
        """
        ...

    @overload
    def get_settlement_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        :param security: The security to get a settlement model for
        :returns: The settlement model for this brokerage.
        """
        ...

    @overload
    def get_settlement_model(self, security: QuantConnect.Securities.Security, account_type: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        Flagged deprecated and will remove December 1st 2018
        
        :param security: The security to get a settlement model for
        :param account_type: The account type
        :returns: The settlement model for this brokerage.
        """
        ...

    def get_shortable_provider(self, security: QuantConnect.Securities.Security) -> QuantConnect.Interfaces.IShortableProvider:
        """
        Gets the shortable provider
        
        :returns: Shortable provider.
        """
        ...

    def get_slippage_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        """
        Gets a new slippage model that represents this brokerage's fill slippage behavior
        
        :param security: The security to get a slippage model for
        :returns: The new slippage model for this brokerage.
        """
        ...


class IBrokerageMessageHandler(metaclass=abc.ABCMeta):
    """
    Provides an plugin point to allow algorithms to directly handle the messages
    that come from their brokerage
    """

    def handle_message(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Handles the message
        
        :param message: The message to be handled
        """
        ...

    def handle_order(self, event_args: QuantConnect.Brokerages.NewBrokerageOrderNotificationEventArgs) -> bool:
        """
        Handles a new order placed manually in the brokerage side
        
        :param event_args: The new order event
        :returns: Whether the order should be added to the transaction handler.
        """
        ...


class BrokerageFactory(System.Object, QuantConnect.Interfaces.IBrokerageFactory, metaclass=abc.ABCMeta):
    """Provides a base implementation of IBrokerageFactory that provides a helper for reading data from a job's brokerage data dictionary"""

    @property
    def brokerage_type(self) -> typing.Type:
        """Gets the type of brokerage produced by this factory"""
        ...

    @property
    @abc.abstractmethod
    def brokerage_data(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Gets the brokerage data required to run the brokerage from configuration/disk"""
        ...

    def __init__(self, brokerageType: typing.Type) -> None:
        """
        Initializes a new instance of the BrokerageFactory class for the specified
        
        This method is protected.
        
        :param brokerageType: The type of brokerage created by this factory
        """
        ...

    def create_brokerage(self, job: QuantConnect.Packets.LiveNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Interfaces.IBrokerage:
        """
        Creates a new IBrokerage instance
        
        :param job: The job packet to create the brokerage for
        :param algorithm: The algorithm instance
        :returns: A new brokerage instance.
        """
        ...

    def create_brokerage_message_handler(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi) -> QuantConnect.Brokerages.IBrokerageMessageHandler:
        """Gets a brokerage message handler"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def get_brokerage_model(self, order_provider: QuantConnect.Securities.IOrderProvider) -> QuantConnect.Brokerages.IBrokerageModel:
        """
        Gets a brokerage model that can be used to model this brokerage's unique behaviors
        
        :param order_provider: The order provider
        """
        ...

    @staticmethod
    def read(brokerage_data: System.Collections.Generic.IReadOnlyDictionary[str, str], key: str, errors: System.Collections.Generic.ICollection[str]) -> QuantConnect_Brokerages_BrokerageFactory_Read_T:
        """
        Reads a value from the brokerage data, adding an error if the key is not found
        
        This method is protected.
        """
        ...


class BestBidAskUpdatedEventArgs(System.EventArgs):
    """Event arguments class for the DefaultOrderBook.BestBidAskUpdated event"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the new best bid price"""
        ...

    @property
    def best_bid_price(self) -> float:
        """Gets the new best bid price"""
        ...

    @property
    def best_bid_size(self) -> float:
        """Gets the new best bid size"""
        ...

    @property
    def best_ask_price(self) -> float:
        """Gets the new best ask price"""
        ...

    @property
    def best_ask_size(self) -> float:
        """Gets the new best ask size"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], bestBidPrice: float, bestBidSize: float, bestAskPrice: float, bestAskSize: float) -> None:
        """
        Initializes a new instance of the BestBidAskUpdatedEventArgs class
        
        :param symbol: The symbol
        :param bestBidPrice: The newly updated best bid price
        :param bestBidSize: >The newly updated best bid size
        :param bestAskPrice: The newly updated best ask price
        :param bestAskSize: The newly updated best ask size
        """
        ...


class IOrderBookUpdater(typing.Generic[QuantConnect_Brokerages_IOrderBookUpdater_K, QuantConnect_Brokerages_IOrderBookUpdater_V], metaclass=abc.ABCMeta):
    """
    Represents an orderbook updater interface for a security.
    Provides the ability to update orderbook price level and to be alerted about updates
    """

    @property
    @abc.abstractmethod
    def best_bid_ask_updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.BestBidAskUpdatedEventArgs], None], None]:
        """Event fired each time BestBidPrice or BestAskPrice are changed"""
        ...

    def remove_ask_row(self, price: QuantConnect_Brokerages_IOrderBookUpdater_K) -> None:
        """
        Removes an ask price level from the order book
        
        :param price: The ask price level to be removed
        """
        ...

    def remove_bid_row(self, price: QuantConnect_Brokerages_IOrderBookUpdater_K) -> None:
        """
        Removes a bid price level from the order book
        
        :param price: The bid price level to be removed
        """
        ...

    def update_ask_row(self, price: QuantConnect_Brokerages_IOrderBookUpdater_K, size: QuantConnect_Brokerages_IOrderBookUpdater_V) -> None:
        """
        Updates or inserts an ask price level in the order book
        
        :param price: The ask price level to be inserted or updated
        :param size: The new size at the ask price level
        """
        ...

    def update_bid_row(self, price: QuantConnect_Brokerages_IOrderBookUpdater_K, size: QuantConnect_Brokerages_IOrderBookUpdater_V) -> None:
        """
        Updates or inserts a bid price level in the order book
        
        :param price: The bid price level to be inserted or updated
        :param size: The new size at the bid price level
        """
        ...


class DefaultOrderBook(System.Object, QuantConnect.Brokerages.IOrderBookUpdater[float, float]):
    """
    Represents a full order book for a security.
    It contains prices and order sizes for each bid and ask level.
    The best bid and ask prices are also kept up to date.
    """

    @property
    def bids(self) -> System.Collections.Generic.SortedDictionary[float, float]:
        """
        Represents bid prices and sizes
        
        This property is protected.
        """
        ...

    @property
    def asks(self) -> System.Collections.Generic.SortedDictionary[float, float]:
        """
        Represents ask prices and sizes
        
        This property is protected.
        """
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Represents a unique security identifier of current Order Book"""
        ...

    @property
    def best_bid_ask_updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.BestBidAskUpdatedEventArgs], None], None]:
        """Event fired each time BestBidPrice or BestAskPrice are changed"""
        ...

    @property
    def best_bid_price(self) -> float:
        """The best bid price"""
        ...

    @property
    def best_bid_size(self) -> float:
        """The best bid size"""
        ...

    @property
    def best_ask_price(self) -> float:
        """The best ask price"""
        ...

    @property
    def best_ask_size(self) -> float:
        """The best ask size"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Initializes a new instance of the DefaultOrderBook class
        
        :param symbol: The symbol for the order book
        """
        ...

    def clear(self) -> None:
        """Clears all bid/ask levels and prices."""
        ...

    def remove_ask_row(self, price: float) -> None:
        """
        Removes an ask price level from the order book
        
        :param price: The ask price level to be removed
        """
        ...

    def remove_bid_row(self, price: float) -> None:
        """
        Removes a bid price level from the order book
        
        :param price: The bid price level to be removed
        """
        ...

    def remove_price_level(self, price_level: float) -> None:
        """Common price level removal method"""
        ...

    def update_ask_row(self, price: float, size: float) -> None:
        """
        Updates or inserts an ask price level in the order book
        
        :param price: The ask price level to be inserted or updated
        :param size: The new size at the ask price level
        """
        ...

    def update_bid_row(self, price: float, size: float) -> None:
        """
        Updates or inserts a bid price level in the order book
        
        :param price: The bid price level to be inserted or updated
        :param size: The new size at the bid price level
        """
        ...


class BrokerageException(System.Exception):
    """Represents an error retuned from a broker's server"""

    @overload
    def __init__(self, message: str) -> None:
        """
        Creates a new BrokerageException with the specified message.
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        """
        Creates a new BrokerageException with the specified message.
        
        :param message: The error message that explains the reason for the exception.
        :param inner: The exception that is the cause of the current exception, or a null reference (Nothing in Visual Basic) if no inner exception is specified.
        """
        ...


class BrokerageMultiWebSocketSubscriptionManager(QuantConnect.Data.EventBasedDataQueueHandlerSubscriptionManager, System.IDisposable):
    """Handles brokerage data subscriptions with multiple websocket connections, with optional symbol weighting"""

    def __init__(self, webSocketUrl: str, maximumSymbolsPerWebSocket: int, maximumWebSocketConnections: int, symbolWeights: System.Collections.Generic.Dictionary[QuantConnect.Symbol, int], webSocketFactory: typing.Callable[[], QuantConnect.Brokerages.WebSocketClientWrapper], subscribeFunc: typing.Callable[[QuantConnect.Brokerages.IWebSocket, QuantConnect.Symbol], bool], unsubscribeFunc: typing.Callable[[QuantConnect.Brokerages.IWebSocket, QuantConnect.Symbol], bool], messageHandler: typing.Callable[[QuantConnect.Brokerages.WebSocketMessage], None], webSocketConnectionDuration: datetime.timedelta, connectionRateLimiter: QuantConnect.Util.RateGate = None) -> None:
        """
        Initializes a new instance of the BrokerageMultiWebSocketSubscriptionManager class
        
        :param webSocketUrl: The URL for websocket connections
        :param maximumSymbolsPerWebSocket: The maximum number of symbols per websocket connection
        :param maximumWebSocketConnections: The maximum number of websocket connections allowed (if zero, symbol weighting is disabled)
        :param symbolWeights: A dictionary for the symbol weights
        :param webSocketFactory: A function which returns a new websocket instance
        :param subscribeFunc: A function which subscribes a symbol
        :param unsubscribeFunc: A function which unsubscribes a symbol
        :param messageHandler: The websocket message handler
        :param webSocketConnectionDuration: The maximum duration of the websocket connection, TimeSpan.Zero for no duration limit
        :param connectionRateLimiter: The rate limiter for creating new websocket connections
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def subscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tick_type: QuantConnect.TickType) -> bool:
        """
        Subscribes to the symbols
        
        This method is protected.
        
        :param symbols: Symbols to subscribe
        :param tick_type: Type of tick data
        """
        ...

    def unsubscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tick_type: QuantConnect.TickType) -> bool:
        """
        Unsubscribes from the symbols
        
        This method is protected.
        
        :param symbols: Symbols to subscribe
        :param tick_type: Type of tick data
        """
        ...


class IConnectionHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Provides handling of a brokerage or data feed connection"""

    @property
    @abc.abstractmethod
    def connection_lost(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event that fires when a connection loss is detected"""
        ...

    @property
    @abc.abstractmethod
    def connection_restored(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event that fires when a lost connection is restored"""
        ...

    @property
    @abc.abstractmethod
    def reconnect_requested(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event that fires when a reconnection attempt is required"""
        ...

    @property
    @abc.abstractmethod
    def is_connection_lost(self) -> bool:
        """Returns true if the connection has been lost"""
        ...

    def enable_monitoring(self, is_enabled: bool) -> None:
        """
        Enables/disables monitoring of the connection
        
        :param is_enabled: True to enable monitoring, false otherwise
        """
        ...

    def initialize(self, connection_id: str) -> None:
        """
        Initializes the connection handler
        
        :param connection_id: The connection id
        """
        ...

    def keep_alive(self, last_data_received_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Notifies the connection handler that new data was received
        
        :param last_data_received_time: The UTC timestamp of the last data point received
        """
        ...


class DefaultConnectionHandler(System.Object, QuantConnect.Brokerages.IConnectionHandler):
    """
    A default implementation of IConnectionHandler
    which signals disconnection if no data is received for a given time span
    and attempts to reconnect automatically.
    """

    @property
    def connection_lost(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event that fires when a connection loss is detected"""
        ...

    @property
    def connection_restored(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event that fires when a lost connection is restored"""
        ...

    @property
    def reconnect_requested(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event that fires when a reconnection attempt is required"""
        ...

    @property
    def maximum_idle_time_span(self) -> datetime.timedelta:
        """The elapsed time with no received data after which a connection loss is reported"""
        ...

    @property.setter
    def maximum_idle_time_span(self, value: datetime.timedelta) -> None:
        ...

    @property
    def minimum_seconds_for_next_reconnection_attempt(self) -> int:
        """The minimum time in seconds to wait before attempting to reconnect"""
        ...

    @property.setter
    def minimum_seconds_for_next_reconnection_attempt(self, value: int) -> None:
        ...

    @property
    def maximum_seconds_for_next_reconnection_attempt(self) -> int:
        """The maximum time in seconds to wait before attempting to reconnect"""
        ...

    @property.setter
    def maximum_seconds_for_next_reconnection_attempt(self, value: int) -> None:
        ...

    @property
    def connection_id(self) -> str:
        """The unique Id for the connection"""
        ...

    @property
    def is_connection_lost(self) -> bool:
        """Returns true if the connection has been lost"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def enable_monitoring(self, is_enabled: bool) -> None:
        """
        Enables/disables monitoring of the connection
        
        :param is_enabled: True to enable monitoring, false otherwise
        """
        ...

    def initialize(self, connection_id: str) -> None:
        """
        Initializes the connection handler
        
        :param connection_id: The connection id
        """
        ...

    def keep_alive(self, last_data_received_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Notifies the connection handler that new data was received
        
        :param last_data_received_time: The UTC timestamp of the last data point received
        """
        ...

    def on_connection_lost(self) -> None:
        """
        Event invocator for the ConnectionLost event
        
        This method is protected.
        """
        ...

    def on_connection_restored(self) -> None:
        """
        Event invocator for the ConnectionRestored event
        
        This method is protected.
        """
        ...

    def on_reconnect_requested(self) -> None:
        """
        Event invocator for the ReconnectRequested event
        
        This method is protected.
        """
        ...


class DefaultBrokerageModel(System.Object, QuantConnect.Brokerages.IBrokerageModel):
    """
    Provides a default implementation of IBrokerageModel that allows all orders and uses
    the default transaction models
    """

    DEFAULT_MARKET_MAP: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str] = ...
    """The default markets for the backtesting brokerage"""

    @property
    def account_type(self) -> QuantConnect.AccountType:
        """Gets or sets the account type used by this model"""
        ...

    @property
    def required_free_buying_power_percent(self) -> float:
        """
        Gets the brokerages model percentage factor used to determine the required unused buying power for the account.
        From 1 to 0. Example: 0 means no unused buying power is required. 0.5 means 50% of the buying power should be left unused.
        """
        ...

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the DefaultBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to QuantConnect.AccountType.Margin
        """
        ...

    def apply_split(self, tickets: System.Collections.Generic.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        """
        Applies the split to the specified order ticket
        
        :param tickets: The open tickets matching the split event
        :param split: The split event data
        """
        ...

    def can_execute_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not perform
        executions during extended market hours. This is not intended to be checking whether or not
        the exchange is open, that is handled in the Security.Exchange property.
        
        :param security: The security being traded
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    @overload
    def get_buying_power_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        """
        Gets a new buying power model for the security, returning the default model with the security's configured leverage.
        For cash accounts, leverage = 1 is used.
        
        :param security: The security to get a buying power model for
        :returns: The buying power model for this brokerage/security.
        """
        ...

    @overload
    def get_buying_power_model(self, security: QuantConnect.Securities.Security, account_type: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        """
        Gets a new buying power model for the security
        
        Flagged deprecated and will remove December 1st 2018
        
        :param security: The security to get a buying power model for
        :param account_type: The account type
        :returns: The buying power model for this brokerage/security.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_fill_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        """
        Gets a new fill model that represents this brokerage's fill behavior
        
        :param security: The security to get fill model for
        :returns: The new fill model for this brokerage.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the brokerage's leverage for the specified security
        
        :param security: The security's whose leverage we seek
        :returns: The leverage for the specified security.
        """
        ...

    def get_margin_interest_rate_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IMarginInterestRateModel:
        """
        Gets a new margin interest rate model for the security
        
        :param security: The security to get a margin interest rate model for
        :returns: The margin interest rate model for this brokerage.
        """
        ...

    @overload
    def get_settlement_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        :param security: The security to get a settlement model for
        :returns: The settlement model for this brokerage.
        """
        ...

    @overload
    def get_settlement_model(self, security: QuantConnect.Securities.Security, account_type: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        Flagged deprecated and will remove December 1st 2018
        
        :param security: The security to get a settlement model for
        :param account_type: The account type
        :returns: The settlement model for this brokerage.
        """
        ...

    def get_shortable_provider(self, security: QuantConnect.Securities.Security) -> QuantConnect.Interfaces.IShortableProvider:
        """
        Gets the shortable provider
        
        :returns: Shortable provider.
        """
        ...

    def get_slippage_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        """
        Gets a new slippage model that represents this brokerage's fill slippage behavior
        
        :param security: The security to get a slippage model for
        :returns: The new slippage model for this brokerage.
        """
        ...

    @staticmethod
    def is_valid_order_size(security: QuantConnect.Securities.Security, order_quantity: float, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Checks if the order quantity is valid, it means, the order size is bigger than the minimum size allowed
        
        :param security: The security of the order
        :param order_quantity: The quantity of the order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may be invalid
        :returns: True if the order quantity is bigger than the minimum allowed, false otherwise.
        """
        ...


class AlpacaBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides an implementation of the DefaultBrokerageModel specific to Alpaca brokerage."""

    def __init__(self) -> None:
        """Initializes a new instance of the AlpacaBrokerageModel class"""
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested updated to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...


class DefaultBrokerageMessageHandler(System.Object, QuantConnect.Brokerages.IBrokerageMessageHandler):
    """
    Provides a default implementation o IBrokerageMessageHandler that will forward
    messages as follows:
    Information -> IResultHandler.Debug
    Warning     -> IResultHandler.Error && IApi.SendUserEmail
    Error       -> IResultHandler.Error && IAlgorithm.RunTimeError
    """

    @overload
    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, initialDelay: typing.Optional[datetime.timedelta] = None, openThreshold: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the DefaultBrokerageMessageHandler class
        
        :param algorithm: The running algorithm
        :param openThreshold: Defines how long before market open to re-check for brokerage reconnect message
        """
        ...

    @overload
    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi, initialDelay: typing.Optional[datetime.timedelta] = None, openThreshold: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the DefaultBrokerageMessageHandler class
        
        :param algorithm: The running algorithm
        :param job: The job that produced the algorithm
        :param api: The api for the algorithm
        :param openThreshold: Defines how long before market open to re-check for brokerage reconnect message
        """
        ...

    def handle_message(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Handles the message
        
        :param message: The message to be handled
        """
        ...

    def handle_order(self, event_args: QuantConnect.Brokerages.NewBrokerageOrderNotificationEventArgs) -> bool:
        """
        Handles a new order placed manually in the brokerage side
        
        :param event_args: The new order event
        :returns: Whether the order should be added to the transaction handler.
        """
        ...


class InteractiveBrokersBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides properties specific to interactive brokers"""

    DEFAULT_MARKET_MAP: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str] = ...
    """The default markets for the IB brokerage"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the InteractiveBrokersBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Margin
        """
        ...

    def can_execute_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not perform
        executions during extended market hours. This is not intended to be checking whether or not
        the exchange is open, that is handled in the Security.Exchange property.
        
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the brokerage's leverage for the specified security
        
        :param security: The security's whose leverage we seek
        :returns: The leverage for the specified security.
        """
        ...


class WolverineBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Wolverine Brokerage model"""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for Wolverine brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Wolverine does not support update of orders
        
        :param security: Security
        :param order: Order that should be updated
        :param request: Update request
        :param message: Outgoing message
        :returns: Always false as Wolverine does not support update of orders.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides Wolverine fee model
        
        :param security: Security
        :returns: Wolverine fee model.
        """
        ...


class FTXBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """FTX Brokerage model"""

    @property
    def market_name(self) -> str:
        """
        market name
        
        This property is protected.
        """
        ...

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Creates an instance of FTXBrokerageModel class
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Please note that the order's queue priority will be reset, and the order ID of the modified order will be different from that of the original order.
        Also note: this is implemented as cancelling and replacing your order.
        There's a chance that the order meant to be cancelled gets filled and its replacement still gets placed.
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    @staticmethod
    def get_default_markets(market: str) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """
        Returns a readonly dictionary of FTX default markets
        
        This method is protected.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides FTX fee model
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the brokerage's leverage for the specified security
        
        :param security: The security's whose leverage we seek
        :returns: The leverage for the specified security.
        """
        ...


class ZerodhaBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Brokerage Model implementation for Zerodha"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the ZerodhaBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Margin
        """
        ...

    def can_execute_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not perform
        executions during extended market hours. This is not intended to be checking whether or not
        the exchange is open, that is handled in the Security.Exchange property.
        
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """Provides Zerodha fee model"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Zerodha global leverage rule"""
        ...


class EzeBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides Eze specific properties"""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for Eze brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: >If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order update. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage could update the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides Eze fee model
        
        :param security: Security
        :returns: Eze Fee model.
        """
        ...


class FxcmBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides FXCM specific properties"""

    DEFAULT_MARKET_MAP: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str] = ...
    """The default markets for the fxcm brokerage"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the DefaultBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_settlement_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        :param security: The security to get a settlement model for
        :returns: The settlement model for this brokerage.
        """
        ...


class BinanceBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides Binance specific properties"""

    @property
    def base_api_endpoint(self) -> str:
        """
        The base Binance API endpoint URL.
        
        This property is protected.
        """
        ...

    @property
    def market_name(self) -> str:
        """
        Market name
        
        This property is protected.
        """
        ...

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the BinanceBrokerageModel class
        
        :param accountType: The type of account to be modeled, defaults to AccountType.Cash
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Binance does not support update of orders
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: Binance does not support update of orders, so it will always return false.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    @staticmethod
    def get_default_markets(market_name: str) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """
        Returns a readonly dictionary of binance default markets
        
        This method is protected.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """Provides Binance fee model"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Binance global leverage rule"""
        ...


class BinanceUSBrokerageModel(QuantConnect.Brokerages.BinanceBrokerageModel):
    """Provides Binance.US specific properties"""

    @property
    def base_api_endpoint(self) -> str:
        """
        The base Binance Futures API endpoint URL.
        
        This property is protected.
        """
        ...

    @property
    def market_name(self) -> str:
        """
        Market name
        
        This property is protected.
        """
        ...

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the BinanceBrokerageModel class
        
        :param accountType: The type of account to be modeled, defaults to AccountType.Cash
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Binance global leverage rule"""
        ...


class BybitBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides Bybit specific properties"""

    @property
    def market_name(self) -> str:
        """
        Market name
        
        This property is protected.
        """
        ...

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the BybitBrokerageModel class
        
        :param accountType: The type of account to be modeled, defaults to AccountType.Cash
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order update. This takes into account
        order type, security type, and order size limits. Bybit can only update inverse, linear, and option orders
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage could update the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """Provides Bybit fee model"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Bybit global leverage rule"""
        ...

    def get_margin_interest_rate_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IMarginInterestRateModel:
        """
        Gets a new margin interest rate model for the security
        
        :param security: The security to get a margin interest rate model for
        :returns: The margin interest rate model for this brokerage.
        """
        ...

    def is_order_size_large_enough(self, security: QuantConnect.Securities.Security, order_quantity: float) -> bool:
        """
        Returns true if the order size is large enough for the given security.
        
        This method is protected.
        
        :param security: The security of the order
        :param order_quantity: The order quantity
        :returns: True if the order size is large enough, false otherwise.
        """
        ...


class BinanceFuturesBrokerageModel(QuantConnect.Brokerages.BinanceBrokerageModel):
    """Provides Binance Futures specific properties"""

    def __init__(self, accountType: QuantConnect.AccountType) -> None:
        """Creates a new instance"""
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides Binance Futures fee model
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_margin_interest_rate_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IMarginInterestRateModel:
        """
        Gets a new margin interest rate model for the security
        
        :param security: The security to get a margin interest rate model for
        :returns: The margin interest rate model for this brokerage.
        """
        ...


class BrokerageExtensions(System.Object):
    """Provides extension methods for handling brokerage operations."""

    @staticmethod
    def order_crosses_zero(holding_quantity: float, order_quantity: float) -> bool:
        """
        Determines if executing the specified order will cross the zero holdings threshold.
        
        :param holding_quantity: The current quantity of holdings.
        :param order_quantity: The quantity of the order to be evaluated.
        :returns: true if the order will change the holdings from positive to negative or vice versa; otherwise, false.
        """
        ...


class TradeStationBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Represents a brokerage model specific to TradeStation."""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for TradeStation brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        TradeStation support Update Order
        
        :param security: Security
        :param order: Order that should be updated
        :param request: Update request
        :param message: Outgoing message
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides TradeStation fee model
        
        :param security: Security
        :returns: TradeStation fee model.
        """
        ...


class BrokerageName(Enum):
    """Specifices what transaction model and submit/execution rules to use"""

    DEFAULT = 0
    """Transaction and submit/execution rules will be the default as initialized"""

    QUANT_CONNECT_BROKERAGE = ...
    """
    Transaction and submit/execution rules will be the default as initialized
    Alternate naming for default brokerage
    """

    INTERACTIVE_BROKERS_BROKERAGE = 2
    """Transaction and submit/execution rules will use interactive brokers models"""

    TRADIER_BROKERAGE = 3
    """Transaction and submit/execution rules will use tradier models"""

    OANDA_BROKERAGE = 4
    """Transaction and submit/execution rules will use oanda models"""

    FXCM_BROKERAGE = 5
    """Transaction and submit/execution rules will use fxcm models"""

    BITFINEX = 6
    """Transaction and submit/execution rules will use bitfinex models"""

    BINANCE = 7
    """Transaction and submit/execution rules will use binance models"""

    GDAX = 12
    """
    Transaction and submit/execution rules will use gdax models
    
    GDAX brokerage name is deprecated. Use Coinbase instead.
    """

    ALPACA = 9
    """Transaction and submit/execution rules will use alpaca models"""

    ALPHA_STREAMS = 10
    """Transaction and submit/execution rules will use AlphaStream models"""

    ZERODHA = 11
    """Transaction and submit/execution rules will use Zerodha models"""

    SAMCO = 12
    """Transaction and submit/execution rules will use Samco models"""

    ATREYU = 13
    """Transaction and submit/execution rules will use atreyu models"""

    TRADING_TECHNOLOGIES = 14
    """Transaction and submit/execution rules will use TradingTechnologies models"""

    KRAKEN = 15
    """Transaction and submit/execution rules will use Kraken models"""

    FTX = 16
    """Transaction and submit/execution rules will use ftx models"""

    FTXUS = 17
    """Transaction and submit/execution rules will use ftx us models"""

    EXANTE = 18
    """Transaction and submit/execution rules will use Exante models"""

    BINANCE_US = 19
    """Transaction and submit/execution rules will use Binance.US models"""

    WOLVERINE = 20
    """Transaction and submit/execution rules will use Wolverine models"""

    TD_AMERITRADE = 21
    """Transaction and submit/execution rules will use TDameritrade models"""

    BINANCE_FUTURES = 22
    """Binance Futures USDⓈ-Margined contracts are settled and collateralized in their quote cryptocurrency, USDT or BUSD"""

    BINANCE_COIN_FUTURES = 23
    """Binance Futures COIN-Margined contracts are settled and collateralized in their based cryptocurrency."""

    RBI = 24
    """Transaction and submit/execution rules will use RBI models"""

    BYBIT = 25
    """Transaction and submit/execution rules will use Bybit models"""

    EZE = 26
    """Transaction and submit/execution rules will use Eze models"""

    AXOS = 27
    """Transaction and submit/execution rules will use Axos models"""

    COINBASE = 28
    """Transaction and submit/execution rules will use Coinbase broker's model"""

    TRADE_STATION = 29
    """Transaction and submit/execution rules will use TradeStation models"""

    TERMINAL_LINK = 30
    """Transaction and submit/execution rules will use Terminal link models"""

    CHARLES_SCHWAB = 31
    """Transaction and submit/execution rules will use Charles Schwab models"""


class BrokerageModel(System.Object):
    """Provides factory method for creating an IBrokerageModel from the BrokerageName enum"""

    @staticmethod
    def create(order_provider: QuantConnect.Securities.IOrderProvider, brokerage: QuantConnect.Brokerages.BrokerageName, account_type: QuantConnect.AccountType) -> QuantConnect.Brokerages.IBrokerageModel:
        """
        Creates a new IBrokerageModel for the specified BrokerageName
        
        :param order_provider: The order provider
        :param brokerage: The name of the brokerage
        :param account_type: The account type
        :returns: The model for the specified brokerage.
        """
        ...

    @staticmethod
    def get_brokerage_name(brokerage_model: QuantConnect.Brokerages.IBrokerageModel) -> QuantConnect.Brokerages.BrokerageName:
        """
        Gets the corresponding BrokerageName for the specified IBrokerageModel
        
        :param brokerage_model: The brokerage model
        :returns: The BrokerageName for the specified brokerage model.
        """
        ...


class FTXUSBrokerageModel(QuantConnect.Brokerages.FTXBrokerageModel):
    """FTX.US Brokerage model"""

    @property
    def market_name(self) -> str:
        """
        Market name
        
        This property is protected.
        """
        ...

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Creates an instance of FTXUSBrokerageModel class
        
        :param accountType: Cash or Margin
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides FTX.US fee model
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...


class BinanceCoinFuturesBrokerageModel(QuantConnect.Brokerages.BinanceFuturesBrokerageModel):
    """Provides Binance Coin Futures specific properties"""

    def __init__(self, accountType: QuantConnect.AccountType) -> None:
        """Creates a new instance"""
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides Binance Coin Futures fee model
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...


class CoinbaseBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """
    Represents a brokerage model for interacting with the Coinbase exchange.
    This class extends the default brokerage model.
    """

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the CoinbaseBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Cash
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Evaluates whether exchange will accept order. Will reject order update
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Determines whether the brokerage supports updating an existing order for the specified security.
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: true if the brokerage supports updating orders; otherwise, false.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_buying_power_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        """
        Gets a new buying power model for the security, returning the default model with the security's configured leverage.
        For cash accounts, leverage = 1 is used.
        
        :param security: The security to get a buying power model for
        :returns: The buying power model for this brokerage/security.
        """
        ...

    @staticmethod
    def get_default_markets(market_name: str) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """
        Gets the default markets for different security types, with an option to override the market name for Crypto securities.
        
        This method is protected.
        
        :param market_name: The default market name for Crypto securities.
        :returns: A read-only dictionary where the keys are SecurityType and the values are market names.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """Provides Coinbase fee model"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Coinbase global leverage rule"""
        ...

    def is_order_size_large_enough(self, security: QuantConnect.Securities.Security, order_quantity: float) -> bool:
        """
        Returns true if the order size is large enough for the given security.
        
        This method is protected.
        
        :param security: The security of the order
        :param order_quantity: The order quantity
        :returns: True if the order size is large enough, false otherwise.
        """
        ...


class BrokerageFactoryAttribute(System.Attribute):
    """Represents the brokerage factory type required to load a data queue handler"""

    @property
    def type(self) -> typing.Type:
        """The type of the brokerage factory"""
        ...

    @property.setter
    def type(self, value: typing.Type) -> None:
        ...

    def __init__(self, type: typing.Type) -> None:
        """
        Creates a new instance of the BrokerageFactoryAttribute class
        
        :param type: The brokerage factory type
        """
        ...


class RBIBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """RBI Brokerage model"""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for RBI brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        RBI supports UpdateOrder
        
        :param security: Security
        :param order: Order that should be updated
        :param request: Update request
        :param message: Outgoing message
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides RBI fee model
        
        :param security: Security
        :returns: RBI fee model.
        """
        ...


class OandaBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Oanda Brokerage Model Implementation for Back Testing."""

    DEFAULT_MARKET_MAP: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str] = ...
    """The default markets for the fxcm brokerage"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the DefaultBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_settlement_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        :param security: The security to get a settlement model for
        :returns: The settlement model for this brokerage.
        """
        ...


class TDAmeritradeBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """TDAmeritrade"""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for TDAmeritrade brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        TDAmeritrade support Update Order
        
        :param security: Security
        :param order: Order that should be updated
        :param request: Update request
        :param message: Outgoing message
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides TDAmeritrade fee model
        
        :param security: Security
        :returns: TDAmeritrade fee model.
        """
        ...


class ExanteBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Exante Brokerage Model Implementation for Back Testing."""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for Exante brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Exante global leverage rule
        
        :param security: The security's whose leverage we seek
        :returns: The leverage for the specified security.
        """
        ...


class DowngradeErrorCodeToWarningBrokerageMessageHandler(System.Object, QuantConnect.Brokerages.IBrokerageMessageHandler):
    """Provides an implementation of IBrokerageMessageHandler that converts specified error codes into warnings"""

    def __init__(self, brokerageMessageHandler: QuantConnect.Brokerages.IBrokerageMessageHandler, errorCodesToIgnore: typing.List[str]) -> None:
        """
        Initializes a new instance of the DowngradeErrorCodeToWarningBrokerageMessageHandler class
        
        :param brokerageMessageHandler: The brokerage message handler to be wrapped
        :param errorCodesToIgnore: The error codes to convert to warning messages
        """
        ...

    def handle_message(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Handles the message
        
        :param message: The message to be handled
        """
        ...

    def handle_order(self, event_args: QuantConnect.Brokerages.NewBrokerageOrderNotificationEventArgs) -> bool:
        """
        Handles a new order placed manually in the brokerage side
        
        :param event_args: The new order event
        :returns: Whether the order should be added to the transaction handler.
        """
        ...


class AxosClearingBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides the Axos clearing brokerage model specific properties"""

    DEFAULT_MARKET_MAP: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str] = ...
    """The default markets for Trading Technologies"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """Creates a new instance"""
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides Axos fee model
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_shortable_provider(self, security: QuantConnect.Securities.Security) -> QuantConnect.Interfaces.IShortableProvider:
        """
        Gets the shortable provider
        
        :returns: Shortable provider.
        """
        ...


class AlphaStreamsBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides properties specific to Alpha Streams"""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the AlphaStreamsBrokerageModel class
        
        :param accountType: The type of account to be modeled, defaults to AccountType.Margin does not accept AccountType.Cash.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the brokerage's leverage for the specified security
        
        :param security: The security's whose leverage we seek
        :returns: The leverage for the specified security.
        """
        ...

    def get_settlement_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        :param security: The security to get a settlement model for
        :returns: The settlement model for this brokerage.
        """
        ...

    def get_slippage_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        """
        Gets a new slippage model that represents this brokerage's fill slippage behavior
        
        :param security: The security to get a slippage model for
        :returns: The new slippage model for this brokerage.
        """
        ...


class KrakenBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Kraken Brokerage model"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    @property
    def coin_leverage(self) -> System.Collections.Generic.IReadOnlyDictionary[str, float]:
        """Leverage map of different coins"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for Kraken brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Kraken does not support update of orders
        
        :param security: Security
        :param order: Order that should be updated
        :param request: Update request
        :param message: Outgoing message
        :returns: Always false as Kraken does not support update of orders.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides Kraken fee model
        
        :param security: Security
        :returns: Kraken fee model.
        """
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Kraken global leverage rule"""
        ...


class SamcoBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Brokerage Model implementation for Samco"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the SamcoBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Margin
        """
        ...

    def can_execute_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not
        perform executions during extended market hours. This is not intended to be checking
        whether or not the exchange is open, that is handled in the Security.Exchange property.
        
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account order
        type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """Provides Samco fee model"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Samco global leverage rule"""
        ...


class CharlesSchwabBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Represents a brokerage model specific to Charles Schwab."""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Constructor for Charles Schwab brokerage model
        
        :param accountType: Cash or Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Provides TradeStation fee model
        
        :param security: Security
        :returns: TradeStation fee model.
        """
        ...


class TradierBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides tradier specific properties"""

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the DefaultBrokerageModel class
        
        :param accountType: The type of account to be modeled, defaults to QuantConnect.AccountType.Margin
        """
        ...

    def apply_split(self, tickets: System.Collections.Generic.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        """
        Applies the split to the specified order ticket
        
        :param tickets: The open tickets matching the split event
        :param split: The split event data
        """
        ...

    def can_execute_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not perform
        executions during extended market hours. This is not intended to be checking whether or not
        the exchange is open, that is handled in the Security.Exchange property.
        
        :param security: The security being ordered
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...


class TradingTechnologiesBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides properties specific to Trading Technologies"""

    DEFAULT_MARKET_MAP: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str] = ...
    """The default markets for Trading Technologies"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the TradingTechnologiesBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Margin
        """
        ...

    def can_execute_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not perform
        executions during extended market hours. This is not intended to be checking whether or not
        the exchange is open, that is handled in the Security.Exchange property.
        
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested update to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...


class BitfinexBrokerageModel(QuantConnect.Brokerages.DefaultBrokerageModel):
    """Provides Bitfinex specific properties"""

    @property
    def default_markets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the BitfinexBrokerageModel class
        
        :param accountType: The type of account to be modeled, defaults to AccountType.Margin
        """
        ...

    def can_submit_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security of the order
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def can_update_order(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Checks whether an order can be updated or not in the Bitfinex brokerage model
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The update request
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the update requested quantity is valid, false otherwise.
        """
        ...

    def get_benchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    def get_fee_model(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """Provides Bitfinex fee model"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """Bitfinex global leverage rule"""
        ...


class GDAXBrokerageModel(QuantConnect.Brokerages.CoinbaseBrokerageModel):
    """
    Provides GDAX specific properties
    
    GDAXBrokerageModel is deprecated. Use CoinbaseBrokerageModel instead.
    """

    def __init__(self, accountType: QuantConnect.AccountType = ...) -> None:
        """
        Initializes a new instance of the GDAXBrokerageModel class
        
        :param accountType: The type of account to be modelled, defaults to AccountType.Cash
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Brokerages__EventContainer_Callable, QuantConnect_Brokerages__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Brokerages__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Brokerages__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Brokerages__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


