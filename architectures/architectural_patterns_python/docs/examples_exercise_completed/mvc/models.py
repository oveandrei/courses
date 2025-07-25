"""
models.py

This file contains the core business logic and data structures
for the Task Application. It defines the Task model and TaskManager,
which handles the logic for managing a list of tasks.
"""

from datetime import date, datetime

class Task:
    """
    Represents a single task with a title, due date, and completion status.
    """

    def __init__(self, title: str, due_date: date, completed: bool = False):
        """
        Initializes a new Task instance.

        Args:
            title (str): The title or name of the task.
            due_date (date): The due date for the task.
            completed (bool): Whether the task is completed. Defaults to False.
        """
        self.__title = title
        self.__due_date = due_date
        self.__completed = completed

    # === Accessors (Getters) ===

    def get_title(self) -> str:
        """Returns the title of the task."""
        return self.__title

    def get_due_date(self) -> date:
        """Returns the due date of the task."""
        return self.__due_date

    def get_completed(self) -> bool:
        """Returns True if the task is completed, False otherwise."""
        return self.__completed

    # === Mutators (Setters / State changers) ===

    def check_completed(self):
        """Marks the task as completed."""
        self.__completed = True

    def set_due_date(self, date: date) -> None:
        """
        Updates the due date of the task.

        Args:
            date (date): The new due date to assign.
        """
        self.__due_date = date


class TaskManager:
    """
    Manages a collection of Task objects.
    Provides methods to add, complete, remove, and list tasks.
    """

    def __init__(self):
        """Initializes an empty list of tasks."""
        self.__tasks: list = []

    def add_task(self, task: Task):
        """
        Adds a new task to the task list.

        Args:
            task (Task): The Task instance to add.
        """
        self.__tasks.append(task)

    def mark_task_completed(self, task: Task):
        """
        Marks a task as completed.

        Args:
            task (Task): The task to mark as completed.
        """
        task.check_completed()

    def show_tasks(self) -> list[Task]:
        """
        Returns the list of all current tasks.

        Returns:
            list[Task]: A list of Task instances.
        """
        return self.__tasks

    def task_complete_list(self, name: str) -> Task | None:
        """
        Marks a task as completed by its title.

        Args:
            name (str): The title of the task to complete.

        Returns:
            Task | None: The task that was marked as completed, or None if not found.
        """
        for task in self.__tasks:
            if task.get_title() == name:
                self.mark_task_completed(task)
                return task
        return None

    def task_remove(self, name: str) -> Task | None:
        """
        Removes a task by its title.

        Args:
            name (str): The title of the task to remove.

        Returns:
            Task | None: The removed task, or None if not found.
        """
        for task in self.__tasks:
            if task.get_title() == name:
                self.__tasks.remove(task)
                return task
        return None
