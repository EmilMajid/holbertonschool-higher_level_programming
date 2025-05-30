#!/usr/bin/python3
"""Module Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height.
        Args:
            width (int): width of the rectangle (private)
            height (int): height of the rectangle (private)
        Raises:
            TypeError: if width or height is not an integer or
            ValueError: if width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.
        Returns:
            int: the area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle.
        Returns:
            str: formatted as [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
