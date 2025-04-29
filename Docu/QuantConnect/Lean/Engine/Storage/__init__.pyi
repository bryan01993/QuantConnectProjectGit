from typing import overload
from enum import Enum
import typing

import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.Storage
import QuantConnect.Packets
import System
import System.Collections.Generic
import System.IO

QuantConnect_Lean_Engine_Storage__EventContainer_Callable = typing.TypeVar("QuantConnect_Lean_Engine_Storage__EventContainer_Callable")
QuantConnect_Lean_Engine_Storage__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Lean_Engine_Storage__EventContainer_ReturnType")


class StorageLimitExceededException(System.Exception):
    """Exception thrown when the object store storage limit has been exceeded"""

    def __init__(self, message: str) -> None:
        """
        Creates a new instance of the storage limit exceeded exception
        
        :param message: The associated message
        """
        ...


class FileHandler(System.Object):
    """Raw file handler"""

    def create_directory(self, path: str) -> System.IO.DirectoryInfo:
        """Create the requested directory path"""
        ...

    def delete(self, path: str) -> None:
        """Will delete the given file path"""
        ...

    def directory_exists(self, path: str) -> bool:
        """True if the given directory exists"""
        ...

    def enumerate_files(self, path: str, pattern: str, search_option: System.IO.SearchOption, rootfolder: typing.Optional[str]) -> typing.Union[System.Collections.Generic.IEnumerable[System.IO.FileInfo], str]:
        """Enumerate the files in the target path"""
        ...

    def exists(self, path: str) -> bool:
        """True if the given file path exists"""
        ...

    def read_all_bytes(self, path: str) -> typing.List[int]:
        """Read all bytes in the given file path"""
        ...

    def try_get_file_length(self, path: str) -> int:
        """Will try to fetch the given file length, will return 0 if it doesn't exist"""
        ...

    def write_all_bytes(self, path: str, data: typing.List[int]) -> None:
        """Will write the given byte array at the target file path"""
        ...


class LocalObjectStore(System.Object, QuantConnect.Interfaces.IObjectStore, typing.Iterable[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]):
    """A local disk implementation of IObjectStore."""

    NO_READ_PERMISSIONS_ERROR: str = ...
    """
    No read permissions error message
    
    This field is protected.
    """

    NO_WRITE_PERMISSIONS_ERROR: str = ...
    """
    No write permissions error message
    
    This field is protected.
    """

    @property
    def error_raised(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.ObjectStoreErrorRaisedEventArgs], None], None]:
        """Event raised each time there's an error"""
        ...

    default_object_store: str
    """Gets the default object store location"""

    @property
    def controls(self) -> QuantConnect.Packets.Controls:
        """
        Provides access to the controls governing behavior of this instance, such as the persistence interval
        
        This property is protected.
        """
        ...

    @property
    def algorithm_storage_root(self) -> str:
        """
        The root storage folder for the algorithm
        
        This property is protected.
        """
        ...

    @property
    def file_handler(self) -> QuantConnect.Lean.Engine.Storage.FileHandler:
        """
        The file handler instance to use
        
        This property is protected.
        """
        ...

    @property.setter
    def file_handler(self, value: QuantConnect.Lean.Engine.Storage.FileHandler) -> None:
        ...

    @property
    def keys(self) -> System.Collections.Generic.ICollection[str]:
        """Returns the file paths present in the object store. This is specially useful not to load the object store into memory"""
        ...

    def clear(self) -> None:
        """Will clear the object store state cache. This is useful when the object store is used concurrently by nodes which want to share information"""
        ...

    def contains_key(self, path: str) -> bool:
        """
        Determines whether the store contains data for the specified path
        
        :param path: The object path
        :returns: True if the key was found.
        """
        ...

    def delete(self, path: str) -> bool:
        """
        Deletes the object data for the specified path
        
        :param path: The object path
        :returns: True if the delete operation was successful.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    def get_file_path(self, path: str) -> str:
        """
        Returns the file path for the specified path
        
        :param path: The object path
        :returns: The path for the file.
        """
        ...

    def initialize(self, user_id: int, project_id: int, user_token: str, controls: QuantConnect.Packets.Controls) -> None:
        """
        Initializes the object store
        
        :param user_id: The user id
        :param project_id: The project id
        :param user_token: The user token
        :param controls: The job controls instance
        """
        ...

    def internal_save_bytes(self, path: str, contents: typing.List[int]) -> bool:
        """
        Won't trigger persist nor will check storage write permissions, useful on initialization since it allows read only permissions to load the object store
        
        This method is protected.
        """
        ...

    def is_within_storage_limit(self, path: str, contents: typing.List[int], take_persist_lock: bool) -> bool:
        """
        Validates storage limits are respected on a new save operation
        
        This method is protected.
        """
        ...

    def on_error_raised(self, error: System.Exception) -> None:
        """
        Event invocator for the ErrorRaised event
        
        This method is protected.
        """
        ...

    def path_for_key(self, path: str) -> str:
        """
        Get's a file path for a given path.
        Internal use only because it does not guarantee the existence of the file.
        
        This method is protected.
        """
        ...

    def persist_data(self) -> bool:
        """
        Overridable persistence function
        
        This method is protected.
        
        :returns: True if persistence was successful, otherwise false.
        """
        ...

    def read_bytes(self, path: str) -> typing.List[int]:
        """
        Returns the object data for the specified path
        
        :param path: The object path
        :returns: A byte array containing the data.
        """
        ...

    def save_bytes(self, path: str, contents: typing.List[int]) -> bool:
        """
        Saves the object data for the specified path
        
        :param path: The object path
        :param contents: The object data
        :returns: True if the save operation was successful.
        """
        ...

    def storage_root(self) -> str:
        """
        Storage root path
        
        This method is protected.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Lean_Engine_Storage__EventContainer_Callable, QuantConnect_Lean_Engine_Storage__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Lean_Engine_Storage__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Lean_Engine_Storage__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Lean_Engine_Storage__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


