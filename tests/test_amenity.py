#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))


if __name__ == "__main__":
    unittest.main()
