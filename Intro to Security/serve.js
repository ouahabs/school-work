const https = require("https");
const fs = require('fs');

const key = fs.readFileSync("./server.key");
const cert = fs.readFileSync("./server.crt");

const express = require ("express") ;
const app = express();

app.get("/", (req, res, next) => {
  res.status(200).send("This website is secure, check in the URL bar");
});

const server = https.createServer({key, cert}, app);

const port = 3000;
server.listen(port, () => {
  console.log(`Server is listening on https://localhost:${port}`);
});