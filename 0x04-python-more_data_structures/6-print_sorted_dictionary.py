#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Function that that prints a dictionary by ordered keys.

    Args:
        a_dictionary: dictionary to be used

    Returns:
        Nothing
    """
    keys_list_sorted = list(a_dictionary.keys())
    keys_list_sorted.sort()
    for key in keys_list_sorted:
        print("{}: {}".format(key, a_dictionary[key]))
