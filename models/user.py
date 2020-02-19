#!/usr/bin/python3
""" User class of AirBnB clone project """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
