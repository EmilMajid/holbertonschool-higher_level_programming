#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
q = n % 10
if n >= 0:
    if q > 5:
        print(f"Last digit of {n} is {q} and is greater than 5")
    elif 0 < q < 6:
        print(f"Last digit of {n} is {q}  and is less than 6 and not 0")
    else:
        print(f"Last digit of {n} is {q} and is 0")
else:
    if q == 0:
        print(f"Last digit of {n} is {q} and is 0")
    else:
        print(f"Last digit of {n} is {q - 10} and is less than 6 and not 0")
