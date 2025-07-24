import json
from fastapi import FastAPI, Request
import redis
import uvicorn

app = FastAPI()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.post("/webhook")
async def webhook_listener(request: Request):
    payload = await request.json()
    print("Received webhook payload:", payload)
    r.publish("events", json.dumps(payload))
    return {"status": "success", "message": "Webhook received"}

if __name__ == "__main__":
    uvicorn.run(app, port=8001)