from typing import Optional

# A product class representing a complex object
class User:
    def __init__(self, username: str, email: str, age: Optional[int] = None, address: Optional[str] = None):
        self.username = username
        self.email = email
        self.age = age
        self.address = address

    def __str__(self):
        return f"User(username={self.username}, email={self.email}, age={self.age}, address={self.address})"

# The Builder class
class UserBuilder:
    def __init__(self, username: str, email: str):
        # Requred parameters
        self._username = username
        self._email = email
        # Optional parameters with default None
        self._age = None
        self._address = None

        # Fluent setter methods
    def with_age(self, age: int) -> "UserBuilder":
        self._age = age
        return self # Retun self to allow method chaining
        
    def with_address(self, address: str) -> "UserBuilder":
        self._address = address
        return self
        
    def build(self) -> User:
        # Final step: construct the User object using all gathered data
        return User(
                username = self._username,
                email = self._email,
                age = self._age,
                address = self._address
            )

# Example usage
builder = UserBuilder("johndoe", "john@example.com")
user = builder.with_age(30).with_address("123 Python Street").build()

print(user) # Output: User(username=johndoe, email=john@example.com, age=30, address=123 Python Street)