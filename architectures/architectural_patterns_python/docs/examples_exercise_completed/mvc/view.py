"""
view.py

This file contains the View class, responsible for all user interaction.
It handles displaying information to the user and receiving input.
It should not contain any business logic.
"""

from models import Task
from datetime import datetime, date

class View:
    """
    The View class manages the user interface.
    It displays menus and task lists, receives input, and gives user feedback.
    """

    # === Menu Display ===

    def show_menu(self):
        """Displays the main menu options to the user."""
        print("Main Menu")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. Show all tasks")
        print("4. Remove a task")
        print("5. Quit")

    # === Task Display ===

    def show_all_tasks(self, tasks: list[Task]):
        """
        Displays all tasks with their titles, due dates, and completion status.

        Args:
            tasks (list[Task]): A list of Task instances to display.
        """
        print("\n=== TASK LIST ===")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task.get_completed() else "❌"
            print(f"{i}. {task.get_title()} - Due: {task.get_due_date()} - {status}")
        print()

    def show_uncompleted_tasks(self, tasks: list[Task]):
        """
        Displays only the tasks that are not yet completed.

        Args:
            tasks (list[Task]): A list of Task instances to filter and display.
        """
        print("\n===== Uncompleted Tasks =====")
        for i, task in enumerate(tasks, start=1):
            if not task.get_completed():
                print(f"{i}. {task.get_title()} - Due: {task.get_due_date()} - ❌")
        print()

    # === Feedback and Notifications ===

    def show_task_added(self, task: Task):
        """
        Displays a message confirming that a task was successfully added.

        Args:
            task (Task): The task that was added.
        """
        print(f"[INFO] Task '{task.get_title()}' added successfully.")

    def show_task_completed(self, task: Task):
        """
        Displays a message confirming that a task was marked as completed.

        Args:
            task (Task): The task that was completed.
        """
        print(f"[INFO] Task '{task.get_title()}' marked as completed ✅.")

    def show_task_removed(self, task: Task):
        """
        Displays a message confirming that a task was removed.

        Args:
            task (Task): The task that was removed.
        """
        print(f"[INFO] Task '{task.get_title()}' removed from list.")

    def show_error(self, message: str):
        """
        Displays an error message to the user.

        Args:
            message (str): The error message to show.
        """
        print(f"[ERROR] {message}")

    def response_not_in_list(self, response: str):
        """
        Displays a warning if the user enters an invalid menu option.

        Args:
            response (str): The invalid input provided by the user.
        """
        print(f"Your response: {response} is not in the menu options.")

    # === Input Collection ===

    def ask_for_task_title(self) -> str:
        """
        Asks the user to enter a task title.

        Returns:
            str: The user-provided task title.
        """
        return input("Enter task title: ")

    def ask_for_due_date(self) -> date:
        """
        Asks the user to enter a due date in DD-MM-YYYY format.

        Returns:
            date: The parsed date object.
        """
        return datetime.strptime(input("Enter due date (DD-MM-YYYY): "), "%d-%m-%Y").date()

    def get_user_choice(self) -> str:
        """
        Prompts the user to choose a menu option.

        Returns:
            str: The chosen menu number as a string.
        """
        return input("Please choose a number: ")

    def complete_task(self) -> str:
        """
        Asks the user for the title of the task they want to complete.

        Returns:
            str: The task title input by the user.
        """
        return input("What task would you like to mark as complete: ")

    def remove_task(self) -> str:
        """
        Asks the user for the title of the task they want to remove.

        Returns:
            str: The task title input by the user.
        """
        return input("What task would you like to remove from the list: ")
