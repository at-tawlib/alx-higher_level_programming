#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    create object from JSON file
    Args:
        filename (string) : name of file
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
