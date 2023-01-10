#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object
    Arg:
        obj : instance of class
    Return:
        dictionary description
    """
    return obj.__dict__
