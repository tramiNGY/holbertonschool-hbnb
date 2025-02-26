from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

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

    def get_place(self, place_id):
        # Retrieve a place from the repository
        return self.place_repo.get(place_id)
    

    #methods for amenity

    def create_amenity(self, amenity_data):
    # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
    # Placeholder for logic to retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
    # Placeholder for logic to retrieve all amenities
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
    # Placeholder for logic to update an amenity
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None

        amenity.name = amenity_data.get('name', amenity.name)
        amenity.description = amenity_data.get('description', amenity.description)
        return amenity

    #methods for place

    def create_place(self, place_data):
        # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
    # Placeholder for logic to retrieve a place by ID, including associated owner and 
        return self.place_repo.get(place_id)

    def get_all_places(self):
    # Placeholder for logic to retrieve all places
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
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
    

    #methods for Reviews
    
    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)
    
    def get_all_reviews(self):
    # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()
    
    def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]
    
    def update_review(self, review_id, review_data):
    # Placeholder for logic to update a review
        review = self.review_repo.get(review_id)
        if not review:
            return None

        review.user_id = review_data.get('user_id', review.user_id)
        review.place_id = review_data.get('place_id', review.place_id)
        review.rating = review_data.get('rating', review.rating)
        review.comment = review_data.get('comment', review.comment)

        return review
    
    def delete_review(self, review_id):
    # Placeholder for logic to delete a review
        return self.review_repo.delete(review_id)
    