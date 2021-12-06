#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function  that converts a Roman numeral to an integer.

    Args:
        roman_string: roman number to be converted

    Returns:
        Integer if roman number is valid, 0 otherwise
    """
    if (not isinstance(roman_string, str)) or (not roman_string):
        return 0
    roman_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for letter in roman_string:
        result += roman_int_map[letter]
    for x in ["IV", "IX", "XL", "XC", "CM", "CD"]:
        if x in roman_string:
            result -= (2 * roman_int_map[x[0]])
    return result
