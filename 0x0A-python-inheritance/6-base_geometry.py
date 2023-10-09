#!/usr/bin/python3

"""
This file contains the BaseGeometry class.

Methods:
    area(self): Raises an exception indicating
    that the area() method is not implemented.
"""


class BaseGeometry:
    """
    This class represents a base geometry.

    Methods:
        area(self): Raises an exception indicating
        that the area() method is not implemented.
    """

    def area(self):
        """
        Raises an exception indicating that the
        area() method is not implemented.
        """
        raise Exception("area() is not implemented")
