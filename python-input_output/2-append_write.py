#!/usr/bin/python3
"""File Append Operations Module.
This module provides a function for appending text to files and tracking
the number of characters added. It handles UTF-8 encoded text files
and manages file creation automatically when needed.
"""


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters added.

    This function safely appends the specified text to the given file using
    UTF-8 encoding. If the file doesn't exist, it will be created automatically.
    The operation is performed using Python's context manager for reliable
    file handling.
    Args:
        filename (str, optional): Path to the target file. Defaults to "".
        text (str, optional): Content to append to the file. Defaults to "".
    Returns:
        int: The number of characters successfully appended to the file
    Features:
        - Automatic file creation if nonexistent
        - Safe append operation (preserves existing content)
        - UTF-8 encoding support
        - No external dependencies
        - Proper resource management via context manager
    Example:
        >>> chars_added = append_write("log.txt", "New entry\n")
        >>> print(chars_added)
        9
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
        