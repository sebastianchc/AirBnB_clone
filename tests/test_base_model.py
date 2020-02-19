#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        base1 = BaseModel()
        base2 = BaseModel()
        base3 = BaseModel()
        self.assertFalse(base1.id == base2.id)
        self.assertFalse(base1.id == base3.id)
        self.assertFalse(base2.id == base3.id)

    def test_created_and_updated(self):
        """Test the updated time"""
        base1 = BaseModel()
        created = base1.created_at
        updated = base1.updated_at
        base1.save()
        self.assertFalse(updated == base1.updated_at)
        self.assertTrue(created == base1.created_at)

    def test_iso(self):
        base1 = BaseModel()
        cre = upd = datetime.now()
        base1.created_at = cre
        base1.updated_at = upd
        d = base1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        base1 = BaseModel()
        d = base1.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(type(d["created_at"]), str)



