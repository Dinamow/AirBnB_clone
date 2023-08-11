#!/usr/bin/python3
""" serializes instances to a JSON file and deserializes JSON file"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class that stores data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        className = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[className] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        all_objects = FileStorage.__objects
        objdict = {}
        for ob in all_objects.keys():
            objdict[ob] = all_objects[ob].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        check_file = os.path.isfile(FileStorage.__file_path)
        if (check_file):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                data_json = json.load(f)
                for key, value in data_json.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
