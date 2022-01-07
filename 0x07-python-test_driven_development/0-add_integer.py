#!/usr/bin/python3
""" Adder function for testing """


def add_integer(a, b=98):
    """functions that adds 2 integers

    Arguments:
        a: first integer
        b: second integer, defaults to 98 if not provided

    Returns:
        addition of a and b, an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
