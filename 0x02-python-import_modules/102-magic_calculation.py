#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        # print("{} + {} = {}".format(a, b, add(a, b)))
        c = add(a, b)
        for i in range(90):
            # print("{} + {} = {}".format(c, i, add(c, i)))
            c = add(c, i)
        return c
    else:
        return sub(a, b)
