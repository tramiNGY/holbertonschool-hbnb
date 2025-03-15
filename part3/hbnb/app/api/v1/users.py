from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from flask import request

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        try:
            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
        except ValueError:
            return {'error': 'Invalid input data'}, 400

    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        if not users:
            return {'error': 'No users found'}, 404
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    @api.response(200, 'User details updated successfully')
    @api.response(400, 'You cannot modify email or password')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @jwt_required()
    def put(self, user_id):
        """Update user details"""
        user = facade.get_user(user_id)
        current_user_id = get_jwt_identity()
        # check if user exists in the database
        if not user:
            return {'error': 'User not found'}, 404
        # user can only modify their own details
       
        if current_user_id != user_id:
            return {'error': 'Unauthorized action'}, 403
        
        user_data = api.payload
        # user cannot modify their email or password
        if 'email' in user_data or 'password' in user_data:
            return {'error': 'You cannot modify email or password'}, 400
        # update user in the database
        updated_user = facade.update_user(user_id, user_data)
        # check if database issue occured when updating user
        if not updated_user:
            return {'error': 'Failed to update user'}, 500
        return {'id': current_user_id, 'first_name': updated_user.first_name, 'last_name': updated_user.last_name, 'email': updated_user.email}, 200

@api.route('/admin')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403


        user_data = request.json
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        # Logic to create a new user
        try:
            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
        except ValueError:
            return {'error': 'Invalid input data'}, 400


@api.route('/admin/<user_id>')
class AdminUserModify(Resource):
    @api.response(200, 'User details updated successfully')
    @api.response(400, 'You cannot modify email or password')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Adminivileges required'}, 403

        data = request.json
        email = data.get('email')

        # Ensure email uniqueness
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
       
        # Logic to update user details
        updated_user = facade.update_user(user_id, data)
        #check if user was updated
        if not updated_user:
            return {'error': 'Failed to update user'}, 500
       
        return {'id': current_user, 'first_name': updated_user.first_name, 'last_name': updated_user.last_name, 'email': updated_user.email,'password': updated_user.password}, 200