#!/usr/bin/python3
"""Definition of a Square"""


class Square:
    """Represents a square
    Args:
            __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size fo a side of the square
        Return: None
        """
        self.size = size

    def area(self):
        """Calculates the area of the square
        Return:
            area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets size of the square
        Return:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size of the suare
        Args:
            value to set to size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __eq__(self, other):
        return self.area() == other.area()
