#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for i in range(len(my_list)):
        if search == my_list[i]:
            newList.append(replace)
        else:
            newList.append(my_list[i])
    return newList
