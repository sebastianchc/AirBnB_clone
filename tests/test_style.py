#!/usr/bin/python3

import inspect
import unittest
import pep8
from models import amenity, base_model, city, place, review, state


class test_scripts(unittest.TestCase):
    @classmethod
    def test_class(cls):
        cls.base_model = inspect.getmembers(base_model, inspect.isfunction)

        cls.amenity = inspect.getmembers(amenity, inspect.isfunction)

        cls.city = inspect.getmembers(city, inspect.isfunction)

        cls.place = inspect.getmembers(place.Place, inspect.isfunction)

        cls.review = inspect.getmembers(review, inspect.isfunction)

        cls.state = inspect.getmembers(state, inspect.isfunction)

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        models_base = style.check_files(['models/base_model.py',
                                         'models/amenity.py',
                                         'models/city.py',
                                         'models/place.py',
                                         'models/review.py',
                                         'models/state.py'])
        self.assertEqual(models_base.total_errors, 0,
                         "Found code style errors(and warnings).")

    def test_module_documentation(self):
        self.assertTrue(len(amenity.__doc__) > 0)
        self.assertTrue(len(base_model.__doc__) > 0)
        self.assertTrue(len(city.__doc__) > 0)
        self.assertTrue(len(place.__doc__) > 0)
        self.assertTrue(len(review.__doc__) > 0)
        self.assertTrue(len(state.__doc__) > 0)

    def test_functions(self):
        for i in self.base_model:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.amenity:
            self.assertTrue(len(i[1].__doc) > 0)
        for i in self.city:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.place:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.review:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.state:
            self.assertTrue(len(i[1].__doc__) > 0)
