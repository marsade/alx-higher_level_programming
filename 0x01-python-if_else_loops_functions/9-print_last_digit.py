#!/usr/bin/python3
def print_last_digit(number):
    if type(number) is int:
        num = str(number)
        num = num[-1]
        print(num, end='')
        return (num)
    else
