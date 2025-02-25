#!/usr/bin/python3
"""
this module contain a class Amenity
"""
from .base_model import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    """Represents an Amenity, Aggregated with Place"""
    def __init__(self, name, description, id=None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.__create_date = datetime.now()
        self.__update_date = datetime.now()

    def amenities_list:

fake def