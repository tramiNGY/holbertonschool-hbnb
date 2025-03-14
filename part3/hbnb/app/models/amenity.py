#!/usr/bin/python3
"""
this module contain a class Amenity
"""
from .base_model import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    """Represents an Amenity, Aggregated with Place"""
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    
    # Many to many
    place_amenities = db.relationship('Place', secondary='place_amenity', backref='amenities')
    places = relationship('Place', secondary=place_amenity, backref=db.backref('amenities', lazy=True))

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.validate_amenity()

    def validate_amenity(self):
        """validates amenity informations format"""
        if not self.name or self.name.strip() == "":
            raise ValueError("name is required")
        if not self.description or self.description.strip() == "":
            raise ValueError("description is required")
