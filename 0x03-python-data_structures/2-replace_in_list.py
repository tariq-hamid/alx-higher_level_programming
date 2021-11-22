#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Function that replaces an element of a list at a specific position

    Args:
        my_list: list
        idx: index of the element to be replaced
        element: new element

    Returns:
        Retrieved element if exists, None otherwise
    """
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
        return my_list
    return my_list
