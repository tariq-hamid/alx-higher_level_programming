#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function that replaces
	all adds all unique integers in a list
	(only once for each integer).

    Args:
        my_list: list to be used

    Returns:
        New edited list
    """
    sum = 0
    for i in set(my_list):
        sum += i
    return sum

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))