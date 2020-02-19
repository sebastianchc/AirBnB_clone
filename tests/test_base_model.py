#!/usr/bin/python3

import inspect
import unittest
import pep8
from models import base_model


class test_scripts(unittest.TestCase):
    @classmethod
    def test_class(cls):
        cls.base_model = inspect.getmembers(base_model, inspect.isfunction)

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        models_base = style.check_files(['models/base_model.py'])
        self.assertEqual(models_base.total_errors, 0,
                         "Found code style errors(and warnings).")

    def test_module_documentation(self):
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_functions(self):
        for i in self.base_model:
            self.assertTrue(len(i[1].__doc__) > 0)
