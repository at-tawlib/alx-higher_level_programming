#!/usr/bin/python3
"""
checks instance of a specified class
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance
    of the specified class otherwise False
    Args:
        obj (objec): object to check
        a_class (class): class to check against
    Return:
        True : if it an instance of a_class
        False: if it is not an instance a_class
    """
    return (type(obj) == a_class)
