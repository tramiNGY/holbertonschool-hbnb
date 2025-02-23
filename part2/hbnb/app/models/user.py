#!/usr/bin/python3
"""
this module contain a class User
"""
from .base_model import BaseModel
from .place import Place
from datetime import datetime


class User(BaseModel):
    """represents a User in the HBNB app"""
    def __init__(self, first_name, last_name, email,
                 password, is_admin=False, id=None):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.__email = email
        self.__password = password
        self.__is_admin = is_admin
        self.__update_date = datetime.now()
        self.__create_date = datetime.now()
        self.owned_places = []

    def __register(self, first_name, last_name, password, email):
        return User(first_name, last_name, email, password)

    def __login(self, email, password):
        return self.__email == email and self.__password == password


     def update(self, first_name=None, last_name=None, email=None, password=None, is_admin=None):
        """
        Updates the user's attributes if new values are provided.
        """
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.__email = email
        if password:
            self.__password = password
        if is_admin is not None:
            self.__is_admin = is_admin

        super().update()


    def delete(self):
        """delete all reviews associated with the user"""
        for place in self.owned_places:
            for review in place.reviews:
                if review.user == self:
                    review.delete()
        del self

    def __user_type(self):
        return "Admin" if self.__is_admin else "Regular User"


class Owner(User):
    """represents an Owner, inherits from User"""
    def __init__(self, first_name, last_name, email, password, id=None):
        super().__init__(first_name, last_name, email, password,
                         is_admin=False, id=id)
        self.places = []

    def delete(self):
        """delete all places associated with the owner"""
        # unlink user from review to delete user while keeping his review uploaded.
        del self

class Admin(User):
    """represents an Admin, inherits from User"""
    def __init__(self, first_name, last_name, email, password, id=None):
        super().__init__(first_name, last_name, email, password,
                         is_admin=True, id=id)
        self.__update_date = datetime.now()
        self.__create_date = datetime.now()

    def __promote(self, user):
        user.__is_admin = True

    def __demote(self, user):
        user.__is_admin = False
