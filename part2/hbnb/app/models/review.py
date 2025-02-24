#!/usr/bin/python3
"""
this module contain a class Review
"""
from .base_model import BaseModel
from .user import User
from datetime import datetime

class Review(BaseModel):
    """represents a Review,
    tied to Place by Composition and dependent on User"""
    # addplace id
    def __init__(self, place, user, rating, comment, id=None):
        super().__init__(id)
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment
        self.__create_date = datetime.now()
        self.__update_date = datetime.now()
        place.add_review(self)

    def update(self, rating=None, comment=None):
        if rating:
            self.rating = rating
        if comment:
            self.comment = comment
        super().update()

    def delete(self):
        del self

    def list_by_place(place_id):
        pass
