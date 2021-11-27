#!/usr/bin/python3
def weight_average(my_list=[]):
    """Function  that returns the
    weighted average of all integers tuple (<score>, <weight>)

    Args:
        my_list: list of tuples

    Returns:
        Weight average
    """
    result = 0
    if my_list:
        denominator = 0
        for tupl in my_list:
            result += (tupl[0] * tupl[1])
            denominator += tupl[1]
        return result / denominator
    return result
