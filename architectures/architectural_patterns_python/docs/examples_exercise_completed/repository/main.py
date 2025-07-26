from repository import InMemoryUserRepository
from service_layer import UserService

def print_menu():
    """
    Prints the command-line menu options for user management.
    """
    print("\n--- User Management ---")
    print("1. Add user")
    print("2. Update user")
    print("3. Delete user")
    print("4. Get user by ID")
    print("5. List all users")
    print("0. Exit")

def main():
    """
    Main function to run the user management CLI application.
    
    It initializes the in-memory repository and user service, then
    enters a loop to accept and process user commands until exit.
    """
    repo = InMemoryUserRepository()  # Create the repository instance
    service = UserService(repo)      # Inject repository into service layer

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new user
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = service.register_user(username, password)
            print(f"User created with ID: {user.user_id}")

        elif choice == "2":
            # Update existing user
            try:
                user_id = int(input("Enter user ID to update: "))
                username = input("Enter new username: ")
                password = input("Enter new password: ")
                service.update_user(user_id, username, password)
                print("User updated.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            # Delete a user
            try:
                user_id = int(input("Enter user ID to delete: "))
                service.delete_user(user_id)
                print("User deleted.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            # Retrieve a user by ID
            try:
                user_id = int(input("Enter user ID: "))
                user = service.get_user(user_id)
                if user:
                    print(user)
                else:
                    print("User not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "5":
            # List all users
            users = service.list_users()
            if users:
                for user in users:
                    print(user)
            else:
                print("No users found.")

        elif choice == "0":
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
