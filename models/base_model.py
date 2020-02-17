#!/usr/bin/python3
""" BaseModel class of AirBnB clone project """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ __init__ method """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """ __str__ method """
        string = "[{}] ({}) {}"
        string = string.format(self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        """ save method """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to_dict method """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
