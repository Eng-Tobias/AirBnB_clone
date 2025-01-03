# File: console.py

import re
from models import storage
from models.state import State
from models.place import Place
from models.base_model import BaseModel

class HBNBCommand:
    def do_create(self, arg):
        """Creates a new instance of a given class and sets attributes with given params"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["State", "Place", "User", "Amenity", "City", "Review"]:
            print("** class doesn't exist **")
            return
        cls = globals().get(class_name)

        # Parse parameters
        params = {}
        for param in args[1:]:
            try:
                key, value = param.split('=')
                value = value.strip('"').replace("_", " ")
                if value.replace(".", "", 1).isdigit():  # Check if it's an integer or float
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                params[key] = value
            except ValueError:
                pass

        # Create object
        new_instance = cls(**params)
        new_instance.save()
        print(f"({new_instance.__class__.__name__}) {new_instance.id}")
