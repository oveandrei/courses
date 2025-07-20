# --- Service Interface ---
class NotificationService:
    def send(self, recipient: str, message: str) -> None:
        """"Send a message to a recipient."""
        raise NotImplementedError

# --- Concrete Implementation ---
class EmailNotificationService(NotificationService):
    def send(self, recipient: str, message: str) -> None:
        print(f"[Email] To: {recipient} | Message: {message}")

# --- Business Logic (dependent on NotificationService) ---
class UserRegistrationService:
    def __init__(self, notifier: NotificationService):
        """
        The notifier is injected as a dependency.
        We don't care *how* messages are sent.
        """
        self._notifier = notifier
    
    def register_user(self, name: str, email: str) -> None:
        print(f"[Service] Registering user: {name}")
        # Send a welcome notification via the injected notifier
        self._notifier.send(email, f"Welcome, {name}!")

# --- Application Setup (Injection) ---
notifier = EmailNotificationService() # could later swap this with SMS, mock, etc.
registration_service = UserRegistrationService(notifier)

registration_service.register_user("Alice", "alice@example.com")

# 