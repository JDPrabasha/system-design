const express = require("express");
const app = express();
const amqp = require("amqplib");

const amqpUrl = "amqp://localhost:5672";

const orderData = {
  customerId: 2,
  orderId: 7,
  number: "ORD-0047",
};

app.get("/", async (req, res) => {
  try {
    const connection = await amqp.connect(amqpUrl);
    const channel = await connection.createChannel();
    await channel.assertQueue("order.shipped");
    channel.sendToQueue(
      "order.shipped",
      Buffer.from(JSON.stringify(orderData))
    );
  } catch (err) {
    console.log(err);
  }
  res.send("ORDERS API");
});

app.listen(8000, () => {
  console.log("ORDERS API listening on port 8000");
});
