#!/usr/bin/python3
"""
this module contain a class Review
"""
from .base_model import BaseModel
from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Review(BaseModel):
    """represents a Review tied to Place by Composition and dependent on User"""
    __tablename__ = 'reviews'
    
    text = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, rating, text):
        super().__init__()
        self.rating = rating
        self.text = text
        self.validate_review()

    def validate_review(self):
        """Validates review informations format"""
        from app.models.place import Place
        from app.models.user import User

        if not isinstance(self.text, str) or not self.text.strip():
            raise ValueError("Text is required and must be a non-empty string")
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        
        # Create an instance of User with user's id who made the review
        user = User.query.get(self.user_id)
        if not user:
            raise ValueError("User_id is not a valid entity")
        user.validate_user()  # Validates user's information format

        # Create an instance of Place with place's id of the review
        place = Place.query.get(self.place_id)
        if not place:
            raise ValueError("Place_id is not a valid entity")
        place.validate_place()  # Validates place's information format

