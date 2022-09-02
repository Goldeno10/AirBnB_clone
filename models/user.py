#!/usr/bin/python3
"""This module contain class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Creates a user based on it parameters"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
