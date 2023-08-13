#!/usr/bin/python
"""Unittest for Base"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """test the BaseModel class"""

    def test_types(self):
        """test the types of attr"""
        p1 = BaseModel()
        p2 = BaseModel()
        x = f"[{p1.__class__.__name__}] ({p1.id}) {p1.__dict__}"

        self.assertIsInstance(p1.id, str)
        self.assertIsInstance(p1.updated_at, datetime)
        self.assertIsInstance(p1.created_at, datetime)
        self.assertNotEqual(p1.id, p2.id)
        self.assertNotEqual(p1.created_at, p2.created_at)
        self.assertTrue(hasattr(p1, "id"))
        self.assertTrue(hasattr(p1, "created_at"))
        self.assertTrue(hasattr(p1, "updated_at"))
        self.assertEqual(p1.__str__(), x)
        self.assertNotEqual(p1.created_at, p1.updated_at)

    def test_methods(self):
        """test base methods"""
        p1 = BaseModel()
        p1.save()
        p1.name = "mezo"
        x = p1.to_dict()
        p1.id = "asa"
        self.assertNotEqual(p1.updated_at, p1.created_at)
        self.assertNotEqual(p1.to_dict(), p1.__dict__)
        self.assertEqual(x["name"], p1.name)
        self.assertEqual(p1.id, "asa")
        self.assertNotEqual(x["id"], p1.name)
        self.assertNotEqual(x["created_at"], p1.created_at)
        self.assertTrue(hasattr(p1.__dict__, "__class__"))
        self.assertTrue(hasattr(p1.to_dict(), "__class__"))
