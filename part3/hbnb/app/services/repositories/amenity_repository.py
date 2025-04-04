from app.models.amenity import Amenity
from app import db
from app.persistence.repository import SQLAlchemyRepository

class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)

    def get_amenities_by_ids(self, amenity_ids):
        """Retrieves a list of amenities object by their ids"""
        return Amenity.query.filter(Amenity.id.in_(amenity_ids)).all()
