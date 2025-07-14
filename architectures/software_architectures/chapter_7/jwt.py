
"""Example JWT OAuth2 + JWT"""

# bash -> pip install fastapi[all] python-jose

# Generate token
token = jwt.encode({"sub": "user123"}, "secret", algorithm="HS256")

# Protect route

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, "secret", algorithms=["HS256"])
    return {"user_id": payload["sub"]}

