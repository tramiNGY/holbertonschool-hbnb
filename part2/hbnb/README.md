part 2 Implementation of Business Logic and API Endpoints
# HBnB Evolution - RESTful API

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

## Directory Overview

### `app/models/`

This directory contains the data models used in the API. Each model represents a different entity:

- `user.py`: Defines the User model with attributes like `first_name`, `last_name`, `email`, and `password`.
- `place.py`: Defines the Place model, including attributes like `title`, `description`, `price`, `latitude`, and `longitude`.
- `review.py`: Defines the Review model, storing user feedback on places.
- `amenity.py`: Defines the Amenity model, storing amenities available for places.

### `app/api/v1/`

This directory contains the API endpoints that handle requests and responses.

- `users.py`: Handles user-related operations (creation, retrieval, update, and deletion).
- `places.py`: Manages places, including creating, updating, and retrieving places.
- `reviews.py`: Manages reviews left by users for different places.
- `amenities.py`: Manages amenities available at different places.

### `app/services/`

This directory contains the business logic layer, abstracting the logic from the API endpoints.

- `facade.py`: Implements a Facade pattern to centralize business logic, ensuring API endpoints remain lightweight.

### `app/persistence/`

This directory contains the data persistence layer, managing database interactions.

- `repository.py`: Provides functions for fetching, creating, updating, and deleting records from the database.

## Installation

- `Clone the repository`:
   git clone https://github.com/tramiNGY/holbertonschool-hbnb.git
- `Navigate to the project directory`:
  cd part2/hbnb/app
- `Create a virtual environment and activate it`:
  python3 -m venv venv
  source venv/bin/activate
- `Install dependencies`:
  pip install flask && pip install flask-restx
- `Running the API`
  python run.py
The API will be available at http://localhost:5000/api/v1/

Testing
To run the test suite, use:
  python -m app.tests.<file_name>

## API Endpoints
### `Users`
- POST /api/v1/users/ - Create a new user
- GET /api/v1/users/ - Retrieve all users
- GET /api/v1/users/<user_id> - Retrieve a specific user
- PUT /api/v1/users/<user_id> - Update a user
- DELETE /api/v1/users/<user_id> - Delete a user

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
