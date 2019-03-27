import aiohttp
import asyncio

urls = ['https://www.douban.com/search?q={}'.format(i) for i in range(10)]


async def fetch(session, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    try:
        async with session.get(url, headers=headers) as response:
            return await response.text()
    except:
        pass


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://douban.com')
        print(html)


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        datas = await asyncio.gather(*[fetch(session, url) for url in urls])
        print(len(datas))
        for data in datas:
            print(data)
        return datas


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all(urls))
