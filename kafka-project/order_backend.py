import json
import time

from kafka import KafkaProducer, producer

ORDER_KAFKA_TOPIC = 'order_details'
ORDER_LIMT = 15

producer = KafkaProducer(bootstrap_servers='localhost:29092')

print("Going to be generating order after 5 seconds")
print("Will generate one unique order every 5 seconds")

for i in range(ORDER_LIMT):
    order = {
        'order_id': i,
        'user_id': f'user_{i}',
        'total_amount': i*2,
        'items': "burger, fries, coke"
    }
    producer.send(ORDER_KAFKA_TOPIC, json.dumps(order).encode('utf-8'))
    print(f"Order {i} generated")
    time.sleep(5)
