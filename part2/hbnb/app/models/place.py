#!/usr/bin/python3
"""
this module contain a class Place
"""
from .base_model import BaseModel
from .review import Review
from .amenity import Amenity


class Place(BaseModel):
    """represents a Place, tied to an Owner by Composition"""
    def __init__(self, title, description, price, latitude, longitude,
                 owner, amenities_list=None, id=None):
        super().__init__(id)
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.amenities_list = amenities_list if amenities_list else []
        self.reviews = []
        owner.places.append(self)

    def add_review(self, review):
        self.reviews.append(review)

    def delete(self):
        """delete all reviews associated with the place"""
        for review in self.reviews:
            review.delete()
        del self
