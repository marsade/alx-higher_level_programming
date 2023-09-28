#!/usr/bin/python3
"""write a class square that defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """initialize a square

        Args:
            size(int): size of the square
        """
        self.size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """print a square with character '#'

        Returns:
            square
        """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()

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
