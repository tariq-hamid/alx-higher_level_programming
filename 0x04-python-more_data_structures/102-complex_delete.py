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
    new_dict = a_dictionary.copy()
    while value in list(new_dict.values()):
        del new_dict[list(
            new_dict.keys()
        )[list(new_dict.values()).index(value)]]
    return new_dict
