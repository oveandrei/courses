from typing import ClassVar

class User:
    # Class-level storage acting as a mock database
    _db: ClassVar[dict[int, "User"]] = {}
    _id_counter: ClassVar[int] = 1

    def __init__(self, name: str):
        self.id = User._id_counter
        self.name = name
        User._id_counter += 1
    
    def save(self) -> None:
        """Saves the current user instance to the in-memory 'database'."""
        User._db[self.id] = self
        print(f"[DB] Saved : {self}")

    def delete(self) -> None:
        """Deletes the current user instance from the 'database'."""
        if self.id in User._db:
            del User._db[self.id]
            print(f"[DB] Deleted: {self}")
    
    @classmethod
    def find_by_id(cls, user_id: int) -> "User | None":
        """Retrieves a user from the 'database' by ID."""
        return cls._db.get(user_id)
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}')"

# --- Usage ---
# Create and save a user
alice = User("Alice")
alice.save()

# Retrieve a user
found = User.find_by_id(alice.id)
print(f"[Query] Found: {found}")

# Delete the user
alice.delete()

'''Expected Output:
[DB] Saved: User(id=1, name='Alice')
[Query] Found: User(id=1, name='Alice')
[DB] Deleted: User(id=1, name='Alice')'''
