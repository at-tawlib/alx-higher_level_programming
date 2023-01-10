#!/usr/bin/python3
"""Add new attribute to a class"""


def add_attribute(obj, att, value):

    """Adds a new attribute to an oject if possible
    Args:
        obj: object to add attribute to
        att: attribute to add
        value: value of attribute
    Raises:
        TypeError: if object can't have a new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
