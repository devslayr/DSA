import unittest
from test import longest_rising_sublist

class TestLongestRisingSublist(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(longest_rising_sublist([]), 0)

    def test_single(self):
        self.assertEqual(longest_rising_sublist([5]), 1)

    def test_all_equal(self):
        self.assertEqual(longest_rising_sublist([5, 5, 5]), 1)

    def test_strict_increasing(self):
        self.assertEqual(longest_rising_sublist([1, 2, 3, 4]), 4)

    def test_multiple_segments(self):
        self.assertEqual(longest_rising_sublist([3, 4, 6, 2, 5, 7, 8, 1]), 4)

    def test_decreasing(self):
        self.assertEqual(longest_rising_sublist([5, 4, 3, 2]), 1)

    def test_plateau_then_increase(self):
        self.assertEqual(longest_rising_sublist([1, 1, 2, 3, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()
