#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Function that deletes a key in a dictionary.

    Args:
        a_dictionary: dictionary to be used
        key: key to be deleted

    Returns:
        Edited dict
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
