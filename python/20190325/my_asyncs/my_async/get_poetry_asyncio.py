import asyncio
import datetime
from parser_util import parse_args

addresses = list(parse_args())


async def fetch(url):
    reader, writer = await asyncio.open_connection(host=url[0], port=url[1])
    get = b'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
    writer.write(get)
    response = await reader.read()
    writer.close()
    return response


def main():
    loop = asyncio.get_event_loop()  # 得到事件循环
    tasks = [fetch(address) for address in addresses]
    # loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == '__main__':
    elapsed = datetime.timedelta()
    start = datetime.datetime.now()
    main()
    time = datetime.datetime.now() - start
    elapsed += time
    print('done in %s' % elapsed)
