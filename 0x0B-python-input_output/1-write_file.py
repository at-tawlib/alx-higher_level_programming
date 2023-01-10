#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    Args:
        filename (string): name of file
        text (string): text to be written
    Return:
        the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
