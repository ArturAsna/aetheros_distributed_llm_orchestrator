import asyncio
from aetheros.core.event_bus import EventBus
from aetheros.core.context import GlobalContext
from aetheros.agents.logger import LoggerAgent
from aetheros.api.server import start_server

async def main():
    bus = EventBus()
    context = GlobalContext()
    LoggerAgent(bus)
    await start_server(bus, context)

if __name__ == "__main__":
    asyncio.run(main())
