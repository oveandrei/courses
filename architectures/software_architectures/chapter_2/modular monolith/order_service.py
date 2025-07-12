
"""order_service.py"""
from fastapi import APIRouter

# Create the router object
router = APIRouter()

# Create a route for the service
@router.get("/orders/{order_id}")
def get_order(order_id: int):
    return {"order_id": order_id, "item": "Book"}
