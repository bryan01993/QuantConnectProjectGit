from typing import overload
from enum import Enum
import QuantConnect
import QuantConnect.Data
import QuantConnect.DownloaderDataProvider.Launcher.Models
import System
import System.Collections.Generic


class BrokerageDataDownloader(System.Object, QuantConnect.IDataDownloader):
    """Class for downloading data from a brokerage."""

    def __init__(self) -> None:
        """Initializes a new instance of the BrokerageDataDownloader class."""
        ...

    def get(self, data_downloader_get_parameters: QuantConnect.DataDownloaderGetParameters) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Get historical data enumerable for a single symbol, type and resolution given this start and end time (in UTC).
        
        :param data_downloader_get_parameters: model class for passing in parameters for historical data
        :returns: Enumerable of base data for this symbol.
        """
        ...


