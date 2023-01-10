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
