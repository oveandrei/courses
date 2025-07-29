"""
This module handles basic user management operations such as registration,
login, logout, and profile viewing. User data is stored in a JSON file.

Note: This implementation is for learning purposes only and does not include
security features like password hashing or input validation.
"""
import json
import os

# Path to the file that stores user data
USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")


def load_users():
    """
    Load the users from the users.json file.

    Returns:
        dict: A dictionary of users where keys are usernames and
              values are dictionaries containing user details.
    """
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # File exists but is empty or malformed — fallback to empty user list
            return {}


def save_users(users):
    """
    Save the user data to the users.json file.

    Args:
        users (dict): A dictionary of user data to save.
    """
    if users is None:
        users = {}

    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)


def register_user(username, password):
    """
    Register a new user if the username is not already taken.

    Args:
        username (str): The desired username.
        password (str): The desired password (stored in plaintext for now).

    Returns:
        None
    """
    users = load_users()

    if username in users:
        print(f"Username {username} already exists.")
        return

    # Add new user to the dictionary
    users[username] = {"password": password}
    save_users(users)
    print(f"User '{username}' registered successfully.")


def login(username, password):
    """
    Attempt to log in a user with the given credentials.

    Args:
        username (str): The username to authenticate.
        password (str): The password to verify.

    Returns:
        str | None: The username if login is successful; None otherwise.
    """
    users = load_users()

    if username in users and users[username]['password'] == password:
        print(f"Welcome back, {username}")
        return username

    print("Invalid username or password")
    return None


def view_profile(username):
    """
    Display the profile information for a given user.

    Args:
        username (str): The username of the user to display.

    Returns:
        None
    """
    users = load_users()

    if username in users:
        print(f"\n--- Profile ---\nUsername: {username}")
    else:
        print("User not found.")


def logout(current_user: str | None):
    """
    Log out the currently logged-in user.

    Args:
        current_user (str | None): The username of the currently logged-in user.

    Returns:
        None or str: Returns None to represent a successful logout,
                     or prints an error if no user was logged in.
    """
    if current_user:
        return None
    else:
        print("You are not logged in.")
