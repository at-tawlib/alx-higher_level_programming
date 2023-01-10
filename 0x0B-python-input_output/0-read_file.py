#!/usr/bin/python3
""" read file """


def read_file(filename=""):
    """reads a text file and prints it to stdout
    Args:
        filename (strin): name of file
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
