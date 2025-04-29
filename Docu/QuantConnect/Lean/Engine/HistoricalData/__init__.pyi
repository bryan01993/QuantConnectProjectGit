from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect.Data
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.HistoricalData
import QuantConnect.Securities
import System.Collections.Generic


class SynchronizingHistoryProvider(QuantConnect.Data.HistoryProviderBase, metaclass=abc.ABCMeta):
    """
    Provides an abstract implementation of IHistoryProvider
    which provides synchronization of multiple history results
    """

    @property
    def algorithm_settings(self) -> QuantConnect.Interfaces.IAlgorithmSettings:
        """The algorithm settings instance to use"""
        ...

    @property.setter
    def algorithm_settings(self, value: QuantConnect.Interfaces.IAlgorithmSettings) -> None:
        ...

    @property
    def data_point_count(self) -> int:
        """Gets the total number of data points emitted by this history provider"""
        ...

    def create_slice_enumerable_from_subscriptions(self, subscriptions: System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.Subscription], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Enumerates the subscriptions into slices
        
        This method is protected.
        """
        ...

    def create_subscription(self, request: QuantConnect.Data.HistoryRequest, history: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a subscription to process the history request
        
        This method is protected.
        """
        ...


class FakeHistoryProvider(QuantConnect.Data.HistoryProviderBase):
    """Provides FAKE implementation of IHistoryProvider used for testing. FakeDataQueue"""

    @property
    def data_point_count(self) -> int:
        """Gets the total number of data points emitted by this history provider"""
        ...

    def get_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param slice_time_zone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
        """
        ...


class HistoryProviderManager(QuantConnect.Data.HistoryProviderBase):
    """
    Provides an implementation of IHistoryProvider which
    acts as a wrapper to use multiple history providers together
    """

    @property
    def data_point_count(self) -> int:
        """Gets the total number of data points emitted by this history provider"""
        ...

    def get_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param slice_time_zone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
        """
        ...

    def set_brokerage(self, brokerage: QuantConnect.Interfaces.IBrokerage) -> None:
        """
        Sets the brokerage to be used for historical requests
        
        :param brokerage: The brokerage instance
        """
        ...


class BrokerageHistoryProvider(QuantConnect.Lean.Engine.HistoricalData.SynchronizingHistoryProvider):
    """
    Provides an implementation of IHistoryProvider that relies on
    a brokerage connection to retrieve historical data
    """

    def get_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param slice_time_zone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
        """
        ...

    def set_brokerage(self, brokerage: QuantConnect.Interfaces.IBrokerage) -> None:
        """
        Sets the brokerage to be used for historical requests
        
        :param brokerage: The brokerage instance
        """
        ...


class SubscriptionDataReaderHistoryProvider(QuantConnect.Lean.Engine.HistoricalData.SynchronizingHistoryProvider):
    """
    Provides an implementation of IHistoryProvider that uses BaseData
    instances to retrieve historical data
    """

    @property
    def data_permission_manager(self) -> QuantConnect.Interfaces.IDataPermissionManager:
        """
        Manager used to allow or deny access to a requested datasource for specific users
        
        This property is protected.
        """
        ...

    @property.setter
    def data_permission_manager(self, value: QuantConnect.Interfaces.IDataPermissionManager) -> None:
        ...

    def get_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param slice_time_zone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def get_intraday_data_enumerator(self, raw_data: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], request: QuantConnect.Data.HistoryRequest) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Gets the intraday data enumerator if any
        
        This method is protected.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
        """
        ...


class SineHistoryProvider(QuantConnect.Data.HistoryProviderBase):
    """Implements a History provider that always return a IEnumerable of Slice with prices following a sine function"""

    @property
    def data_point_count(self) -> int:
        """Gets the total number of data points emitted by this history provider"""
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager) -> None:
        """
        Initializes a new instance of the SineHistoryProvider class
        
        :param securities: Collection of securities that a history request can return
        """
        ...

    def get_history(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], slice_time_zone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param slice_time_zone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
        """
        ...


