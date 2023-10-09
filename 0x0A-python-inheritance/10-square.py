#!/usr/bin/python3

"""
This file contains the Square class.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This is the Square class.
    """

    def __init__(self, size):
        """
        Initializes a Square object.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
