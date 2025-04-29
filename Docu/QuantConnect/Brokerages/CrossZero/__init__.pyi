from typing import overload
from enum import Enum
import QuantConnect.Brokerages.CrossZero
import QuantConnect.Orders
import System


class CrossZeroFirstOrderRequest(System.Object):
    """Represents a first request to cross zero order."""

    @property
    def lean_order(self) -> QuantConnect.Orders.Order:
        """Gets the original lean order."""
        ...

    @property
    def order_type(self) -> QuantConnect.Orders.OrderType:
        """Gets the type of the order."""
        ...

    @property
    def order_quantity(self) -> float:
        """Gets the quantity of the order."""
        ...

    @property
    def absolute_order_quantity(self) -> float:
        """Gets the absolute quantity of the order."""
        ...

    @property
    def order_quantity_holding(self) -> float:
        """Gets the current holding quantity of the order's symbol."""
        ...

    @property
    def order_position(self) -> QuantConnect.Orders.OrderPosition:
        """Gets the position of the order."""
        ...

    def __init__(self, leanOrder: QuantConnect.Orders.Order, orderType: QuantConnect.Orders.OrderType, orderQuantity: float, orderQuantityHolding: float, orderPosition: QuantConnect.Orders.OrderPosition) -> None:
        """
        Initializes a new instance of the CrossZeroFirstOrderRequest struct.
        
        :param leanOrder: The lean order.
        :param orderType: The type of the order.
        :param orderQuantity: The quantity of the order.
        :param orderQuantityHolding: The current holding quantity of the order's symbol.
        :param orderPosition: The position of the order, which depends on the .
        """
        ...


class CrossZeroSecondOrderRequest(QuantConnect.Brokerages.CrossZero.CrossZeroFirstOrderRequest):
    """Represents a second request to cross zero order."""

    @property
    def first_part_cross_zero_order(self) -> QuantConnect.Brokerages.CrossZero.CrossZeroFirstOrderRequest:
        """Gets or sets the first part of CrossZeroOrder."""
        ...

    def __init__(self, leanOrder: QuantConnect.Orders.Order, orderType: QuantConnect.Orders.OrderType, orderQuantity: float, orderQuantityHolding: float, orderPosition: QuantConnect.Orders.OrderPosition, crossZeroFirstOrder: QuantConnect.Brokerages.CrossZero.CrossZeroFirstOrderRequest) -> None:
        """
        Initializes a new instance of the CrossZeroFirstOrderRequest struct.
        
        :param leanOrder: The lean order.
        :param orderType: The type of the order.
        :param orderQuantity: The quantity of the order.
        :param orderQuantityHolding: The current holding quantity of the order's symbol.
        :param orderPosition: The position of the order, which depends on the .
        :param crossZeroFirstOrder: The first part of the cross zero order.
        """
        ...


class CrossZeroOrderResponse:
    """Represents a response for a cross zero order request."""

    @property
    def brokerage_order_id(self) -> str:
        """Gets the brokerage order ID."""
        ...

    @property
    def is_order_placed_successfully(self) -> bool:
        """Gets a value indicating whether the order was placed successfully."""
        ...

    @property
    def message(self) -> str:
        """Gets the message of the order."""
        ...

    def __init__(self, brokerageOrderId: str, isOrderPlacedSuccessfully: bool, message: str = ...) -> None:
        """
        Initializes a new instance of the CrossZeroOrderResponse struct.
        
        :param brokerageOrderId: The brokerage order ID.
        :param isOrderPlacedSuccessfully: if set to true [is order placed successfully].
        :param message: The message of the order. This parameter is optional and defaults to null.
        """
        ...


