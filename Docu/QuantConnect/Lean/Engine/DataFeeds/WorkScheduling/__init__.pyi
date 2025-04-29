from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect
import QuantConnect.Lean.Engine.DataFeeds.WorkScheduling
import System


class WorkScheduler(System.Object, metaclass=abc.ABCMeta):
    """Base work scheduler abstraction"""

    workers_count: int = ...
    """The quantity of workers to be used"""

    def queue_work(self, symbol: typing.Union[QuantConnect.Symbol, str], work_func: typing.Callable[[int], bool], weight_func: typing.Callable[[], int]) -> None:
        """
        Add a new work item to the queue
        
        :param symbol: The symbol associated with this work
        :param work_func: The work function to run
        :param weight_func: The weight function. Work will be sorted in ascending order based on this weight
        """
        ...


class WeightedWorkScheduler(QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WorkScheduler):
    """
    This singleton class will create a thread pool to processes work
    that will be prioritized based on it's weight
    """

    WORK_BATCH_SIZE: int = 50
    """This is the size of each work sprint"""

    max_work_weight: int
    """
    This is the maximum size a work item can weigh,
    if reached, it will be ignored and not executed until its less
    """

    INSTANCE: QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WeightedWorkScheduler
    """Singleton instance"""

    def add_single_call_for_all(self, action: typing.Callable[[], None]) -> None:
        """Execute the given action in all workers once"""
        ...

    def queue_work(self, symbol: typing.Union[QuantConnect.Symbol, str], work_func: typing.Callable[[int], bool], weight_func: typing.Callable[[], int]) -> None:
        """
        Add a new work item to the queue
        
        :param symbol: The symbol associated with this work
        :param work_func: The work function to run
        :param weight_func: The weight function. Work will be sorted in ascending order based on this weight
        """
        ...


class WorkItem(System.Object):
    """Class to represent a work item"""

    @property
    def weight(self) -> int:
        """The current weight"""
        ...

    @property
    def work(self) -> typing.Callable[[int], bool]:
        """The work function to execute"""
        ...

    def __init__(self, work: typing.Callable[[int], bool], weightFunc: typing.Callable[[], int]) -> None:
        """
        Creates a new instance
        
        :param work: The work function, takes an int, the amount of work to do and returns a bool, false if this work item is finished
        :param weightFunc: The function used to determine the current weight
        """
        ...

    @staticmethod
    def compare(obj: QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WorkItem, other: QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WorkItem) -> int:
        """Compares two work items based on their weights"""
        ...

    def update_weight(self) -> int:
        """Updates the weight of this work item"""
        ...


