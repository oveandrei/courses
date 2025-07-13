
"""Saga Pattern
Idea: Each step in a distributed transaction triggers the next; failure triggers compensations
Example: We will orchestrate an Order -> Payment -> Inventory flow
"""

def place_order(order_data):
    order_id = create_order(order_data)

    try:
        process_payment(order_id)
        reserve_inventory(order_id)

    except Exception:
        cancel_order(order_id) # Compensation
        return {"status": "failed"}
    

    return {"status": "success", "order_id": {order_id}}


