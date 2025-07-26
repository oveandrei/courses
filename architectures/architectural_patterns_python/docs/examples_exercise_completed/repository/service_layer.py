from repository import UserRepository
from models import User
from typing import List, Optional

class UserService:
    """
    Service layer responsible for user-related operations.
    This class acts as an intermediary between the UI/controller layer and the repository.
    
    It abstracts the data access logic by depending only on the UserRepository interface,
    thus supporting multiple backend implementations without changing business logic.
    """

    def __init__(self, repository: UserRepository):
        """
        Initialize UserService with a UserRepository implementation.

        Args:
            repository (UserRepository): Concrete implementation of UserRepository.
        """
        self.repository = repository

    def register_user(self, username: str, password: str) -> User:
        """
        Register a new user by adding them to the repository.

        Args:
            username (str): The username of the new user.
            password (str): The password for the new user.

        Returns:
            User: The newly created User object with assigned user_id.
        """
        return self.repository.add(username, password)

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their unique ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[User]: The User object if found, otherwise None or raises exception based on repo implementation.
        """
        return self.repository.get_by_id(user_id)

    def list_users(self) -> List[User]:
        """
        Retrieve all users currently stored in the repository.

        Returns:
            List[User]: A list of all User objects.
        """
        return self.repository.get_all()

    def update_user(self, user_id: int, username: str, password: str) -> None:
        """
        Update the username and password of an existing user.

        Args:
            user_id (int): The ID of the user to update.
            username (str): The new username to set.
            password (str): The new password to set.

        Raises:
            ValueError: If the user with the specified ID does not exist.
        """
        self.repository.update(user_id, username, password)

    def delete_user(self, user_id: int) -> None:
        """
        Delete a user from the repository by their ID.

        Args:
            user_id (int): The ID of the user to delete.

        Raises:
            ValueError: If the user with the specified ID does not exist.
        """
        self.repository.delete(user_id)
