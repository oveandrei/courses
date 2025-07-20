from typing import Optional

# --- Domain Entity ---
class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

# --- Command Side (Write Model) ---
class UserCommandHandler:
    def __init__(self, store: dict[int, User]):
        self._store = store
    
    def create_user(self, user_id: int, name: str) -> bool:
        """Handles user creation command."""
        if user_id in self._store:
            print("[Command] User already exists.")
        
        self._store[user_id] = User(user_id, name)
        print(f"[Command] User '{name}' created.")
        return True
    
    def update_user(self, user_id: int, name: str) -> bool:
        """Handles user update command."""
        user = self._store.get(user_id)
        if not user:
            print("[Command] User not found.")
            return False
        
        user.name = name
        print(f"[Command] User {user_id} updated.")
        return True

# --- Query Side (Read Model) ---
class UserQueryHandler:
    def __init__(self, store: dict[int, User]):
        self._store = store

    def get_user_name(self, user_id: int) -> Optional[str]:
        """Handles read query."""
        user = self._store.get(user_id)
        return user.name if user else None

    def list_users(self) -> list[str]:
        """List all user names."""
        return [user.name for user in self._store.values()]
    
# Example usage
# Shared in-memory store (can be separated in real apps)
data_store: dict[int, User] = {}

# Instantiate command/query handlers
cmd = UserCommandHandler(data_store)
qry = UserQueryHandler(data_store)

cmd.create_user(1, "Alice")
cmd.create_user(2, "Bob")
cmd.create_user(3, "Alice Smith")

print("[Query] All users:", qry.list_users()) # Output: [Query] All users: ['Alice', 'Bob', 'Alice Smith']
print("[Query] User 1:", qry.get_user_name(1)) # Output: [Query] User 1: Alice