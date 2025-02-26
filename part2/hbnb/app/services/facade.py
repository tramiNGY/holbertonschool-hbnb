from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Create a new user and store it in the repository
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        # Retrieve a user from the repository
        return self.user_repo.get(user_id)
    
    def get_user_by_email(self, email):
        # Retrieve a user by email from the repository
        return self.user_repo.get_by_attribute("email", email)

    def get_all_users(self):
        # Retrieve all users from the repository
        return self.user_repo.get_all()
    
    def update_user(self, user_id, user_data):
        # Update user data
        user = self.user_repo.get(user_id)

    def get_place(self, place_id):
        # Retrieve a place from the repository
        return self.place_repo.get(place_id)
