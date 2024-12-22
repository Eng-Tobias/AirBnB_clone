#!/usr/bin/python3
"""Test suite for the FileStorage class."""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class."""

    def test_all_method(self):
        """Test that FileStorage has the 'all' method."""
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "all"))
        self.assertIsInstance(storage.all(), dict)

    def test_save_method(self):
        """Test that FileStorage has the 'save' method."""
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "save"))
