#!/usr/bin/python3
"""writes an object to text file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file using json representation

    Args:
        my_obj(obj): object to write to file
        filename(str): given filename
    """
    with open(filename, 'w', encoding="utf-8") as f:
        app = json.dumps(my_obj)
        f.write(app)
