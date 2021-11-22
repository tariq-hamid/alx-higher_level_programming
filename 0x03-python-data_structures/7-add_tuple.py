#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples.

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        Tuple with 2 integers
    """
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) == 1:
        list_a.append(0)
    elif len(list_a) == 0:
        list_a = [0, 0]
    elif len(list_b) == 1:
        list_b.append(0)
    elif len(list_b) == 0:
        list_b = [0, 0]
    new_list = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    return tuple(new_list)
