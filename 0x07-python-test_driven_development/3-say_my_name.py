#!/usr/bin/python3
"""
This module prints 'My name is <first_name> <last_name>
"""


def say_my_name(first_name, last_name=""):
    """function prints a string containing the first and last name

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: if either the first_name and the last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
