import unittest
from fastapi.testclient import TestClient
from main import app

class TestFacebookScraper(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_facebook_posts_success(self):
        # Send request to endpoint
        response = self.client.get(f"/posts/")
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("posts", data)
        self.assertTrue(isinstance(data["posts"], list))
        self.assertTrue(len(data["posts"]) > 0)

    def test_get_facebook_posts_failure(self,invalid_token ="invalid"):
        # Send request to endpoint
        response = self.client.get(f"/posts/access_token={invalid_token}")
        
        # Check response
        self.assertEqual(response.status_code, 404)

    def test_read_root(self):
        # Test the default root endpoint
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Welcome to the Facebook scraping service.")

if __name__ == "__main__":
    unittest.main()
