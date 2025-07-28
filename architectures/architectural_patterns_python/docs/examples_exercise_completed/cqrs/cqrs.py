from db import Task, TasksDatabase
from typing import List

# Command side (Write Model)
class CreateTaskCommand:
    def __init__(self, database: TasksDatabase):
        self.database = database

    def create_task(self, task_id, title) -> bool:
        if task_id in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} already exists.")
        
        self.database.storage[task_id] = Task(task_id, title)
        return True

    def update_task(self, task_id, title) -> bool:
        if task_id not in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} is not in database.")

        self.database.storage[task_id] = Task(task_id, title)
        return True

    def delete_task(self, task_id) -> bool:
        if task_id not in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} is not in database")
        
        self.database.storage.pop(task_id)
        return True
    
    def complete_task(self, task_id) -> bool:
        if task_id not in self.database.storage:
            raise ValueError(f"[Command] The ID: {task_id} is not in database.")

        self.database.storage[task_id].completed = True
        return True

 # Query Side (Read Model) 
 #   
class GetOpenTasksQuery:
    def __init__(self, database: TasksDatabase):
        self.database = database

    def get_task(self, task_id: int) -> Task:
        if task_id not in self.database.storage:
            raise ValueError(f"[Query] This ID: {task_id} doesn't exist")
        
        return self.database.storage[task_id]

    def get_all_tasks(self) -> List[Task]:
        return list(self.database.storage.values())
        
    def get_completed_tasks(self) -> List[Task]:
        return [task for task in self.database.storage.values() if task.completed]

    def get_uncompleted_tasks(self) -> List[Task]:
        return [task for task in self.database.storage.values() if not task.completed]
