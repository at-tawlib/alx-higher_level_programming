#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a lis, in reverse order"""
    if len(my_list) == 0:
        return
    my_list.reverse()
    for num in my_list:
        print("{:d}".format(num))