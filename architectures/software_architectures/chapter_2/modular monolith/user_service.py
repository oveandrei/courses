
"""user_service.py"""
from fastapi import APIRouter

# Create the router object
router = APIRouter()

# Create a route for the service
@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Alice"}
