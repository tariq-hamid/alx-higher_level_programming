#!/usr/bin/python3
def safe_print_integer_err(value):
    """Function that prints an integer.

    Args:
        value: value to be printed

    Returns:
        Returns True if value is integer, False otherwise
    """
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err))
        return False
    return True
