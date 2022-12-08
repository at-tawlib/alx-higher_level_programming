#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average a tuple"""
    if len(my_list) == 0 and my_list:
        return 0
    dividend = 0
    divisor = 0
    for tup in my_list:
        dividend += (tup[0] * tup[1])
        divisor += tup[1]
    return dividend / divisor
