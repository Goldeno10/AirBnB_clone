#!/usr/bin/python3
""" base_model test module """


import datetime
import os
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_Storage import FileStorage



class TestBaseMethod(unittest.TestCase):
    """ Contains test methods for base_module """
    def setUp(self):
        """Setup test class"""

        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        self.my_model_json = my_model.to_dict()

    def testBaseModel(self):
        """Test attrribute values of BaseModel instance"""
        self.assertEqual(self.my_model.name, self.my_model_json['name'])

if __name__ == '__main__':
    unnittest.main()


