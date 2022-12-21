#!/usr/bin/python3
"""Definition of a Square"""


class Square:
    """Represents a square
    Attributes:
            __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size fo a side of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        Return: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square
        Return:
            area of the square
        """
        return self.__size ** 2
