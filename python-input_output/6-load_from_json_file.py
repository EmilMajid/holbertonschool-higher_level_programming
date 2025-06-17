#!/usr/bin/python3
"""Module for creating Python objects from JSON files."""

import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.
    Args:
        filename (str): The name of the JSON file to read
    Returns:
        object: The Python data structure represented
        by the JSON file
    Note:
        - Uses UTF-8 encoding
        - Raises FileNotFoundError if file doesn't exist
        - Raises JSONDecodeError for invalid JSON
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
