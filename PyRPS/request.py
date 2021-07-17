import aiohttp


class RPS:
    rps = 0


async def request(url: str, session: aiohttp.ClientSession):
    async with session.get(url):
        RPS.rps += 1