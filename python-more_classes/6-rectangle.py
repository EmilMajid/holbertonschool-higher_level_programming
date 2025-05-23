#!/usr/bin/python3
"""
This module defines a Rectangle class that models a rectangle.

Features:
- Private instance attributes: __width and __height with public getters and setters.
- Public class attribute: number_of_instances to track active instances.
- Public instance methods:
    - area(): returns the area of the rectangle.
    - perimeter(): returns the perimeter of the rectangle.
- __str__(): returns the rectangle printed with '#' characters.
- __repr__(): returns a string that can recreate the instance using eval().
- __del__(): prints a message when an instance is deleted and decreases the instance counter.

Constraints:
- width and height must be integers >= 0.
- No modules are imported.

Example:
    >>> r1 = Rectangle(3, 2)
    >>> print(r1)
    ###
    ###
    >>> print(r1.area())
    6
    >>> print(r1.perimeter())
    10
    >>> eval(repr(r1))  # creates a new Rectangle(3, 2)

"""

class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

