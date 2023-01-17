#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangele that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns width of rectangle
        Return:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of rectangle
        Arg:
            value (int) : width to set
        Raises:
            TypeError
            ValueError
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle
        Return:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle
        Arg:
            value (int) : height to set
        Raises:
            TypeError
            ValueError
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x value of rectangle
        Return:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """sets x value of rectangle
        Arg:
            value (int) : x to set
        Raises:
            TypeError
            ValueError
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y value of rectangle
        Return:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """sets y of rectangle
        Arg:
            value (int) : y to set
        Raises:
            TypeError
            ValueError
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates and returns area of the rectangle
        Return:
            area
        """
        return (self.__width * self.__height)

    def display(self):
        """ prints the rectangle with # """
        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns class
        Return:
            string
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        assigns argument to each attribute
        Arg:
            *args (list) : list of arguemnts
            *kwargs (dictionary) : key value pair
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns dictionary represention of Rectangle
        Return:
            dictionary of rectangle
        """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
