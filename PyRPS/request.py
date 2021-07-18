import typing
import time

import aiohttp


class RPS:
    rps = 0


async def request(url: str, session: aiohttp.ClientSession) -> typing.Optional[bool]:
    try:
        async with session.get(url):
            RPS.rps += 1
            return True
        
    except aiohttp.client_exceptions.ClientConnectorError:
        return False
        