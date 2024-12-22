#!/usr/bin/python3
"""Test suite for the State class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class."""

    def test_attributes(self):
        """Test that State has the correct attributes."""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
