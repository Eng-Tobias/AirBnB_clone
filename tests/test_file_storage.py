#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def test_all_method(self):
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "all"))

    def test_save_method(self):
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "save"))


if __name__ == "__main__":
    unittest.main()
