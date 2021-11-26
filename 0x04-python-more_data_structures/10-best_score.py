#!/usr/bin/python3
def best_score(a_dictionary):
    """Function that returns a key
    with the biggest integer value.

    Args:
        a_dictionary: dictionary to be used

    Returns:
        Biggest int value
    """
    if not a_dictionary:
        return None
    high = list(a_dictionary.keys())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > a_dictionary[high]:
            high = key
    return high
