from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.Results
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Orders
import QuantConnect.Securities
import System
import System.Collections.Concurrent
import System.Collections.Generic

QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_Callable = typing.TypeVar("QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_Callable")
QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_ReturnType")


class CancelPendingOrders(System.Object):
    """Class used to keep track of CancelPending orders and their original or updated status"""

    @property
    def get_cancel_pending_orders_size(self) -> int:
        """Amount of CancelPending Orders"""
        ...

    def remove_and_fallback(self, order: QuantConnect.Orders.Order) -> None:
        """
        Removes an order which we failed to cancel and falls back the order Status to previous value
        
        :param order: The order that failed to be canceled
        """
        ...

    def set(self, order_id: int, status: QuantConnect.Orders.OrderStatus) -> None:
        """
        Adds an order which will be canceled and we want to keep track of it Status in case of fallback
        
        :param order_id: The order id
        :param status: The order Status, before the cancel request
        """
        ...

    def update_or_remove(self, order_id: int, new_status: QuantConnect.Orders.OrderStatus) -> None:
        """
        Updates an order that is pending to be canceled.
        
        :param order_id: The id of the order
        :param new_status: The new status of the order. If its OrderStatus.Canceled or OrderStatus.Filled it will be removed
        """
        ...


class ITransactionHandler(QuantConnect.Securities.IOrderProcessor, QuantConnect.Securities.IOrderEventProvider, metaclass=abc.ABCMeta):
    """
    Transaction handlers define how the transactions are processed and set the order fill information.
    The pass this information back to the algorithm portfolio and ensure the cash and portfolio are synchronized.
    """

    @property
    @abc.abstractmethod
    def is_active(self) -> bool:
        """
        Boolean flag indicating the thread is busy.
        False indicates it is completely finished processing and ready to be terminated.
        """
        ...

    @property
    @abc.abstractmethod
    def orders(self) -> System.Collections.Concurrent.ConcurrentDictionary[int, QuantConnect.Orders.Order]:
        """Gets the permanent storage for all orders"""
        ...

    @property
    @abc.abstractmethod
    def order_events(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderEvent]:
        """Gets all order events"""
        ...

    @property
    @abc.abstractmethod
    def order_tickets(self) -> System.Collections.Concurrent.ConcurrentDictionary[int, QuantConnect.Orders.OrderTicket]:
        """Gets the permanent storage for all order tickets"""
        ...

    def add_open_order(self, order: QuantConnect.Orders.Order, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """Register an already open Order"""
        ...

    def exit(self) -> None:
        """Signal a end of thread request to stop montioring the transactions."""
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, brokerage: QuantConnect.Interfaces.IBrokerage, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler) -> None:
        """Initializes the transaction handler for the specified algorithm using the specified brokerage implementation"""
        ...

    def process_synchronous_events(self) -> None:
        """Process any synchronous events from the primary algorithm thread."""
        ...


class BrokerageTransactionHandler(System.Object, QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler):
    """Transaction handler for all brokerages"""

    @property
    def _order_request_queue(self) -> QuantConnect.Interfaces.IBusyCollection[QuantConnect.Orders.OrderRequest]:
        """
        OrderQueue holds the newly updated orders from the user algorithm waiting to be processed. Once
        orders are processed they are moved into the Orders queue awaiting the brokerage response.
        
        This property is protected.
        """
        ...

    @property.setter
    def _order_request_queue(self, value: QuantConnect.Interfaces.IBusyCollection[QuantConnect.Orders.OrderRequest]) -> None:
        ...

    @property
    def _cancel_pending_orders(self) -> QuantConnect.Lean.Engine.TransactionHandlers.CancelPendingOrders:
        """
        The _cancelPendingOrders instance will help to keep track of CancelPending orders and their Status
        
        This property is protected.
        """
        ...

    @property
    def new_order_event(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Orders.OrderEvent], None], None]:
        """Event fired when there is a new OrderEvent"""
        ...

    @property
    def orders(self) -> System.Collections.Concurrent.ConcurrentDictionary[int, QuantConnect.Orders.Order]:
        """Gets the permanent storage for all orders"""
        ...

    @property
    def order_events(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderEvent]:
        """Gets all order events"""
        ...

    @property
    def order_tickets(self) -> System.Collections.Concurrent.ConcurrentDictionary[int, QuantConnect.Orders.OrderTicket]:
        """Gets the permanent storage for all order tickets"""
        ...

    @property
    def orders_count(self) -> int:
        """Gets the current number of orders that have been processed"""
        ...

    @property
    def is_active(self) -> bool:
        """
        Boolean flag indicating the Run thread method is busy.
        False indicates it is completely finished processing and ready to be terminated.
        """
        ...

    @property
    def time_since_last_fill(self) -> datetime.timedelta:
        """
        Gets the amount of time since the last call to algorithm.Portfolio.ProcessFill(fill)
        
        This property is protected.
        """
        ...

    @property
    def current_time_utc(self) -> datetime.datetime:
        """
        Gets current time UTC. This is here to facilitate testing
        
        This property is protected.
        """
        ...

    def add_open_order(self, order: QuantConnect.Orders.Order, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """Register an already open Order"""
        ...

    def add_order(self, request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Add an order to collection and return the unique order id or negative if an error.
        
        :param request: A request detailing the order to be submitted
        :returns: New unique, increasing orderid.
        """
        ...

    def cancel_order(self, request: QuantConnect.Orders.CancelOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Remove this order from outstanding queue: user is requesting a cancel.
        
        :param request: Request containing the specific order id to remove
        """
        ...

    def exit(self) -> None:
        """Signal a end of thread request to stop monitoring the transactions."""
        ...

    def get_open_orders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool] = None) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets open orders matching the specified filter
        
        :param filter: Delegate used to filter the orders
        :returns: All open orders this order provider currently holds.
        """
        ...

    def get_open_order_tickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets and enumerable of opened OrderTicket matching the specified
        
        :param filter: The filter predicate used to find the required order tickets
        :returns: An enumerable of opened OrderTicket matching the specified.
        """
        ...

    def get_order_by_id(self, order_id: int) -> QuantConnect.Orders.Order:
        """
        Get the order by its id
        
        :param order_id: Order id to fetch
        :returns: A clone of the order with the specified id, or null if no match is found.
        """
        ...

    def get_orders(self, filter: typing.Callable[[QuantConnect.Orders.Order], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.Order]:
        """
        Gets all orders matching the specified filter. Specifying null will return an enumerable
        of all orders.
        
        :param filter: Delegate used to filter the orders
        :returns: All orders this order provider currently holds by the specified filter.
        """
        ...

    def get_orders_by_brokerage_id(self, brokerage_id: str) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets the order by its brokerage id
        
        :param brokerage_id: The brokerage id to fetch
        :returns: The first order matching the brokerage id, or null if no match is found.
        """
        ...

    def get_order_ticket(self, order_id: int) -> QuantConnect.Orders.OrderTicket:
        """
        Gets the order ticket for the specified order id. Returns null if not found
        
        :param order_id: The order's id
        :returns: The order ticket with the specified id, or null if not found.
        """
        ...

    def get_order_tickets(self, filter: typing.Callable[[QuantConnect.Orders.OrderTicket], bool] = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderTicket]:
        """
        Gets and enumerable of OrderTicket matching the specified
        
        :param filter: The filter predicate used to find the required order tickets
        :returns: An enumerable of OrderTicket matching the specified.
        """
        ...

    def handle_order_request(self, request: QuantConnect.Orders.OrderRequest) -> None:
        """
        Handles a generic order request
        
        :param request: OrderRequest to be handled
        :returns: OrderResponse for request.
        """
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, brokerage: QuantConnect.Interfaces.IBrokerage, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler) -> None:
        """
        Creates a new BrokerageTransactionHandler to process orders using the specified brokerage implementation
        
        :param algorithm: The algorithm instance
        :param brokerage: The brokerage implementation to process orders and fire fill events
        """
        ...

    def initialize_transaction_thread(self) -> None:
        """
        Create and start the transaction thread, who will be in charge of processing
        the order requests
        
        This method is protected.
        """
        ...

    def process(self, request: QuantConnect.Orders.OrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Adds the specified order to be processed
        
        :param request: The order to be processed
        """
        ...

    def process_asynchronous_events(self) -> None:
        """Processes asynchronous events on the transaction handler's thread"""
        ...

    def process_synchronous_events(self) -> None:
        """Processes all synchronous events that must take place before the next time loop for the algorithm"""
        ...

    def round_off_order(self, order: QuantConnect.Orders.Order, security: QuantConnect.Securities.Security) -> float:
        """Rounds off the order towards 0 to the nearest multiple of Lot Size"""
        ...

    @overload
    def round_order_prices(self, order: QuantConnect.Orders.Order, security: QuantConnect.Securities.Security) -> None:
        """
        Rounds the order prices to its security minimum price variation.
        
        This procedure is needed to meet brokerage precision requirements.
        
        This method is protected.
        """
        ...

    @overload
    def round_order_prices(self, order: QuantConnect.Orders.Order, security: QuantConnect.Securities.Security, combo_is_ready: bool, orders: System.Collections.Generic.Dictionary[QuantConnect.Orders.Order, QuantConnect.Securities.Security]) -> None:
        """
        Rounds the order prices to its security minimum price variation.
        
        This procedure is needed to meet brokerage precision requirements.
        
        This method is protected.
        """
        ...

    def run(self) -> None:
        """
        Primary thread entry point to launch the transaction thread.
        
        This method is protected.
        """
        ...

    def update_order(self, request: QuantConnect.Orders.UpdateOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Update an order yet to be filled such as stop or limit orders.
        
        :param request: Request detailing how the order should be updated
        """
        ...

    def wait_for_order_submission(self, ticket: QuantConnect.Orders.OrderTicket) -> None:
        """
        Wait for the order to be handled by the _processingThread
        
        This method is protected.
        
        :param ticket: The OrderTicket expecting to be submitted
        """
        ...


class BacktestingTransactionHandler(QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler):
    """This transaction handler is used for processing transactions during backtests"""

    @property
    def current_time_utc(self) -> datetime.datetime:
        """
        Gets current time UTC. This is here to facilitate testing
        
        This property is protected.
        """
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, brokerage: QuantConnect.Interfaces.IBrokerage, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler) -> None:
        """
        Creates a new BacktestingTransactionHandler using the BacktestingBrokerage
        
        :param algorithm: The algorithm instance
        :param brokerage: The BacktestingBrokerage
        """
        ...

    def initialize_transaction_thread(self) -> None:
        """
        For backtesting order requests will be processed by the algorithm thread
        sequentially at WaitForOrderSubmission and ProcessSynchronousEvents
        
        This method is protected.
        """
        ...

    def process_asynchronous_events(self) -> None:
        """Processes asynchronous events on the transaction handler's thread"""
        ...

    def process_synchronous_events(self) -> None:
        """Processes all synchronous events that must take place before the next time loop for the algorithm"""
        ...

    def wait_for_order_submission(self, ticket: QuantConnect.Orders.OrderTicket) -> None:
        """
        For backtesting we will submit the order ourselves
        
        This method is protected.
        
        :param ticket: The OrderTicket expecting to be submitted
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_Callable, QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Lean_Engine_TransactionHandlers__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


