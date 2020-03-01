#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.place import Place


class test_place(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        place1 = Place()
        place2 = Place()
        place3 = Place()
        self.assertFalse(place1.id == place2.id)
        self.assertFalse(place1.id == place3.id)
        self.assertFalse(place2.id == place3.id)

    def test_created_and_updated(self):
        """Test the updated time"""
        place1 = Place()
        created = place1.created_at
        updated = place1.updated_at
        place1.save()
        self.assertFalse(updated == place1.updated_at)
        self.assertTrue(created == place1.created_at)

    def test_iso(self):
        place1 = Place()
        cre = upd = datetime.now()
        place1.created_at = cre
        place1.updated_at = upd
        d = place1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        place1 = Place()
        d = place1.to_dict()
        self.assertEqual(d["__class__"], "Place")
        self.assertEqual(type(d["created_at"]), str)
