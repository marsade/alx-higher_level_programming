#!/usr/bin/python3
"""This module finds the peak of a list"""


def find_peak(list_of_integers):
    """FInd the peak of a list of Integers"""
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = low + (high - low) // 2
        mid = int(mid)
        if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[
            mid]) and (mid == len(list_of_integers) - 1 or list_of_integers[
                mid + 1] <= list_of_integers[mid])):
            return list_of_integers[mid]
        elif (mid > 0 and list_of_integers[mid + 1] > list_of_integers[mid]):
            low = mid + 1
        else:
            high = mid - 1

    if low >= high:
        return None
