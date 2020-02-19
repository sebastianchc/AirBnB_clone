#!/usr/bin/python3
""" FileStorage class of AirBnB clone project """
import json


class FileStorage:
    """ FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method """
        return FileStorage.__objects

    def new(self, obj):
        """ new method """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ save method """
        JSON_dict = {}
        for key, value in FileStorage.__objects.items():
            JSON_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(JSON_dict, file)

    def reload(self):
        """ reload method """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                normal_dict = json.load(file)
                for key, value in normal_dict.items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        except OSError:
            pass
