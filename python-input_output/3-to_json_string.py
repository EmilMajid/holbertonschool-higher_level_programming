#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object as a string.
        Args:
        my_obj: The Python object to convert to JSON
    Returns:
        str: The JSON string representation of the object
    Note:
        Will raise TypeError if the object contains non-serializable types
    """

    return json.dumps(my_obj)
