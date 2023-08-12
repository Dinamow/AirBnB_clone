#!/usr/bin/python3
"""test state module"""
import unittest
from models.base_model import BaseModel
from models.state import State


class Test_state(unittest.TestCase):
    """this is the unit test for state module"""

    def test_func(self):
        """this is the test func"""
        p1 = State()
        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1, type(BaseModel()))
