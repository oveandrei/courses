from dataclasses import dataclass

@dataclass
class Product:
    """
    Represents a product in the catalog.

    Attributes:
        product_id (str): Unique identifier for the product.
        name (str): Name of the product.
        price (float): Price of the product.
        stock (int): Number of units available in stock.
    """
    product_id: str
    name: str
    price: float
    stock: int
