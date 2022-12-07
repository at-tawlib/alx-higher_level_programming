#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    # insert list into set
    list_set = set(my_list)
    # convert the set to the list
    unique_list = list(list_set)
    return sum(unique_list)
