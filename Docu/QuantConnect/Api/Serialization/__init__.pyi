from typing import overload
from enum import Enum
import typing

import QuantConnect.Api
import QuantConnect.Api.Serialization
import System

JsonConverter = typing.Any


class ProductJsonConverter(JsonConverter):
    """Provides an implementation of JsonConverter that can deserialize Product"""

    @property
    def can_write(self) -> bool:
        """Gets a value indicating whether this JsonConverter can write JSON."""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def create_product_from_j_object(self, j_object: typing.Any) -> QuantConnect.Api.Product:
        """
        Create an order from a simple JObject
        
        :returns: Order Object.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


