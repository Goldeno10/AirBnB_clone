#!/usr/bin/python3
"""This Module contains the Review class that inherit
from BaseModel class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This class Creates review objects"""
    place_id = ""
    user_id = ""
    text = ""
