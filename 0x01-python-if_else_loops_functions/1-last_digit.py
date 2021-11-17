#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0

if number > 0 or number == 0:
    last_digit = number % 10
else:
    if (number % 10) == 0:
        pass
    else:
        last_digit = 10 - (number % 10)

print("Last digit of {} is {} ".format(number, last_digit), end='')
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
