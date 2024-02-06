#!/usr/bin/python3

def islower(c):
    dec_value = ord(c)
    if dec_value >= 97 and dec_value <= 122:
        return True
    else:
        return False
