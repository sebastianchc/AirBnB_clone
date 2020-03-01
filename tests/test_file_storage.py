#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        file1 = FileStorage()
        file2 = FileStorage()
        file3 = FileStorage()
        self.assertFalse(file1.id == file2.id)
        self.assertFalse(file1.id == file3.id)
        self.assertFalse(file2.id == file3.id)
