#!/usr/bin/python3
"""Module for saving Python objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.
    Args:
        my_obj: The Python object to serialize and save
        filename (str): The name of the file to write to  
    Note:
        - Uses UTF-8 encoding
        - Overwrites existing file content
        - Raises TypeError for non-serializable objects
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
        