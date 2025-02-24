#!/usr/bin/python3
"""
this module contain a class Place
"""
import uuid
from app.persistence.repository import InMemoryRepository as database
from datetime import datetime


class Place():
    """represents a Place, tied to an Owner by Composition"""

    def __init__(self, title, description, price, latitude, longitude, owner, amenities_list=None, id=None):
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

    @staticmethod
    def create():
        print("Creating a new place!")
        title = input("Title: ")
        description = input("Description: ")
        price = input("Price: ")
        latitude = input("Latitude: ")
        longitude = input("Longitude: ")
        amenities_list = input("Amenities List: ")
        owner =
        place_id = str(uuid.uuid4())
        create_date = datetime.now()
        new_place = Place(place_id, title, description, price, latitude, longitude, owner, amenities_list)
        database.add(new_place)
        print("New Place created succesfully")
        return True
    
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
        if amenities_list is not None:
            self.amenities_list = amenities_list
        super().update()

    def list(title, price, latitude, longitude, amenities_list):
        # to be added
        pass

    def add_review(self, review):
        """append reviews to a place"""
        self.reviews.append(review)

    def delete(self):
        """delete all reviews associated with the place"""
        for review in self.reviews:
            review.delete()
        del self
