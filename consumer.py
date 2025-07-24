import redis
import json


def handle_event(event_data):
    print("Handling event:", event_data)
    
    
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe("events")

print("Listening for events...")

for message in pubsub.listen():
    if message['type'] == 'message':
        try:
            event_data = json.loads(message['data'])
            handle_event(event_data)
        except json.JSONDecodeError:
            print("Received non-JSON message:", message['data'])