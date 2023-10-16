#!/usr/bin/python3
""" Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square's attributes."""
        data = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, data[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
