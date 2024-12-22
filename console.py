import cmd
import json
import uuid
from models.base_model import BaseModel  # Ensure you have your model imports correctly

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel}  # Add all your classes here

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[arg]()  # Create instance of class
        new_instance.save()  # Save instance to the file
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = f"{args[0]}.{args[1]}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[instance_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save to the JSON file)"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = f"{args[0]}.{args[1]}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[instance_key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg and arg not in self.__classes:
            print("** class doesn't exist **")
            return
        all_instances = []
        for key, obj in storage.all().items():
            if not arg or key.startswith(arg):
                all_instances.append(str(obj))
        print(all_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = f"{args[0]}.{args[1]}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[instance_key]
        setattr(instance, args[2], args[3])
        instance.save()

    def emptyline(self):
        """Overrides the default empty line behavior to do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
