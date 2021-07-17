import asyncio
import time

import aiohttp

from request import request, RPS
import args


async def main():
    end = time.time() + args.time
    session = aiohttp.ClientSession()

    while end >= time.time():
        await asyncio.wait([request(args.url, session) for _ in range(40)], timeout=end-time.time())
        
    print(
        f"{RPS.rps} RPS in {args.time} seconds",
        f"{RPS.rps // args.time} RPS in second",
        sep="\n"
    )

    await asyncio.sleep(1)
    await session.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())