
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
    "id": "2f4bdca0-acbf-414b-8183-e95b59289cf8",
    "first_name": "John",
    "last_name": "Doe",
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
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MzY4NjY1NCwianRpIjoiOGQ3YTM3MDMtNjUxYi00NzYyLTkxYzktNzQzYTFkOWE1MTk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmNGJkY2EwLWFjYmYtNDE0Yi04MTgzLWU5NWI1OTI4OWNmOCIsIm5iZiI6MTc0MzY4NjY1NCwiY3NyZiI6Ijc1ZTQzNTYxLWIwMjMtNGEzYi1iOWJmLTllNTU3MGJiY2IzNiIsImV4cCI6MTc0Mzc3MzA1NCwiaXNfYWRtaW4iOmZhbHNlfQ.utKTQC0kwLgulWfftQw9ESHjJSo_pE4KNqUWJM1Oaj8"
}

```

#### **CURL PUT User**
- **Update User info by correct user**
```
curl -X PUT "http://127.0.0.1:5000/api/v1/users/a1986924-2c7f-42af-b87f-958d61378d2b" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MzY4NjY1NCwianRpIjoiOGQ3YTM3MDMtNjUxYi00NzYyLTkxYzktNzQzYTFkOWE1MTk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmNGJkY2EwLWFjYmYtNDE0Yi04MTgzLWU5NWI1OTI4OWNmOCIsIm5iZiI6MTc0MzY4NjY1NCwiY3NyZiI6Ijc1ZTQzNTYxLWIwMjMtNGEzYi1iOWJmLTllNTU3MGJiY2IzNiIsImV4cCI6MTc0Mzc3MzA1NCwiaXNfYWRtaW4iOmZhbHNlfQ.utKTQC0kwLgulWfftQw9ESHjJSo_pE4KNqUWJM1Oaj8" \
-H "Content-Type: application/json" \
-d '{
    "first_name": "John",
    "last_name": "Doe"
}'

```
- **Expected output**:

```
{
    "id": "2f4bdca0-acbf-414b-8183-e95b59289cf8",
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
    "id": "11697646-ce7a-4075-8845-8ab1ef6643bf",
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
    "access_token": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0Mzc3OTgzNywianRpIjoiOGFkOGEwZjMtOGY2NC00ZDcwLWEwNjAtN2UwMWZjNjc3ODM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjExNjk3NjQ2LWNlN2EtNDA3NS04ODQ1LThhYjFlZjY2NDNiZiIsIm5iZiI6MTc0Mzc3OTgzNywiY3NyZiI6IjFkOTJiYzMzLWI1ODQtNDRiNS1hNjEyLWRhZmFkNWQzZTc4NCIsImV4cCI6MTc0Mzg2NjIzNywiaXNfYWRtaW4iOmZhbHNlfQ.PZeRZk8-EBfrYb-NNZbMGOZ3xGNYA8Ynge_mqz9-0kM"
}


```

#### **CURL PUT User with wrong user**
- **Try to update John user's info by Anna**
```
curl -X PUT "http://127.0.0.1:5000/api/v1/users/2f4bdca0-acbf-414b-8183-e95b59289cf8" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0Mzc3OTgzNywianRpIjoiOGFkOGEwZjMtOGY2NC00ZDcwLWEwNjAtN2UwMWZjNjc3ODM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjExNjk3NjQ2LWNlN2EtNDA3NS04ODQ1LThhYjFlZjY2NDNiZiIsIm5iZiI6MTc0Mzc3OTgzNywiY3NyZiI6IjFkOTJiYzMzLWI1ODQtNDRiNS1hNjEyLWRhZmFkNWQzZTc4NCIsImV4cCI6MTc0Mzg2NjIzNywiaXNfYWRtaW4iOmZhbHNlfQ.PZeRZk8-EBfrYb-NNZbMGOZ3xGNYA8Ynge_mqz9-0kM" \
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
curl -X PUT "http://127.0.0.1:5000/api/v1/users/2f4bdca0-acbf-414b-8183-e95b59289cf8" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MzY4NjY1NCwianRpIjoiOGQ3YTM3MDMtNjUxYi00NzYyLTkxYzktNzQzYTFkOWE1MTk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmNGJkY2EwLWFjYmYtNDE0Yi04MTgzLWU5NWI1OTI4OWNmOCIsIm5iZiI6MTc0MzY4NjY1NCwiY3NyZiI6Ijc1ZTQzNTYxLWIwMjMtNGEzYi1iOWJmLTllNTU3MGJiY2IzNiIsImV4cCI6MTc0Mzc3MzA1NCwiaXNfYWRtaW4iOmZhbHNlfQ.utKTQC0kwLgulWfftQw9ESHjJSo_pE4KNqUWJM1Oaj8" -H "Content-Type: application/json" -d '{
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
curl -X PUT "http://127.0.0.1:5000/api/v1/users/2f4bdca0-acbf-414b-8183-e95b59289cf8" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MzY4NjY1NCwianRpIjoiOGQ3YTM3MDMtNjUxYi00NzYyLTkxYzktNzQzYTFkOWE1MTk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmNGJkY2EwLWFjYmYtNDE0Yi04MTgzLWU5NWI1OTI4OWNmOCIsIm5iZiI6MTc0MzY4NjY1NCwiY3NyZiI6Ijc1ZTQzNTYxLWIwMjMtNGEzYi1iOWJmLTllNTU3MGJiY2IzNiIsImV4cCI6MTc0Mzc3MzA1NCwiaXNfYWRtaW4iOmZhbHNlfQ.utKTQC0kwLgulWfftQw9ESHjJSo_pE4KNqUWJM1Oaj8" -H "Content-Type: application/json" -d '{
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
    "id": "86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9",
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
    "id": "86dc6bc0-a24e-4879-abd0-7e6cecb6921c",
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
    "id": "b3d1cf15-4482-4edf-bb99-8829d0c61b36",
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
    "name": "Pool",
    "description": "Outdoor swimming pool"
}'


```
- **Expected output**:

```
{
    "id": "bbed3e09-855e-438e-950f-552defdd296d",
    "name": "Pool",
    "description": "Outdoor swimming pool"
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
        "id": "86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9",
        "name": "WiFi",
        "description": "Super fast internet access"
    },
    {
        "id": "86dc6bc0-a24e-4879-abd0-7e6cecb6921c",
        "name": "Air Conditioning",
        "description": "Cool down with air conditioning"
    },
    {
        "id": "b3d1cf15-4482-4edf-bb99-8829d0c61b36",
        "name": "Parking",
        "description": "Free parking for guests"
    },
    {
        "id": "bbed3e09-855e-438e-950f-552defdd296d",
        "name": "Pool",
        "description": "Outdoor swimming pool"
    }
]

```

#### **CURL GET Amenity by amenity_id**
- **Get the amenity info base on amenity_id test with WiFi**
```
curl -X GET http://127.0.0.1:5000/api/v1/amenities/86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9 \
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
curl -X PUT http://127.0.0.1:5000/api/v1/amenities/86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9 \
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
    "id": "86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9",
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
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MzY4NjY1NCwianRpIjoiOGQ3YTM3MDMtNjUxYi00NzYyLTkxYzktNzQzYTFkOWE1MTk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmNGJkY2EwLWFjYmYtNDE0Yi04MTgzLWU5NWI1OTI4OWNmOCIsIm5iZiI6MTc0MzY4NjY1NCwiY3NyZiI6Ijc1ZTQzNTYxLWIwMjMtNGEzYi1iOWJmLTllNTU3MGJiY2IzNiIsImV4cCI6MTc0Mzc3MzA1NCwiaXNfYWRtaW4iOmZhbHNlfQ.utKTQC0kwLgulWfftQw9ESHjJSo_pE4KNqUWJM1Oaj8" \
-d '{
    "title": "Place-1",
    "description": "This is a test place",
    "price": 100.0,
    "latitude": 40.7128,
    "longitude": -74.0060,
    "associated_amenities": ["86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9", "86dc6bc0-a24e-4879-abd0-7e6cecb6921c", "b3d1cf15-4482-4edf-bb99-8829d0c61b36"]
}'

```
- **Expected output**:

```
{
    "id": "ef46b4db-b860-4381-848b-593add5a1df4",
    "title": "Place-1",
    "description": "This is a test place",
    "price": 100.0,
    "latitude": 40.7128,
    "longitude": -74.006,
    "associated_amenities": [
        "86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9",
        "86dc6bc0-a24e-4879-abd0-7e6cecb6921c",
        "b3d1cf15-4482-4edf-bb99-8829d0c61b36"
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
[
    {
        "id": "ef46b4db-b860-4381-848b-593add5a1df4",
        "title": "Updated Place-2",
        "description": "This is an updated test place",
        "price": 175.0,
        "latitude": 51.5075,
        "longitude": -0.128,
        "associated_amenities": [
            "86dc6bc0-a24e-4879-abd0-7e6cecb6921c",
            "bbed3e09-855e-438e-950f-552defdd296d",
            "86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9"
        ]
    }
]

```

#### **CURL GET Place by place_id**
- **Get the place's info by place_id test with Place-1**
```
curl -X GET "http://127.0.0.1:5000/api/v1/places/ef46b4db-b860-4381-848b-593add5a1df4"      -H "Authorization: Bearer <your_token>"

```
- **Expected output**:

```
{
    "place": {
        "id": "ef46b4db-b860-4381-848b-593add5a1df4",
        "title": "Updated Place-2",
        "description": "This is an updated test place",
        "price": 175.0,
        "latitude": 51.5075,
        "longitude": -0.128,
        "user_id": "2f4bdca0-acbf-414b-8183-e95b59289cf8"
    },
    "associated_amenities": [
        "86dc6bc0-a24e-4879-abd0-7e6cecb6921c",
        "86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9",
        "bbed3e09-855e-438e-950f-552defdd296d"
    ]
}

```
#### **CURL PUT place by correct owner**
- **Update assicated_amenities of John's place**:
```
curl -X PUT "http://127.0.0.1:5000/api/v1/places/ef46b4db-b860-4381-848b-593add5a1df4" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MzY4NjY1NCwianRpIjoiOGQ3YTM3MDMtNjUxYi00NzYyLTkxYzktNzQzYTFkOWE1MTk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmNGJkY2EwLWFjYmYtNDE0Yi04MTgzLWU5NWI1OTI4OWNmOCIsIm5iZiI6MTc0MzY4NjY1NCwiY3NyZiI6Ijc1ZTQzNTYxLWIwMjMtNGEzYi1iOWJmLTllNTU3MGJiY2IzNiIsImV4cCI6MTc0Mzc3MzA1NCwiaXNfYWRtaW4iOmZhbHNlfQ.utKTQC0kwLgulWfftQw9ESHjJSo_pE4KNqUWJM1Oaj8" \
-H "Content-Type: application/json" \
-d '{
    "title": "Updated Place-2",
    "description": "This is an updated test place",
    "price": 175.0,
    "latitude": 51.5075,
    "longitude": -0.1280,
    "associated_amenities": ["86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9", "86dc6bc0-a24e-4879-abd0-7e6cecb6921c", "bbed3e09-855e-438e-950f-552defdd296d"]
}'

```
- **Expected output**:
```
{
    "id": "ef46b4db-b860-4381-848b-593add5a1df4",
    "title": "Updated Place-2",
    "description": "This is an updated test place",
    "price": 175.0,
    "latitude": 51.5075,
    "longitude": -0.128,
    "associated_amenities": [
        "86dc6bc0-a24e-4879-abd0-7e6cecb6921c",
        "86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9",
        "bbed3e09-855e-438e-950f-552defdd296d"
    ]
}

```

#### **CURL PUT place by wrong owner**
- **Try update assicated_amenities of John's place by Anna**:
```
curl -X PUT "http://127.0.0.1:5000/api/v1/places/ef46b4db-b860-4381-848b-593add5a1df4" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0Mzc5MDA3MCwianRpIjoiYWQzZmQ0ZjAtNjkwZC00MDkzLThiYTgtNzNkNjg2ZDU5Mzk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjExNjk3NjQ2LWNlN2EtNDA3NS04ODQ1LThhYjFlZjY2NDNiZiIsIm5iZiI6MTc0Mzc5MDA3MCwiY3NyZiI6IjkzMWI1NGFjLWYwZjAtNGMwOC04OGRlLTU0ZDRjZjM1MWE4YSIsImV4cCI6MTc0Mzg3NjQ3MCwiaXNfYWRtaW4iOmZhbHNlfQ.IgAAz2M7QdIWsQX9bOtIF3k8o9Mg-usdrI7U-XvdkZc" \
-H "Content-Type: application/json" \
-d '{
    "title": "Updated Place-2",
    "description": "This is an updated test place",
    "price": 175.0,
    "latitude": 51.5075,
    "longitude": -0.1280,
    "associated_amenities": ["86d70ede-ad4a-4902-ae53-c5d2cf0c5ba9", "86dc6bc0-a24e-4879-abd0-7e6cecb6921c", "8a37fddc-db3c-4d11-abbd-030858c23390"]
}'

```
- **Expected output**:
```
{
    "error": "Unauthorized action"
}

```

### CURL REVIEW
#### **CURL POST Review**
- **Create new review on Place1 owned by John, reviews by Anna (not by the owner)**
```
curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0Mzc5MDA3MCwianRpIjoiYWQzZmQ0ZjAtNjkwZC00MDkzLThiYTgtNzNkNjg2ZDU5Mzk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjExNjk3NjQ2LWNlN2EtNDA3NS04ODQ1LThhYjFlZjY2NDNiZiIsIm5iZiI6MTc0Mzc5MDA3MCwiY3NyZiI6IjkzMWI1NGFjLWYwZjAtNGMwOC04OGRlLTU0ZDRjZjM1MWE4YSIsImV4cCI6MTc0Mzg3NjQ3MCwiaXNfYWRtaW4iOmZhbHNlfQ.IgAAz2M7QdIWsQX9bOtIF3k8o9Mg-usdrI7U-XvdkZc" \
-H "Content-Type: application/json" \
-d '{"text": "Nice place", "rating": 4, "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"}'


```
- **Expected output**:

```
{
    "id": "04e18142-8143-472f-8f81-d9288028da1e",
    "text": "Nice",
    "rating": 4,
    "user_id": "fb13be43-fa7a-41b4-ab36-b2ddcd8c7b6a",
    "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"
}


```

#### **CURL POST another Review on same place with same user**
- **Create another review (but only one per place per user allowed**
```
curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0Mzc5MDA3MCwianRpIjoiYWQzZmQ0ZjAtNjkwZC00MDkzLThiYTgtNzNkNjg2ZDU5Mzk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjExNjk3NjQ2LWNlN2EtNDA3NS04ODQ1LThhYjFlZjY2NDNiZiIsIm5iZiI6MTc0Mzc5MDA3MCwiY3NyZiI6IjkzMWI1NGFjLWYwZjAtNGMwOC04OGRlLTU0ZDRjZjM1MWE4YSIsImV4cCI6MTc0Mzg3NjQ3MCwiaXNfYWRtaW4iOmZhbHNlfQ.IgAAz2M7QdIWsQX9bOtIF3k8o9Mg-usdrI7U-XvdkZc" \
-H "Content-Type: application/json" \
-d '{"comment": "second review", "rating": 4, "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"}'


```
- **Expected output**:

```
{
    "error": "You have already reviewed this place"
}

```

#### **CURL PUT Review**
- **Update new review on Place1 owned by John, reviews by Anna (not by the owner)**
```
curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0Mzc5MDA3MCwianRpIjoiYWQzZmQ0ZjAtNjkwZC00MDkzLThiYTgtNzNkNjg2ZDU5Mzk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjExNjk3NjQ2LWNlN2EtNDA3NS04ODQ1LThhYjFlZjY2NDNiZiIsIm5iZiI6MTc0Mzc5MDA3MCwiY3NyZiI6IjkzMWI1NGFjLWYwZjAtNGMwOC04OGRlLTU0ZDRjZjM1MWE4YSIsImV4cCI6MTc0Mzg3NjQ3MCwiaXNfYWRtaW4iOmZhbHNlfQ.IgAAz2M7QdIWsQX9bOtIF3k8o9Mg-usdrI7U-XvdkZc" \
-H "Content-Type: application/json" \
-d '{"text": "Very nice", "rating": 5, "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"}'


```
- **Expected output**:

```
{
    "id": "04e18142-8143-472f-8f81-d9288028da1e",
    "text": "Very nice",
    "rating": 5,
    "user_id": "fb13be43-fa7a-41b4-ab36-b2ddcd8c7b6a",
    "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"
}

```

#### **CURL GET ALL REVIEWS**
- **Get all reviews on all places**
```
curl -X GET http://127.0.0.1:5000/api/v1/reviews/ -H "Authorization: Bearer <your_token>"

```
- **Expected output**:

```
[
    {
        "id": "19d0c6bd-1c7c-4230-8284-5ab7837aea1e",
        "text": "Test other user comment",
        "rating": 4,
        "user_id": "11697646-ce7a-4075-8845-8ab1ef6643bf",
        "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"
    },
    {
        "id": "3e00a05a-f9ea-426e-93ca-805ee345cb17",
        "text": "Wonderful placet",
        "rating": 5,
        "user_id": "e4fb5b3b-7620-4778-af4e-a613386e5907",
        "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"
    },
    {
        "id": "04e18142-8143-472f-8f81-d9288028da1e",
        "text": "Very nice",
        "rating": 5,
        "user_id": "fb13be43-fa7a-41b4-ab36-b2ddcd8c7b6a",
        "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"
    }
]

```

#### **CURL GET REVIEW BY ID**
- **Get review by its id**
```
curl -X GET http://127.0.0.1:5000/api/v1/reviews/ -H "Authorization: Bearer <your_token>"

```
- **Expected output**:

```
{
    "id": "04e18142-8143-472f-8f81-d9288028da1e",
    "text": "Very nice",
    "rating": 5,
    "user_id": "fb13be43-fa7a-41b4-ab36-b2ddcd8c7b6a",
    "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"
}

```

#### **DELETE REVIEW BY CORRECT USER**
- **Delete a review by the user who wrote it**
```
curl -X DELETE "http://127.0.0.1:5000/api/v1/reviews/19d0c6bd-1c7c-4230-8284-5ab7837aea1e" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0Mzc5MDA3MCwianRpIjoiYWQzZmQ0ZjAtNjkwZC00MDkzLThiYTgtNzNkNjg2ZDU5Mzk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjExNjk3NjQ2LWNlN2EtNDA3NS04ODQ1LThhYjFlZjY2NDNiZiIsIm5iZiI6MTc0Mzc5MDA3MCwiY3NyZiI6IjkzMWI1NGFjLWYwZjAtNGMwOC04OGRlLTU0ZDRjZjM1MWE4YSIsImV4cCI6MTc0Mzg3NjQ3MCwiaXNfYWRtaW4iOmZhbHNlfQ.IgAAz2M7QdIWsQX9bOtIF3k8o9Mg-usdrI7U-XvdkZc" \
-H "Content-Type: application/json" \
-d '{"comment": "Test other user comment", "rating": 4, "place_id": "ef46b4db-b860-4381-848b-593add5a1df4"}'


```
- **Expected output**:

```
{
    "message": "Review deleted successfully"
}

```

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
