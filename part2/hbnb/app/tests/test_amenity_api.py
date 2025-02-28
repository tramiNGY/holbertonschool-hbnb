import unittest
from app import create_app
from app.services import facade

class TestAmenityEndpoints(unittest.TestCase):
    """Test Class for testing amenity endpoints"""
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        # Success create new amenity
        response = self.client.post('/api/v1/amenities/', json={
            "name": "wifi",
            "description": "5ghz"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_invalid_amenity(self):
        # Fail creation of new amenity with incorrect informations data
        response = self.client.post('/api/v1/amenities/', json={
            "name": "",
            "description": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_get_all_amenities(self):
        # Success/Fail retrieving all amenities
        response = self.client.get('/api/v1/amenities/')
        self.assertIn(response.status_code, [200, 404])

    def test_get_amenity_by_id(self):
        # Success/Fail retrieving amenity by id
        amenity_id = "amenity1"
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertIn(response.status_code, [200, 404])

    def test_update_amenity(self):
        # Success/Fail update amenity
        amenity_id = "amenity1"
        response = self.client.put(f'/api/v1/amenity/{amenity_id}', json={
            "name": "wifi",
            "description": "adsl"
        })
        self.assertIn(response.status_code, [200, 404])

if __name__ == '__main__':
    unittest.main()
