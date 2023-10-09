#!/usr/bin/python3

"""
This is a script that adds a new attribute to the given object.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to the given object.

    Args:
        obj: The object to add the attribute to.
        name: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute name is empty.
    """
    obj.name = value

    if not obj.name:
        raise TypeError("can't add new attribute")
