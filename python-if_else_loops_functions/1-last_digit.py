#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
q = number % 10
if number >= 0:
    if(q > 5 and q != 0):
        print (f"Last digit of {number} is {q} and is greater than 5")
    elif(q < 6 and q != 0):
        print (f"Last digit of {number} is {q}  and is less than 6 and not 0")
    else:
        print (f"Last digit of {number} is {q} and is 0")
else:
    if q == 0:
        print(f"Last digit of {number} is {q} and is 0")
    else:
        print (f"Last digit of {number} is {q - 10} and is less than 6 and not 0")
