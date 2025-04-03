from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity

api = Namespace('places', description='Place operations')
# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner'),
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new place"""
        place_data = api.payload
        current_user_id = get_jwt_identity()
        place_data['user_id'] = current_user_id
        try:
            new_place = facade.create_place(place_data)
            associated_amenities = [amenity.id for amenity in new_place.associated_amenities]
            return {'id': new_place.id, 'title': new_place.title, 'description': new_place.description, 'price': new_place.price, 'latitude': new_place.latitude, 'longitude' : new_place.longitude, 'associated_amenities': associated_amenities}, 201
        except ValueError:
            return {'error': 'Invalid input data'}, 400

    @api.response(200, 'List of places retrieved successfully')
    @api.response(404, 'No places found')
    def get(self):
        """Retrieve a list of all places"""
        places_data = facade.get_all_places()
        if not places_data:
            return {'error': 'No places found'}, 404
    
        # Extract informations for dict
        return [{
            'id': place_data['place']['id'],
            'title': place_data['place']['title'],
            'description': place_data['place']['description'],
            'price': place_data['place']['price'],
            'latitude': place_data['place']['latitude'],
            'longitude': place_data['place']['longitude'],
            'associated_amenities': place_data['associated_amenities']
        } for place_data in places_data], 200



@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place_data = facade.get_place(place_id)
        if not place_data:
            return {'error': 'No places found'}, 404
        
        return place_data, 200
    
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(403, 'Unauthorized action')
    @api.response(500, 'Failed to update this place')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        # Retrieve the place by its ID
        place_data = facade.get_place(place_id)
        # Get the current logged-in user ID
        current_user_id = get_jwt_identity()
        # Check if the place exists
        if not place_data:
            return {'error': 'Place not found'}, 404
        # Ensure only the owner of the place can modify it
        if place_data['place']['user_id'] != current_user_id:
            return {'error': 'Unauthorized action'}, 403
        # Get the updated place data from the request payload
        user_place = api.payload
        # Update the place in the database
        updated_place = facade.update_place(place_id, user_place)
        # Check if the update was successful
        if not updated_place:
            return {'error': 'Failed to update this place'}, 500
        # Get associated amenities for the updated place
        associated_amenities = [amenity.id for amenity in updated_place.associated_amenities]
        # Return the updated place details along with associated amenities
        return {
            'id': updated_place.id,
            'title': updated_place.title,
            'description': updated_place.description,
            'price': updated_place.price,
            'latitude': updated_place.latitude,
            'longitude': updated_place.longitude,
            'associated_amenities': associated_amenities
        }, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @api.response(500, 'Failed to delete this review')
    @jwt_required()
    def delete(self, place_id):
        """Delete a review"""
        place = facade.get_place(place_id)
        # check if place exists in the database
        if not place:
            return {'error': 'Place not found'}, 404
        # users can only delete places they own expect if is_admin=True
        current_user = get_jwt_identity()
        claims = get_jwt()
        if place.user_id != current_user and not claims.get('is_admin'):
            return {'error': 'Unauthorized action'}, 403
        # delete place in the database
        deleted_place = facade.delete_place(place_id)
        # check if database issue occured when deleting review
        if not deleted_place:
            return {'error': 'Failed to delete this place'}, 500
        return {'message': 'Place deleted successfully'}, 200


@api.route('/admin/<place_id>')
class AdminPlaceModify(Resource):
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(403, 'Unauthorized action')
    @api.response(500, 'Failed to update this place')
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt_identity()
       
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
       
        # Set is_admin default to False if not exists
       
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
       
        # Logic to update the place
        user_place = api.payload
        # updates the place information in the database
        updated_place = facade.update_place(place_id, user_place)
        # check if database issue occured when updating place
        if not updated_place:
            return {'error': 'Failed to update this place'}, 500
        return {'id': updated_place.id, 'title': updated_place.title, 'description': updated_place.description, 'price': updated_place.price, 'latitude': updated_place.latitude, 'longitude' : updated_place.longitude}, 200