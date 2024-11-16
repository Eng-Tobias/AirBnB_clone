#!/usr/bin/python3
"""
This module contains a simple implementation of a command interpreter.
"""

import os
import sys


def greet_user(name):
    """
    Greet the user by their name.
    
    Arguments:
        name (str): The name of the user.
    """
    print(f"Hello, {name}!")


def main():
    """
    Main function to execute the program.
    """
    if len(sys.argv) != 2:
        print("Usage: ./greet.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    greet_user(name)


if __name__ == "__main__":
    main()
