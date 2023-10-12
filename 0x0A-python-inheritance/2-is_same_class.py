#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """returns true if obj is exactly an instance of a_class

    Args:
        obg(obj): The object
        a_class(str): The name of the class
    """
    if type(obj) == a_class:
        return True
    return False
