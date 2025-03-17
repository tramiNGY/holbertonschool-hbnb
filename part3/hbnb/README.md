
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

Our HBNB app uses JWT (JSON Web Tokens) for user authentication and authorization. JWTs are used to securely transmit information between parties as a JSON object. In this application, JWTs are used to authenticate users and authorize them to access protected routes. Certain routes in the application are protected and require the user to provide a valid JWT in the Authorization header to access them. These routes are secured using the @jwt_required() decorator, which ensures that the user is authenticated before accessing the route.

### For regular users

When a user logs in with their email and password, the application verifies their credentials and generates a JWT if the credentials are valid. This JWT is then returned to the user and can be used for subsequent requests to access protected routes. This happens during the post request to login, the server verifies if the provided email exists in the database and whether the password is correct.
If the credentials are valid, an access token is generated using `create_access_token`. 

### For admin

Certain routes are restricted to users with administrative privileges. These routes check the is_admin claim in the JWT to ensure that the user has admin privileges before allowing access. The user must be authenticated and must have the `is_admin` claim set to True in the JWT to access the route.
If the user is not an admin, the request is rejected with a 403 Forbidden status code.
#### Enter this curl command to get an admin token:
- curl http://127.0.0.1:5000/api/v1/auth/generate_admin_token

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

## CURL TESTS

### Curl tests for Regular User (Not Admin)

### CURL USER
#### **CURL POST User**
- **Create new user John**
```
curl -X POST http://127.0.0.1:5000/api/v1/users/ -H "Content-Type: application/json" -H "Authorization: Bearer <your-jwt-token>" -d '{ "first_name": "John", "last_name": "Voe", "email": "john.doe@example.com", "password": "securePassword123"}'

```
- **Expected output**:

```
{
    "id": "e47e6410-d278-47ca-a3b7-e5d0e266fe1e",
    "first_name": "John",
    "last_name": "Voe",
    "email": "john.doe@example.com"
}

```

#### **CURL POST Login**
- **Login with User John**
```
curl -X POST http://127.0.0.1:5000/api/v1/auth/login -H "Content-Type: application/json" -d '{ "email": "john.doe@example.com", "password": "securePassword123" }'

```
- **Expected output**:

```
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjE1NDc1NSwianRpIjoiYTQ0NmU3MWItNWFjMC00MjY2LWJlOWItODZjOGNiMWVkNDk1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImU0N2U2NDEwLWQyNzgtNDdjYS1hM2I3LWU1ZDBlMjY2ZmUxZSIsIm5iZiI6MTc0MjE1NDc1NSwiY3NyZiI6ImY5Mjc4ZjE0LTFlNjctNDRlZS04NTdmLWE3ZDc1YjRkMDEzNyIsImV4cCI6MTc0MjI0MTE1NSwiaXNfYWRtaW4iOmZhbHNlfQ.ZS9hVTwqddzRnKuyUgb8s5o6YuDPh1NIzhIg6BOVEsQ"
}

```

#### **CURL PUT User**
- **Update User info by correct user**
```
curl -X PUT "http://127.0.0.1:5000/api/v1/users/a1986924-2c7f-42af-b87f-958d61378d2b" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjEzMzE5MSwianRpIjoiYTQ3NTM0NTUtM2M3Ni00NGI4LTk5OWEtMzU5Y2JkMzljNWJjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImExOTg2OTI0LTJjN2YtNDJhZi1iODdmLTk1OGQ2MTM3OGQyYiIsIm5iZiI6MTc0MjEzMzE5MSwiY3NyZiI6IjMzNTRkNmQ3LWMxN2YtNDgzOC04MTZlLTdjMjRjODZlNTliOSIsImV4cCI6MTc0MjIxOTU5MSwiaXNfYWRtaW4iOmZhbHNlfQ.Fl8PpIfNspyWeu8pqhHYc8w-tU-Xj4fO7DtT4wxbP1Y" \
-H "Content-Type: application/json" \
-d '{
    "first_name": "John",
    "last_name": "Doe"
}'

```
- **Expected output**:

```
{
    "id": "a1986924-2c7f-42af-b87f-958d61378d2b",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}

```

#### **CURL POST another User**
- **Create User Anna**
```
curl -X POST http://127.0.0.1:5000/api/v1/users/ -H "Content-Type: application/json" -H "Authorization: Bearer <your-jwt-token>" -d '{ "first_name": "Anna", "last_name": "Doe", "email": "anna.doe@example.com", "password": "securePassword123"}'

```
- **Expected output**:

```
{
    "id": "09174248-810d-49b4-99ed-d642884f822b",
    "first_name": "Anna",
    "last_name": "Doe",
    "email": "anna.doe@example.com"
}

```

#### **CURL POST Login with another user**
- **Login with user Anna**
```
curl -X POST http://127.0.0.1:5000/api/v1/auth/login -H "Content-Type: application/json" -d '{ "email": "anna.doe@example.com", "password": "securePassword123" }'

```
- **Expected output**:

```
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjE1NDgyMywianRpIjoiNmI4MjEwYzktMTlhNC00ZjY3LTkzYWQtMzNmNDUzM2JmYWYzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjA5MTc0MjQ4LTgxMGQtNDliNC05OWVkLWQ2NDI4ODRmODIyYiIsIm5iZiI6MTc0MjE1NDgyMywiY3NyZiI6IjFjNjhhNjI2LTAwNGEtNGVmZC04MDY0LTBlZjE4NjBkYTRjYyIsImV4cCI6MTc0MjI0MTIyMywiaXNfYWRtaW4iOmZhbHNlfQ.HY-k95j5h0bWHUn4pHi2ua8DvA1A2HajSZWnJwIfNtA"
}


```

#### **CURL PUT User with wrong user**
- **Try to update John user's info by Anna**
```
curl -X PUT "http://127.0.0.1:5000/api/v1/users/a1986924-2c7f-42af-b87f-958d61378d2b" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjE1MTc5MCwianRpIjoiODBiYTA2NTItZDEyOS00NzhiLWI1OGItN2VhMTI5NDBkYWMwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjViZGM1NTkzLWRiODAtNDA0OS05MWYxLWI2OWU3MmVjOWNjYiIsIm5iZiI6MTc0MjE1MTc5MCwiY3NyZiI6IjExN2QyNzNiLTFjMzktNDE3ZC1iMWU0LWQzNDI3YjY0NzUxOCIsImV4cCI6MTc0MjIzODE5MCwiaXNfYWRtaW4iOmZhbHNlfQ.J5FXrIhcjYk-wRHpCfFiOhD1-hp6chweKr_QsC5ihk8" \
-H "Content-Type: application/json" \
-d '{                             
    "first_name": "UpdatedFirstNamebyAnna",
    "last_name": "UpdatedLastNamebyAnna"
}'


```
- **Expected output**:

```
{
    "error": "Unauthorized action"
}

```

#### **CURL PUT User Update email by correct user**
- **Try to update John email by John but email is not allowed to be modified**
```
curl -X PUT "http://127.0.0.1:5000/api/v1/users/a1986924-2c7f-42af-b87f-958d61378d2b" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjEzMzE5MSwianRpIjoiYTQ3NTM0NTUtM2M3Ni00NGI4LTk5OWEtMzU5Y2JkMzljNWJjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImExOTg2OTI0LTJjN2YtNDJhZi1iODdmLTk1OGQ2MTM3OGQyYiIsIm5iZiI6MTc0MjEzMzE5MSwiY3NyZiI6IjMzNTRkNmQ3LWMxN2YtNDgzOC04MTZlLTdjMjRjODZlNTliOSIsImV4cCI6MTc0MjIxOTU5MSwiaXNfYWRtaW4iOmZhbHNlfQ.Fl8PpIfNspyWeu8pqhHYc8w-tU-Xj4fO7DtT4wxbP1Y" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe", 
    "email": "john2.doe@email.com"
}'

```
- **Expected output**:

```
{
    "error": "You cannot modify email or password"
}

```

#### **CURL PUT User Update password by correct user**
- **Try to update John password by John but password is not allowed to be modified**
```
curl -X PUT "http://127.0.0.1:5000/api/v1/users/a1986924-2c7f-42af-b87f-958d61378d2b" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjEzMzE5MSwianRpIjoiYTQ3NTM0NTUtM2M3Ni00NGI4LTk5OWEtMzU5Y2JkMzljNWJjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImExOTg2OTI0LTJjN2YtNDJhZi1iODdmLTk1OGQ2MTM3OGQyYiIsIm5iZiI6MTc0MjEzMzE5MSwiY3NyZiI6IjMzNTRkNmQ3LWMxN2YtNDgzOC04MTZlLTdjMjRjODZlNTliOSIsImV4cCI6MTc0MjIxOTU5MSwiaXNfYWRtaW4iOmZhbHNlfQ.Fl8PpIfNspyWeu8pqhHYc8w-tU-Xj4fO7DtT4wxbP1Y" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe", 
    "password": "123!"
}'

```
- **Expected output**:

```
{
    "error": "You cannot modify email or password"
}

```

### CURL AMENITY
#### **CURL POST Amenity**
- **Create new amenity Wifi**
```
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
    "name": "WiFi",
    "description": "High-speed internet access"
}'

```
- **Expected output**:

```
{
    "id": "188628e7-8af7-4dc9-8fb8-1879f69a7f43",
    "name": "WiFi",
    "description": "High-speed internet access"
}

```

#### **CURL POST Amenity**
- **Create new amenity Air Conditioning**
```
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
    "name": "Air Conditioning",
    "description": "Cool down with air conditioning"
}'


```
- **Expected output**:

```
{
    "id": "cb900d74-eeb0-47eb-a241-fb1996776f96",
    "name": "Air Conditioning",
    "description": "Cool down with air conditioning"
}

```

#### **CURL POST Amenity**
- **Create new amenity Parking**
```
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
    "name": "Parking",
    "description": "Free parking for guests"
}'


```
- **Expected output**:

```
{
    "id": "97563b0a-8bd8-4689-ad5c-ac4a5aa1586b",
    "name": "Parking",
    "description": "Free parking for guests"
}

```

#### **CURL POST Amenity**
- **Create new amenity Parking**
```
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
    "name": "Parking",
    "description": "Free parking for guests"
}'


```
- **Expected output**:

```
{
    "id": "97563b0a-8bd8-4689-ad5c-ac4a5aa1586b",
    "name": "Parking",
    "description": "Free parking for guests"
}

```

#### **CURL GET All Amenities**
- **Get all the amenities in the amenities database**
```
curl -X GET http://127.0.0.1:5000/api/v1/amenities/ \
-H "Authorization: Bearer <votre_token>"

```
- **Expected output**:

```
[
    {
        "id": "188628e7-8af7-4dc9-8fb8-1879f69a7f43",
        "name": "WiFi",
        "description": "High-speed internet access"
    },
    {
        "id": "cb900d74-eeb0-47eb-a241-fb1996776f96",
        "name": "Air Conditioning",
        "description": "Cool down with air conditioning"
    },
    {
        "id": "97563b0a-8bd8-4689-ad5c-ac4a5aa1586b",
        "name": "Parking",
        "description": "Free parking for guests"
    }
]

```

#### **CURL GET Amenity by amenity_id**
- **Get the amenity info base on amenity_id test with WiFi**
```
curl -X GET http://127.0.0.1:5000/api/v1/amenities/188628e7-8af7-4dc9-8fb8-1879f69a7f43 \
-H "Authorization: Bearer <votre_token>"

```
- **Expected output**:

```
{
    "id": "188628e7-8af7-4dc9-8fb8-1879f69a7f43",
    "name": "WiFi",
    "description": "High-speed internet access"
}
```

#### **CURL PUT Update Amenity's info**
- **Update amenity WiFi's info**
```
curl -X PUT http://127.0.0.1:5000/api/v1/amenities/188628e7-8af7-4dc9-8fb8-1879f69a7f43 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <votre_token>" \
-d '{
    "name": "WiFi",
    "description": "Super fast internet access"
}'

```
- **Expected output**:

```
{
    "id": "188628e7-8af7-4dc9-8fb8-1879f69a7f43",
    "name": "WiFi",
    "description": "Super fast internet access"
}

```


### CURL PLACE
#### **CURL POST Place**
- **Create new place Place-1 by John**
```
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjE1NDc1NSwianRpIjoiYTQ0NmU3MWItNWFjMC00MjY2LWJlOWItODZjOGNiMWVkNDk1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImU0N2U2NDEwLWQyNzgtNDdjYS1hM2I3LWU1ZDBlMjY2ZmUxZSIsIm5iZiI6MTc0MjE1NDc1NSwiY3NyZiI6ImY5Mjc4ZjE0LTFlNjctNDRlZS04NTdmLWE3ZDc1YjRkMDEzNyIsImV4cCI6MTc0MjI0MTE1NSwiaXNfYWRtaW4iOmZhbHNlfQ.ZS9hVTwqddzRnKuyUgb8s5o6YuDPh1NIzhIg6BOVEsQ" \
-d '{
    "title": "Place-1",
    "description": "This is a test place",
    "price": 100.0,
    "latitude": 40.7128,
    "longitude": -74.0060,
    "associated_amenities": ["WiFi", "Air Conditioning", "Parking"]
}'


```
- **Expected output**:

```
{
    "id": "53cf3bc0-cc72-40e7-8d86-a976d0c11fc6",
    "title": "Place-1",
    "description": "This is a test place",
    "price": 100.0,
    "latitude": 40.7128,
    "longitude": -74.006,
    "associated_amenities": [
        "WiFi",
        "Parking",
        "Air Conditioning"
    ]
}

```

#### **CURL GET ALL Places**
- **Get all the places in the places database**
```
curl -X GET http://127.0.0.1:5000/api/v1/places/ -H "Authorization: Bearer <your_token>"

```
- **Expected output**:

```
{
    "id": "53cf3bc0-cc72-40e7-8d86-a976d0c11fc6",
    "title": "Place-1",
    "description": "This is a test place",
    "price": 100.0,
    "latitude": 40.7128,
    "longitude": -74.006,
    "associated_amenities": [
        "Air Conditioning",
        "Parking",
        "WiFi"
    ]
}

```

#### **CURL GET Place by place_id**
- **Get the place's info by place_id test with Place-1**
```
curl -X GET "http://127.0.0.1:5000/api/v1/places/53cf3bc0-cc72-40e7-8d86-a976d0c11fc6"      -H "Authorization: Bearer <your_token>"

```
- **Expected output**:

```
{
    "place": {
        "id": "53cf3bc0-cc72-40e7-8d86-a976d0c11fc6",
        "title": "Place-1",
        "description": "This is a test place",
        "price": 100.0,
        "latitude": 40.7128,
        "longitude": -74.006,
        "user_id": "e47e6410-d278-47ca-a3b7-e5d0e266fe1e"
    },
    "associated_amenities": [
        "Parking",
        "WiFi",
        "Air Conditioning"
    ]
}

```
### CURL PLACE PUT AND CURL REVIEW
#### Curl are not posted here because issues need to be fixed first_name because Curl tests are failing for those.

### Curl tests for Admin

```
get admin token :  curl http://127.0.0.1:5000/api/v1/auth/generate_admin_token
```
#### Creating a user as an admin
```
curl -X POST "http://127.0.0.1:5000/api/v1/users/admin" -d '{"email": "newuser@example.com", "first_name": "Admin", "last_name": "User"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
```
- **Expected output:**

   `{
  "id": "1"
  "email": "newuser@example.com",
  "password": "password123"
  "first_name": "Admin"
  "last_name": "User"
  "place_list": ["Modern House"]
  #### Editing a user as an admin
```
curl -X PUT "http://127.0.0.1:5000/api/v1/users/admin/<userid>" -d '{"email": "updatedemail@example.com"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
```
- **Expected output:**

   `{
  "email": "updatedemail@example.com",
  "password": "password123"
  "first_name": "Admin"
  "last_name": "User"
  "place_list": ["Modern House"]
  }`
#### Creating an amenity as an admin
```
curl -X POST "http://127.0.0.1:5000/api/v1/amenities/admin" -d '{"name": "Swimming Pool", "description": "a 2 meter deep swimming pool"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
```
- **Expected output:**
   `{
"id": "1"
"name": "Swimming Pool", 
"description": "a 2 meter deep swimming pool"
}`
#### Editing an amenity as an admin
```
curl -X PUT "http://127.0.0.1:5000/api/v1/amenities/admin/<amenity_id>" -d '{"name": "Updated Amenity"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
```
- **Expected output:**
   `{
"name": "Updated Amenity", 
"description": "a 2 meter deep swimming pool"
}`

#### Deleting a place as an admin :
```
curl -X DELETE "http://127.0.0.1:5000/api/v1/places/admin/<placeid>" \
-H "Authorization: Bearer <admin_token>" \
-H "Content-Type: application/json"
```
- **Expected output:**
`Place has been deleted successfully !`
#### Deleting a review as an admin :
```
curl -X DELETE "http://127.0.0.1:5000/api/v1/reviews/admin/<reviewid>" \
-H "Authorization: Bearer <admin_token>" \
-H "Content-Type: application/json"
```
- **Expected output:**
`Review has been deleted successfully !`
## AUTHORS
- [Tra Mi NGUYEN](https://github.com/tramiNGY)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Tom DIBELLONIO](https://github.com/totomus83)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Raphael DOTT](https://github.com/Raphaeldott)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
