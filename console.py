# File: console.py

import re
from models import storage
from models.state import State
from models.place import Place
# Add other imports as necessary

class HBNBCommand:
    # Other methods...

    def do_create(self, arg):
        """Create a new object with provided parameters and print its ID."""
        if not arg:
            print("** class name missing **")
            return

        # Extract class name and parameters from the argument
        arg_list = arg.split()
        class_name = arg_list[0]
        parameters = {}

        # Ensure class name is valid
        if class_name not in globals() or class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        # Process parameters
        for param in arg_list[1:]:
            match = re.match(r'([a-zA-Z0-9_]+)=\"([^\"]+)\"', param)
            if match:
                key, value = match.groups()
                parameters[key] = value
            else:
                match = re.match(r'([a-zA-Z0-9_]+)=([0-9]+\.[0-9]+|[0-9]+)', param)
                if match:
                    key, value = match.groups()
                    if '.' in value:
                        parameters[key] = float(value)
                    else:
                        parameters[key] = int(value)
                else:
                    print("** invalid parameter format **")
                    return

        # Check if parameters are provided correctly for the class
        try:
            cls = globals()[class_name]
            obj = cls(**parameters)  # Create object with parsed parameters
            obj.save()  # Save to storage

            print(obj.id)  # Print the object ID
        except TypeError as e:
            print(f"** error: {str(e)} **")
            return
