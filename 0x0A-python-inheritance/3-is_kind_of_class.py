#!/usr/bin/python3
"""
checks if object is an instance or object of an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of or if
    the object is an instance of a class that inherited from,
    the specified class otherwise false
    Args:
        obj (objec): object to check
        a_class (class): class to check against
    Return:
        True : if it an instance of a_class
        False: if it is not an instance a_class
    """
    return isinstance(obj, a_class)
