import argparse
import asyncio
import time

from request import request

parser = argparse.ArgumentParser()
parser.add_argument('-time', help='Specify how many seconds will be tested', default=5, type=int)
parser.add_argument('-url', help='Specify address', type=str)
args = parser.parse_args()


async def main():
    start = time.time() + args.time
    rps = 0

    while start >= time.time():
        await request(args.url)
        rps += 1

    print("\n".join(
        (f"{rps} RPS in {args.time} seconds",
         f"{rps // args.time} RPS in second")
    ))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
