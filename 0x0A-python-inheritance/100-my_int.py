#!/usr/bin/python3
"""
MyInt a rebel class
"""


class MyInt(int):
    """
    MyInt inherits from int but inverses the equal and not equal functions
    """

    def __eq__(self, value):
        """invert this to be not equal to"""
        return self.real != value

    def __ne__(self, value):
        """invers to be equal to"""
        return self.real == value
