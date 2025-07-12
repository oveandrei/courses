import pika, json

"""Order Service (Publisher)"""
order = {"id": 101, "status": "created"}
channel.basic_publish(exchange='', routing_key="orders", body=json.dumps(order))


"""Notification Service (Consumer)"""
def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"Notify: Order {order['id']} placed!")


    