#!/usr/bin/python3
"""defines a square"""


class Square:
    """square class

    Attributes:
        size(int): size of the square
    """
    __size = None

    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
