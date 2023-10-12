#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """check is a kind of class"""
    if isinstance(obj, a_class):
        return True
    return False
