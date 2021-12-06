#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Function that prints x elements of a list.

    Args:
        my_list: list to be used
        x: the number of elements to print

    Returns:
        the number of elements to print
    """
    i = 0
    np = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end='')
            i += 1
            np += 1
        except:
            print()
            return np
    print()
    return np
