from db import Task, TasksDatabase
from typing import List

# ----- Command Side (Write Model) -----
class CreateTaskCommand:
    """
    Handles task creation, modification, completion, and deletion.
    This class represents the Command side of the CQRS pattern.

    Attributes:
        database (TasksDatabase): The in-memory database used to store task data.
    """
    def __init__(self, database: TasksDatabase):
        self.database = database

    def create_task(self, task_id: int, title: str) -> bool:
        """
        Creates a new task and stores it in the database.

        Args:
            task_id (int): Unique ID for the task.
            title (str): Title of the task.

        Returns:
            bool: True if the task was successfully created.

        Raises:
            ValueError: If a task with the given ID already exists.
        """
        if task_id in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} already exists.")
        
        self.database.storage[task_id] = Task(task_id, title)
        return True

    def update_task(self, task_id: int, title: str) -> bool:
        """
        Updates the title of an existing task.

        Args:
            task_id (int): ID of the task to update.
            title (str): New title for the task.

        Returns:
            bool: True if the task was updated.

        Raises:
            ValueError: If the task ID does not exist.
        """
        if task_id not in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} is not in database.")

        self.database.storage[task_id] = Task(task_id, title)
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by ID.

        Args:
            task_id (int): ID of the task to delete.

        Returns:
            bool: True if the task was deleted.

        Raises:
            ValueError: If the task ID does not exist.
        """
        if task_id not in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} is not in database")
        
        self.database.storage.pop(task_id)
        return True
    
    def complete_task(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): ID of the task to mark as completed.

        Returns:
            bool: True if the task was marked completed.

        Raises:
            ValueError: If the task ID does not exist.
        """
        if task_id not in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} is not in database.")

        self.database.storage[task_id].completed = True
        return True


# ----- Query Side (Read Model) -----
class GetOpenTasksQuery:
    """
    Handles task queries such as retrieving one or more tasks.
    This class represents the Query side of the CQRS pattern.

    Attributes:
        database (TasksDatabase): The in-memory database used for reads.
    """
    def __init__(self, database: TasksDatabase):
        self.database = database

    def get_task(self, task_id: int) -> Task:
        """
        Retrieves a single task by its ID.

        Args:
            task_id (int): ID of the task to retrieve.

        Returns:
            Task: The matching task object.

        Raises:
            ValueError: If the task ID does not exist.
        """
        if task_id not in self.database.storage:
            raise ValueError(f"[Query] This ID: {task_id} doesn't exist")
        
        return self.database.storage[task_id]

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieves all tasks from the database.

        Returns:
            List[Task]: A list of all task objects.
        """
        return list(self.database.storage.values())
        
    def get_completed_tasks(self) -> List[Task]:
        """
        Retrieves all tasks that are marked as completed.

        Returns:
            List[Task]: A list of completed task objects.
        """
        return [task for task in self.database.storage.values() if task.completed]

    def get_uncompleted_tasks(self) -> List[Task]:
        """
        Retrieves all tasks that are not yet completed.

        Returns:
            List[Task]: A list of uncompleted task objects.
        """
        return [task for task in self.database.storage.values() if not task.completed]
