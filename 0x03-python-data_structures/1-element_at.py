#!/usr/bin/python3
def element_at(my_list, idx):
    """Function that retrieves an element from a list

    Args:
        my_list: list to be retrieved from
        idx: index of the element to be retrieved from

    Returns:
        Retrieved element if exists, None otherwise
    """
    if idx < len(my_list) and idx >= 0:
        return my_list[idx]
    return None
