from typing import List

# --- Domain Entity ---
class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

# --- Repository Interface ---
class UserRepository:
    def __init__(self):
        # In-memory database simulation
        self._users: dict[int, User] = {}

    def add(self, user: User) -> None:
        """Add a user to the repository."""
        self._users[user.user_id] = user
    
    def get_by_id(self, user_id: int) -> User:
        """Retrieve a user by ID. Raises ValueError if not found."""
        user = self._users.get(user_id)
        if user is None:
            raise ValueError(f"User with ID {user_id} not found")
        return user
    
    def list_all(self) -> List[User]:
        """Return all users"""
        return list(self._users.values())
    

# --- Business Logic / Service Layer ---
class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def register_user(self, user_id: int, name: str) -> None:
        user = User(user_id, name)
        self._repository.add(user)
    
    def show_users(self) -> None:
        for user in self._repository.list_all():
            print(f"{user.user_id}: {user.name}")

# Example usage
repo = UserRepository()
service = UserService(repo)

service.register_user(1, "Alice")
service.register_user(2, "Bob")

service.show_users() # Output: 1: Alice | 2: Bob
