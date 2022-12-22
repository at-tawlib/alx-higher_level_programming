#!/usr/bin/python3
"""Definition of a Square"""


class Square:
    """Represents a square
    Args:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            size (int): size fo a side of the square
            position: coordinates of square
        Return: None
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

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

    @property
    def position(self):
        """gets position
        Returns:
            position of squar in 2D
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
