import json

from kafka import KafkaConsumer


ORDER_CONFIRMED_KAFKA_TOPIC = 'order_confirmed'

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers='localhost:29092')


print("I'm gonna be listening for orders")

emails_sent_so_far = set()

print("Email is listening for orders...")

while True:

    for message in consumer:
        order = json.loads(message.value.decode('utf-8'))
        customer_email = order['user_email']
        print(f"Sending email to {customer_email}")
        emails_sent_so_far.add(customer_email)
        print(f"Emails sent so far: {len(emails_sent_so_far)}")
