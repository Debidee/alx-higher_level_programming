#!/usr/bin/python3
def uppercase(str):
    strn = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            strn += chr(ord(c) - 32)
        else:
            strn += c
            print("{}".format(strn))
