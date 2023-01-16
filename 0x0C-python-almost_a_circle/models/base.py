#!/usr/bin/python3
import json
"""Base class"""


class Base:
    """Base class for all other classess"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string representation of list_dictionaries
        Args:
            list_dictionaries: dictionary to representation
        Return:
            JSON string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list objects to a file
        Args:
            cls : reference to class
            list_objs : list of objects
        """
        content = []
        if list_objs is not None and list_objs != []:
            for obj in list_objs:
                content.append(cls.to_dictionary(obj))
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        Args:
            json_string: a string representing a list of dictionaries
        Return:
            list of JSON string representation
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance of class with all attributes set
        Args:
            cls: reference to class
            **dictionary: pointer to dictionary
        Return:
            instance of class
        """
        if cls.__name__ == "Square":
            temp = cls(3)
        if cls.__name__ == "Rectangle":
            temp = cls(3, 3)

        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        Args:
            cls: reference to class
        Return:
            list
        """
        try:
            with open(cls.__name__+".json", "r") as file:
                content = cls.from_json_string(file.read())

                result = []
                for i in content:
                    result.append(cls.create(**i))

                return result
        except FileNotFoundError:
            return []
