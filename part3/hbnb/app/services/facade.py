from app import db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.review_repository import ReviewRepository
from app.services.repositories.amenity_repository import AmenityRepository

class HBnBFacade:
    """Class for facade methods"""
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()


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
        return self.user_repo.get_user_by_email(email)
    
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

        # Save the updated user in the database
        db.session.commit()
        # Return the updated user
        return user
    
    def get_user_by_id(self, user_id):
        return self.user_repo.get_user_by_id(user_id)
    

    """methods for amenity"""
    def create_amenity(self, amenity_data):
        # Create a new amenity and stores it in the repository
        amenity = Amenity(
            name=amenity_data['name'],
            description=amenity_data.get('description', None)
        )

        # Add places to the amenity (many-to-many relation)
        place_ids = amenity_data.get('associated_places', [])
        if place_ids:
        # Retrieve the places by their IDs
            places = self.place_repo.get_places_by_ids(place_ids)
            amenity.associated_places.extend(places)  # Adds places to the amenity

        # Add the amenity in the database
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

        # Handles assiociate_places many-to-many relationship
        place_ids = amenity_data.get('associated_places', [])
        if place_ids is not None:
            new_places = self.place_repo.get_places_by_ids(place_ids)

        # Add the new places
        for place in new_places:
            if place not in amenity.associated_places:
                amenity.associated_places.append(place)

        # Delete former places not in the new list
        to_remove = [place for place in amenity.associated_places if place.id not in place_ids]
        for place in to_remove:
            amenity.associated_places.remove(place)

        # Saves changes in the database
        db.session.commit()

        return amenity
    
    def get_amenities_by_ids(self, amenity_ids):
        # Retrieves places by their ids
        return self.amenity_repo.get_amenities_by_ids(amenity_ids)
    
    

    """methods for place"""
    def create_place(self, place_data):
        # Create a new place
        place = Place(
            title=place_data['title'],
            description=place_data['description'],
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
        )
        # Adds user_id to place after its creation
        place.user_id = place_data['user_id']
        # Adds amenities to the place
        amenity_ids = place_data.get('associated_amenities', [])
        if amenity_ids:
            # Fetch Amenity objects corresponding to amenity's name inputed by user
            amenities = self.amenity_repo.get_amenities_by_ids(amenity_ids)
            place.associated_amenities.extend(amenities)  # Adds amenities to the place

        # Adds the place in the database
        self.place_repo.add(place)

        return place
    
    def get_place(self, place_id):
        """Retrieve a place by ID, including associated amenities"""
        place = self.place_repo.get(place_id)  # Utilise la méthode dans le repository
    
        if place:
            # Retourne un dictionnaire avec les informations du place
            return {
                'place': {
                    'id': place.id,
                    'title': place.title,
                    'description': place.description,
                    'price': place.price,
                    'latitude': place.latitude,
                    'longitude': place.longitude,
                    'user_id': place.user_id
                },
                'associated_amenities': [amenity.id for amenity in place.associated_amenities]
            }
    
        return None
    
    def get_all_places(self):
        # Retrieve all places
        places = self.place_repo.get_all()
        return [
            {
                'place': {
                    'id': place.id,
                    'title': place.title,
                    'description': place.description,
                    'price': place.price,
                    'latitude': place.latitude,
                    'longitude': place.longitude
                },
                'associated_amenities': [amenity.id for amenity in place.associated_amenities]
            }
            for place in places
        ]
    
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
        
        # Handles associated_amenities many-to-many relationship
        amenity_ids = place_data.get('associated_amenities', [])
        if amenity_ids is not None:  # If the amenities list is present in the data
            # Fetch the amenities from the database
            new_amenities = self.amenity_repo.get_amenities_by_ids(amenity_ids)
        
        # Add new amenities that are not already associated with the place
        for amenity in new_amenities:
            if amenity not in place.associated_amenities:
                place.associated_amenities.append(amenity)
        
        # Remove amenities that are no longer associated with the place
        to_remove = [amenity for amenity in place.associated_amenities if amenity.id not in amenity_ids]
        for amenity in to_remove:
            place.associated_amenities.remove(amenity)

        # Save the updated place in the database
        db.session.commit()
        return place
    
    def delete_place(self, place_id):
        # Delete a place
        if self.place_repo.delete(place_id):
            return True
        return False
    
    def get_places_by_price_range(self, min_price, max_price):
        # Retrieve places within a specific price range
        return self.place_repo.get_by_price_range(min_price, max_price)

    def get_places_by_amenity(self, amenity_id):
        # Retrieve places with a specific amenity
        return self.place_repo.get_by_amenity(amenity_id)

    def get_places_by_owner(self, owner_id):
        # Retrieve places owned by a specific user
        return self.place_repo.get_by_owner(owner_id)
    
    def get_places_by_ids(self, place_ids):
        # Retrieves places by their ids
        return self.place_repo.get_places_by_ids(place_ids)
    
    
    """methods for review"""
    def create_review(self, review_data):
        # Create a new review
        review = Review(rating=review_data['rating'], text=review_data['text'])
        review.user_id = review_data['user_id']
        review.place_id = review_data['place_id']
        self.review_repo.add(review)

        return review

    def get_review(self, review_id):
        # Retrieve a review by ID
        return self.review_repo.get(review_id)
    
    def get_all_reviews(self):
        # Retrieve all reviews
        return self.review_repo.get_all()
    
    def get_reviews_by_place(self, place_id):
        # Retrieve all reviews for a specific place
        return self.review_repo.get_reviews_by_place(place_id)
    
    def update_review(self, review_id, review_data):
        # Update a review
        review = self.review_repo.get(review_id)
        review.text = review_data.get('text', review.text)
        review.rating = review_data.get('rating', review.rating)

        # Save the updated review in the database
        db.session.commit()
        return review
    
    def delete_review(self, review_id):
        # Delete a review
        if self.review_repo.delete(review_id):
            return True
        return False
