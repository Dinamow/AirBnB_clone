#!/usr/bin/python3
"""this unit test file"""
import unittest
from models.base_model import BaseModel
from models.user import User
import models
from datetime import datetime


class Test_amenity(unittest.TestCase):
    """the unit test"""

    def test_gahsdasdb(self):
        """the test func"""
        self.assertEqual(User, type(User()))
        self.assertIn(User(), models.storage.all().values())
        self.assertEqual(str, type(User().id))
        self.assertIsInstance(User(), type(BaseModel()))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))

        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)
