from app.models.amenity import Amenity
from app import db
from app.persistence.repository import SQLAlchemyRepository

class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)

    def get_amenities_by_names(self, amenity_names):
        """Retrieves a list of amenities object by their names"""
        return Amenity.query.filter(Amenity.name.in_(amenity_names)).all()
