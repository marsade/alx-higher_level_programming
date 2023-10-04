#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """Class that dynamically prevents user from creating
    a new instance asides from first_name
    """
    __slots__ = ["first_name"]
