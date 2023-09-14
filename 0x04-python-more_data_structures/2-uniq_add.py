#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    newList = set(my_list)
    for i in newList:
        num += i
    return num
