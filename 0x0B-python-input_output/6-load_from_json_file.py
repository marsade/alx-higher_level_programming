#!/usr/bin/python3
"""creates object from json file"""
import json


def load_from_json_file(filename):
    """creates object from json file

    Args:
        filename(str): string
    """
    with open(filename, encoding="utf-8") as f:
        app = f.read()
        return json.loads(app)
