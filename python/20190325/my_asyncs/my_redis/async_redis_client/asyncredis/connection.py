# -*- coding:utf-8 -*-

import sys
import socket
from tornado.iostream import IOStream
from .exception import ConnectionError
from tornado import gen


PY3 = sys.version > "3"
if PY3:
    CRLF = b"\r\n"
else:
    CRLF = "\r\n"


class Connection(object):
    def __init__(self, host="localhost", port=6379, timeout=None, io_loop=None):
        self.host = host
        self.port = port

        self._io_loop = io_loop
        self._stream = None
        self.in_porcess = False
        self.timeout = timeout
        self._lock = 0
        self.info = {"db": 0, "pass": None}

    def __del__(self):
        self.disconnect()

    # 链接到 redis 服务器, 使用 tornado.iostream.IOStream 进行数据的读写工作
    def connect(self):
        if not self._stream:
            try:
                sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
                sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
                self._stream = IOStream(sock, io_loop=self._io_loop)
                self._stream.set_close_callback(self.on_stream_close)
                self.info["db"] = 0
                self.info["pass"] = None
            except socket.error as e:
                raise ConnectionError(e.message)

    # 当 stream 关闭时，进行的操作
    def on_stream_close(self):
        if self._stream:
            self.disconnect()

    # 关闭链接
    def disconnect(self):
        if self._stream:
            s = self._stream
            self._stream = None
            try:
                if s.socket:
                    s.socket.shutdown(socket.SHUT_RDWR)
                s.close()
            except:
                pass

    # 写数据
    @gen.coroutine
    def write(self, data):
        if not self._stream:
            raise ConnectionError("Try to write to non-exist Connection")
        try:
            if PY3:
                data = bytes(data, encoding="utf-8")
            yield self._stream.write(data)
        except IOError as e:
            self.disconnect()
            raise ConnectionError(e.message)

    # 读数据
    @gen.coroutine
    def read(self, length):
        try:
            if not self._stream:
                self.disconnect()
                raise ConnectionError("Try to read from non-exist Connection")
            data = yield self._stream.read_bytes(length)
            return data
        except IOError as e:
            self.disconnect()
            raise Connection(e.message)

    # 读取一行数据
    @gen.coroutine
    def read_line(self):
        try:
            if not self._stream:
                self.disconnect()
                raise ConnectionError("Try to read from non-exist Connection")
            line = yield self._stream.read_until(CRLF)
            return line
        except IOError as e:
            self.disconnect()
            raise Connection(e.message)

    # 是否已经链接
    def connected(self):
        if self._stream:
            return True
        return False
