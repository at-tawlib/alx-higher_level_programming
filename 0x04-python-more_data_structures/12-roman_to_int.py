#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for letter in reversed(roman_string):
        number = digits[letter]
        total += number if total < number * 5 else - number
    return total
