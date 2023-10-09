#!/usr/bin/python3

"""
This module contains a function for determining
if an object inherits from a given class.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object inherits from a given class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object inherits from the class, False otherwise.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False
