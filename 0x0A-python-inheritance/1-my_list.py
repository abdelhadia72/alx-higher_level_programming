#!/usr/bin/python3

"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """
    A custom list class that provides additional functionality.
    """

    def print_sorted(self):
        """
        Sorts the list in ascending order and prints it.
        """
        self.sort()
        print(self)
