import json

from kafka import KafkaConsumer, KafkaProducer

ORDER_KAFKA_TOPIC = 'order_details'
ORDER_CONFIRMED_KAFKA_TOPIC = 'order_confirmed'

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC, bootstrap_servers='localhost:29092')

producer = KafkaProducer(bootstrap_servers='localhost:29092')

print("I'm gonna be listening for orders")

while True:
    for message in consumer:
        order = json.loads(message.value.decode('utf-8'))
        print(f"Order {order['order_id']} received")
        print(order)

        user_id = order['user_id']
        total_amount = order['total_amount']
        user_email = f"{user_id}@gmail.com"

        data = {
            'user_id': user_id,
            'user_email': user_email,
            'total_amount': total_amount
        }

        print("Successfully processed order")
        producer.send(ORDER_CONFIRMED_KAFKA_TOPIC,
                      json.dumps(data).encode('utf-8'))
        print(f"Order {order['order_id']} confirmed")
    # producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(order).encode('utf-8'))
    # print(f"Order {order['order_id']} confirmed")
