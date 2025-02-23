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

    def update(self, title=None, description=None, price=None, latitude=None, longitude=None, amenities_list=None):
        """
        Updates the attributes of the Place object if new values are provided.
        """
        if title:
            self.title = title
        if description:
            self.description = description
        if price:
            self.price = price
        if latitude:
            self.latitude = latitude
        if longitude:
            self.longitude = longitude
        if amenities_list is not None:
            self.amenities_list = amenities_list
        super().update()

    def list(title, price, latitude, longitude, amenities_list)
        # to be added
    
    
    def add_review(self, review):
        self.reviews.append(review)

    def delete(self):
        """delete all reviews associated with the place"""
        for review in self.reviews:
            review.delete()
        del self
