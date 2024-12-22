from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    def do_show(self, args):
        """Show the instance with the given ID."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        class_name, model_id = args_list[0], args_list[1]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instance_key = "{}.{}".format(class_name, model_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[instance_key]
        print(instance)

    def do_destroy(self, args):
        """Destroy an instance with the given ID."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        class_name, model_id = args_list[0], args_list[1]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instance_key = "{}.{}".format(class_name, model_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[instance_key]
        storage.save()

    def do_update(self, args):
        """Update an instance with the given ID."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        class_name, model_id = args_list[0], args_list[1]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instance_key = "{}.{}".format(class_name, model_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args_list[2]
        if len(args_list) < 4:
            print("** value missing **")
            return
        value = args_list[3]
        instance = storage.all()[instance_key]
        setattr(instance, attribute_name, value)
        storage.save()
