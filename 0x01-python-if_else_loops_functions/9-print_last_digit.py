#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number > 0 or number == 0:
        last_digit = number % 10
    else:
        if (number % 10) == 0:
            pass
        else:
            last_digit = 10 - (number % 10)
    print("{}".format(last_digit))
