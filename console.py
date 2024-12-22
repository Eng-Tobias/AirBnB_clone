import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    
    prompt = '(hbnb) '  # Custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Override emptyline to prevent execution on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
