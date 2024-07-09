#!/usr/bin/python3

def uppercase(s):
    result = []
    for i in s:  # Looping through chars
        dec_value = ord(i)  # Decimal value of current char
        if 97 <= dec_value <= 122:  # Check if current char is lowercase
            i = chr(dec_value - 32)  # Convert lowercase to uppercase
        result.append(i)
    print("{}".format("".join(result)))  # Print uppercase