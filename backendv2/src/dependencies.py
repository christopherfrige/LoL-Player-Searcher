import aiohttp
from aiohttp import ClientSession

async def aiohttp_session(timeout=300) -> ClientSession:
    
    async with ClientSession() as session:
        yield session
