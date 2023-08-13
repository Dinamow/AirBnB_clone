#!/usr/bin/python
"""Unittest for Base"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
import models


class Test_FileStorage(unittest.TestCase):
    """test the BaseModel class"""

    def test_attributes(self):
        """test attr of FileStorage"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(type(models.storage), FileStorage)
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_save_with_arg(self):
        """test save with one arg"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_save_new(self):
        """test save"""
        b1 = BaseModel()
        u1 = User()
        s1 = State()
        p1 = Place()
        c1 = City()
        a1 = Amenity()
        r1 = Review()
        models.storage.new(b1)
        models.storage.new(u1)
        models.storage.new(s1)
        models.storage.new(p1)
        models.storage.new(c1)
        models.storage.new(a1)
        models.storage.new(r1)
        self.assertIn("BaseModel." + b1.id, models.storage.all().keys())
        self.assertIn(b1, models.storage.all().values())
        self.assertIn("User." + u1.id, models.storage.all().keys())
        self.assertIn(u1, models.storage.all().values())
        self.assertIn("State." + s1.id, models.storage.all().keys())
        self.assertIn(s1, models.storage.all().values())
        self.assertIn("Place." + p1.id, models.storage.all().keys())
        self.assertIn(p1, models.storage.all().values())
        self.assertIn("City." + c1.id, models.storage.all().keys())
        self.assertIn(c1, models.storage.all().values())
        self.assertIn("Amenity." + a1.id, models.storage.all().keys())
        self.assertIn(a1, models.storage.all().values())
        self.assertIn("Review." + r1.id, models.storage.all().keys())
        self.assertIn(r1, models.storage.all().values())
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b1.id, objs)
        self.assertIn("User." + u1.id, objs)
        self.assertIn("State." + s1.id, objs)
        self.assertIn("Place." + p1.id, objs)
        self.assertIn("City." + c1.id, objs)
        self.assertIn("Amenity." + a1.id, objs)
        self.assertIn("Review." + r1.id, objs)
        with open("file.json", "r") as f:
            read_text = f.read()
            self.assertIn("BaseModel." + b1.id, read_text)
            self.assertIn("User." + u1.id, read_text)
            self.assertIn("State." + s1.id, read_text)
            self.assertIn("Place." + p1.id, read_text)
            self.assertIn("City." + c1.id, read_text)
            self.assertIn("Amenity." + a1.id, read_text)
            self.assertIn("Review." + r1.id, read_text)
