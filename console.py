from models import storage  # Import storage object from models module

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_show(self, arg):
        """Show an instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        model_id = args[1]
        instance_key = "{}.{}".format(class_name, model_id)
        
        if instance_key not in storage.all():  # Ensure 'storage' is correctly referenced
            print("** no instance found **")
            return
        
        instance = storage.all()[instance_key]
        print(instance)

    def do_update(self, arg):
        """Update an instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        model_id = args[1]
        instance_key = "{}.{}".format(class_name, model_id)
        
        if instance_key not in storage.all():  # Ensure 'storage' is correctly referenced
            print("** no instance found **")
            return
        
        instance = storage.all()[instance_key]
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        if len(args) < 4:
            print("** value missing **")
            return
        
        attribute_name = args[2]
        attribute_value = args[3]
        
        setattr(instance, attribute_name, attribute_value)
        storage.save()  # Ensure that changes are saved

    def do_destroy(self, arg):
        """Destroy an instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        model_id = args[1]
        instance_key = "{}.{}".format(class_name, model_id)
        
        if instance_key not in storage.all():  # Ensure 'storage' is correctly referenced
            print("** no instance found **")
            return
        
        del storage.all()[instance_key]  # Remove the instance from storage
        storage.save()  # Ensure changes are saved
        print("** instance destroyed **")
    
    def do_all(self, arg):
        """Display all instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        
        instances = storage.all()
        result = []
        for key, value in instances.items():
            if key.startswith(class_name):
                result.append(str(value))
        
        print(result)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
