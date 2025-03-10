import unittest
from app import create_app
from app.services import facade

class TestReviewEndpoints(unittest.TestCase):
    """Test Class for testing review endpoints"""
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
    def test_create_review(self):
        # Success create new review
        response = self.client.post('/api/v1/reviews/', json={
        "comment" : "waow amazing!",
        "rating" : 5,
        "user_id" : "689987644",
        "place_id" : "76543468"
        })
        self.assertEqual(response.status_code, 201)
        
    def test_create_review_invalid_data(self):
        # Fail creation of new review with incorrect informations data
        response = self.client.post('/api/v1/reviews/', json={
        "comment" : 5,
        "rating" : "Nice!",
        "user_id" : "",
        "place_id" : ""
        })
        self.assertEqual(response.status_code, 400)
        
    def test_get_all_review(self):
        # Success/Fail retrieving all reviews
        response = self.client.get('/api/v1/reviews/')
        self.assertIn(response.status_code, [200, 404])
        
    def test_update_review(self):
        # Success/Fail updating a review
        review_id = "review1"
        response = self.client.put(f'/api/v1/reviews/{review_id}', json={
        "comment": "Awesome",
        "rating": 4
        })
        self.assertIn(response.status_code, [200, 404])

    def test_delete_review(self):
        # Success/Fail deleting a review
        review_id = "review2"
        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertIn(response.status_code, [200, 404])

if __name__ == "__main__":
    unittest.main()
