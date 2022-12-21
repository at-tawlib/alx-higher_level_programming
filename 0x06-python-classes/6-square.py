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
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints the square with size
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """gets position
        Returns:
            position of squar in 2D
        """
        return __position

    @position.setter
    def position(self, value):
        """setter for position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

