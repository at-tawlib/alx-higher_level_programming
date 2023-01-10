#!/usr/bin/python3
"""Save JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation
    Args:
        my_obj : object to writes
        filename: name of file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
