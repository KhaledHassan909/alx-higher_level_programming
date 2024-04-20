#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()

# def uppercase(s):
#     for i in s: #Looping through chars
#         dec_value = ord(i)  # decimal value of current char
#         if dec_value >= 97 and dec_value <= 122:  # check if current char is lowercase
#             i = chr(dec_value - 32)  # convert lowercase to uppercase
#         print("{}".format(i), end = "")  # print uppercase
#     print("{}".format(''), end = '\n')