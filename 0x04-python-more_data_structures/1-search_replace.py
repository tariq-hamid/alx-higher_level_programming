#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Function that replaces all occurrences
    of an element by another in a new list.

    Args:
        my_list: matrix to be used
        search: element to be replaced
        replace: new element

    Returns:
        New edited list
    """
    new_list = [i if i != search else replace for i in my_list]
    return new_list
