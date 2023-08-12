#!/usr/bin/python3
"""this unit test file"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class Test_review(unittest.TestCase):
    """the unit test"""

    def test_gahsdasdb(self):
        """the test func"""
        p1 = Review()
        self.assertIsInstance(p1, type(BaseModel()))
        self.assertIsInstance(p1.text, str)
        self.assertIsInstance(p1.place_id, str)
        self.assertIsInstance(p1.user_id, str)
