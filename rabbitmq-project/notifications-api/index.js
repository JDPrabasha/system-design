const express = require("express");
const amqp = require("amqplib");

const amqpUrl = "amqp://localhost:5672";

const app = express();

app.get("/", (req, res) => {
  res.send("NOTIFCATIONS API");
});

async function connect() {
  try {
    const connection = await amqp.connect(amqpUrl);
    const channel = await connection.createChannel();
    await channel.assertQueue("order.shipped");
    channel.consume("order.shipped", (data) => {
      const order = JSON.parse(data.content.toString());
      console.log("Order Shipped:", order);
      channel.ack(data);
    });
  } catch (err) {
    console.log(err);
  }
}

connect();

app.listen(8001, () => {
  console.log("Listening on PORT 8001");
});
