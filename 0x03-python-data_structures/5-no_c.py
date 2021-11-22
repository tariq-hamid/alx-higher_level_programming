#!/usr/bin/python3
def no_c(my_string):
    """Function that removes all characters c and C from a string.

    Args:
        my_string: string to be edited

    Returns:
        new edited string
    """
    new_string = ""
    for char in my_string:
        if ord(char) == 67 or ord(char) == 99:
            continue
        new_string += str(char)
    return new_string
