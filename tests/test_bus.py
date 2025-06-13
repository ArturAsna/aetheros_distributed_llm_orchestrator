import asyncio
from aetheros.core.event_bus import EventBus

async def test_publish():
    bus = EventBus()
    called = []

    async def handler(data):
        called.append(data)

    bus.subscribe("test", handler)
    await bus.publish("test", {"hello": "world"})
    await asyncio.sleep(0.1)

    assert len(called) == 1

if __name__ == "__main__":
    asyncio.run(test_publish())
