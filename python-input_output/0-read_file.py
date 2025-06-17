#!/usr/bin/python3
"""Module for reading files"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")