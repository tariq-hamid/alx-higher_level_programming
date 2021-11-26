#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Function that returns a set
    of common elements in two sets.

    Args:
        set_1: first set
        set_2: second set

    Returns:
        New set
    """
    new_set = []
    for element in set_1:
        if element in set_2:
            new_set.append(element)
        else:
            continue
    return set(new_set)
