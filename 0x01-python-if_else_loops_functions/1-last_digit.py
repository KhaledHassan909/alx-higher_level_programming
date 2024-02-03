#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)
threshold = 5

if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

if last_digit > threshold:
    print("Last digit of {:d} is {:d} and is greater than {:d}".format(
        number, last_digit, threshold))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
else:
    print("Last digit of {:d} is {:d} and is less than {:d} and not 0".format(
        number, last_digit, threshold + 1))
