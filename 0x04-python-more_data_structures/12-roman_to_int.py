#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function  that converts a Roman numeral to an integer.

    Args:
        roman_string: roman number to be converted

    Returns:
        Integer if roman number is valid, 0 otherwise
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    i = 0
    result = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_int_map:
            result += roman_int_map[roman_string[i:i+2]]
            i += 2
        else:
            result += roman_int_map[roman_string[i]]
            i += 1
    return result
