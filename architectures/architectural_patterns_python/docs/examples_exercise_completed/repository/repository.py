from abc import ABC, abstractmethod
from typing import Optional, Dict, List
from models import User

class UserRepository(ABC):
    """
    Abstract base class defining the interface for a user repository.
    Specifies the contract for all concrete implementations to perform
    CRUD operations on User data without depending on storage details.
    """

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their unique ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[User]: The User object if found, otherwise None or raises exception.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        """
        Retrieve all users stored in the repository.

        Returns:
            List[User]: A list of all User objects.
        """
        pass
    
    @abstractmethod
    def add(self, username: str, password: str) -> User:
        """
        Add a new user to the repository.

        Args:
            username (str): Username of the new user.
            password (str): Password of the new user.

        Returns:
            User: The newly created User object with assigned user_id.
        """
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        """
        Delete a user by their ID.

        Args:
            user_id (int): The ID of the user to delete.

        Raises:
            ValueError: If the user with the specified ID does not exist.
        """
        pass

    @abstractmethod
    def update(self, user_id: int, username: str, password: str) -> None:
        """
        Update the user identified by user_id with new username and password.

        Args:
            user_id (int): The ID of the user to update.
            username (str): The new username.
            password (str): The new password.

        Raises:
            ValueError: If the user with the specified ID does not exist.
        """
        pass


class InMemoryUserRepository(UserRepository):
    """
    Concrete implementation of UserRepository that stores users in memory
    using a dictionary. User IDs are auto-incremented integers.
    Suitable for development, testing, or lightweight usage without persistence.
    """

    def __init__(self):
        """
        Initialize the in-memory user repository with an empty user dictionary
        and an ID counter starting from zero.
        """
        self.users: Dict[int, User] = {}
        self._id_counter = 0

    def get_by_id(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their ID.

        Args:
            user_id (int): ID of the user to fetch.

        Returns:
            User: User object with the matching ID.

        Raises:
            ValueError: If user with given ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"The user with id {user_id} doesn't exist")
        else:
            return self.users[user_id]
        
    def get_all(self) -> List[User]:
        """
        Return a list of all users currently stored.

        Returns:
            List[User]: List of all User objects.
        """
        return list(self.users.values())
    
    def add(self, username: str, password: str) -> User:
        """
        Add a new user with an auto-generated ID.

        Args:
            username (str): Username of the new user.
            password (str): Password of the new user.

        Returns:
            User: Newly created User object with assigned user_id.
        """
        user_id = self._auto_id()
        user = User(user_id, username, password)
        self.users[user_id] = user
        return user

    def delete(self, user_id: int) -> None:
        """
        Delete a user by their ID.

        Args:
            user_id (int): ID of the user to delete.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id in self.users:
            del self.users[user_id]
        else:
            raise ValueError(f"The user with id {user_id} doesn't exist")

    def update(self, user_id: int, username: str, password: str) -> None:
        """
        Update an existing user's username and password.

        Args:
            user_id (int): ID of the user to update.
            username (str): New username.
            password (str): New password.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"The user with id {user_id} doesn't exist")
        user = self.users[user_id]
        user.username = username
        user.password = password
    
    def _auto_id(self) -> int:
        """
        Generate a new unique user ID by incrementing the internal counter.

        Returns:
            int: New unique user ID.
        """
        self._id_counter += 1
        return self._id_counter
