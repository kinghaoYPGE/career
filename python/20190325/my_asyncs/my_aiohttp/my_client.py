import asyncio

import aiohttp


async def fetch_single(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, verify_ssl=False) as resp:
            return await resp.text(errors='ignore')


async def fetch(session, id_, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    try:
        async with session.get(url, headers=headers, verify_ssl=False) as resp:
            return await resp.text(), await resp.read()
    except Exception:
        print(f"{id_}, url: {url} error happened:")


async def fetch_all(urls):
    '''
    urls: list[(id_, url)]
    '''
    connector = aiohttp.TCPConnector(limit=60)
    async with aiohttp.ClientSession(connector=connector) as session:
        datas = await asyncio.gather(*[fetch(session, id_, url) for id_, url in urls], return_exceptions=True)
        for ind, data in enumerate(urls):
            id_, url = data
            if isinstance(datas[ind], Exception):
                print(f"{id_}, {url}: ERROR")
        return datas


urls = [(i, f'https://www.baidu.com/?tn={i}') for i in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_all(urls))
loop.close()
