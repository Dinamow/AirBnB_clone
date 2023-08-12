#!/usr/bin/python3
"""this unit test file"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_amenity(unittest.TestCase):
    """the unit test"""

    def test_gahsdasdb(self):
        """the test func"""
        p1 = Amenity()
        self.assertIsInstance(p1, type(BaseModel()))
        self.assertIsInstance(p1.name, str)
