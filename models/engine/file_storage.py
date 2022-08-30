#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file and deserializes JSON file
    to instances
"""

import json
import os.path


class FileStorage:
    """This class 'FileStorage' erializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return __objects

    def new(self, obj):
        __objects[type(obj).__name__.id] = obj

    def save(self):
        with open(__file_path, 'w', encoding="utf-8") as f:
            if __obejects != None and len(__objects) > 0:
                new_d = {keys: value.to_dict() for key, vlaue in __objects}
                json.dumps(new_d, f)
    
    def reload(self):
        if os.path.exists(__file_path) != False:
            with open(__file_path, 'r', encoding="utf-8") as f:
                __objects = json.load(f)

