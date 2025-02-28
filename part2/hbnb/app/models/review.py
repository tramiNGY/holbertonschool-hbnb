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
    user_repository = database()
    place_repository = database()
    # addplace id
    def __init__(self, place_id, user_id, rating, comment):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.validate_review()

    def validate_review(self):
        from app.models.place import Place
        from app.models.user import User
        if not self.comment or self.comment.strip() == "":
            raise ValueError("Comment is required")
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        if not User.validate_user:
            raise ValueError("User_id is not a valid entity")
        if not Place.validate_place:
            raise ValueError("Place_id is not a valid entity")

    def list_review_by_place(place_id):
        "list all reviews per place"
        place_reviews = []
        for review in database.get_all():
            if review.place_id == place_id:
                place_reviews.append(review)
        return place_reviews
