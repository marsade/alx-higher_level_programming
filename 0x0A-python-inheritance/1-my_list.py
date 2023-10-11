#!/usr/bin/python3
"""My list"""


class MyList(list):
    """My list class"""

    def print_sorted(self):
        """Prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
