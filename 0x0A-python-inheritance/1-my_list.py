#!/usr/bin/python3
"""Class that inherits from list
"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """ prints the list in ascending sorting order"""
        print(sorted(self))
