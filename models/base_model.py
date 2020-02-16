#!/usr/bin/python3
"""Base model of AirBnB"""
from datetime import datetime
from uuid import uuid4 as idc
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Init base model
            kwargs: Arguments
            id: unique id
            created_at: creation datetime
            updated_at: updated datetime
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(idc())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a string with
            class name, id, dict
        """
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id,
                                      self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values"""
        dic = dict(self.__dict__)
        dic["__class__"] = str(type(self).__name__)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return (dic)
