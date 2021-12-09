#!/usr/bin/python3
def safe_print_division(a, b):
    """Function that divides 2 integers
    and prints the result.

    Args:
        a: numerator
        b: denominator

    Returns:
        Returns the value of the division, otherwise: None
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
