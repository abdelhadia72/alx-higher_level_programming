#!/usr/bin/python3
def safe_print_integer(value):
    try:
        res = value/1
    except TypeError:
        return False
    else:
        print("{:.0f}".format(res))
        return True
