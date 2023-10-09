#!/usr/bin/python3

"""
This module defines a function is_same_class
that checks if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance
        of the specified class. False otherwise.
    """
    return True if type(obj) is a_class else False
