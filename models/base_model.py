#!/usr/bin/python3
"""this is the module file"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """this is the base model class"""
    def __init__(self, *args, **kwargs):
        """the init func"""
        time_convert = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_convert)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """this string func"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """the save func"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """convert to dic"""
        tmp = self.__dict__.copy()
        tmp["__class__"] = self.__class__.__name__
        tmp["created_at"] = self.created_at.isoformat()
        tmp["updated_at"] = self.updated_at.isoformat()
        return tmp
