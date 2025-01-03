# File: tests/test_create_command.py

import unittest
from io import StringIO
from unittest.mock import patch
from models import storage
from console import HBNBCommand
from models.state import State
from models.place import Place


class TestCreateCommand(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state(self, mock_stdout):
        """Test creating a new state"""
        command = HBNBCommand()
        command.do_create("State name=\"California\"")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith('('))
        self.assertTrue(output.endswith(')'))

        state = storage.all(State)
        self.assertTrue(len(state) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place(self, mock_stdout):
        """Test creating a new place"""
        command = HBNBCommand()
        command.do_create("Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith('('))
        self.assertTrue(output.endswith(')'))

        place = storage.all(Place)
        self.assertTrue(len(place) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test creating a new object with an invalid class name"""
        command = HBNBCommand()
        command.do_create("InvalidClass name=\"Test\"")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        """Test creating an object without a class name"""
        command = HBNBCommand()
        command.do_create("")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

if __name__ == "__main__":
    unittest.main()
