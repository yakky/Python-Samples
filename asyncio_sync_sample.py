import asyncio
import re
import urllib.error
import urllib.parse
from pprint import pprint

import requests

HREF_RE = re.compile(r'href="(.*?)"')


async def fetch_html(url: str, **kwargs) -> str:
    resp = requests.get(url=url, **kwargs)
    resp.raise_for_status()
    html = resp.text
    return html


async def parse(url: str, **kwargs) -> None:
    found = set()
    try:
        html = await fetch_html(url=url, **kwargs)
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
    tasks = []
    for url in urls:
        tasks.append(parse(url=url, **kwargs))
    await asyncio.gather(*tasks)


def main() -> None:
    urls = {
        "https://www.google.com",
        "https://www.python.org",
        "https://www.yahoo.com",
    }

    asyncio.run(bulk_crawl(urls=urls))
