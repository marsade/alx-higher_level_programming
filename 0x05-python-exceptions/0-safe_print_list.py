#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0
    for i in my_list:
        length += 1
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except IndexError:
        print()
        return length
