from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import timedelta
from app.services import facade

api = Namespace('login', description='User authentication')

# Request model for login
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class LoginResource(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload
        user = facade.get_user_by_email(credentials['email'])

        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401
        access_token = create_access_token(identity=str(user.id), additional_claims={"is_admin": user.is_admin}, expires_delta=timedelta(days=1))
        return {'access_token': access_token}, 200

@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """Example protected endpoint"""
        current_user_id = get_jwt_identity()  # This is now a string
        claims = get_jwt()  # Get additional claims (like is_admin)

        return {
            'message': f'Hello, user {current_user_id}',
            'is_admin': claims.get("is_admin", False)  # Get is_admin status
        }, 200

@api.route('/generate_admin_token')
class GenerateAdminToken(Resource):
    def get(self):
        ad_token = create_access_token(identity="admin", expires_delta=timedelta(days=365),
                                    additional_claims={"is_admin": True})
        return ({'admin_token': ad_token})