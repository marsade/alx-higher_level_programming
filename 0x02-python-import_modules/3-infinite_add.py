#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv) - 1
    num = 0
    for i in range(1, n + 1):
        num += int(sys.argv[i])
    print(num)
