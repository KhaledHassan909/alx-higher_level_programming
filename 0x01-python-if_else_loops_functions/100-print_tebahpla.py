#!/usr/bin/python3

def print_characters():
    for i in range(122, 96, -1):
        char_used = chr(i)
        if i % 2 != 0:
            char_used = chr(i - 32)
        print("{}".format(char_used), end = '')

print_characters()