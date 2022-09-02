#!/usr/bin/python3
"""
This module contain class State that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Creates a state"""
    state_id = ""
    name = ""
