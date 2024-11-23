#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "user_id"))

if __name__ == "__main__":
    unittest.main()
