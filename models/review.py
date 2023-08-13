#!/usr/bin/python3
"""module file"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User calss"""
    place_id = ""
    user_id = ""
    text = ""
