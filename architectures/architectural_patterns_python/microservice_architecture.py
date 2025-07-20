# --- User Service ---
class UserService:
    def get_user(self, user_id: int) -> dict:
        """Simulates fetching user data from the User microservice."""
        print(f"[UserService] Getting userr info...")
        return {"id": user_id, "name": "Alice"}

# --- Order Service ---
class OrderService:
    def create_order(self, user_id: int, product: str) -> str:
        """Simulates creating an order in the Order microservice."""
        print(f"[OrderService] Creating order for user {user_id} - Product: {product}")
        return f"Order for {product} created for user {user_id}"

# --- API Gateway or Orchestrator ---
class Orchestrator:
    def __init__(self, user_service: UserService, order_service: OrderService):
        self.user_service = user_service
        self.order_service = order_service
    
    def place_order(self, user_id: int, product: str) -> None:
        """Simulates API gateway or orchestrator coordinating services."""
        user = self.user_service.get_user(user_id)
        if user:
            result = self.order_service.create_order(user_id, product)
            print(f"[Gateway] Success: {result}")
        else:
            print("[Gateway] User not found.")

# --- Simulated Microservices Communication ---
user_service = UserService()
order_service = OrderService()
gateway = Orchestrator(user_service, order_service)

gateway.place_order(1, "Book")
'''Output:
[UserService] Getting userr info...
[OrderService] Creating order for user 1 - Product: Book
[Gateway] Success: Order for Book created for user 1'''