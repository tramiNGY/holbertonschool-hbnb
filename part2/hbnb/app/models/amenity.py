#!/usr/bin/python3
"""
this module contain a class Amenity
"""
from .base_model import BaseModel
from datetime import datetime
from app.persistence.repository import InMemoryRepository as database


class Amenity(BaseModel):
    """Represents an Amenity, Aggregated with Place"""
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.validate_amenity()

    def validate_amenity(self):
        if not self.name or self.name.strip() == "":
            raise ValueError("name is required")
        if not self.description or self.description.strip() == "":
            raise ValueError("description is required")

    def amenities_list():
        return {amenity.name: amenity.description for amenity in database().get_all()}
