
"""Event Sourcing / CQRS
Idea: Store changers as events instead of overwriting records. Read model is optimized separately.
"""

# Save event 
EVENTS.apend({"type": "OrderCreated", "order_id": 123, "user_id": 1})

# Rebuild state
def rebuild_order(order_id):
    state = {}
    for event in EVENTS:
        if event["order_id"] == order_id:
            if event["type"] == "OrderCreated":
                state = {"id": order_id, "status": "created"}
            elif event["type"] == "OrderShipped":
                state['status'] = 'shipped'

    return state
