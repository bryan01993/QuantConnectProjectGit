from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect
import QuantConnect.DownloaderDataProvider.Launcher
import QuantConnect.Interfaces
import System
import System.Collections.Generic


class DownloaderDataProviderArgumentParser(System.Object):
    """This class has no documentation."""

    @staticmethod
    def parse_arguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """
        Parses the command-line arguments and returns a dictionary containing parsed values.
        
        :param args: An array of command-line arguments.
        :returns: A dictionary containing parsed values from the command-line arguments.
        """
        ...


class DataDownloadConfig:
    """Represents the configuration for data download."""

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """Type of tick data to download."""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Type of security for which data is to be downloaded."""
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """Resolution of the downloaded data."""
        ...

    @property
    def start_date(self) -> datetime.datetime:
        """Start date for the data download."""
        ...

    @property
    def end_date(self) -> datetime.datetime:
        """End date for the data download."""
        ...

    @property
    def market_name(self) -> str:
        """Market name for which the data is to be downloaded."""
        ...

    @property
    def symbols(self) -> System.Collections.Generic.List[QuantConnect.Symbol]:
        """List of symbols for which data is to be downloaded."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the DataDownloadConfig struct."""
        ...

    @overload
    def __init__(self, tickType: QuantConnect.TickType, securityType: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, startDate: typing.Union[datetime.datetime, datetime.date], endDate: typing.Union[datetime.datetime, datetime.date], market: str, symbols: System.Collections.Generic.List[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the DataDownloadConfig class with the specified parameters.
        
        :param tickType: The type of tick data to be downloaded.
        :param securityType: The type of security for which data is being downloaded.
        :param resolution: The resolution of the data being downloaded.
        :param startDate: The start date for the data download range.
        :param endDate: The end date for the data download range.
        :param market: The name of the market from which the data is being downloaded.
        :param symbols: A list of symbols for which data is being downloaded.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string representation of the DataDownloadConfig struct.
        
        :returns: A string representation of the DataDownloadConfig struct.
        """
        ...


class Program(System.Object):
    """This class has no documentation."""

    @staticmethod
    def initialize_configurations() -> None:
        """
        Initializes various configurations for the application.
        This method sets up logging, data providers, map file providers, and factor file providers.
        """
        ...

    @staticmethod
    def main(args: typing.List[str]) -> None:
        """
        The main entry point for the application.
        
        :param args: Command-line arguments passed to the application.
        """
        ...

    @staticmethod
    def run_download(data_downloader: QuantConnect.IDataDownloader, data_download_config: QuantConnect.DownloaderDataProvider.Launcher.DataDownloadConfig, data_directory: str, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, map_symbol: bool = True) -> None:
        """
        Executes a data download operation using the specified data downloader.
        
        :param data_downloader: An instance of an object implementing the IDataDownloader interface, responsible for downloading data.
        :param data_download_config: Configuration settings for the data download operation.
        :param data_directory: The directory where the downloaded data will be stored.
        :param data_cache_provider: The provider used to cache history data files
        :param map_symbol: True if the symbol should be mapped while writing the data
        """
        ...


