#!/usr/bin/python3
"""
this module contain a class Review
"""
from .base_model import BaseModel
from app.persistence.repository import InMemoryRepository as database
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

    def list_review_by_place(place_id):
        "list all reviews per place"
        place_reviews = []
        for review in database.get_all():
            if review.place_id == place_id:
                place_reviews.append(review)
        return place_reviews
