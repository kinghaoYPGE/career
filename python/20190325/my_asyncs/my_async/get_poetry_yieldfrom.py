import socket
import datetime
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
from parser_util import parse_args

selector = DefaultSelector()
stopped = False
addresses = list(parse_args())


def connect(sock, address):
    f = Future()
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    def on_connected():
        f.set_result(None)

    selector.register(sock.fileno(), EVENT_WRITE, on_connected)
    yield from f
    selector.unregister(sock.fileno())


def read(sock):
    f = Future()

    def on_readable():
        try:
            f.set_result(sock.recv(1024))
        except ConnectionResetError:
            pass
    selector.register(sock.fileno(), EVENT_READ, on_readable)
    poem = yield from f
    selector.unregister(sock.fileno())
    return poem


def read_all(sock):
    response = []
    poem = yield from read(sock)
    while poem:
        response.append(poem)
        poem = yield from read(sock)
    return b''.join(response)


class Future(object):
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

    def __iter__(self):
        yield self
        return self.result


class Crawler:
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        global stopped
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        yield from connect(sock, self.url)
        get = b'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
        sock.send(get)
        self.response = yield from read_all(sock)
        addresses.remove(self.url)
        if not addresses:
            stopped = True


class Task(object):
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)


def loop():
    """消息事件循环+回调函数"""
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


def main():
    for i, address in enumerate(addresses):
        crawler = Crawler(address)
        Task(crawler.fetch())
    loop()


if __name__ == '__main__':
    elapsed = datetime.timedelta()
    start = datetime.datetime.now()
    main()
    time = datetime.datetime.now() - start
    elapsed += time
    print('done in %s' % elapsed)
