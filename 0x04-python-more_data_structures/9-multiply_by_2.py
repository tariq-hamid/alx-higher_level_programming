#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Function that returns a new
    dictionary with all values multiplied by 2

    Args:
        a_dictionary: dictionary to be used

    Returns:
        Edited dict
    """
    new_dict = list(map(lambda a: a * 2, a_dictionary.values()))
    return dict([(key, val) for key, val in zip(a_dictionary.keys(), new_dict)])
