#!/usr/bin/python3
"""this unit test file"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class Test_amenity(unittest.TestCase):
    """the unit test"""

    def test_gahsdasdb(self):
        """the test func"""
        p1 = Place()
        self.assertIsInstance(p1, type(BaseModel()))
        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1.city_id, str)
        self.assertIsInstance(p1.user_id, str)
        self.assertIsInstance(p1.description, str)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertIsInstance(p1.max_guest, int)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertIsInstance(p1.latitude, float)
        self.assertIsInstance(p1.longitude, float)
        self.assertIsInstance(p1.amenity_ids, list)
