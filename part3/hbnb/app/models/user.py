#!/usr/bin/python3
"""
this module contain a class User
"""
from .base_model import BaseModel
from app import db
from app.persistence.repository import InMemoryRepository as database
from datetime import datetime
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


class User(BaseModel):
    """represents a User in the HBNB app"""
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    place_list = db.relationship('Place', backref='owner', lazy=True)
    review_list = db.relationship('Review', backref='author', lazy=True)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hash_password(password)
        self.is_admin = is_admin
        self.validate_user()

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def validate_user(self):
        """Validate user informations format"""
        if not self.first_name:
            raise ValueError("First name is required")
        if not self.last_name:
            raise ValueError("Last name is required")
        if not self.email:
            raise ValueError("Email is required")
        if not self.password:
            raise ValueError("Password is required")
        #email validation
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, self.email):
            raise ValueError("Invalid email format")
        


class Admin(User):
    """represents an Admin, inherits from User"""
    def __promote(self, user_id):
        "Updates a regular user to Admin"
        if self.is_admin == True:
            update_date = datetime.now()
            if database.update(self, user_id, {"is_admin": True, "update_date": update_date}) is not None:
                print("User has been promoted to Admin")
                return True
            return False

    def __demote(self, user_id):
        """Updates an Admin back to regular user"""
        if self.is_admin == False:
            update_date = datetime.now()
            if database.update(self, user_id, {"is_admin": False, "update_date": update_date}) is not None:
                print("User is no longer an Admin")
                return True
            return False
