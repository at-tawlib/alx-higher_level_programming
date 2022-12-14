#!/usr/bin/python3
"""
This module prints a square with the character #
"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): length of the square

    Raises:
        TypeError: if size is not an integer
        TypeError: if size is float and less than zero
        TypeError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
