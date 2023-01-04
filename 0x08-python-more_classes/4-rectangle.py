#!/usr/bin/python3
"""Definition of  a rectangle"""


class Rectangle:
    """Represents a rectangle
    Args:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than zero
        Return: None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle
        Return:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value (int): width to set
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle
        Return:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value (int): height to set
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle
        Return:
            area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle
        Return:
            perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """prints a rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
