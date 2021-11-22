#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list, in reverse order.

    Args:
        my_list: list to be reversed

    Returns:
        Nothing
    """
    i = -1
    while (i >= -len(my_list) and len(my_list) != 0):
        print("{:d}".format(my_list[i]))
        i -= 1
