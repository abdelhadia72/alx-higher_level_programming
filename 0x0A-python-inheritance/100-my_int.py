#!/usr/bin/python3

"""
A custom integer class that overrides
the equality and inequality operators.
"""


class MyInt(int):
    """
    A custom integer class that overrides
    the equality and inequality operators.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.
        """
        return super().__eq__(other)
