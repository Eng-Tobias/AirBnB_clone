#!/usr/bin/python3
"""Defines the FileStorage class."""

class FileStorage:
    """Handles storage of models in JSON format."""
    __file_path = "file.json"  # Private attribute
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Returns the dictionary of stored objects."""
        return self.__objects

    def save(self):
        """Simulates saving objects to a file."""
        pass
