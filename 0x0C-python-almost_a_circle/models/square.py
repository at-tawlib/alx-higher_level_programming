#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """prints the instance in human readable format"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        returns size of square
        Return:
            size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        Args:
            value (int) : size of square
        Raises:
            TypeError
            ValueError
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates argument to each attribute
        Arg:
            *args (list) : list of arguemnts
            **kwargs (dictionary) : key value pair
        """
        if args is not None and len(args) != 0:
            i = 0
            for arg in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns dictionary represention of square
        Return:
            dictionary of square
        """
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
