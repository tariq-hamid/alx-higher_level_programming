#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function that returns a set of
    all elements present in only one set.

    Args:
        set_1: first set
        set_2: second set

    Returns:
        New odd set
    """
    od_set = []
    for element in set_2:
        if element in set_1:
            continue
        else:
            od_set.append(element)
    for element in set_1:
        if element in set_2:
            continue
        else:
            od_set.append(element)
    return od_set
