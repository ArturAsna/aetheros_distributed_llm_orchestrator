from rich.console import Console
console = Console()

class LoggerAgent:
    def __init__(self, bus):
        self.bus = bus
        self.bus.subscribe("log", self.on_event)

    async def on_event(self, data):
        console.log(f"[Logger] {data}")
