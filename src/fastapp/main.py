from fastapi import FastAPI
from socket import gethostname
from requests import get


app = FastAPI()
hostname = gethostname()


@app.get("/")
async def index():
    return {"message": f"Python service: {hostname}"}


@app.get("/expapp/")
async def ping_express_app():
    url = "http://expapp:3000/"
    resp = get(url)
    return resp.text
