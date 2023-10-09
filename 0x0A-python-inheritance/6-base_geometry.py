class BaseGeometry:
    """
    This class represents a base geometry.

    Methods:
        area(self): Raises an exception indicating
        that the area() method is not implemented.
    """

    def area(self):
        """
        Raises an exception indicating that
        the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
