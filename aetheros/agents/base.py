class BaseAgent:
    def __init__(self, name, bus, context):
        self.name = name
        self.bus = bus
        self.context = context

    async def on_event(self, data):
        raise NotImplementedError

    def register(self, event_type):
        self.bus.subscribe(event_type, self.on_event)
