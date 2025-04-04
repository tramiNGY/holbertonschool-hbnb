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

        if not isinstance(self.text, str) or not self.text.strip():
            raise ValueError("Text is required and must be a non-empty string")
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        

