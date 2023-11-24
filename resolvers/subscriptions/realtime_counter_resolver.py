import asyncio
from typing import AsyncGenerator


async def realtime_counter_resolver(target: int = 100) -> AsyncGenerator[int, None]:
    for i in range(target):
        yield i
        await asyncio.sleep(0.5)
