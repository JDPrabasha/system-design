import json

from kafka import KafkaConsumer


ORDER_CONFIRMED_KAFKA_TOPIC = 'order_confirmed'

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers='localhost:29092')

total_orders = 0
total_revenue = 0

print("Analytics is listening...")

while True:

    for message in consumer:
        print("Updating analytics")
        order = json.loads(message.value.decode('utf-8'))
        total_orders += 1
        total_revenue += order['total_amount']
        print(f"Total orders today: {total_orders}")
        print(f"Total revenue today: {total_revenue}")
