#!/usr/bin/python3
"""
this module contain a class User
"""
from app.persistence.repository import InMemoryRepository as database
import uuid
from .place import Place
from datetime import datetime


class User():
    """represents a User in the HBNB app"""
    def __init__(self, user_id=None, first_name, last_name, email, password, place_list, is_admin=False, is_owner):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.__email = email
        self.__password = password
        self.place_list = []
        self.__is_admin = is_admin
        self.is_owner = is_owner

    @staticmethod
    def __register():
        print("Register new account:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        password = input("Password: ")

        if database.get_by_attribute("email", email) is not None:
            user_id = str(uuid.uuid4)
            create_date = datetime.now()
            new_user = User(user_id, first_name, last_name, email, password, create_date)
            database.add(new_user)
            print("User registered successfully!")
            return True

        return False

    @staticmethod()
    def __login():
        email = input("Email: ")
        password = input("Password: ")
        if database.get_by_attribute("email", email) == email and database.get_by_attribute("password", password) == password:
            print("Login success")
            return True
        return False


    def update(self):
        """
        Updates the user's attributes if new values are provided.
        """
        print("Update User informations:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        password = input("Password: ")
        update_date = datetime.now()

        new_infos = dict({"first_name": first_name, "last_name": last_name, "email": email, "password": password, "update_date": update_date})

        for key, value in new_infos.items():
            if value is not ("" or None):
                new_infos[key] = value

        if database.update(self, self.user_id, new_infos) is not None:
            print("Informations have been updated")
            return True
        return False


    def delete(self):
        """delete all reviews associated with the user"""
        if self.is_owner == True:
            for place_id in self.place_list:
                database.delete(self, place_id)
        database.delete(self, self.user_id)


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
