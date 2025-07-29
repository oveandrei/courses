from .models import CartItem, Order, Cart
from typing import Dict
import json
import os
import uuid
from dataclasses import asdict

ORDERS_FILE = os.path.join(os.path.dirname(__file__), "orders.json")


# --- Order Persistence Functions ---

def load_orders() -> Dict[str, Order]:
    """
    Loads all orders from the JSON file into a dictionary.

    Returns:
        Dict[str, Order]: A dictionary mapping order IDs to Order instances.
    """
    if not os.path.exists(ORDERS_FILE):
        return {}
    with open(ORDERS_FILE, 'r') as f:
        try:
            raw_data = json.load(f)
        except json.JSONDecodeError:
            return {}
    return {
        oid: Order(
            order_id=oid,
            user_username=data['user_username'],
            items=[CartItem(**item) for item in data['items']],
            status=data['status']
        )
        for oid, data in raw_data.items()
    }

def save_orders(orders: Dict[str, Order]) -> None:
    """
    Saves the given orders dictionary to the JSON file.

    Args:
        orders (Dict[str, Order]): The dictionary of orders to save.
    """
    with open(ORDERS_FILE, 'w') as f:
        json.dump({oid: asdict(order) for oid, order in orders.items()}, f, indent=2)


# --- Order Operations ---

def add_order(order: Order):
    """
    Adds a new order to storage.

    Args:
        order (Order): The Order object to be added.
    """
    orders = load_orders()
    orders[order.order_id] = order
    save_orders(orders)

def get_order(order_id: str) -> Order | None:
    """
    Retrieves an order by its ID.

    Args:
        order_id (str): The ID of the order to retrieve.

    Returns:
        Order | None: The Order object if found, otherwise None.
    """
    orders = load_orders()
    return orders.get(order_id)

def place_order(user_username: str, cart: Cart) -> Order | None:
    """
    Places an order for the user based on the contents of their cart.

    Args:
        user_username (str): The username of the user placing the order.
        cart (Cart): The Cart instance containing the user's cart items.

    Returns:
        Order | None: The created Order object, or None if the cart is empty.
    """
    user_cart = cart.get_cart(user_username)
    if not user_cart:
        print(f"No items in cart for user: {user_username}")
        return None

    order = Order(
        order_id=str(uuid.uuid4()),
        user_username=user_username,
        items=user_cart.copy(),
        status="pending"
    )

    add_order(order)
    cart.clear_cart(user_username)
    return order

def clear_order(order_id: str):
    """
    Deletes an order by its ID.

    Args:
        order_id (str): The ID of the order to remove.
    """
    orders = load_orders()
    if order_id in orders:
        del orders[order_id]
        save_orders(orders)
