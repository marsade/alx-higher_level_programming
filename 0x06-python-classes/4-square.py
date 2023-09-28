#!/usr/bin/python3
"""write a square class that defines a square"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """intialize a square

        Args:
            size (int) : size of the square
        """
        self.size = size

    def area(self):
        return self.size * self.size

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
