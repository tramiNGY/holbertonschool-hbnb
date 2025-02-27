#!/usr/bin/python3
"""
this module contain a class User
"""
from .base_model import BaseModel
from app.persistence.repository import InMemoryRepository as database
import uuid
from .place import Place
from datetime import datetime
import re


class User(BaseModel):
    """represents a User in the HBNB app"""
    def __init__(self, first_name, last_name, email, password, place_list=[], is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.place_list = place_list
        self.is_admin = is_admin
        self.validate_user()

    def validate_user(self):
        if not self.first_name:
            raise ValueError("First name is required")
        if not self.last_name:
            raise ValueError("Last name is required")
        if not self.email:
            raise ValueError("Email is required")
        if not self.password:
            raise ValueError("Password is required")
        
    @staticmethod
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None


class Admin(User):
    """represents an Admin, inherits from User"""
    def __promote(self, user_id):
        if self.__is_admin == True:
            update_date = datetime.now()
            if database.update(self, user_id, {"is_admin": True, "update_date": update_date}) is not None:
                print("User has been promoted to Admin")
                return True
            return False

    def __demote(self, user_id):
        if self.__is_admin == False:
            update_date = datetime.now()
            if database.update(self, user_id, {"is_admin": False, "update_date": update_date}) is not None:
                print("User is no longer an Admin")
                return True
            return False
