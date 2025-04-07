#!/usr/bin/python3
"""Initialize the app module"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask import request, Response

# Initialize exensions
bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()


# Initialize the app
def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, origins=["http://localhost:5500", "https://localhost:5500"], supports_credentials=True)

    @app.before_request
    def handle_options():
        if request.method == 'OPTIONS':
            # If it's an OPTIONS request, respond with necessary headers
            response = Response()
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5500'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            return response

    app.config['PREFERRED_URL_SCHEME'] = 'http'
    
    # Initialize extensions with the app
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    
    # Create the API object
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    
    # Import API namespaces after initializing extensions
    from app.api.v1.users import api as users_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.auth import api as auth_ns

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')

    return app
