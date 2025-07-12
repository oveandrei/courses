from fastapi import FastAPI

app = FastAPI() # Create the app object

# A simple route where we return the user id specified in the route + Alice
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Alice"}

# Order Service fetching user data:
import requests

# Get the json response from the users route.
user = requests.get("http://user-service:8000/users/123").json()
