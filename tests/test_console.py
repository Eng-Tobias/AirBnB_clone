#!/usr/bin/python3
"""Unittest for console.py"""

import unittest


from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console"""

    def test_help_command(self):
        self.assertTrue(hasattr(HBNBCommand, "do_help"))


if __name__ == "__main__":
    unittest.main()
