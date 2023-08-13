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
        p1 = FileStorage
        self.assertFalse(hasattr(p1, "file_path"))
        self.assertFalse(hasattr(p1, "objects"))
