#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Function that replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: dictionary to be used
        key: key to be used
        value: new value

    Returns:
        A new dictionary
    """
    new_dict = a_dictionary.copy()
    new_dict[key] = value
    return new_dict
