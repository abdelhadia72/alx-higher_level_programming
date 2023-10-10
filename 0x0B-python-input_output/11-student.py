#!/usr/bin/python3
""" read/write from file """


class Student:
    """
    definitions of class Student
    """

    def __init__(self, first_name, last_name, age):
        """initialize Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json method"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """reload from json method"""
        # print("Type json --> {}".format(type(json)))
        self.__dict__.update(json)
