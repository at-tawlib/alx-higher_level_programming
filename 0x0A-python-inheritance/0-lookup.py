#!/usr/bin/python3
"""
list of attributes and methods of an object
"""


def lookup(obj):
    """returns a the list of attributes and methods of an object
    Args:
        obj (object): object to check
    """
    return dir(obj)
