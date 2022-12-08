#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if a_dictionary is None:
        return None
    biggest_int = 0
    biggesst_key = None
    for key in a_dictionary:
        if a_dictionary[key] > biggest_int:
            biggest_int = a_dictionary[key]
            biggest_key = key
    return biggest_key
