import json
from models.base_model import BaseModel  # Importing relevant models

class FileStorage:
    """Class that handles saving and reloading objects to/from a file."""

    __file_path = 'file.json'  # Path to the file where objects are stored
    __objects = {}

    def reload(self):
        """Reloads the stored objects from the file."""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    class_name = value.get("__class__")
                    if class_name:
                        class_ref = globals().get(class_name)  # Get class reference from globals
                        if class_ref:
                            self.__objects[key] = class_ref(**value)  # Instantiate the object with the correct class
                        else:
                            print(f"Class {class_name} not found")
        except Exception as e:
            print(f"Error reloading data: {e}")

    def save(self):
        """Saves all objects to the file."""
        with open(self.__file_path, 'w') as f:
            objs_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(objs_dict, f)
