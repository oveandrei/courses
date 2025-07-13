
"""Strangler Fig

Idea: Route only new functionality to a new service, while leaving the old system untouched
Example: You want to modernize the Order part of a monolithic e-commerce app.
Setup:
API Gateway checks path and routes accordingly
Legacy app still handles old paths
"""

@app.get("/orders/{id}")
def route_to_new_order_service(id):
    return requests.get(f"http://order-service/api/orders/{id}").json()

@app.get("/{path:path}")
def fallback_to_legacy(path):
    return requests.get(f"http://legacy-app/{path}").json()

