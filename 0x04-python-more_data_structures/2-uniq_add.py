#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function that replace
    all adds all unique integers in a list
    (only once for each integer).

    Args:
        my_list: list to be used

    Returns:
        New edited list
    """
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
