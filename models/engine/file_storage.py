#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file and deserializes JSON 
file to instances
"""

import json
import os.path


class FileStorage:
    """This class 'FileStorage' serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        type(self).__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {k: v.to_dict() for k,v in type(self).__objects.items()}
        with open(type(self).__file_path, "w") as f:
            json.dump(new_dict, f, indent=4)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, does nothing
        """
        from models.base_model import BaseModel
        from models.user import User

        if os.path.exists(type(self).__file_path) is True:
            with open(type(self).__file_path, "r") as f:
                for key, value in json.load(f).items():
                    self.new(eval(value["__class__"])(**value))

