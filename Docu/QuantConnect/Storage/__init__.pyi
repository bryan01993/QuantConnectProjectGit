from typing import overload
from enum import Enum
import typing

import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Storage
import System
import System.Collections.Generic
import System.Text

QuantConnect_Storage_ObjectStore_ReadJson_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_ReadJson_T")
QuantConnect_Storage_ObjectStore_ReadXml_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_ReadXml_T")
QuantConnect_Storage_ObjectStore_SaveJson_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_SaveJson_T")
QuantConnect_Storage_ObjectStore_SaveXml_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_SaveXml_T")
QuantConnect_Storage__EventContainer_Callable = typing.TypeVar("QuantConnect_Storage__EventContainer_Callable")
QuantConnect_Storage__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Storage__EventContainer_ReturnType")


class ObjectStore(System.Object, QuantConnect.Interfaces.IObjectStore, typing.Iterable[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]):
    """Helper class for easier access to IObjectStore methods"""

    @property
    def error_raised(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.ObjectStoreErrorRaisedEventArgs], None], None]:
        """Event raised each time there's an error"""
        ...

    @property
    def keys(self) -> System.Collections.Generic.ICollection[str]:
        """Returns the file paths present in the object store. This is specially useful not to load the object store into memory"""
        ...

    def __init__(self, store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Initializes a new instance of the ObjectStore class
        
        :param store: The IObjectStore instance to wrap
        """
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

    def read(self, path: str, encoding: System.Text.Encoding = None) -> str:
        """
        Returns the string object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :returns: A string containing the data.
        """
        ...

    def read_bytes(self, path: str) -> typing.List[int]:
        """
        Returns the object data for the specified path
        
        :param path: The object path
        :returns: A byte array containing the data.
        """
        ...

    def read_json(self, path: str, encoding: System.Text.Encoding = None, settings: typing.Any = None) -> QuantConnect_Storage_ObjectStore_ReadJson_T:
        """
        Returns the JSON deserialized object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :param settings: The settings used by the JSON deserializer
        :returns: An object containing the data.
        """
        ...

    def read_string(self, path: str, encoding: System.Text.Encoding = None) -> str:
        """
        Returns the string object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :returns: A string containing the data.
        """
        ...

    def read_xml(self, path: str, encoding: System.Text.Encoding = None) -> QuantConnect_Storage_ObjectStore_ReadXml_T:
        """
        Returns the XML deserialized object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :returns: An object containing the data.
        """
        ...

    @overload
    def save(self, path: str) -> bool:
        """
        Saves the data from a local file path associated with the specified path
        
        :param path: The object path
        :returns: True if the object was saved successfully.
        """
        ...

    @overload
    def save(self, path: str, text: str, encoding: System.Text.Encoding = None) -> bool:
        """
        Saves the object data in text format for the specified path
        
        :param path: The object path
        :param text: The string object to be saved
        :param encoding: The string encoding used, Encoding.UTF8 by default
        :returns: True if the object was saved successfully.
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

    def save_json(self, path: str, obj: QuantConnect_Storage_ObjectStore_SaveJson_T, encoding: System.Text.Encoding = None, settings: typing.Any = None) -> bool:
        """
        Saves the object data in JSON format for the specified path
        
        :param path: The object path
        :param obj: The object to be saved
        :param encoding: The string encoding used
        :param settings: The settings used by the JSON serializer
        :returns: True if the object was saved successfully.
        """
        ...

    def save_string(self, path: str, text: str, encoding: System.Text.Encoding = None) -> bool:
        """
        Saves the object data in text format for the specified path
        
        :param path: The object path
        :param text: The string object to be saved
        :param encoding: The string encoding used
        :returns: True if the object was saved successfully.
        """
        ...

    def save_xml(self, path: str, obj: QuantConnect_Storage_ObjectStore_SaveXml_T, encoding: System.Text.Encoding = None) -> bool:
        """
        Saves the object data in XML format for the specified path
        
        :param path: The object path
        :param obj: The object to be saved
        :param encoding: The string encoding used
        :returns: True if the object was saved successfully.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Storage__EventContainer_Callable, QuantConnect_Storage__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Storage__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Storage__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Storage__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


