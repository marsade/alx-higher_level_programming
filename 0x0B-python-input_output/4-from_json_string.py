#!/usr/bin/python3
"""decode json representation of an object"""
import json


def from_json_string(my_str):
    """converts from json string representation

    Args:
        my_obj: object to convert
    """
    return json.loads(my_str)
