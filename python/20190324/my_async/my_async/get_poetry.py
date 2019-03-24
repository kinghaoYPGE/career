import datetime
import optparse
import socket
from concurrent import futures
from multiprocessing import Pool
from threading import Thread


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, blocking edition.
Run it like this:

  python get-poetry.py port1 port2 port3 ...

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python blocking-client/get-poetry.py 10001 10002 10003

to grab poetry from servers on ports 10001, 10002, and 10003.

Of course, there need to be servers listening on those ports
for that to work.
"""

    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()

    if not addresses:
        print(parser.format_help())
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)


def blocking_way(address):
    """阻塞方式"""
    """Download a piece of poetry from the given address."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)  # 默认阻塞
    poem = ''
    while True:
        data = sock.recv(1024)  # 默认阻塞
        if not data:
            sock.close()
            break
        poem += str(data)
    return poem


def nonblocking_way(address):
    """非阻塞方式"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass
    request = b'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
    while True:
        try:
            sock.send(request)
            break
        except OSError:
            pass
    poem = ''
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                sock.close()
                break
            poem += str(data)
        except OSError:
            pass
    return poem


def sync_way():
    """同步方式"""
    addresses = parse_args()
    elapsed = datetime.timedelta()
    for i, address in enumerate(addresses):
        addr_fmt = format_address(address)
        print('Task %d: get poetry from: %s' % (i + 1, addr_fmt))
        start = datetime.datetime.now()
        poem = nonblocking_way(address)
        time = datetime.datetime.now() - start
        msg = 'Task %d: got %d bytes of poetry from %s in %s'
        print(msg % (i + 1, len(poem), addr_fmt, time))
        elapsed += time
    print('Got %d poems in %s' % (i+1, elapsed))


def process_way():
    """多进程方式"""
    addresses = parse_args()
    p = Pool(4)
    for i, address in enumerate(addresses):
        p.apply_async(get_poetry, args=(address, ))
    p.close()
    p.join()


def thread_way():
    """多线程方式"""
    addresses = parse_args()
    for i, address in enumerate(addresses):
        t = Thread(target=get_poetry, args=(address, ))
        t.start()
        t.join()


def get_poetry(address):
    print('run task %s' % address[1])
    return blocking_way(address)


def format_address(address):
    host, port = address
    return '%s:%s' % (host or '127.0.0.1', port)


def main():
    sync_way()


if __name__ == '__main__':
    elapsed = datetime.timedelta()
    start = datetime.datetime.now()
    main()
    time = datetime.datetime.now() - start
    elapsed += time
    print('done in %s' % elapsed)
