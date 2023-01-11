#!/usr/bin/python3
"""search and update file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
    a specific string"""
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as write_file:
        write_file.write(text)
