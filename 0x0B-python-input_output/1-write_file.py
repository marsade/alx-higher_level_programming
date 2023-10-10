#!/usr/bin/python3
"""writes a string to a text file and returns
number of characters written"""


def write_file(filename="", text=""):
    """write file function

    Args:
        filename(str):string to write
        text(str): string to write
    Returns:
        the number of bytes written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
