from abc import ABC, abstractmethod

# --- Abstract Notification Interface ---
class NotificationService(ABC):
    """
    Abstract base class that defines the contract for notification senders.
    
    Subclasses must implement the `send` method to send messages via a specific channel.
    """

    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        """
        Send a notification message to a recipient.

        Args:
            message (str): The message content to send.
            recipient (str): The recipient identifier (email address, phone number, etc.).
        """
        pass


# --- Concrete Notification Providers ---
class EmailSender(NotificationService):
    """
    Sends notifications via email.
    """

    def send(self, message: str, recipient: str) -> None:
        """
        Send an email message to the specified recipient.

        Args:
            message (str): The email message content.
            recipient (str): The recipient's email address.
        """
        print(f"[Email] To: {recipient} | Message: {message}")


class SMSSender(NotificationService):
    """
    Sends notifications via SMS.
    """

    def send(self, message: str, recipient: str) -> None:
        """
        Send an SMS message to the specified recipient.

        Args:
            message (str): The SMS message content.
            recipient (str): The recipient's phone number.
        """
        print(f"[SMS] To: {recipient} | Message: {message}")


class PushSender(NotificationService):
    """
    Sends notifications via push notification (e.g., to a mobile device).
    """

    def send(self, message: str, recipient: str) -> None:
        """
        Send a push notification to the specified recipient.

        Args:
            message (str): The push message content.
            recipient (str): The recipient's device identifier.
        """
        print(f"[Push] To: {recipient} | Message: {message}")
