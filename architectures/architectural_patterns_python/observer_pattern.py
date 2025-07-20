from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, data: str) -> None:
        """Receive update from the subjects."""
        pass

# Concrete observer
class EmailSubscriber(Observer):
    def __init__(self, email: str):
        self.email = email
    
    def update(self, data: str) -> None:
        print(f"Email sent to {self.email}: {data}")
   
# Another concrete observer
class SMSSubscriber(Observer):
    def __init__(self, phone: str):
        self.phone = phone
    
    def update(self, data: str) -> None:
        print(f"SMS sent to {self.phone}: {data}")

# Subject class that notifies observers
class NewsPublisher:
    def __init__(self):
        self._observers: list[Observer] = []
    
    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def unsuscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self, news: str) -> None:
        for observer in self._observers:
            observer.update(news)

# Example usage
publisher = NewsPublisher()

email_sub = EmailSubscriber("user@example.com")
sms_sub = SMSSubscriber("+123456789")

publisher.subscribe(email_sub)
publisher.subscribe(sms_sub)

# Notify all subscribers
publisher.notify("New article: Observer Pattern in Python")