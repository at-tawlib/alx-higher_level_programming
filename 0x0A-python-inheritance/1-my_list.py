#!/usr/bin/python3
# Class that inherits from list

class MyList(list):

    def print_sorted(self):
        """ prints the list in ascending sorting order
        """
        print(sorted(self))
