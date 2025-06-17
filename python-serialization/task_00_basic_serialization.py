#!/usr/bin/env python3
"""
Basic JSON Serialization Module

This module provides functions to serialize Python dictionaries to JSON files
and deserialize JSON files back to Python dictionaries.

Functions:
    serialize_and_save_to_file(data, filename):
        Serializes a Python dictionary and saves it to a JSON file.
    load_and_deserialize(filename):
        Loads and deserializes a JSON file to a Python dictionary.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): A Python Dictionary with data to be serialized
        filename (str): The filename of the output JSON file. If the file exists,
                       it will be overwritten.

    Example:
        >>> data = {"name": "John", "age": 30}
        >>> serialize_and_save_to_file(data, 'data.json')
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: A Python Dictionary with the deserialized JSON data

    Example:
        >>> data = load_and_deserialize('data.json')
        >>> print(data)
        {'name': 'John', 'age': 30}
    """
    with open(filename, 'r') as file:
        return json.load(file)
