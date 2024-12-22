#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))


if __name__ == "__main__":
    unittest.main()
