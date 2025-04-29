from typing import overload
from enum import Enum
import typing

import QuantConnect.Optimizer
import QuantConnect.Optimizer.Launcher
import QuantConnect.Optimizer.Parameters
import System


class ConsoleLeanOptimizer(QuantConnect.Optimizer.LeanOptimizer):
    """Optimizer implementation that launches Lean as a local process"""

    def __init__(self, nodePacket: QuantConnect.Optimizer.OptimizationNodePacket) -> None:
        """
        Creates a new instance
        
        :param nodePacket: The optimization node packet to handle
        """
        ...

    def abort_lean(self, backtest_id: str) -> None:
        """
        Stops lean process
        
        This method is protected.
        
        :param backtest_id: Specified backtest id
        """
        ...

    def run_lean(self, parameter_set: QuantConnect.Optimizer.Parameters.ParameterSet, backtest_name: str) -> str:
        """
        Handles starting Lean for a given parameter set
        
        This method is protected.
        
        :param parameter_set: The parameter set for the backtest to run
        :param backtest_name: The backtest name to use
        :returns: The new unique backtest id.
        """
        ...

    def send_update(self) -> None:
        """
        Sends an update of the current optimization status to the user
        
        This method is protected.
        """
        ...


class Program(System.Object):
    """This class has no documentation."""

    @staticmethod
    def main(args: typing.List[str]) -> None:
        ...


