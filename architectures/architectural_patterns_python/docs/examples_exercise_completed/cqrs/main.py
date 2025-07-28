from cqrs import CreateTaskCommand, GetOpenTasksQuery
from db import TasksDatabase

def main_menu():
    """
    Prints the main menu options to the user.
    """
    print("----Main Menu----")
    print("1. Create a Task")
    print("2. Update a Task")
    print("3. Complete a Task")
    print("4. Delete a Task")
    print("5. Get a Task")
    print("6. Get all Tasks")
    print("7. Get completed Tasks")
    print("8. Get uncompleted Tasks")
    print("9. Quit")


def main():
    """
    Entry point for the CLI task manager using the CQRS pattern.
    """
    database = TasksDatabase()
    cmd = CreateTaskCommand(database)
    queries = GetOpenTasksQuery(database)

    while True:
        main_menu()
        choice = input("Select an option (1-9): ").strip()

        try:
            if choice == "1":
                task_id = int(input("Enter Task ID: "))
                title = input("Enter Task Title: ")
                cmd.create_task(task_id, title)
                print("[Success] Task created.")

            elif choice == "2":
                task_id = int(input("Enter Task ID to update: "))
                title = input("Enter new Task Title: ")
                cmd.update_task(task_id, title)
                print("[Success] Task updated.")

            elif choice == "3":
                task_id = int(input("Enter Task ID to complete: "))
                cmd.complete_task(task_id)
                print("[Success] Task marked as completed.")

            elif choice == "4":
                task_id = int(input("Enter Task ID to delete: "))
                cmd.delete_task(task_id)
                print("[Success] Task deleted.")

            elif choice == "5":
                task_id = int(input("Enter Task ID to fetch: "))
                task = queries.get_task(task_id)
                print(f"[Task] ID: {task.task_id} | Title: {task.title} | Completed: {task.completed}")

            elif choice == "6":
                tasks = queries.get_all_tasks()
                if not tasks:
                    print("[Info] No tasks available.")
                for task in tasks:
                    print(f"ID: {task.task_id} | Title: {task.title} | Completed: {task.completed}")

            elif choice == "7":
                tasks = queries.get_completed_tasks()
                if not tasks:
                    print("[Info] No completed tasks.")
                for task in tasks:
                    print(f"ID: {task.task_id} | Title: {task.title}")

            elif choice == "8":
                tasks = queries.get_uncompleted_tasks()
                if not tasks:
                    print("[Info] No uncompleted tasks.")
                for task in tasks:
                    print(f"ID: {task.task_id} | Title: {task.title}")

            elif choice == "9":
                print("Exiting application...")
                break

            else:
                print("[Error] Invalid choice. Please select from 1 to 9.")

        except ValueError as e:
            print(f"[Error] {e}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")

        print()  # Add spacing for readability


if __name__ == "__main__":
    main()
