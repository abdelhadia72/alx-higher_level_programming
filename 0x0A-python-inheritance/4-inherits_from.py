#!usr/bin/python3
"""
    check if if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """return true if the object is an instance of
    a class and not the same object otherways false"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
