#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Function that prints the first x elements
    of a list and only integers.

    Args:
        my_list: list to be used
        x: the number of elements to print

    Returns:
        the real number of integers printed
    """
    np = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            np += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return np
