#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """Returns the Python data structure represented by a JSON string.
    Args:
        my_str (str): The JSON string to convert to a Python object
    Returns:
        object: The Python data structure (dict, list, etc.)
        represented by the JSON
    Note:
        Will raise json.JSONDecodeError if the string is not valid JSON
    """
    return json.loads(my_str)
