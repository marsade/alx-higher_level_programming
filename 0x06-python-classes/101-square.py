#!/usr/bin/python3
"""write a class that defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a square

        Args:
            size(int): size of the square
            position(tuple): position of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print a square with character '#'

        Returns:
            square
        """
        if self.size == 0:
            print()
            return
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.size):
            if self.__position[0] > 0:
                for k in range(self.__position[0]):
                    print(" ", end="")
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

    @property
    def position(self):
        """returns the position of the sqaure"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or any(not isinstance(x, int) or x < 0
                                               for x in value) or len(
                                                   value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        if self.size == 0:
            return ""
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.size):
            if self.__position[0] > 0:
                for k in range(self.__position[0]):
                    print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            if i != self.__size - 1:
                print("")
        return ""
