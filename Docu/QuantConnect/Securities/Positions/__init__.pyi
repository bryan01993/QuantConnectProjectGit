from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Securities
import QuantConnect.Securities.Option.StrategyMatcher
import QuantConnect.Securities.Positions
import System
import System.Collections.Generic

QuantConnect_Securities_Positions_PositionGroupKey = typing.Any
QuantConnect_Securities_Positions_IPositionGroupBuyingPowerModel = typing.Any


class IPosition(metaclass=abc.ABCMeta):
    """Defines a position for inclusion in a group"""

    @property
    @abc.abstractmethod
    def symbol(self) -> QuantConnect.Symbol:
        """The symbol"""
        ...

    @property
    @abc.abstractmethod
    def quantity(self) -> float:
        """The quantity"""
        ...

    @property
    @abc.abstractmethod
    def unit_quantity(self) -> float:
        """
        The unit quantity. The unit quantities of a group define the group. For example, a covered
        call has 100 units of stock and -1 units of call contracts.
        """
        ...


class IPositionGroup(System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], metaclass=abc.ABCMeta):
    """Defines a group of positions allowing for more efficient use of portfolio margin"""

    @property
    @abc.abstractmethod
    def key(self) -> QuantConnect.Securities.Positions.PositionGroupKey:
        """Gets the key identifying this group"""
        ...

    @property
    @abc.abstractmethod
    def quantity(self) -> float:
        """Gets the whole number of units in this position group"""
        ...

    @property
    @abc.abstractmethod
    def positions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]:
        """Gets the positions in this group"""
        ...

    @property
    @abc.abstractmethod
    def buying_power_model(self) -> QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel:
        """Gets the buying power model defining how margin works in this group"""
        ...

    def try_get_position(self, symbol: typing.Union[QuantConnect.Symbol, str], position: typing.Optional[QuantConnect.Securities.Positions.IPosition]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPosition]:
        """
        Attempts to retrieve the position with the specified symbol
        
        :param symbol: The symbol
        :param position: The position, if found
        :returns: True if the position was found, otherwise false.
        """
        ...


class GetMaximumLotsResult(System.Object):
    """
    Result type for IPositionGroupBuyingPowerModel.GetMaximumLotsForDeltaBuyingPower
    and IPositionGroupBuyingPowerModel.GetMaximumLotsForTargetBuyingPower
    """

    @property
    def number_of_lots(self) -> float:
        """
        Returns the maximum number of lots of the position group that can be
        ordered. This is a whole number and is the IPositionGroup.Quantity
        """
        ...

    @property
    def reason(self) -> str:
        """Returns the reason for which the maximum order quantity is zero"""
        ...

    @property
    def is_error(self) -> bool:
        """Returns true if the zero order quantity is an error condition and will be shown to the user."""
        ...

    @overload
    def __init__(self, numberOfLots: float, reason: str = None) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityResult class
        
        :param numberOfLots: Returns the maximum number of lots of the position group that can be ordered
        :param reason: The reason for which the maximum order quantity is zero
        """
        ...

    @overload
    def __init__(self, numberOfLots: float, reason: str, isError: bool = True) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityResult class
        
        :param numberOfLots: Returns the maximum number of lots of the position group that can be ordered
        :param reason: The reason for which the maximum order quantity is zero
        :param isError: True if the zero order quantity is an error condition
        """
        ...


class GetMaximumLotsForTargetBuyingPowerParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.GetMaximumLotsForTargetBuyingPower"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def target_buying_power(self) -> float:
        """The target buying power."""
        ...

    @property
    def silence_non_error_reasons(self) -> bool:
        """
        True enables the IBuyingPowerModel to skip setting GetMaximumLotsResult.Reason
        for non error situations, for performance
        """
        ...

    @property
    def minimum_order_margin_portfolio_percentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, targetBuyingPower: float, minimumOrderMarginPortfolioPercentage: float, silenceNonErrorReasons: bool = False) -> None:
        """
        Initializes a new instance of the GetMaximumLotsForTargetBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param targetBuyingPower: The target buying power
        :param minimumOrderMarginPortfolioPercentage: Configurable minimum order margin portfolio percentage to ignore orders with unrealistic small sizes
        :param silenceNonErrorReasons: True will not return GetMaximumLotsResult.Reason set for non error situation, this is for performance
        """
        ...

    def error(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an error message."""
        ...

    def result(self, quantity: float) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult for the specified quantity and no message."""
        ...

    @overload
    def zero(self) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and no message."""
        ...

    @overload
    def zero(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an info message."""
        ...


class PositionGroupBuyingPowerParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.GetPositionGroupBuyingPower"""

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def direction(self) -> QuantConnect.Orders.OrderDirection:
        """Gets the direction in which buying power is to be computed"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, direction: QuantConnect.Orders.OrderDirection) -> None:
        """
        Initializes a new instance of the PositionGroupBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param direction: The direction to compute buying power in
        """
        ...


class PositionGroupInitialMarginParameters(System.Object):
    """Defines parameters for IPositionGroupBuyingPowerModel.GetInitialMarginRequirement"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> None:
        """
        Initializes a new instance of the PositionGroupInitialMarginParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        """
        ...


class PositionGroupState(System.Object):
    """Snapshot of a position group state"""

    @property
    def name(self) -> str:
        """Name of this position group"""
        ...

    @property.setter
    def name(self, value: str) -> None:
        ...

    @property
    def margin_used(self) -> float:
        """Currently margin used"""
        ...

    @property.setter
    def margin_used(self, value: float) -> None:
        ...

    @property
    def portfolio_value_percentage(self) -> float:
        """The margin used by this position in relation to the total portfolio value"""
        ...

    @property.setter
    def portfolio_value_percentage(self, value: float) -> None:
        ...

    @property
    def positions(self) -> System.Collections.Generic.List[QuantConnect.Securities.Positions.IPosition]:
        """The positions which compose this group"""
        ...

    @property.setter
    def positions(self, value: System.Collections.Generic.List[QuantConnect.Securities.Positions.IPosition]) -> None:
        ...


class PortfolioState(System.Object):
    """Snapshot of an algorithms portfolio state"""

    @property
    def time(self) -> datetime.datetime:
        """Utc time this portfolio snapshot was taken"""
        ...

    @property.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def total_portfolio_value(self) -> float:
        """The current total portfolio value"""
        ...

    @property.setter
    def total_portfolio_value(self, value: float) -> None:
        ...

    @property
    def total_margin_used(self) -> float:
        """The margin used"""
        ...

    @property.setter
    def total_margin_used(self, value: float) -> None:
        ...

    @property
    def position_groups(self) -> System.Collections.Generic.List[QuantConnect.Securities.Positions.PositionGroupState]:
        """The different positions groups"""
        ...

    @property.setter
    def position_groups(self, value: System.Collections.Generic.List[QuantConnect.Securities.Positions.PositionGroupState]) -> None:
        ...

    @property
    def cash_book(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Gets the cash book that keeps track of all currency holdings (only settled cash)"""
        ...

    @property.setter
    def cash_book(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]) -> None:
        ...

    @property
    def unsettled_cash_book(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Gets the cash book that keeps track of all currency holdings (only unsettled cash)"""
        ...

    @property.setter
    def unsettled_cash_book(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]) -> None:
        ...

    @staticmethod
    def create(portfolio_manager: QuantConnect.Securities.SecurityPortfolioManager, utc_now: typing.Union[datetime.datetime, datetime.date], current_portfolio_value: float) -> QuantConnect.Securities.Positions.PortfolioState:
        """Helper method to create the portfolio state snapshot"""
        ...


class PortfolioMarginChart(System.Object):
    """Helper method to sample portfolio margin chart"""

    @staticmethod
    def add_sample(portfolio_chart: QuantConnect.Chart, portfolio_state: QuantConnect.Securities.Positions.PortfolioState, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, current_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Helper method to add the portfolio margin series into the given chart"""
        ...

    @staticmethod
    def remove_single_point_series(portfolio_chart: QuantConnect.Chart) -> None:
        """Helper method to set the tooltip values after we've sampled and filter series with a single value"""
        ...


class PositionGroupMaintenanceMarginParameters(System.Object):
    """Defines parameters for IPositionGroupBuyingPowerModel.GetMaintenanceMargin"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> None:
        """
        Initializes a new instance of the PositionGroupMaintenanceMarginParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        """
        ...


class PositionGroupInitialMarginForOrderParameters(System.Object):
    """Defines parameters for IPositionGroupBuyingPowerModel.GetInitialMarginRequiredForOrder"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the PositionGroupInitialMarginForOrderParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param order: The order
        """
        ...


class ReservedBuyingPowerImpact(System.Object):
    """
    Specifies the impact on buying power from changing security holdings that affects current IPositionGroup,
    including the current reserved buying power, without the change, and a contemplate reserved buying power, which takes
    into account a contemplated change to the algorithm's positions that impacts current position groups.
    """

    @property
    def current(self) -> float:
        """Gets the current reserved buying power for the impacted groups"""
        ...

    @property
    def contemplated(self) -> float:
        """Gets the reserved buying power for groups resolved after applying a contemplated change to the impacted groups"""
        ...

    @property
    def delta(self) -> float:
        """Gets the change in reserved buying power, Current minus Contemplated"""
        ...

    @property
    def impacted_groups(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]:
        """Gets the impacted groups used as the basis for these reserved buying power numbers"""
        ...

    @property
    def contemplated_changes(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]:
        """Gets the position changes being contemplated"""
        ...

    @property
    def contemplated_groups(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]:
        """Gets the newly resolved groups resulting from applying the contemplated changes to the impacted groups"""
        ...

    def __init__(self, current: float, contemplated: float, impactedGroups: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup], contemplatedChanges: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], contemplatedGroups: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerImpact class
        
        :param current: The current reserved buying power for impacted groups
        :param contemplated: The reserved buying power for impacted groups after applying the contemplated changes
        :param impactedGroups: The groups impacted by the contemplated changes
        :param contemplatedChanges: The position changes being contemplated
        :param contemplatedGroups: The groups resulting from applying the contemplated changes
        """
        ...


class ReservedBuyingPowerImpactParameters(System.Object):
    """Parameters for the IPositionGroupBuyingPowerModel.GetReservedBuyingPowerImpact"""

    @property
    def contemplated_changes(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position changes being contemplated"""
        ...

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """The orders associated with this request"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, contemplatedChanges: QuantConnect.Securities.Positions.IPositionGroup, orders: System.Collections.Generic.List[QuantConnect.Orders.Order]) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerImpactParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param contemplatedChanges: The position changes being contemplated
        :param orders: The orders associated with this request
        """
        ...


class HasSufficientPositionGroupBuyingPowerForOrderParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.HasSufficientBuyingPowerForOrder"""

    @property
    def orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """The orders associated with this request"""
        ...

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group representing the holdings changes contemplated by the order"""
        ...

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, orders: System.Collections.Generic.List[QuantConnect.Orders.Order]) -> None:
        """
        Initializes a new instance of the HasSufficientPositionGroupBuyingPowerForOrderParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param orders: The orders
        """
        ...

    def error(self, reason: str) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there was an error"""
        ...

    def insufficient(self, reason: str) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there is insufficient buying power for the contemplated order"""
        ...

    def sufficient(self) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there is sufficient buying power for the contemplated order"""
        ...


class ReservedBuyingPowerForPositionGroup(System.Object):
    """Defines the result for IBuyingPowerModel.GetReservedBuyingPowerForPosition"""

    @property
    def absolute_used_buying_power(self) -> float:
        """Gets the reserved buying power"""
        ...

    def __init__(self, reservedBuyingPowerForPosition: float) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerForPosition class
        
        :param reservedBuyingPowerForPosition: The reserved buying power for the security's holdings
        """
        ...


class ReservedBuyingPowerForPositionGroupParameters(System.Object):
    """Defines the parameters for IBuyingPowerModel.GetReservedBuyingPowerForPosition"""

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the IPositionGroup"""
        ...

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerForPositionGroupParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        """
        ...


class GetMaximumLotsForDeltaBuyingPowerParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.GetMaximumLotsForDeltaBuyingPower"""

    @property
    def portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def position_group(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def delta_buying_power(self) -> float:
        """The delta buying power."""
        ...

    @property
    def silence_non_error_reasons(self) -> bool:
        """
        True enables the IBuyingPowerModel to skip setting GetMaximumLotsResult.Reason
        for non error situations, for performance
        """
        ...

    @property
    def minimum_order_margin_portfolio_percentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, deltaBuyingPower: float, minimumOrderMarginPortfolioPercentage: float, silenceNonErrorReasons: bool = False) -> None:
        """
        Initializes a new instance of the GetMaximumLotsForDeltaBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param deltaBuyingPower: The delta buying power to apply. Sign defines the position side to apply the delta
        :param minimumOrderMarginPortfolioPercentage: Configurable minimum order margin portfolio percentage to ignore orders with unrealistic small sizes
        :param silenceNonErrorReasons: True will not return GetMaximumLotsResult.Reason set for non error situation, this is for performance
        """
        ...

    def error(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an error message."""
        ...

    def result(self, quantity: float) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult for the specified quantity and no message."""
        ...

    @overload
    def zero(self) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and no message."""
        ...

    @overload
    def zero(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an info message."""
        ...


class PositionGroupBuyingPower(System.Object):
    """Defines the result for IPositionGroupBuyingPowerModel.GetPositionGroupBuyingPower"""

    @property
    def value(self) -> float:
        """Gets the buying power"""
        ...

    def __init__(self, buyingPower: float) -> None:
        """
        Initializes a new instance of the PositionGroupBuyingPower class
        
        :param buyingPower: The buying power
        """
        ...


class IPositionGroupBuyingPowerModel(System.IEquatable[QuantConnect_Securities_Positions_IPositionGroupBuyingPowerModel], metaclass=abc.ABCMeta):
    """Represents a position group's model of buying power"""

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

    def get_maximum_lots_for_delta_buying_power(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForDeltaBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum market position group order quantity to obtain a delta in the buying power used by a position group.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the position group and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_maximum_lots_for_target_buying_power(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForTargetBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum position group order quantity to obtain a position with a given buying power
        percentage. Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the position group and the target     signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_position_group_buying_power(self, parameters: QuantConnect.Securities.Positions.PositionGroupBuyingPowerParameters) -> QuantConnect.Securities.Positions.PositionGroupBuyingPower:
        """
        Gets the buying power available for a position group trade
        
        :param parameters: A parameters object containing the algorithm's portfolio, security, and order direction
        :returns: The buying power available for the trade.
        """
        ...

    def get_reserved_buying_power_for_position_group(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroupParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroup:
        """Computes the amount of buying power reserved by the provided position group"""
        ...

    def get_reserved_buying_power_impact(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerImpactParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerImpact:
        """
        Computes the impact on the portfolio's buying power from adding the position group to the portfolio. This is
        a 'what if' analysis to determine what the state of the portfolio would be if these changes were applied. The
        delta (before - after) is the margin requirement for adding the positions and if the margin used after the changes
        are applied is less than the total portfolio value, this indicates sufficient capital.
        
        :param parameters: An object containing the portfolio and a position group containing the contemplated changes to the portfolio
        :returns: Returns the portfolio's total portfolio value and margin used before and after the position changes are applied.
        """
        ...

    def has_sufficient_buying_power_for_order(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power for the position group to execute this order.
        
        :param parameters: An object containing the portfolio, the position group and the order
        :returns: Returns buying power information for an order against a position group.
        """
        ...


class PositionGroupKey(System.Object, System.IEquatable[QuantConnect_Securities_Positions_PositionGroupKey]):
    """Defines a unique and deterministic key for IPositionGroup"""

    @property
    def is_default_group(self) -> bool:
        """Gets whether or not this key defines a default group"""
        ...

    @property
    def buying_power_model(self) -> QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel:
        """Gets the IPositionGroupBuyingPowerModel being used by the group"""
        ...

    @property
    def unit_quantities(self) -> System.Collections.Generic.IReadOnlyList[System.Tuple[QuantConnect.Symbol, float]]:
        """Gets the unit quantities defining the ratio between position quantities in the group"""
        ...

    @overload
    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes a new instance of the PositionGroupKey class for groups with a single security
        
        :param buyingPowerModel: The group's buying power model
        :param security: The security
        """
        ...

    @overload
    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionGroupKey class
        
        :param buyingPowerModel: The group's buying power model
        :param positions: The positions comprising the group
        """
        ...

    def create_empty_positions(self) -> typing.List[QuantConnect.Securities.Positions.IPosition]:
        """Creates a new array of empty positions with unit quantities according to this key"""
        ...

    @overload
    def equals(self, other: QuantConnect.Securities.Positions.PositionGroupKey) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class PositionGroupBuyingPowerModelExtensions(System.Object):
    """
    Provides methods aimed at reducing the noise introduced from having result/parameter types for each method.
    These methods aim to accept raw arguments and return the desired value type directly.
    """

    @staticmethod
    def get_initial_margin_required_for_order(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group: QuantConnect.Securities.Positions.IPositionGroup, order: QuantConnect.Orders.Order) -> float:
        """Gets the total margin required to execute the specified order in units of the account currency including fees"""
        ...

    @staticmethod
    def get_initial_margin_requirement(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """The margin that must be held in order to change positions by the changes defined by the provided position group"""
        ...

    @staticmethod
    def get_maintenance_margin(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """Gets the margin currently allocated to the specified position group"""
        ...

    @staticmethod
    def get_position_group_buying_power(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group: QuantConnect.Securities.Positions.IPositionGroup, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Securities.Positions.PositionGroupBuyingPower:
        """Gets the buying power available for a position group trade"""
        ...

    @staticmethod
    def get_reserved_buying_power_for_position_group(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """Computes the amount of buying power reserved by the provided position group"""
        ...

    @staticmethod
    def has_sufficient_buying_power_for_order(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group: QuantConnect.Securities.Positions.IPositionGroup, orders: System.Collections.Generic.List[QuantConnect.Orders.Order]) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Check if there is sufficient buying power for the position group to execute this order."""
        ...


class PositionGroupCollection(System.Object, System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup], typing.Iterable[QuantConnect.Securities.Positions.IPositionGroup]):
    """Provides a collection type for IPositionGroup"""

    EMPTY: QuantConnect.Securities.Positions.PositionGroupCollection
    """Gets an empty instance of the PositionGroupCollection class"""

    @property
    def count(self) -> int:
        """Gets the number of positions in this group"""
        ...

    @property
    def is_only_default_groups(self) -> bool:
        """Gets whether or not this collection contains only default position groups"""
        ...

    def __getitem__(self, key: QuantConnect.Securities.Positions.PositionGroupKey) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Gets the IPositionGroup matching the specified key. If one does not exist, then an empty
        group is returned matching the unit quantities defined in the
        
        :param key: The position group key to search for
        :returns: The position group matching the specified key, or a new empty group if no matching group is found.
        """
        ...

    @overload
    def __init__(self, groups: System.Collections.Generic.Dictionary[QuantConnect.Securities.Positions.PositionGroupKey, QuantConnect.Securities.Positions.IPositionGroup], groupsBySymbol: System.Collections.Generic.Dictionary[QuantConnect.Symbol, System.Collections.Generic.HashSet[QuantConnect.Securities.Positions.IPositionGroup]]) -> None:
        """
        Initializes a new instance of the PositionGroupCollection class
        
        :param groups: The position groups keyed by their group key
        :param groupsBySymbol: The position groups keyed by the symbol of each position
        """
        ...

    @overload
    def __init__(self, groups: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]) -> None:
        """
        Initializes a new instance of the PositionGroupCollection class
        
        :param groups: The position groups
        """
        ...

    def add(self, group: QuantConnect.Securities.Positions.IPositionGroup) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Creates a new PositionGroupCollection that contains all of the position groups
        in this collection in addition to the specified . If a group with the
        same key already exists then it is overwritten.
        """
        ...

    def combine_with(self, other: QuantConnect.Securities.Positions.PositionGroupCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """Merges this position group collection with the provided  collection."""
        ...

    def contains(self, key: QuantConnect.Securities.Positions.PositionGroupKey) -> bool:
        """
        Determines whether or not a group with the specified key exists in this collection
        
        :param key: The group key to search for
        :returns: True if a group with the specified key was found, false otherwise.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    def try_get_group(self, key: QuantConnect.Securities.Positions.PositionGroupKey, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to retrieve the group with the specified key
        
        :param key: The group key to search for
        :param group: The position group
        :returns: True if group with key found, otherwise false.
        """
        ...

    def try_get_groups(self, symbol: typing.Union[QuantConnect.Symbol, str], groups: typing.Optional[System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]]) -> typing.Union[bool, System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]]:
        """
        Attempts to retrieve all groups that contain the provided symbol
        
        :param symbol: The symbol
        :param groups: The groups if any were found, otherwise null
        :returns: True if groups were found for the specified symbol, otherwise false.
        """
        ...


class PositionExtensions(System.Object):
    """Provides extension methods for IPosition"""

    @staticmethod
    def combine(position: QuantConnect.Securities.Positions.IPosition, other: QuantConnect.Securities.Positions.IPosition) -> QuantConnect.Securities.Positions.IPosition:
        """
        Combines the provided positions into a single position with the quantities added and the minimum unit quantity.
        
        :param position: The position
        :param other: The other position to add
        :returns: The combined position.
        """
        ...

    @staticmethod
    def consolidate(positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Securities.Positions.IPosition]:
        """
        Consolidates the provided  into a dictionary
        
        :param positions: The positions to be consolidated
        :returns: A dictionary containing the consolidated positions.
        """
        ...

    @staticmethod
    def deduct(position: QuantConnect.Securities.Positions.IPosition, quantity_to_deduct: float) -> QuantConnect.Securities.Positions.IPosition:
        """
        Deducts the specified  from the specified
        
        :param position: The source position
        :param quantity_to_deduct: The quantity to deduct
        :returns: A new position with the same properties but quantity reduced by the specified amount.
        """
        ...

    @staticmethod
    def get_group_quantity(position: QuantConnect.Securities.Positions.IPosition) -> float:
        """
        Gets the quantity a group would have if the given position were part of it.
        
        :param position: The position
        :returns: The group quantity.
        """
        ...

    @staticmethod
    def with_lots(position: QuantConnect.Securities.Positions.IPosition, number_of_lots: float) -> QuantConnect.Securities.Positions.IPosition:
        """
        Creates a new IPosition with quantity equal to  times its unit quantity
        
        :param position: The position
        :param number_of_lots: The number of lots for the new position
        :returns: A new position with the specified number of lots.
        """
        ...


class PositionCollection(System.Object, typing.Iterable[QuantConnect.Securities.Positions.IPosition]):
    """
    Provides a collection type for IPosition aimed at providing indexing for
    common operations required by the resolver implementations.
    """

    @property
    def count(self) -> int:
        """Gets the number of elements in the collection."""
        ...

    @overload
    def __init__(self, positions: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionCollection class
        
        :param positions: The positions to include in this collection
        """
        ...

    @overload
    def __init__(self, positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionCollection class
        
        :param positions: The positions to include in this collection
        """
        ...

    def clear(self) -> None:
        """Clears this collection of all positions"""
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Positions.IPosition]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    def remove(self, groups: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]) -> None:
        """
        Removes the quantities in the provided groups from this position collection.
        This should be called following IPositionGroupResolver has resolved
        position groups in order to update the collection of positions for the next resolver,
        if one exists.
        
        :param groups: The resolved position groups
        """
        ...

    def try_get_position(self, symbol: typing.Union[QuantConnect.Symbol, str], position: typing.Optional[QuantConnect.Securities.Positions.IPosition]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPosition]:
        """
        Attempts to retrieve the position with the specified symbol from this collection
        
        :param symbol: The symbol
        :param position: The position
        :returns: True if the position is found, otherwise false.
        """
        ...


class IPositionGroupResolver(metaclass=abc.ABCMeta):
    """Resolves position groups from a collection of positions."""

    def get_impacted_groups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the position groups that exist within the specified collection of positions.
        
        :param positions: The collection of positions
        :returns: An enumerable of position groups.
        """
        ...

    def try_group(self, new_positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], current_positions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param new_positions: The positions to be grouped
        :param current_positions: The currently grouped positions
        :param group: The grouped positions when this resolver is able to, otherwise null
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class PositionGroupBuyingPowerModel(System.Object, QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, metaclass=abc.ABCMeta):
    """Provides a base class for implementations of IPositionGroupBuyingPowerModel"""

    @property
    def required_free_buying_power_percent(self) -> float:
        """
        Gets the percentage of portfolio buying power to leave as a buffer
        
        This property is protected.
        """
        ...

    def __init__(self, requiredFreeBuyingPowerPercent: float = 0) -> None:
        """
        Initializes a new instance of the PositionGroupBuyingPowerModel class
        
        This method is protected.
        
        :param requiredFreeBuyingPowerPercent: The percentage of portfolio buying power to leave as a buffer
        """
        ...

    @overload
    def equals(self, other: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def get_contemplated_groups_initial_margin(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, contemplated_groups: QuantConnect.Securities.Positions.PositionGroupCollection, orders_positions: System.Collections.Generic.List[QuantConnect.Securities.Positions.IPosition]) -> float:
        """
        Gets the initial margin required for the specified contemplated position group.
        Used by GetReservedBuyingPowerImpact to get the contemplated groups margin.
        
        This method is protected.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
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

    def get_maximum_lots_for_delta_buying_power(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForDeltaBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum market position group order quantity to obtain a delta in the buying power used by a position group.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the position group and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_maximum_lots_for_target_buying_power(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForTargetBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum position group order quantity to obtain a position with a given buying power
        percentage. Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the position group and the target     signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.  Since there is no sense of "short" or "long" on position groups with multiple positions, the sign of the returned quantity will indicate the direction of the order regarding the reference position group passed in the parameters:     - quantity > 0: the order should be placed in the same direction as the reference position group to increase it,                        without changing the positions' signs.     - quantity < 0: the order should be placed in the opposite direction as the reference position group to reduce it,                        using each position's opposite sign.
        """
        ...

    def get_order_fee_in_account_currency(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """
        Helper function to compute the order fees associated with executing market orders for the specified
        
        This method is protected.
        """
        ...

    def get_position_group_buying_power(self, parameters: QuantConnect.Securities.Positions.PositionGroupBuyingPowerParameters) -> QuantConnect.Securities.Positions.PositionGroupBuyingPower:
        """
        Gets the buying power available for a position group trade
        
        :param parameters: A parameters object containing the algorithm's portfolio, security, and order direction
        :returns: The buying power available for the trade.
        """
        ...

    def get_position_group_order_quantity(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, current_position_group: QuantConnect.Securities.Positions.IPositionGroup, current_used_margin: float, target_final_margin: float, group_unit: QuantConnect.Securities.Positions.IPositionGroup, unit_margin: float, final_margin: typing.Optional[float]) -> typing.Union[float, float]:
        """
        Helper method that determines the amount to order to get to a given target safely.
        Meaning it will either be at or just below target always.
        
        :param portfolio: Current portfolio
        :param current_position_group: Current position group
        :param current_used_margin: Current margin reserved for the position
        :param target_final_margin: The target margin
        :param group_unit: Unit position group corresponding to the
        :param unit_margin: Margin required for the
        :param final_margin: Output the final margin allocated for the position group
        :returns: The size of the order to get safely to our target.
        """
        ...

    def get_reserved_buying_power_for_position_group(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroupParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroup:
        """Computes the amount of buying power reserved by the provided position group"""
        ...

    def get_reserved_buying_power_impact(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerImpactParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerImpact:
        """
        Computes the impact on the portfolio's buying power from adding the position group to the portfolio. This is
        a 'what if' analysis to determine what the state of the portfolio would be if these changes were applied. The
        delta (before - after) is the margin requirement for adding the positions and if the margin used after the changes
        are applied is less than the total portfolio value, this indicates sufficient capital.
        
        :param parameters: An object containing the portfolio and a position group containing the contemplated changes to the portfolio
        :returns: Returns the portfolio's total portfolio value and margin used before and after the position changes are applied.
        """
        ...

    def has_sufficient_buying_power_for_order(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power for the position group to execute this order.
        
        :param parameters: An object containing the portfolio, the position group and the order
        :returns: Returns buying power information for an order against a position group.
        """
        ...

    def passes_position_group_specific_buying_power_for_order_checks(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters, available_buying_power: float) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Provides a mechanism for derived types to add their own buying power for order checks without needing to
        recompute the available buying power. Implementations should return null if all checks pass and should
        return an instance of HasSufficientBuyingPowerForOrderResult with IsSufficient=false if it
        fails.
        
        This method is protected.
        """
        ...

    def to_account_currency(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, cash: QuantConnect.Securities.CashAmount) -> float:
        """
        Helper function to convert a CashAmount to the account currency
        
        This method is protected.
        """
        ...

    @staticmethod
    def unable_to_converge(current_margin_difference: float, last_margin_difference: float, group_unit: QuantConnect.Securities.Positions.IPositionGroup, portfolio: QuantConnect.Securities.SecurityPortfolioManager, position_group_quantity: float, target_margin: float, current_margin: float, abs_unit_margin: float, error: typing.Optional[System.ArgumentException]) -> typing.Union[bool, System.ArgumentException]:
        """
        Checks if the margin difference is not growing in final margin calculation, just making sure we don't end up in an infinite loop.
        This function was split out to support derived types using the same error message as well as removing the added noise of the check
        and message creation.
        
        This method is protected.
        """
        ...


class SecurityPositionGroupResolver(System.Object, QuantConnect.Securities.Positions.IPositionGroupResolver):
    """Provides an implementation of IPositionGroupResolver that places all positions into a default group of one security."""

    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel) -> None:
        """
        Initializes a new instance of the SecurityPositionGroupResolver class
        
        :param buyingPowerModel: The buying power model to use for created groups
        """
        ...

    def get_impacted_groups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the IPositionGroupResolver.Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the position groups that exist within the specified collection of positions.
        
        :param positions: The collection of positions
        :returns: An enumerable of position groups.
        """
        ...

    def try_group(self, new_positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], current_positions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param new_positions: The positions to be grouped
        :param current_positions: The currently grouped positions
        :param group: The grouped positions when this resolver is able to, otherwise null
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class OptionStrategyPositionGroupResolver(System.Object, QuantConnect.Securities.Positions.IPositionGroupResolver):
    """Class in charge of resolving option strategy groups which will use the OptionStrategyPositionGroupBuyingPowerModel"""

    @overload
    def __init__(self, securities: QuantConnect.Securities.SecurityManager) -> None:
        """Creates the default option strategy group resolver for OptionStrategyDefinitions.AllDefinitions"""
        ...

    @overload
    def __init__(self, securities: QuantConnect.Securities.SecurityManager, strategyMatcherOptions: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions) -> None:
        """
        Creates a custom option strategy group resolver
        
        :param securities: The algorithms securities
        :param strategyMatcherOptions: The option strategy matcher options instance to use
        """
        ...

    def get_impacted_groups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the position groups that exist within the specified collection of positions.
        
        :param positions: The collection of positions
        :returns: An enumerable of position groups.
        """
        ...

    def try_group(self, new_positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], current_positions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param new_positions: The positions to be grouped
        :param current_positions: The currently grouped positions
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class Position(System.Object, QuantConnect.Securities.Positions.IPosition):
    """Defines a quantity of a security's holdings for inclusion in a position group"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """The symbol"""
        ...

    @property
    def quantity(self) -> float:
        """The quantity"""
        ...

    @property
    def unit_quantity(self) -> float:
        """
        The unit quantity. The unit quantities of a group define the group. For example, a covered
        call has 100 units of stock and -1 units of call contracts.
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, unitQuantity: float) -> None:
        """
        Initializes a new instance of the Position class
        
        :param symbol: The symbol
        :param quantity: The quantity
        :param unitQuantity: The position's unit quantity within its group
        """
        ...

    @overload
    def __init__(self, security: QuantConnect.Securities.Security, quantity: typing.Optional[float] = None) -> None:
        """
        Initializes a new instance of the Position class using the security's lot size
        as it's unit quantity. If quantity is null, then the security's holdings quantity is used.
        
        :param security: The security
        :param quantity: The quantity, if null, the security's holdings quantity is used
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class PositionGroup(System.Object, QuantConnect.Securities.Positions.IPositionGroup, typing.Iterable[QuantConnect.Securities.Positions.IPosition]):
    """Provides a default implementation of IPositionGroup"""

    @property
    def count(self) -> int:
        """Gets the number of positions in the group"""
        ...

    @property
    def key(self) -> QuantConnect.Securities.Positions.PositionGroupKey:
        """Gets the key identifying this group"""
        ...

    @property
    def quantity(self) -> float:
        """Gets the whole number of units in this position group"""
        ...

    @property
    def positions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]:
        """Gets the positions in this group"""
        ...

    @property
    def buying_power_model(self) -> QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel:
        """Gets the buying power model defining how margin works in this group"""
        ...

    @overload
    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, quantity: float, *positions: QuantConnect.Securities.Positions.IPosition) -> None:
        """
        Initializes a new instance of the PositionGroup class
        
        :param buyingPowerModel: The buying power model to use for this group
        :param quantity: The group quantity, which must be the ratio of quantity to unit quantity of each position
        :param positions: The positions comprising this group
        """
        ...

    @overload
    def __init__(self, key: QuantConnect.Securities.Positions.PositionGroupKey, quantity: float, *positions: QuantConnect.Securities.Positions.IPosition) -> None:
        """
        Initializes a new instance of the PositionGroup class
        
        :param key: The deterministic key for this group
        :param quantity: The group quantity, which must be the ratio of quantity to unit quantity of each position
        :param positions: The positions comprising this group
        """
        ...

    @overload
    def __init__(self, key: QuantConnect.Securities.Positions.PositionGroupKey, quantity: float, positions: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionGroup class
        
        :param key: The deterministic key for this group
        :param quantity: The group quantity, which must be the ratio of quantity to unit quantity of each position
        :param positions: The positions comprising this group
        """
        ...

    @staticmethod
    def empty(buying_power_model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel) -> QuantConnect.Securities.Positions.PositionGroup:
        """
        Instantiates a default empty position group instance
        
        :param buying_power_model: The buying power model to use for this group
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Positions.IPosition]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def try_get_position(self, symbol: typing.Union[QuantConnect.Symbol, str], position: typing.Optional[QuantConnect.Securities.Positions.IPosition]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPosition]:
        """
        Attempts to retrieve the position with the specified symbol
        
        :param symbol: The symbol
        :param position: The position, if found
        :returns: True if the position was found, otherwise false.
        """
        ...


class CompositePositionGroupResolver(System.Object, QuantConnect.Securities.Positions.IPositionGroupResolver):
    """
    Provides an implementation of IPositionGroupResolver that invokes multiple wrapped implementations
    in succession. Each successive call to IPositionGroupResolver.Resolve will receive
    the remaining positions that have yet to be grouped. Any non-grouped positions are placed into identity groups.
    """

    @property
    def count(self) -> int:
        """Gets the count of registered resolvers"""
        ...

    @overload
    def __init__(self, *resolvers: QuantConnect.Securities.Positions.IPositionGroupResolver) -> None:
        """
        Initializes a new instance of the CompositePositionGroupResolver class
        
        :param resolvers: The position group resolvers to be invoked in order
        """
        ...

    @overload
    def __init__(self, resolvers: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroupResolver]) -> None:
        """
        Initializes a new instance of the CompositePositionGroupResolver class
        
        :param resolvers: The position group resolvers to be invoked in order
        """
        ...

    @overload
    def add(self, resolver: QuantConnect.Securities.Positions.IPositionGroupResolver) -> None:
        """
        Adds the specified  to the end of the list of resolvers. This resolver will run last.
        
        :param resolver: The resolver to be added
        """
        ...

    @overload
    def add(self, resolver: QuantConnect.Securities.Positions.IPositionGroupResolver, index: int) -> None:
        """
        Inserts the specified  into the list of resolvers at the specified index.
        
        :param resolver: The resolver to be inserted
        :param index: The zero based index indicating where to insert the resolver, zero inserts to the beginning of the list making this resolver un first and Count inserts the resolver to the end of the list making this resolver run last
        """
        ...

    def get_impacted_groups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def remove(self, resolver: QuantConnect.Securities.Positions.IPositionGroupResolver) -> bool:
        """
        Removes the specified  from the list of resolvers
        
        :param resolver: The resolver to be removed
        :returns: True if the resolver was removed, false if it wasn't found in the list.
        """
        ...

    def resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the optimal set of IPositionGroup from the provided .
        Implementations are required to deduct grouped positions from the  collection.
        """
        ...

    def try_group(self, new_positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], current_positions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param new_positions: The positions to be grouped
        :param current_positions: The currently grouped positions
        :param group: The grouped positions when this resolver is able to, otherwise null
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class SecurityPositionGroupBuyingPowerModel(QuantConnect.Securities.Positions.PositionGroupBuyingPowerModel):
    """Provides an implementation of IPositionGroupBuyingPowerModel for groups containing exactly one security"""

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

    def get_maximum_lots_for_delta_buying_power(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForDeltaBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum market position group order quantity to obtain a delta in the buying power used by a position group.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the position group and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def get_maximum_lots_for_target_buying_power(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForTargetBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum position group order quantity to obtain a position with a given buying power
        percentage. Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the position group and the target     signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def has_sufficient_buying_power_for_order(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power for the position group to execute this order.
        
        :param parameters: An object containing the portfolio, the position group and the order
        :returns: Returns buying power information for an order against a position group.
        """
        ...

    def passes_position_group_specific_buying_power_for_order_checks(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters, available_buying_power: float) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Additionally check initial margin requirements if the algorithm only has default position groups
        
        This method is protected.
        """
        ...


class SecurityPositionGroupModel(System.Object):
    """Responsible for managing the resolution of position groups for an algorithm"""

    NULL: QuantConnect.Securities.Positions.SecurityPositionGroupModel = ...
    """Gets an implementation of SecurityPositionGroupModel that will not group multiple securities"""

    @property
    def position_group_buying_power_model(self) -> QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel:
        """
        Get's the single security position group buying power model to use
        
        This property is protected.
        """
        ...

    @property
    def groups(self) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """Gets the set of currently resolved position groups"""
        ...

    @property
    def is_only_default_groups(self) -> bool:
        """Gets whether or not the algorithm is using only default position groups"""
        ...

    def __getitem__(self, key: QuantConnect.Securities.Positions.PositionGroupKey) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Gets the IPositionGroup matching the specified . If one is not found,
        then a new empty position group is returned.
        """
        ...

    def create_default_key(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.Positions.PositionGroupKey:
        """Creates a PositionGroupKey for the security's default position group"""
        ...

    def get_impacted_groups(self, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines which position groups could be impacted by changes in the specified positions
        
        :param positions: The positions to be changed
        :returns: All position groups that need to be re-evaluated due to changes in the positions.
        """
        ...

    def get_or_create_default_group(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets or creates the default position group for the specified"""
        ...

    def get_position_group_resolver(self) -> QuantConnect.Securities.Positions.IPositionGroupResolver:
        """
        Get the position group resolver instance to use
        
        This method is protected.
        
        :returns: The position group resolver instance.
        """
        ...

    def initialize(self, securities: QuantConnect.Securities.SecurityManager) -> None:
        """
        Initializes a new instance of the SecurityPositionGroupModel class
        
        :param securities: The algorithm's security manager
        """
        ...

    def resolve_position_groups(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves position groups using the specified collection of positions
        
        :param positions: The positions to be grouped
        :returns: A collection of position groups containing all of the provided positions.
        """
        ...

    def try_create_position_group(self, orders: System.Collections.Generic.List[QuantConnect.Orders.Order], group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Creates a position group for the specified order, pulling
        
        :param orders: The order
        :param group: The resulting position group
        :returns: A new position group matching the provided order.
        """
        ...


class PositionGroupExtensions(System.Object):
    """Provides extension methods for IPositionGroup"""

    @staticmethod
    def closes(final_group: QuantConnect.Securities.Positions.IPositionGroup, initial_group: QuantConnect.Securities.Positions.IPositionGroup) -> bool:
        """
        Checks whether the provided groups are closing/reducing each other, that is, each of their positions are in opposite sides.
        
        :param final_group: The final position group that would result from a trade
        :param initial_group: The initial position group before a trade
        :returns: Whether final resulting position group is a reduction of the initial one.
        """
        ...

    @staticmethod
    def create_unit_group(template: QuantConnect.Securities.Positions.IPositionGroup, position_mananger: QuantConnect.Securities.Positions.SecurityPositionGroupModel) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Creates a new IPositionGroup with each position's quantity equaling it's unit quantity
        
        :param template: The group template
        :returns: A position group with the same position ratios as the template but with the specified group quantity.
        """
        ...

    @staticmethod
    def get_position(group: QuantConnect.Securities.Positions.IPositionGroup, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Positions.IPosition:
        """Gets the position in the  matching the provided"""
        ...

    @staticmethod
    def get_user_friendly_name(group: QuantConnect.Securities.Positions.IPositionGroup) -> str:
        """Gets a user friendly name for the provided"""
        ...

    @staticmethod
    def is_empty(position_group: QuantConnect.Securities.Positions.IPositionGroup) -> bool:
        """
        Determines whether the position group is empty
        
        :param position_group: The position group
        :returns: True if the position group is empty, that is, it has no positions, false otherwise.
        """
        ...

    @staticmethod
    def is_inverted_of(group: QuantConnect.Securities.Positions.IPositionGroup, other: QuantConnect.Securities.Positions.IPositionGroup) -> bool:
        """
        Checks whether the provided groups are in opposite sides, that is, each of their positions are in opposite sides.
        
        :param group: The group to check
        :param other: The group to check against
        :returns: Whether the position groups are the inverted version of each other, that is, contain the same positions each on the opposite side.
        """
        ...

    @staticmethod
    def with_quantity(template: QuantConnect.Securities.Positions.IPositionGroup, group_quantity: float, position_mananger: QuantConnect.Securities.Positions.SecurityPositionGroupModel) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Creates a new IPositionGroup with the specified .
        If the quantity provided equals the template's quantity then the template is returned.
        
        :param template: The group template
        :param group_quantity: The quantity of the new group
        :param position_mananger: The position manager to use to resolve positions
        :returns: A position group with the same position ratios as the template but with the specified group quantity.
        """
        ...


class NullSecurityPositionGroupModel(QuantConnect.Securities.Positions.SecurityPositionGroupModel):
    """
    Responsible for managing the resolution of position groups for an algorithm.
    Will only resolve single position groups
    """

    def get_position_group_resolver(self) -> QuantConnect.Securities.Positions.IPositionGroupResolver:
        """
        Get the position group resolver instance to use
        
        This method is protected.
        
        :returns: The position group resolver instance.
        """
        ...


