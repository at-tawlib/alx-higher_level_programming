#!/usr/bin/python3
"""appending string to file"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file(UTF-9)
    Args:
        filename (string): name of file
        text (string): text to append
    Return:
        number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)

    return len(text)
