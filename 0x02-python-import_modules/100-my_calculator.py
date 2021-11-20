#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def check_op(op):
    """Function to validate used operators

    Args:
        op: used operator

    Returns:
        True if operator is valid, False otherwise.
    """
    ops = ["+", "-", "*", "/"]
    if op in ops:
        return True
    return False


def map_func(a, b, op):
    """Function to map imported functions with operators

    Args:
        a: first integer
        b: second integer

    Returns:
        The returned value by the mapped function
    """
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return div(a, b)


if __name__ == "__main__":
    argc = len(argv)
    if argc == 4:
        a = int(argv[1])
        op = str(argv[2])
        b = int(argv[3])
        if check_op(op):
            print("{0} {1} {2} = {3}".format(a, op, b, map_func(a, b, op)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
