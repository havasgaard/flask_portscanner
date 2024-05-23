import unittest
from app.scanner.scanner import scan_ports


class ScannerTestCase(unittest.TestCase):
    def test_scan_ports(self):
        results = scan_ports('127.0.0.1')
        self.assertIsInstance(results, dict)
        self.assertIn(80, results)


if __name__ == '__main__':
    unittest.main()
