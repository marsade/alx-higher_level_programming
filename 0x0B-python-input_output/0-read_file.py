#!/usr/bin/python3
"""reads a file and prints it to stdout"""


def read_file(filename=""):
    """Reads a file and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")