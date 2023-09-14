#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_new = sorted(a_dictionary.items(), key=lambda item: str(item[0]))
    for item in sorted_new:
        key, value = item
        print("{}: {}".format(key, value))
