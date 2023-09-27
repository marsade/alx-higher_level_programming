#!/usr/bin/python3
"""defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """


class Square:
    """square class.

    Attributes:
        size(int): size of square
    """
    __size = None

    def __init__(self, size=None):
        """Initialize square

        Args:
            size(int): size of square

        """
        self.__size = size
