from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    """Class for facade methods"""
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    """methods for user"""
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
        if not user:
            return None
        # Update the user fields
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.email = user_data.get('email', user.email)
        user.password = user_data.get('password', user.password)
        user.place_list = user_data.get('place_list', user.place_list)
        # Return the updated user
        return user
    """methods for amenity"""
    def create_amenity(self, amenity_data):
    # Create a new amenity and stores it in the repository
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity
    def get_amenity(self, amenity_id):
    # Retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)
    def get_all_amenities(self):
    # Retrieve all amenities
        return self.amenity_repo.get_all()
    def update_amenity(self, amenity_id, amenity_data):
    # Update an amenity
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        amenity.name = amenity_data.get('name', amenity.name)
        amenity.description = amenity_data.get('description', amenity.description)
        return amenity
    """methods for place"""
    def create_place(self, place_data):
        # Create a new place and stores it in the repository
        place = Place(**place_data)
        self.place_repo.add(place)
        return place
    def get_place(self, place_id):
    # Retrieve a place by ID
        return self.place_repo.get(place_id)
    def get_all_places(self):
    # Retrieve all places
        return self.place_repo.get_all()
    def update_place(self, place_id, place_data):
    # Update a place
        place = self.place_repo.get(place_id)
        if not place:
            return None
        place.title = place_data.get('title', place.title)
        place.description = place_data.get('description', place.description)
        place.price = place_data.get('price', place.price)
        place.latitude = place_data.get('latitude', place.latitude)
        place.longitude = place_data.get('longitude', place.longitude)
        place.owner = place_data.get('owner', place.owner)
        place.amenities = place_data.get('amenities', place.amenities)
        return place
    
    def delete_place(self, place_id):
    # Delete a place
        if self.place_repo.delete(place_id):
            return True
        return False
    """methods for review"""
    def create_review(self, review_data):
    # Create a new review
        review = Review(**review_data)
        self.review_repo.add(review)
        return {
        'id': review.id,
        'comment': review.comment,
        'rating': review.rating,
        'user_id': review.user_id,
        'place_id': review.place_id
    }
    def get_review(self, review_id):
    # Retrieve a review by ID
        return self.review_repo.get(review_id)
    def get_all_reviews(self):
    # Retrieve all reviews
        return self.review_repo.get_all()
    def get_reviews_by_place(self, place_id):
    # Retrieve all reviews for a specific place
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]
    def update_review(self, review_id, review_data):
    # Update a review
        review = self.review_repo.get(review_id)
        if not review:
            return None
        review.user_id = review_data.get('user_id', review.user_id)
        review.place_id = review_data.get('place_id', review.place_id)
        review.rating = review_data.get('rating', review.rating)
        review.comment = review_data.get('comment', review.comment)
        return review
    def delete_review(self, review_id):
    # Delete a review
        if self.review_repo.delete(review_id):
            return True
        return False