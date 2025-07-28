# db.py

# ----- Model -----
class Task:
    """
    Represents a single task in the task management system.

    Attributes:
        task_id (int): A unique identifier for the task.
        title (str): A short descriptive title of the task.
        completed (bool): Status of the task; True if completed, False otherwise.
    """
    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.task_id = task_id
        self.title = title
        self.completed = completed


# ----- Database -----
class TasksDatabase:
    """
    In-memory database that stores all tasks.

    Attributes:
        storage (dict[int, Task]): A dictionary mapping task IDs to Task objects.
    """
    def __init__(self):
        # Use task_id as the key for quick lookup, update, and delete operations.
        self.storage: dict[int, Task] = {}
