from providers import NotificationService

class UserRegistrationService:
    """
    Business service responsible for registering users.

    Uses a NotificationService to send a welcome message upon successful registration.
    """

    def __init__(self, notifier: NotificationService):
        """
        Initialize the service with a given notification provider.

        Args:
            notifier (NotificationService): The notification service to use (injected).
        """
        self._notifier = notifier

    def register_user(self, name: str, recipient: str) -> None:
        """
        Register a new user and send a welcome notification.

        Args:
            name (str): The name of the user to register.
            recipient (str): The recipient to send the welcome message to.
        """
        print(f"[Service] Registering user: {name}")
        self._notifier.send(f"Welcome, {name}!", recipient)
