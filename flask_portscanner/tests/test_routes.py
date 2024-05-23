import unittest
from app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_scan(self):
        response = self.client.post('/scan', data={'target': '127.0.0.1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Scan Results', response.data)

if __name__ == '__main__':
    unittest.main()
