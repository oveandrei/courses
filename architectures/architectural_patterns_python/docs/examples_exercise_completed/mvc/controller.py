"""
controller.py

This file contains the Controller class for the MVC Task Application.
The Controller coordinates interactions between the View (user interface)
and the Model (business logic and data).
"""

from models import Task, TaskManager
from view import View

class Controller:
    """
    The Controller class manages the main application loop and handles
    the coordination between user inputs (via the View) and task logic (via the Model).
    """

    def __init__(self):
        """
        Initializes the Controller by setting up the View and TaskManager instances.
        """
        self.view = View()
        self.manager = TaskManager()

    def start(self):
        """
        Starts the application loop.
        Displays the menu, captures user input, and triggers corresponding actions.
        """
        print("------------This is your Task Application -------------")
        while True:
            self.view.show_menu()
            response = self.view.get_user_choice()

            # Add a new task
            if response == '1':
                title = self.view.ask_for_task_title()
                due_date = self.view.ask_for_due_date()
                task = Task(title, due_date)

                self.manager.add_task(task)
                self.view.show_task_added(task)

            # Complete a task
            elif response == '2':
                self.view.show_uncompleted_tasks(self.manager.show_tasks())
                # Ask user which task to complete and mark it as done
                completed_task = self.manager.task_complete_list(self.view.complete_task())
                self.view.show_task_completed(completed_task)  # type: ignore (we skip None handling on purpose)

            # Show all tasks
            elif response == '3':
                self.view.show_all_tasks(self.manager.show_tasks())

            # Remove a task
            elif response == '4':
                self.view.show_all_tasks(self.manager.show_tasks())
                removed_task = self.manager.task_remove(self.view.remove_task())
                self.view.show_task_removed(removed_task)  # type: ignore (no validation needed here)

            # Quit the application
            elif response == '5':
                break

            # Invalid option
            else:
                self.view.response_not_in_list(response)
