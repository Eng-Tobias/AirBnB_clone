#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))


if __name__ == "__main__":
    unittest.main()
