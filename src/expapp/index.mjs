import express from "express";
import os, { hostname } from "os";

const app = express();
const PORT = 3000;
const HOST_NAME = os.hostname();

app.get("/", (_, res) => {
	res.send(`Node Service: ${HOST_NAME}`);
});

app.listen(PORT, () => {
	console.log(`Server started on ${HOST_NAME}`);
});
