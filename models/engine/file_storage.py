#!/usr/bin/python3
import json

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w") as f:
            json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    from models.base_model import BaseModel  # Avoid circular imports
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
