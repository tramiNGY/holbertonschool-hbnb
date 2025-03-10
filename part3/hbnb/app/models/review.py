#!/usr/bin/python3
"""
this module contain a class Review
"""
from .base_model import BaseModel
from .user import User
from datetime import datetime


class Review(BaseModel):
    """represents a Review tied to Place by Composition and dependent on User"""
    def __init__(self, place_id, user_id, rating, comment):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.validate_review()

    def validate_review(self):
        """Validates review informations format"""
        from app.models.place import Place
        from app.models.user import User
        if not isinstance(self.comment, str) or not self.comment.strip():
            raise ValueError("Comment is required and must be a non-empty string")
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        if not User.validate_user:
            raise ValueError("User_id is not a valid entity")
        if not Place.validate_place:
            raise ValueError("Place_id is not a valid entity")

