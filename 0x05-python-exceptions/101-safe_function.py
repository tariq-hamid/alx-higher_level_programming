#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """Function that executes a function safely.

    Args:
        value: value to be printed

    Returns:
        Returns result of a function, None otherwise.
    """
    result = None
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
    return result
