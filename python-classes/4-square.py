#!/usr/bin/python3
'''
This module defines the Square class (3-square.py).
'''


class Square:
    '''
    square class has private attr size returns the current square area
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''
        it is getter for size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        this is setter for size
        '''
        self.__size = value



my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)