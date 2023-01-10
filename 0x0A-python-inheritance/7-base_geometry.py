#!/usr/bin/python3
"""
Base class for geometries
"""


class BaseGeometry:
    """Simple Base geometry class"""

    def area(self):
        """calculates area of geometry
        Raises:
            Execption: area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
