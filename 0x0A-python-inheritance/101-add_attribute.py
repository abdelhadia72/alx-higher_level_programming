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
        TypeError: If the attribute name is empty or if the attribute cannot be set.
    """
    if not name:
        raise TypeError("Attribute name cannot be empty")

    obj.__setattr__(name, value)
    if not hasattr(obj, name):
        raise TypeError("Cannot add new attribute")
