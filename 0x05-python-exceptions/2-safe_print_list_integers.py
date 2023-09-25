#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                j += 1
                print("{}".format(my_list[i]), end="")
        print()
        return j
    except IndexError:
        print(end="")
