const axios = require("axios");
const express = require("express");
const redis = require("redis");

const REDIS_PORT = process.env.PORT || 6379;

const client = redis.createClient({
  legacyMode: true,
  PORT: REDIS_PORT,
});
client.connect().catch(console.error);

const app = express();

function setResponse(username, repoCount) {
  return `<h2>${username} has ${repoCount} Github repos</h2>`;
}

async function getRepoCount(req, res) {
  const { username } = req.params;
  const url = `https://api.github.com/users/${username}`;
  const headers = {
    Accept: "application/vnd.github.v3+json",
  };

  try {
    const response = await axios.get(url, { headers });
    const repoCount = response.data.public_repos;
    client.setEx(username, 3600, repoCount);
    res.send(setResponse(username, repoCount));
  } catch (error) {
    res.status(404).json({ message: "User not found" });
  }
}

function cache(req, res, next) {
  const { username } = req.params;
  client.get(username, (err, data) => {
    if (err) throw err;
    if (data !== null) {
      console.log("Retrieved from cache");
      res.send(setResponse(username, data));
    } else {
      next();
    }
  });
}

app.get("/repos/:username", cache, getRepoCount);

app.listen(3000, () => {
  console.log("Server listening on port 3000");
});
