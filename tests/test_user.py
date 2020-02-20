#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.user import User


class test_user(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        user1 = User()
        user2 = User()
        user3 = User()
        self.assertFalse(user1.id == user2.id)
        self.assertFalse(user1.id == user3.id)
        self.assertFalse(user2.id == user3.id)

    def test_created_and_updated(self):
        """Test the updated time"""
        user1 = User()
        created = user1.created_at
        updated = user1.updated_at
        user1.save()
        self.assertFalse(updated == user1.updated_at)
        self.assertTrue(created == user1.created_at)

    def test_iso(self):
        user1 = User()
        cre = upd = datetime.now()
        user1.created_at = cre
        user1.updated_at = upd
        d = user1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        user1 = User()
        d = user1.to_dict()
        self.assertEqual(d["__class__"], "User")
        self.assertEqual(type(d["created_at"]), str)
