import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User  # Add your model imports here
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create a new instance of BaseModel and save it to the file"""
        if not line:
            print("** class name missing **")
            return
        elif line not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[line]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Show the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        try:
            print(storage.all()[args[0] + "." + args[1]])
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Display all instances of a class"""
        if line:
            if line not in globals():
                print("** class doesn't exist **")
                return
            instances = storage.all(line)
            print([str(instance) for instance in instances.values()])
        else:
            instances = storage.all()
            print([str(instance) for instance in instances.values()])

    def do_count(self, line):
        """Display the number of instances of a class"""
        if line:
            if line not in globals():
                print("** class doesn't exist **")
                return
            instances = storage.all(line)
            print(len(instances))
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        try:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_update(self, line):
        """Update an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        try:
            instance = storage.all()[args[0] + "." + args[1]]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return
            setattr(instance, args[2], args[3])
            instance.save()
        except KeyError:
            print("** no instance found **")

    def do_quit(self, line):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, line):
        """Handle EOF to exit"""
        return True
