#!/usr/bin/python3
""" base_model test module """


from datetime import datetime
import inspect
import os
import unittest
import models
import pycodestyle
BaseModel = models.base_model.BaseModel

class TestBaseMethod(unittest.TestCase):
    """ Contains test methods for base_module """
    def setUp(self):
        """Setup test class"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        self.my_model_json = self.my_model.to_dict()
        self.module_doc = models.base_model.__doc__
        self.base_methods = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_instance_creation(self):
        """Test attrribute values of BaseModel instance"""
        self.assertEqual(self.my_model.name, self.my_model_json['name'])
        self.assertTrue(self.my_model_json['my_number'] is 89)
        self.assertIsInstance(self.my_model_json['my_number'], int)
        self.assertIn('created_at', self.my_model_json)
        self.assertIsInstance(self.my_model.__dict__['created_at'], datetime)

    def test_uuid(self):
        """Test that ids are unique and valid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(inst=inst):
                self.assertIsInstance(uuid, str)
        self.assertNotEqual(inst1.id, inst2.id)

    def test_module_docstring(self):
        "Test for the presence of module documentation"""
        self.assertIsNot(self.module_doc, None,
                'Module documentation not found')
        self.assertTrue(len(self.module_doc) > 1,
                'Module documantation not found')
        
    def test_class_docstring(self):
        "Test for the presence of class documentation"""
        self.assertIsNot(BaseModel.__doc__, None,
                'class documentation not found')
        self.assertTrue(len(BaseModel.__doc__) > 1,
                'class documantation not found')

    def test_method_docstring(self):
        "Test for the presence of class methods documentation"""
        for method in self.base_methods:
            with self.subTest(method=method):
                self.assertIsNot(method.__doc__, None,
                        f'{method} documentation not found')
        self.assertTrue(len(method.__doc__) > 1,
                f'{method} documantation not found')

if __name__ == '__main__':
    unnittest.main()

