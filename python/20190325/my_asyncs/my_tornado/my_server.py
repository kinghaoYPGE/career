import tornado.gen
import requests
impor tornado.httpclient
import tornado.ioloop
from tornado import gen
import time

N = 10
URL = 'http://localhost:8888/sleep'

@gen.coroutine
def main():
    http_client = tornado.httpclient.AsyncHTTPClient()
    responses = yield [
        http_client.fetch(URL) for i in range(N)
    ]

beg1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print('async', time.time()-beg1)

beg2 = time.time()
for i in range(N):
    requests.get(URL)
print('req', time.time()-beg2)
