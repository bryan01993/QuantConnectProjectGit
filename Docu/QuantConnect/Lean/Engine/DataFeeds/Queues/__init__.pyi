from typing import overload
from enum import Enum
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds.Queues
import QuantConnect.Packets
import System
import System.Collections.Generic


class FakeDataQueue(System.Object, QuantConnect.Interfaces.IDataQueueHandler, QuantConnect.Interfaces.IDataQueueUniverseProvider):
    """This is an implementation of IDataQueueHandler used for testing. FakeHistoryProvider"""

    @property
    def time_provider(self) -> QuantConnect.ITimeProvider:
        """
        Continuous UTC time provider
        
        This property is protected.
        """
        ...

    @property
    def is_connected(self) -> bool:
        """Returns whether the data provider is connected"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the FakeDataQueue class to randomly emit data for each symbol"""
        ...

    @overload
    def __init__(self, dataAggregator: QuantConnect.Data.IDataAggregator, dataPointsPerSecondPerSymbol: int = 500000) -> None:
        """Initializes a new instance of the FakeDataQueue class to randomly emit data for each symbol"""
        ...

    def can_perform_selection(self) -> bool:
        """Checks if the FakeDataQueue can perform selection"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def lookup_symbols(self, symbol: typing.Union[QuantConnect.Symbol, str], include_expired: bool, security_currency: str = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Method returns a collection of Symbols that are available at the data source.
        
        :param symbol: Symbol to lookup
        :param include_expired: Include expired contracts
        :param security_currency: Expected security currency(if any)
        :returns: Enumerable of Symbols, that are associated with the provided Symbol.
        """
        ...

    def set_job(self, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Sets the job we're subscribing for
        
        :param job: Job we're subscribing for
        """
        ...

    def subscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig, new_data_available_handler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Subscribe to the specified configuration
        
        :param data_config: defines the parameters to subscribe to a data feed
        :param new_data_available_handler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def unsubscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Removes the specified configuration
        
        :param data_config: Subscription config to be removed
        """
        ...


class LiveDataQueue(System.Object, QuantConnect.Interfaces.IDataQueueHandler):
    """Live Data Queue is the cut out implementation of how to bind a custom live data source"""

    @property
    def is_connected(self) -> bool:
        """Returns whether the data provider is connected"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def set_job(self, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Sets the job we're subscribing for
        
        :param job: Job we're subscribing for
        """
        ...

    def subscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig, new_data_available_handler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """Desktop/Local doesn't support live data from this handler"""
        ...

    def unsubscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """Desktop/Local doesn't support live data from this handler"""
        ...


