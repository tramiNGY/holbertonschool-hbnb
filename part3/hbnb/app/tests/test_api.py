import unittest
import json
from app import create_app  # Ensure that `create_app` is in your main app.py file to initialize the Flask app
from flask_jwt_extended import create_access_token


class TestAPI(unittest.TestCase):

    def setUp(self):
        """Prepare the app for testing"""
        self.app = create_app()  # Create an instance of the app
        self.client = self.app.test_client()
        self.app.testing = True
        
        # Create a test user and an access token
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "securePassword123",
            "place_list": []
        }
        
        # Authenticate the user to get the access token
        self.user_token = self.login_user(self.user_data['email'], self.user_data['password'])

    def login_user(self, email, password):
        """Simulate logging in the user to obtain a JWT"""
        response = self.client.post('/api/v1/auth/login', json={
            "email": email,
            "password": password
        })
        return json.loads(response.data)["access_token"]

    def test_create_place(self):
        """Test the creation of a place"""
        place_data = {
            "title": "New Place",
            "description": "A wonderful place to stay.",
            "price": 150.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner": "ca7f599b-7398-4a01-a080-6f0e281b7f9e",  # Valid user ID
            "amenities": ["WiFi", "AC"]
        }
        
        response = self.client.post('/api/v1/places/', 
                                    headers={"Authorization": f"Bearer {self.user_token}"},
                                    json=place_data)
        self.assertEqual(response.status_code, 201)  # Check if the place was created successfully
        self.assertIn("id", json.loads(response.data))  # Ensure the place ID is returned

    def test_unauthorized_place_update(self):
        """Test unauthorized attempt to update a place that the user does not own"""
        place_id = "some-valid-place-id"
        place_data = {
            "title": "Updated Place"
        }
        
        response = self.client.put(f'/api/v1/places/{place_id}', 
                                   headers={"Authorization": f"Bearer {self.user_token}"},
                                   json=place_data)
        self.assertEqual(response.status_code, 403)  # Check for unauthorized access
        self.assertEqual(json.loads(response.data)["error"], "Unauthorized action")

    def test_create_review(self):
        """Test the creation of a review for a place"""
        place_id = "valid-place-id"
        review_data = {
            "place_id": place_id,
            "rating": 5,
            "comment": "Great place!"
        }
        
        response = self.client.post('/api/v1/reviews/', 
                                    headers={"Authorization": f"Bearer {self.user_token}"},
                                    json=review_data)
        self.assertEqual(response.status_code, 201)  # Check if the review was created successfully
        self.assertIn("id", json.loads(response.data))  # Ensure the review ID is returned

    def test_update_review(self):
        """Test the update of a review"""
        review_id = "valid-review-id"
        review_data = {
            "comment": "Updated review",
            "rating": 4
        }
        
        response = self.client.put(f'/api/v1/reviews/{review_id}', 
                                   headers={"Authorization": f"Bearer {self.user_token}"},
                                   json=review_data)
        self.assertEqual(response.status_code, 200)  # Check if the update was successful
        self.assertEqual(json.loads(response.data)["comment"], "Updated review")

    def test_delete_review(self):
        """Test the deletion of a review"""
        review_id = "valid-review-id"
        
        response = self.client.delete(f'/api/v1/reviews/{review_id}', 
                                      headers={"Authorization": f"Bearer {self.user_token}"})
        self.assertEqual(response.status_code, 200)  # Check if the deletion was successful
        self.assertEqual(json.loads(response.data)["message"], "Review deleted successfully")

    def test_unauthorized_user_update(self):
        """Test unauthorized attempt to modify user data by another user"""
        user_id = "other-user-id"
        update_data = {
            "first_name": "Updated Name"
        }
        
        response = self.client.put(f'/api/v1/users/{user_id}', 
                                   headers={"Authorization": f"Bearer {self.user_token}"},
                                   json=update_data)
        self.assertEqual(response.status_code, 403)  # Check for unauthorized access
        self.assertEqual(json.loads(response.data)["error"], "Unauthorized action")

    # Public endpoints tests
    def test_get_places(self):
        """Test access to the list of places without authentication"""
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)  # Check if the response is correct
        places = json.loads(response.data)
        self.assertIsInstance(places, list)

    def test_get_place(self):
        """Test access to details of a specific place without authentication"""
        place_id = "valid-place-id"
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 200)  # Check if the response is correct
        place = json.loads(response.data)
        self.assertEqual(place["id"], place_id)  # Verify the place ID matches
        

if __name__ == "__main__":
    unittest.main()
