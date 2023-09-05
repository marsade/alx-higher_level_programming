#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
t_number = f"{number}"
if t_number[-1] > '5':
    print("Last digit of ",
          number, " is ", t_number[-1], " and is greater than 5")
elif t_number[-1] == '0':
    print("Last digit of ", number, " is ", t_number[-1], " and is 0")
elif t_number[-1] < '6' and t_number[-1] != '0':
    print("Last digit of ", number, " is ", t_number[-1], " and is 0")
