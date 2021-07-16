import aiohttp


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url):
            pass
