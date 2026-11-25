
import unittest
from calculator import add, subtract


class CalculatorTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, 3), 1)

    def test_subtract_negative(self):
        self.assertEqual(subtract(3, 8), -5)


if __name__ == "__main__":
    unittest.main()
