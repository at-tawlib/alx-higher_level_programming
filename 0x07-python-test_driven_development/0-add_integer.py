#!/bin/bash/python3
"""
Module adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value of a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
