#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.review import Review


class test_review(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        review1 = Review()
        review2 = Review()
        review3 = Review()
        self.assertFalse(review1.id == review2.id)
        self.assertFalse(review1.id == review3.id)
        self.assertFalse(review2.id == review3.id)

    def test_created_and_updated(self):
        """Test the updated time"""
        review1 = Review()
        created = review1.created_at
        updated = review1.updated_at
        review1.save()
        self.assertFalse(updated == review1.updated_at)
        self.assertTrue(created == review1.created_at)

    def test_iso(self):
        review1 = Review()
        cre = upd = datetime.now()
        review1.created_at = cre
        review1.updated_at = upd
        d = review1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        review1 = Review()
        d = review1.to_dict()
        self.assertEqual(d["__class__"], "Review")
        self.assertEqual(type(d["created_at"]), str)
