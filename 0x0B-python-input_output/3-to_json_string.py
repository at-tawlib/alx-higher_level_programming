#!/usr/bin/python3
"""object to JSON"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object
    Args:
        my_obj (string): object to be used
    Return:
        the JSON representation
    """
    return json.dumps(my_obj)
