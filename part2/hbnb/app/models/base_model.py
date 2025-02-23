#!/usr/bin/python3
"""
this module contain a class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """aase class for common attributes and methods
    all class inherits from BaseModel to avoid redundancy in the code"""
    def __init__(self, id=None):
        self.id = id if id else uuid.uuid4()
        self.__create_date = datetime.now()

    def update(self):
        self.__update_date = datetime.now()
