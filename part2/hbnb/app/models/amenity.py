#!/usr/bin/python3
"""
this module contain a class Amenity
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity, Aggregated with Place"""
    def __init__(self, name, description, id=None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.__create_date = datetime.now()
        self.__update_date = datetime.now()

    def update(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        super().update()

    def delete(self):
        del self
