to be changed for part 3
![printf image image (1)](https://pbs.twimg.com/media/Gj1Hgv2XYAAiHmC?format=jpg&name=small)


# **HBnB Evolution - RESTful API**

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

## Project Structure
![structure](https://i.postimg.cc/RZrz8D16/hbnb-api-structure.png)


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

## Testing the API  

To ensure the reliability and correctness of the API, **unit tests** have been implemented using `unittest`. These tests cover all major functionalities, including resource creation, retrieval, updating, and deletion.  

### `Curl tests`

- **Here is an exemple of a cURL test for a POST api that you can run while the run.py file is running:**

  `curl -X POST http://localhost:5000/api/v1/reviews
-H "Content-Type: application/json" \
-d '{
    "comment": "Great place, really enjoyed my stay!",
    "rating": 5,
    "user_id": 1,
    "place_id": 10
}'`

- **Expected output:**

   `{
  "comment": "Great place, really enjoyed my stay!",
  "rating": 5,
  "user_id": 1,
  "place_id": 10
}`


### `Running the Unitests`

To run the test suite, use the following command in the root directory of your project:  
python -m app.tests.<file_name>
Each test case checks for correct status codes **(200 OK, 201 Created, 400 Bad Request, 404 Not Found)**

### Amenity Tests

- **test_create_amenity** → Create a new amenity (✅ success)
- **test_create_invalid_amenity** → Fail to create an amenity with invalid data (❌ fail)
- **test_get_all_amenities** → Retrieve all amenities (✅/❌ success or not found)
- **test_get_amenity_by_id** → Retrieve an amenity by ID (✅/❌ success or not found)
- **test_update_amenity** → Update an amenity (✅/❌ success or not found)

### Place Tests

- **test_create_place** → Create a new place (✅ success)
- **test_create_place_invalid_data** → Fail to create a place with invalid data (❌ fail)
- **test_create_out_of_range** → Fail to create a place with out-of-range latitude/longitude (❌ fail)
- **test_get_all_places** → Retrieve all places (✅/❌ success or not found)
- **test_get_place_by_id** → Retrieve a place by ID (✅/❌ success or not found)
- **test_update_place** → Update a place (✅/❌ success or not found)

### Review Tests

- **test_create_review** → Create a new review (✅ success)
- **test_create_review_invalid_data** → Fail to create a review with invalid data (❌ fail)
- **test_get_all_review** → Retrieve all reviews (✅/❌ success or not found)
- **test_update_review** → Update a review (✅/❌ success or not found)
- **test_delete_review** → Delete a review (✅/❌ success or not found)

### User Tests

- **test_create_user** → Create a new user (✅ success)
- **test_create_user_invalid_data** → Fail to create a user with invalid data (❌ fail)
- **test_create_user_duplicate_email** → Fail to create a user with an existing email (❌ fail)
- **test_get_all_users** → Retrieve all users (✅ success)
- **test_get_user_by_id** → Retrieve a user by ID (✅ success)
- **test_get_user_not_found** → Fail to retrieve a user with a non-existent ID (❌ fail)
- **test_update_user** → Update user information (✅ success)
- **test_update_user_not_found** → Fail to update a user that does not exist (❌ fail)



## AUTHORS
- [Tra Mi NGUYEN](https://github.com/tramiNGY)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Tom DIBELLONIO](https://github.com/totomus83)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Raphael DOTT](https://github.com/Raphaeldott)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
