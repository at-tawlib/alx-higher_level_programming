#!/usr/bin/python3
def print_last_digit(number):
    num_str = str(number)
    number = int(num_str[-1])
    print(number, end="")
    return number
