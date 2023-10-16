#!/usr/bin/python3

import json
import csv


class Base:
    """
    Base class for all other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The id of the object. If None, a new id will be assigned.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: The id of the object.
        """
        return str(self.id)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): The list of dictionaries to convert.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a file in JSON format.

        Args:
            list_objs (list): The list of objects to save.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        string = cls.to_json_string(list_dicts)

        with open(filename, "w") as file:
            file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string into a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: The list of dictionaries.
        """
        if json_string is None or json_string == "":
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class
        using a dictionary of attributes.

        Args:
            dictionary (dict): The dictionary of attributes.

        Returns:
            object: The new instance of the class.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of objects from a file in JSON format.

        Returns:
            list: The list of objects.
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
            list_objs (list): The list of objects to save.

        Returns:
            None
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads a list of objects from a CSV file.

        Returns:
            list: The list of objects.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row)
                        obj = cls(width, height, x, y, id)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        obj = cls(size, x, y, id)
                    list_objs.append(obj)
                return list_objs
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws the list of rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): The list of rectangles.
            list_squares (list): The list of squares.

        Returns:
            None
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
