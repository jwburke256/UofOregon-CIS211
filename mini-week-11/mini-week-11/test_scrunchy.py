"""Test cases for scrunchy.py"""

from scrunchy import *
import unittest


class TestScrunch(unittest.TestCase):
    def test_scrunch_sum(self):
        """Scrunching rows by summing them"""
        g = ScrunchableBySum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        g.scrunch()
        self.assertEqual(g, ScrunchableBySum([[6], [15], [24]]))
        # It's as scrunched as it gets
        g.scrunch()
        self.assertEqual(g, ScrunchableBySum([[6], [15], [24]]))

    def test_scrunch_min(self):
        """Scrunching rows by taking their minimum"""
        g = ScrunchableByMin([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        g.scrunch()
        self.assertEqual(g, ScrunchableBySum([[1], [4], [7]]))
        # It's as scrunched as it gets
        # (this is called "idempotence", by the way)
        g.scrunch()
        self.assertEqual(g, ScrunchableBySum([[1], [4], [7]]))

    def test_scrunch_product(self):
        g = ScrunchableByProduct([[2, 3], [5, 2], [3, 8]])
        g.scrunch()
        self.assertEqual(g, ScrunchableBySum([[6], [10], [24]]))


if __name__ == "__main__":
    unittest.main()
