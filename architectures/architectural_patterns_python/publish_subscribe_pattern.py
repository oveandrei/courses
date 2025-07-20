from collections import defaultdict
from typing import Callable, Any

# --- Event Bus ---
class EventBus:
    def __init__(self):
        """
        Initializes the EventBus.
        _subscribers is a dictionary where each key is an event type (e.g., "order_placed")
        and the value is a list of handler functions subscribed to that event.
        defaultdict(list) ensures new keys are initialized with empty lists automatically.
        """
        self._subscribers: dict[str, list[Callable[[Any], None]]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable[[Any], None]) -> None:
        """
        Subscribes a handler function to a specific event type.
        
        Parameters:
        - event_type (str): The name of the event (e.g., "order_placed").
        - handler (Callable): A function that will be called with event data when the event is published.
        
        This allows multiple subscribers to respond to the same event independently.
        """
        self._subscribers[event_type].append(handler)

    def publish(self, event_type: str, data: Any) -> None:
        """
        Publishes an event to all subscribed handler functions.
        
        Parameters:
        - event_type (str): The name of the event being triggered.
        - data (Any): The data payload associated with the event, passed to each subscriber.

        It loops through all handlers for the given event type and calls each with the event data.
        """
        print(f"[EventBus] Publishing event: {event_type}")
        for handler in self._subscribers[event_type]:
            handler(data)

# --- Subscribers (Event Handlers) ---
def log_event(data):
    """
    A subscriber that logs the entire event data.
    
    Example:
    Input: {"user": "Alice", "item": "Laptop"}
    Output: [Logger] Event received: {'user': 'Alice', 'item': 'Laptop'}
    """
    print(f"[Logger] Event received: {data}")

def notify_user(data):
    """
    A subscriber that simulates notifying a user.

    Example:
    Input: {"user": "Alice", "item": "Laptop"}
    Output: [Notification] Notifying user: Alice
    """
    print(f"[Notification] Notifying user: {data['user']}")

# --- Simulating Pub/Sub Usage ---
# Create an instance of the EventBus
event_bus = EventBus()

# Subscribe both logging and notification handlers to the "order_placed" event
event_bus.subscribe("order_placed", log_event)
event_bus.subscribe("order_placed", notify_user)

# Simulate publishing an event that represents a user placing an order
order_data = {"user": "Alice", "item": "Laptop"}
event_bus.publish("order_placed", order_data)

"""
Expected Output:
[EventBus] Publishing event: order_placed
[Logger] Event received: {'user': 'Alice', 'item': 'Laptop'}
[Notification] Notifying user: Alice

Explanation:
- First, the event is published.
- Then, log_event() prints the entire payload.
- Then, notify_user() prints a message specific to the user.
"""
