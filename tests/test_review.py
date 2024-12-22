#!/usr/bin/python3
"""Test suite for the Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for the Review class."""

    def test_attributes(self):
        """Test that Review has the correct attributes."""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
