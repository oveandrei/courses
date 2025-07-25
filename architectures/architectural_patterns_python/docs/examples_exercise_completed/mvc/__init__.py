"""
__init__.py

This is the entry point for the Task Application (MVC version).

NOTE:
This project is intentionally simplified for educational purposes:
- Input validation is minimal or missing
- No persistence (data is not saved between runs)
- No exception handling for incorrect input types

The focus is to demonstrate HOW to implement the Model-View-Controller (MVC) architectural pattern in Python using a simple task management console app.

Feel free to improve or expand this example as a learning exercise.
"""

from controller import Controller

if __name__ == '__main__':
    # Instantiate the controller and start the main application loop
    controller = Controller()
    controller.start()
