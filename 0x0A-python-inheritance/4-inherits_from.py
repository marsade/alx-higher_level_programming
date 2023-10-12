#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """checks if obj is an instance that inherits from
    a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
