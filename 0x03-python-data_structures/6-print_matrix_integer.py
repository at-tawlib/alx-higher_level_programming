#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for num_list in matrix:
        for i in range(len(num_list)):
            if i != (len(num_list) - 1):
                print("{:d} ".format(num_list[i]), end="")
            else:
                print("{:d}".format(num_list[i]), end="")
        print()
