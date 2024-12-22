#!/usr/bin/python3
"""Test suite for the Amenity class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""

    def test_attributes(self):
        """Test that Amenity has the correct attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
