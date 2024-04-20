#!/usr/bin/python3

def uppercase(s):
    for i in s:
        dec_value = ord(i)  # decimal value
        if dec_value >= 97 and dec_value <= 122:  # check if current char is lowercase
            dec_value -= 32  # convert lowercase to uppercase
            print(chr(dec_value), end='')  # print uppercase
        else:
            print(chr(dec_value), end='')  # print uppercase
    print('\n')  # print newline
