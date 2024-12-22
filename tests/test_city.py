#!/usr/bin/python3
"""Test suite for the City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def test_attributes(self):
        """Test that City has the correct attributes."""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
