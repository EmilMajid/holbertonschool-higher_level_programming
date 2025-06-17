#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a UTF-8 encoded text file and returns the number of characters written.

    This function opens the specified file in write mode ('w'), which means:
    - If the file doesn't exist, it will be created
    - If the file exists, its contents will be overwritten
    - The text will be encoded using UTF-8

    Args:
        filename (str, optional): The path to the file to be written. 
                                  Defaults to an empty string.
        text (str, optional): The string content to write to the file. 
                              Defaults to an empty string.

    Returns:
        int: The number of characters written to the file

    Note:
        - Uses Python's built-in open() function with UTF-8 encoding
        - Employs context manager (with statement) for proper file handling
        - Does not handle file permission exceptions
        - Returns the exact character count as returned by file.write()
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
        