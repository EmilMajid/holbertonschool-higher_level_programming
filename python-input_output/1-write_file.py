#!/usr/bin/python3
"""Module for file writing operations.

Contains function to write text to files and return character count.
"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns character count.   
    Args:
        filename: Path to file (default "")
        text: Content to write (default "") 
    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
