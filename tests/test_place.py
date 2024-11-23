#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))

if __name__ == "__main__":
    unittest.main()
