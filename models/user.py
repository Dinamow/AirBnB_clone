#!/usr/bin/python3
from models.base_model import BaseModel
"""module file"""


class User(BaseModel):
    """User calss"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
