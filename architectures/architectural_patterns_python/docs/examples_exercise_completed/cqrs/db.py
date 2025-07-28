

# ----- Model -----
class Task:
    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.title = title
        self.completed = completed
        self.task_id = task_id

# ------ Database -----
class TasksDatabase:
    def __init__(self):
        self.storage: dict[int, Task] = {}

