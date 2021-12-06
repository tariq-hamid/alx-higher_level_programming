#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Function that deletes keys with a
    specific value in a dictionary.

    Args:
        a_dictionary: dictionary to be used
        value: value to be searched

    Returns:
        edited dict
    """
    while value in list(a_dictionary.values()):
        del a_dictionary[list(
            a_dictionary.keys()
        )[list(a_dictionary.values()).index(value)]]
