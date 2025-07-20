from abc import ABC, abstractmethod

# Define an abstract product
class Notification(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        """All notification types must implement this method."""
        pass


# Create concrete products
class EmailNotification(Notification):
    def notify(self, message):
        # Implementation specific to email notification
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def notify(self, message):
        # Implementation specific to SMS notifiation
        print(f"Sending SMS: {message}")


# Now we define the Factory function

def notification_factory(type_: str) -> Notification:
    """
    Factory method to create instances of Notification subclasses
    based on the input type.
    """
    if type_ == "email":
        return EmailNotification()
    elif type_ == "sms":
        return SMSNotification()
    else:
        raise ValueError(f"Unknown notification type: {type_}")

# Use the factory to create instances without knowing their class
notifier = notification_factory("email") # Creates EmailNotification
notifier.notify("Hello, you've got mail!")

notifier2 = notification_factory("sms") # Creates SMSNotification
notifier2.notify("Your OTP is 123456")