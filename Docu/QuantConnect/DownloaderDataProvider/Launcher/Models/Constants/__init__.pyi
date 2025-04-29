from typing import overload
from enum import Enum
import QuantConnect.DownloaderDataProvider.Launcher.Models.Constants
import System


class DownloaderCommandArguments(System.Object):
    """This class has no documentation."""

    COMMAND_DOWNLOADER_DATA_DOWNLOADER: str = "data-downloader"

    COMMAND_DATA_TYPE: str = "data-type"

    COMMAND_TICKERS: str = "tickers"

    COMMAND_SECURITY_TYPE: str = "security-type"

    COMMAND_MARKET_NAME: str = "market"

    COMMAND_RESOLUTION: str = "resolution"

    COMMAND_START_DATE: str = "start-date"

    COMMAND_END_DATE: str = "end-date"


