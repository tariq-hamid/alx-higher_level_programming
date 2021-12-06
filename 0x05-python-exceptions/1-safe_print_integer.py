#!/usr/bin/python3
def safe_print_integer(value):
    """Function that prints an integer with "{:d}".format().

    Args:
        value: value to be printed

    Returns:
        True if value is int, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
    