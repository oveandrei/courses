from dataclasses import dataclass
from typing import List, Dict

@dataclass
class CartItem:
    """
    Represents an item in a user's shopping cart.

    Attributes:
        product_name (str): Name of the product.
        quantity (int): Quantity of the product added to the cart.
    """
    product_name: str
    quantity: int

@dataclass
class Order:
    """
    Represents a user's order.

    Attributes:
        order_id (str): Unique identifier for the order.
        user_username (str): Username of the user who placed the order.
        items (List[CartItem]): List of items in the order.
        status (str): Current status of the order (e.g., "pending", "completed", "canceled").
    """
    order_id: str
    user_username: str
    items: List[CartItem]
    status: str  # e.g., "pending", "completed", "canceled"

class Cart:
    """
    Manages user-specific shopping carts.

    Attributes:
        carts (Dict[str, List[CartItem]]): Maps usernames to their list of cart items.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to store user carts.
        """
        self.carts: Dict[str, List[CartItem]] = {}

    def add_to_cart(self, user_username: str, product_name: str, quantity: int):
        """
        Adds a product to the user's cart. If the product already exists, it increments the quantity.

        Args:
            user_username (str): The username of the user.
            product_name (str): The name of the product to add.
            quantity (int): The quantity of the product to add.
        """
        if user_username not in self.carts:
            self.carts[user_username] = []

        for item in self.carts[user_username]:
            if item.product_name == product_name:
                item.quantity += quantity
                break
        else:
            self.carts[user_username].append(CartItem(product_name, quantity))

    def get_cart(self, user_username: str) -> List[CartItem]:
        """
        Retrieves the list of items in a user's cart.

        Args:
            user_username (str): The username of the user.

        Returns:
            List[CartItem]: A list of cart items for the user. Empty list if cart not found.
        """
        return self.carts.get(user_username, [])

    def clear_cart(self, user_username: str):
        """
        Empties the user's cart.

        Args:
            user_username (str): The username of the user.
        """
        self.carts[user_username] = []

    def remove_from_cart(self, user_username: str, product_name: str):
        """
        Removes a specific product from the user's cart.

        Args:
            user_username (str): The username of the user.
            product_name (str): The name of the product to remove.
        """
        items = self.carts.get(user_username, [])
        self.carts[user_username] = [item for item in items if item.product_name != product_name]
