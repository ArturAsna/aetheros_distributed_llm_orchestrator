from fastapi import FastAPI
import uvicorn

app = FastAPI()

event_bus = None
context = None

@app.post("/event/{event_type}")
async def post_event(event_type: str, data: dict):
    await event_bus.publish(event_type, data)
    return {"status": "published", "event": event_type}

def init(bus, ctx):
    global event_bus, context
    event_bus = bus
    context = ctx

async def start_server(bus, ctx):
    init(bus, ctx)
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()
