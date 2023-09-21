import asyncio
import re
import urllib.error
import urllib.parse
from pprint import pprint

from aiohttp import ClientSession

HREF_RE = re.compile(r'href="(.*?)"')


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs) -> None:
    found = set()
    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except Exception:
        return None
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                # error when parsing URL
                pass
            else:
                found.add(abslink)
        pprint(found)


async def bulk_crawl(urls: set, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(parse(url=url, session=session, **kwargs))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = {
        "https://www.google.com",
        "https://www.python.org",
        "https://www.yahoo.com",
    }

    asyncio.run(bulk_crawl(urls=urls))
