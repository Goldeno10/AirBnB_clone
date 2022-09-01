#!/usr/bin/python3
"""This module contains classes and methods/functions that are the base of other classes
"""


import datetime
import uuid
from models import storage


class BaseModel:
    
    """This class 'BaseModel' defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Initializer method """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key != '__class__':
                        if key in ['created_at', 'updated_at']:
                            kwargs[key] = datetime.datetime.fromisoformat(kwargs[key])
                            setattr(self, key, kwargs[key])
                        else:
                            setattr(self, key, kwargs[key])

    def save(self):
        """Updates the records"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Return dictionary representation of object """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = str(type(self).__name__)
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep

    def __str__(self):
        """ Return string representation of the object """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
