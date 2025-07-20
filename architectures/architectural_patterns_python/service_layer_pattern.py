from typing import Optional

# --- Domain Entity ---
class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

# --- Repository Layer (Persistence) ---
class UserRepository:
    def __init__(self):
        self._users: dict[int, User] = {}
    
    def add(self, user: User) -> None:
        self._users[user.user_id] = user
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Return user or None if not found."""
        return self._users.get(user_id)
    
# --- Service Layer (Business Logic) ---
class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository
    
    def register_user(self, user_id: int, name: str) -> bool:
        """Register a new user if they don't already exist."""
        if self._repository.get_by_id(user_id):
            print(f"[Service] User ID {user_id} already exists.")
            return False
        
        user = User(user_id, name)
        self._repository.add(user)
        print(f"[Service] User '{name}' registered successfully.")
        return True
    
    def get_user_summary(self, user_id: int) -> str:
        """Fetch user info in a business-friendly format."""
        user = self._repository.get_by_id(user_id)
        if not user:
            return "User not found."
        return f"User: {user.name} (ID: {user.user_id})"

# --- Application Logic (e.g., Controller or CLI) ---
repo = UserRepository()
service = UserService(repo)

service.register_user(1, "Alice")
service.register_user(1, "Alice") # Should fail
print(service.get_user_summary(1))
print(service.get_user_summary(42))  # Should return not found.