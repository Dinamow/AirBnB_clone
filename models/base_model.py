#!/usr/bin/python3
"""this is the module file"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """this is the base model class"""
    def __init__(self):
        """the init func"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """this string func"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """the save func"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """convert to dic"""
        tmp = self.__dict__.copy()
        tmp["__class__"] = self.__class__.__name__
        tmp["created_at"] = self.created_at.isoformat()
        tmp["updated_at"] = self.updated_at.isoformat()
        return tmp


if "__main__" == __name__:
    usr1 = BaseModel()
    print(usr1.to_dict())
    print("***************")
    test = usr1.to_dict()
    for key in test.keys():
        print("\t{}: ({}) - {}".format(key, type(test[key]), test[key]))
