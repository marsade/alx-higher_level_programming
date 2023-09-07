#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(n))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))
