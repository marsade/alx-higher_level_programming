#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sorted_new = sorted(a_dictionary.items(), key=lambda item: item[0])
    name = sorted_new[-1][0]
    return name
