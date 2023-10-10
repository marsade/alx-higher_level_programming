#!/usr/bin/python3
"""reads a file and prints it to stdout"""


def read_file(filename=""):
    """Reads a file and prints it to stdout"""

    with open(filename, "r") as f:
        for line in f:
            print(line)

read_file("my_file_0.txt")