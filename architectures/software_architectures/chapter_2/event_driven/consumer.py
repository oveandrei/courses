import pika
import json

"""consumer.py"""

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"Send email to {order['user_email']} about order {order['order_id']}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) # Create the connection object
channel = connection.channel() # Create a channel


channel.queue_declare(queue='order_created')
channel.basic_consume(queue='order_created', on_message_callback=callback, auto_ack=True)


print("Waiting for order_created events...")
channel.start_consuming()
