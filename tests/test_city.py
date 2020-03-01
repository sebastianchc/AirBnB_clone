#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.city import City


class test_city(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        city1 = City()
        city2 = City()
        city3 = City()
        self.assertFalse(city1.id == city2.id)
        self.assertFalse(city1.id == city3.id)
        self.assertFalse(city2.id == city3.id)

    def test_created_and_updated(self):
        """Test the updated time"""
        city1 = City()
        created = city1.created_at
        updated = city1.updated_at
        city1.save()
        self.assertFalse(updated == city1.updated_at)
        self.assertTrue(created == city1.created_at)

    def test_iso(self):
        city1 = City()
        cre = upd = datetime.now()
        city1.created_at = cre
        city1.updated_at = upd
        d = city1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        city1 = City()
        d = city1.to_dict()
        self.assertEqual(d["__class__"], "City")
        self.assertEqual(type(d["created_at"]), str)
