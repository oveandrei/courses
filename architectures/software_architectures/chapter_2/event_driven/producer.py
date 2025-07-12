import pika
import json

"""producer.py"""

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) # Create the connection object
channel = connection.channel() # Create the channel

channel.queue_declare(queue='order_created') # Make a queue

# Create a fake order
order = {"order_id": 123, "user_email": "alice@example.com"}
# Publish the order
channel.basic_publish(
    exchange='',
    routing_key='order_created',
    body=json.dumps(order)
)

# Close connection
print("Order created event sent.")
connection.close()

