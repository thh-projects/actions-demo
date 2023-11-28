import unittest
from calculations import *

class TestCalculations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertFalse(add(2, 2) == 4)
        self.assertTrue(add(2, 2) == 4)
        self.assertRaises(TypeError, add("x", "y"))

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_power(self):
        self.assertEqual(power(3, 5), 243)

if __name__ == '__main__':
    unittest.main()