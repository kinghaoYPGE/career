import socket
import datetime
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
from parser_util import parse_args

selector = DefaultSelector()
stopped = False
addresses = list(parse_args())


class Crawler:
    def __init__(self, url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        try:
            self.sock.connect(self.url)
        except BlockingIOError:
            pass
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = b'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
        self.sock.send(get)
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped
        poem = b''  # 诗歌片段
        try:
            poem = self.sock.recv(1024)
        except OSError:
            pass
        if poem:
            self.response += poem
        else:
            selector.unregister(key.fd)
            addresses.remove(self.url)
            if not addresses:
                stopped = True


def loop():
    """消息事件循环+回调函数"""
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)


def main():
    for i, address in enumerate(addresses):
        crawler = Crawler(address)
        crawler.fetch()
    loop()


if __name__ == '__main__':
    elapsed = datetime.timedelta()
    start = datetime.datetime.now()
    main()
    time = datetime.datetime.now() - start
    elapsed += time
    print('done in %s' % elapsed)
