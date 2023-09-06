#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upp = chr(ord(i) - 32)
            new_str += upp
        else:
            new_str += i
    print("{}".format(new_str))
