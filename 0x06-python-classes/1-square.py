#!/usr/bin/python3
"""defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """


class Square:
    """square class"""
    __size = None

    def __init__(self, size=None):
        self.__size = size
