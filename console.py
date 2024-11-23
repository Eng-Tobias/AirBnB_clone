#!/usr/bin/python3
""" Console module """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter for AirBnB_clone """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit the program"""
        return True

    def emptyline(self):
        """Override default behavior to do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
