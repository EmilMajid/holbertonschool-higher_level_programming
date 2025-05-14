#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for crt in my_string:
        if crt != "c" and crt != "C":
            new_string += crt
    return new_string
