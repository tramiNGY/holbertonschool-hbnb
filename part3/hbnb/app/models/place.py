#!/usr/bin/python3
"""
this module contain a class Place
"""
from .base_model import BaseModel
from app import db
from app.models.association_tables import place_amenity_association


class Place(BaseModel):
    """Represents a place that can be rented in the HbnB app"""
    __tablename__ = 'places'

    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    review_list = db.relationship('Review', backref='reviewed_place', lazy=True)
    associated_amenities = db.relationship('Amenity', secondary=place_amenity_association, back_populates='associated_places')

    def __init__(self, title, description, price, latitude, longitude):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.validate_place()

    def validate_place(self):
        """Validate place informations format"""
        if not self.title:
            raise ValueError("Title is required")
        if (not self.price) or self.price <= 0:
            raise ValueError("Price is required and must be positive")
        if (not self.latitude) or self.latitude < -90 or self.latitude > 90:
            raise ValueError("Latitude must be between -90 and 90")
        if (not self.longitude) or self.longitude < -180 or self.longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")


    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def list_by_place(self):
        """Dictionary of details for place."""
        place_info = {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
        return place_info
