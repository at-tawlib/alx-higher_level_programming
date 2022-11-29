#!/usr/bin/python3
for number in range(90, 64, -1):
    if number % 2 == 0:
        number += 32
    print("{0}".format(chr(number)), end="")
