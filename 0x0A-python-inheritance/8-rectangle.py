#!/usr/bin/python3

"""
This file contains the BaseGeometry class.
"""


class BaseGeometry:
    """
    This class represents a base geometry.
    """

    def area(self):
        """
        Raises an exception indicating that
        the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer greater than 0.
        Raises a TypeError if the value is not an integer,
        and a ValueError if the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.
        """
        self.integer_validator("width", width)
        self.__height = height

        self.integer_validator("height", height)
        self.__width = width
