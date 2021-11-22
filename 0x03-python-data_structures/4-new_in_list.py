#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list at a
    specific position without modifying the original list

    Args:
        my_list: list
        idx: index of the element to be replaced
        element: new element

    Returns:
        Retrieved element if exists, None otherwise
    """
    cp_list = my_list.copy()
    if idx < len(cp_list) and idx >= 0:
        cp_list[idx] = element
        return cp_list
    return cp_list
