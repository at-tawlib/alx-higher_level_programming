#!/usr/bin/python3
"""
Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class which inherits from Rectangle"""

    def __init__(self, size):
        """initializes a new Square
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates area of the square
        Return:
            the area
        """
        return self.__size ** 2

    def __str__(self):
        square = "[" + str(self.__class__.__name__) + "]"
        return f"{square} {self.__size}/{self.__size}"
