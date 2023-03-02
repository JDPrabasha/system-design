# Kafka

Kafka is like a big mailbox where people can send messages to each other. Imagine you have a bunch of friends who live in different parts of the world, and you want to send them messages. You can't just send one message to all of them at once, because they might not be online at the same time.

So instead, you put your messages in the mailbox, and your friends can check the mailbox whenever they want to see if there are any new messages. Kafka works the same way - it's a big mailbox where lots of different programs can send and receive messages, called "events". Programs can put events into Kafka and other programs can read those events whenever they want.

Kafka is really good at handling lots of messages at once, even if they're coming from different places. It's also really reliable, so you can be sure that your messages will get to where they're supposed to go. That's why lots of companies use Kafka to send messages between different parts of their software.

## Project System Design

<img width="605" alt="image" src="https://user-images.githubusercontent.com/62155402/222492220-d1c52efc-94b2-4f6e-997a-61cf01b4a999.png">

## How to Run

1. In the kafka-project folder, run `docker-compose up`
2. Run the python files separately in different shells to see how Kafka handles different consumers and producers

## Original Source

This project is based on the wonderful tutorial by **Code with Irtiza**. You can find it at https://www.youtube.com/watch?v=qi7uR3ItaOY
