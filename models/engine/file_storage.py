#!/usr/bin/python3
# serializes instances to a JSON file and deserializes JSON file to instances
import json
import os.path


class FileStorage:
    """class that stores data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        className = self.__class__.__name__ + "." + obj["id"]
        self.__objects[className] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w+", encoding='utf-8') as f:
            if os.path.getsize(self.__file_path) > 0:
                readed_file = f.read()
                new_obj = json.loads(readed_file)
                new_obj = self.__objects | new_obj
                f.write(new_obj)
            else:
                data = json.dumps(self.__objects)
                f.write(data)

    def reload(self):
        """deserializes the JSON file to __objects"""
        check_file = os.path.isfile(self.__file_path)
        if check_file:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                new_obj = json.loads(f.read())
                self.__objects = new_obj


test = FileStorage()
test.new({"id": "hello", "name": "hello"})
test.save()
test.new({"id": "negga", "name": "hello"})
test.save()
test.reload()
test.new({"id": "nigga", "name": "hello"})
test.save()
print(test.all())
print("fuck u")
test.reload()
print(test.all())
