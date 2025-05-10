#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
     filtered = sorted([n for n in names if not n.startswith("__")])
    for name in filtered:
        print(name)
