#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Function  that deletes the item at a specific position in a list.

    Args:
        my_list: the list to be edited

    Returns:
        New edited list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i == idx:
            continue
        new_list.append(my_list[i])
    my_list[:] = new_list.copy()
    return new_list
