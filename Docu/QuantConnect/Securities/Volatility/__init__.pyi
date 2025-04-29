from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Interfaces
import QuantConnect.Securities
import QuantConnect.Securities.Volatility
import System
import System.Collections.Generic


class VolatilityModelExtensions(System.Object):
    """Provides extension methods to volatility models"""

    @staticmethod
    @overload
    def warm_up(volatility_model: QuantConnect.Securities.IVolatilityModel, history_provider: QuantConnect.Interfaces.IHistoryProvider, subscription_manager: QuantConnect.Data.SubscriptionManager, security: QuantConnect.Securities.Security, utc_time: typing.Union[datetime.datetime, datetime.date], time_zone: typing.Any, live_mode: bool, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> None:
        """
        Warms up the security's volatility model.
        This can happen either on initialization or after a split or dividend is processed.
        
        :param volatility_model: The volatility model to be warmed up
        :param history_provider: The history provider to use to get historical data
        :param subscription_manager: The subscription manager to use
        :param security: The security which volatility model is being warmed up
        :param utc_time: The current UTC time
        :param time_zone: The algorithm time zone
        :param live_mode: Whether the algorithm is in live mode
        :param data_normalization_mode: The security subscribed data normalization mode
        """
        ...

    @staticmethod
    @overload
    def warm_up(volatility_model: QuantConnect.Securities.IndicatorVolatilityModel, history_provider: QuantConnect.Interfaces.IHistoryProvider, subscription_manager: QuantConnect.Data.SubscriptionManager, security: QuantConnect.Securities.Security, utc_time: typing.Union[datetime.datetime, datetime.date], time_zone: typing.Any, resolution: typing.Optional[QuantConnect.Resolution], bar_count: int, live_mode: bool, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> None:
        """
        Warms up the security's volatility model.
        This can happen either on initialization or after a split or dividend is processed.
        
        :param volatility_model: The volatility model to be warmed up
        :param history_provider: The history provider to use to get historical data
        :param subscription_manager: The subscription manager to use
        :param security: The security which volatility model is being warmed up
        :param utc_time: The current UTC time
        :param time_zone: The algorithm time zone
        :param resolution: The data resolution required for the indicator
        :param bar_count: The bar count required to fully warm the indicator up
        :param live_mode: Whether the algorithm is in live mode
        :param data_normalization_mode: The security subscribed data normalization mode
        """
        ...

    @staticmethod
    @overload
    def warm_up(volatility_model: QuantConnect.Securities.IndicatorVolatilityModel, algorithm: QuantConnect.Interfaces.IAlgorithm, security: QuantConnect.Securities.Security, resolution: typing.Optional[QuantConnect.Resolution], bar_count: int, data_normalization_mode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> None:
        """
        Warms up the security's volatility model.
        This can happen either on initialization or after a split or dividend is processed.
        
        :param volatility_model: The volatility model to be warmed up
        :param algorithm: The algorithm running
        :param security: The security which volatility model is being warmed up
        :param resolution: The data resolution required for the indicator
        :param bar_count: The bar count required to fully warm the indicator up
        :param data_normalization_mode: The security subscribed data normalization mode
        """
        ...


class BaseVolatilityModel(System.Object, QuantConnect.Securities.IVolatilityModel):
    """Represents a base model that computes the volatility of a security"""

    @property
    def subscription_data_config_provider(self) -> QuantConnect.Interfaces.ISubscriptionDataConfigProvider:
        """
        Provides access to registered SubscriptionDataConfig
        
        This property is protected.
        """
        ...

    @property.setter
    def subscription_data_config_provider(self, value: QuantConnect.Interfaces.ISubscriptionDataConfigProvider) -> None:
        ...

    @property
    def volatility(self) -> float:
        """Gets the volatility of the security as a percentage"""
        ...

    @overload
    def get_history_requirements(self, security: QuantConnect.Securities.Security, utc_time: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Returns history requirements for the volatility model expressed in the form of history request
        
        :param security: The security of the request
        :param utc_time: The date/time of the request
        :returns: History request object list, or empty if no requirements.
        """
        ...

    @overload
    def get_history_requirements(self, security: QuantConnect.Securities.Security, utc_time: typing.Union[datetime.datetime, datetime.date], resolution: typing.Optional[QuantConnect.Resolution], bar_count: int) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Gets history requests required for warming up the greeks with the provided resolution
        
        :param security: Security to get history for
        :param utc_time: UTC time of the request (end time)
        :param resolution: Resolution of the security
        :param bar_count: Number of bars to lookback for the start date
        :returns: Enumerable of history requests.
        """
        ...

    def set_subscription_data_config_provider(self, subscription_data_config_provider: QuantConnect.Interfaces.ISubscriptionDataConfigProvider) -> None:
        """
        Sets the ISubscriptionDataConfigProvider instance to use.
        
        :param subscription_data_config_provider: Provides access to registered SubscriptionDataConfig
        """
        ...

    def update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        """
        Updates this model using the new price information in
        the specified security instance
        
        :param security: The security to calculate volatility for
        :param data: The new data used to update the model
        """
        ...


