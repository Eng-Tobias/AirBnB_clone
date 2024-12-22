#!/usr/bin/python3
"""Test suite for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class."""

    def test_attributes(self):
        """Test that User has the correct attributes."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
