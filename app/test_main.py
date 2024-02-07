""" some basic tests because my focus is on CICD 

author: ashraf minhaj
co-author: chatGPT
mail: ashraf_minhaj@yahoo.com
"""
import unittest
import json
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_health(self):
        response = self.app.get('/health')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'ok')

    def test_info(self):
        response = self.app.get('/info')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['version'], '1.2')
        self.assertEqual(data['message'], 'bro, this works on your machine too')

if __name__ == '__main__':
    unittest.main()
