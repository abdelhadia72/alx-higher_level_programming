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

    def to_json(self):
        """to json method"""
        return self.__dict__
