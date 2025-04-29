from typing import overload
from enum import Enum
import typing

import QuantConnect.Lean.Launcher
import System


class Program(System.Object):
    """This class has no documentation."""

    @staticmethod
    def exit(exit_code: int) -> None:
        ...

    @staticmethod
    def exit_key_press(sender: typing.Any, args: System.ConsoleCancelEventArgs) -> None:
        ...


