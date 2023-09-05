#!/usr/bin/python3
def uppercase(str):
    holder = None
    for i in str:
        holder = i
        if 97 <= ord(i) <= 122:
            holder = chr(ord(i) - 32)
        print("{}".format(holder), end="")
    print()
