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
    def __init__(self, place_id, user_id, rating, comment):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def list_review_by_place(place_id):
        "list all reviews per place"
        place_reviews = []
        for review in database.get_all():
            if review.place_id == place_id:
                place_reviews.append(review)
        return place_reviews
