AirBnB Clone - The Console
Description
The AirBnB Clone project is a command-line interpreter for managing data related to the AirBnB platform. This project serves as the foundation for an AirBnB clone by implementing a command interpreter that can manage various objects such as users, places, and bookings. The interpreter enables interaction with the system for creating, showing, updating, and deleting objects, all while using a simple command-line interface.

The command interpreter is designed to function in an interactive mode (like a shell) and non-interactive mode, providing flexibility for users and enabling automated scripts.

Description of the Command Interpreter
The AirBnB command interpreter (console.py) allows interaction with the AirBnB objects via commands entered into the terminal. The commands include operations to manipulate data stored in a storage system. The system supports both interactive and non-interactive modes for maximum usability.

How to Start It
To start the command interpreter, run the console.py script. In an interactive mode, open the terminal and execute the following:

bash
Copy code
$ ./console.py
This will open the command prompt (hbnb).

How to Use It
Once in the interactive mode, you can enter the commands to manage objects. Some of the basic commands are as follows:

help: Displays a list of documented commands.
quit: Exits the command interpreter.
EOF: Exits the command interpreter.
For example:

Start the command interpreter:
bash
Copy code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
Run the command in non-interactive mode:
You can also run commands non-interactively. For example:

bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
Example Usage
bash
Copy code
$ ./console.py
(hbnb) help
Documented commands:
======================
EOF  help  quit
(hbnb)
You can issue the quit command to exit the interpreter.

Run the command in non-interactive mode:
bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands:
======================
EOF  help  quit
(hbnb)
$
Requirements
Python Scripts
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
All files should end with a new line.
The first line of all files should be exactly #!/usr/bin/python3.
All scripts must adhere to the pycodestyle (version 2.8.*).
All files must be executable.
Files will be tested using wc for line count.
Modules, classes, and functions should all have appropriate documentation.
Python Unit Tests
Unit tests should be written using the unittest module.
All test files should reside in the tests folder.
The organization of the tests should mirror the structure of the main project.
Example: For models/base_model.py, the test file should be located in tests/test_models/test_base_model.py.
Run tests using python3 -m unittest discover tests to execute all tests.
You can test individual files by running python3 -m unittest tests/test_models/test_base_model.py.
Ensure that all your modules, classes, and functions are documented.
Project Structure
bash
Copy code
AirBnB_clone/
│
├── README.md           # Project overview
├── AUTHORS             # Author details
├── console.py          # Command interpreter entry point
├── models/             # Contains various models (e.g., BaseModel, User)
├── tests/              # Unit tests for models and console
│   ├── test_console.py
│   ├── test_models/    # Unit tests for models
│   │   └── test_base_model.py
├── ...
Example Command Usage:
Start interactive mode:

bash
Copy code
$ ./console.py
(hbnb) help
Documented commands:
======================
EOF  help  quit
(hbnb) quit
$
Run a command in non-interactive mode:

bash
Copy code
$ echo "help" | ./console.py
(hbnb)
Documented commands:
======================
EOF  help  quit
(hbnb)
$
Contributing
To contribute to the project:

Clone the repository to your local machine.
Create a new branch for the feature or bug fix you're working on.
Implement the changes and ensure that they pass all unit tests.
Submit a pull request for review.
Version Control
Use GitHub for version control.
All work should be done on separate branches and submitted via pull requests.
AUTHORS
txt
Copy code
Tobias Guya <engtobiasguya100@gmail.com>
