#!/usr/bin/python3
"""class to JSON"""


def class_to_json(obj):
    """returns the dictionary description"""
    return obj.__dict__
