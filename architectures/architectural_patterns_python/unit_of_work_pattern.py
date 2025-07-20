from typing import List, Protocol

# Define a protocol (interface) for operations that can be committed/rolled back
class Command(Protocol):
    def execute(self) -> None:
        ...
    def rollback(self) -> None:
        ...

# --- Unit of Work ---
class UnitOfWork:
    def __init__(self):
        """ Initializes the Unit of Work with empty command and rollback stacks."""
        self._commands: List[Command] = []
    
    def register(self, command: Command) -> None:
        """Adds a new command (operation) to the current unit of work."""
        self._commands.append(command)
    
    def commit(self) -> None:
        """Executs all registered commands. If any command fails, 
        rolls back all previously executed commands"""
        executed = []
        try:
            for cmd in self._commands:
                cmd.execute()
                executed.append(cmd)
        except Exception as e:
            print(f"[UnitOfWork] Error: {e}. Rolling back...")
            for cmd in reversed(executed):
                cmd.rollback()

# --- Example Commands ---
class CreateUserCommand:
    def __init__(self, username: str):
        self.username = username
        self.created = False

    def execute(self) -> None:
        # Simulate DB insert
        print(f"[DB] Creating user: {self.username}")
        self.created = True
        if self.username == "fail":
            raise Exception("Simulated failure")
    
    def rollback(self) -> None:
        if self.created:
            print(f"[DB] Rolling back user: {self.username}")

class SendWelcomeEmailCommand:
    def __init__(self, username: str):
        self.username = username
        self.sent = False
    
    def execute(self) -> None:
        print(f"[Email] Sending welcome email to: {self.username}")
        self.sent = True
    
    def rollback(self) -> None:
        if self.sent:
            print(f"[Email] Recalling welcome email for: {self.username}")

# Usage
uow = UnitOfWork()
uow.register(CreateUserCommand('Alice'))
uow.register(SendWelcomeEmailCommand("Alice"))
uow.commit()
'''Expected Output:
[DB] Creating user: Alice
[Email] Sending welcome email to: Alice'''