
"""Backends for Frontends
Idea: Frontend-specific backends tailor APIs to each client (mobile, web etc)
Example: Mobile needs compressed order data, Web needs full detail
"""

# Web BFF
@app.get("/orders/{id}")
def get_order_web(id: int):
    # returns full object
    return {"id": id, "items": [...], "status": "shipped", "customer": {...}}

# Mobile BFF
@app.get("/orders/{id}")
def get_order_mobile(id: int):
    # returns trimmed object
    order = requests.get(f"http://order-service/orders/{id}").json()
    return {"id": order["id"], "status": order["status"]}
