#!/usr/bin/python3
"""prints the first name and the last name"""


def say_my_name(first_name, last_name=""):
    """prints My name is first_name and last_name

    Args:
        first_name(str): First name
        last_name(str): Last name
    Returns:
        Nothing"""
    if not isinstance(first_name, str) and isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    if isinstance(first_name, str) and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
