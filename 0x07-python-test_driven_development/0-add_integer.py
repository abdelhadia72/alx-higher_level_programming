#!/usr/bin/python3

def add_integer(a, b=98):
    try:
        return int(a) + int(b)
    except TypeError:
        raise TypeError(f"{'a' if not a else 'b'} must be an integer")
