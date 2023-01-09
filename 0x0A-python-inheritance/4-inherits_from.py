#!/usr/bin/python3
"""
check if object is an instance of a class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a
    class that inherited form the specified class
    Args:
        obj (object): object to check
        a_class (class): class to check against
    Return:
        True: if object is an instance
        False: if object is not an instance
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
