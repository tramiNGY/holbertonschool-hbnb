from app.models.place import Place
from app.models.amenity import Amenity
from app import db
from app.persistence.repository import SQLAlchemyRepository
from sqlalchemy.orm import joinedload

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_by_price_range(self, min_price, max_price):
        return self.model.query.filter(Place.price >= min_price, Place.price <= max_price).all()
    
    def get_by_amenity(self, amenity_id):
        return self.model.query.join(Place.amenities).filter(Amenity.id == amenity_id).all()
    
    def get_by_owner(self, owner_id):
        return self.model.query.filter(Place.owner_id == owner_id).all()
    
    def get_places_by_ids(self, place_ids):
        """Retrieve places by their IDs."""
        # Assuming place_ids is a list of integers (IDs of the places)
        return self.model.query.filter(Place.id.in_(place_ids)).all()
    
    def get_all(self):
        """Retrieve all places with their associated amenities"""
        return self.model.query.options(joinedload(Place.associated_amenities)).all()
    
    def get(self, place_id):
        """Retrieve a place by its ID, including associated amenities"""
        place = self.model.query.options(joinedload(Place.associated_amenities)).filter(Place.id == place_id).first()
    
        if place:
            return place
        return None
