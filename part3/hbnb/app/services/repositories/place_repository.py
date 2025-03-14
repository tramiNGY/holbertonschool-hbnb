from app.models.place import Place
from app.models.amenity import Amenity
from app import db
from app.persistence.repository import SQLAlchemyRepository

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_by_price_range(self, min_price, max_price):
        return self.model.query.filter(Place.price >= min_price, Place.price <= max_price).all()
    
    def get_by_amenity(self, amenity_id):
        return self.model.query.join(Place.amenities).filter(Amenity.id == amenity_id).all()
    
    def get_by_owner(self, owner_id):
        return self.model.query.filter(Place.owner_id == owner_id).all()