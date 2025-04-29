from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.RealTime
import QuantConnect.Lean.Engine.Results
import QuantConnect.Packets
import QuantConnect.Scheduling
import QuantConnect.Securities
import System
import System.Collections.Concurrent
import System.Collections.Generic


class IRealTimeHandler(QuantConnect.Scheduling.IEventSchedule, metaclass=abc.ABCMeta):
    """Real time event handler, trigger functions at regular or pretimed intervals"""

    @property
    @abc.abstractmethod
    def is_active(self) -> bool:
        """Thread status flag."""
        ...

    def exit(self) -> None:
        """Trigger and exit signal to terminate real time event scanner."""
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Event fired each time that we add/remove securities from the data feed"""
        ...

    def scan_past_events(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def set_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the current time for the event scanner (so we can use same code for backtesting and live events)
        
        :param time: Current real or backtest time.
        """
        ...

    def setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolator_limit_provider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """Initializes the real time handler for the specified algorithm and job"""
        ...


class BaseRealTimeHandler(System.Object, QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, metaclass=abc.ABCMeta):
    """
    Base class for the real time handler LiveTradingRealTimeHandler
    and BacktestingRealTimeHandler implementations
    """

    @property
    @abc.abstractmethod
    def is_active(self) -> bool:
        """Thread status flag."""
        ...

    @property
    def scheduled_events(self) -> System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Scheduling.ScheduledEvent, int]:
        """
        The scheduled events container
        
        This property is protected.
        """
        ...

    @property
    def isolator_limit_provider(self) -> QuantConnect.IIsolatorLimitResultProvider:
        """
        The isolator limit result provider instance
        
        This property is protected.
        """
        ...

    @property
    def algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        The algorithm instance
        
        This property is protected.
        """
        ...

    @property
    def time_monitor(self) -> QuantConnect.Scheduling.TimeMonitor:
        """
        The time monitor instance to use
        
        This property is protected.
        """
        ...

    def add(self, scheduled_event: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Adds the specified event to the schedule
        
        :param scheduled_event: The event to be scheduled, including the date/times the event fires and the callback
        """
        ...

    def exit(self) -> None:
        """Stop the real time thread"""
        ...

    def get_scheduled_event_unique_id(self) -> int:
        """
        Gets a new scheduled event unique id
        
        This method is protected.
        """
        ...

    def get_time_monitor_timeout(self) -> int:
        """
        Get's the timeout the scheduled task time monitor should use
        
        This method is protected.
        """
        ...

    def on_securities_changed(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Event fired each time that we add/remove securities from the data feed"""
        ...

    def remove(self, scheduled_event: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Removes the specified event from the schedule
        
        :param scheduled_event: The event to be removed
        """
        ...

    def scan_past_events(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def set_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the current time for the event scanner (so we can use same code for backtesting and live events)
        
        :param time: Current real or backtest time.
        """
        ...

    def setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolator_limit_provider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """
        Initializes the real time handler for the specified algorithm and job.
        Adds EndOfDayEvents
        """
        ...


class ScheduledEventFactory(System.Object):
    """Provides methods for creating common scheduled events"""

    @staticmethod
    def create_event_name(scope: str, name: str) -> str:
        """
        Defines the format of event names generated by this system.
        
        :param scope: The scope of the event, example, 'Algorithm' or 'Security'
        :param name: A name for this specified event in this scope, example, 'EndOfDay'
        :returns: A string representing a fully scoped event name.
        """
        ...

    @staticmethod
    def every_algorithm_end_of_day(algorithm: QuantConnect.Interfaces.IAlgorithm, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], end_of_day_delta: datetime.timedelta, current_utc_time: typing.Optional[datetime.datetime] = None) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Creates a new ScheduledEvent that will fire before market close by the specified time
        
        This method is deprecated. It will generate ScheduledEvents for the deprecated IAlgorithm.OnEndOfDay()
        
        :param algorithm: The algorithm instance the event is fo
        :param result_handler: The result handler, used to communicate run time errors
        :param start: The date to start the events
        :param end: The date to end the events
        :param end_of_day_delta: The time difference between the market close and the event, positive time will fire before market close
        :param current_utc_time: Specfies the current time in UTC, before which, no events will be scheduled. Specify null to skip this filter.
        :returns: The new ScheduledEvent that will fire near market close each tradeable dat.
        """
        warnings.warn("This method is deprecated. It will generate ScheduledEvents for the deprecated IAlgorithm.OnEndOfDay()", DeprecationWarning)

    @staticmethod
    def every_day_at(name: str, dates: System.Collections.Generic.IEnumerable[datetime.datetime], time_of_day: datetime.timedelta, callback: typing.Callable[[str, datetime.datetime], None], current_utc_time: typing.Optional[datetime.datetime] = None) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Creates a new ScheduledEvent that will fire at the specified  for every day in
        
        :param name: An identifier for this event
        :param dates: The dates to set events for at the specified time. These act as a base time to which the  is added to, that is, the implementation does not use .Date before the addition
        :param time_of_day: The time each tradeable date to fire the event
        :param callback: The delegate to call when an event fires
        :param current_utc_time: Specfies the current time in UTC, before which, no events will be scheduled. Specify null to skip this filter.
        :returns: A new ScheduledEvent instance that fires events each tradeable day from the start to the finish at the specified time.
        """
        ...

    @staticmethod
    def every_security_end_of_day(algorithm: QuantConnect.Interfaces.IAlgorithm, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, security: QuantConnect.Securities.Security, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], end_of_day_delta: datetime.timedelta, current_utc_time: typing.Optional[datetime.datetime] = None) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Creates a new ScheduledEvent that will fire before market close by the specified time
        
        :param algorithm: The algorithm instance the event is fo
        :param result_handler: The result handler, used to communicate run time errors
        :param security: The security used for defining tradeable dates
        :param start: The first date for the events
        :param end: The date to end the events
        :param end_of_day_delta: The time difference between the market close and the event, positive time will fire before market close
        :param current_utc_time: Specfies the current time in UTC, before which, no events will be scheduled. Specify null to skip this filter.
        :returns: The new ScheduledEvent that will fire near market close each tradeable dat.
        """
        ...


class BacktestingRealTimeHandler(QuantConnect.Lean.Engine.RealTime.BaseRealTimeHandler):
    """Pseudo realtime event processing for backtesting to simulate realtime events in fast forward."""

    @property
    def is_active(self) -> bool:
        """
        Flag indicating the hander thread is completely finished and ready to dispose.
        this doesn't run as its own thread
        """
        ...

    def add(self, scheduled_event: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Adds the specified event to the schedule
        
        :param scheduled_event: The event to be scheduled, including the date/times the event fires and the callback
        """
        ...

    def remove(self, scheduled_event: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Removes the specified event from the schedule
        
        :param scheduled_event: The event to be removed
        """
        ...

    def scan_past_events(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def set_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the time for the realtime event handler.
        
        :param time: Current time.
        """
        ...

    def setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolator_limit_provider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """Initializes the real time handler for the specified algorithm and job"""
        ...

    @staticmethod
    def sort_first_element(scheduled_events: System.Collections.Generic.IList[QuantConnect.Scheduling.ScheduledEvent]) -> None:
        """
        Sorts the first element of the provided list and supposes the rest of the collection is sorted.
        Supposes the collection has at least 1 element
        """
        ...


class LiveTradingRealTimeHandler(QuantConnect.Lean.Engine.RealTime.BacktestingRealTimeHandler):
    """Live trading realtime event processing."""

    @property
    def market_hours_database(self) -> QuantConnect.Securities.MarketHoursDatabase:
        """
        Gets the current market hours database instance
        
        This property is protected.
        """
        ...

    @property.setter
    def market_hours_database(self, value: QuantConnect.Securities.MarketHoursDatabase) -> None:
        ...

    @property
    def symbol_properties_database(self) -> QuantConnect.Securities.SymbolPropertiesDatabase:
        """
        Gets the current symbol properties database instance
        
        This property is protected.
        """
        ...

    @property.setter
    def symbol_properties_database(self, value: QuantConnect.Securities.SymbolPropertiesDatabase) -> None:
        ...

    @property
    def time_provider(self) -> QuantConnect.ITimeProvider:
        """
        Gets the time provider
        
        This property is protected.
        """
        ...

    @property
    def is_active(self) -> bool:
        """Boolean flag indicating thread state."""
        ...

    def exit(self) -> None:
        """Stop the real time thread"""
        ...

    def get_time_monitor_timeout(self) -> int:
        """
        Get's the timeout the scheduled task time monitor should use
        
        This method is protected.
        """
        ...

    def reset_market_hours_database(self) -> None:
        """
        Resets the market hours database, forcing a reload when reused.
        Called in tests where multiple algorithms are run sequentially,
        and we need to guarantee that every test starts with the same environment.
        
        This method is protected.
        """
        ...

    def reset_symbol_properties_database(self) -> None:
        """
        Resets the symbol properties database, forcing a reload when reused.
        
        This method is protected.
        """
        ...

    def scan_past_events(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def set_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Set the current time. If the date changes re-start the realtime event setup routines."""
        ...

    def setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolator_limit_provider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """Initializes the real time handler for the specified algorithm and job"""
        ...


