#!/usr/bin/python3

import inspect
import unittest
import pep8
from datetime import datetime
from models.state import State


class test_state(unittest.TestCase):

    def test_ids(self):
        """Verify's exists different ids"""
        state1 = State()
        state2 = State()
        state3 = State()
        self.assertFalse(state1.id == state2.id)
        self.assertFalse(state1.id == state3.id)
        self.assertFalse(state2.id == state3.id)

    def test_created_and_updated(self):
        """Test the updated time"""
        state1 = State()
        created = state1.created_at
        updated = state1.updated_at
        state1.save()
        self.assertFalse(updated == state1.updated_at)
        self.assertTrue(created == state1.created_at)

    def test_iso(self):
        state1 = State()
        cre = upd = datetime.now()
        state1.created_at = cre
        state1.updated_at = upd
        d = state1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())

    def test_dict_date(self):
        state1 = State()
        d = state1.to_dict()
        self.assertEqual(d["__class__"], "State")
        self.assertEqual(type(d["created_at"]), str)
