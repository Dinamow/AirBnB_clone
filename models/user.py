#!/usr/bin/python3
"""module file"""
from models.base_model import BaseModel


class User(BaseModel):
    """User calss"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
