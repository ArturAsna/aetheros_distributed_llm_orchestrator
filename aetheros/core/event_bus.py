from collections import defaultdict
import asyncio

class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)

    async def publish(self, event_type, data):
        for callback in self.listeners[event_type]:
            asyncio.create_task(callback(data))
