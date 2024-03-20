import unittest

# Example function to be tested
def add(x, y):
    return x + y

# Test cases for the add function
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -3), 7)
        self.assertEqual(add(-10, 10), 0)

if __name__ == '__main__':
    unittest.main()