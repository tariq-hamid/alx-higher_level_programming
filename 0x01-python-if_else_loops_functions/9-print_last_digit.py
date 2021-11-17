#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[-1]
    print("{:1}".format(last_digit), end='')
    return last_digit
