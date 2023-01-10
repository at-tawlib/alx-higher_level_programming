#!/usr/bin/python3
""" read file """


def read_file(filename="", encoding='utf8'):
    """reads a text file and prints it to stdout
    Args:
        filename (strin): name of file
    """
    with open(filename, encoding='utf-8') as file:
        data = file.read()
        print(data)
