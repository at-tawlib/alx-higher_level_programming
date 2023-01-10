#!/usr/bin/python3
"""
Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializes a new Rectangle
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates area of the rectangle
        Return:
            the area
        """
        return self.__width * self.__height

    def __str__(self):
        rect = "[" + str(self.__class__.__name__) + "]"
        return f"{rect} {self.__width}/{self.__height}"
