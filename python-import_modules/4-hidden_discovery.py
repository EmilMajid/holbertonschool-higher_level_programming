#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden_names = dir(hidden_4)
    for i in hidden_names:
        if i.startswith("__") == False:
            print(i)
