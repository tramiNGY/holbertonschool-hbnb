import unittest
from app import create_app
from app.services import facade

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "password": "securepassword",
            "place_list": []
        })
        self.assertEqual(response.status_code, 201)

        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['first_name'], "Jane")
        self.assertEqual(data['last_name'], "Doe")
        self.assertEqual(data['email'], "jane.doe@example.com")
        self.assertEqual(data['place_list'], [])

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email",
            "password": "",
            "place_list": []
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_duplicate_email(self):
        # Create first user
        self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "securepassword",
            "place_list": []
        })
        
        # Try to create another user with the same email
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Johnny",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "anotherpassword",
            "place_list": []
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_get_all_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_user_by_id(self):
        # Create a user first
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com",
            "password": "securepassword",
            "place_list": []
        })
        user_id = create_response.get_json().get('id')
        
        # Retrieve the created user
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['email'], "alice@example.com")

    def test_get_user_not_found(self):
        response = self.client.get('/api/v1/users/99999')
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        # Create a user first
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "Bob",
            "last_name": "Brown",
            "email": "bob@example.com",
            "password": "securepassword",
            "place_list": []
        })
        user_id = create_response.get_json().get('id')
        
        # Update user details
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Robert",
            "last_name": "Brown",
            "email": "bob@example.com",
            "password": "securepassword",
            "place_list": []
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['first_name'], "Robert")

    def test_update_user_not_found(self):
        response = self.client.put('/api/v1/users/99999', json={
            "first_name": "Unknown",
            "last_name": "User",
            "email": "unknown@example.com",
            "password": "securepassword",
            "place_list": []
        })
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
