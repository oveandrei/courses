from dataclasses import asdict
import json
import os
import uuid
from typing import Optional, Dict, List
from .models import Product

PRODUCTS_FILE = os.path.join(os.path.dirname(__file__), "products.json")

def load_products() -> Dict[str, Product]:
    """
    Load products from the JSON file.

    Returns:
        Dict[str, Product]: A dictionary mapping product IDs to Product instances.
    """
    if not os.path.exists(PRODUCTS_FILE):
        return {}

    with open(PRODUCTS_FILE, 'r') as f:
        try:
            raw_data = json.load(f)
        except json.JSONDecodeError:
            return {}

    return {pid: Product(**data) for pid, data in raw_data.items()}

def save_products(products: Dict[str, Product]) -> None:
    """
    Save products to the JSON file.

    Args:
        products (Dict[str, Product]): Products to be saved.
    """
    with open(PRODUCTS_FILE, 'w') as f:
        json.dump({pid: asdict(prod) for pid, prod in products.items()}, f, indent=2)

def add_product(name: str, price: float, stock: int) -> bool:
    """
    Add a new product if the name doesn't already exist.

    Args:
        name (str): Product name.
        price (float): Product price.
        stock (int): Initial stock count.

    Returns:
        bool: True if product added successfully, False otherwise.
    """
    products = load_products()

    for product in products.values():
        if product.name.lower() == name.lower():
            print(f"Product with name '{name}' already exists.")
            return False

    product_id = str(uuid.uuid4())
    new_product = Product(product_id=product_id, name=name, price=price, stock=stock)
    products[product_id] = new_product
    save_products(products)
    print(f"Added product: {name} | Price: {price} | Stock: {stock}")
    return True

def list_all_products() -> List[Dict[str, str | float | int]]:
    """
    List all products as dictionaries.

    Returns:
        List[Dict]: List of products with basic fields.
    """
    products = load_products()
    return [
        {
            "id": product_id,
            "name": prod.name,
            "price": prod.price,
            "stock": prod.stock
        }
        for product_id, prod in products.items()
    ]

def search_product_by_name(name: str) -> Optional[Product]:
    """
    Search for a product by name.

    Args:
        name (str): Name to search for.

    Returns:
        Optional[Product]: Product if found, None otherwise.
    """
    products = load_products()
    for prod in products.values():
        if name.lower() == prod.name.lower():
            return prod
    return None

def update_stock(name: str, new_stock: int) -> bool:
    """
    Update the stock of a product by name.

    Args:
        name (str): Product name.
        new_stock (int): New stock quantity.

    Returns:
        bool: True if updated, False otherwise.
    """
    products = load_products()

    for prod in products.values():
        if name.lower() == prod.name.lower():
            if prod.stock != new_stock and new_stock >= 0:
                prod.stock = new_stock
                save_products(products)
                print(f"New stock: {prod.stock} updated for the product name: {name}")
                return True
            else:
                print("The product's stock is the same as the one you entered.")
                return False

    print(f"There was no product matching the name: {name}")
    return False

def update_price(name: str, new_price: float) -> bool:
    """
    Update the price of a product.

    Args:
        name (str): Product name.
        new_price (float): New price.

    Returns:
        bool: True if updated, False otherwise.
    """
    products = load_products()

    for prod in products.values():
        if name.lower() == prod.name.lower():
            if prod.price != new_price and new_price > 0:
                prod.price = new_price
                save_products(products)
                print(f"New price: {prod.price} updated for the product name: {name}")
                return True
            else:
                print("The product's price is the same as the one you entered.")
                return False

    print(f"There was no product matching the name: {name}")
    return False

def update_name(name: str, new_name: str) -> bool:
    """
    Rename a product.

    Args:
        name (str): Current product name.
        new_name (str): New product name.

    Returns:
        bool: True if renamed, False otherwise.
    """
    products = load_products()

    if not new_name.strip():
        print("Name cannot be empty.")
        return False

    for prod in products.values():
        if name.lower() == prod.name.lower():
            if new_name != prod.name:
                prod.name = new_name
                save_products(products)
                print(f"Successfully changed the name to '{new_name}' from the old '{name}'")
                return True
            else:
                print("The product's name is the same as the one you entered.")
                return False

    print(f"There was no product matching the name: {name}")
    return False

def delete_product(name: str) -> bool:
    """
    Delete a product by name.

    Args:
        name (str): Product name.

    Returns:
        bool: True if deleted, False if not found.
    """
    products = load_products()
    to_delete = None

    for product_id, prod in products.items():
        if name.lower() == prod.name.lower():
            to_delete = product_id
            break

    if to_delete:
        del products[to_delete]
        save_products(products)
        print(f"Successfully deleted the product '{name}'.")
        return True

    print(f"There was no product matching the name '{name}'.")
    return False
