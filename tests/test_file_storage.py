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

    def test_created_and_updated(self):
        """Test the updated time"""
        file1 = FileStorage()
        created = file1.created_at
        updated = file1.updated_at
        file1.save()
        self.assertFalse(updated == file1.updated_at)
        self.assertTrue(created == file1.created_at)

    def test_iso(self):
        file1 = FileStorage()
        cre = upd = datetime.now()
        file1.created_at = cre
        file1.updated_at = upd
        d = file1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        file1 = FileStorage()
        d = file1.to_dict()
        self.assertEqual(d["__class__"], "FileStorage")
        self.assertEqual(type(d["created_at"]), str)
