
![printf image image (1)](https://pbs.twimg.com/media/Gj1Hgv2XYAAiHmC?format=jpg&name=small)


# **HBnB Evolution - Authorisation and Database**

## Description

HBnB Evolution is a RESTful API that provides endpoints for managing users, places, amenities, and reviews. This project follows a structured architecture to ensure scalability and maintainability.



## Features

- User management (Create, Read, Update, Delete)
- Place management with location data
- Review system for places
- Amenity tracking
- RESTful API design with Flask
- Business logic abstraction using the Facade pattern
- Data persistence layer
- Admin authorisation
- SQL databse

## Project Structure
![structure](https://pbs.twimg.com/media/GmLKXb8bkAAhtlc?format=png&name=small)


# Directory Overview

## `app/models/`

This directory contains the data models used in the API. Each model represents a different entity:

- `user.py`: Defines the User model with attributes like `first_name`, `last_name`, `email`, and `password`. Allows admin to modify email and password unlike regular user, admins can now also modify every user, also hashes the passorw for security.
- `place.py`: Defines the Place model, including attributes like `title`, `description`, `price`, `latitude`, and `longitude`.
- `review.py`: Defines the Review model, storing user feedback on places.
- `amenity.py`: Defines the Amenity model, storing amenities available for places.
- `place_amenity.py`: Defines the association table linking places and amenities.
- `base_model.py`: Defines a reusable base model with UUID primary keys and timestamp management.

## `app/api/v1/`

This directory contains the API endpoints that handle requests and responses.

- `users.py`: Handles user-related operations (creation, retrieval, update, and deletion).
- `places.py`: Manages places, including creating, updating, and retrieving places.
- `reviews.py`: Manages reviews left by users for different places.
- `amenities.py`: Manages amenities available at different places.
- `auth.py`: Handles regular user and admin authentication, including login and token generation for access control.

### JWT Authentication Implementation

Our HBNB app uses JWT (JSON Web Tokens) for user authentication and authorization. JWTs are used to securely transmit information between parties as a JSON object. In this application, JWTs are used to authenticate users and authorize them to access protected routes.

### For regular users

When a user logs in with their email and password, the application verifies their credentials and generates a JWT if the credentials are valid. This JWT is then returned to the user and can be used for subsequent requests to access protected routes.

## `app/services/`

This directory contains the business logic layer, abstracting the logic from the API endpoints.

`facade.py`: A service class that provides methods to manage users, places, amenities, and reviews, including CRUD operations and additional filtering functionality.

## `app/services/repositories`

- `amenity_repository.py`: Implements a repository for managing amenities.
- `place_repository.py`: Implements a repository for managing places with filters for price range, amenities, and owners.
- `review_repository.py`: Implements a repository for managing reviews, including retrieval by place.
- `user_repository.py`: Implements a repository for managing users, including retrieval by email.

## `app/persistence/`

This directory contains the data persistence layer, managing database interactions.

- `repository.py`: Defines an abstract repository pattern with in-memory and SQLAlchemy implementations.

## Installation

- `Clone the repository`:
   git clone https://github.com/tramiNGY/holbertonschool-hbnb.git
- `Navigate to the project directory`:
  cd part3/hbnb/app
- `Create a virtual environment and activate it`:
  python3 -m venv venv
  source venv/bin/activate
- `Install dependencies`:
  pip install flask && pip install flask-restx && pip install  flask-bcrypt && pip install flask-jwt-extended && pip install sqlalchemy && pip install flask_sqlalchemy
- `Running the API`
  python run.py
The API will be available at http://localhost:5000/api/v1/

## API Endpoints
### `Users`
- POST /api/v1/users/ - Create a new user
- GET /api/v1/users/ - Retrieve all users
- GET /api/v1/users/<user_id> - Retrieve a specific user
- PUT /api/v1/users/<user_id> - Update a user
- DELETE /api/v1/users/<user_id> - Delete a user
- POST /api/v1/users/admin: Create a new user.
- PUT /api/v1/users/admin/<user_id>: Modify a user's details, including email and password.

### `Places`
- POST /api/v1/places/ - Create a new place
- GET /api/v1/places/ - Retrieve all places
- GET /api/v1/places/<place_id> - Retrieve a specific place
- PUT /api/v1/places/<place_id> - Update a place
- DELETE /api/v1/places/<place_id> - Delete a place

### `Reviews`
- POST /api/v1/reviews/ - Create a new review
- GET /api/v1/reviews/ - Retrieve all reviews
- GET /api/v1/reviews/<review_id> - Retrieve a specific review
- PUT /api/v1/reviews/<review_id> - Update a review
- DELETE /api/v1/reviews/<review_id> - Delete a review

### `Amenities`
- POST /api/v1/amenities/ - Create a new amenity
- GET /api/v1/amenities/ - Retrieve all amenities
- GET /api/v1/amenities/<amenity_id> - Retrieve a specific amenity
- PUT /api/v1/amenities/<amenity_id> - Update an amenity
- DELETE /api/v1/amenities/<amenity_id> - Delete an amenity
- POST /api/v1/amenities/admin: Add a new amenity.
- PUT /api/v1/amenities/admin/<amenity_id>: Modify the details of an amenity.


## Testing the API  

To ensure the reliability and correctness of the API, **unit tests** have been implemented using `unittest`. These tests cover all major functionalities, including resource creation, retrieval, updating, and deletion.  

### `Curl tests`

- **Here is an exemple of a cURL test for a POST api that you can run while the run.py file is running:**

  get admin token :  curl http://127.0.0.1:5000/api/v1/auth/generate_admin_token

curl -X POST "http://127.0.0.1:5000/api/v1/users/admin" 
-d '{"email": "newuser@example.com", "first_name": "Admin", "last_name": "User"}' 
-H "Authorization: Bearer <admin_token>" 
-H "Content-Type: application/json"

- **Expected output:**

   `{
  "id": "1"
  "email": "newuser@example.com",
  "password": "password123"
  "first_name": "Admin"
  "last_name": "User"
  "place_list": ["Modern House"]
}`

## AUTHORS
- [Tra Mi NGUYEN](https://github.com/tramiNGY)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Tom DIBELLONIO](https://github.com/totomus83)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Raphael DOTT](https://github.com/Raphaeldott)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
