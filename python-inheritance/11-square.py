#!/usr/bin/python3
"""
Module: 11-square
Defines a Square class that inherits from Rectangle (from 9-rectangle.py).
This class validates size, implements area computation, and defines
a custom string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square (both width and height).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size <= 0.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: Formatted as [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
