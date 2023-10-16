#!/usr/bin/python3
"""Base class"""


class Base:
    """base class for all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
