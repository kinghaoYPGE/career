from tornado import httpclient
import time
from tornado import ioloop
import requests
from tornado import gen
import asyncio

N = 3
URL = 'http://localhost:8080'


async def main():
    http_client = httpclient.AsyncHTTPClient()
    return await asyncio.gather(*[http_client.fetch(URL) for i in range(N)])


beg1 = time.time()
ioloop.IOLoop.current().run_sync(main)
print('async', time.time()-beg1)

beg2 = time.time()
for i in range(N):
    requests.get(URL)
print('requests', time.time()-beg2)


