#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function  that converts a Roman numeral to an integer.

    Args:
        roman_string: roman number to be converted

    Returns:
        Integer if roman number is valid, 0 otherwise
    """
    number = 0
    if isinstance(roman_string, str) and roman_string != None:
        for char in roman_string:
            if char == "I":
                number += 1
            elif char == "V":
                number += 5
            elif char == "X":
                number += 10            
            elif char == "L":
                number += 50
            elif char == "C":
                number += 100
            elif char == "D":
                number += 500
            elif char == "M":
                number += 1000
    return number
