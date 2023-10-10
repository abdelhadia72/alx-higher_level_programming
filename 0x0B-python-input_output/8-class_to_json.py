#!/usr/bin/python3
""" read/write from file """


def class_to_json(obj):
    """unction that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__
