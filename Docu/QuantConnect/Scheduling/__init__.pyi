from typing import overload
from enum import Enum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Scheduling
import QuantConnect.Securities
import System
import System.Collections.Generic

QuantConnect_Scheduling__EventContainer_Callable = typing.TypeVar("QuantConnect_Scheduling__EventContainer_Callable")
QuantConnect_Scheduling__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Scheduling__EventContainer_ReturnType")


class BaseScheduleRules(System.Object):
    """Base rule scheduler"""

    @property
    def time_zone(self) -> typing.Any:
        """
        The algorithm's default time zone
        
        This property is protected.
        """
        ...

    @property.setter
    def time_zone(self, value: typing.Any) -> None:
        ...

    @property
    def securities(self) -> QuantConnect.Securities.SecurityManager:
        """
        The security manager
        
        This property is protected.
        """
        ...

    @property.setter
    def securities(self, value: QuantConnect.Securities.SecurityManager) -> None:
        ...

    @property
    def market_hours_database(self) -> QuantConnect.Securities.MarketHoursDatabase:
        """
        The market hours database instance to use
        
        This property is protected.
        """
        ...

    @property.setter
    def market_hours_database(self, value: QuantConnect.Securities.MarketHoursDatabase) -> None:
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: typing.Any, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> None:
        """
        Initializes a new instance of the TimeRules helper class
        
        :param securities: The security manager
        :param timeZone: The algorithm's default time zone
        :param marketHoursDatabase: The market hours database instance to use
        """
        ...

    def get_security_exchange_hours(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.SecurityExchangeHours:
        """
        Helper method to fetch the security exchange hours
        
        This method is protected.
        """
        ...


class IDateRule(metaclass=abc.ABCMeta):
    """Specifies dates that events should be fired, used in conjunction with the ITimeRule"""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Gets a name for this rule"""
        ...

    def get_dates(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Gets the dates produced by this date rule between the specified times
        
        :param start: The start of the interval to produce dates for
        :param end: The end of the interval to produce dates for
        :returns: All dates in the interval matching this date rule.
        """
        ...


class DateRules(QuantConnect.Scheduling.BaseScheduleRules):
    """Helper class used to provide better syntax when defining date rules"""

    @property
    def today(self) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should only fire today in the algorithm's time zone
        using _securities.UtcTime instead of 'start' since ScheduleManager backs it up a day
        """
        ...

    @property
    def tomorrow(self) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should only fire tomorrow in the algorithm's time zone
        using _securities.UtcTime instead of 'start' since ScheduleManager backs it up a day
        """
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: typing.Any, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> None:
        """
        Initializes a new instance of the DateRules helper class
        
        :param securities: The security manager
        :param timeZone: The algorithm's default time zone
        :param marketHoursDatabase: The market hours database instance to use
        """
        ...

    @overload
    def every(self, day: System.DayOfWeek) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on each of the specified days of week
        
        :param day: The day the event should fire
        :returns: A date rule that fires on every specified day of week.
        """
        ...

    @overload
    def every(self, *days: System.DayOfWeek) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on each of the specified days of week
        
        :param days: The days the event should fire
        :returns: A date rule that fires on every specified day of week.
        """
        ...

    @overload
    def every_day(self) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire every day
        
        :returns: A date rule that fires every day.
        """
        ...

    @overload
    def every_day(self, symbol: typing.Union[QuantConnect.Symbol, str], extended_market_hours: bool = False) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire every day the symbol is trading
        
        :param symbol: The symbol whose exchange is used to determine tradable dates
        :param extended_market_hours: True to include days with extended market hours only, like sunday for futures
        :returns: A date rule that fires every day the specified symbol trades.
        """
        ...

    @overload
    def month_end(self, days_offset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last of each month
        
        :param days_offset: The amount of days to offset the schedule by; must be between 0 and 30
        :returns: A date rule that fires on the last of each month - offset.
        """
        ...

    @overload
    def month_end(self, symbol: typing.Union[QuantConnect.Symbol, str], days_offset: int = 0, extended_market_hours: bool = True) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last tradable date - offset for the specified symbol of each month
        
        :param symbol: The symbol whose exchange is used to determine the last tradable date of the month
        :param days_offset: The amount of tradable days to offset the schedule by; must be between 0 and 30.
        :param extended_market_hours: True to include days with extended market hours only, like sunday for futures
        :returns: A date rule that fires on the last tradable date - offset for the specified security each month.
        """
        ...

    @overload
    def month_start(self, days_offset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first of each month + offset
        
        :param days_offset: The amount of days to offset the schedule by; must be between 0 and 30.
        :returns: A date rule that fires on the first of each month + offset.
        """
        ...

    @overload
    def month_start(self, symbol: typing.Union[QuantConnect.Symbol, str], days_offset: int = 0, extended_market_hours: bool = True) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first tradable date + offset for the specified symbol of each month
        
        :param symbol: The symbol whose exchange is used to determine the first tradable date of the month
        :param days_offset: The amount of tradable days to offset the schedule by; must be between 0 and 30
        :param extended_market_hours: True to include days with extended market hours only, like sunday for futures
        :returns: A date rule that fires on the first tradable date + offset for the specified security each month.
        """
        ...

    @overload
    def on(self, year: int, month: int, day: int) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire only on the specified day
        
        :param year: The year
        :param month: The month
        :param day: The day
        """
        ...

    @overload
    def on(self, *dates: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire only on the specified days
        
        :param dates: The dates the event should fire
        """
        ...

    def set_default_time_zone(self, time_zone: typing.Any) -> None:
        """
        Sets the default time zone
        
        :param time_zone: The time zone to use for helper methods that can't resolve a time zone
        """
        ...

    @overload
    def week_end(self, days_offset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on Friday - offset
        
        :param days_offset: The amount of days to offset Friday by; must be between 0 and 6
        :returns: A date rule that fires on Friday each week.
        """
        ...

    @overload
    def week_end(self, symbol: typing.Union[QuantConnect.Symbol, str], days_offset: int = 0, extended_market_hours: bool = True) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last - offset tradable date for the specified
        symbol of each week
        
        :param symbol: The symbol whose exchange is used to determine the last tradable date of the week
        :param days_offset: The amount of tradable days to offset the last tradable day by each week
        :param extended_market_hours: True to include extended market hours, false otherwise
        :returns: A date rule that fires on the last - offset tradable date for the specified security each week.
        """
        ...

    @overload
    def week_start(self, days_offset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on Monday + offset each week
        
        :param days_offset: The amount of days to offset monday by; must be between 0 and 6
        :returns: A date rule that fires on Monday + offset each week.
        """
        ...

    @overload
    def week_start(self, symbol: typing.Union[QuantConnect.Symbol, str], days_offset: int = 0, extended_market_hours: bool = True) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first tradable date + offset for the specified
        symbol each week
        
        :param symbol: The symbol whose exchange is used to determine the first tradeable date of the week
        :param days_offset: The amount of tradable days to offset the first tradable day by
        :param extended_market_hours: True to include extended market hours, false otherwise
        :returns: A date rule that fires on the first + offset tradable date for the specified security each week.
        """
        ...

    @overload
    def year_end(self, days_offset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last of each year
        
        :param days_offset: The amount of days to offset the schedule by; must be between 0 and 365
        :returns: A date rule that fires on the last of each year - offset.
        """
        ...

    @overload
    def year_end(self, symbol: typing.Union[QuantConnect.Symbol, str], days_offset: int = 0, extended_market_hours: bool = True) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last tradable date - offset for the specified symbol of each year
        
        :param symbol: The symbol whose exchange is used to determine the last tradable date of the year
        :param days_offset: The amount of tradable days to offset the schedule by; must be between 0 and 365.
        :param extended_market_hours: True to include days with extended market hours only, like sunday for futures
        :returns: A date rule that fires on the last tradable date - offset for the specified security each year.
        """
        ...

    @overload
    def year_start(self, days_offset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first of each year + offset
        
        :param days_offset: The amount of days to offset the schedule by; must be between 0 and 365.
        :returns: A date rule that fires on the first of each year + offset.
        """
        ...

    @overload
    def year_start(self, symbol: typing.Union[QuantConnect.Symbol, str], days_offset: int = 0, extended_market_hours: bool = True) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first tradable date + offset for the specified symbol of each year
        
        :param symbol: The symbol whose exchange is used to determine the first tradable date of the year
        :param days_offset: The amount of tradable days to offset the schedule by; must be between 0 and 365
        :param extended_market_hours: True to include days with extended market hours only, like sunday for futures
        :returns: A date rule that fires on the first tradable date + offset for the specified security each year.
        """
        ...


class ScheduledEvent(System.Object, System.IDisposable):
    """Real time self scheduling event"""

    SECURITY_END_OF_DAY_DELTA: datetime.timedelta = ...
    """Gets the default time before market close end of trading day events will fire"""

    ALGORITHM_END_OF_DAY_DELTA: datetime.timedelta = ...
    """Gets the default time before midnight end of day events will fire"""

    @property
    def event_fired(self) -> _EventContainer[typing.Callable[[str, datetime.datetime], None], None]:
        """Event that fires each time this scheduled event happens"""
        ...

    @property
    def enabled(self) -> bool:
        """Gets or sets whether this event is enabled"""
        ...

    @property.setter
    def enabled(self, value: bool) -> None:
        ...

    @property
    def next_event_utc_time(self) -> datetime.datetime:
        """Gets the next time this scheduled event will fire in UTC"""
        ...

    @property
    def name(self) -> str:
        """Gets an identifier for this event"""
        ...

    @overload
    def __init__(self, name: str, eventUtcTime: typing.Union[datetime.datetime, datetime.date], callback: typing.Callable[[str, datetime.datetime], None] = None) -> None:
        """
        Initializes a new instance of the ScheduledEvent class
        
        :param name: An identifier for this event
        :param eventUtcTime: The date time the event should fire
        :param callback: Delegate to be called when the event time passes
        """
        ...

    @overload
    def __init__(self, name: str, orderedEventUtcTimes: System.Collections.Generic.IEnumerable[datetime.datetime], callback: typing.Callable[[str, datetime.datetime], None] = None) -> None:
        """
        Initializes a new instance of the ScheduledEvent class
        
        :param name: An identifier for this event
        :param orderedEventUtcTimes: An enumerable that emits event times
        :param callback: Delegate to be called each time an event passes
        """
        ...

    @overload
    def __init__(self, name: str, orderedEventUtcTimes: System.Collections.Generic.IEnumerator[datetime.datetime], callback: typing.Callable[[str, datetime.datetime], None] = None) -> None:
        """
        Initializes a new instance of the ScheduledEvent class
        
        :param name: An identifier for this event
        :param orderedEventUtcTimes: An enumerator that emits event times
        :param callback: Delegate to be called each time an event passes
        """
        ...

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

    def on_event_fired(self, trigger_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Event invocator for the EventFired event
        
        This method is protected.
        
        :param trigger_time: The event's time in UTC
        """
        ...

    def to_string(self) -> str:
        """Will return the ScheduledEvents name"""
        ...


class IEventSchedule(metaclass=abc.ABCMeta):
    """Provides the ability to add/remove scheduled events from the real time handler"""

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


class ITimeRule(metaclass=abc.ABCMeta):
    """Specifies times times on dates for events, used in conjunction with IDateRule"""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Gets a name for this rule"""
        ...

    def create_utc_event_times(self, dates: System.Collections.Generic.IEnumerable[datetime.datetime]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Creates the event times for the specified dates in UTC
        
        :param dates: The dates to apply times to
        :returns: An enumerable of date times that is the result of applying this rule to the specified dates.
        """
        ...


class TimeRules(QuantConnect.Scheduling.BaseScheduleRules):
    """Helper class used to provide better syntax when defining time rules"""

    @property
    def now(self) -> QuantConnect.Scheduling.ITimeRule:
        """Specifies an event should fire at the current time"""
        ...

    @property
    def midnight(self) -> QuantConnect.Scheduling.ITimeRule:
        """Convenience property for running a scheduled event at midnight in the algorithm time zone"""
        ...

    @property
    def noon(self) -> QuantConnect.Scheduling.ITimeRule:
        """Convenience property for running a scheduled event at noon in the algorithm time zone"""
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: typing.Any, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> None:
        """
        Initializes a new instance of the TimeRules helper class
        
        :param securities: The security manager
        :param timeZone: The algorithm's default time zone
        :param marketHoursDatabase: The market hours database instance to use
        """
        ...

    def after_market_close(self, symbol: typing.Union[QuantConnect.Symbol, str], minutes_after_close: float = 0, extended_market_close: bool = False) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the market close +-
        
        :param symbol: The symbol whose market close we want an event for
        :param minutes_after_close: The time after market close that the event should fire
        :param extended_market_close: True to use extended market close, false to use regular market close
        :returns: A time rule that fires the specified number of minutes after the symbol's market close.
        """
        ...

    def after_market_open(self, symbol: typing.Union[QuantConnect.Symbol, str], minutes_after_open: float = 0, extended_market_open: bool = False) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at market open +-
        
        :param symbol: The symbol whose market open we want an event for
        :param minutes_after_open: The minutes after market open that the event should fire
        :param extended_market_open: True to use extended market open, false to use regular market open
        :returns: A time rule that fires the specified number of minutes after the symbol's market open.
        """
        ...

    @overload
    def at(self, time_of_day: datetime.timedelta) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the algorithm's time zone
        
        :param time_of_day: The time of day in the algorithm's time zone the event should fire
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def at(self, hour: int, minute: int, second: int = 0) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the algorithm's time zone
        
        :param hour: The hour
        :param minute: The minute
        :param second: The second
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def at(self, hour: int, minute: int, time_zone: typing.Any) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the specified time zone
        
        :param hour: The hour
        :param minute: The minute
        :param time_zone: The time zone the event time is represented in
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def at(self, hour: int, minute: int, second: int, time_zone: typing.Any) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the specified time zone
        
        :param hour: The hour
        :param minute: The minute
        :param second: The second
        :param time_zone: The time zone the event time is represented in
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def at(self, time_of_day: datetime.timedelta, time_zone: typing.Any) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the specified time zone
        
        :param time_of_day: The time of day in the algorithm's time zone the event should fire
        :param time_zone: The time zone the date time is expressed in
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    def before_market_close(self, symbol: typing.Union[QuantConnect.Symbol, str], minutes_before_close: float = 0, extended_market_close: bool = False) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the market close +-
        
        :param symbol: The symbol whose market close we want an event for
        :param minutes_before_close: The time before market close that the event should fire
        :param extended_market_close: True to use extended market close, false to use regular market close
        :returns: A time rule that fires the specified number of minutes before the symbol's market close.
        """
        ...

    def before_market_open(self, symbol: typing.Union[QuantConnect.Symbol, str], minutes_before_open: float = 0, extended_market_open: bool = False) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at market open +-
        
        :param symbol: The symbol whose market open we want an event for
        :param minutes_before_open: The minutes before market open that the event should fire
        :param extended_market_open: True to use extended market open, false to use regular market open
        :returns: A time rule that fires the specified number of minutes before the symbol's market open.
        """
        ...

    def every(self, interval: datetime.timedelta) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire periodically on the requested interval
        
        :param interval: The frequency with which the event should fire, can not be zero or less
        :returns: A time rule that fires after each interval passes.
        """
        ...

    def set_default_time_zone(self, time_zone: typing.Any) -> None:
        """
        Sets the default time zone
        
        :param time_zone: The time zone to use for helper methods that can't resolve a time zone
        """
        ...


class IFluentSchedulingRunnable(QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier, metaclass=abc.ABCMeta):
    """Specifies the callback component of a scheduled event, as well as final filters"""

    def during_market_hours(self, symbol: typing.Union[QuantConnect.Symbol, str], extended_market: bool = False) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Filters the event times to only include times where the symbol's market is considered open"""
        ...

    @overload
    def run(self, callback: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    @overload
    def run(self, callback: typing.Callable[[datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    @overload
    def run(self, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...


class IFluentSchedulingTimeSpecifier(metaclass=abc.ABCMeta):
    """Specifies the time rule component of a scheduled event"""

    def after_market_open(self, symbol: typing.Union[QuantConnect.Symbol, str], minutes_after_open: float = 0, extended_market_open: bool = False) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire a specified number of minutes after market open"""
        ...

    @overload
    def at(self, hour: int, minute: int, second: int = 0) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def at(self, hour: int, minute: int, time_zone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def at(self, hour: int, minute: int, second: int, time_zone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def at(self, time_of_day: datetime.timedelta, time_zone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def at(self, time_of_day: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specific time of day in the algorithm's time zone"""
        ...

    def before_market_close(self, symbol: typing.Union[QuantConnect.Symbol, str], minute_before_close: float = 0, extended_market_close: bool = False) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire a specified numer of minutes before market close"""
        ...

    def every(self, interval: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire on a period define by the specified interval"""
        ...

    def where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Filters the event times using the predicate"""
        ...


class IFluentSchedulingDateSpecifier(metaclass=abc.ABCMeta):
    """Specifies the date rule component of a scheduled event"""

    def every(self, *days: System.DayOfWeek) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on each of the specified day of week"""
        ...

    @overload
    def every_day(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on every day of the year"""
        ...

    @overload
    def every_day(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on every trading day of the year for the symbol"""
        ...

    @overload
    def month_start(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on the first day of the month"""
        ...

    @overload
    def month_start(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on the first trading day of the month"""
        ...

    @overload
    def on(self, year: int, month: int, day: int) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events only on the specified date"""
        ...

    @overload
    def on(self, *dates: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events only on the specified dates"""
        ...

    def where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Filters the event times using the predicate"""
        ...


class ScheduleManager(System.Object, QuantConnect.Scheduling.IEventSchedule):
    """Provides access to the real time handler's event scheduling feature"""

    @property
    def date_rules(self) -> QuantConnect.Scheduling.DateRules:
        """Gets the date rules helper object to make specifying dates for events easier"""
        ...

    @property
    def time_rules(self) -> QuantConnect.Scheduling.TimeRules:
        """Gets the time rules helper object to make specifying times for events easier"""
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: typing.Any, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase) -> None:
        """
        Initializes a new instance of the ScheduleManager class
        
        :param securities: Securities manager containing the algorithm's securities
        :param timeZone: The algorithm's time zone
        :param marketHoursDatabase: The market hours database instance to use
        """
        ...

    def add(self, scheduled_event: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Adds the specified event to the schedule
        
        :param scheduled_event: The event to be scheduled, including the date/times the event fires and the callback
        """
        ...

    @overload
    def event(self) -> QuantConnect.Scheduling.IFluentSchedulingDateSpecifier:
        """Entry point for the fluent scheduled event builder"""
        ...

    @overload
    def event(self, name: str) -> QuantConnect.Scheduling.IFluentSchedulingDateSpecifier:
        """Entry point for the fluent scheduled event builder"""
        ...

    @overload
    def on(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def on(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, callback: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def on(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def on(self, name: str, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param name: The event's unique name
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def on(self, name: str, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, callback: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param name: The event's unique name
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def on(self, name: str, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param name: The event's unique name
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    def remove(self, scheduled_event: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Removes the specified event from the schedule
        
        :param scheduled_event: The event to be removed
        """
        ...

    @overload
    def training(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, training_code: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the training code to run using the specified date and time rules
        
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param training_code: The training code to be invoked
        """
        ...

    @overload
    def training(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, training_code: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the training code to run using the specified date and time rules
        
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param training_code: The training code to be invoked
        """
        ...

    @overload
    def training(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, training_code: typing.Callable[[datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the training code to run using the specified date and time rules
        
        :param date_rule: Specifies what dates the event should run
        :param time_rule: Specifies the times on those dates the event should run
        :param training_code: The training code to be invoked
        """
        ...

    @overload
    def training_now(self, training_code: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Schedules the provided training code to execute immediately"""
        ...

    @overload
    def training_now(self, training_code: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """Schedules the provided training code to execute immediately"""
        ...


class FuncDateRule(System.Object, QuantConnect.Scheduling.IDateRule):
    """Uses a function to define an enumerable of dates over a requested start/end period"""

    @property
    def name(self) -> str:
        """Gets a name for this rule"""
        ...

    @overload
    def __init__(self, name: str, getDatesFunction: typing.Callable[[datetime.datetime, datetime.datetime], System.Collections.Generic.IEnumerable[datetime.datetime]]) -> None:
        """
        Initializes a new instance of the FuncDateRule class
        
        :param name: The name of this rule
        :param getDatesFunction: The time applicator function
        """
        ...

    @overload
    def __init__(self, name: str, getDatesFunction: typing.Any) -> None:
        """
        Initializes a new instance of the FuncDateRule class using a Python function
        
        :param name: The name of this rule
        :param getDatesFunction: The time applicator function in Python
        """
        ...

    def get_dates(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Gets the dates produced by this date rule between the specified times
        
        :param start: The start of the interval to produce dates for
        :param end: The end of the interval to produce dates for
        :returns: All dates in the interval matching this date rule.
        """
        ...


class TimeConsumer(System.Object):
    """Represents a timer consumer instance"""

    @property
    def finished(self) -> bool:
        """True if the consumer already finished it's work and no longer consumes time"""
        ...

    @property.setter
    def finished(self, value: bool) -> None:
        ...

    @property
    def time_provider(self) -> QuantConnect.ITimeProvider:
        """The time provider associated with this consumer"""
        ...

    @property.setter
    def time_provider(self, value: QuantConnect.ITimeProvider) -> None:
        ...

    @property
    def isolator_limit_provider(self) -> QuantConnect.IIsolatorLimitResultProvider:
        """The isolator limit provider to be used with this consumer"""
        ...

    @property.setter
    def isolator_limit_provider(self, value: QuantConnect.IIsolatorLimitResultProvider) -> None:
        ...

    @property
    def next_time_request(self) -> typing.Optional[datetime.datetime]:
        """
        The next time, base on the TimeProvider, that time should be requested
        to be IsolatorLimitProvider
        """
        ...

    @property.setter
    def next_time_request(self, value: typing.Optional[datetime.datetime]) -> None:
        ...


class TimeMonitor(System.Object, System.IDisposable):
    """
    Helper class that will monitor timer consumers and request more time if required.
    Used by IsolatorLimitResultProvider
    """

    @property
    def time_consumers(self) -> System.Collections.Generic.List[QuantConnect.Scheduling.TimeConsumer]:
        """
        List to store the coming TimeConsumer objects
        
        This property is protected.
        """
        ...

    @property
    def count(self) -> int:
        """Returns the number of time consumers currently being monitored"""
        ...

    def __init__(self, monitorIntervalMs: int = 100) -> None:
        """Creates a new instance"""
        ...

    def add(self, consumer: QuantConnect.Scheduling.TimeConsumer) -> None:
        """
        Adds a new time consumer element to be monitored
        
        :param consumer: Time consumer instance
        """
        ...

    def dispose(self) -> None:
        """Disposes of the inner timer"""
        ...

    def process_consumer(self, consumer: QuantConnect.Scheduling.TimeConsumer) -> None:
        """
        Process the TimeConsumer object in TimeConsumers list
        
        This method is protected.
        
        :param consumer: The TimeConsumer object to be processed
        """
        ...

    def remove_all(self) -> None:
        """
        Remove all TimeConsumer objects where the `Finished` field is marked as true
        
        This method is protected.
        """
        ...


class CompositeTimeRule(System.Object, QuantConnect.Scheduling.ITimeRule):
    """Combines multiple time rules into a single rule that emits for each rule"""

    @property
    def rules(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Scheduling.ITimeRule]:
        """Gets the individual rules for this composite rule"""
        ...

    @property
    def name(self) -> str:
        """Gets a name for this rule"""
        ...

    @overload
    def __init__(self, *timeRules: QuantConnect.Scheduling.ITimeRule) -> None:
        """
        Initializes a new instance of the CompositeTimeRule class
        
        :param timeRules: The time rules to compose
        """
        ...

    @overload
    def __init__(self, timeRules: System.Collections.Generic.IEnumerable[QuantConnect.Scheduling.ITimeRule]) -> None:
        """
        Initializes a new instance of the CompositeTimeRule class
        
        :param timeRules: The time rules to compose
        """
        ...

    def create_utc_event_times(self, dates: System.Collections.Generic.IEnumerable[datetime.datetime]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Creates the event times for the specified dates in UTC
        
        :param dates: The dates to apply times to
        :returns: An enumerable of date times that is the result of applying this rule to the specified dates.
        """
        ...


class FluentScheduledEventBuilder(System.Object, QuantConnect.Scheduling.IFluentSchedulingDateSpecifier, QuantConnect.Scheduling.IFluentSchedulingRunnable):
    """Provides a builder class to allow for fluent syntax when constructing new events"""

    def __init__(self, schedule: QuantConnect.Scheduling.ScheduleManager, securities: QuantConnect.Securities.SecurityManager, name: str = None) -> None:
        """
        Initializes a new instance of the FluentScheduledEventBuilder class
        
        :param schedule: The schedule to send created events to
        :param securities: The algorithm's security manager
        :param name: A specific name for this event
        """
        ...


class ScheduledEventException(System.Exception):
    """Throw this if there is an exception in the callback function of the scheduled event"""

    @property
    def scheduled_event_name(self) -> str:
        """Gets the name of the scheduled event"""
        ...

    def __init__(self, name: str, message: str, innerException: System.Exception) -> None:
        """
        ScheduledEventException constructor
        
        :param name: The name of the scheduled event
        :param message: The exception as a string
        :param innerException: The exception that is the cause of the current exception
        """
        ...


class FuncTimeRule(System.Object, QuantConnect.Scheduling.ITimeRule):
    """Uses a function to define a time rule as a projection of date times to date times"""

    @property
    def name(self) -> str:
        """Gets a name for this rule"""
        ...

    @overload
    def __init__(self, name: str, createUtcEventTimesFunction: typing.Callable[[System.Collections.Generic.IEnumerable[datetime.datetime]], System.Collections.Generic.IEnumerable[datetime.datetime]]) -> None:
        """
        Initializes a new instance of the FuncTimeRule class
        
        :param name: The name of the time rule
        :param createUtcEventTimesFunction: Function used to transform dates into event date times
        """
        ...

    @overload
    def __init__(self, name: str, createUtcEventTimesFunction: typing.Any) -> None:
        """
        Initializes a new instance of the FuncTimeRule class using a Python function
        
        :param name: The name of the time rule
        :param createUtcEventTimesFunction: Function used to transform dates into event date times in Python
        """
        ...

    def create_utc_event_times(self, dates: System.Collections.Generic.IEnumerable[datetime.datetime]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Creates the event times for the specified dates in UTC
        
        :param dates: The dates to apply times to
        :returns: An enumerable of date times that is the result of applying this rule to the specified dates.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Scheduling__EventContainer_Callable, QuantConnect_Scheduling__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Scheduling__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Scheduling__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Scheduling__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


