import unittest
from app import create_app
from app.services import facade

class TestPlaceEndpoints(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_create_place(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 75.0,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner": "user123",
            "reviews": [],
            "amenities": ["wifi", "kitchen"]
        })
        self.assertEqual(response.status_code, 201)
        
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['title'], "Cozy Apartment")
        self.assertEqual(data['price'], 75.0)
        self.assertEqual(data['latitude'], 48.8566)
        self.assertEqual(data['longitude'], 2.3522)
        self.assertEqual(data['owner'], "user123")
        self.assertEqual(data['amenities'], ["wifi", "kitchen"])
    
    def test_create_place_invalid_data(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": -50.0,
            "latitude": "invalid",
            "longitude": None,
            "owner": "",
            "reviews": "",
            "amenities": "not_a_list"
        })
        self.assertEqual(response.status_code, 400)
    
    def test_create_out_of_range(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "villa",
            "description": "vue sur mer",
            "price": 3000000,
            "latitude": 100,
            "longitude": 190,
            "owner": "tom",
            "reviews": ["wonderful"],
            "amenities": ["toilette"]
        })
    
    def test_get_all_places(self):
        response = self.client.get('/api/v1/places/')
        self.assertIn(response.status_code, [200, 404])  # 200 if places exist, 404 if none
    
    def test_get_place_by_id(self):
        place_id = "place123"
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertIn(response.status_code, [200, 404])  # 200 if exists, 404 if not
    
    def test_update_place(self):
        place_id = "place123"
        response = self.client.put(f'/api/v1/places/{place_id}', json={
            "title": "Updated Apartment",
            "description": "A newly renovated place",
            "price": 100.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "amenities": ["wifi", "pool"]
        })
        self.assertIn(response.status_code, [200, 404])  # 200 if updated, 404 if not found
        
        if response.status_code == 200:
            data = response.get_json()
            self.assertEqual(data['title'], "Updated Apartment")
            self.assertEqual(data['price'], 100.0)
            self.assertEqual(data['latitude'], 40.7128)
            self.assertEqual(data['longitude'], -74.0060)
            self.assertEqual(data['amenities'], ["wifi", "pool"])

if __name__ == '__main__':
    unittest.main()
