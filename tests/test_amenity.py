#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.amenity import Amenity


class test_amenity(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        amenity3 = Amenity()
        self.assertFalse(amenity1.id == amenity2.id)
        self.assertFalse(amenity1.id == amenity3.id)
        self.assertFalse(amenity2.id == amenity3.id)

    def test_created_and_updated(self):
        """Test the updated time"""
        amenity1 = Amenity()
        created = amenity1.created_at
        updated = amenity1.updated_at
        amenity1.save()
        self.assertFalse(updated == amenity1.updated_at)
        self.assertTrue(created == amenity1.created_at)

    def test_iso(self):
        amenity1 = Amenity()
        cre = upd = datetime.now()
        amenity1.created_at = cre
        amenity1.updated_at = upd
        d = amenity1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        amenity1 = Amenity()
        d = amenity1.to_dict()
        self.assertEqual(d["__class__"], "Amenity")
        self.assertEqual(type(d["created_at"]), str)
