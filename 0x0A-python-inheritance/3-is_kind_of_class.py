#!/usr/bin/python3

"""
This module defines a function is_kind_of_class that checks
if an object is an instance of, or a subclass of, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of
    or a subclass of, a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of,
        or a subclass of, the specified class. False otherwise.
    """
    return isinstance(obj, a_class)
