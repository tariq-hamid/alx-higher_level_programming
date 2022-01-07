#!/usr/bin/python3
""" Module containing a function that prints a square """


def print_square(size):
    """Function that prints a square with the character #

    Args:
        size: length of the square

    Returns:
        nth
    """
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print("#")
            else:
                print("#", end='')
