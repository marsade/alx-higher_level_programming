#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = str(sys.argv[2])
    op1 = int(sys.argv[1])
    op2 = int(sys.argv[3])
    if op == "+":
        print("{} + {} = {}".format(op1, op2, add(op1, op2)))
    elif op == "-":
        print("{} - {} = {}".format(op1, op2, sub(op1, op2)))
    elif op == "*":
        print("{} * {} = {}".format(op1, op2, mul(op1, op2)))
    elif op == "/":
        print("{} / {} = {}".format(op1, op2, div(op1, op2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /i")
