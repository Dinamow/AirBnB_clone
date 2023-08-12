#!/usr/bin/python3
"""this is the test file"""
import unittest
from models.base_model import BaseModel
from models.city import City


class Test_city(unittest.TestCase):
    """this is the unit test"""

    def test_whatever(self):
        """this is the test func"""
        p1 = City()
        self.assertIsInstance(p1, type(BaseModel()))
        self.assertIsInstance(p1.state_id, str)
        self.assertIsInstance(p1.name, str)
