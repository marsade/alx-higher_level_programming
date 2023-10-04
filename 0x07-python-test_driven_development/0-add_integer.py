#!/usr/bin/python3

def add_integer(a, b=98):
    """function to add integer
    
    raises errors if arguments are not integers
    
    Return:
        addition
    """
    if isinstance(a, int) and not isinstance(b, int):
        raise TypeError("a i")