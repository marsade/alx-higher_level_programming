#!/usr/bin/python3
"""json representation of an object"""


import json
def to_json_string(my_obj):
    """converts to json string representation

    Args:
        my_obj: object to convert
    """
    json.dumps(my_obj)
