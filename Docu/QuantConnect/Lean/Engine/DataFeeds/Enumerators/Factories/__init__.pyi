from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.DataFeeds.Enumerators
import QuantConnect.Lean.Engine.DataFeeds.Enumerators.Factories
import QuantConnect.Lean.Engine.Results
import QuantConnect.Securities
import System
import System.Collections.Generic


class OptionChainUniverseSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """Provides an implementation of ISubscriptionEnumeratorFactory for the OptionChainUniverse"""

    def __init__(self, enumeratorConfigurator: typing.Callable[[QuantConnect.Data.UniverseSelection.SubscriptionRequest], System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]], symbolUniverse: QuantConnect.Interfaces.IDataQueueUniverseProvider, timeProvider: QuantConnect.ITimeProvider) -> None:
        """
        Initializes a new instance of the OptionChainUniverseSubscriptionEnumeratorFactory class
        
        :param enumeratorConfigurator: Function used to configure the sub-enumerators before sync (fill-forward/filter/ect...)
        :param symbolUniverse: Symbol universe provider of the data queue
        :param timeProvider: The time provider instance used to determine when bars are completed and can be emitted
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class CorporateEventEnumeratorFactory(System.Object):
    """
    Helper class used to create the corporate event providers
    MappingEventProvider, SplitEventProvider,
    DividendEventProvider, DelistingEventProvider
    """

    @staticmethod
    def create_enumerators(raw_data_enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], config: QuantConnect.Data.SubscriptionDataConfig, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, tradable_day_notifier: QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDatesNotifier, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, start_time: typing.Union[datetime.datetime, datetime.date], end_time: typing.Union[datetime.datetime, datetime.date], enable_price_scaling: bool = True) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates a new AuxiliaryDataEnumerator that will hold the
        corporate event providers
        
        :param raw_data_enumerator: The underlying raw data enumerator
        :param config: The SubscriptionDataConfig
        :param factor_file_provider: Used for getting factor files
        :param tradable_day_notifier: Tradable dates provider
        :param map_file_provider: The MapFile provider to use
        :param start_time: Start date for the data request
        :param end_time: End date for the data request. This will be used for DataNormalizationMode.ScaledRaw data normalization mode to adjust prices to the given end date
        :param enable_price_scaling: Applies price factor
        :returns: The new auxiliary data enumerator.
        """
        ...


class TimeTriggeredUniverseSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory to emit
    ticks based on UserDefinedUniverse.GetTriggerTimes, allowing universe
    selection to fire at planned times.
    """

    def __init__(self, universe: QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase, timeProvider: QuantConnect.ITimeProvider) -> None:
        """
        Initializes a new instance of the TimeTriggeredUniverseSubscriptionEnumeratorFactory class
        
        :param universe: The user defined universe
        :param marketHoursDatabase: The market hours database
        :param timeProvider: The time provider
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class BaseDataCollectionSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory that reads
    an entire SubscriptionDataSource into a single BaseDataCollection
    to be emitted on the tradable date at midnight
    """

    def __init__(self, objectStore: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Instanciates a new BaseDataCollectionSubscriptionEnumeratorFactory
        
        :param objectStore: The object store to use
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class BaseDataSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides a default implementation of ISubscriptionEnumeratorFactory that uses
    BaseData factory methods for reading sources
    """

    def __init__(self, optionChainProvider: QuantConnect.Interfaces.IOptionChainProvider, futureChainProvider: QuantConnect.Interfaces.IFutureChainProvider) -> None:
        """
        Initializes a new instance of the BaseDataSubscriptionEnumeratorFactory class
        
        :param optionChainProvider: The option chain provider
        :param futureChainProvider: The future chain provider
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class LiveCustomDataSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """Provides an implementation of ISubscriptionEnumeratorFactory to handle live custom data."""

    def __init__(self, timeProvider: QuantConnect.ITimeProvider, objectStore: QuantConnect.Interfaces.IObjectStore, dateAdjustment: typing.Callable[[datetime.datetime], datetime.datetime] = None, minimumIntervalCheck: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the LiveCustomDataSubscriptionEnumeratorFactory class
        
        :param timeProvider: Time provider from data feed
        :param objectStore: The object store to use
        :param dateAdjustment: Func that allows adjusting the datetime to use
        :param minimumIntervalCheck: Allows specifying the minimum interval between each enumerator refresh and data check, default is 30 minutes
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request.
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...

    def get_subscription_data_source_reader(self, source: QuantConnect.Data.SubscriptionDataSource, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], base_data_instance: QuantConnect.Data.BaseData, data_provider: QuantConnect.Interfaces.IDataProvider) -> QuantConnect.Lean.Engine.DataFeeds.ISubscriptionDataSourceReader:
        """
        Gets the ISubscriptionDataSourceReader for the specified source
        
        This method is protected.
        """
        ...


class SubscriptionDataReaderSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory, System.IDisposable):
    """Provides an implementation of ISubscriptionEnumeratorFactory that used the SubscriptionDataReader"""

    def __init__(self, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, cacheProvider: QuantConnect.Interfaces.IDataCacheProvider, algorithm: QuantConnect.Interfaces.IAlgorithm, enablePriceScaling: bool = True) -> None:
        """
        Initializes a new instance of the SubscriptionDataReaderSubscriptionEnumeratorFactory class
        
        :param resultHandler: The result handler for the algorithm
        :param mapFileProvider: The map file provider
        :param factorFileProvider: The factor file provider
        :param cacheProvider: Provider used to get data when it is not present on disk
        :param algorithm: The algorithm instance to use
        :param enablePriceScaling: Applies price factor
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates a SubscriptionDataReader to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...


