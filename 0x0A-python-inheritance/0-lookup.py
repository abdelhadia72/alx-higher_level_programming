#!/usr/bin/python3

"""
This script defines a function that returns a list of attributes
and methods of an object.
"""


def lookup(obj):
    """Return a list of attributes
    and methods of an object."""
    return dir(obj)
