#!/usr/bin/python3
"""
this module contain a class Place
"""
from .base_model import BaseModel
import uuid
from app.persistence.repository import InMemoryRepository as database
from datetime import datetime


class Place(BaseModel):
    """Represents a place that can be rented in the HbnB app"""
    def __init__(self, title, description, price, latitude, longitude, owner, reviews=[], amenities=[]):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = reviews # List to store related reviews
        self.amenities = amenities # List to store related amenities
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
            "longitude": self.longitude,
            "owner": self.owner,
            "reviews": self.reviews,
            "amenities": self.amenities
        }
        return place_info
