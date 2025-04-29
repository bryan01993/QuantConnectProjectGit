from typing import overload
from enum import Enum
import typing

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds.Transport
import System
import System.Collections.Generic
import System.IO


class LocalFileSubscriptionStreamReader(System.Object, QuantConnect.Interfaces.IStreamReader):
    """Represents a stream reader capable of reading lines from disk"""

    @property
    def should_be_rate_limited(self) -> bool:
        """Gets whether or not this stream reader should be rate limited"""
        ...

    @property
    def stream_reader(self) -> System.IO.StreamReader:
        """Direct access to the StreamReader instance"""
        ...

    @property
    def entry_file_names(self) -> System.Collections.Generic.IEnumerable[str]:
        """Returns the list of zip entries if local file stream reader is reading zip archive"""
        ...

    @property
    def transport_medium(self) -> QuantConnect.SubscriptionTransportMedium:
        """Gets SubscriptionTransportMedium.LocalFile"""
        ...

    @property
    def end_of_stream(self) -> bool:
        """Gets whether or not there's more data to be read in the stream"""
        ...

    @overload
    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, source: str, entryName: str = None) -> None:
        """
        Initializes a new instance of the LocalFileSubscriptionStreamReader class.
        
        :param dataCacheProvider: The IDataCacheProvider used to retrieve a stream of data
        :param source: The local file to be read
        :param entryName: Specifies the zip entry to be opened. Leave null if not applicable, or to open the first zip entry found regardless of name
        """
        ...

    @overload
    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, source: str, startingPosition: int) -> None:
        """
        Initializes a new instance of the LocalFileSubscriptionStreamReader class.
        
        :param dataCacheProvider: The IDataCacheProvider used to retrieve a stream of data
        :param source: The local file to be read
        :param startingPosition: The position in the stream from which to start reading
        """
        ...

    @overload
    def __init__(self, zipFile: typing.Any, entryName: str = None) -> None:
        """
        Initializes a new instance of the LocalFileSubscriptionStreamReader class.
        
        :param zipFile: The local zip archive to be read
        :param entryName: Specifies the zip entry to be opened. Leave null if not applicable, or to open the first zip entry found regardless of name
        """
        ...

    def dispose(self) -> None:
        """Disposes of the stream"""
        ...

    def read_line(self) -> str:
        """Gets the next line/batch of content from the stream"""
        ...


class ObjectStoreSubscriptionStreamReader(System.Object, QuantConnect.Interfaces.IStreamReader):
    """Represents a stream reader capable of reading lines from the object store"""

    @property
    def should_be_rate_limited(self) -> bool:
        """Gets whether or not this stream reader should be rate limited"""
        ...

    @property
    def stream_reader(self) -> System.IO.StreamReader:
        """Direct access to the StreamReader instance"""
        ...

    @property
    def transport_medium(self) -> QuantConnect.SubscriptionTransportMedium:
        """Gets SubscriptionTransportMedium.LocalFile"""
        ...

    @property
    def end_of_stream(self) -> bool:
        """Gets whether or not there's more data to be read in the stream"""
        ...

    def __init__(self, objectStore: QuantConnect.Interfaces.IObjectStore, key: str) -> None:
        """
        Initializes a new instance of the ObjectStoreSubscriptionStreamReader class.
        
        :param objectStore: The IObjectStore used to retrieve a stream of data
        :param key: The object store key the data should be fetched from
        """
        ...

    def dispose(self) -> None:
        """Disposes of the stream"""
        ...

    def read_line(self) -> str:
        """Gets the next line/batch of content from the stream"""
        ...


class RestSubscriptionStreamReader(System.Object, QuantConnect.Interfaces.IStreamReader):
    """Represents a stream reader capable of polling a rest client"""

    @property
    def should_be_rate_limited(self) -> bool:
        """Gets whether or not this stream reader should be rate limited"""
        ...

    @property
    def stream_reader(self) -> System.IO.StreamReader:
        """Direct access to the StreamReader instance"""
        ...

    @property
    def transport_medium(self) -> QuantConnect.SubscriptionTransportMedium:
        """Gets SubscriptionTransportMedium.Rest"""
        ...

    @property
    def end_of_stream(self) -> bool:
        """Gets whether or not there's more data to be read in the stream"""
        ...

    def __init__(self, source: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]], isLiveMode: bool) -> None:
        """
        Initializes a new instance of the RestSubscriptionStreamReader class.
        
        :param source: The source url to poll with a GET
        :param headers: Defines header values to add to the request
        :param isLiveMode: True for live mode, false otherwise
        """
        ...

    def dispose(self) -> None:
        """This stream reader doesn't require disposal"""
        ...

    def read_line(self) -> str:
        """Gets the next line/batch of content from the stream"""
        ...


class RemoteFileSubscriptionStreamReader(System.Object, QuantConnect.Interfaces.IStreamReader):
    """
    Represents a stream reader capabable of downloading a remote file and then
    reading it from disk
    """

    @property
    def should_be_rate_limited(self) -> bool:
        """Gets whether or not this stream reader should be rate limited"""
        ...

    @property
    def stream_reader(self) -> System.IO.StreamReader:
        """Direct access to the StreamReader instance"""
        ...

    @property
    def local_file_name(self) -> str:
        """The local file name of the downloaded file"""
        ...

    @property
    def transport_medium(self) -> QuantConnect.SubscriptionTransportMedium:
        """Gets SubscriptionTransportMedium.RemoteFile"""
        ...

    @property
    def end_of_stream(self) -> bool:
        """Gets whether or not there's more data to be read in the stream"""
        ...

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, source: str, downloadDirectory: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]]) -> None:
        """
        Initializes a new instance of the RemoteFileSubscriptionStreamReader class.
        
        :param dataCacheProvider: The IDataCacheProvider used to retrieve a stream of data
        :param source: The remote url to be downloaded via web client
        :param downloadDirectory: The local directory and destination of the download
        :param headers: Defines header values to add to the request
        """
        ...

    def dispose(self) -> None:
        """Disposes of the stream"""
        ...

    def read_line(self) -> str:
        """Gets the next line/batch of content from the stream"""
        ...

    @staticmethod
    def set_download_provider(downloader: QuantConnect.Interfaces.IDownloadProvider) -> None:
        """
        Save reference to the download system.
        
        :param downloader: Downloader provider for the remote file fetching.
        """
        ...


