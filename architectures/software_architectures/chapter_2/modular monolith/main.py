
"""main.py"""
from fastapi import FastAPI
from order_service import router as order_service
from user_service import router as user_service

# Create an object of the FastAPI server
app = FastAPI()

# Include in the app the 2 services from the modules
app.include_router(user_service.router, prefix="/api")
app.include_router(order_service.router, prefix="/api")
