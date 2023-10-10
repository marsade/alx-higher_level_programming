#!/usr/bin/python3
"""appends a string to the file"""


def append_write(filename="", text=""):
    """Appends a string to the end of the file

    Args:
        filename(str): filename to append to
        text(str): string

    Returns:
        number of bytes appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
