#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list.

    Args:
        my_list: the list to be scanned

    Returns:
        Max value in a list
    """
    if len(my_list) == 0:
        return None
    max = 0
    for i in my_list:
        if i > max:
            max = i
    return max
