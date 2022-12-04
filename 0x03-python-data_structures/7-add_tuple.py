#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples and returns a tuple with two integers
    the first element is the addition of the first element of each argument
    the second element should be the addition of the second element of each argument"""
    if len(tuple_b) == 0:
        return tuple_a
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_a) < 2:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    if len(tuple_b) < 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
