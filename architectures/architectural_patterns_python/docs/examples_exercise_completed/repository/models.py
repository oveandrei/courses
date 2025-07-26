from dataclasses import dataclass

@dataclass
class User:
    """
    Data model representing a user in the system.

    Attributes:
        user_id (int): Unique identifier for the user.
        username (str): The username chosen by the user.
        password (str): The user's password (stored as plain text here for simplicity).
                        In a real system, passwords should be securely hashed.
    """
    user_id: int
    username: str
    password: str
