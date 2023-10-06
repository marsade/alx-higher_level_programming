#!/usr/bin/python3
"""prints the character '#'"""


def print_square(size):
    """print the squares

    Args:
        size (int): size of the square

    Returns:
        a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
