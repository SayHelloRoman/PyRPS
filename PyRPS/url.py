import re
import asyncio

import aiohttp

from request import request


class URL:
    @staticmethod
    def correctness(url) -> bool:
        regex = re.compile(
            r"^(?:http|ftp)s?://"
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
            r"(?::\d+)?"
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE
        )

        return re.match(regex, url) is not None


    @staticmethod
    def working_capacity(url) -> bool:
        session = aiohttp.ClientSession()
        loop = asyncio.get_event_loop()
        i = loop.run_until_complete(request(url, session))
        loop.run_until_complete(session.close())

        return i